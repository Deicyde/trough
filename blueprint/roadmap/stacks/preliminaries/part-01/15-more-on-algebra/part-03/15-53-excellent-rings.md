---
declaration: section
origin: cited
lean: IsQuasiExcellent, IsExcellent, isQuasiExcellent_and_isExcellent_of_essFiniteType, isExcellent_of_standard_classes_and_finiteType, isNagataRing_iff_formalFibers_geometricallyReduced, isNagataRing_of_isQuasiExcellent, isNormalRing_adicCompletion_maximalIdeal
statement: formalized
proof: formalized
---

# 15.53 Excellent rings

Section 15.53 of the Stacks Project, [Tag 07QS](https://stacks.math.columbia.edu/tag/07QS). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07QT, a definition

[Tag 07QT](https://stacks.math.columbia.edu/tag/07QT) in the Stacks Project.

**`IsQuasiExcellent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L173). The attribute's comment: “(1)”. References: EGA IV (7.8.2), “(ii), (iii)”.

> A commutative ring is quasi-excellent if it is Noetherian, a G-ring, and J-2.

```lean
public def IsQuasiExcellent (R : Type u) [CommRing R] : Prop
```

**`IsExcellent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L178). The attribute's comment: “(2)”. References: EGA IV (7.8.2).

> A commutative ring is excellent if it is quasi-excellent and universally catenary.

```lean
public def IsExcellent (R : Type u) [CommRing R] : Prop
```

## Tag 07QU, a lemma

[Tag 07QU](https://stacks.math.columbia.edu/tag/07QU) in the Stacks Project.

**`isQuasiExcellent_and_isExcellent_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L282). References: EGA IV (7.8.3), “more general”; EGA IV (7.8.4), “more general”.

> An algebra essentially of finite type over a quasi-excellent ring is quasi-excellent, and
> an algebra essentially of finite type over an excellent ring is excellent.

```lean
public theorem isQuasiExcellent_and_isExcellent_of_essFiniteType
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.EssFiniteType R S] :
    (IsQuasiExcellent R → IsQuasiExcellent S) ∧
      (IsExcellent R → IsExcellent S)
```

## Tag 07QW, a proposition

[Tag 07QW](https://stacks.math.columbia.edu/tag/07QW) in the Stacks Project.

**`isExcellent_of_standard_classes_and_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L386). References: EGA IV (7.8.3), “(iii), part of (ii)”; EGA IV (7.8.6), “(i), affine case”; EGA IV (6.12.6), “special case”; SGA 3 VIB (10.10), “more general”.

> **Stacks 07QW.** Fields, Noetherian complete local rings, the integers, and Dedekind domains
> whose fraction fields have characteristic zero are excellent; moreover, every finite-type
> algebra over an excellent ring is excellent.

```lean
public theorem isExcellent_of_standard_classes_and_finiteType :
    (∀ (K : Type u) [Field K], IsExcellent K) ∧
      (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
        [IsPrecomplete (IsLocalRing.maximalIdeal R) R], IsExcellent R) ∧
      IsExcellent ℤ ∧
      (∀ (R : Type u) [CommRing R] [IsDedekindDomain R] [CharZero (FractionRing R)],
        IsExcellent R) ∧
      (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
        [Algebra.FiniteType R S], IsExcellent R → IsExcellent S)
```

## Tag 0BJ0, a lemma

[Tag 0BJ0](https://stacks.math.columbia.edu/tag/0BJ0) in the Stacks Project.

**`isNagataRing_iff_formalFibers_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L480). References: EGA IV (7.6.4), “local case, a'')<=>b)”; EGA IV (7.7.3), “A local Noetherian”; EGA IV (7.7.4), “formal fibres clause”.

> **Stacks 0BJ0.** A Noetherian local ring is Nagata if and only if all its formal fibres are
> geometrically reduced.

```lean
public theorem isNagataRing_iff_formalFibers_geometricallyReduced
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A] :
    IsNagataRing A ↔
      ∀ q : PrimeSpectrum A,
        Algebra.IsGeometricallyReduced q.asIdeal.ResidueField
          (q.asIdeal.Fiber (AdicCompletion (maximalIdeal A) A))
```

## Tag 07QV, a lemma

[Tag 07QV](https://stacks.math.columbia.edu/tag/07QV) in the Stacks Project.

**`isNagataRing_of_isQuasiExcellent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Excellent/Basic.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Excellent/Basic.lean#L351). References: EGA IV (7.8.3), “more general”; EGA IV (7.8.4), “(iii)”.

> **Stacks 07QV.** A quasi-excellent commutative ring is a Nagata ring.

```lean
public theorem isNagataRing_of_isQuasiExcellent {R : Type u} [CommRing R]
    (hR : IsQuasiExcellent R) : IsNagataRing R
```

## Tag 0C23, a lemma

[Tag 0C23](https://stacks.math.columbia.edu/tag/0C23) in the Stacks Project.

**`isNormalRing_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L572). References: EGA IV (7.8.3), “(v) normal ascends”.

> **Stacks Tag 0C23.** The completion of a Noetherian normal local ring whose formal fibres
> are normal is a normal ring.

```lean
public theorem isNormalRing_adicCompletion_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsNormalRing A)
    (hformal : ∀ (p : Ideal A) [p.IsPrime],
      IsNormalRing (p.Fiber (AdicCompletion (IsLocalRing.maximalIdeal A) A))) :
    IsNormalRing (AdicCompletion (IsLocalRing.maximalIdeal A) A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.53, Tag 07QS](https://stacks.math.columbia.edu/tag/07QS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
