---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub
statement: formalized
proof: formalized
---

# Moser's theorem relative to a compact set, with a given primitive

Let `σ₀`, `σ₁` be
two-forms on a boundaryless manifold, with `σ₀` closed and `σ₁ - σ₀ = dβ` for a smooth one-form
`β`. Let `K` be a compact set along which `β` vanishes and along which the path
`σ₀ + s (σ₁ - σ₀)`, `s ∈ [0, 1]`, stays nondegenerate. Then there is a diffeomorphism `Φ` of the
manifold which fixes every point of `K`, moves only the points of a compact set, and pulls `σ₁`
back to `σ₀` on a neighbourhood of `K`.

```lean
TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub.{u_1, u_2,
    u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E] [I.Boundaryless] [T2Space M]
  {σ₀ σ₁ : TauCeti.SmoothTwoForm I M} (h₀ : TauCeti.SmoothForm.IsClosed σ₀)
  {β : TauCeti.SmoothForm I M ℝ 1} (hβ : TauCeti.mextDeriv ↑β = ↑(σ₁ - σ₀)) {K : Set M}
  (hK : IsCompact K) (hβK : ∀ x ∈ K, ↑β x = 0)
  (hnd :
    ∀ x ∈ K,
      ∀ s ∈ Set.Icc 0 1, (TauCeti.SmoothForm.bilinFormAt (σ₀ + s • (σ₁ - σ₀)) x).Nondegenerate) :
  ∃ Φ,
    (∀ x ∈ K, Φ x = x) ∧
      (∃ C, IsCompact C ∧ ∀ x ∉ C, Φ x = x) ∧
        ∀ᶠ (x : M) in nhdsSet K, ↑((TauCeti.SmoothForm.mpullback ⇑Φ ⋯) σ₁) x = ↑σ₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../../manifold/part-01/cartans-magic-formula.md)
- [Moser's principle for families of forms](../../manifold/part-03/mosers-principle-for-families-of-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.html#TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.html#TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub)
- [Source of `TauCeti.SmoothTwoForm.exists_diffeomorph_fix_eventually_mpullback_eq_of_mextDeriv_eq_sub` in TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.lean#L291)
