---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSyntomic, AlgebraicGeometry.Space.IsSyntomicAt, AlgebraicGeometry.Space.isSyntomic_comp, AlgebraicGeometry.Space.isSyntomic_isStableUnderBaseChange, AlgebraicGeometry.Space.isSyntomic_tfae, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isSyntomic, AlgebraicGeometry.Space.isFlat_of_isSyntomic, AlgebraicGeometry.Space.universallyOpen_of_isSyntomic
statement: formalized
proof: formalized
---

# 67.36 Syntomic morphisms

Section 67.36 of the Stacks Project, [Tag 03Z6](https://stacks.math.columbia.edu/tag/03Z6). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03Z7, a definition

[Tag 03Z7](https://stacks.math.columbia.edu/tag/03Z7) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSyntomic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Syntomic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Syntomic.lean#L59). The attribute's comment: “part (1): syntomic morphisms”.

> **Stacks 03Z7, part (1).** A morphism of algebraic spaces over `S` is *syntomic* when
> the scheme morphism underlying every commuting square of étale scheme charts of it is
> syntomic.

```lean
abbrev IsSyntomic (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsSyntomicAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Syntomic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Syntomic.lean#L67). The attribute's comment: “part (2): syntomic at a point”.

> **Stacks 03Z7, part (2).** A morphism of algebraic spaces over `S` is *syntomic at* a
> point `x` of its source when it is syntomic on some open subspace of the source having a
> point over `x`.

```lean
abbrev IsSyntomicAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 03Z8, a lemma

[Tag 03Z8](https://stacks.math.columbia.edu/tag/03Z8) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L162).

> **Stacks 03Z8.** The composite of two syntomic morphisms of algebraic spaces over `S` is
> syntomic.
>
> Syntomicity of scheme morphisms is stable under composition ([Stacks Project, Tag 01UH]) and is
> étale local on the source and target (Tag 04R3), so this is the instance of
> [Stacks Project, Tag 0AML] at that property.

```lean
theorem isSyntomic_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsSyntomic B S hS f) (hg : IsSyntomic B S hS g) :
    IsSyntomic B S hS (f ≫ g)
```

## Tag 03Z9, a lemma

[Tag 03Z9](https://stacks.math.columbia.edu/tag/03Z9) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L178).

> **Stacks 03Z9.** Syntomic morphisms of algebraic spaces over `S` are stable under base
> change.
>
> Syntomicity of scheme morphisms is stable under base change ([Stacks Project, Tag 01UI]) and is
> étale local on the source and target (Tag 04R3), so this is the instance of
> [Stacks Project, Tag 0AMM] at that property.

```lean
theorem isSyntomic_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsSyntomic B S hS f.hom)
```

## Tag 03ZA, a lemma

[Tag 03ZA](https://stacks.math.columbia.edu/tag/03ZA) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SyntomicTfae.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SyntomicTfae.lean#L92).

> **Stacks 03ZA.** Nine criteria for a morphism of algebraic spaces over `S` to be syntomic:
> pointwise syntomicity, syntomicity of every base change to a scheme or to an affine scheme or
> to one surjective étale chart of the target, syntomicity of the composite with one surjective
> étale chart of the source, syntomicity of the morphism of schemes in every — or in one
> surjective — commuting square of étale charts, or over a pair of Zariski coverings.
>
> Syntomicity of morphisms of schemes is étale local on the source and target (Tag 04R3), stable
> under composition ([Stacks Project, Tag 01UH]) and under base change
> ([Stacks Project, Tag 01UI]), and implied by étaleness ([Stacks Project, Tag 01VD]), so this
> is the instance of `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_tfae` — Tag 03MM for an
> arbitrary such property — at that property. Condition (2) is
> `AlgebraicGeometry.Space.IsSyntomicAt`, which is by definition condition (2) of that
> theorem.

```lean
theorem isSyntomic_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsSyntomic B S hS f,
      ∀ x : points B S hS X, IsSyntomicAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsSyntomic B S hS (pullback.fst g f),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) → IsSyntomic B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ IsSyntomic B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsSyntomic B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsSyntomic B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsSyntomic B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsSyntomic B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 0DEY, a lemma

[Tag 0DEY](https://stacks.math.columbia.edu/tag/0DEY) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L128).

> **Stacks 0DEY.** A syntomic morphism of algebraic spaces over `S` is locally of finite
> presentation.
>
> Both properties are the condition of Tag 03MJ on every commuting square of étale charts, so the
> statement is the scheme-level implication of [Stacks Project, Tag 01UK] quantified over the
> charts.

```lean
theorem isLocallyOfFinitePresentation_of_isSyntomic {f : X ⟶ Y}
    (hf : IsSyntomic B S hS f) : IsLocallyOfFinitePresentation B S hS f
```

## Tag 0DEZ, a lemma

[Tag 0DEZ](https://stacks.math.columbia.edu/tag/0DEZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_isSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L139).

> **Stacks 0DEZ.** A syntomic morphism of algebraic spaces over `S` is flat.
>
> Both properties are the condition of Tag 03MJ on every commuting square of étale charts, so the
> statement is the scheme-level implication of [Stacks Project, Tag 01UL] quantified over the
> charts.

```lean
theorem isFlat_of_isSyntomic {f : X ⟶ Y} (hf : IsSyntomic B S hS f) : IsFlat B S hS f
```

## Tag 0DF0, a lemma

[Tag 0DF0](https://stacks.math.columbia.edu/tag/0DF0) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_of_isSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean, line 814](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean#L814).

> A syntomic morphism of algebraic spaces over `S` is universally open in the sense of
> Stacks 03Z2.

```lean
theorem universallyOpen_of_isSyntomic
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsSyntomic B S hS f) : UniversallyOpen B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.36, Tag 03Z6](https://stacks.math.columbia.edu/tag/03Z6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
