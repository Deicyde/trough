---
declaration: module
origin: cited
lean: TimeAndSpace.schwartzSpacetimeEuclideanAction, TimeAndSpace.schwartzSpacetimeEuclideanAction_apply, TimeAndSpace.reflectedConjugate, TimeAndSpace.reflectedConjugate_apply, TimeAndSpace.reflectedConjugate_involutive, TimeAndSpace.PositiveTimeTestFunction, TimeAndSpace.bumpToSchwartz, TimeAndSpace.integral_bumpToSchwartz
statement: formalized
proof: formalized
---

# Schwartz test functions on time and space

The module `Physlib.SpaceAndTime.TimeAndSpace.TestFunctions.Schwartz`, [Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean): 9 declarations, 9 with a docstring.

> Euclidean symmetries, positive-time support, bumps and translations of Schwartz tests.

## i. Overview

> Schwartz functions on `TimeAndSpace d` are the test functions of Euclidean field theory.
> The full `EuclideanGroup (d + 1)` acts on them by pullback, transported through
> time-first Euclidean coordinates, so it includes transformations mixing time and space.
> The reflected conjugate combines complex conjugation with time reflection, and
> positive-time test functions are those supported strictly at positive time.
>
> Normalized smooth bumps are constructed in Euclidean coordinates and pulled back to
> `TimeAndSpace d`, keeping integral one.

## ii. Key results

> * `TimeAndSpace.schwartzSpacetimeEuclideanAction`: the full spacetime Euclidean group
>   `EuclideanGroup (d + 1)` acting on complex tests, as opposed to the spatial
>   `schwartzEuclideanAction`.
> * `TimeAndSpace.reflectedConjugate`: conjugation combined with Euclidean time reflection.
> * `TimeAndSpace.PositiveTimeTestFunction`: complex tests supported at positive time.
> * `TimeAndSpace.bumpToSchwartz`: a normalized bump as a real Schwartz test.

## iv. References

> * Glimm and Jaffe, *Quantum Physics*. [ref: glimm1987quantum]
> * Cherkis et al., *OSforGFF*. [ref: osforgff]

## A. Euclidean symmetries and positive time

**`TimeAndSpace.schwartzSpacetimeEuclideanAction`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L63).

> Pullback by a full Euclidean transformation, including rotations mixing time and space.

```lean
def schwartzSpacetimeEuclideanAction (g : EuclideanGroup (d + 1)) :
    𝓢(TimeAndSpace d, ℂ) →L[ℂ] 𝓢(TimeAndSpace d, ℂ)
```

**`TimeAndSpace.schwartzSpacetimeEuclideanAction_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L81).

> The full Euclidean pullback expressed in time-first coordinates.

```lean
lemma schwartzSpacetimeEuclideanAction_apply (g : EuclideanGroup (d + 1))
    (f : 𝓢(TimeAndSpace d, ℂ)) (x : TimeAndSpace d) :
    schwartzSpacetimeEuclideanAction g f x = f (TimeAndSpace.euclideanCoordinates.symm
      (EuclideanGroup.toAffineIsometryHom g⁻¹ (TimeAndSpace.euclideanCoordinates x)))
```

**`TimeAndSpace.reflectedConjugate`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L94).

> Complex conjugation after time reflection, `f ↦ (x ↦ conj (f (Θ x)))`,
> in any spatial dimension.

```lean
def reflectedConjugate (f : 𝓢(TimeAndSpace d, ℂ)) :
    𝓢(TimeAndSpace d, ℂ)
```

**`TimeAndSpace.reflectedConjugate_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L101).

> The reflected conjugate includes both time reflection and complex conjugation.

```lean
lemma reflectedConjugate_apply (f : 𝓢(TimeAndSpace d, ℂ))
    (x : TimeAndSpace d) :
    reflectedConjugate f x = starRingEnd ℂ (f (TimeAndSpace.timeReflection x))
```

**`TimeAndSpace.reflectedConjugate_involutive`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L107).

> Applying the reflected conjugation twice recovers the original test.

```lean
lemma reflectedConjugate_involutive (f : 𝓢(TimeAndSpace d, ℂ)) :
    reflectedConjugate (reflectedConjugate f) = f
```

**`TimeAndSpace.PositiveTimeTestFunction`**, an abbrev, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L116).

> Complex Schwartz functions whose topological support lies strictly at positive time.
> This uses the support convention of `OSforGFF` in any spatial dimension.

```lean
abbrev PositiveTimeTestFunction (d : ℕ)
```

## B. Bumps and translations

**`TimeAndSpace.bumpToSchwartz`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L122).

> Convert a smooth bump centered at zero to a real Schwartz test with integral one.

```lean
def bumpToSchwartz (φ : ContDiffBump (0 : EuclideanSpace ℝ (Fin (d + 1)))) :
    𝓢(TimeAndSpace d, ℝ)
```

**`TimeAndSpace.integral_bumpToSchwartz`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L129).

> The Euclidean bump retains integral one after transport to time and space coordinates.

```lean
lemma integral_bumpToSchwartz (φ : ContDiffBump (0 : EuclideanSpace ℝ (Fin (d + 1)))) :
    ∫ x, bumpToSchwartz φ x = 1
```

**`TimeAndSpace.translateSchwartz`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean#L137).

> Translate a complex Schwartz test by `a`, with value `f (x - a)` at `x`.

```lean
def translateSchwartz (f : 𝓢(TimeAndSpace d, ℂ))
    (a : TimeAndSpace d) : 𝓢(TimeAndSpace d, ℂ)
```

## Depends on

- [The inclusion of the Euclidean group into the affine automorphism group](../space/part-02/euclideangroup-affinegroup.md)
- [Functions and distributions on Time and Space d](basic.md)

## Sources

- [Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/TimeAndSpace/TestFunctions/Schwartz.lean)
