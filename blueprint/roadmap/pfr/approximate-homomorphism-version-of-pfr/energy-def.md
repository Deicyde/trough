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

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 3](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/approx_hom_pfr.tex#L3)
