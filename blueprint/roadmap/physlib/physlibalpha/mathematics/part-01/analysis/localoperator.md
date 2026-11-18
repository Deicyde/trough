---
declaration: module
origin: cited
lean: LocalOperator, compactFields, LocalOperator.compactSources, LocalOperator.operator_mem_compactSources, LocalOperator.compactOperator, LocalOperator.compactOperator_coe, LocalOperator.solutionSpace, LocalOperator.mem_solutionSpace
statement: formalized
proof: formalized
---

# Linear operators that do not enlarge support

The module `PhyslibAlpha.Mathematics.Analysis.LocalOperator`, [PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean): 14 declarations, 12 with a docstring.

> A linear operator on a space of functions with support contained in the support of the argument.

## i. Overview

> A linear operator on a space of functions with support contained in the support of the argument. It
> acts on compactly supported functions and has a kernel. Such operators agree at a point when their
> arguments agree near it.

## ii. Key results

> - `compactFields` : Compactly supported admissible fields form the source space of Green operators.
> - `compactSources` : The compact test-field space depends on the admissible fields rather than the
>   operator.
> - `compactOperator` : The restriction of the equation to compactly supported admissible fields.
> - `solutionSpace` : Homogeneous admissible fields are the kernel of the field operator.
> - `IsLocalFieldSpace` : Admissibility is local when a function locally agreeing with admissible
>   fields is admissible.
> - `FieldIntertwiner` : A local linear map that commutes with two field equations.
> - `compactMap` : Restrict the local intertwiner to compact test fields.

## iv. References

> None.

## A. Linear field equations and compact sources

> - `compactFields` : Compactly supported admissible fields form the source space of Green operators.
> - `compactSources` : The compact test-field space depends on the admissible fields rather than the
>   operator.
> - `compactOperator` : The restriction of the equation to compactly supported admissible fields.
> - `solutionSpace` : Homogeneous admissible fields are the kernel of the field operator.
>
> Lemmas: `operator_mem_compactSources`, `compactOperator_coe`, `mem_solutionSpace`.

## B. Local field equations and causal agreement

> - `IsLocalFieldSpace` : Admissibility is local when a function locally agreeing with admissible
>   fields is admissible.
>
> Lemmas: `notMem_tsupport_sub_iff_eventuallyEq`, `operator_eventuallyEq`,
> `operator_eq_of_eventuallyEq`.

## C. Differential constraints and Green responses

> - `FieldIntertwiner` : A local linear map that commutes with two field equations.
> - `compactMap` : Restrict the local intertwiner to compact test fields.

**`LocalOperator`**, a structure, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L83).

> A linear equation on admissible fields with the support locality of a differential operator.
> Smoothness is supplied by the admissible field submodule in each application.

```lean
structure LocalOperator (S : Submodule 𝕜 (M → V)) where
  /-- The field differential operator on admissible fields. -/
  operator : S →ₗ[𝕜] S
  /-- A local field equation cannot create support away from the field. -/
  support_operator : ∀ u : S, tsupport (operator u : M → V) ⊆ tsupport (u : M → V)
```

**`compactFields`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L90).

> Compactly supported admissible fields form the source space of Green operators.

```lean
def compactFields (S : Submodule 𝕜 (M → V)) : Submodule 𝕜 S
```

**`LocalOperator.compactSources`**, an abbrev, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L108).

> The compact test-field space depends on the admissible fields rather than the operator.

```lean
abbrev compactSources (_P : LocalOperator S) : Submodule 𝕜 S
```

**`LocalOperator.operator_mem_compactSources`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L111).

> The equation preserves compact sources by locality.

```lean
lemma operator_mem_compactSources (u : P.compactSources) :
    P.operator u.val ∈ P.compactSources
```

**`LocalOperator.compactOperator`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L116).

> The restriction of the equation to compactly supported admissible fields.

```lean
def compactOperator : P.compactSources →ₗ[𝕜] P.compactSources
```

**`LocalOperator.compactOperator_coe`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L121).

```lean
lemma compactOperator_coe (u : P.compactSources) :
    (P.compactOperator u).val = P.operator u.val
```

**`LocalOperator.solutionSpace`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L125).

> Homogeneous admissible fields are the kernel of the field operator.

```lean
def solutionSpace : Submodule 𝕜 S
```

**`LocalOperator.mem_solutionSpace`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L128).

```lean
lemma mem_solutionSpace (u : S) : u ∈ P.solutionSpace ↔ P.operator u = 0
```

**`IsLocalFieldSpace`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L138).

> Admissibility is local when a function locally agreeing with admissible fields is admissible.

```lean
def IsLocalFieldSpace (S : Submodule 𝕜 (M → V)) : Prop
```

**`notMem_tsupport_sub_iff_eventuallyEq`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L142).

> Vanishing support of a difference at a point is exactly equality of field germs.

```lean
lemma notMem_tsupport_sub_iff_eventuallyEq {f g : M → V} {x : M} :
    x ∉ tsupport (f - g) ↔ f =ᶠ[𝓝 x] g
```

**`LocalOperator.operator_eventuallyEq`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L158).

> A local field operator preserves equality of germs.

```lean
lemma operator_eventuallyEq {u v : S} {x : M}
    (h : (u : M → V) =ᶠ[𝓝 x] (v : M → V)) :
    (P.operator u : M → V) =ᶠ[𝓝 x] (P.operator v : M → V)
```

**`LocalOperator.operator_eq_of_eventuallyEq`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L169).

> Equality of field germs implies equality of their equations at the observation point.

```lean
lemma operator_eq_of_eventuallyEq {u v : S} {x : M}
    (h : (u : M → V) =ᶠ[𝓝 x] (v : M → V)) :
    (P.operator u : M → V) x = (P.operator v : M → V) x
```

**`FieldIntertwiner`**, a structure, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L183).

> A local linear map that commutes with two field equations.
> The two equations may act on different field types, as for divergence of a vector wave equation.

```lean
structure FieldIntertwiner (P : LocalOperator S) (R : LocalOperator T) where
  /-- The differential constraint or transformation of fields. -/
  toLinearMap : S →ₗ[𝕜] T
  /-- Differential constraints do not enlarge support. -/
  support : ∀ u, tsupport (toLinearMap u : M → W) ⊆ tsupport (u : M → V)
  /-- Apply the constraint before or after the corresponding field equation. -/
  commutes : ∀ u, R.operator (toLinearMap u) = toLinearMap (P.operator u)
```

**`FieldIntertwiner.compactMap`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean#L200).

> Restrict the local intertwiner to compact test fields.

```lean
def compactMap : P.compactSources →ₗ[𝕜] R.compactSources
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/LocalOperator.lean)
