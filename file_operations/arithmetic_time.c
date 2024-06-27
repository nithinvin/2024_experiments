#include <stdio.h>
#include <time.h>
#include <stdint.h>

#define BILLION 1000000000

int main() {
  
  long long product = 0;
  struct timespec start, end;
  uint64_t time_elapsed_ns;

  clock_gettime(CLOCK_MONOTONIC_RAW, &start);
  product = 49890l * 48909l;
  clock_gettime(CLOCK_MONOTONIC_RAW, &end);
  
  time_elapsed_ns = (end.tv_sec - start.tv_sec) * BILLION;
  time_elapsed_ns += end.tv_nsec - start.tv_nsec;

  printf("Operation: time_elapsed_ns %ld\n", time_elapsed_ns);

  return 0;
}
