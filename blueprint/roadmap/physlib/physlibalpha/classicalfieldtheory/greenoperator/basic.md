---
declaration: module
origin: cited
lean: LocalOperator.spacelikeCompactFields, LocalOperator.futureSupportedFields, LocalOperator.operator_mem_futureSupportedFields, LocalOperator.futureSupportedOperator, LocalOperator.spacelikeCompactSolution, LocalOperator.operator_mem_spacelikeCompactFields, LocalOperator.futureSupportedFields_le_spacelikeCompactFields, LocalOperator.pastSupportedFields_le_spacelikeCompactFields
statement: formalized
proof: formalized
---

# Green operators and causally supported fields

The module `PhyslibAlpha.ClassicalFieldTheory.GreenOperator.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean): 17 declarations, 17 with a docstring.

> Retarded and advanced Green operators of a local operator.

## i. Overview

> Retarded and advanced Green operators of a local operator. Fields with spacelike compact, future or
> past compact support.

## ii. Key results

> - `spacelikeCompactFields` : Admissible fields with support contained in the causal hull of a
>   compact set.
> - `futureSupportedFields` : Fields supported in the future of a compact set.
> - `futureSupportedOperator` : Restrict the field equation to fields supported to the future of
>   compact sets.
> - `spacelikeCompactSolution` : Spacelike-compact homogeneous solutions.
> - `spacelikeCompactOperator` : The field equation restricted to spacelike-compact admissible fields.
> - `RetardedGreenOperator` : A retarded two-sided inverse on compact sources with future causal
>   support.
> - `AdvancedGreenOperator` : An advanced two-sided inverse on compact sources with past causal
>   support.
> - `GreenOperators` : A pair of causal Green inverses for the same field equation.

## iv. References

> None.

## A. Linear field equations and compact sources

> - `spacelikeCompactFields` : Admissible fields with support contained in the causal hull of a
>   compact set.
> - `futureSupportedFields` : Fields supported in the future of a compact set.
> - `futureSupportedOperator` : Restrict the field equation to fields supported to the future of
>   compact sets.
> - `spacelikeCompactSolution` : Spacelike-compact homogeneous solutions.
> - `spacelikeCompactOperator` : The field equation restricted to spacelike-compact admissible fields.
>
> Lemmas: `operator_mem_futureSupportedFields`, `operator_mem_spacelikeCompactFields`,
> `futureSupportedFields_le_spacelikeCompactFields`, `pastSupportedFields_le_spacelikeCompactFields`.

## B. Retarded and advanced Green operators

> - `RetardedGreenOperator` : A retarded two-sided inverse on compact sources with future causal
>   support.
> - `AdvancedGreenOperator` : An advanced two-sided inverse on compact sources with past causal
>   support.
> - `GreenOperators` : A pair of causal Green inverses for the same field equation.
> - `reverse` : Reverse time orientation and exchange the Green operators.

## C. Past-compact and future-compact support

> - `pastCompactFields` : The full past-compact admissible source and field space.
> - `pastCompactOperator` : The field equation restricted to the full past-compact support class.
>
> Lemmas: `operator_mem_pastCompactFields`, `futureSupportedFields_le_pastCompactFields`.

**`LocalOperator.spacelikeCompactFields`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L92).

> Admissible fields with support contained in the causal hull of a compact set.

```lean
def spacelikeCompactFields (_P : LocalOperator S) (C : CausalRelation M) : Submodule 𝕜 S
```

**`LocalOperator.futureSupportedFields`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L111).

> Fields supported in the future of a compact set. This is a strictly specified support class;
> it is not identified with all past-compact fields without additional geometry.

```lean
def futureSupportedFields (_P : LocalOperator S) (C : CausalRelation M) : Submodule 𝕜 S
```

**`LocalOperator.operator_mem_futureSupportedFields`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L129).

> Locality preserves support in the causal future of a compact set.

```lean
lemma operator_mem_futureSupportedFields (C : CausalRelation M)
    {u : S} (hu : u ∈ P.futureSupportedFields C) :
    P.operator u ∈ P.futureSupportedFields C
```

**`LocalOperator.futureSupportedOperator`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L136).

> Restrict the field equation to fields supported to the future of compact sets.

```lean
def futureSupportedOperator (C : CausalRelation M) :
    P.futureSupportedFields C →ₗ[𝕜] P.futureSupportedFields C
```

**`LocalOperator.spacelikeCompactSolution`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L142).

> Spacelike-compact homogeneous solutions.

```lean
def spacelikeCompactSolution (C : CausalRelation M) : Submodule 𝕜 S
```

**`LocalOperator.operator_mem_spacelikeCompactFields`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L146).

> Locality preserves spacelike-compact support.

```lean
lemma operator_mem_spacelikeCompactFields (C : CausalRelation M)
    {u : S} (hu : u ∈ P.spacelikeCompactFields C) :
    P.operator u ∈ P.spacelikeCompactFields C
```

**`LocalOperator.futureSupportedFields_le_spacelikeCompactFields`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L152).

> One-sided compactly generated support is spacelike compact.

```lean
lemma futureSupportedFields_le_spacelikeCompactFields (C : CausalRelation M) :
    P.futureSupportedFields C ≤ P.spacelikeCompactFields C
```

**`LocalOperator.pastSupportedFields_le_spacelikeCompactFields`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L158).

> Past-supported compactly generated support is spacelike compact.

```lean
lemma pastSupportedFields_le_spacelikeCompactFields (C : CausalRelation M) :
    P.futureSupportedFields C.reverse ≤ P.spacelikeCompactFields C
```

**`LocalOperator.spacelikeCompactOperator`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L164).

> The field equation restricted to spacelike-compact admissible fields.

```lean
def spacelikeCompactOperator (C : CausalRelation M) :
    P.spacelikeCompactFields C →ₗ[𝕜] P.spacelikeCompactFields C
```

**`GreenOperator.RetardedGreenOperator`**, a structure, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L181).

> A retarded two-sided inverse on compact sources with future causal support.

```lean
structure RetardedGreenOperator (C : CausalRelation M) (P : LocalOperator S) where
  /-- Compact sources produce admissible fields without a compact support requirement. -/
  toLinearMap : P.compactSources →ₗ[𝕜] S
  /-- The response solves the prescribed sourced equation. -/
  solves : ∀ f, P.operator (toLinearMap f) = f.val
  /-- Compact fields are recovered from their equation of motion. -/
  comp_operator : ∀ f, toLinearMap (P.compactOperator f) = f.val
  /-- Retarded propagation is supported in the source's causal future. -/
  support : ∀ f, tsupport (toLinearMap f : M → V) ⊆
    C.causalFuture (tsupport (f.val : M → V))
```

**`GreenOperator.AdvancedGreenOperator`**, a structure, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L193).

> An advanced two-sided inverse on compact sources with past causal support.

```lean
structure AdvancedGreenOperator (C : CausalRelation M) (P : LocalOperator S) where
  /-- Compact sources produce unrestricted admissible fields. -/
  toLinearMap : P.compactSources →ₗ[𝕜] S
  /-- The response solves the prescribed sourced equation. -/
  solves : ∀ f, P.operator (toLinearMap f) = f.val
  /-- Compact fields are recovered from their equation of motion. -/
  comp_operator : ∀ f, toLinearMap (P.compactOperator f) = f.val
  /-- Advanced propagation is supported in the source's causal past. -/
  support : ∀ f, tsupport (toLinearMap f : M → V) ⊆
    C.causalPast (tsupport (f.val : M → V))
```

**`GreenOperator.GreenOperators`**, a structure, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L206).

> A pair of causal Green inverses for the same field equation.
> Formal-adjoint hypotheses and support extensions are not implicit in this bundle.

```lean
structure GreenOperators (C : CausalRelation M) (P : LocalOperator S) where
  /-- The retarded Green inverse. -/
  retarded : RetardedGreenOperator C P
  /-- The advanced Green inverse. -/
  advanced : AdvancedGreenOperator C P
```

**`GreenOperator.GreenOperators.reverse`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L225).

> Reverse time orientation and exchange the Green operators.

```lean
def reverse : GreenOperators C.reverse P
```

**`LocalOperator.pastCompactFields`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L241).

> The full past-compact admissible source and field space.

```lean
def pastCompactFields (_P : LocalOperator S) (C : CausalRelation M) : Submodule 𝕜 S
```

**`LocalOperator.operator_mem_pastCompactFields`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L255).

> Local field equations preserve past-compact support.

```lean
lemma operator_mem_pastCompactFields {u : S} (hu : u ∈ P.pastCompactFields C) :
    P.operator u ∈ P.pastCompactFields C
```

**`LocalOperator.pastCompactOperator`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L260).

> The field equation restricted to the full past-compact support class.

```lean
def pastCompactOperator : P.pastCompactFields C →ₗ[𝕜] P.pastCompactFields C
```

**`LocalOperator.futureSupportedFields_le_pastCompactFields`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean#L265).

> Support in the future of one compact set is included in the full past-compact class.

```lean
lemma futureSupportedFields_le_pastCompactFields (hC : C.HasCompactCausalDiamonds) :
    P.futureSupportedFields C ≤ P.pastCompactFields C
```

## Depends on

- [Linear operators that do not enlarge support](../../mathematics/part-01/analysis/localoperator.md)
- [Causal support geometry](../../mathematics/part-02/order/causalrelation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Basic.lean)
