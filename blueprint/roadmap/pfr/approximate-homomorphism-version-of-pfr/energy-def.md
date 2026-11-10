---
declaration: definition
origin: cited
lean: Finset.addEnergy'
statement: formalized
---

# Additive energy

If $G$ is a finite additive group and $A$ is a subset of $G$, the *additive energy* $E(A)$ of $A$ is the normalized count

$$
E(A) := \frac{|\{(a_1,a_2,a_3,a_4) \in A^4 : a_1+a_2 = a_3+a_4\}|}{|G|^3}.
$$

The normalization by $|G|^3$ is the convention of `Finset.addEnergy'`, and every statement in this chapter that mentions $E(A)$ uses it.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Finset.addEnergy'`](https://teorth.github.io/pfr/docs/find/#doc/Finset.addEnergy').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 3](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/approx_hom_pfr.tex#L3)
