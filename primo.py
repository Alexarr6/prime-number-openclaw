#!/usr/bin/env python3
import argparse


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Indica si un número es primo o no")
    parser.add_argument("n", type=int, help="Número entero a evaluar")
    args = parser.parse_args()

    print("primo" if es_primo(args.n) else "no primo")


if __name__ == "__main__":
    main()
