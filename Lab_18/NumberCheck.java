/*Write a Java method checkNumber(int num) that checks if a number is positive, negative, or zero.*/
public class NumberCheck {
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is a positive number.");
        } else if (num < 0) {
            System.out.println(num + " is a negative number.");
        } else {
            System.out.println("The number is zero.");
        }
    }

    public static void main(String[] args) {
        checkNumber(5);  // Example usage
        checkNumber(-7);  // Example usage
        checkNumber(0);   // Example usage
    }
}