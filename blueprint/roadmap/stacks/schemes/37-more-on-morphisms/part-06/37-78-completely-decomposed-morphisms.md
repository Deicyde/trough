---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsCompletelyDecomposed, AlgebraicGeometry.IsCompletelyDecomposedFamily, AlgebraicGeometry.isCompletelyDecomposed_comp, AlgebraicGeometry.isCompletelyDecomposedFamily_comp, AlgebraicGeometry.isCompletelyDecomposed_pullback, AlgebraicGeometry.isCompletelyDecomposedFamily_pullback, AlgebraicGeometry.exists_finite_immersion_cover_with_sections, AlgebraicGeometry.exists_isCompletelyDecomposed_baseChange_of_limitBaseChange
statement: formalized
proof: formalized
---

# 37.78 Completely decomposed morphisms

Section 37.78 of the Stacks Project, [Tag 0GTH](https://stacks.math.columbia.edu/tag/0GTH). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GTI, a definition

[Tag 0GTI](https://stacks.math.columbia.edu/tag/0GTI) in the Stacks Project.

**`AlgebraicGeometry.IsCompletelyDecomposed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L59). The attribute's comment: “morphism”.

> A morphism of schemes is **completely decomposed** if every point of the target is the
> image of a point at which the induced map on residue fields is an isomorphism.

```lean
def IsCompletelyDecomposed {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.IsCompletelyDecomposedFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L65). The attribute's comment: “family”.

> A family of morphisms of schemes with a common target is **completely decomposed** if the
> induced morphism from the coproduct of the source schemes is completely decomposed.

```lean
def IsCompletelyDecomposedFamily {I : Type v} [Small.{u} I]
    {X : I → Scheme.{u}} {Y : Scheme.{u}} (f : ∀ i, X i ⟶ Y) : Prop
```

## Tag 0GTJ, a lemma

[Tag 0GTJ](https://stacks.math.columbia.edu/tag/0GTJ) in the Stacks Project.

**`AlgebraicGeometry.isCompletelyDecomposed_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L120). The attribute's comment: “morphisms”.

> The composite of two completely decomposed morphisms of
> schemes is completely decomposed.

```lean
lemma isCompletelyDecomposed_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsCompletelyDecomposed f) (hg : IsCompletelyDecomposed g) :
    IsCompletelyDecomposed (f ≫ g)
```

**`AlgebraicGeometry.isCompletelyDecomposedFamily_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L132). The attribute's comment: “families”.

> Composing a completely decomposed family with a completely
> decomposed family over each of its sources gives a completely decomposed family indexed by the
> dependent sum.

```lean
lemma isCompletelyDecomposedFamily_comp {I : Type v} [Small.{u} I]
    {J : I → Type w} [∀ i, Small.{u} (J i)] {X : I → Scheme.{u}}
    {X' : ∀ i, J i → Scheme.{u}} {Y : Scheme.{u}} (f : ∀ i, X i ⟶ Y)
    (g : ∀ i j, X' i j ⟶ X i) (hf : IsCompletelyDecomposedFamily f)
    (hg : ∀ i, IsCompletelyDecomposedFamily (g i)) :
    IsCompletelyDecomposedFamily
      (fun ij : Σ i, J i => g ij.1 ij.2 ≫ f ij.1)
```

## Tag 0GTK, a lemma

[Tag 0GTK](https://stacks.math.columbia.edu/tag/0GTK) in the Stacks Project.

**`AlgebraicGeometry.isCompletelyDecomposed_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L197). The attribute's comment: “morphism”.

> A completely decomposed morphism remains completely
> decomposed after arbitrary base change.

```lean
lemma isCompletelyDecomposed_pullback
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : IsCompletelyDecomposed f) :
    IsCompletelyDecomposed (pullback.snd f g)
```

**`AlgebraicGeometry.isCompletelyDecomposedFamily_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CompletelyDecomposed.lean#L208). The attribute's comment: “family”.

> A completely decomposed family of morphisms remains completely decomposed after arbitrary
> base change.

```lean
lemma isCompletelyDecomposedFamily_pullback
    {I : Type v} [Small.{u} I] {X : I → Scheme.{u}} {Y Y' : Scheme.{u}}
    (f : ∀ i, X i ⟶ Y) (g : Y' ⟶ Y)
    (hf : IsCompletelyDecomposedFamily f) :
    IsCompletelyDecomposedFamily (fun i ↦ pullback.snd (f i) g)
```

## Tag 0GTL, a lemma

[Tag 0GTL](https://stacks.math.columbia.edu/tag/0GTL) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_immersion_cover_with_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CompletelyDecomposed/FiniteCover.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CompletelyDecomposed/FiniteCover.lean#L299).

> A completely decomposed morphism locally of finite presentation over a
> quasi-compact, quasi-separated base has a finite surjective cover by immersions
> of finite presentation on each of which the morphism admits a section.

```lean
theorem exists_finite_immersion_cover_with_sections
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsCompletelyDecomposed f)
    [LocallyOfFinitePresentation f] [CompactSpace Y] [QuasiSeparatedSpace Y] :
    ∃ (n : ℕ) (Z : Fin n → Scheme.{u}) (g : ∀ i, Z i ⟶ Y),
      Surjective (Sigma.desc g) ∧
        (∀ i, IsImmersion (g i)) ∧
        (∀ i, FinitePresentation (g i)) ∧
        (∀ i, ∃ s : Z i ⟶ pullback f (g i),
          s ≫ pullback.snd f (g i) = 𝟙 (Z i))
```

## Tag 0GTM, a lemma

[Tag 0GTM](https://stacks.math.columbia.edu/tag/0GTM) in the Stacks Project.

**`AlgebraicGeometry.exists_isCompletelyDecomposed_baseChange_of_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/CompletelyDecomposed.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/CompletelyDecomposed.lean#L236).

> **Stacks Project, Tag 0GTM.** Let a scheme be the limit of a cofiltered inverse system of
> schemes with affine transition morphisms, and let a locally finitely presented morphism over one
> stage have quasi-compact, quasi-separated target. If its base change to the limit is completely
> decomposed, then its base change to some later stage is completely decomposed.

```lean
theorem exists_isCompletelyDecomposed_baseChange_of_limitBaseChange
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (S : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (c : Cone S) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (S.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    (hf : IsCompletelyDecomposed ((Over.pullback (c.π.app i₀)).map f₀).left) :
    ∃ (i : I) (g : i ⟶ i₀),
      IsCompletelyDecomposed ((Over.pullback (S.map g)).map f₀).left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.78, Tag 0GTH](https://stacks.math.columbia.edu/tag/0GTH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
