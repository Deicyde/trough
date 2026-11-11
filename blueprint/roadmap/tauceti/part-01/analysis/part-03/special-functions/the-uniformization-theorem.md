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

- [The identity theorem for Riemann surfaces](../../part-02/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../part-02/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)
- [Subgroup.CompactifiedQuotient](../../part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.ModularGroup.jBiholomorph](../../part-01/fuchsian-groups-and-orbifold-riemann-surfaces/tauceti-modulargroup-jbiholomorph.md)

## Lean

Formalized in Tau Ceti as [`PeriodPair.exists_g₂_g₃_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.exists_g%E2%82%82_g%E2%82%83_eq).

## Sources

- [Tau Ceti documentation: `PeriodPair.exists_g₂_g₃_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.exists_g%E2%82%82_g%E2%82%83_eq)
- [Source of `PeriodPair.exists_g₂_g₃_eq` in TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean#L229)
