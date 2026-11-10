---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpen_setOf_flatOverAt, AlgebraicGeometry.modulePullback_isFlatOverAt_of_isFlatOverAt, AlgebraicGeometry.isFlatOverAt_of_modulePullback, AlgebraicGeometry.setOf_isFlatOverAt_modulePullback, AlgebraicGeometry.isOpen_setOf_isFlatOverAt_modulePullback
statement: formalized
proof: formalized
---

# 37.15 Openness of the flat locus

Section 37.15 of the Stacks Project, [Tag 0398](https://stacks.math.columbia.edu/tag/0398). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0399, a theorem

[Tag 0399](https://stacks.math.columbia.edu/tag/0399) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_flatOverAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatLocus.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatLocus.lean#L331). References: EGA IV (11.3.1), “U open”; EGA IV (15.4.1), “partial”.

> **Stacks Project, Tag 0399.** The locus where a finitely presented quasi-coherent module is
> flat over the target of a locally finitely presented morphism is open.

```lean
public theorem isOpen_setOf_flatOverAt
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation] :
    IsOpen {x : X | IsFlatOverAt f.toLRSHom.toShHom F x}
```

## Tag 047C, a lemma

[Tag 047C](https://stacks.math.columbia.edu/tag/047C) in the Stacks Project.

**`AlgebraicGeometry.modulePullback_isFlatOverAt_of_isFlatOverAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L131). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 047C (1).** For a cartesian square of schemes a quasi-coherent module
> which is flat over the base at the image of a point pulls back to a module which is flat over the
> new base at that point. Nothing is assumed of the base morphism, so this holds for an arbitrary
> base change. This is a restatement of `AlgebraicGeometry.modulePullback_isFlatOverAt`.

```lean
public lemma modulePullback_isFlatOverAt_of_isFlatOverAt
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    (x' : X') (hF : IsFlatOverAt f.toLRSHom.toShHom F (g' x')) :
    IsFlatOverAt f'.toLRSHom.toShHom ((modulePullback g'.toLRSHom.toShHom).obj F) x'
```

**`AlgebraicGeometry.isFlatOverAt_of_modulePullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L142). The attribute's comment: “part (2)”. References: SGA 3 V (7.4), “(i) descent”.

> **Stacks Project, Tag 047C (2).** Relative flatness of the pullback of a quasi-coherent
> module along a cartesian square descends at a point at which the base morphism is flat.

```lean
public lemma isFlatOverAt_of_modulePullback
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    (x' : X') (hg : IsFlatAt g.toLRSHom.toShHom (f' x'))
    (hF : IsFlatOverAt f'.toLRSHom.toShHom
      ((modulePullback g'.toLRSHom.toShHom).obj F) x') :
    IsFlatOverAt f.toLRSHom.toShHom F (g' x')
```

**`AlgebraicGeometry.setOf_isFlatOverAt_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L180). The attribute's comment: “flat locus”.

> **Stacks Project, Tag 047C (flat locus).** Under flat base change the relative flat locus
> of a quasi-coherent module is the preimage of the relative flat locus of the module itself.

```lean
public theorem setOf_isFlatOverAt_modulePullback
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    [Flat g] :
    {x' : X' | IsFlatOverAt f'.toLRSHom.toShHom
      ((modulePullback g'.toLRSHom.toShHom).obj F) x'} =
      g' ⁻¹' {x : X | IsFlatOverAt f.toLRSHom.toShHom F x}
```

**`AlgebraicGeometry.isOpen_setOf_isFlatOverAt_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L202). The attribute's comment: “open locus after base change”. References: EGA IV (11.3.1), “more general”.

> **Stacks Project, Tag 047C (open locus).** The relative flat locus of the pullback of a
> finitely presented quasi-coherent module along any base change of a morphism locally of finite
> presentation is open. Together with
> `AlgebraicGeometry.setOf_isFlatOverAt_modulePullback` this says that the open subset of
> [Stacks, Tag 0399] commutes with flat base change.

```lean
public theorem isOpen_setOf_isFlatOverAt_modulePullback
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    [F.IsFinitePresentation] [LocallyOfFinitePresentation f] :
    IsOpen {x' : X' | IsFlatOverAt f'.toLRSHom.toShHom
      ((modulePullback g'.toLRSHom.toShHom).obj F) x'}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.15, Tag 0398](https://stacks.math.columbia.edu/tag/0398)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
