---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.scalarPotential
statement: formalized
proof: formalized
---

# The Scalar Potential

The module `Physlib.Electromagnetism.TemperedDistributional.ScalarPotential`, [Physlib/Electromagnetism/TemperedDistributional/ScalarPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ScalarPotential.lean): 1 declaration, 1 with a docstring.

## i. Overview

> The electromagnetic potential is given by
> `A = (1/c φ, \vec A)`
> where `φ` is the scalar potential and `\vec A` is the vector potential.
>
> In this module we define the scalar potential, and prove lemmas about it.
>
> Since `A` is relativistic it is a distribution of `SpaceTime d`, whilst
> the scalar potential is non-relativistic and is therefore a distribution of `Time` and `Space d`.

## ii. Key results

> - `TempDistElectromagneticPotential.scalarPotential` : The scalar potential from an
>   electromagnetic potential which is a distribution.

## iv. References

> * None.

## A. Scalar potential for distributions

**`Electromagnetism.TempDistElectromagneticPotential.scalarPotential`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ScalarPotential.lean#L61).

> The scalar potential of an electromagnetic potential which is a distribution.

```lean
noncomputable def scalarPotential {d} (c : SpeedOfLight) :
    TempDistElectromagneticPotential d →ₗ[ℝ]
    (Time × Space d) →d[ℝ] ℝ
```

## Depends on

- [The Electromagnetic Potential](basic.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/ScalarPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ScalarPotential.lean)
