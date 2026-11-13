---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_of_isClosedImmersion_of_finrank_comp_eq, AlgebraicGeometry.IsClosedImmersion.exists_iso_hom_comp_eq_of_range_eq, AlgebraicGeometry.IsOpenImmersion.of_isClosedImmersion_of_flat_comp_of_etale, AlgebraicGeometry.IsClosedImmersion.of_isPullback, AlgebraicGeometry.Surjective.of_isPullback, AlgebraicGeometry.UniversallyClosed.of_isPullback, AlgebraicGeometry.IsSeparated.of_isPullback, AlgebraicGeometry.IsProper.of_isPullback
statement: formalized
proof: formalized
---

# Closed and open immersions

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html).

## Closed immersions of constant fibre rank are isomorphisms

A closed immersion between maps of constant fibre rank is an
isomorphism.

Formalized by `AlgebraicGeometry.isIso_of_isClosedImmersion_of_finrank_comp_eq`, a theorem declared in [MathlibExt/AlgebraicGeometry/ClosedImmersionIsIso.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/ClosedImmersionIsIso.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#is-iso-of-is-closed-immersion-of-finrank).

## Reduced closed immersions with equal range are isomorphic

Two reduced closed immersions with the same range are isomorphic over
the target.

Formalized by `AlgebraicGeometry.IsClosedImmersion.exists_iso_hom_comp_eq_of_range_eq`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#exists-iso-hom-comp-eq-of-range-eq).

## Closed immersions flat over the base of an étale map are open

A closed immersion whose composite with an étale map is flat and
locally of finite presentation is open.

Formalized by `AlgebraicGeometry.IsOpenImmersion.of_isClosedImmersion_of_flat_comp_of_etale`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-closed-immersion-of-flat-comp-of-e).

## Closed immersions are stable under base change

Closed immersions transfer along pullback squares.

Formalized by `AlgebraicGeometry.IsClosedImmersion.of_isPullback`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-pullback).

## Surjectivity is stable under base change

Surjectivity transfers along pullback squares.

Formalized by `AlgebraicGeometry.Surjective.of_isPullback`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-pullback-2).

## Universal closedness descends along surjective closed immersions

Universal closedness transfers along a pullback square whose base map is
a surjective closed immersion.

Formalized by `AlgebraicGeometry.UniversallyClosed.of_isPullback`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-pullback-3).

## Separatedness descends along surjective closed immersions

Separatedness transfers along a pullback square whose base map is a
surjective closed immersion.

Formalized by `AlgebraicGeometry.IsSeparated.of_isPullback`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-pullback-4).

## Properness descends along surjective closed immersions

Properness transfers along a pullback square whose base map is a
surjective closed immersion.

Formalized by `AlgebraicGeometry.IsProper.of_isPullback`, a theorem declared in [MathlibExt/AlgebraicGeometry/Immersions.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Immersions.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html#of-is-pullback-5).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closed and open immersions](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/schemes-and-morphisms/closed-and-open-immersions)
