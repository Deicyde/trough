---
declaration: definition
origin: cited
lean: ZHat.e
statement: formalized
---

# ZHat.e

The infinite sum $0!+1!+2!+3!+4!+5!+\cdots$ looks like it makes no sense at all; it is the sum of an infinite series of larger and larger positive numbers. However, the sum is *finite* modulo $N$ for every positive integer $N$, because all the terms from $N!$ onwards are multiples of $N$ and thus are zero in $\mathbb{Z}/N\mathbb{Z}$. Thus it makes sense to define $e_N$ to be the value of the finite sum modulo $N$. Explicitly, $e_N=0!+1!+\cdots+(N-1)!$ modulo $N$.

## Depends on

- [ZHat.commRing](zhat-commring.md)

## Lean

Formalized as [`ZHat.e`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ZHat.e).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 139](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L139)
