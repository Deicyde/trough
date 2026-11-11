---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuous_clm_bundle_extension_isInvertible
statement: formalized
proof: formalized
---

# Extending a bundle isomorphism from a closed subset

Over a normal paracompact base, let
`ϕ` be a fibrewise continuous linear map between real or complex vector bundles of finite rank,
continuous as a Hom-bundle section on a closed set `s` and invertible at every point of `s`. Then
`ϕ` agrees on `s` with a continuous Hom-bundle section on the whole base which is invertible on an
open neighbourhood of `s`.

```lean
TauCeti.exists_continuous_clm_bundle_extension_isInvertible.{u, u_1, u_2, u_3, u_4, u_5}
  {𝕜 : Type u_1} [RCLike 𝕜] {B : Type u} [TopologicalSpace B] [NormalSpace B] [ParacompactSpace B]
  {F₁ : Type u_2} {F₂ : Type u_3} [NormedAddCommGroup F₁] [NormedSpace 𝕜 F₁]
  [FiniteDimensional 𝕜 F₁] [NormedAddCommGroup F₂] [NormedSpace 𝕜 F₂] [FiniteDimensional 𝕜 F₂]
  {E₁ : B → Type u_4} {E₂ : B → Type u_5} [(x : B) → AddCommGroup (E₁ x)]
  [(x : B) → _root_.Module 𝕜 (E₁ x)] [(x : B) → TopologicalSpace (E₁ x)]
  [TopologicalSpace (Bundle.TotalSpace F₁ E₁)] [(x : B) → AddCommGroup (E₂ x)]
  [(x : B) → _root_.Module 𝕜 (E₂ x)] [(x : B) → TopologicalSpace (E₂ x)]
  [TopologicalSpace (Bundle.TotalSpace F₂ E₂)] [FiberBundle F₁ E₁] [VectorBundle 𝕜 F₁ E₁]
  [FiberBundle F₂ E₂] [VectorBundle 𝕜 F₂ E₂] [∀ (x : B), IsTopologicalAddGroup (E₂ x)]
  [∀ (x : B), ContinuousSMul 𝕜 (E₂ x)] {s : Set B} (hs : IsClosed s) {ϕ : (x : B) → E₁ x →L[𝕜] E₂ x}
  (hϕ : ContinuousOn (fun x => ⟨x, ϕ x⟩) s) (hinv : ∀ x ∈ s, (ϕ x).IsInvertible) :
  ∃ ψ,
    (Continuous fun x => ⟨x, ψ x⟩) ∧
      (∀ x ∈ s, ψ x = ϕ x) ∧ ∃ U, IsOpen U ∧ s ⊆ U ∧ ∀ x ∈ U, (ψ x).IsInvertible
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuous_clm_bundle_extension_isInvertible`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Extension.html#TauCeti.exists_continuous_clm_bundle_extension_isInvertible).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuous_clm_bundle_extension_isInvertible`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Extension.html#TauCeti.exists_continuous_clm_bundle_extension_isInvertible)
- [Source of `TauCeti.exists_continuous_clm_bundle_extension_isInvertible` in TauCeti/Topology/VectorBundle/Extension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/Extension.lean#L136)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
