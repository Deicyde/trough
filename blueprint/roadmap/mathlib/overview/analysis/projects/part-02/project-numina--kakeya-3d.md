---
declaration: theorem
origin: cited
lean: KakeyaDimensionThree, Unconditional.KakeyaDimensionThree, stickyFrostmanHypothesis_of_pureWZ2
statement: formalized
---

# Kakeya in dimension three

[project-numina/kakeya-3d](https://github.com/project-numina/kakeya-3d) at commit [a26427e3](https://github.com/project-numina/kakeya-3d/tree/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3), 2026-09-09.

> This is a standalone Lean 4 formalization of the three-dimensional Kakeya argument following Guth, Wang and Zahl: every compact set in real Euclidean three-space containing a unit segment in every direction has Hausdorff dimension three. The statement is reached in two layers. `KakeyaDimensionThree` proves it from one explicit mathematical input, and `Unconditional.KakeyaDimensionThree` discharges that input, so the conjecture is obtained with no hypothesis, no `sorry` and no project axiom.

*Quoted from [README.md](https://github.com/project-numina/kakeya-3d/blob/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Affine space](../../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Markov inequality](../../../probability-theory/convergence-of-a-sequence-of-random-variables/markov-inequality.md)
- [Hausdorff dimension](../../measures-and-integral-calculus/part-01/hausdorff-dimension.md)
- [Affine subspace](../../../geometry/affine-and-euclidean-geometry/affine-subspace.md)
- [Hall's marriage theorem](../../../combinatorics/transversals/halls-marriage-theorem.md)
- [Angle](../../../geometry/affine-and-euclidean-geometry/angle.md)
- [Existence of orthonormal basis](../../../linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`KakeyaDimensionThree`](https://github.com/project-numina/kakeya-3d/blob/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3/Kakeya/DimensionThree/KakeyaConjecture.lean#L48) (theorem)
- [`Unconditional.KakeyaDimensionThree`](https://github.com/project-numina/kakeya-3d/blob/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3/Unconditional/KakeyaConjecture.lean#L22) (theorem)
- [`stickyFrostmanHypothesis_of_pureWZ2`](https://github.com/project-numina/kakeya-3d/blob/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3/Unconditional/StickyFrostman.lean#L21) (theorem)

Of the files its headlines import, directly or not, `Kakeya/DimensionThree/MainLemma1/QuotientAwareQV5W58.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.0-rc1, Mathlib at [1b0782d8](https://github.com/leanprover-community/mathlib4/tree/1b0782d8191b03e0001caac10e1601d17f2cd580).
- 905 .lean files; its Lean libraries `Kakeya`, `FinalCheck`, `Unconditional` hold 902, declaring 8,912 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/project-numina/kakeya-3d/blob/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3/LICENSE)).

## Builds on

- Mathlib, at [1b0782d8](https://github.com/leanprover-community/mathlib4/tree/1b0782d8191b03e0001caac10e1601d17f2cd580).

## Placement

Of its imports of Mathlib modules in an overview area, 178 of 363 are in Analysis, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (178 of 363 imports, 1.8×), Topology (37 of 363 imports, 1.4×), General algebra (59 of 363 imports, 0.5×). *Proof depends on* lists 8 of the 68 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [project-numina/kakeya-3d at a26427e3](https://github.com/project-numina/kakeya-3d/tree/a26427e3c2fcaf9f98694fbd0d4dd49e41dcf5e3)
