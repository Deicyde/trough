---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.band, ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_band, ProbabilisticTheory.UnitalPositiveLinearMap.le_band, ProbabilisticTheory.UnitalPositiveLinearMap.band_le, ProbabilisticTheory.UnitalPositiveLinearMap.band_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.band_add, ProbabilisticTheory.UnitalPositiveLinearMap.apply_smul_inf_smul, ProbabilisticTheory.UnitalPositiveLinearMap.band_smul
statement: formalized
proof: formalized
---

# Lattice-ordered observables

The module `PhyslibAlpha.ProbabilisticTheory.Classical.LatticeObservables`, [PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean): 31 declarations (2 instances with no name), 15 with a docstring.

> When observables form a lattice, the state space is a Bauer simplex.

## i. Overview

> When observables form a lattice, a state is pure exactly when it gives the minimum
> of two observables the smaller of their expectation values, `ω (f ⊓ g) = min (ω f) (ω g)`. This
> condition is closed, so the pure states form a compact space, and every observable becomes a
> continuous function on it. The positive functionals form a lattice as well, so ensembles refine.
> Hence the state space is a Bauer simplex and every state is a mixture of pure states in exactly one
> way.

## ii. Key results

> - `UnitalPositiveLinearMap.isPure_iff_map_inf` proves that a state is pure exactly when it preserves
>   minima.
> - `OrderUnitLattice.isClosed_setOf_isPure` proves that the pure states form a closed set.
> - `OrderUnitLattice.isBauerSimplexStateSpace` proves that the state space is a Bauer simplex.
> - `OrderUnitLattice.hasUniquePureDecomposition` proves that every state is a mixture of pure states
>   in exactly one way.

## iv. References

> - E. M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971, ch. II.

## A. The band component

**`ProbabilisticTheory.UnitalPositiveLinearMap.band`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L76).

> The part of `ω` carried by `u`: `h ↦ sup {ω (h ⊓ a • u) | a ≥ 0}`.

```lean
noncomputable def band (h : E) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_band`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L80).

```lean
lemma bddAbove_band (h : E) : BddAbove (range fun a : ℝ≥0 => ω (h ⊓ (a : ℝ) • u))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.le_band`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L83).

```lean
lemma le_band (h : E) (a : ℝ≥0) : ω (h ⊓ (a : ℝ) • u) ≤ band ω u h
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.band_le`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L86).

```lean
lemma band_le {h : E} {r : ℝ} (hr : ∀ a : ℝ≥0, ω (h ⊓ (a : ℝ) • u) ≤ r) : band ω u h ≤ r
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.band_nonneg`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L89).

```lean
lemma band_nonneg {h : E} (hh : 0 ≤ h) : 0 ≤ band ω u h
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.band_add`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L92).

```lean
lemma band_add (hu : 0 ≤ u) {h₁ h₂ : E} (h₁0 : 0 ≤ h₁) (h₂0 : 0 ≤ h₂) :
    band ω u (h₁ + h₂) = band ω u h₁ + band ω u h₂
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_smul_inf_smul`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L106).

```lean
lemma apply_smul_inf_smul {c : ℝ} (hc : 0 ≤ c) (h : E) (a : ℝ) :
    ω (c • h ⊓ (c * a) • u) = c * ω (h ⊓ a • u)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.band_smul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L110).

```lean
lemma band_smul {c : ℝ} (hc : 0 < c) {h : E} :
    band ω u (c • h) = c * band ω u h
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bandMap`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L124).

> The part of `ω` carried by a positive element `u`, as a positive functional.

```lean
noncomputable def bandMap (hu : 0 ≤ u) : E →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bandMap_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L128).

```lean
lemma bandMap_apply (hu : 0 ≤ u) {h : E} (hh : 0 ≤ h) : bandMap ω hu h = band ω u h
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bandMap_le`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L131).

```lean
lemma bandMap_le (hu : 0 ≤ u) : bandMap ω hu ≤ ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bandMap_self`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L135).

```lean
lemma bandMap_self (hu : 0 ≤ u) : bandMap ω hu u = ω u
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bandMap_eq_zero`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L140).

```lean
lemma bandMap_eq_zero (hu : 0 ≤ u) {g : E} (hg : 0 ≤ g) (h : g ⊓ u = 0) : bandMap ω hu g = 0
```

## B. Pure states preserve infima

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_zero_of_inf_eq_zero`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L152).

> A pure state vanishes on one of any two disjoint positive elements.

```lean
lemma IsPure.apply_eq_zero_of_inf_eq_zero {ω : 𝓢[ℝ, E]} (hω : ω.IsPure) {g u : E} (hg : 0 ≤ g)
    (hu : 0 ≤ u) (h : g ⊓ u = 0) : ω g = 0 ∨ ω u = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.map_inf`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L167).

> Pure states preserve infima.

```lean
lemma IsPure.map_inf {ω : 𝓢[ℝ, E]} (hω : ω.IsPure) (f g : E) :
    ω (f ⊓ g) = min (ω f) (ω g)
```

## C. States preserving infima are pure

**`ProbabilisticTheory.UnitalPositiveLinearMap.map_abs_sub_eq_zero_of_map_inf`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L184).

> An infimum-preserving state does not see the deviation of an observable from its value.

```lean
lemma map_abs_sub_eq_zero_of_map_inf {ω : 𝓢[ℝ, E]} (h : ∀ f g, ω (f ⊓ g) = min (ω f) (ω g))
    (f : E) : ω |f - ω f • (1 : E)| = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.eq_of_le_smul_of_map_inf`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L193).

> A state dominated by a multiple of an infimum-preserving state is that state.

```lean
lemma eq_of_le_smul_of_map_inf {ω φ : 𝓢[ℝ, E]} (h : ∀ f g, ω (f ⊓ g) = min (ω f) (ω g))
    {c : ℝ} (hφ : ∀ f, 0 ≤ f → φ f ≤ c * ω f) : φ = ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_of_map_inf`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L208).

> States preserving infima are pure.

```lean
lemma isPure_of_map_inf {ω : 𝓢[ℝ, E]} (h : ∀ f g, ω (f ⊓ g) = min (ω f) (ω g)) : ω.IsPure
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_map_inf`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L221).

> The pure states of an order-unit lattice are the states preserving infima.

```lean
lemma isPure_iff_map_inf {ω : 𝓢[ℝ, E]} : ω.IsPure ↔ ∀ f g, ω (f ⊓ g) = min (ω f) (ω g)
```

## D. Pure states of order-unit lattices

**`ProbabilisticTheory.OrderUnitLattice.isClosed_setOf_isPure`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L239).

> The pure states of an order-unit lattice form a weak-star closed set.

```lean
lemma isClosed_setOf_isPure : IsClosed {ω : stateSpace E | (toState ω).IsPure}
```

**An instance with no name**, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L257).

```lean
instance : CompactSpace (PureState E)
```

## E. Observables as continuous functions

**`ProbabilisticTheory.OrderUnitLattice.evalPure_inf`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L266).

```lean
lemma evalPure_inf (f g : E) : evalPure (f ⊓ g) = evalPure f ⊓ evalPure g
```

**`ProbabilisticTheory.OrderUnitLattice.evalPure_sup`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L270).

```lean
lemma evalPure_sup (f g : E) : evalPure (f ⊔ g) = evalPure f ⊔ evalPure g
```

**`ProbabilisticTheory.OrderUnitLattice.separatesPointsStrongly`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L275).

```lean
lemma separatesPointsStrongly : (range (evalPure (E := E))).SeparatesPointsStrongly
```

**`ProbabilisticTheory.OrderUnitLattice.denseRange_evalPure`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L283).

> **Stone–Weierstrass**: observables are dense among continuous functions on the pure
> states.

```lean
lemma denseRange_evalPure : DenseRange (evalPure (E := E))
```

## F. Unique decomposition

**`ProbabilisticTheory.OrderUnitLattice.isBauerSimplexStateSpace`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L297).

> **Classicality of lattice-ordered observables**: the state space of an order-unit lattice is a
> Bauer simplex.

```lean
lemma isBauerSimplexStateSpace : IsBauerSimplexStateSpace E
```

**`ProbabilisticTheory.OrderUnitLattice.hasUniquePureDecomposition`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L303).

> **Unique decomposition into pure states**: every state of an order-unit lattice is a mixture
> of pure states in exactly one way.

```lean
lemma hasUniquePureDecomposition (φ : 𝓢[ℝ, E]) : φ.HasUniquePureDecomposition
```

## G. Classical systems are Bauer simplices

**`BoundedMeasurable.isBauerSimplexStateSpace`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L325).

> **The state space of a classical system is a Bauer simplex.**

```lean
lemma isBauerSimplexStateSpace : IsBauerSimplexStateSpace (BoundedMeasurable Ω)
```

**`BoundedMeasurable.hasUniquePureDecomposition`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L329).

> **Classicality**: every state of a classical system decomposes uniquely into pure states.

```lean
lemma hasUniquePureDecomposition
    (φ : 𝓢[ℝ, BoundedMeasurable Ω]) : φ.HasUniquePureDecomposition
```

## H. Finite classical systems are Bauer simplices

**An instance with no name**, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L351).

```lean
instance : OrderUnitLattice (FiniteClassicalSystem ι)
```

**`ProbabilisticTheory.FiniteClassicalSystem.isBauerSimplexStateSpace`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean#L356).

> The state space of a finite classical system is a Bauer simplex.

```lean
lemma isBauerSimplexStateSpace : IsBauerSimplexStateSpace (FiniteClassicalSystem ι)
```

## Depends on

- [Observables of a sample space](boundedmeasurable.md)
- [Finite classical systems](finitesystem.md)
- [Classical systems: unique decomposition into pure states](simplexstatespace.md)

## Proof depends on

- [Bauer simplices](bauersimplex.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/LatticeObservables.lean)
