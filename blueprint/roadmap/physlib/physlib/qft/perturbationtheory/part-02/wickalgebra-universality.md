---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.universalLiftMap, FieldSpecification.WickAlgebra.universalLiftMap_ι, FieldSpecification.WickAlgebra.universalLift, FieldSpecification.WickAlgebra.universalLift_ι, FieldSpecification.WickAlgebra.universality
statement: formalized
proof: formalized
---

# Universality properties of WickAlgebra

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.Universality`, [Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean): 5 declarations, 3 with a docstring.

**`FieldSpecification.WickAlgebra.universalLiftMap`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean#L29).

> For a field specification, `𝓕`, given an algebra `A` and a function `f : 𝓕.CrAnFieldOp → A`
> such that the lift of `f` to `FreeAlgebra.lift ℂ f : FreeAlgebra ℂ 𝓕.CrAnFieldOp → A` is
> zero on the ideal defining `𝓕.WickAlgebra`, the corresponding map `𝓕.WickAlgebra → A`.

```lean
def universalLiftMap {A : Type} [Semiring A] [Algebra ℂ A] (f : 𝓕.CrAnFieldOp → A)
    (h1 : ∀ a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet, FreeAlgebra.lift ℂ f a = 0) :
    WickAlgebra 𝓕 → A
```

**`FieldSpecification.WickAlgebra.universalLiftMap_ι`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean#L41).

```lean
lemma universalLiftMap_ι {A : Type} [Semiring A] [Algebra ℂ A] (f : 𝓕.CrAnFieldOp → A)
    (h1 : ∀ a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet, FreeAlgebra.lift ℂ f a = 0) :
    universalLiftMap f h1 (ι a) = FreeAlgebra.lift ℂ f a
```

**`FieldSpecification.WickAlgebra.universalLift`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean#L50).

> For a field specification, `𝓕`, given an algebra `A` and a function `f : 𝓕.CrAnFieldOp → A`
> such that the lift of `f` to `FreeAlgebra.lift ℂ f : FreeAlgebra ℂ 𝓕.CrAnFieldOp → A` is
> zero on the ideal defining `𝓕.WickAlgebra`, the corresponding algebra map
> `𝓕.WickAlgebra → A`.

```lean
def universalLift {A : Type} [Semiring A] [Algebra ℂ A] (f : 𝓕.CrAnFieldOp → A)
    (h1 : ∀ a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet, FreeAlgebra.lift ℂ f a = 0) :
    WickAlgebra 𝓕 →ₐ[ℂ] A
```

**`FieldSpecification.WickAlgebra.universalLift_ι`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean#L75).

```lean
lemma universalLift_ι {A : Type} [Semiring A] [Algebra ℂ A] (f : 𝓕.CrAnFieldOp → A)
    (h1 : ∀ a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet, FreeAlgebra.lift ℂ f a = 0) :
    universalLift f h1 (ι a) = FreeAlgebra.lift ℂ f a
```

**`FieldSpecification.WickAlgebra.universality`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean#L87).

> For a field specification, `𝓕`, the algebra `𝓕.WickAlgebra` satisfies the following universal
> property. Let `f : 𝓕.CrAnFieldOp → A` be a function and `g : 𝓕.FieldOpFreeAlgebra →ₐ[ℂ] A`
> the universal lift of that function associated with the free algebra `𝓕.FieldOpFreeAlgebra`.
> If `g` is zero on the ideal defining `𝓕.WickAlgebra`, then there exists
> algebra map `g' : WickAlgebra 𝓕 →ₐ[ℂ] A` such that `g' ∘ ι = g`, and furthermore this
> algebra map is unique.

```lean
lemma universality {A : Type} [Semiring A] [Algebra ℂ A] (f : 𝓕.CrAnFieldOp → A)
    (h1 : ∀ a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet, FreeAlgebra.lift ℂ f a = 0) :
    ∃! g : WickAlgebra 𝓕 →ₐ[ℂ] A, g ∘ ι = FreeAlgebra.lift ℂ f
```

## Depends on

- [The Wick Algebra](wickalgebra-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Universality.lean)
