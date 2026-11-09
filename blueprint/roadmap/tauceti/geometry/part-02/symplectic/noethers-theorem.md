---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff, TauCeti.hasDerivAt_noetherCharge, TauCeti.noetherCharge_eq_of_eulerLagrange
statement: formalized
proof: formalized
---

# Noether's theorem

The derivative of a function `f` along the generated vector field `Z_M`
vanishes exactly when `f` Poisson-commutes with the component `μ_Z` of a moment map.

```lean
TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {𝔤 : Type u_4} [LieRing 𝔤] [LieAlgebra ℝ 𝔤] {σ : TauCeti.SmoothTwoForm I M}
  {a : TauCeti.InfinitesimalAction 𝔤 I M} {μ : M → Module.Dual ℝ 𝔤} [FiniteDimensional ℝ E]
  (h : σ.IsMomentMap a μ) (hσ : σ.IsNondegenerate) (f : M → ℝ) (Z : 𝔤) :
  σ.poissonBracket (fun y => (μ y) Z) f = 0 ↔ ∀ (x : M), (d% f x) (a Z x) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/MomentMap.html#TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff).

## Other forms

**Noether's theorem, pointwise in time.** Formalized in Tau Ceti as [`TauCeti.hasDerivAt_noetherCharge`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Noether.html#TauCeti.hasDerivAt_noetherCharge).

```lean
TauCeti.hasDerivAt_noetherCharge.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {L : ℝ → E × E → ℝ} {ξ : ℝ × E → E} {B : ℝ × E → ℝ} {q v : ℝ → E} {t : ℝ}
  (hq : HasDerivAt q (v t) t)
  (hEL :
    HasDerivAt (fun s => fderiv ℝ (fun u => L s (q s, u)) (v s))
      (fderiv ℝ (fun y => L t (y, v t)) (q t)) t)
  (hL : DifferentiableAt ℝ (L t) (q t, v t)) (hξ : DifferentiableAt ℝ ξ (t, q t))
  (hB : DifferentiableAt ℝ B (t, q t))
  (hsym : TauCeti.lagrangianVariation L ξ t (q t, v t) = (fderiv ℝ B (t, q t)) (1, v t)) :
  HasDerivAt (fun s => TauCeti.noetherCharge L ξ B s (q s, v s)) 0 t
```

**Noether's theorem.** Formalized in Tau Ceti as [`TauCeti.noetherCharge_eq_of_eulerLagrange`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Noether.html#TauCeti.noetherCharge_eq_of_eulerLagrange).

```lean
TauCeti.noetherCharge_eq_of_eulerLagrange.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {L : ℝ → E × E → ℝ} {ξ : ℝ × E → E} {B : ℝ × E → ℝ} {q v : ℝ → E} {s : Set ℝ}
  (hs : IsOpen s) (hs' : IsPreconnected s) (hq : ∀ t ∈ s, HasDerivAt q (v t) t)
  (hEL :
    ∀ t ∈ s,
      HasDerivAt (fun s => fderiv ℝ (fun u => L s (q s, u)) (v s))
        (fderiv ℝ (fun y => L t (y, v t)) (q t)) t)
  (hL : ∀ t ∈ s, DifferentiableAt ℝ (L t) (q t, v t)) (hξ : ∀ t ∈ s, DifferentiableAt ℝ ξ (t, q t))
  (hB : ∀ t ∈ s, DifferentiableAt ℝ B (t, q t))
  (hsym : ∀ t ∈ s, TauCeti.lagrangianVariation L ξ t (q t, v t) = (fderiv ℝ B (t, q t)) (1, v t))
  {t₀ t₁ : ℝ} (h₀ : t₀ ∈ s) (h₁ : t₁ ∈ s) :
  TauCeti.noetherCharge L ξ B t₀ (q t₀, v t₀) = TauCeti.noetherCharge L ξ B t₁ (q t₁, v t₁)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/MomentMap.html#TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff)
- [Source of `TauCeti.SmoothTwoForm.IsMomentMap.poissonBracket_eq_zero_iff` in TauCeti/Geometry/Symplectic/Hamiltonian/MomentMap.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Hamiltonian/MomentMap.lean#L277)
