---
declaration: module
origin: cited
lean: bidualSubmodule, Bidual, Bidual.mk, Bidual.toSub, Bidual.mk_apply, Bidual.ext, Bidual.map_add, Bidual.map_nnsmul
statement: formalized
proof: formalized
---

# The bidual

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.Bidual`, [PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean): 36 declarations (7 instances with no name), 12 with a docstring.

> The bidual of an ordered vector space via positive functionals, and its monotone completeness.

## i. Overview

> An element of an ordered real vector space `E` assigns to every positive functional its value,
> additively and positively homogeneously, and dominated by the values of some element of `E`. The
> bidual consists of all such assignments. It contains `E` when the order is directed, and is
> ordered by comparing values on every positive functional. Positive functionals extend to the
> bidual by evaluation.
>
> The bidual is monotone complete: a bounded upward directed family of elements has a least upper
> bound, their pointwise supremum.

## ii. Key results

> - `Bidual E` : the bidual of `E`.
> - `Bidual.ofE` : an element of `E` as an element of the bidual.
> - `Bidual.eval` : a positive functional extended to the bidual.
> - `Bidual.isLUB_ciSup` : a bounded directed family in the bidual has its pointwise supremum as
>   least upper bound.

## iv. References

> * None.

## A. The bidual

**`bidualSubmodule`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L62).

> Functions on positive functionals that are additive, positively homogeneous, and dominated by
> an element of `E`.

```lean
def bidualSubmodule : Submodule ℝ ((E →ₚ[ℝ] ℝ) → ℝ)
```

**`Bidual`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L83).

> The bidual of `E`.

```lean
def Bidual : Type _
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L87).

```lean
instance : AddCommGroup (Bidual E)
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L89).

```lean
instance : Module ℝ (Bidual E)
```

**`Bidual.mk`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L92).

> The element of the bidual given by an additive, positively homogeneous, bounded function.

```lean
def mk (x : (E →ₚ[ℝ] ℝ) → ℝ) (h₁ : ∀ φ ψ, x (φ + ψ) = x φ + x ψ)
    (h₂ : ∀ (c : ℝ≥0) φ, x (c • φ) = c * x φ) (h₃ : ∃ f : E, ∀ φ, |x φ| ≤ φ f) :
    Bidual E
```

**`Bidual.toSub`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L98).

> An element of the bidual as an element of the submodule.

```lean
def toSub (x : Bidual E) : bidualSubmodule E
```

**An instance with no name**, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L100).

```lean
instance : CoeFun (Bidual E) fun _ => (E →ₚ[ℝ] ℝ) → ℝ
```

**`Bidual.mk_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L102).

```lean
lemma mk_apply (x : (E →ₚ[ℝ] ℝ) → ℝ) (h₁ h₂ h₃) (φ : E →ₚ[ℝ] ℝ) :
    mk x h₁ h₂ h₃ φ = x φ
```

**`Bidual.ext`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L106).

```lean
lemma ext {x y : Bidual E} (h : ∀ φ, x φ = y φ) : x = y
```

**`Bidual.map_add`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L109).

```lean
lemma map_add (x : Bidual E) (φ ψ : E →ₚ[ℝ] ℝ) : x (φ + ψ) = x φ + x ψ
```

**`Bidual.map_nnsmul`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L112).

```lean
lemma map_nnsmul (x : Bidual E) (c : ℝ≥0) (φ : E →ₚ[ℝ] ℝ) : x (c • φ) = c * x φ
```

**`Bidual.exists_bound`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L115).

```lean
lemma exists_bound (x : Bidual E) : ∃ f : E, ∀ φ, |x φ| ≤ φ f
```

**`Bidual.apply_nonneg_of_bound`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L119).

> A dominating element has nonnegative values on positive functionals.

```lean
lemma apply_nonneg_of_bound {x : Bidual E} {f : E} (hf : ∀ φ, |x φ| ≤ φ f)
    (φ : E →ₚ[ℝ] ℝ) : 0 ≤ φ f
```

**`Bidual.coe_add`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L123).

```lean
lemma coe_add (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : (x + y) φ = x φ + y φ
```

**`Bidual.coe_sub`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L124).

```lean
lemma coe_sub (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : (x - y) φ = x φ - y φ
```

**`Bidual.coe_neg`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L125).

```lean
lemma coe_neg (x : Bidual E) (φ : E →ₚ[ℝ] ℝ) : (-x) φ = -x φ
```

**`Bidual.coe_zero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L126).

```lean
lemma coe_zero (φ : E →ₚ[ℝ] ℝ) : (0 : Bidual E) φ = 0
```

**`Bidual.coe_smul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L127).

```lean
lemma coe_smul (c : ℝ) (x : Bidual E) (φ : E →ₚ[ℝ] ℝ) : (c • x) φ = c * x φ
```

**`Bidual.map_zero`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L129).

```lean
lemma map_zero (x : Bidual E) : x 0 = 0
```

**`Bidual.map_sum`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L134).

```lean
lemma map_sum {ι : Type*} (x : Bidual E) (s : Finset ι) (φ : ι → E →ₚ[ℝ] ℝ) :
    x (∑ i ∈ s, φ i) = ∑ i ∈ s, x (φ i)
```

## B. Order

**An instance with no name**, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L144).

> An element of the bidual is nonnegative when it is nonnegative on every positive functional.

```lean
instance : PartialOrder (Bidual E)
```

**`Bidual.le_def`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L147).

```lean
lemma le_def {x y : Bidual E} : x ≤ y ↔ ∀ φ, x φ ≤ y φ
```

**An instance with no name**, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L150).

```lean
instance : IsOrderedAddMonoid (Bidual E)
```

**An instance with no name**, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L153).

```lean
instance : PosSMulMono ℝ (Bidual E)
```

## C. Elements and positive functionals

**`Bidual.ofE`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L163).

> An element of `E` as an element of the bidual: its value on each positive functional.

```lean
def ofE : E →ₗ[ℝ] Bidual E
```

**`Bidual.ofE_apply`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L173).

```lean
lemma ofE_apply (A : E) (φ : E →ₚ[ℝ] ℝ) : ofE A φ = φ A
```

**`Bidual.ofE_mono`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L175).

```lean
lemma ofE_mono {A B : E} (h : A ≤ B) : ofE A ≤ ofE B
```

**An instance with no name**, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L179).

> The bidual of a directed space is directed: `ofE (f + g)` lies above `x` and `y` when `f`
> dominates `x` and `g` dominates `y`.

```lean
instance : IsDirectedOrder (Bidual E)
```

**`Bidual.eval`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L192).

> A positive functional extended to the bidual by evaluation.

```lean
def eval (φ : E →ₚ[ℝ] ℝ) : Bidual E →ₚ[ℝ] ℝ
```

**`Bidual.eval_apply`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L196).

```lean
lemma eval_apply (φ : E →ₚ[ℝ] ℝ) (x : Bidual E) : eval φ x = x φ
```

**`Bidual.eval_ofE`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L198).

```lean
lemma eval_ofE (φ : E →ₚ[ℝ] ℝ) (A : E) : eval φ (ofE A) = φ A
```

**`Bidual.eval_mono`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L201).

> Extension to the bidual preserves the order of positive functionals.

```lean
lemma eval_mono {φ ψ : E →ₚ[ℝ] ℝ} (h : φ ≤ ψ) : eval φ ≤ eval ψ
```

## D. Monotone completeness

**`Bidual.bddAbove_apply`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L216).

```lean
lemma bddAbove_apply (φ : E →ₚ[ℝ] ℝ) : BddAbove (Set.range fun i => x i φ)
```

**`Bidual.ciSup`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L220).

> The pointwise supremum of a bounded directed family.

```lean
noncomputable def ciSup : Bidual E
```

**`Bidual.ciSup_apply`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L240).

```lean
lemma ciSup_apply (φ : E →ₚ[ℝ] ℝ) : ciSup hx hb φ = ⨆ i, x i φ
```

**`Bidual.isLUB_ciSup`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean#L244).

> **Monotone completeness**: a bounded directed family in the bidual has its pointwise supremum
> as least upper bound.

```lean
lemma isLUB_ciSup : IsLUB (Set.range x) (ciSup hx hb)
```

## Depends on

- [Positive functionals](positivedual-basic.md)

## Proof depends on

- [Elementary real bounds](../../part-01/analysis/realbounds.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Bidual.lean)
