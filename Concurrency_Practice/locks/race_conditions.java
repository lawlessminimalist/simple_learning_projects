package locks;
import java.util.concurrent.locks.*;


class Soltuion_wk2_1{

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

class ShopperLocked extends Thread{
    static int garlicCount = 0;
    static Lock pencil = new ReentrantLock();

    public void run(){
        pencil.lock();
        for(int i = 0; i<9_000_000;i++){
            garlicCount ++;
        }
        System.out.println("Total number of garlic needed:"+garlicCount);
        pencil.unlock();
    }
}


class ShopperUnlocked extends Thread{
    static int garlicCount = 0;

    public void run(){
        for(int i = 0; i<99_000_000;i++){
            garlicCount++;
        }
        try{
            Thread.sleep(1);
            
        }catch(InterruptedException e){e.printStackTrace();}
        
        System.out.println("Total number of garlic needed:"+garlicCount);


    }
}