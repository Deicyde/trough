---
declaration: module
origin: cited
lean: unitary.conjugationLinearMap, unitary.coe_conjugationLinearMap, unitary.conjugationLinearMap_conjugationLinearMap, unitary.conjugationLinearMap_one, unitary.conjugationLinearMap_star_conjugationLinearMap, unitary.conjugationLinearMap_conjugationLinearMap_star, unitary.conjugationChannel, unitary.coe_conjugationChannel
statement: formalized
proof: formalized
---

# Unitary conjugation as a symmetry

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.ConjugationSymmetry`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean): 17 declarations, 10 with a docstring.

> Conjugation by a unitary as a channel and a symmetry, and symmetry actions of representations.

## i. Overview

> A symmetry of a quantum system is usually implemented as `a ↦ u a u⋆` for a unitary `u`. Conjugation
> by a unitary maps self-adjoint elements to self-adjoint elements, preserves positivity and the unit,
> and is inverted by conjugation by `u⋆`. So it is a symmetry of the observables, and `u ↦ u (·) u⋆`
> is a group homomorphism from the unitaries to the symmetry group. Composing with a unitary
> representation of a group `G` gives a symmetry action of `G`.

## ii. Key results

> - `unitary.conjugationChannel` : conjugation by a unitary, as a channel.
> - `unitary.conjugationSymmetry` : conjugation by a unitary, as a symmetry.
> - `unitary.conjugationSymmetryHom` : the homomorphism from unitaries to symmetries.
> - `Unitary.Representation.toSymmetryHom` : the symmetry action of a unitary representation.

## iv. References

> * None.

## A. Conjugation as a linear map

**`unitary.conjugationLinearMap`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L56).

> The underlying `ℝ`-linear map of conjugation by a unitary `u`, `a ↦ u a u*`, restricted to
> self-adjoint elements. Lands back in `selfAdjoint A` by `IsSelfAdjoint.conjugate`.

```lean
def conjugationLinearMap (u : unitary A) : selfAdjoint A →ₗ[ℝ] selfAdjoint A
```

**`unitary.coe_conjugationLinearMap`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L69).

```lean
lemma coe_conjugationLinearMap (u : unitary A) (a : selfAdjoint A) :
    (conjugationLinearMap u a : A) = (u : A) * (a : A) * star (u : A)
```

**`unitary.conjugationLinearMap_conjugationLinearMap`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L73).

> Conjugating by `v` and then by `u` is conjugating by `u * v`.

```lean
lemma conjugationLinearMap_conjugationLinearMap (u v : unitary A) (a : selfAdjoint A) :
    conjugationLinearMap u (conjugationLinearMap v a) = conjugationLinearMap (u * v) a
```

**`unitary.conjugationLinearMap_one`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L83).

> Conjugation by `1` does nothing.

```lean
lemma conjugationLinearMap_one (a : selfAdjoint A) :
    conjugationLinearMap (1 : unitary A) a = a
```

**`unitary.conjugationLinearMap_star_conjugationLinearMap`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L91).

> Conjugating by `u` then by `star u` is the identity: this is
> `conjugationLinearMap_conjugationLinearMap` specialized along `star u * u = 1`.

```lean
lemma conjugationLinearMap_star_conjugationLinearMap (u : unitary A) (a : selfAdjoint A) :
    conjugationLinearMap (star u) (conjugationLinearMap u a) = a
```

**`unitary.conjugationLinearMap_conjugationLinearMap_star`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L97).

> Conjugating by `star u` then by `u` is the identity: this is
> `conjugationLinearMap_conjugationLinearMap` specialized along `u * star u = 1`.

```lean
lemma conjugationLinearMap_conjugationLinearMap_star (u : unitary A) (a : selfAdjoint A) :
    conjugationLinearMap u (conjugationLinearMap (star u) a) = a
```

## B. Conjugation as a unital positive linear map

**`unitary.conjugationChannel`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L105).

> Conjugation by a unitary `u`, `a ↦ u a u*`, as a unital positive linear map (channel) on
> `selfAdjoint A`: positive by `star_right_conjugate_nonneg`, unital because `u * star u = 1`.

```lean
noncomputable def conjugationChannel (u : unitary A) : Channel (selfAdjoint A) (selfAdjoint A)
```

**`unitary.coe_conjugationChannel`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L114).

```lean
lemma coe_conjugationChannel (u : unitary A) (a : selfAdjoint A) :
    (conjugationChannel u a : A) = (u : A) * (a : A) * star (u : A)
```

**`unitary.conjugationChannel_comp_conjugationChannel`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L117).

```lean
lemma conjugationChannel_comp_conjugationChannel (u v : unitary A) :
    (conjugationChannel u).comp (conjugationChannel v) = conjugationChannel (u * v)
```

**`unitary.conjugationChannel_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L122).

```lean
lemma conjugationChannel_one : conjugationChannel (1 : unitary A) = .id ℝ (selfAdjoint A)
```

## C. Conjugation as a symmetry

**`unitary.conjugationSymmetry`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L130).

> Conjugation by a unitary `u`, as a symmetry of the observables, with inverse conjugation by
> `u⋆`.

```lean
noncomputable def conjugationSymmetry (u : unitary A) : Symmetry (selfAdjoint A)
```

**`unitary.val_conjugationSymmetry`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L138).

```lean
lemma val_conjugationSymmetry (u : unitary A) :
    (conjugationSymmetry u : Channel (selfAdjoint A) (selfAdjoint A)) = conjugationChannel u
```

**`unitary.conjugationSymmetryHom`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L142).

> Conjugation as a group homomorphism from the unitaries to the symmetries of the observables.

```lean
noncomputable def conjugationSymmetryHom : unitary A →* Symmetry (selfAdjoint A)
```

**`unitary.conjugationSymmetryHom_apply`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L151).

```lean
lemma conjugationSymmetryHom_apply (u : unitary A) :
    conjugationSymmetryHom u = conjugationSymmetry u
```

## D. Unitary representations induce symmetry actions

**`ProbabilisticTheory.Unitary.Representation.toSymmetryHom`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L165).

> The symmetry action `α_g(a) = U_g a U_g*` of a unitary representation `U : G →* unitary A`.

```lean
noncomputable def Representation.toSymmetryHom {G : Type*} [Group G] (U : G →* unitary A) :
    G →* Symmetry (selfAdjoint A)
```

**`ProbabilisticTheory.Unitary.Representation.toSymmetryHom_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L170).

```lean
lemma Representation.toSymmetryHom_apply {G : Type*} [Group G] (U : G →* unitary A) (g : G) :
    Representation.toSymmetryHom U g = unitary.conjugationSymmetry (U g)
```

**`ProbabilisticTheory.Unitary.Representation.toSymmetryHom_apply_coe`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean#L175).

> Unwinding `Representation.toSymmetryHom` on an element `a` recovers `α_g(a) = U_g a U_g*`
> literally.

```lean
lemma Representation.toSymmetryHom_apply_coe {G : Type*} [Group G] (U : G →* unitary A) (g : G)
    (a : selfAdjoint A) :
    ((Representation.toSymmetryHom U g).1 a : A) = (U g : A) * (a : A) * star (U g : A)
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Symmetries](../channel/symmetry.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/ConjugationSymmetry.lean)
