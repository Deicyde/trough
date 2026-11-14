---
declaration: module
origin: cited
lean: VectorLattice.posPart_le_of_le, VectorLattice.riesz_decomposition, VectorLattice.add_inf_le, VectorLattice.inf_add_of_inf_eq_zero, VectorLattice.inf_add_eq_zero, VectorLattice.inf_sum_eq_zero, VectorLattice.add_inf_le_of_inf_eq_zero, VectorLattice.inf_sum_of_pairwise
statement: formalized
proof: formalized
---

# Vector lattices

The module `PhyslibAlpha.Mathematics.Order.VectorLattice`, [PhyslibAlpha/Mathematics/Order/VectorLattice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean): 13 declarations, 13 with a docstring.

> Elementary arithmetic of infima in real vector lattices: Riesz decomposition and disjointness.

## i. Overview

> A real vector lattice is an ordered real vector space in which any two elements have a least upper
> bound. Two nonnegative elements are disjoint when their infimum is `0`. This file collects the
> elementary arithmetic of infima: the Riesz decomposition, the behaviour of infima under positive
> scalars, and how disjointness interacts with sums and with least upper bounds of sequences.

## ii. Key results

> - `VectorLattice.riesz_decomposition` : an element below a sum of two nonnegative elements splits
>   into two pieces, one below each summand.
> - `VectorLattice.smul_inf` : positive scalars distribute over infima.
> - `VectorLattice.inf_sum_of_pairwise` : infima distribute over sums of pairwise disjoint nonnegative
>   elements.
> - `VectorLattice.isLUB_inf` : infima distribute over least upper bounds of sequences.

## iv. References

> * None.

**`VectorLattice.posPart_le_of_le`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L53).

> The positive part of an element below a nonnegative element is below it.

```lean
lemma posPart_le_of_le {y z : G} (h : y ≤ z) (hz : 0 ≤ z) : y⁺ ≤ z
```

## A. Riesz decomposition and disjointness

**`VectorLattice.riesz_decomposition`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L62).

> **Riesz decomposition**: if `0 ≤ g ≤ f₁ + f₂` with `0 ≤ f₁, f₂`, then `g ⊓ f₁` and
> `g - g ⊓ f₁` split `g` into pieces between `0` and `f₁`, resp. `f₂`.

```lean
lemma riesz_decomposition {f₁ f₂ g : G} (h₁ : 0 ≤ f₁) (h₂ : 0 ≤ f₂) (hg0 : 0 ≤ g)
    (hg : g ≤ f₁ + f₂) :
    0 ≤ g ⊓ f₁ ∧ g ⊓ f₁ ≤ f₁ ∧ 0 ≤ g - g ⊓ f₁ ∧ g - g ⊓ f₁ ≤ f₂
```

**`VectorLattice.add_inf_le`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L71).

> The infimum of a sum of nonnegative elements with a nonnegative element is at most the sum of
> the infima.

```lean
lemma add_inf_le {h₁ h₂ c : G} (h₁0 : 0 ≤ h₁) (h₂0 : 0 ≤ h₂) (hc : 0 ≤ c) :
    (h₁ + h₂) ⊓ c ≤ h₁ ⊓ c + h₂ ⊓ c
```

**`VectorLattice.inf_add_of_inf_eq_zero`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L81).

> Disjoint nonnegative elements split every nonnegative element additively.

```lean
lemma inf_add_of_inf_eq_zero {x u v : G} (hx : 0 ≤ x) (hu : 0 ≤ u) (hv : 0 ≤ v) (h : u ⊓ v = 0) :
    x ⊓ (u + v) = x ⊓ u + x ⊓ v
```

**`VectorLattice.inf_add_eq_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L91).

> An element disjoint from two nonnegative elements is disjoint from their sum.

```lean
lemma inf_add_eq_zero {x u v : G} (hx : 0 ≤ x) (hu : 0 ≤ u) (hv : 0 ≤ v) (hxu : x ⊓ u = 0)
    (hxv : x ⊓ v = 0) : x ⊓ (u + v) = 0
```

**`VectorLattice.inf_sum_eq_zero`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L99).

> An element disjoint from every member of a finite family of nonnegative elements is disjoint
> from their sum.

```lean
lemma inf_sum_eq_zero {ι : Type*} (s : Finset ι) {x : G} (hx : 0 ≤ x) (u : ι → G)
    (hu : ∀ i ∈ s, 0 ≤ u i) (h : ∀ i ∈ s, x ⊓ u i = 0) : x ⊓ ∑ i ∈ s, u i = 0
```

**`VectorLattice.add_inf_le_of_inf_eq_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L114).

> A nonnegative element below `x + w`, where `w` is disjoint from `s`, meets `s` at most where
> `x` does.

```lean
lemma add_inf_le_of_inf_eq_zero {x w s : G} (hx : 0 ≤ x) (hw : 0 ≤ w) (hs : 0 ≤ s)
    (h : w ⊓ s = 0) : (x + w) ⊓ s ≤ x ⊓ s
```

**`VectorLattice.inf_sum_of_pairwise`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L121).

> A nonnegative element splits along a finite family of pairwise disjoint nonnegative
> elements.

```lean
lemma inf_sum_of_pairwise {κ : Type*} (t : Finset κ) {x : G} (hx : 0 ≤ x) (u : κ → G)
    (hu : ∀ i ∈ t, 0 ≤ u i) (hd : ∀ i ∈ t, ∀ j ∈ t, i ≠ j → u i ⊓ u j = 0) :
    x ⊓ ∑ i ∈ t, u i = ∑ i ∈ t, x ⊓ u i
```

**`VectorLattice.isLUB_inf`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L137).

> Infima distribute over least upper bounds of sequences.

```lean
lemma isLUB_inf {a : ℕ → G} {c : G} (ha : IsLUB (Set.range a) c) (b : G) :
    IsLUB (Set.range fun n => a n ⊓ b) (c ⊓ b)
```

## B. Positive scalars

**`VectorLattice.smul_inf`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L157).

> Positive scalars distribute over infima.

```lean
lemma smul_inf {c : ℝ} (hc : 0 ≤ c) (x y : G) : c • (x ⊓ y) = c • x ⊓ c • y
```

**`VectorLattice.inf_smul_eq_zero`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L167).

> Disjoint nonnegative elements stay disjoint after scaling one of them.

```lean
lemma inf_smul_eq_zero {g u : G} (hg : 0 ≤ g) (hu : 0 ≤ u) (h : g ⊓ u = 0) {a : ℝ} (ha : 0 ≤ a) :
    g ⊓ a • u = 0
```

**`VectorLattice.smul_inf_smul_eq_zero`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L176).

> Disjoint nonnegative elements stay disjoint after scaling both.

```lean
lemma smul_inf_smul_eq_zero {u v : G} (hu : 0 ≤ u) (hv : 0 ≤ v) (h : u ⊓ v = 0) {a b : ℝ}
    (ha : 0 ≤ a) (hb : 0 ≤ b) : a • u ⊓ b • v = 0
```

**`VectorLattice.isLUB_smul`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean#L184).

> Positive scalars preserve least upper bounds of sequences.

```lean
lemma isLUB_smul {a : ℕ → G} {c : G} (ha : IsLUB (Set.range a) c) {r : ℝ} (hr : 0 < r) :
    IsLUB (Set.range fun n => r • a n) (r • c)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Order/VectorLattice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/VectorLattice.lean)
