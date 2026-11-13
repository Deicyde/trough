---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.vectorPotential
statement: formalized
proof: formalized
---

# The vector Potential

The module `Physlib.Electromagnetism.TemperedDistributional.VectorPotential`, [Physlib/Electromagnetism/TemperedDistributional/VectorPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/VectorPotential.lean): 1 declaration, 1 with a docstring.

## i. Overview

> The electromagnetic potential is given by
> `A = (1/c φ, \vec A)`
> where `φ` is the scalar potential and `\vec A` is the vector potential.
>
> In this module we define the vector potential, and prove lemmas about it.
>
> Since `A` is relativistic it is a distribution of `SpaceTime d`, whilst
> the vector potential is non-relativistic and is therefore a distribution of `Time` and `Space d`.

## ii. Key results

> - `TempDistElectromagneticPotential.vectorPotential` : The vector potential from an
>   electromagnetic potential which is a distribution.

## iv. References

> * None.

## A. Vector potential for distributions

**`Electromagnetism.TempDistElectromagneticPotential.vectorPotential`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/VectorPotential.lean#L62).

> The vector potential of an electromagnetic potential which is a distribution.

```lean
noncomputable def vectorPotential {d} (c : SpeedOfLight) :
    TempDistElectromagneticPotential d →ₗ[ℝ]
    (Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)
```

## Depends on

- [The Electromagnetic Potential](basic.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/VectorPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/VectorPotential.lean)
