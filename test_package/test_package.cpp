#include <cstdlib>
#include <cstdio>
#include <vector>

#include <linq.h>

int main() {

    std::vector<int> numbers = { 1, 3, 4, 5 };

    auto q = LINQ(from(number, numbers) where(number % 2));

    for (auto x : q) {
         printf("%s score: %i\n", x.first.c_str(), x.second);
    }

    return EXIT_SUCCESS;
}