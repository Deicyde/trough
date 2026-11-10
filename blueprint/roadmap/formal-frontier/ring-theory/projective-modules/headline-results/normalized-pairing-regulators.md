---
declaration: def
origin: cited
lean: LinearMap.pairingRegulator
statement: formalized
---

# Normalized pairing regulators

For finitely generated abelian groups of equal
integer-module rank and a real-valued integer-bilinear pairing,
[`LinearMap.pairingRegulator`](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Pairing/Regulator/Basic.lean)
is the absolute determinant on independent full frames divided by the product of
their spans' indices in the original groups, including torsion. Frame invariance
and arbitrary-frame evaluation require neither freeness of the original groups
nor nondegeneracy; zero determinants and rank zero are included. Evaluation on
[subgroup bases](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Pairing/Regulator/Subgroup.lean) uses their
whole-group indices, while [lifts of bases modulo torsion](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Pairing/Regulator/Torsion.lean)
use the two torsion cardinalities. At rank zero the regulator is the reciprocal
of the product of the original group cardinalities. The definition and
nonnegativity do not require finite generation; infinite indices are represented
by zero.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results) of [FormalFrontier/projective-modules](https://github.com/FormalFrontier/projective-modules) at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `LinearMap.pairingRegulator` (def), declared in [ProjectiveModules/Pairing/Regulator/Basic.lean, line 64](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Pairing/Regulator/Basic.lean#L64).

Read from the source at commit [27f95a8b](https://github.com/FormalFrontier/projective-modules/tree/27f95a8b2a0669df91bfc703a078030fbf191d75), without running Lean.

## Sources

- [projective-modules at 27f95a8b: README, headline results](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/README.md#headline-results)
- [Source of `LinearMap.pairingRegulator` in ProjectiveModules/Pairing/Regulator/Basic.lean](https://github.com/FormalFrontier/projective-modules/blob/27f95a8b2a0669df91bfc703a078030fbf191d75/ProjectiveModules/Pairing/Regulator/Basic.lean#L64)
