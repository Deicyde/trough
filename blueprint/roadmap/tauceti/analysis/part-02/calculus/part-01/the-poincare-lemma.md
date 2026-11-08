---
declaration: theorem
origin: cited
lean: StarConvex.exists_contDiffOn_forall_extDeriv_eq, StarConvex.extDeriv_poincareHomotopy, Convex.exists_invariant_contDiffOn_forall_extDerivWithin_eq, StarConvex.exists_invariant_contDiffOn_forall_extDeriv_eq
statement: formalized
proof: formalized
---

# The Poincaré lemma

A closed `C^r` form, `r ≥ 1`, on an open star-convex set is the
exterior derivative of a `C^r` form, which can be chosen to vanish at the centre.

```lean
StarConvex.exists_contDiffOn_forall_extDeriv_eq.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {n : ℕ} {x₀ : E}
  {s : Set E} {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} [CompleteSpace F] (hs : StarConvex ℝ x₀ s)
  (hso : IsOpen s) {r : ℕ∞} (hr : 1 ≤ r) (hω : ContDiffOn ℝ (↑r) ω s)
  (hclosed : ∀ y ∈ s, extDeriv ω y = 0) :
  ∃ α, ContDiffOn ℝ (↑r) α s ∧ α x₀ = 0 ∧ ∀ x ∈ s, extDeriv α x = ω x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative Poincaré lemma](the-relative-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`StarConvex.exists_contDiffOn_forall_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#StarConvex.exists_contDiffOn_forall_extDeriv_eq).

## Other forms

**The Poincaré lemma.** Formalized in Tau Ceti as [`StarConvex.extDeriv_poincareHomotopy`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#StarConvex.extDeriv_poincareHomotopy).

```lean
StarConvex.extDeriv_poincareHomotopy.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {n : ℕ} {x₀ : E} {s : Set E}
  {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} [CompleteSpace F] (hs : StarConvex ℝ x₀ s) (hso : IsOpen s)
  (hω : ContDiffOn ℝ 1 ω s) (hclosed : ∀ y ∈ s, extDeriv ω y = 0) {x : E} (hx : x ∈ s) :
  extDeriv (TauCeti.poincareHomotopy x₀ ω) x = ω x
```

**The Poincaré lemma for forms invariant under a finite group.** Formalized in Tau Ceti as [`Convex.exists_invariant_contDiffOn_forall_extDerivWithin_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Invariant.html#Convex.exists_invariant_contDiffOn_forall_extDerivWithin_eq).

```lean
Convex.exists_invariant_contDiffOn_forall_extDerivWithin_eq.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] {n : ℕ} {G : Type u_3} [Group G] [Finite G] {ρ : ContRepresentation ℝ G E}
  {s : Set E} {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} (hs : Convex ℝ s) (hsu : UniqueDiffOn ℝ s)
  (hsne : s.Nonempty) (hρs : ∀ (g : G), Set.MapsTo (⇑(ρ g)) s s) {r : ℕ∞} (hr : 1 ≤ r)
  (hωr : ContDiffOn ℝ (↑r) ω s) (hclosed : ∀ y ∈ s, extDerivWithin ω s y = 0)
  (hω : ∀ (g : G), ∀ y ∈ s, (ω ((ρ g) y)).compContinuousLinearMap (ρ g) = ω y) :
  ∃ α,
    ContDiffOn ℝ (↑r) α s ∧
      (∀ (g : G), ∀ y ∈ s, (α ((ρ g) y)).compContinuousLinearMap (ρ g) = α y) ∧
        ∀ y ∈ s, extDerivWithin α s y = ω y
```

**The Poincaré lemma for invariant forms.** Formalized in Tau Ceti as [`StarConvex.exists_invariant_contDiffOn_forall_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Invariant.html#StarConvex.exists_invariant_contDiffOn_forall_extDeriv_eq).

```lean
StarConvex.exists_invariant_contDiffOn_forall_extDeriv_eq.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] {n : ℕ} {x₀ : E} {s : Set E} {ω : E → E [⋀^Fin (n + 1)]→L[ℝ] F} {G : Type u_3}
  [Monoid G] {ρ : ContRepresentation ℝ G E} (hs : StarConvex ℝ x₀ s) (hso : IsOpen s)
  (hρx₀ : ∀ (g : G), (ρ g) x₀ = x₀) (hρs : ∀ (g : G), Set.MapsTo (⇑(ρ g)) s s) {r : ℕ∞} (hr : 1 ≤ r)
  (hωr : ContDiffOn ℝ (↑r) ω s) (hclosed : ∀ y ∈ s, extDeriv ω y = 0)
  (hω : ∀ (g : G), ∀ y ∈ s, (ω ((ρ g) y)).compContinuousLinearMap (ρ g) = ω y) :
  ∃ α,
    ContDiffOn ℝ (↑r) α s ∧
      α x₀ = 0 ∧
        (∀ (g : G), ∀ y ∈ s, (α ((ρ g) y)).compContinuousLinearMap (ρ g) = α y) ∧
          ∀ y ∈ s, extDeriv α y = ω y
```

## Sources

- [Tau Ceti documentation: `StarConvex.exists_contDiffOn_forall_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.html#StarConvex.exists_contDiffOn_forall_extDeriv_eq)
- [Source of `StarConvex.exists_contDiffOn_forall_extDeriv_eq` in TauCeti/Analysis/Calculus/DifferentialForm/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DifferentialForm/Poincare.lean#L391)
