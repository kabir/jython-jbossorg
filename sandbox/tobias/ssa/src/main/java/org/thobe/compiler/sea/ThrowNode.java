package org.thobe.compiler.sea;

class ThrowNode extends Node {
    private final ExceptionValue exception;

    ThrowNode(ExceptionValue exception) {
        this.exception = exception;
    }

    @Override
    Node accept(GraphTraverser traverser) {
        return traverser.raiseException(this, exception).traverse(traverser);
    }
    
    @Override
    Node traverse(GraphTraverser traverser) {
        return this;
    }

    @Override
    NodeSuccession succession() {
        return NodeSuccession.DUMMY;
    }

    @Override
    public String toString() {
        return "ThrowNode[" + exception + "]";
    }
}
