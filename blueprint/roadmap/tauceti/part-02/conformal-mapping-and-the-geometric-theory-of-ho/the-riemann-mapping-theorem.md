---
declaration: theorem
origin: cited
lean: TauCeti.riemannMapping
statement: formalized
proof: formalized
---

# The Riemann mapping theorem

A simply connected open proper subset `Ω` of `ℂ` admits a
holomorphic bijection onto the open unit disc, with nonvanishing derivative throughout `Ω`.

Existence only: the map is not asserted to be unique, and no normalization is imposed.

```lean
TauCeti.riemannMapping {Ω : Set ℂ} (hΩo : IsOpen Ω) (hΩc : IsSimplyConnected Ω)
  (hΩ : Ω ≠ Set.univ) :
  ∃ f, Set.BijOn f Ω (Metric.ball 0 1) ∧ DifferentiableOn ℂ f Ω ∧ ∀ z ∈ Ω, deriv f z ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.riemannMapping`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.riemannMapping).

## Sources

- [Tau Ceti documentation: `TauCeti.riemannMapping`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.html#TauCeti.riemannMapping)
- [Source of `TauCeti.riemannMapping` in TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Existence.lean#L84)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
