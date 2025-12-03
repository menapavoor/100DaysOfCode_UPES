#include <stdio.h>
#include <stdlib.h>


struct Student {
    char name[50];
    int roll;
    int marks;
};

int main() {
  
    struct Student *ptr = (struct Student *)malloc(sizeof(struct Student));

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

   
    sprintf(ptr->name, "John");  
    ptr->roll = 106;
    ptr->marks = 91;

   
    printf("Modified Data: Name: %s | Roll: %d | Marks: %d\n",
           ptr->name, ptr->roll, ptr->marks);

 
    free(ptr);

    return 0;
}