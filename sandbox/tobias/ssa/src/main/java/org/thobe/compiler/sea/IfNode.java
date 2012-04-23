package org.thobe.compiler.sea;

final class IfNode extends Node {
    private Node trueSuccessor;
    private Node falseSuccessor;
    private final Value predicate;

    IfNode(Value predicate) {
        this.predicate = predicate;
    }

    void setOnTrue(Node next) {
        trueSuccessor = next;
    }

    void setOnFalse(Node next) {
        falseSuccessor = next;
    }

    @Override
    Node accept(GraphTraverser traverser) {
        // FIXME: this is wrong! successors should be traversed after this node.
        return traverser.selection(this, predicate,
                trueSuccessor.accept(traverser),
                falseSuccessor.accept(traverser)).traverse(traverser);
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
        return "IfNode[" + predicate + " ? " + trueSuccessor + " : "
                + falseSuccessor + "]";
    }
}
