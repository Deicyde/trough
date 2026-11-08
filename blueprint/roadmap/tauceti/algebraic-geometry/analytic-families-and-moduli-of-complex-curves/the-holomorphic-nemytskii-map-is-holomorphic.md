---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.analyticOnNhd_nemytskii
statement: formalized
proof: formalized
---

# The holomorphic Nemytskii map is holomorphic

If `F` is holomorphic on an open set `U`,
then `u ↦ nemytskii F u` is analytic on the open subset of `H^s`, `s > 1/2`, of elements with
values in `U` (`isOpen_setOf_forall_toContinuousMap_mem`).

```lean
TauCeti.CircleSobolev.analyticOnNhd_nemytskii {s : ℝ} (T : ℝ) [hT : Fact (0 < T)]
  [hs : Fact (1 / 2 < s)] {F : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U) (hF : DifferentiableOn ℂ F U) :
  AnalyticOnNhd ℂ (TauCeti.CircleSobolev.nemytskii F)
    {u | ∀ (x : AddCircle T), ((TauCeti.CircleSobolev.toContinuousMap T ⋯) u) x ∈ U}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for unconditional sums in `ℝ≥0∞`](../../analysis/part-02/other-results/holders-inequality-for-unconditional-sums-in-r0.md)
- [The product estimate in `H^s(A)`, `s > 1/2`](the-product-estimate-in-h-s-a-s-1-2.md)
- [Young's inequality](../../analysis/part-02/normed/part-02/youngs-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.analyticOnNhd_nemytskii`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Nemytskii.html#TauCeti.CircleSobolev.analyticOnNhd_nemytskii).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.analyticOnNhd_nemytskii`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Nemytskii.html#TauCeti.CircleSobolev.analyticOnNhd_nemytskii)
- [Source of `TauCeti.CircleSobolev.analyticOnNhd_nemytskii` in TauCeti/Analysis/Sobolev/Circle/Nemytskii.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Nemytskii.lean#L438)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
