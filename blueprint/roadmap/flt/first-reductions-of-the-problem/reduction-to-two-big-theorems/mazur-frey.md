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

This follows from a profound and long result of Mazur \[mazur-torsion\] from 1977, namely the fact that the torsion subgroup of an elliptic curve over $\mathbb{Q}$ can have size at most 16. In fact there is still a little more work which needs to be done to deduce the theorem from Mazur's result. A pre-1990 reference for the full proof of this claim is Proposition 6 in §4.1 of \[serreconj\].

## Lean

Formalized as [`FreyPackage.mazur`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FreyPackage.mazur).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch02reductions.tex, line 172](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch02reductions.tex#L172)
