---
declaration: theorem
origin: cited
lean: FroehlichSpencer.BKT.Provider.existsUnique_tendsto_planeRotatorTwoPoint, FroehlichSpencer.BKT.Provider.existsUnique_tendsto_clockTwoPoint, FroehlichSpencer.BKT.planeRotator_powerLaw_lower_bound, FroehlichSpencer.BKT.planeRotator_kosterlitzThouless_transition, FroehlichSpencer.BKT.clock_phase_diagram, FroehlichSpencer.BKT.clock_disorder_lowerBound, FroehlichSpencer.BKT.freeVillain_disorderLimit_upper_bound, FroehlichSpencer.BKT.integerGFF_delocalization
statement: formalized
proof: formalized
---

# Frohlich-Spencer

*Classical theorems of Fröhlich and Spencer, formalized in Lean 4*

[scottnarmstrong/Frohlich-Spencer](https://github.com/scottnarmstrong/Frohlich-Spencer) at commit [e01623b7](https://github.com/scottnarmstrong/Frohlich-Spencer/tree/e01623b7347c272eac9480f04743f38b8d0df223), 2026-10-11.

> A **Lean 4 / Mathlib** formalization of three papers of J. Fröhlich and T. Spencer on phase transitions in lattice systems with an abelian symmetry and on localization: the Kosterlitz–Thouless transition (1981), massless phases of lattice gauge theories and spin systems (1982), and the absence of diffusion in the Anderson model (1983). The two-dimensional multiscale analysis follows the finite-volume presentation of Kharash and Peled.

*Quoted from [README.md](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/README.md), Apache-2.0.*

## Depends on

- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Exponential](../../special-functions/exponential.md)
- [Isogeny volcanoes](../../../../../atlas/algebra-number-theory/algebraic-geometry/elliptic-curves/isogeny-volcanoes.md)
- [Logarithm](../../special-functions/logarithm.md)

## Proof depends on

- [Mean of product of independent random variables](../../../probability-theory/random-variables-and-their-laws/mean-of-product-of-independent-random-variables.md)
- [Gershgorin circle theorem](../../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/gershgorin-circle-theorem.md)
- [Inverse hyperbolic trigonometric functions](../../special-functions/inverse-hyperbolic-trigonometric-functions.md)
- [Bolzano-Weierstrass theorem (Topology of R)](../../../../undergraduate/single-variable-real-analysis/topology-of-r/bolzano-weierstrass-theorem.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Poisson’s formula](../../../../undergraduate/distribution-calculus/applications/poissons-formula.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Characteristic function](../../../probability-theory/definitions-in-probability-theory/characteristic-function.md)

## Main results

Its Lean names are 8 of the 31 theorems its README names in code:

- [`FroehlichSpencer.BKT.Provider.existsUnique_tendsto_planeRotatorTwoPoint`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Provider/PlaneRotatorLimitWellDefined.lean#L32) (theorem)
- [`FroehlichSpencer.BKT.Provider.existsUnique_tendsto_clockTwoPoint`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Provider/ClockLimitWellDefined.lean#L31) (theorem)
- [`FroehlichSpencer.BKT.planeRotator_powerLaw_lower_bound`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/PlaneRotatorPowerLaw.lean#L34) (theorem)
- [`FroehlichSpencer.BKT.planeRotator_kosterlitzThouless_transition`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/PlaneRotatorTransition.lean#L30) (theorem)
- [`FroehlichSpencer.BKT.clock_phase_diagram`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/ClockPhaseDiagram.lean#L38) (theorem)
- [`FroehlichSpencer.BKT.clock_disorder_lowerBound`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/ClockDisorderLowerBound.lean#L28) (theorem)
- [`FroehlichSpencer.BKT.freeVillain_disorderLimit_upper_bound`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/FreeVillainTheoremD.lean#L29) (theorem)
- [`FroehlichSpencer.BKT.integerGFF_delocalization`](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/FroehlichSpencer/BKT/Surface/IntegerGFFDelocalization.lean#L42) (theorem)

No file its headlines import, directly or not (540 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 1,667 .lean files; its Lean libraries `FroehlichSpencer`, `comparators` hold 1,667, declaring 13,928 names, with `sorry` in 4 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/Frohlich-Spencer/blob/e01623b7347c272eac9480f04743f38b8d0df223/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 740 of 1289 are in Analysis, 2.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (740 of 1289 imports, 2.1×), General algebra (134 of 1289 imports, 0.3×). *Proof depends on* lists 8 of the 99 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [scottnarmstrong/Frohlich-Spencer at e01623b7](https://github.com/scottnarmstrong/Frohlich-Spencer/tree/e01623b7347c272eac9480f04743f38b8d0df223)
