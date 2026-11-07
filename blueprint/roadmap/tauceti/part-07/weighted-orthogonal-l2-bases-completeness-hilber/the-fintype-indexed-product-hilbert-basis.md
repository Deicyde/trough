---
declaration: def
origin: cited
lean: TauCeti.piHilbertBasis
statement: formalized
---

# The `Fintype`-indexed product Hilbert basis

Pointwise products of coordinatewise Hilbert
bases form a Hilbert basis of `L²(Measure.pi μ)`, indexed by the dependent function type.

```lean
TauCeti.piHilbertBasis.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {ι : Type u_2} [Fintype ι]
  {α : ι → Type u_3} [(i : ι) → MeasurableSpace (α i)] {μ : (i : ι) → MeasureTheory.Measure (α i)}
  [∀ (i : ι), MeasureTheory.SigmaFinite (μ i)] [RCLike 𝕜] {κ : ι → Type u_4}
  (b : (i : ι) → HilbertBasis (κ i) 𝕜 ↥(MeasureTheory.Lp 𝕜 2 (μ i))) :
  HilbertBasis ((i : ι) → κ i) 𝕜 ↥(MeasureTheory.Lp 𝕜 2 (MeasureTheory.Measure.pi μ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.piHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/L2/Pi.html#TauCeti.piHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.piHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/L2/Pi.html#TauCeti.piHilbertBasis)
- [Source of `TauCeti.piHilbertBasis` in TauCeti/Analysis/InnerProductSpace/L2/Pi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/L2/Pi.lean#L337)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
