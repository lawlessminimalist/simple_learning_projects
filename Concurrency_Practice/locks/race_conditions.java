package Concurrency_Practice.locks;

import java.util.concurrent.locks.*;

//An example program that show's how concurrent modules (thread's in this case) can
//cause race conditions where state is incorrectly read/set
class RaceConditions {

    public static void main(String[] args) throws InterruptedException {
        Thread x = new ShopperLocked();
        Thread y = new ShopperLocked();
        Thread xx = new ShopperUnlocked();
        Thread yy = new ShopperUnlocked();
        xx.start();
        yy.start();
        x.start();
        y.start();

    }
}

class ShopperLocked extends Thread {
    static int garlicCount = 0;
    static Lock pencil = new ReentrantLock();

    public void run() {
        pencil.lock();
        for (int i = 0; i < 9_000_000; i++) {
            garlicCount++;
        }
        System.out.println("Locked thread garlic count:" + garlicCount);
        pencil.unlock();
    }
}

class ShopperUnlocked extends Thread {
    static int garlicCount = 0;

    public void run() {
        for (int i = 0; i < 9_000_000; i++) {
            garlicCount++;
        }
        System.out.println("Unlocked thread garlic count:" + garlicCount);
    }
}


