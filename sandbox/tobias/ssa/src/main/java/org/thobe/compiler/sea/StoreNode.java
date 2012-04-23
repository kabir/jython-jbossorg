package org.thobe.compiler.sea;

class StoreNode extends Node {
    private Node next;
    private final Variable variable;
    private final Value value;

    StoreNode(Variable variable, Value value) {
        this.variable = variable;
        this.value = value;
    }

    @Override
    Node accept(GraphTraverser traverser) {
        return traverser.store(this, variable, value).traverse(traverser);
    }
    
    @Override
    Node traverse(GraphTraverser traverser) {
        // FIXME: what about the result from the next-traversal?
        next.accept(traverser);
        return this;
    }

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

    @Override
    public String toString() {
        return "StoreNode[" + variable + " <- " + value + "]";
    }
}
