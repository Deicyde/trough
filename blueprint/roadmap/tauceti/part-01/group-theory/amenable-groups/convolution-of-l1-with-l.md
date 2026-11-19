---
declaration: def
origin: cited
lean: MeasureTheory.Lp.convolutionUCB
statement: formalized
---

# Convolution of `L¹` with `L∞`

For `h ∈ L¹(G, μ)`, the operator
`φ ↦ h ⋆ φ = (x ↦ ∫ y, h y * φ (y⁻¹ * x) ∂μ)` from `L∞(G, μ)` to `UCB G`. Its values are actual
functions, uniformly continuous under small left multiplication; the operator norm is at most
`‖h‖₁` (`MeasureTheory.Lp.norm_convolutionUCB_le`).

```lean
MeasureTheory.Lp.convolutionUCB.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [LocallyCompactSpace G] [MeasurableSpace G] [BorelSpace G]
  {μ : MeasureTheory.Measure G} [μ.IsHaarMeasure] [μ.Regular] (h : ↥(MeasureTheory.Lp ℝ 1 μ)) :
  ↥(MeasureTheory.Lp ℝ ⊤ μ) →L[ℝ] TauCeti.UCB G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.convolutionUCB`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/UCB.html#MeasureTheory.Lp.convolutionUCB).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.convolutionUCB`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/UCB.html#MeasureTheory.Lp.convolutionUCB)
- [Source of `MeasureTheory.Lp.convolutionUCB` in TauCeti/MeasureTheory/Group/Convolution/UCB.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Group/Convolution/UCB.lean#L217)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
