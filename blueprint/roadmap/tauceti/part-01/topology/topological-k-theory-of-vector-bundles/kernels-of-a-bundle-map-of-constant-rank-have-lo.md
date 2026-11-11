---
declaration: theorem
origin: cited
lean: TauCeti.hasLocalSubbundleFrames_ker
statement: formalized
proof: formalized
---

# Kernels of a bundle map of constant rank have local frames

If a continuous bundle map
`φ` between finite-rank vector bundles has rank `r` at every point, then its kernels have
continuous local frames with `finrank F₁ - r` members near every point. Over `ℝ` or `ℂ` they
therefore form a subbundle of `E₁` (`TauCeti.HasLocalSubbundleFrames.vectorBundle`).

```lean
TauCeti.hasLocalSubbundleFrames_ker.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1} {B : Type u_2}
  {F₁ : Type u_3} {F₂ : Type u_4} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [TopologicalSpace B]
  [NormedAddCommGroup F₁] [NormedSpace 𝕜 F₁] [FiniteDimensional 𝕜 F₁] [NormedAddCommGroup F₂]
  [NormedSpace 𝕜 F₂] [FiniteDimensional 𝕜 F₂] {E₁ : B → Type u_5} {E₂ : B → Type u_6}
  [(x : B) → AddCommGroup (E₁ x)] [(x : B) → _root_.Module 𝕜 (E₁ x)]
  [(x : B) → TopologicalSpace (E₁ x)] [TopologicalSpace (Bundle.TotalSpace F₁ E₁)]
  [FiberBundle F₁ E₁] [VectorBundle 𝕜 F₁ E₁] [(x : B) → AddCommGroup (E₂ x)]
  [(x : B) → _root_.Module 𝕜 (E₂ x)] [(x : B) → TopologicalSpace (E₂ x)]
  [TopologicalSpace (Bundle.TotalSpace F₂ E₂)] [FiberBundle F₂ E₂] [VectorBundle 𝕜 F₂ E₂]
  [∀ (x : B), IsTopologicalAddGroup (E₂ x)] [∀ (x : B), ContinuousSMul 𝕜 (E₂ x)]
  {φ : (x : B) → E₁ x →L[𝕜] E₂ x} {r : ℕ} (hφ : Continuous fun x => ⟨x, φ x⟩)
  (hr : ∀ (x : B), Module.finrank 𝕜 ↥(↑(φ x)).range = r) :
  TauCeti.HasLocalSubbundleFrames F₁ (Fin (Module.finrank 𝕜 F₁ - r)) fun x => (↑(φ x)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasLocalSubbundleFrames_ker`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/ConstantRank.html#TauCeti.hasLocalSubbundleFrames_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.hasLocalSubbundleFrames_ker`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/ConstantRank.html#TauCeti.hasLocalSubbundleFrames_ker)
- [Source of `TauCeti.hasLocalSubbundleFrames_ker` in TauCeti/Topology/VectorBundle/ConstantRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/ConstantRank.lean#L70)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
