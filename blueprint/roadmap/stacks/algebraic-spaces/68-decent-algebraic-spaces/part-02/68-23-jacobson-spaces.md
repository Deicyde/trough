---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_jacobson_atlas_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.exists_isClosed_pointsToScheme_of_isFiniteTypePoint, AlgebraicGeometry.Space.isFiniteTypePoint_iff_isClosed_singleton, AlgebraicGeometry.Space.finiteTypePoints_eq_setOf_isClosed_singleton, AlgebraicGeometry.Space.exists_jacobson_atlas_iff_jacobsonSpace_points, AlgebraicGeometry.Space.stacksSober_properGeneralizations, AlgebraicGeometry.Space.spectralSpace_properGeneralizations, AlgebraicGeometry.Space.jacobsonSpace_properGeneralizations
statement: formalized
proof: formalized
---

# 68.23 Jacobson spaces

Section 68.23 of the Stacks Project, [Tag 0BA2](https://stacks.math.columbia.edu/tag/0BA2). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BA3, a lemma

[Tag 0BA3](https://stacks.math.columbia.edu/tag/0BA3) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_jacobson_atlas_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Jacobson.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Jacobson.lean#L54). References: EGA IV (10.4.7), “Y Jacobson”.

> **Stacks 0BA3.** An algebraic space locally of finite type over a Jacobson algebraic
> space is Jacobson: if the algebraic space `X` over `S` has a surjective étale atlas by a
> Jacobson scheme and `f : Y ⟶ X` is locally of finite type, then so does `Y`.

```lean
theorem exists_jacobson_atlas_of_isLocallyOfFiniteType (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : Y ⟶ X)
    (hf : IsLocallyOfFiniteType B S hS f)
    (hJac : ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj U)) :
    ∃ (V : BigFppfOver B S hS) (b : yoneda.obj V ⟶ Y),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) b ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) b ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj V)
```

## Tag 0BA4, a lemma

[Tag 0BA4](https://stacks.math.columbia.edu/tag/0BA4) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isClosed_pointsToScheme_of_isFiniteTypePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/JacobsonClosedPoints.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/JacobsonClosedPoints.lean#L74).

> **Stacks 0BA4.** Let `X` be a Jacobson algebraic space over `S`, written as having a
> surjective étale atlas by a Jacobson scheme, and let `g : h_W ⟶ X` be locally of finite type
> with `W` an object of the big fppf site of `S`. A finite type point of `X` in the image of `g`
> is the image of a point of `h_W` whose underlying point of the scheme `W` is closed.

```lean
theorem exists_isClosed_pointsToScheme_of_isFiniteTypePoint
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hJac : ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj U))
    (W : BigFppfOver B S hS) (g : yoneda.obj W ⟶ X)
    (hg : IsLocallyOfFiniteType B S hS g)
    (x : points B S hS X) (hx : IsFiniteTypePoint B S hS X x)
    (himage : x ∈ Set.range (pointsMap B S hS (yoneda.obj W) g)) :
    ∃ y : points B S hS (yoneda.obj W),
      IsClosed ({pointsToScheme B S hS W y} :
        Set ((BigFppfOver.toScheme B S hS).obj W)) ∧
      pointsMap B S hS (yoneda.obj W) g y = x
```

## Tag 0BA5, a lemma

[Tag 0BA5](https://stacks.math.columbia.edu/tag/0BA5) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypePoint_iff_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/JacobsonFiniteTypePoints.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/JacobsonFiniteTypePoints.lean#L149). The attribute's comment: “pointwise form”.

> **Stacks 0BA5**, pointwise. Let `X` be a decent Jacobson algebraic space over `S`, the
> Jacobson condition being written as the existence of a surjective étale atlas by a Jacobson
> scheme. A point of `X` is a finite type point exactly when it is a closed point of `|X|`.

```lean
theorem isFiniteTypePoint_iff_isClosed_singleton
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X)
    (hJac : ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj U))
    (x : points B S hS X) :
    IsFiniteTypePoint B S hS X x ↔ IsClosed ({x} : Set (points B S hS X))
```

**`AlgebraicGeometry.Space.finiteTypePoints_eq_setOf_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/JacobsonFiniteTypePoints.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/JacobsonFiniteTypePoints.lean#L200).

> **Stacks 0BA5.** Let `X` be a decent Jacobson algebraic space over `S`, the Jacobson
> condition being written as the existence of a surjective étale atlas by a Jacobson scheme.
> Then `X_{ft-pts} ⊂ |X|` is the set of closed points.

```lean
theorem finiteTypePoints_eq_setOf_isClosed_singleton
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X)
    (hJac : ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj U)) :
    finiteTypePoints B S hS X = {x | IsClosed ({x} : Set (points B S hS X))}
```

## Tag 0BA6, a lemma

[Tag 0BA6](https://stacks.math.columbia.edu/tag/0BA6) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_jacobson_atlas_iff_jacobsonSpace_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/JacobsonPointSpace.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/JacobsonPointSpace.lean#L295).

> **Stacks 0BA6.** A decent algebraic space `X` over `S` is Jacobson — the Jacobson
> condition being written as the existence of a surjective étale atlas by a Jacobson scheme —
> if and only if its topological space `|X|` of points is a Jacobson topological space.

```lean
theorem exists_jacobson_atlas_iff_jacobsonSpace_points
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) :
    (∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) a ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj U)) ↔
    JacobsonSpace (points B S hS X)
```

## Tag 0ED2, a lemma

[Tag 0ED2](https://stacks.math.columbia.edu/tag/0ED2) in the Stacks Project.

**`AlgebraicGeometry.Space.stacksSober_properGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean#L224). The attribute's comment: “sobriety”.

> **Stacks 0ED2, sobriety.** The proper generalizations of a point `x` of a decent
> algebraic space over `S` form a sober topological space, sobriety being that of Stacks 004X:
> every irreducible closed subset has a unique generic point.

```lean
theorem stacksSober_properGeneralizations (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (x : points B S hS X) :
    StacksSober {x' : points B S hS X // x' ⤳ x ∧ x' ≠ x}
```

**`AlgebraicGeometry.Space.spectralSpace_properGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean#L235). The attribute's comment: “spectrality”.

> **Stacks 0ED2, spectrality.** The proper generalizations of a point `x` of a decent
> locally Noetherian algebraic space over `S` form a spectral topological space.

```lean
theorem spectralSpace_properGeneralizations (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (x : points B S hS X) :
    SpectralSpace {x' : points B S hS X // x' ⤳ x ∧ x' ≠ x}
```

**`AlgebraicGeometry.Space.jacobsonSpace_properGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProperGeneralizations.lean#L252). The attribute's comment: “the Jacobson property”.

> **Stacks 0ED2, the Jacobson property.** The proper generalizations of a point `x` of a
> decent locally Noetherian algebraic space over `S` form a Jacobson topological space.

```lean
theorem jacobsonSpace_properGeneralizations (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (x : points B S hS X) :
    JacobsonSpace {x' : points B S hS X // x' ⤳ x ∧ x' ≠ x}
```

**`AlgebraicGeometry.Space.noetherianSpace_properGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperGeneralizations.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperGeneralizations.lean#L50). The attribute's comment: “the Noetherian property”.

> **Stacks 0ED2, the Noetherian property.** The proper generalizations of a point `x` of a
> locally Noetherian algebraic space over `S` form a Noetherian topological space.

```lean
theorem noetherianSpace_properGeneralizations (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsLocallyNoetherian Y))
    (x : points B S hS X) :
    NoetherianSpace {x' : points B S hS X // x' ⤳ x ∧ x' ≠ x}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.23, Tag 0BA2](https://stacks.math.columbia.edu/tag/0BA2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
