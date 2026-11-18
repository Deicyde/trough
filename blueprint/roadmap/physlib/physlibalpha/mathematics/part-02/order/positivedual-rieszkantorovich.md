---
declaration: module
origin: cited
lean: HasRieszDecomposition, VectorLattice.hasRieszDecomposition, PositiveLinearMap.rkSup, PositiveLinearMap.bddAbove_rkSup, PositiveLinearMap.le_rkSup, PositiveLinearMap.rkSup_le, PositiveLinearMap.rkSup_nonneg, PositiveLinearMap.rkSup_add_rkSup_le
statement: formalized
proof: formalized
---

# The Riesz–Kantorovich formula

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.RieszKantorovich`, [PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean): 21 declarations, 13 with a docstring.

> Riesz decomposition makes positive functionals a lattice via the Riesz–Kantorovich formula.

## i. Overview

> An ordered real vector space has the Riesz decomposition when a nonnegative element below a sum of
> two nonnegative elements splits into pieces below the summands. Vector lattices have it. Then any
> two positive functionals have a least upper bound, given by the Riesz–Kantorovich formula
> `(φ ⊔ ψ) f = sup {φ g + ψ (f - g) | 0 ≤ g ≤ f}`: the positive functionals form a lattice.
>
> In a lattice of positive functionals, a positive functional below a sum splits into pieces below
> the summands, and finite families with the same sum have common refinements.

## ii. Key results

> - `HasRieszDecomposition E` : the Riesz decomposition.
> - `PositiveLinearMap.isLUB_rkSup` : the Riesz–Kantorovich formula gives the least upper bound.
> - `HasLatticeDualCone E` : the positive functionals form a lattice.
> - `HasRieszDecomposition.hasLatticeDualCone` : the Riesz decomposition makes the positive
>   functionals a lattice.
> - `VectorLattice.hasLatticeDualCone` : the positive functionals on a vector lattice form a lattice.
> - `HasLatticeDualCone.exists_refinement` : positive functionals refine.
> - `PositiveLinearMap.HasRefinement` : finite families with the same sum have a common refinement.

## iv. References

> - C. D. Aliprantis and O. Burkinshaw, *Positive Operators*, Springer, 2006, ch. 1.
> - E. M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971, ch. II.

## A. The Riesz–Kantorovich supremum

**`HasRieszDecomposition`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L65).

> Riesz decomposition: a nonnegative observable below a sum of two nonnegative observables splits
> into two pieces, each below one summand.

```lean
def HasRieszDecomposition (E : Type*) [AddCommGroup E] [PartialOrder E] : Prop
```

**`VectorLattice.hasRieszDecomposition`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L70).

> A real vector lattice has the Riesz decomposition.

```lean
lemma VectorLattice.hasRieszDecomposition (E : Type*) [AddCommGroup E] [Lattice E]
    [IsOrderedAddMonoid E] : HasRieszDecomposition E
```

**`PositiveLinearMap.rkSup`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L85).

> The best split of `f` between `φ` and `ψ`: the supremum of `φ g + ψ (f - g)` over
> `0 ≤ g ≤ f`.

```lean
noncomputable def rkSup (f : E) : ℝ
```

**`PositiveLinearMap.bddAbove_rkSup`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L89).

```lean
lemma bddAbove_rkSup (f : E) : BddAbove ((fun g => φ g + ψ (f - g)) '' Set.Icc 0 f)
```

**`PositiveLinearMap.le_rkSup`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L93).

```lean
lemma le_rkSup {f g : E} (hg : g ∈ Set.Icc 0 f) : φ g + ψ (f - g) ≤ rkSup φ ψ f
```

**`PositiveLinearMap.rkSup_le`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L97).

```lean
lemma rkSup_le {f : E} (hf : 0 ≤ f) {r : ℝ} (h : ∀ g ∈ Set.Icc 0 f, φ g + ψ (f - g) ≤ r) :
    rkSup φ ψ f ≤ r
```

**`PositiveLinearMap.rkSup_nonneg`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L101).

```lean
lemma rkSup_nonneg {f : E} (hf : 0 ≤ f) : 0 ≤ rkSup φ ψ f
```

**`PositiveLinearMap.rkSup_add_rkSup_le`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L104).

```lean
lemma rkSup_add_rkSup_le {f₁ f₂ : E} (h₁ : 0 ≤ f₁) (h₂ : 0 ≤ f₂) :
    rkSup φ ψ f₁ + rkSup φ ψ f₂ ≤ rkSup φ ψ (f₁ + f₂)
```

**`PositiveLinearMap.rkSup_add`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L118).

```lean
lemma rkSup_add (hE : HasRieszDecomposition E) {f₁ f₂ : E} (h₁ : 0 ≤ f₁) (h₂ : 0 ≤ f₂) :
    rkSup φ ψ (f₁ + f₂) = rkSup φ ψ f₁ + rkSup φ ψ f₂
```

**`PositiveLinearMap.rkSup_smul`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L126).

```lean
lemma rkSup_smul [PosSMulMono ℝ E] {c : ℝ} (hc : 0 < c) {f : E} (hf : 0 ≤ f) :
    rkSup φ ψ (c • f) = c * rkSup φ ψ f
```

**`PositiveLinearMap.rkSupMap`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L144).

> The Riesz–Kantorovich supremum of two positive functionals.

```lean
noncomputable def rkSupMap : E →ₚ[ℝ] ℝ
```

**`PositiveLinearMap.rkSupMap_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L150).

```lean
lemma rkSupMap_apply {f : E} (hf : 0 ≤ f) : rkSupMap φ ψ hE f = rkSup φ ψ f
```

**`PositiveLinearMap.isLUB_rkSup`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L157).

> **Riesz–Kantorovich**: the least upper bound of two positive functionals, when the space has
> the Riesz decomposition.

```lean
lemma isLUB_rkSup : IsLUB {φ, ψ} (rkSupMap φ ψ hE)
```

## B. The lattice dual cone

**`HasLatticeDualCone`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L184).

> The positive functionals on `E` form a lattice: any two have a least upper bound.

```lean
def HasLatticeDualCone (E : Type*) [AddCommGroup E] [PartialOrder E] [IsOrderedAddMonoid E]
    [Module ℝ E] [IsDirectedOrder E] : Prop
```

**`HasRieszDecomposition.hasLatticeDualCone`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L190).

> **Riesz–Kantorovich**: when the space has the Riesz decomposition, the positive functionals
> form a lattice.

```lean
lemma HasRieszDecomposition.hasLatticeDualCone {E : Type*} [AddCommGroup E] [PartialOrder E]
    [IsOrderedAddMonoid E] [Module ℝ E] [PosSMulMono ℝ E] [IsDirectedOrder E]
    (hE : HasRieszDecomposition E) : HasLatticeDualCone E
```

**`VectorLattice.hasLatticeDualCone`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L196).

> **Riesz–Kantorovich**: the positive functionals on a real vector lattice form a lattice.

```lean
lemma VectorLattice.hasLatticeDualCone (E : Type*) [AddCommGroup E] [Lattice E]
    [IsOrderedAddMonoid E] [Module ℝ E] [PosSMulMono ℝ E] : HasLatticeDualCone E
```

## C. Riesz decomposition of positive functionals

**`HasLatticeDualCone.exists_add_eq_of_le_add`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L216).

> **Riesz decomposition**: a positive functional below `α + β` splits into pieces below `α`,
> resp. `β`.

```lean
lemma exists_add_eq_of_le_add {θ α β : E →ₚ[ℝ] ℝ} (h : θ ≤ α + β) :
    ∃ θ₁ θ₂, θ₁ ≤ α ∧ θ₂ ≤ β ∧ θ = θ₁ + θ₂
```

**`HasLatticeDualCone.exists_refinement`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L237).

> **Riesz refinement**: a finite family of positive functionals summing to `α + β` splits into
> two families summing to `α`, resp. `β`.

```lean
lemma exists_refinement {m : ℕ} (ψ : Fin m → E →ₚ[ℝ] ℝ) {α β : E →ₚ[ℝ] ℝ}
    (h : ∑ i, ψ i = α + β) : ∃ ψ₁ ψ₂ : Fin m → E →ₚ[ℝ] ℝ,
      (∀ i, ψ i = ψ₁ i + ψ₂ i) ∧ ∑ i, ψ₁ i = α ∧ ∑ i, ψ₂ i = β
```

## D. Finite refinement of positive functionals

**`PositiveLinearMap.HasRefinement`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L268).

> Positive functionals have finite refinement when any two finite families with the same sum
> are the row and column sums of a common table of positive functionals.

```lean
def HasRefinement : Prop
```

**`PositiveLinearMap.HasLatticeDualCone.hasRefinement`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L275).

> A lattice dual cone gives finite refinement of positive functionals.

```lean
lemma HasLatticeDualCone.hasRefinement [IsDirectedOrder E] (hE : HasLatticeDualCone E) :
    HasRefinement E
```

**`PositiveLinearMap.HasRefinement.exists_table`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean#L298).

> Finite refinement, indexed by arbitrary finite types.

```lean
lemma HasRefinement.exists_table (hE : HasRefinement E) {I K : Type*} [Fintype I] [Fintype K]
    (α : I → E →ₚ[ℝ] ℝ) (β : K → E →ₚ[ℝ] ℝ) (h : ∑ i, α i = ∑ j, β j) :
    ∃ γ : I → K → E →ₚ[ℝ] ℝ, (∀ i, ∑ j, γ i j = α i) ∧ ∀ j, ∑ i, γ i j = β j
```

## Depends on

- [Positive functionals](positivedual-basic.md)

## Proof depends on

- [Vector lattices](vectorlattice.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/RieszKantorovich.lean)
