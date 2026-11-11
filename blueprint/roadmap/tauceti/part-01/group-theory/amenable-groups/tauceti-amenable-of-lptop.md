---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_lpTop
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_lpTop

A topological group is amenable if, for some left-invariant measure `μ` on its Borel sets,
`L∞(G, μ)` carries a positive linear functional `M` with `M 1 = 1` which is invariant under left
translation.

```lean
TauCeti.Amenable.of_lpTop.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [MeasurableSpace G] [BorelSpace G] {μ : MeasureTheory.Measure G} [μ.IsMulLeftInvariant]
  (M : ↥(MeasureTheory.Lp ℝ ⊤ μ) →ₚ[ℝ] ℝ) (hM : M 1 = 1)
  (h :
    ∀ (g : G) (φ : ↥(MeasureTheory.Lp ℝ ⊤ μ)),
      M (((MeasureTheory.Lp.leftTranslation μ ⊤ ℝ) g) φ) = M φ) :
  TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_lpTop`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Linfty.html#TauCeti.Amenable.of_lpTop).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_lpTop`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Linfty.html#TauCeti.Amenable.of_lpTop)
- [Source of `TauCeti.Amenable.of_lpTop` in TauCeti/GroupTheory/Amenable/Linfty.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/Linfty.lean#L156)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
