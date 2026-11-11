---
declaration: theorem
origin: cited
lean: TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace
statement: formalized
proof: formalized
---

# TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace

Every Cᵏ function on the closed upper half-space admits a constructed global Cᵏ extension.

```lean
TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  (k : ℕ) (f : ℝ × E → F) (hf : ContDiffOn ℝ (↑k) f (TauCeti.HalfSpaceExtension.upperHalfSpace E)) :
  ∃ g, ContDiff ℝ (↑k) g ∧ Set.EqOn g f (TauCeti.HalfSpaceExtension.upperHalfSpace E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trace/Reflection/HalfSpace.html#TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trace/Reflection/HalfSpace.html#TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace)
- [Source of `TauCeti.HalfSpaceExtension.exists_contDiff_extension_halfSpace` in TauCeti/Analysis/Sobolev/Trace/Reflection/HalfSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Trace/Reflection/HalfSpace.lean#L236)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Poincare3D/STATUS.md)
