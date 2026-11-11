---
declaration: theorem
origin: cited
lean: TauCeti.perimeter_steinerSymmetrization_le
statement: formalized
proof: formalized
---

# Steiner symmetrization does not increase perimeter

For every null-measurable set `s` of
finite volume and every unit vector `e`, the Steiner symmetral of `s` in direction `e` has
perimeter at most that of `s`. No boundedness or regularity is assumed, and the perimeter of `s`
may be infinite.

```lean
TauCeti.perimeter_steinerSymmetrization_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (e : E)
  (he : ‖e‖ = 1) {s : Set E} (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume)
  (hfin : MeasureTheory.volume s ≠ ⊤) :
  TauCeti.perimeter MeasureTheory.volume ⊤ (TauCeti.steinerSymmetrization e he s) ≤
    TauCeti.perimeter MeasureTheory.volume ⊤ s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse--Sard theorem](../../analysis/part-02/calculus/part-01/the-morse-sard-theorem.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-02/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [TauCeti.Wkp](../../analysis/part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.perimeter_steinerSymmetrization_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.html#TauCeti.perimeter_steinerSymmetrization_le).

## Sources

- [Tau Ceti documentation: `TauCeti.perimeter_steinerSymmetrization_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.html#TauCeti.perimeter_steinerSymmetrization_le)
- [Source of `TauCeti.perimeter_steinerSymmetrization_le` in TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.lean#L235)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
