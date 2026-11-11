---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_over_hom_base_closedPoint_eq_of_isClosed_singleton, AlgebraicGeometry.Scheme.Pullback.eq_of_fst_eq_of_snd_eq_of_isIso_residueFieldMap, AlgebraicGeometry.exists_section_comp_eq_iff_factors_of_universallyClosed_of_valuationRing, AlgebraicGeometry.dense_setOf_exists_section_of_isAlgClosed, AlgebraicGeometry.ext_of_forall_comp_eq_of_isAlgClosed, AlgebraicGeometry.exists_comp_eq_of_surjective_of_locallyOfFiniteType_of_isAlgClosed
statement: formalized
proof: formalized
---

# Points and sections of schemes

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html).

## Closed points of finite-type schemes over algebraically closed fields

A closed point of a scheme of finite type over an algebraically
closed field lifts to a point over the base.

Formalized by `AlgebraicGeometry.exists_over_hom_base_closedPoint_eq_of_isClosed_singleton`, a theorem declared in [MathlibExt/AlgebraicGeometry/ClosedPoint.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/ClosedPoint.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#exists-over-hom-base-closed-point-eq-of).

## Pullback points determined by projections given a residue isomorphism

Two points of a pullback with the same first and second projections are
equal, when the residue field map at the second point's first projection is
an isomorphism.

Formalized by `AlgebraicGeometry.Scheme.Pullback.eq_of_fst_eq_of_snd_eq_of_isIso_residueFieldMap`, a theorem declared in [MathlibExt/AlgebraicGeometry/PullbackPoints.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PullbackPoints.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#eq-of-fst-eq-of-snd-eq-of-is-iso-residue).

## Valuative criterion for factoring sections through an open subscheme

A section over a valuation ring factors through a universally closed
open subscheme exactly when the generic point does.

Formalized by `AlgebraicGeometry.exists_section_comp_eq_iff_factors_of_universallyClosed_of_valuationRing`, a theorem declared in [MathlibExt/AlgebraicGeometry/Sections.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Sections.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#exists-section-comp-eq-iff-factors-of-un).

## Density of rational points over an algebraically closed field

Rational points over an algebraically closed field are dense.

Formalized by `AlgebraicGeometry.dense_setOf_exists_section_of_isAlgClosed`, a theorem declared in [MathlibExt/AlgebraicGeometry/Sections.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Sections.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#dense-set-of-exists-section-of-is-alg-cl).

## Morphisms are determined by their values on rational points

Two morphisms over an algebraically closed field agreeing on all
rational points are equal.

Formalized by `AlgebraicGeometry.ext_of_forall_comp_eq_of_isAlgClosed`, a theorem declared in [MathlibExt/AlgebraicGeometry/Sections.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Sections.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#ext-of-forall-comp-eq-of-is-alg-closed).

## Surjective morphisms of finite type lift rational points

A surjective morphism locally of finite type lifts rational points over
an algebraically closed field.

Formalized by `AlgebraicGeometry.exists_comp_eq_of_surjective_of_locallyOfFiniteType_of_isAlgClosed`, a theorem declared in [MathlibExt/AlgebraicGeometry/Sections.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Sections.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html#exists-comp-eq-of-surjective-of-locally).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Points and sections of schemes](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/schemes-and-morphisms/points-and-sections-of-schemes)
