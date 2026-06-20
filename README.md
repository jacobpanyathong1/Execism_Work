# Exercism Solutions

My solutions to [Exercism](https://exercism.org) exercises across several language tracks,
practicing clean, readable, and robust code.

Profile: [@jacobpanyathong1](https://exercism.org/profiles/jacobpanyathong1)

## Tracks

| Track | Exercises |
| --- | --- |
| **Python** | `acronym`, `card-games`, `chaitanas-colossal-coaster`, `hamming`, `hello-world`, `making-the-grade`, `matching-brackets`, `perfect-numbers`, `resistor-color`, `resistor-color-duo` |
| **C++** | `freelancer-rates`, `leap` |
| **C#** | `phone-number-analysis` |
| **JavaScript** | `vehicle-purchase` |

## Layout

```
<track>/<exercise>/        e.g. python/acronym/
```

Each exercise folder holds the solution file(s), the provided test file, and Exercism's
README for that exercise.

## Running the tests

**Python** — from inside an exercise folder:

```bash
python3 -m pytest
```

**C++** — from inside an exercise folder:

```bash
cmake -G "Unix Makefiles" -S . -B build -DEXERCISM_RUN_ALL_TESTS=1
cmake --build build
./build/<exercise>
```
