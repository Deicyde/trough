---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.exists_division_isField_quotient_of_isoSpecField, AlgebraicGeometry.exists_finiteFlatQuotient_isAffine_of_mono_groupoidPreRelation, AlgebraicGeometry.GroupoidScheme.exists_division
statement: formalized
proof: formalized
---

# 80.9 Quotient by a subgroupoid

Section 80.9 of the Stacks Project, [Tag 04S3](https://stacks.math.columbia.edu/tag/04S3). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04S4, a lemma

[Tag 04S4](https://stacks.math.columbia.edu/tag/04S4) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_division_isField_quotient_of_isoSpecField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FieldObjectDivision.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FieldObjectDivision.lean#L180). The attribute's comment: “all four conclusions, at an object scheme which is the spectrum of a field and with only finiteness assumed of the source and target of the subgroupoid, together with the quotient being the spectrum of a field”.

> **Stacks Project, Tag 04S4, at an object scheme which is the spectrum of a field.**  A
> subgroupoid on the same object scheme whose pre-relation is a monomorphism and whose source and
> target maps are *finite* can be divided out, and the quotient is the spectrum of a field.
>
> Over a field the two finite locally free hypotheses of
> `AlgebraicGeometry.GroupoidScheme.exists_division` reduce to finiteness, by
> `AlgebraicGeometry.isFiniteLocallyFree_of_isFinite_of_isoSpecField`, and affineness of the
> object scheme is automatic.  The quotient morphism being finite locally free and surjective, its
> global functions are a field by
> `AlgebraicGeometry.isField_sections_of_isFiniteLocallyFree_of_surjective`.

```lean
theorem exists_division_isField_quotient_of_isoSpecField {S : Scheme.{u}} (G H : GroupoidScheme S)
    (i : GroupoidScheme.Hom H G) (hobj : H.objects = G.objects)
    (hiobj : i.mapObjects = eqToHom hobj) (k : Type u) [Field k]
    (e : G.objects.left ≅ Spec (.of k))
    [Mono i.mapArrows]
    [IsFinite H.source.left] [IsFinite H.target.left]
    [Mono (prod.lift H.target H.source)]
    [IsSeparated (prod.lift G.target G.source).left]
    [LocallyOfFiniteType (prod.lift G.target G.source).left]
    [LocallyQuasiFinite (prod.lift G.target G.source).left] :
    ∃ D : Division G H i hobj, IsField Γ(D.quotient.left, ⊤)
```

**`AlgebraicGeometry.exists_finiteFlatQuotient_isAffine_of_mono_groupoidPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/SubgroupoidDivision.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/SubgroupoidDivision.lean#L494). References: SGA 3 V (4.1), “special case”.

> **Stacks Project, Tag 04S4.** Let `(U, R, s, t, c)` be a groupoid scheme `G` over `S` and
> let `(U, P, s|_P, t|_P, c|_P)` be a groupoid scheme `H` mapping to it by a morphism `i` which is
> an isomorphism on objects, such that
>
> 1. `s|_P, t|_P : P ⟶ U` are finite locally free,
> 2. `j|_P = (t|_P, s|_P) : P ⟶ U ×_S U` is a monomorphism,
> 3. `U` is affine, and
> 4. `j = (t, s) : R ⟶ U ×_S U` is separated and locally quasi-finite (locally of finite type
>    with finite fibres; the finite type half is a separate class here).
>
> Then `U/P` is representable by an affine scheme `Ū`, the quotient morphism `U ⟶ Ū` is finite
> locally free (and surjective), and `P = U ×_Ū U`; these are the fields of
> `Stacks.Groupoids.FiniteFlatQuotient` together with affineness of its quotient scheme.
> Moreover `R` is the restriction of a groupoid scheme on `Ū` along the quotient morphism: there
> is a groupoid scheme `K` with object scheme `Ū` and a morphism `G ⟶ K` which is the quotient
> morphism on objects and whose square of arrow schemes over the pairs of objects is cartesian,
> `R = (U ×_S U) ×_{Ū ×_S Ū} R̄`; equivalently, it is fully faithful on the generalized points of
> every test scheme.
>
> The source asks in addition that `P ⟶ R` be a monomorphism; this follows from the other
> hypotheses (`j ∘ i = (i × i) ∘ j|_P` is a monomorphism) and is not used.

```lean
theorem exists_finiteFlatQuotient_isAffine_of_mono_groupoidPreRelation (G H : GroupoidScheme S)
    (i : GroupoidScheme.Hom H G) [IsIso i.mapObjects]
    [IsFiniteLocallyFree H.source.left] [IsFiniteLocallyFree H.target.left]
    [Mono (groupoidPreRelation H)] [IsAffine G.objects.left]
    [IsSeparated (groupoidPreRelation G).left] [LocallyQuasiFinite (groupoidPreRelation G).left]
    [LocallyOfFiniteType (groupoidPreRelation G).left] :
    ∃ Q : FiniteFlatQuotient H, IsAffine Q.space.left ∧
      ∃ (K : GroupoidScheme S) (he : K.objects = Q.space) (F : GroupoidScheme.Hom G K),
        F.mapObjects = (inv i.mapObjects ≫ Q.quotientMap) ≫ eqToHom he.symm ∧
          IsPullback F.mapArrows (groupoidPreRelation G) (groupoidPreRelation K)
            (prod.map F.mapObjects F.mapObjects) ∧
          ∀ T : Over S, Nonempty (F.evaluation T).FullyFaithful
```

**`AlgebraicGeometry.GroupoidScheme.exists_division`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/SubgroupoidDivisionDescent.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/SubgroupoidDivisionDescent.lean#L1075). The attribute's comment: “all four conclusions: the affine quotient Ū = U/P as the fppf-sheaf coequalizer, its finite locally free surjective quotient map, the kernel-pair square P = U ×\_Ū U, and the descent of the ambient groupoid R to a groupoid on Ū of which it is the restriction”.

> A finite locally free subgroupoid equivalence relation on an affine scheme can be
> divided out, and a separated locally quasi-finite ambient groupoid descends to the quotient.

```lean
theorem exists_division {S : Scheme.{u}} (G H : GroupoidScheme S)
    (i : GroupoidScheme.Hom H G) (hobj : H.objects = G.objects)
    (hiobj : i.mapObjects = eqToHom hobj)
    [Mono i.mapArrows]
    [Stacks.Morphisms.IsFiniteLocallyFree H.source.left]
    [Stacks.Morphisms.IsFiniteLocallyFree H.target.left]
    [Mono (prod.lift H.target H.source)]
    [IsAffine G.objects.left]
    [IsSeparated (prod.lift G.target G.source).left]
    [LocallyOfFiniteType (prod.lift G.target G.source).left]
    [LocallyQuasiFinite (prod.lift G.target G.source).left] :
    Nonempty (Division G H i hobj)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.9, Tag 04S3](https://stacks.math.columbia.edu/tag/04S3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
