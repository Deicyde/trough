---
declaration: theorem
origin: cited
lean: infinity_of_primes₃
statement: formalized
proof: formalized
---

# Third Proof

There is no largest prime.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose $\mathbb{P}$ is finite and $p$ is the largest prime. We consider the so-called *Mersenne number* $2^p - 1$ and show that any prime factor $q$ of $2^p - 1$ is bigger than $p$, which will yield the desired conclusion. Let $q$ be a prime dividing $2^p - 1$, so we have $2^p \equiv 1 \pmod{q}$. Since $p$ is prime, this means that the element 2 has order $p$ in the multiplicative group $\mathbb{Z}_q \setminus \{0\}$ of the field $\mathbb{Z}_q$. This group has $q - 1$ elements. By Lagrange's theorem, we know that the order of every element divides the size of the group, that is, we have $p \mid q - 1$, and hence $p < q$.

## Lean

Formalized as [`infinity_of_primes₃`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₃).

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 48](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L48)
