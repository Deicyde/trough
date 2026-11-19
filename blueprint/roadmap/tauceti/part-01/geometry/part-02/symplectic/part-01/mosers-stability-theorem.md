---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq, TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq_of_isCompact
statement: formalized
proof: formalized
---

# Moser's stability theorem

Let `σ` be a smooth two-form on `ℝ × M`, for a compact
boundaryless manifold `M`, whose slices `σ_t = ι_t^* σ` are symplectic, and let `α` be a smooth
one-form on `ℝ × M` whose slices are primitives of the velocity, `ι_t^* L_{∂_t} σ = dα_t`. Then
there is an isotopy `ψ_t` of `M`, jointly smooth in `(t, x)`, with `ψ_0 = id` and
`ψ_t^* σ_t = σ_0` for every `t`, which fixes every point at which `α_t` vanishes for all `t`.

```lean
TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [I.Boundaryless] [T2Space M] [CompactSpace M]
  (σ : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 2)
  (α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1)
  (hσ :
    ∀ (t : ℝ), TauCeti.SmoothTwoForm.IsSymplectic ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ))
  (hα :
    ∀ (t : ℝ),
      TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t)
          (TauCeti.mlieDerivForm (fun x => (1, 0)) ↑σ) =
        TauCeti.mextDeriv ↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) :
  ∃ ψ,
    (ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) I ↑⊤ fun p => (ψ p.1) p.2) ∧
      (∀ (x : M), (ψ 0) x = x) ∧
        (∀ (t : ℝ) (x : M),
            (∀ (u : ℝ), ↑((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α) x = 0) → (ψ t) x = x) ∧
          ∀ (t : ℝ),
            (TauCeti.SmoothForm.mpullback ⇑(ψ t) ⋯)
                ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ) =
              (TauCeti.SmoothForm.mpullback (Prod.mk 0) ⋯) σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moser's isotopy lemma](mosers-isotopy-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Moser.html#TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq).

## Other forms

**Moser's stability theorem, with support control.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Moser.html#TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq_of_isCompact).

```lean
TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq_of_isCompact.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [I.Boundaryless] [T2Space M]
  (σ : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 2)
  (α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1)
  (hσ :
    ∀ (t : ℝ), TauCeti.SmoothTwoForm.IsSymplectic ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ))
  (hα :
    ∀ (t : ℝ),
      TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t)
          (TauCeti.mlieDerivForm (fun x => (1, 0)) ↑σ) =
        TauCeti.mextDeriv ↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α))
  {K : Set M} (hK : IsCompact K)
  (hαK : ∀ (t : ℝ), ∀ x ∉ K, ↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α) x = 0) :
  ∃ ψ,
    (ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) I ↑⊤ fun p => (ψ p.1) p.2) ∧
      (∀ (x : M), (ψ 0) x = x) ∧
        (∀ (t : ℝ) (x : M),
            (∀ (u : ℝ), ↑((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α) x = 0) → (ψ t) x = x) ∧
          ∀ (t : ℝ),
            (TauCeti.SmoothForm.mpullback ⇑(ψ t) ⋯)
                ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ) =
              (TauCeti.SmoothForm.mpullback (Prod.mk 0) ⋯) σ
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Moser.html#TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq)
- [Source of `TauCeti.SmoothTwoForm.exists_isotopy_mpullback_eq` in TauCeti/Geometry/Symplectic/Manifold/Moser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/Moser.lean#L193)
