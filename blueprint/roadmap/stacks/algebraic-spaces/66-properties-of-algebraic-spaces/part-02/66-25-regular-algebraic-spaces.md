---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRegular_iff_etaleLocalRings_regular, AlgebraicGeometry.Space.IsRegularAt, AlgebraicGeometry.Space.isRegularAt_iff_exists_etale_chart, AlgebraicGeometry.Space.isRegularAt_tfae, AlgebraicGeometry.Space.isNormal_of_isRegular
statement: formalized
proof: formalized
---

# 66.25 Regular algebraic spaces

Section 66.25 of the Stacks Project, [Tag 06LP](https://stacks.math.columbia.edu/tag/06LP). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06LQ, a lemma

[Tag 06LQ](https://stacks.math.columbia.edu/tag/06LQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegular_iff_etaleLocalRings_regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingRegular.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingRegular.lean#L88).

> A locally Noetherian algebraic space is regular exactly when its étale local rings at all
> geometric points are regular local rings.

```lean
theorem isRegular_iff_etaleLocalRings_regular (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F)
    (hnoeth : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsLocallyNoetherian X)) :
    HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsRegular X) ↔
      ∀ x : GeometricPoint B S hS F, IsRegularLocalRing (etaleLocalRing B S hS F x)
```

## Tag 0AH9, a definition

[Tag 0AH9](https://stacks.math.columbia.edu/tag/0AH9) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRegularAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularLocalRings.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularLocalRings.lean#L72).

> An algebraic space is *regular at a point* when every étale scheme chart has a regular local
> ring at every point of it above that point.

```lean
abbrev IsRegularAt (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.isRegularAt_iff_exists_etale_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularLocalRings.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularLocalRings.lean#L85). The attribute's comment: “some étale chart characterization”.

> An algebraic space is regular at a point if and only if some étale scheme chart has a regular
> local ring at some point of it above that point.

```lean
theorem isRegularAt_iff_exists_etale_chart (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    IsRegularAt B S hS F x ↔
      ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) a ∧
        ∃ p : FieldValuedPoint B S hS (yoneda.obj U),
          pointsMap B S hS (yoneda.obj U) a (p.class B S hS (yoneda.obj U)) = x ∧
          IsRegularLocalRing
            (((BigFppfOver.toScheme B S hS).obj U).presheaf.stalk (schemePoint B S hS U p))
```

## Tag 0AHA, a lemma

[Tag 0AHA](https://stacks.math.columbia.edu/tag/0AHA) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegularAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularAtGeometricPoints.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularAtGeometricPoints.lean#L112).

> **Stacks 0AHA.** For a point `x` of an algebraic space `F` the three conditions are
> equivalent: `F` is regular at `x`; the étale local ring of `F` is a regular local ring at every
> geometric point above `x`; and it is a regular local ring at some geometric point above `x`.

```lean
theorem isRegularAt_tfae (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) :
    List.TFAE
      [IsRegularAt B S hS F x,
        ∀ xbar : GeometricPoint B S hS F, xbar.LiesOver x →
          IsRegularLocalRing (etaleLocalRing B S hS F xbar),
        ∃ xbar : GeometricPoint B S hS F, xbar.LiesOver x ∧
          IsRegularLocalRing (etaleLocalRing B S hS F xbar)]
```

## Tag 0BGT, a lemma

[Tag 0BGT](https://stacks.math.columbia.edu/tag/0BGT) in the Stacks Project.

**`AlgebraicGeometry.Space.isNormal_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Normal.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Normal.lean#L160).

> **Stacks 0BGT.** A regular algebraic space is normal: a surjective étale atlas by a
> regular scheme is one by a normal scheme.

```lean
theorem isNormal_of_isRegular (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hreg : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsRegular X)) :
    HasEtaleLocalProperty B S hS F
      (fun X : Scheme.{u} => _root_.AlgebraicGeometry.IsNormal X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.25, Tag 06LP](https://stacks.math.columbia.edu/tag/06LP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
