#include <iostream>

int* bubbleSort(int nums[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                int t = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = t;
            }
        }
    } return nums;
}

int main() {    
    int nums[] = { 6,2,7,9,36,32,76 };
    int size = sizeof(nums) / sizeof(nums[0]);
    std::cout << "INPUT: ";
    for (int i = 0; i < size; i++) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;

    int* sorted = bubbleSort(nums, size);
    std::cout << "SORTED: ";
    for (int i = 0; i < size; i++) {
        std::cout << sorted[i] << " ";
    } std::cout << std::endl;
    return 0;
}