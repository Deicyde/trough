---
declaration: theorem
origin: cited
lean: FreyCurve.torsion_isHardlyRamified
statement: formalized
---

# Frey_curve_hardly_ramified

The $\ell$-torsion $\rho:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(\mathbb{Z}/\ell\mathbb{Z})$ in the Frey curve associated to a Frey package $(a,b,c,\ell)$ is hardly ramified.

## Depends on

- [hardly_ramified](hardly-ramified.md)

## Proof

This was well-known in the 1980s. A proof sketch is as follows. First note that $\ell\geq5>3$ by definition of a Frey package. Let $\rho$ denote the Galois representation on the $\ell$-torsion of the Frey curve. The fact that $\rho$ is 2-dimensional is Corollary III.6.4(b) of ([Silverman 2009](https://doi.org/10.1007/978-0-387-09494-6)), and the fact that its determinant is cyclotomic is Proposition III.8.3 of the same reference. These results hold for elliptic curves in general. The remaining claims are specific to the Frey curve and lie deeper. The fact that $\rho$ is unramified outside $2\ell$ is a consequence of (4.1.12) and (4.1.13) of ([Serre 1987](https://doi.org/10.1215/S0012-7094-87-05413-5)). The fact that $\rho$ at 2 has an unramified 1-dimensional quotient of order at most 2 follows from the fact that the Frey curve is semistable at 2 (see (4.1.5) of ([Serre 1987](https://doi.org/10.1215/S0012-7094-87-05413-5))) and the theory of the Tate curve. Finally, the claim that $\rho$ is flat at $\ell$ is Proposition 5 and (4.1.13) of ([Serre 1987](https://doi.org/10.1215/S0012-7094-87-05413-5)).

## Lean

Stated as [`FreyCurve.torsion_isHardlyRamified`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FreyCurve.torsion_isHardlyRamified); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch03freyreduction.tex, line 96](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch03freyreduction.tex#L96)
