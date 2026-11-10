---
declaration: section
origin: cited
lean: IsLocalRing.isAlgClosed_residueField_of_normal, normal_local_domain_sepClosed_fractionField_isStrictlyHenselian, MulSemiringAction.inertia_eq_inertia_baseChange, MulSemiringAction.exists_etale_away_fixedPoints_inertia, IsIntegralClosure.isFilteredColimitOfEtale_localization_fixedPoints_inertia
statement: formalized
proof: formalized
---

# 58.12 Group actions and integral closure

Section 58.12 of the Stacks Project, [Tag 0BSN](https://stacks.math.columbia.edu/tag/0BSN). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BSP, a lemma

[Tag 0BSP](https://stacks.math.columbia.edu/tag/0BSP) in the Stacks Project.

**`IsLocalRing.isAlgClosed_residueField_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/ResidueFields.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/ResidueFields.lean#L101).

> The residue field at a nonzero prime ideal of a normal domain whose fraction field is
> separably closed is algebraically closed.

```lean
public theorem isAlgClosed_residueField_of_normal
    (A : Type*) [CommRing A] [IsDomain A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K] [IsSepClosed K]
    (hA : IsIntegrallyClosed A) (p : Ideal A) [p.IsPrime] (hp : p ≠ ⊥) :
    IsAlgClosed p.ResidueField
```

## Tag 0BSQ, a lemma

[Tag 0BSQ](https://stacks.math.columbia.edu/tag/0BSQ) in the Stacks Project.

Declarations registered for the tag:

- [`normal_local_domain_sepClosed_fractionField_isStrictlyHenselian`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Criteria.lean#L326), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/ResidueFields.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/ResidueFields.lean#L38) (StacksFrontier).

## Tag 0BSS, a lemma

[Tag 0BSS](https://stacks.math.columbia.edu/tag/0BSS) in the Stacks Project.

**`MulSemiringAction.inertia_eq_inertia_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/Inertia.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GroupActionsIntegral/Inertia.lean#L105). References: SGA 1 V (2.1), “special case”.

> The inertia group of an ideal is unchanged after arbitrary base change from the invariant
> subring, for any ideal of the base change lying above it.

```lean
public theorem inertia_eq_inertia_baseChange
    (q : Ideal R)
    (q' : Ideal (TensorProduct (FixedPoints.subring R G) A R))
    (hq' : q = q'.comap Algebra.TensorProduct.includeRight) :
    let := baseChangeMulSemiringAction (G := G) (R := R) (A := A)
    q.inertia G = q'.inertia G
```

## Tag 0BST, a lemma

[Tag 0BST](https://stacks.math.columbia.edu/tag/0BST) in the Stacks Project.

**`MulSemiringAction.exists_etale_away_fixedPoints_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/Inertia.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/Inertia.lean#L610).

> For a finite group acting on a ring, the inclusion of the invariant ring into the ring of
> invariants of the inertia subgroup at a prime `q` is étale at the prime below `q`.

```lean
public theorem exists_etale_away_fixedPoints_inertia (q : Ideal R) [q.IsPrime] :
    let I := q.inertia G
    let RG := FixedPoints.subring R G
    let RI := FixedPoints.subring R I
    letI : Algebra RG RI := (Subring.inclusion (by
      intro x hx g
      exact hx g)).toAlgebra
    ∃ g : RI, g ∉ q.comap RI.subtype ∧ Algebra.Etale RG (Localization.Away g)
```

## Tag 0BSU, a lemma

[Tag 0BSU](https://stacks.math.columbia.edu/tag/0BSU) in the Stacks Project.

**`IsIntegralClosure.isFilteredColimitOfEtale_localization_fixedPoints_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Invariant/InertiaIndEtale.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Invariant/InertiaIndEtale.lean#L512).

> **Stacks 0BSU.** Let `A` be a normal domain with fraction field `K`, let `L / K` be a
> possibly infinite Galois extension with group `G = Gal(L/K)`, and let `B` be the integral
> closure of `A` in `L`. For a prime `q` of `B` with inertia subgroup
> `I = {σ ∈ G | σ q = q and σ ≡ id modulo q}`, the localization of `B ^ I` at the prime below `q`
> is a filtered colimit of étale `A`-algebras.

```lean
public theorem isFilteredColimitOfEtale_localization_fixedPoints_inertia
    (q : Ideal (integralClosure A L)) (hq : q.IsPrime) :
    let C := FixedPoints.subalgebra A (integralClosure A L)
      (q.inertia Gal(L/K))
    let p := q.comap C.val
    IsFilteredColimitOfEtaleHom (A := Localization.AtPrime p)
      ((algebraMap C (Localization.AtPrime p)).comp (algebraMap A C))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.12, Tag 0BSN](https://stacks.math.columbia.edu/tag/0BSN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
