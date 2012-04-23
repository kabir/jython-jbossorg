package org.thobe.compiler.sea.output;

import org.thobe.compiler.sea.output.TestOperation;
import org.thobe.compiler.sea.Graph;
import org.thobe.compiler.sea.GraphBuilder;
import org.thobe.compiler.sea.GraphVisitor;
import org.thobe.compiler.sea.NamespacePopulator;
import org.thobe.compiler.sea.Node;
import org.thobe.compiler.sea.Value;
import org.thobe.compiler.sea.ValueNode;
import org.thobe.compiler.sea.Variable;
import org.thobe.compiler.sea.VariableFactory;

public final class BuildGraph extends GraphBuilder {
    private static abstract class GraphDefinition implements NamespacePopulator {
        abstract void build(BuildGraph builder);

        abstract void verify(Graph graph);
    }

    private BuildGraph(GraphDefinition populator) {
        super(populator);
    }

    private static GraphDefinition[] graphs = { new GraphDefinition() {
        public void populate(VariableFactory factory) {
            factory.createLocalVariable("x");
            factory.createLocalVariable("y");
        }

        @Override
        void build(BuildGraph builder) {
            Variable x = builder.variable("x");
            Variable y = builder.variable("y");
            builder.schedule(builder.storeVariable(x, Value.integer(10)));
            builder.schedule(builder.storeVariable(y, Value.integer(42)));
            ValueNode load_x = builder.loadVariable(x);
            ValueNode load_y = builder.loadVariable(y);
            ValueNode add = builder.schedule(builder.invoke(TestOperation.ADD,
                    load_x.result(), load_y.result()));
            builder.schedule(builder.returnValue(add.result()));
            builder.schedule(builder.invoke(TestOperation.CALL_ME));
        }

        @Override
        void verify(Graph graph) {
            System.out.println("Graph:");
            graph.serialize(new GraphVisitor() {
                public void node(Node node) {
                    System.out.println("  " + node);
                }
            });
        }
    } };

    public static void main(String[] args) {
        for (GraphDefinition graph : graphs) {
            BuildGraph builder = new BuildGraph(graph);
            graph.build(builder);
            graph.verify(builder.build());
        }
    }
}
