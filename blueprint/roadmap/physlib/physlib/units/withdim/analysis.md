---
declaration: module
origin: cited
lean: WithDim.toValueAddEquiv, WithDim.instNormedAddCommGroup, WithDim.toValueLinearEquiv, WithDim.instNormedSpace, WithDim.norm_eq, WithDim.toValueLinearIsometryEquiv, WithDim.toValueLinearIsometryEquiv_apply, WithDim.toValueLinearIsometryEquiv_symm_apply
statement: formalized
proof: formalized
---

# A. Analysis of dimension-tagged quantities

The module `Physlib.Units.WithDim.Analysis`, [Physlib/Units/WithDim/Analysis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean): 13 declarations, 8 with a docstring.

> The numerical value of `WithDim d M` identifies it with `M`. We use that explicit
> identification to induce a norm on the existing additive group, not to replace
> its addition, natural/integer scalar multiplication, or the existing `NNReal` action.
>
> The norm measures a numerical representation in fixed units. It is not asserted to
> be invariant under a change of units. The coordinate equivalence is explicit: no
> coercion silently discards a dimension tag. No `Ring` or `Field` on a nontrivial
> physical dimension is introduced.
>
> `transport` and `transportLinearMap` lift a function and its derivative between tagged
> coordinates. They do not assert that the function is dimensionally correct. In particular,
> changing the units of model parameters is a separate question. `hasFDerivAt_transport`
> uses the existing calculus of continuous linear equivalences.

## A.1. Coordinates and the induced norm

**`WithDim.toValueAddEquiv`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L43).

> Forget the dimension tag by an explicit additive equivalence of numerical values.

```lean
def toValueAddEquiv (d : Dimension B) (M : Type) [AddCommMonoid M] :
    WithDim d M ≃+ M
```

**`WithDim.instNormedAddCommGroup`**, an instance, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L52).

> The existing additive group carries the norm of its numerical representation.

```lean
instance instNormedAddCommGroup (d : Dimension B) (M : Type) [NormedAddCommGroup M] :
    NormedAddCommGroup (WithDim d M)
```

**`WithDim.toValueLinearEquiv`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L58).

> The numerical-value coordinates are linear over dimensionless real scalars.

```lean
def toValueLinearEquiv (d : Dimension B) (M : Type) [AddCommMonoid M] [Module ℝ M] :
    WithDim d M ≃ₗ[ℝ] M
```

**`WithDim.instNormedSpace`**, an instance, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L68).

> The induced norm is compatible with the existing real scalar multiplication.

```lean
instance instNormedSpace (d : Dimension B) (M : Type) [NormedAddCommGroup M]
    [NormedSpace ℝ M] : NormedSpace ℝ (WithDim d M)
```

**`WithDim.norm_eq`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L73).

```lean
lemma norm_eq {d : Dimension B} {M : Type} [NormedAddCommGroup M] (x : WithDim d M) :
    ‖x‖ = ‖x.val‖
```

**`WithDim.toValueLinearIsometryEquiv`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L77).

> Numerical-value coordinates form a linear isometry for a fixed unit representation.

```lean
def toValueLinearIsometryEquiv (d : Dimension B) (M : Type) [NormedAddCommGroup M]
    [NormedSpace ℝ M] : WithDim d M ≃ₗᵢ[ℝ] M
```

**`WithDim.toValueLinearIsometryEquiv_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L82).

```lean
lemma toValueLinearIsometryEquiv_apply (d : Dimension B) (M : Type)
    [NormedAddCommGroup M] [NormedSpace ℝ M] (x : WithDim d M) :
    toValueLinearIsometryEquiv d M x = x.val
```

**`WithDim.toValueLinearIsometryEquiv_symm_apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L87).

```lean
lemma toValueLinearIsometryEquiv_symm_apply (d : Dimension B) (M : Type)
    [NormedAddCommGroup M] [NormedSpace ℝ M] (x : M) :
    (toValueLinearIsometryEquiv d M).symm x = (⟨x⟩ : WithDim d M)
```

## A.2. Transport of existing functions and derivatives

**`WithDim.transport`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L97).

> Express a numerical function in explicitly chosen input and output dimensions.
> This definition by itself makes no claim of dimensional correctness.

```lean
def transport {M N : Type} (d e : Dimension B) (f : M → N) :
    WithDim d M → WithDim e N
```

**`WithDim.transport_val`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L101).

```lean
lemma transport_val {M N : Type} (d e : Dimension B) (f : M → N) (x : WithDim d M) :
    (transport d e f x).val = f x.val
```

**`WithDim.transportLinearMap`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L105).

> Express a continuous linear map between tagged numerical coordinates.

```lean
def transportLinearMap {M N : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    [NormedAddCommGroup N] [NormedSpace ℝ N] (d e : Dimension B) (f : M →L[ℝ] N) :
    WithDim d M →L[ℝ] WithDim e N
```

**`WithDim.transportLinearMap_val`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L112).

```lean
lemma transportLinearMap_val {M N : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    [NormedAddCommGroup N] [NormedSpace ℝ N] (d e : Dimension B) (f : M →L[ℝ] N)
    (x : WithDim d M) : (transportLinearMap d e f x).val = f x.val
```

**`WithDim.hasFDerivAt_transport`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean#L117).

> Reuse a derivative in numerical coordinates for the corresponding tagged function.

```lean
lemma hasFDerivAt_transport {M N : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    [NormedAddCommGroup N] [NormedSpace ℝ N] (d e : Dimension B) {f : M → N}
    {f' : M →L[ℝ] N} {x : WithDim d M} (h : HasFDerivAt f f' x.val) :
    HasFDerivAt (transport d e f) (transportLinearMap d e f') x
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Analysis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Analysis.lean)
