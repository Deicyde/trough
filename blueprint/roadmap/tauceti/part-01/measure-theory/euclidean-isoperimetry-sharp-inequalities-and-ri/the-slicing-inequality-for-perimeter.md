---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_perimeter_lineSection_le
statement: formalized
proof: formalized
---

# The slicing inequality for perimeter

For a null-measurable set `s` of finite volume and
a unit vector `e`, the perimeters in `ℝ` of the line sections `{t | y + t • e ∈ s}` integrate,
over the orthogonal hyperplane, to at most the perimeter of `s`.

```lean
TauCeti.lintegral_perimeter_lineSection_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {s : Set E}
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) (hfin : MeasureTheory.volume s ≠ ⊤)
  (e : E) (he : ‖e‖ = 1) :
  ∫⁻ (y : ↥(ℝ ∙ e)ᗮ), TauCeti.perimeter MeasureTheory.volume ⊤ {t | ↑y + t • e ∈ s} ≤
    TauCeti.perimeter MeasureTheory.volume ⊤ s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-02/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_perimeter_lineSection_le`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Slicing/Basic.html#TauCeti.lintegral_perimeter_lineSection_le).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_perimeter_lineSection_le`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Slicing/Basic.html#TauCeti.lintegral_perimeter_lineSection_le)
- [Source of `TauCeti.lintegral_perimeter_lineSection_le` in TauCeti/Analysis/BoundedVariation/Slicing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Slicing/Basic.lean#L319)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
