---
declaration: theorem
origin: cited
lean: infinity_of_primes₂
statement: formalized
proof: formalized
---

# Second Proof

Any two Fermat numbers $F_n := 2^{2^n} + 1$ are relatively prime.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let us first look at the Fermat numbers $F_n = 2^{2^n} +1$ for $n = 0,1,2,\dots$. We will show that any two Fermat numbers are relatively prime; hence there must be infinitely many primes. To this end, we verify the recursion

$$
\prod_{k=0}^{n-1} F_k = F_n - 2,
$$

from which our assertion follows immediately. Indeed, if $m$ is a divisor of, say, $F_k$ and $F_n$ (with $k < n$), then $m$ divides 2, and hence $m = 1$ or $2$. But $m = 2$ is impossible since all Fermat numbers are odd. To prove the recursion we use induction on $n$. For $n = 1$, we have $F_0 = 3$ and $F_1 - 2 = 3$. With induction we now conclude

$$
\prod_{k=0}^{n} F_k = \left( \prod_{k=0}^{n-1} F_k \right) F_n =
(F_n - 2)F_n = (2^{2^n} - 1)(2^{2^n} + 1) = 2^{2^{n+1}} - 1 = F_{n+1} - 2.
$$

## Lean

Formalized as [`infinity_of_primes₂`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₂).

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 21](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L21)
