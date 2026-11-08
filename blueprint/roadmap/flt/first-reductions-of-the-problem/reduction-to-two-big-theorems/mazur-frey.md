---
declaration: theorem
origin: cited
lean: FreyPackage.mazur
statement: formalized
---

# Mazur

If $\rho$ is the mod $p$ Galois representation associated to a Frey package $(a,b,c,p)$ then $\rho$ is irreducible.

## Depends on

- [Frey](../the-frey-curve/freycurve.md)

## Proof

This follows from a profound and long result of Mazur ([Mazur 1977](http://www.numdam.org/item?id=PMIHES_1977__47__33_0)) from 1977, namely the fact that the torsion subgroup of an elliptic curve over $\mathbb{Q}$ can have size at most 16. In fact there is still a little more work which needs to be done to deduce the theorem from Mazur's result. A pre-1990 reference for the full proof of this claim is Proposition 6 in §4.1 of ([Serre 1987](https://doi.org/10.1215/S0012-7094-87-05413-5)).

## Lean

Stated as [`FreyPackage.mazur`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FreyPackage.mazur); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch02reductions.tex, line 172](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch02reductions.tex#L172)
