---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.fact_B
statement: formalized
---

# B

For the field $F$ defined in (A), there exists an element $\zeta \in F$ of multiplicative order $p$, that is, $\zeta^p = 1$. Moreover, we have a polynomial decomposition

$$
x^p - 1 = (x - \zeta) (x - \zeta^2) \cdots (x - \zeta^p).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Fermat's little theorem](fermats-little.md)
- [mult_cyclic](mult-cyclic.md)

## Proof

The multiplicative group $F^* = F \setminus \{0\}$ is cyclic of size $q^{p-1} - 1$. Since by Fermat's little theorem $p$ is a divisor of $q^{p-1} - 1$, there exists an element $\zeta \in F$ of order $p$, that is, $\zeta^p = 1$, and $\zeta$ generates the subgroup $\{\zeta, \zeta^2, \dots, \zeta^p = 1\}$ of $F^*$. Note that any $\zeta^i$ ($i \ne p$) is again a generator. Hence we obtain the polynomial decomposition $x^p - 1 = (x - \zeta) (x - \zeta^2) \cdots (x - \zeta^p)$.

## Lean

Stated as [`book.quadratic_reciprocity.fact_B`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.fact_B); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 162](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L162)
