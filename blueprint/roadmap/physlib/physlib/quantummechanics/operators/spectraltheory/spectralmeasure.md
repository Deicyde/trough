---
declaration: module
origin: cited
lean: SpectralMeasure, SpectralMeasure.instCoeVectorMeasure, SpectralMeasure.instCoeFun, SpectralMeasure.isStarProjection, SpectralMeasure.univ, SpectralMeasure.comp_self, SpectralMeasure.comp_of_disjoint, SpectralMeasure.comp_eq_of_inter
statement: formalized
proof: formalized
---

# Spectral measures

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.SpectralMeasure`, [Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean): 10 declarations (1 instance with no name), 1 with a docstring.

## i. Overview

> A spectral measure `μS` on a measurable space `α` is a σ-additive function `Set α → H →L[ℂ] H`
> such that each set is mapped to a star projection on `H`, the empty set and non-measurable sets are
> mapped to zero, and `univ` is mapped to the identity.
> This is implemented as a structure extending `VectorMeasure α (H →L[ℂ] H)` with additional fields
> constraining `μS A` to be a star projection for each set `A` and `μS univ = 1`.
>
> For each `x : H` there is an associated measure `μₓ` given by `μₓ A = ‖μS A x‖² = ⟪x, μS A x⟫ ≤ 1`.

## ii. Key results

> - `SpectralMeasure` : A star projection-valued measure.
> - `comp_eq_of_inter` : For a spectral measure `μS` and measurable sets `A` and `B`,
>     the composition `μS A ∘ μS B = μS (A ∩ B)`.

## iv. References

> * None.

**An instance with no name**, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L48).

```lean
instance (H : Type*) [SeminormedAddCommGroup H] [InnerProductSpace ℂ H] :
    HasUniqueDiv (H →L[ℂ] H)
```

## A. Definition

**`SpectralMeasure`**, a structure, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L61).

> A \_spectral measure\_ on a measurable space `α` is a σ-additive function `Set α → H →L[ℂ] H`
> such that each set is mapped to a star projection on `H`, the empty set and non-measurable sets
> are mapped to zero, and `univ` is mapped to the identity.

```lean
structure SpectralMeasure
    (α : Type*) [MeasurableSpace α]
    (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    extends VectorMeasure α (H →L[ℂ] H) where
  isStarProjection' : ∀ A, IsStarProjection (measureOf' A)
  univ' : measureOf' univ = 1
```

**`SpectralMeasure.instCoeVectorMeasure`**, an instance, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L76).

```lean
instance instCoeVectorMeasure : Coe (SpectralMeasure α H) (VectorMeasure α (H →L[ℂ] H))
```

**`SpectralMeasure.instCoeFun`**, an instance, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L79).

```lean
instance instCoeFun : CoeFun (SpectralMeasure α H) fun _ ↦ Set α → H →L[ℂ] H
```

**`SpectralMeasure.isStarProjection`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L82).

```lean
lemma isStarProjection (A : Set α) : IsStarProjection (μS A)
```

**`SpectralMeasure.univ`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L85).

```lean
lemma univ : μS univ = 1
```

## B. Composition

**`SpectralMeasure.comp_self`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L92).

```lean
lemma comp_self (A : Set α) : μS A ∘L μS A = μS A
```

**`SpectralMeasure.comp_of_disjoint`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L94).

```lean
lemma comp_of_disjoint
    {A B : Set α} (h : Disjoint A B) (hA : MeasurableSet A) (hB : MeasurableSet B) :
    μS A ∘L μS B = 0
```

**`SpectralMeasure.comp_eq_of_inter`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L102).

```lean
lemma comp_eq_of_inter {A B : Set α} (hA : MeasurableSet A) (hB : MeasurableSet B) :
    μS A ∘L μS B = μS (A ∩ B)
```

**`SpectralMeasure.commute`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean#L111).

```lean
lemma commute (A B : Set α) : Commute (μS A) (μS B)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SpectralMeasure.lean)
