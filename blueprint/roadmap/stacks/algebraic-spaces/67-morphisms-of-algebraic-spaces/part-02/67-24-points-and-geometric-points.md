---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSurjective_iff_surjective_app_isAlgClosed, AlgebraicGeometry.Space.geometricPoints_large_enough
statement: formalized
proof: formalized
---

# 67.24 Points and geometric points

Section 67.24 of the Stacks Project, [Tag 0485](https://stacks.math.columbia.edu/tag/0485). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0487, a lemma

[Tag 0487](https://stacks.math.columbia.edu/tag/0487) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_iff_surjective_app_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L610). References: EGA IV (1.3.7), “more general”; EGA I (6.3.10), “more general”.

> **Stacks 0487.** A morphism of algebraic spaces over `S` which is locally of finite type is
> surjective exactly when, for every algebraically closed field `k` of the working universe whose
> spectrum lies in the chosen site and every structure morphism `Spec k ⟶ S`, the induced map
> `X(k) ⟶ Y(k)` is surjective.

```lean
theorem isSurjective_iff_surjective_app_isAlgClosed
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    IsSurjective B S hS f ↔
      ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : B.Contains (Spec (.of k)))
        (b : Spec (.of k) ⟶ S),
        Function.Surjective
          (f.app (Opposite.op (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS))))
```

## Tag 0488, a lemma

[Tag 0488](https://stacks.math.columbia.edu/tag/0488) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricPoints_large_enough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeEnoughFields.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeEnoughFields.lean#L76).

> **Stacks 0488.** Let `S` be a scheme and let `X`, `Y` be algebraic spaces over `S`.
>
> 1. As `k` ranges over all algebraically closed fields over `S` the geometric points
>    `ȳ ∈ Y(k)` cover all of `|Y|`.
> 2. As `k` ranges over all algebraically closed fields over `S` with `|k| ≥ λ(Y)` and
>    `|k| > λ(X)` the geometric points `ȳ ∈ Y(k)` cover all of `|Y|`.
> 3. For any geometric point `s̄ : Spec k → S` where `k` has cardinality `> λ(X)` the map
>    `X(k) → |X_s|` is surjective.
> 4. For a morphism `X → Y` and any geometric point `s̄ : Spec k → S` where `k` has
>    cardinality `> λ(X)`, the map `X(k) → |X| ×_{|Y|} Y(k)` is surjective.
> 5. A morphism `X → Y` is surjective if and only if `X(k) → Y(k)` is surjective for all
>    algebraically closed fields `k` over `S` with `|k| > λ(X)` and `|k| ≥ λ(Y)`.
>
> Following the source, `λ(X)` and `λ(Y)` are the cardinals `AlgebraicGeometry.Scheme.lambdaCard`
> of schemes carrying a surjective étale morphism onto `X` and onto `Y`; the clauses quantify
> over all such atlases.

```lean
theorem geometricPoints_large_enough
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    -- (1) geometric points cover the point set
    (∀ y : points B S hS Y, ∃ p : GeometricPoint B S hS Y, p.image = y) ∧
    -- (2) geometric points over large enough fields cover the point set
    (∀ (UX UY : BigFppfOver B S hS) (fX : yoneda.obj UX ⟶ X) (fY : yoneda.obj UY ⟶ Y),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fX →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fX →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fY →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fY →
      ∀ y : points B S hS Y, ∃ p : GeometricPoint B S hS Y, p.LiesOver y ∧
        ((BigFppfOver.toScheme B S hS).obj UY).lambdaCard ≤ Cardinal.mk p.val.carrier ∧
        ((BigFppfOver.toScheme B S hS).obj UX).lambdaCard < Cardinal.mk p.val.carrier) ∧
    -- (3) `X(k) → |X_s|` is surjective
    (∀ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f →
      ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : B.Contains (Spec (.of k)))
        (b : Spec (.of k) ⟶ S),
        ((BigFppfOver.toScheme B S hS).obj U).lambdaCard < Cardinal.mk k →
      ∀ (s : S) (hs : ∀ t, b t = s) (Xs : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (pr : Xs ⟶ X) (pr' : Xs ⟶ yoneda.obj (residueSiteObject B S hS s))
        (hpb : IsPullback pr pr' (toBaseSiteMap B S hS X)
          (yoneda.map (toBaseSiteObject B S hS (residueSiteObject B S hS s)))),
        Function.Surjective (fibrePointOfFieldPoint B S hS hk b s hs pr pr' hpb)) ∧
    -- (4) `X(k) → |X| ×_{|Y|} Y(k)` is surjective
    (∀ (a : X ⟶ Y) (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f →
      ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : B.Contains (Spec (.of k)))
        (b : Spec (.of k) ⟶ S),
        ((BigFppfOver.toScheme B S hS).obj U).lambdaCard < Cardinal.mk k →
      ∀ (x : points B S hS X)
        (y : Y.obj (Opposite.op (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)))),
        pointsMap B S hS X a x =
            (⟨k, hk, b, y⟩ : FieldValuedPoint B S hS Y).class B S hS Y →
        ∃ z : X.obj (Opposite.op (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS))),
          a.app (Opposite.op (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS))) z = y ∧
          (⟨k, hk, b, z⟩ : FieldValuedPoint B S hS X).class B S hS X = x) ∧
    -- (5) surjectivity is tested on the field-valued points over large enough fields
    (∀ (a : X ⟶ Y) (UX UY : BigFppfOver B S hS)
        (fX : yoneda.obj UX ⟶ X) (fY : yoneda.obj UY ⟶ Y),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fX →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fX →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fY →
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) fY →
      (IsSurjective B S hS a ↔
        ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : B.Contains (Spec (.of k)))
          (b : Spec (.of k) ⟶ S),
          ((BigFppfOver.toScheme B S hS).obj UX).lambdaCard < Cardinal.mk k →
          ((BigFppfOver.toScheme B S hS).obj UY).lambdaCard ≤ Cardinal.mk k →
          Function.Surjective
            (a.app (Opposite.op (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS))))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.24, Tag 0485](https://stacks.math.columbia.edu/tag/0485)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
