---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq, TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq_of_isInteriorPoint
statement: formalized
proof: formalized
---

# The point-germ relative Darboux theorem

Let `i : Q → M` be a smooth map between
boundaryless manifolds with injective differential at `p`, and let `σ₀`, `σ₁` be closed two-forms
on `M`, nondegenerate at `i p`, whose pullbacks along `i` agree near `p`. Then some smooth partial
diffeomorphism `Φ` of `M` with `i p` in its source fixes `i q` for every `q` near `p` and pulls
`σ₁` back to `σ₀` on its source.

```lean
TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq.{u_1, u_2, u_3, u_4, u_5,
    u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {E' : Type u_4} {H' : Type u_5} {Q : Type u_6}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [TopologicalSpace Q] [ChartedSpace H' Q] [IsManifold J (↑⊤) Q]
  [BoundarylessManifold I M] [BoundarylessManifold J Q] {σ₀ σ₁ : TauCeti.SmoothTwoForm I M}
  (hσ₀ : TauCeti.SmoothForm.IsClosed σ₀) (hσ₁ : TauCeti.SmoothForm.IsClosed σ₁) {i : Q → M} {p : Q}
  (hi : ∀ᶠ (q : Q) in nhds p, ContMDiffAt J I (↑⊤) i q) (hinj : Function.Injective ⇑(mfderiv% i p))
  (htan : ∀ᶠ (q : Q) in nhds p, TauCeti.mpullback J I i (↑σ₁) q = TauCeti.mpullback J I i (↑σ₀) q)
  (hnd₀ : (TauCeti.SmoothForm.bilinFormAt σ₀ (i p)).Nondegenerate)
  (hnd₁ : (TauCeti.SmoothForm.bilinFormAt σ₁ (i p)).Nondegenerate) :
  ∃ Φ,
    i p ∈ Φ.source ∧
      (∀ᶠ (q : Q) in nhds p, ↑Φ.toPartialEquiv (i q) = i q) ∧
        ∀ x ∈ Φ.source, TauCeti.mpullback I I (↑Φ.toPartialEquiv) (↑σ₁) x = ↑σ₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative Darboux theorem along an immersion](the-relative-darboux-theorem-along-an-immersion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeDarboux.html#TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq).

## Other forms

**The point-germ relative Darboux theorem at interior points.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeDarboux.html#TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq_of_isInteriorPoint).

```lean
TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq_of_isInteriorPoint.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {E' : Type u_4} {H' : Type u_5} {Q : Type u_6}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [TopologicalSpace Q] [ChartedSpace H' Q] [IsManifold J (↑⊤) Q]
  {σ₀ σ₁ : TauCeti.SmoothTwoForm I M} (hσ₀ : TauCeti.SmoothForm.IsClosed σ₀)
  (hσ₁ : TauCeti.SmoothForm.IsClosed σ₁) {i : Q → M} {p : Q} (hp : J.IsInteriorPoint p)
  (hip : I.IsInteriorPoint (i p)) (hi : ∀ᶠ (q : Q) in nhds p, ContMDiffAt J I (↑⊤) i q)
  (hinj : Function.Injective ⇑(mfderiv% i p))
  (htan : ∀ᶠ (q : Q) in nhds p, TauCeti.mpullback J I i (↑σ₁) q = TauCeti.mpullback J I i (↑σ₀) q)
  (hnd₀ : (TauCeti.SmoothForm.bilinFormAt σ₀ (i p)).Nondegenerate)
  (hnd₁ : (TauCeti.SmoothForm.bilinFormAt σ₁ (i p)).Nondegenerate) :
  ∃ Φ,
    i p ∈ Φ.source ∧
      (∀ᶠ (q : Q) in nhds p, ↑Φ.toPartialEquiv (i q) = i q) ∧
        ∀ x ∈ Φ.source, TauCeti.mpullback I I (↑Φ.toPartialEquiv) (↑σ₁) x = ↑σ₀ x
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/RelativeDarboux.html#TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq)
- [Source of `TauCeti.SmoothTwoForm.exists_partialDiffeomorph_fix_immersion_mpullback_eq` in TauCeti/Geometry/Symplectic/Manifold/RelativeDarboux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/RelativeDarboux.lean#L175)
