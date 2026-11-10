---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isCoequalizer_of_surjective_flat_locallyOfFinitePresentation, AlgebraicGeometry.Space.isCoequalizer_of_surjectiveFiniteLocallyFree, AlgebraicGeometry.Space.isEquivalenceRelation_of_isPullback, AlgebraicGeometry.Space.isCoequalizer_of_surjectiveEtale, CategoryTheory.MorphismProperty.relative.property, Stacks.Groupoids.IsEtaleEquivalenceRelation, AlgebraicGeometry.Space.Presentation
statement: formalized
proof: formalized
---

# 65.9 Presentations of algebraic spaces

Section 65.9 of the Stacks Project, [Tag 0261](https://stacks.math.columbia.edu/tag/0261). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0262, a lemma

[Tag 0262](https://stacks.math.columbia.edu/tag/0262) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoequalizer_of_surjective_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatChartCoequalizer.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatChartCoequalizer.lean#L140). The attribute's comment: “part (3), with the étale chart of the source replaced by a surjective flat chart locally of finite presentation”.

> **Stacks 0262**, part (3), with the étale hypothesis on the chart weakened to flatness
> together with local finite presentation.  A surjective flat chart locally of finite
> presentation of an algebraic space is the coequalizer, in fppf sheaves of sets, of its kernel
> pair.
>
> The three conditions are the relative properties of Tag 02YN: they are asked of every
> represented base change of the chart.

```lean
theorem isCoequalizer_of_surjective_flat_locallyOfFinitePresentation
    (f : yoneda.obj U ⟶ F) (s t : R ⟶ U)
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f)
    (hF : IsAlgebraicSpace B S hS F)
    (hsurj : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f)
    (hflat : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Flat.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f)
    (hlfp : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFinitePresentation.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    let J := BigFppfOver.topology B S hS
    ∃ (hRsh : Presheaf.IsSheaf J (yoneda.obj R))
      (hUsh : Presheaf.IsSheaf J (yoneda.obj U)),
      let RF : Sheaf J (Type u) := ⟨yoneda.obj R, hRsh⟩
      let UF : Sheaf J (Type u) := ⟨yoneda.obj U, hUsh⟩
      let FF : Sheaf J (Type u) := ⟨F, hF.isSheaf⟩
      let sf : RF ⟶ UF := ⟨yoneda.map s⟩
      let tf : RF ⟶ UF := ⟨yoneda.map t⟩
      let ff : UF ⟶ FF := ⟨f⟩
    let w : sf ≫ ff = tf ≫ ff := by
        apply Sheaf.hom_ext
        exact hR.w
      Nonempty (IsColimit (Cofork.ofπ ff w))
```

**`AlgebraicGeometry.Space.isCoequalizer_of_surjectiveFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatChartCoequalizer.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatChartCoequalizer.lean#L187). The attribute's comment: “part (3), for a surjective finite locally free chart of the source in place of a surjective étale one”.

> **Stacks 0262**, part (3), for a surjective finite locally free chart in place of a
> surjective étale one.  Such a chart of an algebraic space is the coequalizer, in fppf sheaves
> of sets, of its kernel pair.
>
> Finite local freeness is read in the representable sense, condition (1) of Stacks 03ZW, and
> gives flatness and local finite presentation of every represented base change by the
> scheme-level equivalence Tag 02KB.

```lean
theorem isCoequalizer_of_surjectiveFiniteLocallyFree
    (f : yoneda.obj U ⟶ F) (s t : R ⟶ U)
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f)
    (hF : IsAlgebraicSpace B S hS F)
    (hsurj : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f)
    (hflf : (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    let J := BigFppfOver.topology B S hS
    ∃ (hRsh : Presheaf.IsSheaf J (yoneda.obj R))
      (hUsh : Presheaf.IsSheaf J (yoneda.obj U)),
      let RF : Sheaf J (Type u) := ⟨yoneda.obj R, hRsh⟩
      let UF : Sheaf J (Type u) := ⟨yoneda.obj U, hUsh⟩
      let FF : Sheaf J (Type u) := ⟨F, hF.isSheaf⟩
      let sf : RF ⟶ UF := ⟨yoneda.map s⟩
      let tf : RF ⟶ UF := ⟨yoneda.map t⟩
      let ff : UF ⟶ FF := ⟨f⟩
    let w : sf ≫ ff = tf ≫ ff := by
        apply Sheaf.hom_ext
        exact hR.w
      Nonempty (IsColimit (Cofork.ofπ ff w))
```

**`AlgebraicGeometry.Space.isEquivalenceRelation_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean#L96). The attribute's comment: “part (1)”.

> The kernel pair of a map from a representable presheaf defines an equivalence
> relation over the base scheme. This includes monicity of `R ⟶ U ×_S U`.

```lean
theorem isEquivalenceRelation_of_isPullback
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f) :
    IsEquivalenceRelation ((Over.post B.inclusion).map s)
      ((Over.post B.inclusion).map t)
```

**`AlgebraicGeometry.Space.isCoequalizer_of_surjectiveEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean#L179). The attribute's comment: “part (3)”.

> **Stacks 0262**, part (3). A surjective étale atlas of an algebraic space is the
> coequalizer, in fppf sheaves of sets, of its kernel pair: every map to a sheaf which
> identifies the two projections descends uniquely.

```lean
theorem isCoequalizer_of_surjectiveEtale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {R U : BigFppfOver B S hS}
    (f : yoneda.obj U ⟶ F) (s t : R ⟶ U)
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f)
    (hF : IsAlgebraicSpace B S hS F)
    (hsurj : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f)
    (hetale : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f) :
    let J := BigFppfOver.topology B S hS
    ∃ (hRsh : Presheaf.IsSheaf J (yoneda.obj R))
      (hUsh : Presheaf.IsSheaf J (yoneda.obj U)),
      let RF : Sheaf J (Type u) := ⟨yoneda.obj R, hRsh⟩
      let UF : Sheaf J (Type u) := ⟨yoneda.obj U, hUsh⟩
      let FF : Sheaf J (Type u) := ⟨F, hF.isSheaf⟩
      let sf : RF ⟶ UF := ⟨yoneda.map s⟩
      let tf : RF ⟶ UF := ⟨yoneda.map t⟩
      let ff : UF ⟶ FF := ⟨f⟩
    let w : sf ≫ ff = tf ≫ ff := by
        apply Sheaf.hom_ext
        exact hR.w
      Nonempty (IsColimit (Cofork.ofπ ff w))
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative.property`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative.property#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/KernelPairRelation.lean#L173) (StacksFrontier): “part (2), étale projections”.

## Tag 02WS, a definition

[Tag 02WS](https://stacks.math.columbia.edu/tag/02WS) in the Stacks Project.

**`Stacks.Groupoids.IsEtaleEquivalenceRelation`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L103).

> **Stacks 02WS.** An equivalence relation over `S` is *étale* when its source and
> target maps are étale morphisms of schemes.

```lean
class IsEtaleEquivalenceRelation {R U : Over S} (j : PreRelation R U) : Prop
```

## Tag 0263, a definition

[Tag 0263](https://stacks.math.columbia.edu/tag/0263) in the Stacks Project.

**`AlgebraicGeometry.Space.Presentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtalePresentation.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtalePresentation.lean#L50).

> **Stacks 0263.** An étale presentation of an algebraic space by a scheme over `S` together
> with an étale equivalence relation on it.

```lean
structure Presentation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hF : IsAlgebraicSpace B S hS F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.9, Tag 0261](https://stacks.math.columbia.edu/tag/0261)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
