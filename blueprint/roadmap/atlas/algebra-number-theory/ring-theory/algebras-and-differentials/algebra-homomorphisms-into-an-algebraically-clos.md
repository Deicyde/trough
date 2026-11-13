---
declaration: section
origin: cited
lean: Algebra.eq_zero_of_forall_algHom_apply_eq_zero_of_isReduced_tensorProduct, Algebra.Etale.natCard_algHom_eq_finrank_of_isAlgClosed, AlgHom.natCard_eq_finrank_of_isReduced_of_isAlgClosed, Algebra.TensorProduct.eq_zero_of_forall_lift_apply_eq_zero, Algebra.exists_algHom_adjoin_of_linearRelations, Algebra.exists_algHom_adjoin_of_primeSubfield, RingHom.exists_comp_algebraMap_eq_and_ker_eq_of_isIntegral_of_isAlgClosed
statement: formalized
proof: formalized
---

# Algebra homomorphisms into an algebraically closed field

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html).

## Geometric points detect elements when the generic fiber is reduced

An element of a torsion-free algebra that vanishes under every algebra
homomorphism into an algebraically closed field is zero, provided the
tensor product with the fraction field is reduced and finite.

This is the Nullstellensatz-style statement that points detect functions:
it is used to show maps of schemes are determined by their values on
geometric points, to pass from vanishing on fibers to vanishing globally,
and to prove reducedness from pointwise vanishing.

Formalized by `Algebra.eq_zero_of_forall_algHom_apply_eq_zero_of_isReduced_tensorProduct`, a theorem declared in [MathlibExt/Algebra/Algebra/ZeroOfAlgHom.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Algebra/ZeroOfAlgHom.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#eq-zero-of-forall-alg-hom-apply-eq-zero).

## Counting algebra homomorphisms from an étale algebra

Over an algebraically closed field, the number of algebra homomorphisms
from an étale algebra to the base field equals its rank.

Formalized by `Algebra.Etale.natCard_algHom_eq_finrank_of_isAlgClosed`, a theorem declared in [MathlibExt/Algebra/Etale/AlgHomCount.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Etale/AlgHomCount.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#nat-card-alg-hom-eq-finrank-of-is-alg-cl).

## Counting algebra homomorphisms of a finite reduced algebra

A finite reduced algebra over an algebraically closed field has
`finrank` many algebra homomorphisms to the field.

Formalized by `AlgHom.natCard_eq_finrank_of_isReduced_of_isAlgClosed`, a theorem declared in [MathlibExt/Algebra/Algebra/AlgHomCount.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Algebra/AlgHomCount.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#nat-card-eq-finrank-of-is-reduced-of-is).

## A tensor vanishing at all pairs of algebraic points is zero

If the scalar-extended evaluation map is injective, a tensor vanishing at
all pairs of selected algebraic points is zero. The algebra and the point
index may be infinite; no closedness or perfection assumption is needed.

Formalized by `Algebra.TensorProduct.eq_zero_of_forall_lift_apply_eq_zero`, a theorem declared in [MathlibExt/Algebra/TensorProduct/PointSeparation.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/TensorProduct/PointSeparation.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#eq-zero-of-forall-lift-apply-eq-zero).

## Algebra maps from relation-preserving generator assignments

A unital, multiplicatively consistent assignment on generators extends to
an algebra homomorphism when it preserves every finite linear relation.

The index family need not be injective or finite; the target may have zero
divisors. This preserves the full statement of the source theorem
`exists_algHom_adjoin_range_apply_eq_of_forall_sum_smul_eq_zero_of_algebra`.

Formalized by `Algebra.exists_algHom_adjoin_of_linearRelations`, a theorem declared in [MathlibExt/RingTheory/Adjoin/LinearRelations.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Adjoin/LinearRelations.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#exists-alg-hom-adjoin-of-linear-relation).

## Extending a ring character via prime-subfield-valued linear forms

A ring character extends to the algebra generated by another ring image
when its kernel contains the first kernel and a separating family of linear
forms takes prime-subfield values on that image.

The ambient algebra may be noncommutative, and the separating family may be
infinite. The prime subfield is `⊥ : Subfield κ`, in any characteristic.
This is the source theorem
`exists_algHom_adjoin_range_apply_eq_of_forall_apply_mem_bot`.

Formalized by `Algebra.exists_algHom_adjoin_of_primeSubfield`, a theorem declared in [MathlibExt/RingTheory/Adjoin/LinearRelations.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Adjoin/LinearRelations.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#exists-alg-hom-adjoin-of-prime-subfield).

## Lifting maps to algebraically closed fields along integral extensions

A homomorphism from `R` to an algebraically closed field extends to an
integral extension `S` with any prescribed prime kernel lying over `ker χ`.

This is the key step for extending points of a scheme along integral
morphisms, for going-up arguments, and for lifting maps through integral
closures: the kernel control `RingHom.ker χ' = Q` says the lifted map has
exactly the prescribed residue behavior.

Formalized by `RingHom.exists_comp_algebraMap_eq_and_ker_eq_of_isIntegral_of_isAlgClosed`, a theorem declared in [MathlibExt/RingTheory/RingHom/IntegralAlgClosed.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RingHom/IntegralAlgClosed.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html#exists-comp-algebra-map-eq-and-ker-eq-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebra homomorphisms into an algebraically closed field](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/algebras-and-differentials/algebra-homomorphisms-into-an-algebraically-clos)
