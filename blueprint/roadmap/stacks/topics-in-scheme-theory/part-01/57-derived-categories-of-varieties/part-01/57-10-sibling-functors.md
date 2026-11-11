---
declaration: section
origin: cited
lean: AlgebraicGeometry.AreSiblings, AlgebraicGeometry.areSiblings_of_restrictionIso_of_negative_ext, AlgebraicGeometry.essSurj_of_areSiblings, AlgebraicGeometry.fullyFaithful_of_areSiblings, AlgebraicGeometry.exists_negative_epimorphic_lift_comp_eq_zero, AlgebraicGeometry.iso_of_areSiblings_of_fullyFaithful, AlgebraicGeometry.shiftedRestrictionIso_naturality
statement: formalized
proof: formalized
---

# 57.10 Sibling functors

Section 57.10 of the Stacks Project, [Tag 0FZS](https://stacks.math.columbia.edu/tag/0FZS). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FZT, a definition

[Tag 0FZT](https://stacks.math.columbia.edu/tag/0FZT) in the Stacks Project.

**`AlgebraicGeometry.AreSiblings`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Basic.lean#L67).

> **Stacks Project, Tag 0FZT.** Two exact functors from the bounded derived category of an
> abelian category are **siblings** if their restrictions to the abelian category are naturally
> isomorphic and their values at each object of the bounded derived category are isomorphic.

```lean
public structure AreSiblings (F F' : DerivedCategory.Bounded A ⥤ D) [IsTriangulated D]
    [F.CommShift ℤ] [F.IsTriangulated] [F'.CommShift ℤ] [F'.IsTriangulated] : Prop
```

## Tag 0FZU, a lemma

[Tag 0FZU](https://stacks.math.columbia.edu/tag/0FZU) in the Stacks Project.

**`AlgebraicGeometry.areSiblings_of_restrictionIso_of_negative_ext`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Criterion.lean, line 753](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Criterion.lean#L753).

> **Stacks Project, Tag 0FZU.** Exact functors from the bounded derived category of an
> abelian category are siblings if their restrictions to the abelian category are naturally
> isomorphic and all negative Ext groups between images of objects of the abelian category under
> the first functor vanish.

```lean
public lemma areSiblings_of_restrictionIso_of_negative_ext
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    {D : Type u'} [Category.{v'} D] [HasZeroObject D] [HasShift D ℤ]
    [Preadditive D] [∀ n : ℤ, (shiftFunctor D n).Additive]
    [Pretriangulated D] [IsTriangulated D]
    (F F' : DerivedCategory.Bounded A ⥤ D)
    [F.CommShift ℤ] [F.IsTriangulated] [F'.CommShift ℤ] [F'.IsTriangulated]
    (h_restriction : Nonempty
      (boundedSingleFunctor A ⋙ F ≅ boundedSingleFunctor A ⋙ F'))
    (h_negative : ∀ (X Y : A) (q : ℤ), q < 0 →
      Subsingleton
        (F.obj ((boundedSingleFunctor A).obj X) ⟶
          (F.obj ((boundedSingleFunctor A).obj Y))⟦q⟧)) :
    AreSiblings F F'
```

## Tag 0FZV, a lemma

[Tag 0FZV](https://stacks.math.columbia.edu/tag/0FZV) in the Stacks Project.

**`AlgebraicGeometry.essSurj_of_areSiblings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Transfer.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Transfer.lean#L720). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0FZV, part (1).** If two exact functors from a bounded
> derived category are siblings and the first is essentially surjective, then the second is
> essentially surjective.

```lean
public theorem essSurj_of_areSiblings (h : AreSiblings F F')
    (hF : F.EssSurj) : F'.EssSurj
```

**`AlgebraicGeometry.fullyFaithful_of_areSiblings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Transfer.lean, line 731](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Transfer.lean#L731). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0FZV, part (2).** If two exact functors from a bounded
> derived category are siblings and the first is fully faithful, then the second is fully
> faithful.

```lean
public theorem fullyFaithful_of_areSiblings (h : AreSiblings F F')
    (hF : Nonempty F.FullyFaithful) : Nonempty F'.FullyFaithful
```

## Tag 0GWF, a lemma

[Tag 0GWF](https://stacks.math.columbia.edu/tag/0GWF) in the Stacks Project.

**`AlgebraicGeometry.exists_negative_epimorphic_lift_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/NegativeObjects.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/NegativeObjects.lean#L117). The attribute's comment: “the case `X' = 0`, with no condition on the composition”.

> **Stacks Project, Tag 0GWG.** A map of bounded derived objects whose target has zero
> cohomology in degree `b` can be killed by a map from a negative object in degree `b` which
> surjects onto the degree-`b` cohomology.

```lean
public theorem exists_negative_epimorphic_lift_comp_eq_zero
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    (hA : ∀ Y : A, ∃ (N : A) (p : N ⟶ Y), Epi p ∧ Subsingleton (Y ⟶ N))
    (X X' : DerivedCategory.Bounded A) (f : X ⟶ X') (b : ℤ)
    (hX' : IsZero ((DerivedCategory.homologyFunctor A b).obj X'.obj)) :
    ∃ (N : A) (g : (DerivedCategory.singleFunctor A b).obj N ⟶ X.obj),
      Epi ((DerivedCategory.singleFunctorCompHomologyFunctorIso A b).inv.app N ≫
        (DerivedCategory.homologyFunctor A b).map g) ∧
      Subsingleton (((DerivedCategory.homologyFunctor A b).obj X.obj) ⟶ N) ∧
      g ≫ (DerivedCategory.Bounded.ι.map f) = 0
```

## Tag 0GWG, a lemma

[Tag 0GWG](https://stacks.math.columbia.edu/tag/0GWG) in the Stacks Project.

**`AlgebraicGeometry.exists_negative_epimorphic_lift_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/NegativeObjects.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/NegativeObjects.lean#L117).

> **Stacks Project, Tag 0GWG.** A map of bounded derived objects whose target has zero
> cohomology in degree `b` can be killed by a map from a negative object in degree `b` which
> surjects onto the degree-`b` cohomology.

```lean
public theorem exists_negative_epimorphic_lift_comp_eq_zero
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    (hA : ∀ Y : A, ∃ (N : A) (p : N ⟶ Y), Epi p ∧ Subsingleton (Y ⟶ N))
    (X X' : DerivedCategory.Bounded A) (f : X ⟶ X') (b : ℤ)
    (hX' : IsZero ((DerivedCategory.homologyFunctor A b).obj X'.obj)) :
    ∃ (N : A) (g : (DerivedCategory.singleFunctor A b).obj N ⟶ X.obj),
      Epi ((DerivedCategory.singleFunctorCompHomologyFunctorIso A b).inv.app N ≫
        (DerivedCategory.homologyFunctor A b).map g) ∧
      Subsingleton (((DerivedCategory.homologyFunctor A b).obj X.obj) ⟶ N) ∧
      g ≫ (DerivedCategory.Bounded.ι.map f) = 0
```

## Tag 0FZW, a proposition

[Tag 0FZW](https://stacks.math.columbia.edu/tag/0FZW) in the Stacks Project.

**`AlgebraicGeometry.iso_of_areSiblings_of_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Isomorphism.lean, line 1114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/Isomorphism.lean#L1114).

> **Stacks Project, Tag 0FZW.** Sibling exact functors from a bounded derived category
> are naturally isomorphic if the first is fully faithful and the source abelian category has
> enough negative objects.

```lean
public theorem iso_of_areSiblings_of_fullyFaithful
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    {D : Type u'} [Category.{v'} D] [HasZeroObject D] [HasShift D ℤ]
    [Preadditive D] [∀ n : ℤ, (shiftFunctor D n).Additive]
    [Pretriangulated D] [IsTriangulated D]
    (F F' : DerivedCategory.Bounded A ⥤ D)
    [F.CommShift ℤ] [F.IsTriangulated] [F'.CommShift ℤ] [F'.IsTriangulated]
    (h : AreSiblings F F')
    (hF : Nonempty F.FullyFaithful)
    (hA : HasEnoughNegativeObjects A) : Nonempty (F ≅ F')
```

## Tag 0FZX, an equation

[Tag 0FZX](https://stacks.math.columbia.edu/tag/0FZX) in the Stacks Project.

**`AlgebraicGeometry.shiftedRestrictionIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Support/ShiftedComparison.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Support/ShiftedComparison.lean#L57).

> **Stacks Project, Tag 0FZX.** The shifted comparison with a functor agreeing with the
> identity on the heart commutes with morphisms between objects concentrated in the same degree.

```lean
public theorem shiftedRestrictionIso_naturality
    (α : boundedSingleFunctor A ≅ boundedSingleFunctor A ⋙ F)
    (n : ℤ) (X Y : A)
    (f : ((boundedSingleFunctor A).obj X)⟦n⟧ ⟶ ((boundedSingleFunctor A).obj Y)⟦n⟧) :
    f ≫ (shiftedRestrictionIso α n Y).hom =
      (shiftedRestrictionIso α n X).hom ≫ F.map f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.10, Tag 0FZS](https://stacks.math.columbia.edu/tag/0FZS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
