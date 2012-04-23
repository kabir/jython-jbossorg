package org.thobe.compiler.sea;

class ReturnNode extends Node {
    private final Value value;

    ReturnNode(Value value) {
        this.value = value;
    }

    @Override
    Node accept(GraphTraverser traverser) {
        return traverser.returnValue(this, value).traverse(traverser);
    }
    
    @Override
    Node traverse(GraphTraverser traverser) {
        return this;
    }

    @Override
    NodeSuccession succession() {
        return NodeSuccession.NOTHING;
    }

    @Override
    public String toString() {
        return "ReturnNode[" + value + "]";
    }
}
