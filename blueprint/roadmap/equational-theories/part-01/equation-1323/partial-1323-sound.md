---
declaration: lemma
origin: cited
---

# Soundness

Let ${\mathcal F}$ be a partial solution. Then if one defines a partial operation $\diamond$ on $M$ by requiring axioms (i), (ii), imposing the additional operations

$$
(\phi_a(b)^n x,a) \diamond (\phi_b(c)^n y,b) = (\phi_c(a)^n z,c)
$$

$$
(\phi_b(c)^n y,b) \diamond (\phi_c(a)^n z,c) = (\phi_a(b)^{n+1} x, a)
$$

$$
(\phi_c(a)^n z,c) \diamond (\phi_a(b)^{n+1} x, a) = (\phi_b(c)^{n+1} y,b)
$$

for all $n \geq 0$ and $(x,y,z,a,b,c) \in {\mathcal F}$, and no other operations, then this is a well-defined partial operation that satisfies axiom (iii) whenever it is defined.

## Depends on

- [Partial solution](partial-1323.md)

## Proof

Routine.

## Sources

- [Equational Theories blueprint: chapter/1323.tex, line 91](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1323.tex#L91)
