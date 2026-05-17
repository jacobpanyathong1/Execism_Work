#include <string>

namespace log_line {
    std::string message(std::string line) {
        size_t finder_index = line.find(" ");
        std::string error = line.substr(finder_index + 1);
        return error;
    }

    std::string log_level(std::string line) {
        size_t finder_index = line.find("[");
        size_t end_index = line.find("]");
        std::string error = line.substr(finder_index + 1, end_index - 1);
        return error;
    }

    std::string reformat(std::string line) {
      std::string co_str = log_line::message(line) + " (" + log_line::log_level(line) + ")";
        return co_str;
    }
}
