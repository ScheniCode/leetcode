package selection;


public class Selection {


    public static void main(String[] args) {
        int random = getRandom();
        System.out.println(random);
    }

    private static int getRandom() {
        return (int) (100 * Math.random());
    }
}
