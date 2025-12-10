//Translate the code present in the factorial.py file into a C++ function int factorial(int n).

#include <iostream>
using namespace std;    
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Example usage
    cout << factorial(5) << endl;  // Output: 120
    cout << factorial(0) << endl;  // Output: 1
    return 0;
}