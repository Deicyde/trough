---
declaration: theorem
origin: cited
lean: TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul, TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_eq
statement: formalized
proof: formalized
---

# Moser's principle for families of forms

Let `X` be a jointly `C²` time-dependent vector
field with complete suspension and time-dependent flow `φ`, and let `α` be a `C¹` form on `ℝ × M`
with slices `α_t = ι_t^* α`. If the rate `ι_t^* L_{∂_t} α + L_{X_t} α_t` is `g_t • α_t` for a
continuous function `g` on `ℝ × M`, then the flow rescales the slices:
`(φ_{s,t}^* α_t)ₓ = exp (∫ₛᵗ g (u, φ_{s,u} x) du) • (α_s)ₓ`.

```lean
TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul.{u_1, u_2, u_3,
    u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I 2 M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} {X : ℝ → (x : M) → TangentSpace I x}
  {α : TauCeti.RoughForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) F k}
  (hX : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) I.tangent 2 fun p => ⟨p.2, X p.1 p.2⟩)
  (hc : TauCeti.IsCompleteVectorField (TauCeti.timeDependentSuspensionField X)) {g : ℝ × M → ℝ}
  (hg : Continuous g)
  (hα :
    ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I)
      (((modelWithCornersSelf ℝ ℝ).prod I).prod (modelWithCornersSelf ℝ ((ℝ × E) [⋀^Fin k]→L[ℝ] F)))
      1 fun p => ⟨p, α p⟩)
  (hL :
    ∀ (t : ℝ),
      TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t)
            (TauCeti.mlieDerivForm (fun x => (1, 0)) α) +
          TauCeti.mlieDerivForm (X t)
            (TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) α) =
        fun y => g (t, y) • TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) α y)
  (s t : ℝ) (x : M) :
  TauCeti.mpullback I I (TauCeti.timeDependentFlowOf X s t)
      (TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) α) x =
    Real.exp (∫ (u : ℝ) in s..t, g (u, TauCeti.timeDependentFlowOf X s u x)) •
      TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk s) α x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Flow/Family.html#TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul).

## Other forms

**Moser's principle for families of forms, invariance case.** Formalized in Tau Ceti as [`TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Flow/Family.html#TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_eq).

```lean
TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_eq.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I 2 M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {k : ℕ} {X : ℝ → (x : M) → TangentSpace I x}
  {α : TauCeti.RoughForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) F k}
  (hX : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) I.tangent 2 fun p => ⟨p.2, X p.1 p.2⟩)
  (hc : TauCeti.IsCompleteVectorField (TauCeti.timeDependentSuspensionField X))
  (hα :
    ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I)
      (((modelWithCornersSelf ℝ ℝ).prod I).prod (modelWithCornersSelf ℝ ((ℝ × E) [⋀^Fin k]→L[ℝ] F)))
      1 fun p => ⟨p, α p⟩)
  (hL :
    ∀ (t : ℝ),
      TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t)
            (TauCeti.mlieDerivForm (fun x => (1, 0)) α) +
          TauCeti.mlieDerivForm (X t)
            (TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) α) =
        0)
  (s t : ℝ) :
  TauCeti.mpullback I I (TauCeti.timeDependentFlowOf X s t)
      (TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk t) α) =
    TauCeti.mpullback I ((modelWithCornersSelf ℝ ℝ).prod I) (Prod.mk s) α
```

## Sources

- [Tau Ceti documentation: `TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Flow/Family.html#TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul)
- [Source of `TauCeti.mpullback_timeDependentFlowOf_mpullback_prodMk_apply_eq_exp_integral_smul` in TauCeti/Geometry/Manifold/DifferentialForm/Flow/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Flow/Family.lean#L384)
