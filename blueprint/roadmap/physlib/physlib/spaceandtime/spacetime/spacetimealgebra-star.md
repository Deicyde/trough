---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.coeff_star, SpaceTimeAlgebra.constantCoeff_star, SpaceTimeAlgebra.star_C, SpaceTimeAlgebra.star_X, SpaceTimeAlgebra.pderiv_star, SpaceTimeAlgebra.iteratedPDeriv_star
statement: formalized
proof: formalized
---

# Complex conjugation in the spacetime algebra

The module `Physlib.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Star`, [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean): 10 declarations (4 instances with no name), 6 with a docstring.

> The spacetime algebra is a star ring under complex conjugation of the Taylor coefficients.

## i. Overview

> The star of a series in the spacetime algebra conjugates each of its complex coefficients and
> fixes each coordinate variable `x^μ`. The Taylor coefficients of the complex conjugate of a smooth
> field are the conjugates of its Taylor coefficients, so if `f` records a field at the base point
> then `star f` records the conjugate field.
>
> Conjugation is an involution that respects sums and products. It conjugates complex scalars, fixes
> real scalars, and commutes with every iterated derivative `∂^s`.

## ii. Key results

> - `SpaceTimeAlgebra.coeff_star` : the coefficients of `star f` are the conjugates of those of `f`.
> - `SpaceTimeAlgebra.star_C` : conjugating a constant series conjugates the constant.
> - `SpaceTimeAlgebra.star_X` : the coordinate variables are fixed by conjugation.
> - `SpaceTimeAlgebra.pderiv_star` : conjugation commutes with formal partial derivatives.
> - `SpaceTimeAlgebra.iteratedPDeriv_star` : conjugation commutes with iterated derivatives.

## iv. References

> * None.

## A. Coefficientwise conjugation

> The star is the coefficient map `map (starRingEnd ℂ)`. Since `SpaceTimeAlgebra` is an
> abbreviation, these are instances on `MvPowerSeries (Fin 1 ⊕ Fin 3) ℂ`.

**An instance with no name**, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L64).

> The star of a series in the spacetime algebra conjugates each of its coefficients.

```lean
instance : Star SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.coeff_star`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L68).

```lean
lemma coeff_star (n : (Fin 1 ⊕ Fin 3) →₀ ℕ) (f : SpaceTimeAlgebra) :
    coeff n (star f) = star (coeff n f)
```

**`SpaceTimeAlgebra.constantCoeff_star`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L72).

```lean
lemma constantCoeff_star (f : SpaceTimeAlgebra) :
    constantCoeff (star f) = star (constantCoeff f)
```

### A.1. The star ring structure

> Since the spacetime algebra is commutative, a ring homomorphism that is an involution makes it a
> star ring.

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L85).

> The spacetime algebra is a star ring under coefficientwise conjugation.

```lean
instance : StarRing SpaceTimeAlgebra
```

### A.2. Constants and coordinates

**`SpaceTimeAlgebra.star_C`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L97).

```lean
lemma star_C (a : ℂ) : star (C a : SpaceTimeAlgebra) = C (star a)
```

**`SpaceTimeAlgebra.star_X`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L100).

```lean
lemma star_X (μ : Fin 1 ⊕ Fin 3) : star (X μ : SpaceTimeAlgebra) = X μ
```

### A.3. Real and complex scalars

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L109).

> Conjugation fixes real scalars, `star (r • f) = r • star f`.

```lean
instance : StarModule ℝ SpaceTimeAlgebra
```

**An instance with no name**, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L113).

> Conjugation conjugates complex scalars, `star (c • f) = star c • star f`.

```lean
instance : StarModule ℂ SpaceTimeAlgebra
```

## B. Formal partial derivatives

> The coefficient of `x^n` in `pderiv μ f` is the coefficient of `x^(n + single μ 1)` in `f` times
> the natural number `n μ + 1`, which conjugation fixes.

**`SpaceTimeAlgebra.pderiv_star`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L126).

> Conjugation commutes with formal partial derivatives.

```lean
lemma pderiv_star (μ : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) :
    pderiv μ (star f) = star (pderiv μ f)
```

**`SpaceTimeAlgebra.iteratedPDeriv_star`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean#L132).

> Conjugation commutes with iterated formal partial derivatives.

```lean
lemma iteratedPDeriv_star (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    iteratedPDeriv s (star f) = star (iteratedPDeriv s f)
```

## Depends on

- [The spacetime algebra](spacetimealgebra-basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Star.lean)
