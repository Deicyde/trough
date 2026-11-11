---
declaration: theorem
origin: cited
lean: MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow
statement: formalized
proof: formalized
---

# The sharp isoperimetric inequality

In a Euclidean space of dimension `n`, every
null-measurable set `s` of finite positive volume satisfies `P(s)^n ≥ n^n ω_n |s|^(n-1)`, where
`ω_n = volume (ball 0 1)` and `P(s)` is the perimeter of `s` in the whole space, finite or
infinite. No boundedness or regularity is assumed, and the case `n = 0` is trivial. Balls attain
equality (`TauCeti.perimeter_ball_pow`).

```lean
MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {s : Set E}
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) (hμs : MeasureTheory.volume s ≠ ⊤)
  (hs0 : MeasureTheory.volume s ≠ 0) :
  ↑(Module.finrank ℝ E) ^ Module.finrank ℝ E * MeasureTheory.volume (Metric.ball 0 1) *
      MeasureTheory.volume s ^ (Module.finrank ℝ E - 1) ≤
    TauCeti.perimeter MeasureTheory.volume ⊤ s ^ Module.finrank ℝ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brunn–Minkowski for a shell](brunn-minkowski-for-a-shell.md)
- [The Morse--Sard theorem](../../analysis/part-02/calculus/part-01/the-morse-sard-theorem.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-02/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Isoperimetric.html#MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow).

## Sources

- [Tau Ceti documentation: `MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Isoperimetric.html#MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow)
- [Source of `MeasureTheory.NullMeasurableSet.finrank_pow_mul_volume_ball_mul_volume_pow_le_perimeter_pow` in TauCeti/Analysis/BoundedVariation/Isoperimetric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Isoperimetric.lean#L335)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
