---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.euler_criterion
statement: formalized
---

# Euler's criterion

For $a \not\equiv 0 \pmod{p}$,

$$
(\frac{a}{p}) \equiv a ^{\frac{p-1}{2}} \pmod{p}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Fermat's little theorem](fermats-little.md)

## Proof

From Fermat's little theorem, the polynomial $x^{p-1} - 1 \in \mathbb{Z}_p[x]$ has as roots all nonzero residues. Next we note that

$$
x^{p-1} - 1 = \left(x^{\frac{p-1}{2}} - 1\right)\left(x^{\frac{p-1}{2}} + 1\right).
$$

Suppose $a \equiv b^2 \pmod{p}$ is a quadratic residue. Then by Fermat's little theorem $a^{\frac{p-1}{2}} \equiv b^{p-1} \equiv 1 \pmod{p}$. Hence the quadratic residues are precisely the roots of the first factor $x^{\frac{p-1}{2}} - 1$, and the $\frac{p-1}{2}$ nonresidues must thus be the roots of the second factor $x^{\frac{p-1}{2}} + 1$. Comparing this to the definition of the Legendre symbol, we obtain

$$
(\frac{a}{p}) \equiv a^{\frac{p-1}{2}} \pmod{p}. \qedhere
$$

## Lean

Stated as [`book.quadratic_reciprocity.euler_criterion`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.euler_criterion); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 22](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L22)
