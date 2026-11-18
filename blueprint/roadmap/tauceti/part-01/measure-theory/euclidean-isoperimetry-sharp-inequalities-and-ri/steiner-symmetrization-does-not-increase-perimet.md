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

- [The Morse--Sard theorem](../../analysis/part-01/analytic-heegaard-floer-homology/the-morse-sard-theorem.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.perimeter_steinerSymmetrization_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.html#TauCeti.perimeter_steinerSymmetrization_le).

## Sources

- [Tau Ceti documentation: `TauCeti.perimeter_steinerSymmetrization_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.html#TauCeti.perimeter_steinerSymmetrization_le)
- [Source of `TauCeti.perimeter_steinerSymmetrization_le` in TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Perimeter.lean#L235)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Isoperimetry/STATUS.md)
