---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.exists_pointNorm_eq_norm
statement: formalized
proof: formalized
---

# Maximum modulus principle for Tate algebras

Every series `f ∈ K⟨X₁, …, Xₙ⟩` attains its
Gauss norm at a classical point: `|f(x)| = ‖f‖` for some maximal ideal `x`.

```lean
TauCeti.MvPowerSeries.exists_pointNorm_eq_norm.{u_1} {K : Type u_1} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {n : ℕ}
  (f : ↥(MvPowerSeries.IsRestricted.subring fun x => 1)) : ∃ x, TauCeti.pointNorm K x f = ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.exists_pointNorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.exists_pointNorm_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.exists_pointNorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.exists_pointNorm_eq_norm)
- [Source of `TauCeti.MvPowerSeries.exists_pointNorm_eq_norm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L75)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
