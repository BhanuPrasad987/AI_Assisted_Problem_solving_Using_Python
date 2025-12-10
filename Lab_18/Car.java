/* Translate the code present incar.py file into a Java class Car with attributes and a methoddisplayDetails(). */
public class Car {
    // Attributes
    private String make;
    private String model;
    private int year;

    // Constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Method to display car details
    public void displayDetails() {
        System.out.println("Car Make: " + make);
        System.out.println("Car Model: " + model);
        System.out.println("Car Year: " + year);
    }

    // Main method for testing
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Camry", 2020);
        myCar.displayDetails();
    }
}