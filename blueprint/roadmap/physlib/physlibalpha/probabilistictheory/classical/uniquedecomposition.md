---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.upperEnvelope_le, ProbabilisticTheory.StateSpace.maxApply, ProbabilisticTheory.StateSpace.maxApply_apply, ProbabilisticTheory.StateSpace.apply_le_maxApply, ProbabilisticTheory.StateSpace.maxApply_le_of_forall, ProbabilisticTheory.StateSpace.exists_eq_maxApply, ProbabilisticTheory.StateSpace.maxApply_le, ProbabilisticTheory.StateSpace.abs_maxApply_le
statement: formalized
proof: formalized
---

# Uniqueness of pure decompositions

The module `PhyslibAlpha.ProbabilisticTheory.Classical.UniqueDecomposition`, [PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean): 35 declarations, 14 with a docstring.

> Choquet–Meyer uniqueness: when ensembles refine, pure decompositions are unique.

## i. Overview

> When ensembles refine, every state has at most one pure decomposition. This is the uniqueness half
> of the Choquet–Meyer theorem.
>
> A measure on the pure states is fixed by the averages it gives to continuous functions. We test it
> on special functions: the largest of finitely many expectation values, `ω ↦ max (ω A₁) … (ω Aₙ)`.
> Every pure decomposition of a state `ω` averages this function to the same number, the upper
> envelope of `A₁, …, Aₙ` at `ω`. To see this, cut the pure states into small pieces on each of which
> one `Aᵢ` is nearly the largest, and glue the pieces with refinement. These test functions and their
> differences are dense among all continuous functions, so two pure decompositions of the same state
> agree.

## ii. Key results

> - `StateSpace.maxApply` is the largest expectation value of a state on finitely many observables.
> - `PureState.integral_maxApply_eq` proves that, when ensembles refine, a pure decomposition averages
>   the largest value to the upper envelope.
> - `EnsemblesRefine.eq_of_toPositive_eq` proves that two measures on the pure states giving the same
>   positive functional are equal. This is **Choquet–Meyer uniqueness**.
> - `EnsemblesRefine.hasUniquePureDecomposition` proves that, when ensembles refine, a pure
>   decomposition is unique.

## iv. References

> - G. Choquet and P.-A. Meyer, *Existence et unicité des représentations intégrales dans les
>   convexes compacts quelconques*, Ann. Inst. Fourier 13 (1963), 139–154.
> - E. M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971, ch. II.3.

## A. The largest value on a finite family

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.upperEnvelope_le`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L77).

> At a pure state, the upper envelope of a family is at most its largest value on the family.

```lean
lemma UnitalPositiveLinearMap.IsPure.upperEnvelope_le {e : 𝓢[ℝ, E]} (he : e.IsPure) (s : ι → E)
    {M : ℝ} (hM : ∀ i, e (s i) ≤ M) : upperEnvelope s e.toPositiveLinearMap ≤ M
```

**`ProbabilisticTheory.StateSpace.maxApply`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L97).

> The largest value of a state on a finite family of observables.

```lean
noncomputable def maxApply (s : ι → E) : C(stateSpace E, ℝ)
```

**`ProbabilisticTheory.StateSpace.maxApply_apply`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L100).

```lean
lemma maxApply_apply (s : ι → E) (ω : stateSpace E) :
    maxApply s ω = Finset.univ.sup' Finset.univ_nonempty fun i => toState ω (s i)
```

**`ProbabilisticTheory.StateSpace.apply_le_maxApply`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L104).

```lean
lemma apply_le_maxApply (s : ι → E) (ω : stateSpace E) (i : ι) :
    toState ω (s i) ≤ maxApply s ω
```

**`ProbabilisticTheory.StateSpace.maxApply_le_of_forall`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L109).

```lean
lemma maxApply_le_of_forall {s : ι → E} {ω : stateSpace E} {r : ℝ}
    (h : ∀ i, toState ω (s i) ≤ r) : maxApply s ω ≤ r
```

**`ProbabilisticTheory.StateSpace.exists_eq_maxApply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L114).

```lean
lemma exists_eq_maxApply (s : ι → E) (ω : stateSpace E) : ∃ i, maxApply s ω = toState ω (s i)
```

**`ProbabilisticTheory.StateSpace.maxApply_le`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L118).

```lean
lemma maxApply_le {s : ι → E} {b : E} (hb : b ∈ upperBounds (range s)) (ω : stateSpace E) :
    maxApply s ω ≤ toState ω b
```

**`ProbabilisticTheory.StateSpace.abs_maxApply_le`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L122).

```lean
lemma abs_maxApply_le (s : ι → E) (ω : stateSpace E) :
    |maxApply s ω| ≤ ∑ i, orderUnitNorm (s i)
```

**`ProbabilisticTheory.StateSpace.maxApply_unit`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L129).

```lean
lemma maxApply_unit (a : E) (ω : stateSpace E) : maxApply (fun _ : Unit => a) ω = toState ω a
```

**`ProbabilisticTheory.StateSpace.maxApply_sumElim`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L132).

```lean
lemma maxApply_sumElim (s : ι → E) (t : κ → E) :
    maxApply (Sum.elim s t) = maxApply s ⊔ maxApply t
```

**`ProbabilisticTheory.StateSpace.maxApply_add`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L143).

```lean
lemma maxApply_add (s : ι → E) (t : κ → E) :
    maxApply (fun p : ι × κ => s p.1 + t p.2) = maxApply s + maxApply t
```

## B. Integrating the largest value

**`ProbabilisticTheory.PureState.integrable_maxApply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L170).

```lean
lemma integrable_maxApply : Integrable (fun k : PureState E => maxApply s k.1) μ
```

**`ProbabilisticTheory.PureState.integral_maxApply_le`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L175).

> Integrating the largest value on a family stays below the upper envelope.

```lean
lemma integral_maxApply_le : ∫ k, maxApply s k.1 ∂μ ≤ upperEnvelope s (toPositive μ)
```

**`ProbabilisticTheory.PureState.toPositive_restrict_univ`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L179).

```lean
lemma toPositive_restrict_univ : toPositive (μ.restrict univ) = toPositive μ
```

**`ProbabilisticTheory.PureState.toPositive_restrict_inter_add_sdiff`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L182).

```lean
lemma toPositive_restrict_inter_add_sdiff (A : Set (PureState E)) {W : Set (PureState E)}
    (hW : MeasurableSet W) :
    toPositive (μ.restrict (A ∩ W)) + toPositive (μ.restrict (A \ W)) =
      toPositive (μ.restrict A)
```

**`ProbabilisticTheory.PureState.sum_norm_smul_one_mem_upperBounds`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L190).

> A finite family of observables lies below the sum of their norms times the unit.

```lean
lemma sum_norm_smul_one_mem_upperBounds (s : ι → E) :
    (∑ i, orderUnitNorm (s i)) • (1 : E) ∈ upperBounds (Set.range s)
```

**`ProbabilisticTheory.PureState.upperEnvelope_restrict_le_norm`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L198).

> On any piece, the upper envelope exceeds the integral of the largest value by at most twice
> the norm of the family times the mass of the piece.

```lean
lemma upperEnvelope_restrict_le_norm (A : Set (PureState E)) :
    upperEnvelope s (toPositive (μ.restrict A)) ≤
      ∫ k in A, maxApply s k.1 ∂μ + 2 * (∑ i, orderUnitNorm (s i)) * μ.real A
```

**`ProbabilisticTheory.PureState.exists_nhds_upperEnvelope_restrict_le`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L210).

> Near a pure state, the upper envelope on a piece is within `ε` times its mass of the integral
> of the largest value.

```lean
lemma exists_nhds_upperEnvelope_restrict_le {ε : ℝ} (hε : 0 < ε) (e : PureState E) :
    ∃ W : Set (PureState E), IsOpen W ∧ e ∈ W ∧ ∀ A ⊆ W, MeasurableSet A →
      upperEnvelope s (toPositive (μ.restrict A)) ≤ ∫ k in A, maxApply s k.1 ∂μ + ε * μ.real A
```

**`ProbabilisticTheory.PureState.upperEnvelope_restrict_empty_le`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L229).

```lean
lemma upperEnvelope_restrict_empty_le [Nonempty ι] :
    upperEnvelope s (toPositive (μ.restrict ∅)) ≤ 0
```

## C. Integrating the largest value when ensembles refine

**`ProbabilisticTheory.PureState.upperEnvelope_restrict_le_of_inter_sdiff`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L243).

```lean
lemma upperEnvelope_restrict_le_of_inter_sdiff {A W : Set (PureState E)} (hW : MeasurableSet W)
    {r₁ r₂ : ℝ}
    (h₁ : upperEnvelope s (toPositive (μ.restrict (A ∩ W))) ≤
      ∫ k in A ∩ W, maxApply s k.1 ∂μ + r₁)
    (h₂ : upperEnvelope s (toPositive (μ.restrict (A \ W))) ≤
      ∫ k in A \ W, maxApply s k.1 ∂μ + r₂) :
    upperEnvelope s (toPositive (μ.restrict A)) ≤ ∫ k in A, maxApply s k.1 ∂μ + (r₁ + r₂)
```

**`ProbabilisticTheory.PureState.upperEnvelope_restrict_le_of_subset_biUnion`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L256).

> Pieces covered by finitely many good neighbourhoods are good.

```lean
lemma upperEnvelope_restrict_le_of_subset_biUnion {ε : ℝ} {W : PureState E → Set (PureState E)}
    (hWm : ∀ e, MeasurableSet (W e)) (hW : ∀ e, ∀ A ⊆ W e, MeasurableSet A →
      upperEnvelope s (toPositive (μ.restrict A)) ≤ ∫ k in A, maxApply s k.1 ∂μ + ε * μ.real A)
    (t : Finset (PureState E)) : ∀ A, MeasurableSet A → A ⊆ ⋃ e ∈ t, W e →
      upperEnvelope s (toPositive (μ.restrict A)) ≤ ∫ k in A, maxApply s k.1 ∂μ + ε * μ.real A
```

**`ProbabilisticTheory.PureState.upperEnvelope_restrict_le_of_isCompact`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L280).

> On a compact set of pure states, the upper envelope is within `ε` times its mass of the
> integral of the largest value.

```lean
lemma upperEnvelope_restrict_le_of_isCompact {ε : ℝ} (hε : 0 < ε) {C : Set (PureState E)}
    (hC : IsCompact C) :
    upperEnvelope s (toPositive (μ.restrict C)) ≤ ∫ k in C, maxApply s k.1 ∂μ + ε * μ.real C
```

**`ProbabilisticTheory.PureState.exists_isCompact_measureReal_sdiff_lt`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L290).

> A finite regular measure gives all but `ε` of its mass to a compact set.

```lean
lemma exists_isCompact_measureReal_sdiff_lt (μ : Measure (PureState E)) [IsFiniteMeasure μ]
    [μ.Regular] {ε : ℝ} (hε : 0 < ε) : ∃ C, IsCompact C ∧ μ.real (univ \ C) < ε
```

**`ProbabilisticTheory.PureState.upperEnvelope_le_integral_add`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L297).

```lean
lemma upperEnvelope_le_integral_add [IsProbabilityMeasure μ] [μ.Regular] {ε : ℝ} (hε : 0 < ε) :
    upperEnvelope s (toPositive μ) ≤
      ∫ k, maxApply s k.1 ∂μ + (ε + 2 * (∑ i, orderUnitNorm (s i)) * ε)
```

**`ProbabilisticTheory.PureState.integral_maxApply_eq`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L314).

> **Choquet–Meyer**: when ensembles refine, a regular probability measure on the pure states
> integrates the largest value of a finite family to the upper envelope at its barycenter.

```lean
lemma integral_maxApply_eq [IsProbabilityMeasure μ] [μ.Regular] :
    ∫ k, maxApply s k.1 ∂μ = upperEnvelope s (toPositive μ)
```

## D. Density of largest values

**`ProbabilisticTheory.StateSpace.maxApplyDiffs`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L334).

> Differences of largest values on finite families of observables.

```lean
def maxApplyDiffs : Set C(stateSpace E, ℝ)
```

**`ProbabilisticTheory.StateSpace.sup_mem_maxApplyDiffs`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L338).

```lean
lemma sup_mem_maxApplyDiffs {g h : C(stateSpace E, ℝ)} (hg : g ∈ maxApplyDiffs)
    (hh : h ∈ maxApplyDiffs) : g ⊔ h ∈ maxApplyDiffs
```

**`ProbabilisticTheory.StateSpace.neg_mem_maxApplyDiffs`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L350).

```lean
lemma neg_mem_maxApplyDiffs {g : C(stateSpace E, ℝ)} (hg : g ∈ maxApplyDiffs) :
    -g ∈ maxApplyDiffs
```

**`ProbabilisticTheory.StateSpace.inf_mem_maxApplyDiffs`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L355).

```lean
lemma inf_mem_maxApplyDiffs {g h : C(stateSpace E, ℝ)} (hg : g ∈ maxApplyDiffs)
    (hh : h ∈ maxApplyDiffs) : g ⊓ h ∈ maxApplyDiffs
```

**`ProbabilisticTheory.StateSpace.separatesPointsStrongly_maxApplyDiffs`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L361).

```lean
lemma separatesPointsStrongly_maxApplyDiffs :
    (maxApplyDiffs (E := E)).SeparatesPointsStrongly
```

**`ProbabilisticTheory.StateSpace.closure_maxApplyDiffs`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L369).

> **Stone–Weierstrass**: differences of largest values are dense among continuous functions on
> the state space.

```lean
lemma closure_maxApplyDiffs : closure (maxApplyDiffs (E := E)) = univ
```

## E. Uniqueness

**`ProbabilisticTheory.PureState.eq_of_map_val_eq`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L386).

```lean
lemma eq_of_map_val_eq {μ ν : Measure (PureState E)}
    (h : μ.map Subtype.val = ν.map Subtype.val) : μ = ν
```

**`ProbabilisticTheory.PureState.integral_map_val_eq`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L397).

```lean
lemma integral_map_val_eq (h : toPositive μ = toPositive ν) (g : C(stateSpace E, ℝ)) :
    ∫ ω, g ω ∂μ.map Subtype.val = ∫ ω, g ω ∂ν.map Subtype.val
```

**`ProbabilisticTheory.EnsemblesRefine.eq_of_toPositive_eq`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L417).

> **Choquet–Meyer uniqueness**: when ensembles refine, two regular probability measures on the
> pure states with the same barycenter are equal.

```lean
lemma EnsemblesRefine.eq_of_toPositive_eq (hE : EnsemblesRefine E)
    {μ ν : Measure (PureState E)} [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [μ.Regular]
    [ν.Regular] (h : toPositive μ = toPositive ν) : μ = ν
```

## F. Unique pure decompositions

**`ProbabilisticTheory.EnsemblesRefine.hasUniquePureDecomposition`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean#L433).

> **Choquet–Meyer**: when ensembles refine, a state with a decomposition into pure states has
> exactly one.

```lean
lemma EnsemblesRefine.hasUniquePureDecomposition (hE : EnsemblesRefine E) {ω : 𝓢[ℝ, E]}
    (h : ω.HasPureDecomposition) : ω.HasUniquePureDecomposition
```

## Depends on

- [Refinement of ensembles](ensemblerefinement.md)

## Proof depends on

- [Integration as a continuous functional](../../mathematics/part-02/measuretheory/integrationfunctional.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/UniqueDecomposition.lean)
