---
declaration: theorem
origin: cited
lean: PeriodPair.exists_g₂_g₃_eq
statement: formalized
proof: formalized
---

# The uniformization theorem

for all `a, b ∈ ℂ` with `a³ - 27 b² ≠ 0` there is a lattice `Λ`
with `g₂(Λ) = a` and `g₃(Λ) = b`.

```lean
PeriodPair.exists_g₂_g₃_eq {a b : ℂ} (hab : a ^ 3 - 27 * b ^ 2 ≠ 0) : ∃ L, L.g₂ = a ∧ L.g₃ = b
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A degree-one map is a biholomorphism](../../part-01/fuchsian-groups-and-orbifold-riemann-surfaces/a-degree-one-map-is-a-biholomorphism.md)
- [Descent of an invariant map to the orbit space](../../../geometry/part-01/complex-manifolds-transport-quotients-bundles-an/descent-of-an-invariant-map-to-the-orbit-space.md)
- [The identity theorem for Riemann surfaces](../complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [Rouché's theorem for a disc, classical form](../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../complex/part-03/shimizus-inequality-at-two-cusps.md)
- [Subgroup.CompactifiedQuotient](../../part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.ModularGroup.jBiholomorph](../../part-01/fuchsian-groups-and-orbifold-riemann-surfaces/tauceti-modulargroup-jbiholomorph.md)

## Lean

Formalized in Tau Ceti as [`PeriodPair.exists_g₂_g₃_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.exists_g%E2%82%82_g%E2%82%83_eq).

## Sources

- [Tau Ceti documentation: `PeriodPair.exists_g₂_g₃_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.exists_g%E2%82%82_g%E2%82%83_eq)
- [Source of `PeriodPair.exists_g₂_g₃_eq` in TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean#L124)
