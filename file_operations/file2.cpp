#include <iostream>
#include <fstream>

int main() {
  // Replace "myfile.txt" with the actual filename
  std::ifstream infile("myfile.txt");

  if (!infile.is_open()) {
    std::cerr << "Error opening file\n";
    return 1;
  }

  std::string line;
  while (std::getline(infile, line)) {
    std::cout << line << std::endl;
  }

  infile.close();

  return 0;
}
