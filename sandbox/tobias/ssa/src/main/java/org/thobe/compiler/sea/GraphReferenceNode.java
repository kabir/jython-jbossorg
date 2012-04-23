package org.thobe.compiler.sea;

final class GraphReferenceNode extends Node {
    Node start;

    @Override
    Node accept(GraphTraverser traverser) {
        start = start.accept(traverser);
        return start;
    }

    @Override
    Node traverse(GraphTraverser traverser) {
        throw new UnsupportedOperationException(
                "traverse should never be invoked on GraphReferenceNode");
    }

    @Override
    NodeSuccession succession() {
        return new NodeSuccession() {
            @Override
            NodeSuccession setNext(Node node) {
                start = node;
                return node.succession();
            }
        };
    }

    @Override
    public String toString() {
        return start != null ? start.toString() : "NullGraph";
    }
}
