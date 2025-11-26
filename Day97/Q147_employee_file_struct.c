#include <stdio.h>

// Define Employee structure
struct Employee {
    char name[50];
    int id;
    float salary;
};

int main() {
    struct Employee emp, emp_read;
    FILE *fp;

    // Input employee details
    printf("Enter Employee Name: ");
    scanf("%s", emp.name);

    printf("Enter Employee ID: ");
    scanf("%d", &emp.id);

    printf("Enter Employee Salary: ");
    scanf("%f", &emp.salary);

    // Write to binary file
    fp = fopen("employee.dat", "wb");  // open for writing in binary mode
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fwrite(&emp, sizeof(struct Employee), 1, fp);
    fclose(fp);

    // Read from binary file
    fp = fopen("employee.dat", "rb");  // open for reading in binary mode
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fread(&emp_read, sizeof(struct Employee), 1, fp);
    fclose(fp);

    // Display employee details read from file
    printf("\nEmployee Details Read from File:\n");
    printf("Name: %s | ID: %d | Salary: %.2f\n", emp_read.name, emp_read.id, emp_read.salary);

    return 0;
}