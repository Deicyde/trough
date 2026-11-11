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

## Proof depends on

- [Maximum modulus at roots of unity](maximum-modulus-at-roots-of-unity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.exists_pointNorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.exists_pointNorm_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.exists_pointNorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.exists_pointNorm_eq_norm)
- [Source of `TauCeti.MvPowerSeries.exists_pointNorm_eq_norm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L71)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
