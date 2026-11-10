---
declaration: section
origin: cited
lean: AlgebraicGeometry.GlueingNearPoint.finitePresentationAwayBaseChange_isEquivalence, AlgebraicGeometry.GlueingNearPoint.isSeparated_iff_isSeparated_baseChange, AlgebraicGeometry.GlueingNearPoint.isProper_iff_isProper_baseChange, AlgebraicGeometry.GlueingNearPoint.isFinite_iff_isFinite_baseChange, AlgebraicGeometry.GlueingNearPoint.etale_iff_etale_baseChange
statement: formalized
proof: formalized
---

# 32.21 Application to modifications

Section 32.21 of the Stacks Project, [Tag 0B3W](https://stacks.math.columbia.edu/tag/0B3W). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B3X, a lemma

[Tag 0B3X](https://stacks.math.columbia.edu/tag/0B3X) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.finitePresentationAwayBaseChange_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Modifications.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Modifications.lean#L308).

> **Stacks Project, Tag 0B3X.** Let `s` be a closed point of a scheme `S` whose open
> complement `U = S ∖ {s}` has quasi-compact inclusion.  Base change along
> `Spec 𝒪_{S, s} ⟶ S` is an equivalence from the category of finitely presented morphisms to `S`
> which are isomorphisms over `U` onto the category of finitely presented morphisms to
> `Spec 𝒪_{S, s}` which are isomorphisms over the punctured spectrum.

```lean
theorem finitePresentationAwayBaseChange_isEquivalence (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι) :
    (finitePresentationAwayBaseChange S s hs).IsEquivalence
```

## Tag 0BFN, a lemma

[Tag 0BFN](https://stacks.math.columbia.edu/tag/0BFN) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.isSeparated_iff_isSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean#L131). The attribute's comment: “separated”.

> **Stacks Project, Tag 0BFN (separated case).** A morphism of finite presentation to `S` which
> is an isomorphism over the complement of a closed point `s` is separated exactly when its base
> change along `Spec 𝒪_{S, s} ⟶ S` is separated.

```lean
theorem isSeparated_iff_isSeparated_baseChange (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι)
    (X : FinitePresentationAway (puncturedOpen hs)) :
    IsSeparated X.obj.hom ↔
      IsSeparated ((finitePresentationAwayBaseChange S s hs).obj X).obj.hom
```

**`AlgebraicGeometry.GlueingNearPoint.isProper_iff_isProper_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean#L144). The attribute's comment: “proper”.

> **Stacks Project, Tag 0BFN (proper case).** A morphism of finite presentation to `S` which is
> an isomorphism over the complement of a closed point `s` is proper exactly when its base change
> along `Spec 𝒪_{S, s} ⟶ S` is proper.

```lean
theorem isProper_iff_isProper_baseChange (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι)
    (X : FinitePresentationAway (puncturedOpen hs)) :
    IsProper X.obj.hom ↔
      IsProper ((finitePresentationAwayBaseChange S s hs).obj X).obj.hom
```

**`AlgebraicGeometry.GlueingNearPoint.isFinite_iff_isFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean#L157). The attribute's comment: “finite”.

> **Stacks Project, Tag 0BFN (finite case).** A morphism of finite presentation to `S` which is
> an isomorphism over the complement of a closed point `s` is finite exactly when its base change
> along `Spec 𝒪_{S, s} ⟶ S` is finite.

```lean
theorem isFinite_iff_isFinite_baseChange (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι)
    (X : FinitePresentationAway (puncturedOpen hs)) :
    IsFinite X.obj.hom ↔
      IsFinite ((finitePresentationAwayBaseChange S s hs).obj X).obj.hom
```

**`AlgebraicGeometry.GlueingNearPoint.etale_iff_etale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ModificationProperties.lean#L170). The attribute's comment: “etale”.

> **Stacks Project, Tag 0BFN (étale case).** A morphism of finite presentation to `S` which is
> an isomorphism over the complement of a closed point `s` is étale exactly when its base change
> along `Spec 𝒪_{S, s} ⟶ S` is étale.

```lean
theorem etale_iff_etale_baseChange (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι)
    (X : FinitePresentationAway (puncturedOpen hs)) :
    Etale X.obj.hom ↔
      Etale ((finitePresentationAwayBaseChange S s hs).obj X).obj.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.21, Tag 0B3W](https://stacks.math.columbia.edu/tag/0B3W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
