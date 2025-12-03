#include <stdio.h>

// Define structure Student
struct Student {
    char name[50];
    int roll_no;
    int marks;
};

int main() {
    struct Student students[5];  // Array of 5 students
    int i;

    // Read details of 5 students
    for (i = 0; i < 5; i++) {
        printf("Enter details of student %d\n", i + 1);

        printf("Name: ");
        scanf("%s", students[i].name);

        printf("Roll: ");
        scanf("%d", &students[i].roll_no);

        printf("Marks: ");
        scanf("%d", &students[i].marks);
    }

    // Print all student details in tabular format
    printf("\n%-10s | %-6s | %-5s\n", "Name", "Roll", "Marks");
    printf("---------------------------------\n");
    for (i = 0; i < 5; i++) {
        printf("%-10s | %-6d | %-5d\n", students[i].name, students[i].roll_no, students[i].marks);
    }

    return 0;
}