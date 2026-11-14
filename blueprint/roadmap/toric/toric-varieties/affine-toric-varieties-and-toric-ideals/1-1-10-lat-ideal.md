---
declaration: definition
origin: cited
lean: AddMonoidAlgebra.monoidIdeal
statement: formalized
---

# Lattice ideal

Let $R$ be a ring. Let $G$ be a free abelian group and $M$ an affine monoid whose Grothendieck group is $G$. Let $L \le G$ be a sublattice. The *lattice ideal* of $L$ is the $R$-ideal of $R[M]$ defined by

$$
I_L := \langle X^\alpha - X^\beta | \alpha, \beta \in M, \alpha - \beta \in L\rangle.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`AddMonoidAlgebra.monoidIdeal`](https://yaeldillies.github.io/toric/docs/find/#doc/AddMonoidAlgebra.monoidIdeal).

## Sources

- [Toric varieties blueprint: chapters/5-3-toric-ideal.tex, line 11](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/5-3-toric-ideal.tex#L11)
