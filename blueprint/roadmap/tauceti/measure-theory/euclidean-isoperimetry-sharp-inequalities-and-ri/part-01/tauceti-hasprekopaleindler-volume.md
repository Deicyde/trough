---
declaration: theorem
origin: cited
lean: TauCeti.hasPrekopaLeindler_volume
statement: formalized
proof: formalized
---

# TauCeti.hasPrekopaLeindler_volume

The **Prékopa–Leindler inequality** on a finite-dimensional real inner product space, such as
`EuclideanSpace ℝ (Fin n)`: its volume has the Prékopa–Leindler property at every weight
`0 ≤ θ ≤ 1`.

```lean
TauCeti.hasPrekopaLeindler_volume.{u_1} (E : Type u_1) [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {θ : ℝ}
  (hθ₀ : 0 ≤ θ) (hθ₁ : θ ≤ 1) : MeasureTheory.volume.HasPrekopaLeindler θ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prékopa–Leindler inequality for the minimum on `ℝ`](../part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasPrekopaLeindler_volume`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler.html#TauCeti.hasPrekopaLeindler_volume).

## Sources

- [Tau Ceti documentation: `TauCeti.hasPrekopaLeindler_volume`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler.html#TauCeti.hasPrekopaLeindler_volume)
- [Source of `TauCeti.hasPrekopaLeindler_volume` in TauCeti/MeasureTheory/Integral/PrekopaLeindler.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/PrekopaLeindler.lean#L363)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
