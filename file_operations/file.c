#include <stdio.h>

int main() {
  // Replace "myfile.txt" with the actual filename
  FILE *fp = fopen("myfile.txt", "r");

  if (fp == NULL) {
    printf("Error opening file\n");
    return 1;
  }

  char ch;
  while ((ch = fgetc(fp)) != EOF) {
    printf("%c", ch);
  }

  fclose(fp);

  return 0;
}
