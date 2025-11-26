#include <stdio.h>

// Define structure Student
struct Student {
    char name[50];
    int roll_no;
    int marks;
};

int main() {
    struct Student students[3];
    int i, topperIndex = 0;

    // Read details of 3 students
    for (i = 0; i < 3; i++) {
        printf("Enter details of student %d\n", i + 1);

        printf("Name: ");
        scanf("%s", students[i].name);

        printf("Roll: ");
        scanf("%d", &students[i].roll_no);

        printf("Marks: ");
        scanf("%d", &students[i].marks);
    }

    // Find student with highest marks
    for (i = 1; i < 3; i++) {
        if (students[i].marks > students[topperIndex].marks) {
            topperIndex = i;
        }
    }

    // Print topper details
    printf("\nTopper: %s (Marks: %d)\n", students[topperIndex].name, students[topperIndex].marks);

    return 0;
}