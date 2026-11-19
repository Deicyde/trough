---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq, TauCeti.SmoothTwoForm.exists_diffeomorph_opens_of_eq_along
statement: formalized
proof: formalized
---

# The relative Moser theorem

Let `σ₀`, `σ₁` be closed two-forms on a boundaryless
second-countable Hausdorff manifold `M` which agree, as bilinear forms on the full tangent spaces of
`M`, at every point of a compact embedded submanifold `f : Q → M`, and let `σ₀` be nondegenerate
along it. Then there is a diffeomorphism `Φ` of `M` which fixes every point of `f(Q)`, moves only
the points of a compact set, and pulls `σ₁` back to `σ₀` on a neighbourhood of `f(Q)`.

```lean
TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq.{u_1, u_2, u_3, u_4,
    u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E] [I.Boundaryless] [T2Space M]
  [SecondCountableTopology M] {E' : Type u_4} {H' : Type u_5} {Q : Type u_6} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  [J.Boundaryless] [TopologicalSpace Q] [ChartedSpace H' Q] [IsManifold J (↑⊤) Q] [CompactSpace Q]
  (f : TauCeti.SmoothEmbedding J I (↑⊤) Q M) {σ₀ σ₁ : TauCeti.SmoothTwoForm I M}
  (h₀ : TauCeti.SmoothForm.IsClosed σ₀) (h₁ : TauCeti.SmoothForm.IsClosed σ₁)
  (hnd : ∀ (q : Q), (TauCeti.SmoothForm.bilinFormAt σ₀ (f q)).Nondegenerate)
  (heq : ∀ (q : Q), ↑σ₁ (f q) = ↑σ₀ (f q)) :
  ∃ Φ,
    (∀ (q : Q), Φ (f q) = f q) ∧
      (∃ C, IsCompact C ∧ ∀ x ∉ C, Φ x = x) ∧
        ∀ᶠ (x : M) in nhdsSet (Set.range ⇑f), ↑((TauCeti.SmoothForm.mpullback ⇑Φ ⋯) σ₁) x = ↑σ₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moser's theorem relative to a compact set, with a given primitive](../part-01/mosers-theorem-relative-to-a-compact-set-with-a.md)
- [The relative Poincaré lemma on a tube](../../manifold/part-04/the-relative-poincare-lemma-on-a-tube.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.html#TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq).

## Other forms

**The relative Moser theorem between neighbourhoods (Cannas da Silva, Theorem 7.4).** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_diffeomorph_opens_of_eq_along`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.html#TauCeti.SmoothTwoForm.exists_diffeomorph_opens_of_eq_along).

```lean
TauCeti.SmoothTwoForm.exists_diffeomorph_opens_of_eq_along.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E] [I.Boundaryless] [T2Space M]
  [SecondCountableTopology M] {E' : Type u_4} {H' : Type u_5} {Q : Type u_6} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  [J.Boundaryless] [TopologicalSpace Q] [ChartedSpace H' Q] [IsManifold J (↑⊤) Q] [CompactSpace Q]
  (f : TauCeti.SmoothEmbedding J I (↑⊤) Q M) {σ₀ σ₁ : TauCeti.SmoothTwoForm I M}
  (h₀ : TauCeti.SmoothForm.IsClosed σ₀) (h₁ : TauCeti.SmoothForm.IsClosed σ₁)
  (hnd : ∀ (q : Q), (TauCeti.SmoothForm.bilinFormAt σ₀ (f q)).Nondegenerate)
  (heq : ∀ (q : Q), ↑σ₁ (f q) = ↑σ₀ (f q)) :
  ∃ U₀ U₁ φ,
    (∀ (q : Q), ∃ (h : f q ∈ U₀), ↑(φ ⟨f q, h⟩) = f q) ∧
      (TauCeti.SmoothForm.mpullback ⇑φ ⋯) ((TauCeti.SmoothForm.mpullback Subtype.val ⋯) σ₁) =
        (TauCeti.SmoothForm.mpullback Subtype.val ⋯) σ₀
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.html#TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq)
- [Source of `TauCeti.SmoothTwoForm.exists_diffeomorph_fix_embedding_eventually_mpullback_eq` in TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/RelativeMoser.lean#L350)
