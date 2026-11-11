---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_not_hasSomeSurjectivePresentation, AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_sections_isField_reduction_infinite, AlgebraicGeometry.FormalSpace.exists_representable_hasSomeSurjectivePresentation_not
statement: formalized
proof: formalized
---

# 110.77 Affine formal algebraic spaces

Section 110.77 of the Stacks Project, [Tag 0ANY](https://stacks.math.columbia.edu/tag/0ANY). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CBC, a lemma

[Tag 0CBC](https://stacks.math.columbia.edu/tag/0CBC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_not_hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NotMcQuillanExample.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/NotMcQuillanExample.lean#L56).

> **Stacks 0CBC.** There exists an affine formal algebraic space which is not McQuillan: the
> example of Stacks 0CBD admits no presentation by affine thickenings whose section-ring
> projections are all surjective.

```lean
public theorem exists_isAffineFormalAlgebraicSpace_not_hasSomeSurjectivePresentation :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (X : FppfSheaf B S hS),
      IsAffineFormalAlgebraicSpace B S hS X ∧ ¬ HasSomeSurjectivePresentation B S hS X
```

## Tag 0CBD, a lemma

[Tag 0CBD](https://stacks.math.columbia.edu/tag/0CBD) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_sections_isField_reduction_infinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SectionsDoNotSeparatePoints.lean, line 840](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SectionsDoNotSeparatePoints.lean#L840).

> **Stacks 0CBD.** There is an affine formal algebraic space whose regular functions do not
> separate points: writing `X = colim X_λ` as in Stacks 0AI7, the inverse limit of the rings
> `Γ(X_λ, O_{X_λ})` is a field, while the reduction of `X` has infinitely many points. The
> reduction is exhibited as a reduced affine scheme `T` of the site together with a
> representable thickening `T ⟶ X` through which every morphism to `X` from a reduced algebraic
> space factors uniquely, which determines it up to unique isomorphism.

```lean
public theorem exists_isAffineFormalAlgebraicSpace_sections_isField_reduction_infinite :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (X : FppfSheaf B S hS),
      IsAffineFormalAlgebraicSpace B S hS X ∧
      (∃ (I : Type (u + 1)) (pre : Preorder I),
        letI : Preorder I := pre
        Nonempty I ∧ IsDirected I (· ≤ ·) ∧
          ∃ D : I ⥤ BigAffineFppf B S hS,
            (∀ ⦃i j : I⦄ (f : i ⟶ j),
              Stacks.Thickenings.IsThickening
                ((BigAffineFppf.toScheme B S hS).map (D.map f))) ∧
            Nonempty (X ≅ colimit
              (D ⋙ BigAffineFppf.inclusion B S hS ⋙
                Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))) ∧
            (letI : CommRing (sectionDiagram B S hS D ⋙ forget CommRingCat.{u}).sections :=
              @Subring.toCommRing (∀ j, (sectionDiagram B S hS D).obj j) _
                (RingCat.sectionsSubring
                  (sectionDiagram B S hS D ⋙ forget₂ CommRingCat RingCat.{u}))
            IsField (sectionDiagram B S hS D ⋙ forget CommRingCat.{u}).sections)) ∧
      (∃ T : BigFppfOver B S hS,
        IsReduced ((BigFppfOver.toScheme B S hS).obj T) ∧
        Infinite ((BigFppfOver.toScheme B S hS).obj T) ∧
        ∃ ι : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj T ⟶ X,
          (MorphismProperty.relative
            (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
            (MorphismProperty.inverseImage
              (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
              (BigFppfOver.toScheme B S hS))) ι ∧
          ∀ U : FppfSheaf B S hS, Space.IsAlgebraicSpaceULift.{u + 1} B S hS U.obj →
            (∃ (V : BigFppfOver B S hS) (p : (uliftYoneda.{u + 1}).obj V ⟶ U.obj),
              (MorphismProperty.relative (uliftYoneda.{u + 1})
                (MorphismProperty.inverseImage
                  (@Surjective.{u} : MorphismProperty Scheme.{u})
                  (BigFppfOver.toScheme B S hS))) p ∧
              (MorphismProperty.relative (uliftYoneda.{u + 1})
                (MorphismProperty.inverseImage
                  (@Etale.{u} : MorphismProperty Scheme.{u})
                  (BigFppfOver.toScheme B S hS))) p ∧
              IsReduced ((BigFppfOver.toScheme B S hS).obj V)) →
            ∀ g : U ⟶ X, ∃! l : U ⟶
              (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj T, l ≫ ι = g)
```

## Tag 0CBE, a lemma

[Tag 0CBE](https://stacks.math.columbia.edu/tag/0CBE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_representable_hasSomeSurjectivePresentation_not`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverMcQuillan.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverMcQuillan.lean#L635).

> There exists a representable morphism `f : X ⟶ Y` of affine formal algebraic spaces with `Y`
> McQuillan, but `X` not McQuillan. The morphism is representable by schemes, and every represented
> base change of it is moreover an affine morphism of schemes.

```lean
theorem exists_representable_hasSomeSurjectivePresentation_not :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (inS : B.Contains S) (X Y : FppfSheaf B S inS)
      (f : X ⟶ Y),
      IsAffineFormalAlgebraicSpace B S inS X ∧ IsAffineFormalAlgebraicSpace B S inS Y ∧
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S inS)).relativelyRepresentable f ∧
      (MorphismProperty.inverseImage (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S inS)).relative
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S inS)) f ∧
      HasSomeSurjectivePresentation B S inS Y ∧ ¬ HasSomeSurjectivePresentation B S inS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.77, Tag 0ANY](https://stacks.math.columbia.edu/tag/0ANY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
