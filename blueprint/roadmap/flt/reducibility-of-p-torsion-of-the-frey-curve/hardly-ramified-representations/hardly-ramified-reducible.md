---
declaration: theorem
origin: cited
lean: FreyCurve.torsion_not_isIrreducible
statement: formalized
---

# hardly_ramified_reducible

If $\ell\geq 3$ is a prime and $\rho:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(\mathbb{Z}/\ell\mathbb{Z})$ is hardly ramified, then $\rho$ is reducible.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [hardly_ramified_lifts](hardly-ramified-lifts.md)
- [hardly_ramified_spreads_out](hardly-ramified-spreads-out.md)
- [hardly_ramified_3adic_reducible](hardly-ramified-3adic-reducible.md)

## Proof

Assume for a contradiction that $\overline{\rho}$ is irreducible. By theorem [hardly_ramified_lifts](hardly-ramified-lifts.md), $\overline{\rho}$ lifts to a hardly ramified $\ell$-adic reprepresentation $\rho$. By theorem [hardly_ramified_spreads_out](hardly-ramified-spreads-out.md), $\rho$ is part of a compatible family of $q$-adic Galois representations. By theorem [hardly_ramified_3adic_reducible](hardly-ramified-3adic-reducible.md), any 3-adic member $\rho_3$ of this family has semisimplification $1\oplus\chi_3$ and in particular for $p\nmid 6$ we have that the characteristic polynomial of $\rho_3(\operatorname{Frob}_p)=(X-p)(X-1).$ By compatibility of the family we deduce that for $p\nmid 6\ell$ the characteristic polynomial of $\rho(\operatorname{Frob}_p)$ is $(X-p)(X-1)$, and thus the characteristic polynomial of $\overline{\rho}(\operatorname{Frob}_p)$ is $(X-p)(X-1)$. By the Cebotarev density theorem, $\overline{\rho}$ and $1\oplus\chi$ have the same characteristic polynomials everywhere (here $\chi$ is the mod $\ell$ cyclotomic character). Thus by the Brauer-Nesbitt theorem, $\overline{\rho}$ is reducible, the contradiction we seek.

## Lean

Stated as [`FreyCurve.torsion_not_isIrreducible`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FreyCurve.torsion_not_isIrreducible); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch03freyreduction.tex, line 128](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch03freyreduction.tex#L128)
