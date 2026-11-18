---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq
statement: formalized
proof: formalized
---

# Moser's isotopy lemma

Let `σ` be a smooth two-form on `ℝ × M` whose slices
`σ_t = ι_t^* σ` are symplectic, and let `α` be a smooth one-form on `ℝ × M` whose slices are
primitives of the velocity, `ι_t^* L_{∂_t} σ = dα_t`. If a time-dependent vector field `X` solves
Moser's equation `ι_{X_t} σ_t = -α_t` and its suspension is complete, then its time-dependent flow
`φ_{s,t}` pulls `σ_t` back to `σ_s`, for all times `s` and `t`.

```lean
TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
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
  {X : ℝ → (x : M) → TangentSpace I x}
  (hX :
    ∀ (t : ℝ),
      TauCeti.RoughForm.interior (X t) ↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ) =
        -↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α))
  (hc : TauCeti.IsCompleteVectorField (TauCeti.timeDependentSuspensionField X)) (s t : ℝ) :
  TauCeti.mpullback I I (TauCeti.timeDependentFlowOf X s t)
      ↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) σ) =
    ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../../manifold/part-01/cartans-magic-formula.md)
- [Moser's principle for families of forms](../../manifold/part-03/mosers-principle-for-families-of-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Moser.html#TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Moser.html#TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq)
- [Source of `TauCeti.SmoothTwoForm.mpullback_timeDependentFlowOf_eq` in TauCeti/Geometry/Symplectic/Manifold/Moser.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/Moser.lean#L94)
