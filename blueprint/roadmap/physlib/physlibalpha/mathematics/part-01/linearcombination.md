---
declaration: module
origin: cited
lean: Submodule.map_span_range, LinearMap.range_eq_span_range_basis, Submodule.mul_le_of_le_span_range, Submodule.mul_mul_le_of_le_span_range
statement: formalized
proof: formalized
---

# Finite linear combinations under a linear map

The module `PhyslibAlpha.Mathematics.LinearCombination`, [PhyslibAlpha/Mathematics/LinearCombination.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean): 4 declarations, 4 with a docstring.

## i. Overview

> A family `T : ι → B` of vectors of an `R`-module spans Mathlib's
> `Submodule.span R (Set.range T)`. The index type is arbitrary and may be empty. When it is
> finite, the elements of the span are exactly the combinations `∑ i, c i • T i`, for
> coefficients `c : ι → R` that need not be unique (`Submodule.mem_span_range_iff_exists_fun`).
> A linear map carries this span to the span of the images of the family
> (`Submodule.map_span_range`) (A).
>
> Spans are bounded through their members: the range of a linear map is the span of the images
> of a basis, and a product of submodules lying in spans of families lies in any submodule
> containing the products of their members (B).

## ii. Key results

> - `Submodule.map_span_range` : the image of the span of a family is the span of the images
> - `LinearMap.range_eq_span_range_basis` : the range of a linear map is the span of the images of
>   a basis
> - `Submodule.mul_le_of_le_span_range` : a product of submodules inside spans of families

## iv. References

> * None.

## A. The image of the span of a family

**`Submodule.map_span_range`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean#L52).

> The image of the span of a family is the span of the images.

```lean
lemma Submodule.map_span_range {R B B' : Type*} [Semiring R] [AddCommMonoid B] [Module R B]
    [AddCommMonoid B'] [Module R B'] {ι : Sort*} (f : B →ₗ[R] B') (T : ι → B) :
    (Submodule.span R (Set.range T)).map f = Submodule.span R (Set.range fun i => f (T i))
```

## B. Spans bounded through their members

**`LinearMap.range_eq_span_range_basis`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean#L64).

> The range of a linear map is the span of the images of a basis.

```lean
lemma LinearMap.range_eq_span_range_basis {ι R M N : Type*} [Semiring R] [AddCommMonoid M]
    [Module R M] [AddCommMonoid N] [Module R N] (b : Module.Basis ι R M) (f : M →ₗ[R] N) :
    LinearMap.range f = Submodule.span R (Set.range fun i => f (b i))
```

**`Submodule.mul_le_of_le_span_range`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean#L71).

> A product of two submodules, each inside the span of a family, lies in any submodule
> containing the products of the members of the two families.

```lean
lemma Submodule.mul_le_of_le_span_range {ι κ R A : Type*} [CommSemiring R] [Semiring A]
    [Algebra R A] {V V' X : Submodule R A} {a : ι → A} {b : κ → A}
    (hV : V ≤ Submodule.span R (Set.range a)) (hV' : V' ≤ Submodule.span R (Set.range b))
    (hX : ∀ i j, a i * b j ∈ X) : V * V' ≤ X
```

**`Submodule.mul_mul_le_of_le_span_range`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean#L81).

> The three-factor form of `Submodule.mul_le_of_le_span_range`.

```lean
lemma Submodule.mul_mul_le_of_le_span_range {ι κ ν R A : Type*} [CommSemiring R] [Semiring A]
    [Algebra R A] {V V' V'' X : Submodule R A} {a : ι → A} {b : κ → A} {c : ν → A}
    (hV : V ≤ Submodule.span R (Set.range a)) (hV' : V' ≤ Submodule.span R (Set.range b))
    (hV'' : V'' ≤ Submodule.span R (Set.range c)) (hX : ∀ i j k, a i * (b j * c k) ∈ X) :
    V * (V' * V'') ≤ X
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/LinearCombination.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/LinearCombination.lean)
