---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.fact_A
statement: formalized
---

# A

Let $p$ and $q$ be distinct odd primes, and consider the finite field $F$ with $q^{p-1}$ elements. Then for any $a, b \in F$, $(a + b)^q = a^q + b^q$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The prime field of $F$ is $\mathbb{Z}_q$, whence $qa = 0$ for any $a \in F$. This implies that $(a + b)^q = a^q + b^q$, since any binomial coefficient $\binom{q}{i}$ is a multiple of $q$ for $0 < i < q$, and thus 0 in $F$.

## Lean

Stated as [`book.quadratic_reciprocity.fact_A`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.fact_A); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 152](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L152)
