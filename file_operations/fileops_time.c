#include <stdio.h>
#include <time.h>
#include <stdint.h>

#define BILLION 1000000000

int main() {
  
  // Replace "myfile.txt" with the actual filename
  struct timespec start, end;
  uint64_t time_elapsed_ns;

  clock_gettime(CLOCK_MONOTONIC_RAW, &start);
  FILE *fp = fopen("myfile.txt", "r");
  clock_gettime(CLOCK_MONOTONIC_RAW, &end);
  
  time_elapsed_ns = (end.tv_sec - start.tv_sec) * BILLION;
  time_elapsed_ns += end.tv_nsec - start.tv_nsec;

  printf("File open: time_elapsed_us %ld\n", time_elapsed_ns/1000);
  if (fp == NULL) {
    printf("Error opening file\n");
    return 1;
  }

  char ch;
  clock_gettime(CLOCK_MONOTONIC_RAW, &start);
  while ((ch = fgetc(fp)) != EOF) {
    printf("%c", ch);
  }
  clock_gettime(CLOCK_MONOTONIC_RAW, &end);
  time_elapsed_ns = (end.tv_sec - start.tv_sec) * BILLION;
  time_elapsed_ns += end.tv_nsec - start.tv_nsec;

  printf("File read: time_elapsed_us %ld\n", time_elapsed_ns/1000);

  fclose(fp);

  return 0;
}
