---
declaration: def
origin: cited
lean: TauCeti.hilbertBasisOfWeightedMeasure
statement: formalized
---

# The weighted-measure basis

The normalized bare functions, orthonormal by the
orthogonality relation and complete by hypothesis, form a Hilbert basis of `L²(w·μ)` — the textbook
statement that a family of orthogonal functions is an orthonormal basis of its own weighted `L²`
space.

```lean
TauCeti.hilbertBasisOfWeightedMeasure.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜] {α : Type u_2}
  [MeasurableSpace α] (f : ℕ → α → ℝ) (w : α → ℝ) (c : ℕ → ℝ) {μ : MeasureTheory.Measure α}
  (hwnn : ∀ᵐ (x : α) ∂μ, 0 ≤ w x) (hwm : AEMeasurable w μ) (hc : ∀ (n : ℕ), 0 < c n)
  (horth : ∀ (m n : ℕ), ∫ (x : α), f m x * f n x * w x ∂μ = if m = n then c n else 0)
  (hmem :
    ∀ (n : ℕ),
      MeasureTheory.MemLp (fun x => (algebraMap ℝ 𝕜) (f n x / √(c n))) 2
        (μ.withDensity fun x => ENNReal.ofReal (w x)))
  (hcomplete : (Submodule.span 𝕜 (Set.range (TauCeti.bareNormalizedLp f w c hmem)))ᗮ = ⊥) :
  HilbertBasis ℕ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 (μ.withDensity fun x => ENNReal.ofReal (w x)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertBasisOfWeightedMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/WeightedOrthogonalBasis.html#TauCeti.hilbertBasisOfWeightedMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertBasisOfWeightedMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/WeightedOrthogonalBasis.html#TauCeti.hilbertBasisOfWeightedMeasure)
- [Source of `TauCeti.hilbertBasisOfWeightedMeasure` in TauCeti/Analysis/InnerProductSpace/WeightedOrthogonalBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/WeightedOrthogonalBasis.lean#L165)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalL2Bases/STATUS.md)
