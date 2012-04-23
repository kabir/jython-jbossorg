package org.thobe.compiler.sea;

public abstract class ValueNode extends Node implements Cloneable {
    static ValueNode repeat(final Value value) {
        return value.node;
    }

    private Node next;

    ValueNode() {
        // TODO Auto-generated constructor stub
    }

    final Node traverse(GraphTraverser traverser) {
        // FIXME: implement this
        next.accept(traverser);
        return this;
    }

    @Override
    protected final ValueNode clone() {
        try {
            return (ValueNode) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new LinkageError("ValueNode should be Cloneable.");
        }
    }

    public abstract Value result();

    @Override
    NodeSuccession succession() {
        return new NodeSuccession() {
            @Override
            NodeSuccession setNext(Node node) {
                next = node;
                return node.succession();
            }
        };
    }
}
