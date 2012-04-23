package org.thobe.compiler.sea;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public abstract class GraphBuilder {
    private final GraphReferenceNode entry;
    private NodeSuccession succession;
    private final Map<String, Variable> variables;
    private final Variable[] parameters;

    protected GraphBuilder(NamespacePopulator populator) {
        entry = new GraphReferenceNode();
        succession = entry.succession();
        variables = new HashMap<String, Variable>();
        final List<Variable> parameters = new ArrayList<Variable>();
        populator.populate(new VariableFactory() {
            @Override
            public void createCellVariable(String name) {
                variables.put(name, new CellVariable(name));
            }

            @Override
            public void createLocalVariable(String name) {
                variables.put(name, new LocalVariable(name));
            }

            @Override
            public void createParameter(String name) {
                Variable var = variables.get(name);
                if (var == null) {
                    var = new LocalVariable(name);
                    variables.put(name, var);
                }
                parameters.add(var);
            }
        });
        this.parameters = parameters.toArray(new Variable[parameters.size()]);
    }

    public final Graph build() {
        return new Graph(entry);
    }

    protected ValueNode invoke(InvocationType invocation, Value... arguments) {
        return new InvocationNode(invocation, arguments);
    }

    protected ValueNode array(Value[] content) {
        return new ArrayNode(content);
    }

    protected <N extends Node> N schedule(N node) {
        succession = succession.setNext(node);
        return node;
    }

    protected <V extends Value> V schedule(V value) {
        schedule(ValueNode.repeat(value));
        return value;
    }

    protected NodeSuccession replaceSuccession(NodeSuccession succession) {
        try {
            return this.succession;
        } finally {
            this.succession = succession;
        }
    }

    protected NodeSuccession currentSuccession() {
        return succession;
    }

    protected void nextSuccession(NodeSuccession start) {
        // TODO Auto-generated method stub

    }

    protected NodeSuccession newSuccession() {
        // TODO Auto-generated method stub
        return null;
    }

    protected NodeSuccession merge(final NodeSuccession... previous) {
        return new NodeSuccession() {
            @Override
            NodeSuccession setNext(Node node) {
                for (NodeSuccession prev : previous) {
                    prev.setNext(node);
                }
                return node.succession();
            }
        };
    }

    protected Value phi(Value... values) {
        return new PhiNode(values).result();
    }

    protected Value phiOrNull(Value... values) {
        boolean hasNull = false;
        for (int i = 0; i < values.length; i++) {
            if (values[i] == null) {
                if (hasNull) {
                    continue;
                } else if (i == 0) {
                    hasNull = true;
                } else {
                    throw new IllegalArgumentException(
                            "Either all or no arguments to phiOrNull needs to be null.");
                }
            } else if (hasNull) {
                throw new IllegalArgumentException(
                        "Either all or no arguments to phiOrNull needs to be null.");
            }
        }
        if (hasNull) {
            return null;
        } else {
            return phi(values);
        }
    }

    protected final Node returnValue(Value value) {
        return new ReturnNode(value);
    }

    protected final ValueNode loadVariable(Variable variable) {
        return new LoadNode(variable);
    }

    protected final Node storeVariable(Variable variable, Value value) {
        return new StoreNode(variable, value);
    }

    protected final Value NULL() {
        // TODO Auto-generated method stub
        return null;
    }

    public Node throwException(ExceptionValue exception) {
        return new ThrowNode(exception);
    }

    public Variable variable(String name) {
        return variables.get(name);
    }

    public Variable argument(int index) {
        return parameters[index];
    }
}
