---
declaration: theorem
origin: cited
lean: TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE
statement: formalized
proof: formalized
---

# Hartogs' local removable singularity theorem on complex manifolds

On a boundaryless complex
manifold modelled on `E` with `2 ≤ Module.finrank ℂ E`, any map `f : M → F` into a complete complex
normed space that is holomorphic on a punctured neighbourhood of `p` agrees on a punctured
neighbourhood of `p` with a map `C^ω` at `p`.

```lean
TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℂ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : M → F} {p : M}
  (hf : ∀ᶠ (x : M) in nhdsWithin p {p}ᶜ, MDiffAt f x) :
  ∃ g, ContMDiffAt I (modelWithCornersSelf ℂ F) ⊤ g p ∧ g =ᶠ[nhdsWithin p {p}ᶜ] f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hartogs' local removable singularity theorem](../../../../analysis/part-03/complex/part-02/hartogs-local-removable-singularity-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE)
- [Source of `TauCeti.exists_contMDiffAt_omega_and_eventuallyEq_nhdsNE` in TauCeti/Geometry/Manifold/Complex/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/Hartogs.lean#L79)
