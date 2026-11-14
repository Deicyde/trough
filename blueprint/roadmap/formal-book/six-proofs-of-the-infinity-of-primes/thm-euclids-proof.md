---
declaration: theorem
origin: cited
lean: infinity_of_primes₁
statement: formalized
proof: formalized
---

# Euclid's proof

A finite set $\{p_1, \dots, p_r\}$ cannot be the collection of *all* prime numbers.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For any finite set $\{p_1, \dots, p_r\}$ of primes, consider the number $n = p_1 p_2 \cdots p_r + 1$. This $n$ has a prime divisor $p$. But $p$ is not one of the $p_i$'s: otherwise $p$ would be a divisor of $n$ and of the product $p_1p_2\dots p_r$, and thus also of the difference $n - p_1 p_2 \cdots p_r = 1$, which is impossible. So a finite set $\{p_1, \dots, p_r\}$ cannot be the collection of *all* prime numbers.

## Lean

Formalized as [`infinity_of_primes₁`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₁).

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 3](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L3)
