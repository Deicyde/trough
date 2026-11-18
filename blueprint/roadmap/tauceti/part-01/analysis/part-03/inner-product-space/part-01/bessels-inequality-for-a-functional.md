---
declaration: theorem
origin: cited
lean: Orthonormal.summable_norm_apply_sq, LinearMap.sum_norm_inner_leftSingularVector_sq_le, Orthonormal.norm_analysisMap_le, TauCeti.mul_norm_sq_le_apply_self_of_forall_inner_eq_zero
statement: formalized
proof: formalized
---

# Bessel's inequality for a functional

The values of a continuous linear functional `φ` on
an orthonormal family are square summable. The space need not be complete, and its seminorm need
not be a norm.

```lean
Orthonormal.summable_norm_apply_sq.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E] {v : ι → E} (hv : Orthonormal 𝕜 v)
  (φ : StrongDual 𝕜 E) : Summable fun i => ‖φ (v i)‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Orthonormal.summable_norm_apply_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#Orthonormal.summable_norm_apply_sq).

## Other forms

**Bessel's inequality for the left singular vectors.** Formalized in Tau Ceti as [`LinearMap.sum_norm_inner_leftSingularVector_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SingularValues.html#LinearMap.sum_norm_inner_leftSingularVector_sq_le).

```lean
LinearMap.sum_norm_inner_leftSingularVector_sq_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F] (A : E →ₗ[𝕜] F) (x : F) :
  ∑ i, ‖inner 𝕜 (A.leftSingularVector i) x‖ ^ 2 ≤ ‖x‖ ^ 2
```

**Bessel's inequality for the analysis map of an orthonormal family.** Formalized in Tau Ceti as [`Orthonormal.norm_analysisMap_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Family.html#Orthonormal.norm_analysisMap_le).

```lean
Orthonormal.norm_analysisMap_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] {v : ι → E}
  (hv : Orthonormal 𝕜 v) (x : E) : ‖(TauCeti.analysisMap 𝕜 v) x‖ ≤ ‖x‖
```

**Bessel's inequality and the lower half of the min–max principle.** Formalized in Tau Ceti as [`TauCeti.mul_norm_sq_le_apply_self_of_forall_inner_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/MinMax.html#TauCeti.mul_norm_sq_le_apply_self_of_forall_inner_eq_zero).

```lean
TauCeti.mul_norm_sq_le_apply_self_of_forall_inner_eq_zero.{u_1, u_2} {V : Type u_1} {H : Type u_2}
  [AddCommGroup V] [_root_.Module ℝ V] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  {B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ} {J : V →ₗ[ℝ] H} {kappa : ℕ → ℝ} {u : ℕ → V}
  (hsymm : ∀ (v w : V), (B v) w = (B w) v) (hnonneg : ∀ (v : V), 0 ≤ (B v) v)
  (e : HilbertBasis ℕ ℝ H) (hkappa : Monotone kappa) (hJu : ∀ (j : ℕ), J (u j) = e j)
  (heq : ∀ (j : ℕ) (v : V), (B (u j)) v = kappa j * inner ℝ (J (u j)) (J v)) {k : ℕ} {v : V}
  (hv : ∀ j < k, inner ℝ (e j) (J v) = 0) : kappa k * ‖J v‖ ^ 2 ≤ (B v) v
```

## Sources

- [Tau Ceti documentation: `Orthonormal.summable_norm_apply_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#Orthonormal.summable_norm_apply_sq)
- [Source of `Orthonormal.summable_norm_apply_sq` in TauCeti/Analysis/InnerProductSpace/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Parseval.lean#L89)
