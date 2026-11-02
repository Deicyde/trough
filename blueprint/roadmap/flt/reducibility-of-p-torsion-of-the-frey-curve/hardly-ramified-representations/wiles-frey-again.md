---
declaration: theorem
origin: cited
lean: FLT.Bosses.B4_proof
statement: formalized
---

# Wiles\_Frey\_again

If $\overline{\rho}$ is the mod $p$ Galois representation associated to a Frey package $(a,b,c,p)$ then $\overline{\rho}$ is reducible.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Frey\_curve\_hardly\_ramified](frey-curve-hardly-ramified.md)
- [hardly\_ramified\_reducible](hardly-ramified-reducible.md)

## Proof

Indeed, $\rho$ is hardly ramified by theorem [Theorem Frey\_curve\_hardly\_ramified](frey-curve-hardly-ramified.md) and thus reducible by theorem [Theorem hardly\_ramified\_reducible](hardly-ramified-reducible.md).

## Lean

Formalized as [`FLT.Bosses.B4_proof`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FLT.Bosses.B4_proof).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch03freyreduction.tex, line 142](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch03freyreduction.tex#L142)
