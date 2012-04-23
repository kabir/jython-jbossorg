package org.thobe.frame;

import org.thobe.frame.Frame.ThreadFrames;

public class Test {
    @Override
    public String toString() {
	return "[test instance]";
    }

    private static void printLocal(Frame frame, int offset) {
	System.out.print("local " + offset);
	System.out.print(" \"" + frame.getName(offset) + "\" (of type "
			 + frame.getSignature(offset) + ") ");
	Object object = frame.getLocal(offset);
	if (!frame.isLocalLive(offset)) {
	    System.out.println("is not live");
	} else if (object == null) {
	    System.out.println("is null");
	} else {
	    try {
		System.out.println("has value = " + object.toString());
	    } catch (NullPointerException ex) {
		System.out.println("is garbage collected");
	    }
	}
    }

    private static void printFrame(Frame frame) {
	if (frame == null) {
	    System.out.println("frame is null");
	    return;
	}
	System.out.println("Inspecting frame for: " + frame.getMethod());
	if (!frame.isNative()) {
	    System.out.println("   instruction: " + frame.getLocation()
			       + ", line number: " +
			       (frame.hasLineNumber() ? frame.getLineNumber()
				: "unknown"));
	}
	System.out.println("this = " + frame.getThis());
	if (!frame.couldLocalsBeLoaded()) {
	    System.out.println("The locals of the frame could not be loaded.");
	} else {
	    int numLocals = frame.getLocalsCount();
	    System.out.println("frame has " + numLocals + " local variables.");
	    for (int i = 0; i < numLocals; i++) {
		printLocal(frame, i);
	    }
	}
    }

    private static void printTraces(ThreadFrames[] traces) {
	for (ThreadFrames trace : traces) {
	    System.out.println("in thread: " + trace.getThread());
	    if (trace.hasStack()) {
		for (int i = 0; i < trace.getStackDepth(); i++) {
		    printFrame(trace.getFrame(i));
		}
	    } else {
		System.out.println("there is no Java stack");
	    }
	}
    }

    public static void main(String[] args) {
	printFrame(Frame.getFrame(0));
	Test test = new Test();
	System.out.println("\nTEST ONE");
	printFrame(test.testOne(1,2,"Hello"));
	System.out.println("\nTEST TWO");
	printFrame(test.testTwo(1,2,"Hello"));
	System.out.println("\nTEST THREE");
	printFrame(test.testThree());
	System.out.println("\nTEST FOUR");
	printFrame(test.testFour());
	System.out.println("\nTEST FIVE");
	test.testFive(1,2,"Hello");
	System.out.println("\nTEST SIX");
	test.testSix(1,2,"Hello");
	System.out.println("\nTEST SEVEN");
	printTraces(Frame.getAllThreadsFrames(100));
    }

    private Frame testOne(int x, int y, Object some) {
	return Frame.getFrame(0);
    }

    private Frame testTwo(int x, int y, Object some) {
	return frame();
    }

    private Frame frame() {
	return Frame.getFrame(1);
    }

    private Frame testThree() {
	return testOne(1,2,"Hello");
    }

    private Frame testFour() {
	return testTwo(1,2,"Hello");
    }

    private void testFive(int x, int y, Object some) {
	for (Frame frame : stack()) {
	    printFrame(frame);
	}
    }

    private Frame[] stack() {
	return Frame.getFrames();
    }

    private void testSix(int x, int y, Object some) {
	printTraces(Frame.getThreadsFrames(100, Thread.currentThread()));
    }
}
