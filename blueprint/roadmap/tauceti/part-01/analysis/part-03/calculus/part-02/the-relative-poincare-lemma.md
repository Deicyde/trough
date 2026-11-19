---
declaration: theorem
origin: cited
lean: Convex.exists_contDiffOn_forall_extDerivWithin_eq, Convex.extDerivWithin_poincareHomotopy, IsOpen.exists_contDiffOn_relative_primitive
statement: formalized
proof: formalized
---

# The relative Poincaré lemma

A `C^r` form, `r ≥ 1`, closed within a convex set with unique
derivatives is the exterior derivative within the set of a `C^r` form, which can be chosen to
vanish at any given point of the set. The set need not be open: a closed half-ball, the image of
a boundary chart, is allowed.

```lean
Convex.exists_contDiffOn_forall_extDerivWithin_eq.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {n : ℕ} {x₀ : E}
  {s : Set E} {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} [CompleteSpace F] (hs : Convex ℝ s)
  (hsu : UniqueDiffOn ℝ s) (hx₀ : x₀ ∈ s) {r : ℕ∞} (hr : 1 ≤ r) (hω : ContDiffOn ℝ (↑r) ω s)
  (hclosed : ∀ y ∈ s, extDerivWithin ω s y = 0) :
  ∃ α, ContDiffOn ℝ (↑r) α s ∧ α x₀ = 0 ∧ ∀ x ∈ s, extDerivWithin α s x = ω x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.exists_contDiffOn_forall_extDerivWithin_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#Convex.exists_contDiffOn_forall_extDerivWithin_eq).

## Other forms

**The relative Poincaré lemma.** Formalized in Tau Ceti as [`Convex.extDerivWithin_poincareHomotopy`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#Convex.extDerivWithin_poincareHomotopy).

```lean
Convex.extDerivWithin_poincareHomotopy.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {n : ℕ} {x₀ : E}
  {s : Set E} {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} [CompleteSpace F] (hs : Convex ℝ s)
  (hsu : UniqueDiffOn ℝ s) (hx₀ : x₀ ∈ s) (hω : ContDiffOn ℝ 1 ω s)
  (hclosed : ∀ y ∈ s, extDerivWithin ω s y = 0) {x : E} (hx : x ∈ s) :
  extDerivWithin (TauCeti.poincareHomotopy x₀ ω) s x = ω x
```

**The relative Poincaré lemma on an adapted open neighborhood.** Formalized in Tau Ceti as [`IsOpen.exists_contDiffOn_relative_primitive`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Relative/Basic.html#IsOpen.exists_contDiffOn_relative_primitive).

```lean
IsOpen.exists_contDiffOn_relative_primitive.{u_1, u_2, u_3} {E : Type u_1} {N : Type u_2}
  {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup N] [NormedSpace ℝ N]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [CompleteSpace F] {s : Set (E × N)}
  (hso : IsOpen s) {r : ℕ∞} (hr : 1 ≤ r) {ω : E × N → (E × N) [⋀^Fin (k + 1)]→L[ℝ] F}
  (hω : ContDiffOn ℝ (↑r) ω s) (hscale : ∀ x ∈ s, ∀ t ∈ Set.Icc 0 1, (x.1, t • x.2) ∈ s)
  (hclosed : ∀ x ∈ s, extDeriv ω x = 0)
  (hzero :
    ∀ (q : E),
      (q, 0) ∈ s → (ω (q, 0)).compContinuousLinearMap (ContinuousLinearMap.inl ℝ E N) = 0) :
  ∃ β, ContDiffOn ℝ (↑r) β s ∧ (∀ (q : E), β (q, 0) = 0) ∧ ∀ x ∈ s, extDeriv β x = ω x
```

## Sources

- [Tau Ceti documentation: `Convex.exists_contDiffOn_forall_extDerivWithin_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#Convex.exists_contDiffOn_forall_extDerivWithin_eq)
- [Source of `Convex.exists_contDiffOn_forall_extDerivWithin_eq` in TauCeti/Analysis/Calculus/DifferentialForm/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.lean#L822)
