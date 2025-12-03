#include <stdio.h>

// Define Date structure
struct Date {
    int day;
    int month;
    int year;
};

// Define Employee structure with nested Date
struct Employee {
    char name[50];
    int id;
    struct Date joining_date;
};

int main() {
    struct Employee emp;

    // Read employee details
    printf("Enter Name: ");
    scanf("%s", emp.name);

    printf("Enter ID: ");
    scanf("%d", &emp.id);

    printf("Enter Joining Date (dd mm yyyy): ");
    scanf("%d %d %d", &emp.joining_date.day, &emp.joining_date.month, &emp.joining_date.year);

    // Print employee details
    printf("Name: %s | ID: %d | Joining Date: %02d/%02d/%d\n",
           emp.name, emp.id,
           emp.joining_date.day, emp.joining_date.month, emp.joining_date.year);

    return 0;
}