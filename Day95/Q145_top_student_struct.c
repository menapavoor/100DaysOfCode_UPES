#include <stdio.h>

// Define structure Student
struct Student {
    char name[50];
    int roll_no;
    int marks;
};

// Function to find and return the top student
struct Student findTopper(struct Student students[], int n) {
    int i, topperIndex = 0;

    for (i = 1; i < n; i++) {
        if (students[i].marks > students[topperIndex].marks) {
            topperIndex = i;
        }
    }

    return students[topperIndex];  // Return the structure
}

int main() {
    struct Student students[3];
    int i;

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

    // Get the topper
    struct Student topper = findTopper(students, 3);

    // Print topper details
    printf("\nTop Student: %s | Roll: %d | Marks: %d\n", topper.name, topper.roll_no, topper.marks);

    return 0;
}