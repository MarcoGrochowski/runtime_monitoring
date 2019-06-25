import paho.mqtt.client as mqtt
import runtime_monitor.formula as F
import time
import json
from antlr4 import CommonTokenStream, InputStream
from runtime_monitor.grammar.SpecificationLexer import SpecificationLexer
from runtime_monitor.grammar.SpecificationParser import SpecificationParser
from runtime_monitor.ast import AST
from runtime_monitor.rewriter import Rewriter
from runtime_monitor.monitor import Monitor


class Manager(mqtt.Client):
    def __init__(self, cname, **kwargs):
        super(Manager, self).__init__(cname, **kwargs)

        self.monitors = dict()
        self.event_queues = dict()

        self.eps = 0

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        data = json.loads(msg.payload)
        if msg.topic == "runtime_monitor/create":
            self.add_monitor(data['specification'], data['topics'])
        elif msg.topic in self.event_queues:
            self.event_queues[msg.topic].append(data)
        else:
            self.event_queues[msg.topic] = [data]

    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self.connect('broker', 8883, 60)

        example = '{"topics": ["thing/"], "specification": "always property"}'
        data = json.loads(example)
        m.add_monitor(data['specification'], data['topics'])

        rc = 0
        previous_time = time.time()
        for monitor in self.monitors:
            monitor.now = previous_time
        while True:
            rc = self.loop()
            current_time = time.time()
            dt = current_time - previous_time
            previous_time = current_time
            for topic in self.event_queues:
                for event in self.event_queues[topic]:
                    print("New event %s for the topic %s" % (event, topic))
                    timestamp = int(float(event.pop('timestamp', None)))
                    for monitor in self.monitors:
                        if topic in monitor.topics:
                            monitor.step(timestamp=timestamp, state=event)
                            if len(monitor.boolean_verdicts) != 0:
                                print("Boolean verdicts for time-point %d:" % monitor.now)
                                for boolean_verdict in sorted(monitor.boolean_verdicts):
                                    print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                            if len(monitor.equivalence_verdicts) != 0:
                                print("Equivalence verdicts for time-point %d:" % monitor.now)
                                for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                                    print("(%d,%d) = (%d,%d)" % (equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0], equivalence_verdict[1][0][1]))
                    self.event_queues[topic].remove(event)
            # check if monitor went into a timeout
            for monitor in self.monitors:
                if current_time > monitor.now + self.horizon(monitor.formula) + self.eps:
                    start, end = monitor.now, monitor.now + self.horizon(monitor.formula) + self.eps
                    for i in range(int(start), int(end)):
                        monitor.step(i, {})  # empty step semantics
            time.sleep(1.0 - ((current_time - previous_time) % 1))

    def add_monitor(self, specification, topics):
        print("Topics: %s" % topics)
        print("Specification: %s" % specification)
        lexer = SpecificationLexer(InputStream(specification))
        parser = SpecificationParser(CommonTokenStream(lexer))
        ast = AST().visit(parser.specification())
        formula = ast.accept(Rewriter())
        print("Formula: %s" % formula)
        self.monitors[Monitor(formula=formula, topics=topics)] = self.horizon(formula)
        for topic in topics:
            self.subscribe(topic)

    def horizon(self, formula):
        if isinstance(formula, F.Boolean):
            return 0
        elif isinstance(formula, F.Atomic):
            return 0
        elif isinstance(formula, F.Negation):
            return self.horizon(formula.left)
        elif isinstance(formula, F.Until):
            if formula.is_unbounded():
                return self.horizon(formula.right)
            else:
                return formula.right_bound + max(self.horizon(formula.left), self.horizon(formula.right))
        else:
            raise NotImplementedError("Horizon not implemented for F.Formula %s." % formula)


if __name__ == '__main__':
    m = Manager("manager")
    m.run()
