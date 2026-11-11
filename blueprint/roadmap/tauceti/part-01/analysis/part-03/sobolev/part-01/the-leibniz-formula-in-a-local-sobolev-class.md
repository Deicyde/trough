---
declaration: theorem
origin: cited
lean: TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul
statement: formalized
proof: formalized
---

# The Leibniz formula in a local Sobolev class

If `D` is a weak derivative of `u` on the
interior of `U`, both lie in `MemWkpLoc p U k`, and `χ` is `C^n` on an open neighbourhood of `U`
with `k + 1 ≤ n`, then `χ Du + Dχ ⊗ u` is a weak derivative of `χ u` on the interior of `U`,
again in `MemWkpLoc p U k`.

```lean
TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ENNReal} {U : Set ℂ} {Ω : TopologicalSpace.Opens ℂ} {k : ℕ}
  {n : WithTop ℕ∞} {χ : ℂ → ℝ} {u : ℂ → F} {D : ℂ → ℂ →L[ℝ] F} (hu : TauCeti.MemWkpLoc p U k u)
  (hD : TauCeti.HasWeakFDerivOn MeasureTheory.volume (TopologicalSpace.Opens.interior U) u D)
  (hDk : TauCeti.MemWkpLoc p U k D) (hχ : ContDiffOn ℝ n χ ↑Ω) (hk : ↑k + 1 ≤ n) (hU : U ⊆ ↑Ω) :
  (TauCeti.HasWeakFDerivOn MeasureTheory.volume (TopologicalSpace.Opens.interior U)
      (fun z => χ z • u z) fun z => χ z • D z + (fderiv ℝ χ z).smulRight (u z)) ∧
    TauCeti.MemWkpLoc p U k fun z => χ z • D z + (fderiv ℝ χ z).smulRight (u z)
```

## Depends on

- [TauCeti.MemWkpLoc](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-memwkploc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/SmoothCoefficients.html#TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/SmoothCoefficients.html#TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul)
- [Source of `TauCeti.MemWkpLoc.hasWeakFDerivOn_contDiffOn_smul` in TauCeti/Analysis/Sobolev/Local/SmoothCoefficients.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Local/SmoothCoefficients.lean#L120)
