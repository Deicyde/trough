---
declaration: module
origin: cited
lean: Minkowski.smoothFields, Minkowski.TestField, Minkowski.smoothFields_contDiff, Minkowski.smoothFields_isLocal, Minkowski.smoothDerivative, Minkowski.smoothDerivative_coe, Minkowski.smoothDerivative_support, Minkowski.smoothField_support_sum
statement: formalized
proof: formalized
---

# Smooth fields and distributions on spacetime

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.Fields`, [PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean): 12 declarations, 10 with a docstring.

> Smooth fields form a local space of functions on `SpaceTime d` with derivatives.

## i. Overview

> Smooth fields form a local space of functions on `SpaceTime d` with derivatives. Distribution fields
> are the distributions with values in a normed space.

## ii. Key results

> - `smoothFields` : Smooth spacetime fields with values in a fixed real vector space.
> - `TestField` : Smooth compactly supported test fields on Minkowski spacetime.
> - `smoothDerivative` : The existing spacetime derivative restricted to smooth fields.
> - `smoothFiberMap` : Apply a constant continuous linear transformation to each field value.
> - `DistributionField` : Distributional fields on all of Minkowski spacetime use Mathlib's native
>   continuous dual.
> - `testFunctionEquiv` : The existing compact smooth test fields are Mathlib test functions on the
>   whole spacetime.

## iv. References

> None.

## A. Smooth Minkowski fields

> - `smoothFields` : Smooth spacetime fields with values in a fixed real vector space.
> - `TestField` : Smooth compactly supported test fields on Minkowski spacetime.
> - `smoothDerivative` : The existing spacetime derivative restricted to smooth fields.
> - `smoothFiberMap` : Apply a constant continuous linear transformation to each field value.
>
> Lemmas: `smoothFields_contDiff`, `smoothFields_isLocal`, `smoothDerivative_coe`,
> `smoothDerivative_support`, `smoothField_support_sum`, `smoothFiberMap_derivative`.

## B. Minkowski test fields and distributions

> - `DistributionField` : Distributional fields on all of Minkowski spacetime use Mathlib's native
>   continuous dual.
> - `testFunctionEquiv` : The existing compact smooth test fields are Mathlib test functions on the
>   whole spacetime.

**`Minkowski.smoothFields`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L75).

> Smooth spacetime fields with values in a fixed real vector space.

```lean
def smoothFields (d : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] :
    Submodule ℝ (SpaceTime d → V)
```

**`Minkowski.TestField`**, an abbrev, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L87).

> Smooth compactly supported test fields on Minkowski spacetime.

```lean
abbrev TestField (d : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V]
```

**`Minkowski.smoothFields_contDiff`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L91).

> The regularity carried by an admissible smooth field.

```lean
lemma smoothFields_contDiff (u : smoothFields d V) : ContDiff ℝ ∞ u.val
```

**`Minkowski.smoothFields_isLocal`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L94).

> Smooth spacetime fields satisfy the local gluing hypothesis of the Green extension theorem.

```lean
lemma smoothFields_isLocal : IsLocalFieldSpace (smoothFields d V)
```

**`Minkowski.smoothDerivative`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L103).

> The existing spacetime derivative restricted to smooth fields.

```lean
def smoothDerivative (μ : Fin 1 ⊕ Fin d) : smoothFields d V →ₗ[ℝ] smoothFields d V
```

**`Minkowski.smoothDerivative_coe`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L114).

```lean
lemma smoothDerivative_coe (μ : Fin 1 ⊕ Fin d) (u : smoothFields d V) :
    (smoothDerivative μ u : SpaceTime d → V) = SpaceTime.deriv μ u.val
```

**`Minkowski.smoothDerivative_support`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L118).

> Spacetime differentiation is local in the support sense required by field equations.

```lean
lemma smoothDerivative_support (μ : Fin 1 ⊕ Fin d) (u : smoothFields d V) :
    tsupport (smoothDerivative μ u : SpaceTime d → V) ⊆ tsupport (u : SpaceTime d → V)
```

**`Minkowski.smoothField_support_sum`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L123).

```lean
lemma smoothField_support_sum {ι : Type*} (s : Finset ι)
    (f : ι → SpaceTime d → V) (K : Set (SpaceTime d))
    (hf : ∀ i ∈ s, tsupport (f i) ⊆ K) :
    tsupport (∑ i ∈ s, f i) ⊆ K
```

**`Minkowski.smoothFiberMap`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L137).

> Apply a constant continuous linear transformation to each field value.

```lean
def smoothFiberMap {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W]
    (L : V →L[ℝ] W) : smoothFields d V →ₗ[ℝ] smoothFields d W
```

**`Minkowski.smoothFiberMap_derivative`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L144).

> Constant fibre transformations commute with spacetime differentiation.

```lean
lemma smoothFiberMap_derivative {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W]
    (L : V →L[ℝ] W) (μ : Fin 1 ⊕ Fin d) (u : smoothFields d V) :
    smoothDerivative μ (smoothFiberMap L u) = smoothFiberMap L (smoothDerivative μ u)
```

**`Minkowski.DistributionField`**, an abbrev, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L155).

> Distributional fields on all of Minkowski spacetime use Mathlib's native continuous dual.

```lean
abbrev DistributionField (d : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V]
```

**`Minkowski.testFunctionEquiv`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean#L160).

> The existing compact smooth test fields are Mathlib test functions on the whole spacetime.
> The equivalence is algebraic. The LF topology lives on the Mathlib side.

```lean
def testFunctionEquiv : TestField d V ≃ₗ[ℝ]
    _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) V ⊤
```

## Depends on

- [Derivatives on SpaceTime](../../../physlib/spaceandtime/spacetime/derivatives.md)
- [Linear operators that do not enlarge support](../../mathematics/part-01/analysis/localoperator.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/Fields.lean)
