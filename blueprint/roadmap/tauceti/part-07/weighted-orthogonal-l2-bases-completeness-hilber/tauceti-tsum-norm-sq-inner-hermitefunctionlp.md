---
declaration: theorem
origin: cited
lean: TauCeti.tsum_norm_sq_inner_hermiteFunctionLp
statement: formalized
proof: formalized
---

# TauCeti.tsum\_norm\_sq\_inner\_hermiteFunctionLp

**Parseval's identity for the Hermite basis** (norm-square form): the squared Hermite
coordinates of `f` sum to `‖f‖²`.

```lean
TauCeti.tsum_norm_sq_inner_hermiteFunctionLp.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 MeasureTheory.volume)) :
  ∑' (n : ℕ), ‖inner 𝕜 (TauCeti.hermiteFunctionLp 𝕜 n) f‖ ^ 2 = ‖f‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hermite functions are a Hilbert basis of `L²(ℝ)`](the-hermite-functions-are-a-hilbert-basis-of-l2.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)
- [The weight ↔ measure isometry](the-weight-measure-isometry.md)
- [The weighted-measure basis](the-weighted-measure-basis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_inner_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.html#TauCeti.tsum_norm_sq_inner_hermiteFunctionLp).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_norm_sq_inner_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.html#TauCeti.tsum_norm_sq_inner_hermiteFunctionLp)
- [Source of `TauCeti.tsum_norm_sq_inner_hermiteFunctionLp` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.lean#L57)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
