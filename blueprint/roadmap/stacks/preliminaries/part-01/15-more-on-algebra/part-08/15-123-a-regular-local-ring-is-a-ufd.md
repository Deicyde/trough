---
declaration: section
origin: cited
lean: IsRegularLocalRing.pic_subsingleton_localization_away, IsRegularLocalRing.uniqueFactorizationMonoid, ValuationRing.subsingleton_pic_genericFibre_of_isRegular_specialFibre
statement: formalized
proof: formalized
---

# 15.123 A regular local ring is a UFD

Section 15.123 of the Stacks Project, [Tag 0FJH](https://stacks.math.columbia.edu/tag/0FJH). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AFZ, a lemma

[Tag 0AFZ](https://stacks.math.columbia.edu/tag/0AFZ) in the Stacks Project.

**`IsRegularLocalRing.pic_subsingleton_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/UniqueFactorization.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/UniqueFactorization.lean#L306).

> **Stacks 0AFZ.** The Picard group of the localization of a regular local ring at an
> element is trivial.

```lean
public theorem pic_subsingleton_localization_away
    (R : Type u) [CommRing R] [IsRegularLocalRing R] (f : R) :
    Subsingleton (CommRing.Pic (Localization.Away f))
```

## Tag 0AG0, a lemma

[Tag 0AG0](https://stacks.math.columbia.edu/tag/0AG0) in the Stacks Project.

**`IsRegularLocalRing.uniqueFactorizationMonoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/UniqueFactorization.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/UniqueFactorization.lean#L550). References: SGA 2 XI (3.13); SGA 6 X (7.8), “more general”; SGA 7 VIII (6.5.1), “special case”.

> **Stacks 0AG0.** A regular local ring is a unique factorization domain.

```lean
public theorem uniqueFactorizationMonoid
    (R : Type u) [CommRing R] [IsRegularLocalRing R] :
    UniqueFactorizationMonoid R
```

## Tag 0DLQ, a lemma

[Tag 0DLQ](https://stacks.math.columbia.edu/tag/0DLQ) in the Stacks Project.

**`ValuationRing.subsingleton_pic_genericFibre_of_isRegular_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/PicardGenericFibre.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/PicardGenericFibre.lean#L297). References: SGA 6 X (7.8), “special case”.

> **Stacks 0DLQ.** Let `R` be a valuation ring with fraction field `K`, and let `A` be a
> flat local `R`-algebra, essentially of finite type, whose special fibre is regular. Then the
> Picard group of the generic fibre is trivial.

```lean
public theorem subsingleton_pic_genericFibre_of_isRegular_specialFibre
    {R : Type u} {A : Type v} {K : Type w}
    [CommRing R] [IsDomain R] [ValuationRing R]
    [CommRing A] [IsLocalRing A] [Algebra R A] [IsLocalHom (algebraMap R A)]
    [Module.Flat R A] [Algebra.EssFiniteType R A]
    [Field K] [Algebra R K] [IsFractionRing R K]
    [IsRegularRing (A ⊗[R] (IsLocalRing.ResidueField R))] :
    Subsingleton (CommRing.Pic (A ⊗[R] K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.123, Tag 0FJH](https://stacks.math.columbia.edu/tag/0FJH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
