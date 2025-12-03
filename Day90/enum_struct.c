#include <stdio.h>

// Define enum for Gender
enum Gender { MALE, FEMALE };

// Define struct with enum member
struct Person {
    enum Gender gender;
};

int main() {
    // Create a person and assign gender
    struct Person p;
    p.gender = MALE;

    // Print gender
    if (p.gender == MALE) {
        printf("Male\n");
    } else if (p.gender == FEMALE) {
        printf("Female\n");
    }

    return 0;
}