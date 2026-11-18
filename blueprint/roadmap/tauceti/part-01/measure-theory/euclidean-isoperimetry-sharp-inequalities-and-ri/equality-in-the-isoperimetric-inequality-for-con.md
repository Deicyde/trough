---
declaration: theorem
origin: cited
lean: ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall
statement: formalized
proof: formalized
---

# Equality in the isoperimetric inequality for convex bodies

In dimension `n ≥ 1`, a
convex body `K` of positive volume satisfies `P(K)^n = n^n ω_n |K|^(n-1)`, where
`ω_n = volume (ball 0 1)`, exactly when it is a closed ball of positive radius.

```lean
ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (K : ConvexBody E) (hn : Module.finrank ℝ E ≠ 0) (hK : MeasureTheory.volume ↑K ≠ 0) :
  TauCeti.perimeter MeasureTheory.volume ⊤ ↑K ^ Module.finrank ℝ E =
      ↑(Module.finrank ℝ E) ^ Module.finrank ℝ E * MeasureTheory.volume (Metric.ball 0 1) *
        MeasureTheory.volume ↑K ^ (Module.finrank ℝ E - 1) ↔
    ∃ c r, 0 < r ∧ ↑K = Metric.closedBall c r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brunn's concavity principle](brunns-concavity-principle.md)
- [Prékopa–Leindler inequality for the minimum on `ℝ`](../integral/part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Isoperimetric.html#ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall).

## Sources

- [Tau Ceti documentation: `ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Isoperimetric.html#ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall)
- [Source of `ConvexBody.perimeter_pow_eq_iff_exists_eq_closedBall` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Isoperimetric.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Isoperimetric.lean#L133)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Isoperimetry/STATUS.md)
