#include <stdio.h>

float add(float a, float b);
float subtract(float a, float b);
float multiply(float a, float b);
float divide(float a, float b);

int main() {
    float num1, num2, result;
    int choice;

do {
        printf("\nMultiple functions to perform Arithmetic Operations\n");

        printf("Enter first number: ");
        scanf("%f", &num1);

        printf("Enter second number: ");
        scanf("%f", &num2);

        printf("\nChoose operation:\n");
        printf("[1] Addition\n");
        printf("[2] Subtraction\n");
        printf("[3] Multiplication\n");
        printf("[4] Division\n");
        printf("[5] Exit Program\n");
        printf("Enter your choice [1-5]: ");
        scanf("%d", &choice);

    switch (choice) {
            case 1:
                result = add(num1, num2);
                printf("%g + %g = %g\n", num1, num2, result);
                break;

            case 2:
                result = subtract(num1, num2);
                printf("%g - %g = %g\n", num1, num2, result);
                break;

            case 3:
                result = multiply(num1, num2);
                printf("%g * %g = %g\n", num1, num2, result);
                break;

            case 4:
                if (num2 != 0) {
                    result = divide(num1, num2);
                    printf("%g / %g = %g\n", num1, num2, result);
                } else {
                    printf("Error! Invalid choice, Please Try Again!\n");
                }
                break;

            case 5:
                printf("\nExiting Program...\n");
                break;

            default:
                printf("\nInvalid choice, Please Try Again!\n");
        }
    } while (choice != 5);

    return 0;
}

float add(float a, float b) { return a + b; }
float subtract(float a, float b) { return a - b; }
float multiply(float a, float b) { return a * b; }
float divide(float a, float b) { return a / b; }
