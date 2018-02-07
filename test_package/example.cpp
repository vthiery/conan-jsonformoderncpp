#include <iostream>

#include <nlohmann/json.hpp>

using nlohmann::json;

int main()
{
    const json myJson = {
        { "Hello", "World" }
    };

    for (auto it{ myJson.cbegin() }; it != myJson.cend(); ++it)
    {
        std::cout << it.key() << " " << it.value() << std::endl;
    }
}
