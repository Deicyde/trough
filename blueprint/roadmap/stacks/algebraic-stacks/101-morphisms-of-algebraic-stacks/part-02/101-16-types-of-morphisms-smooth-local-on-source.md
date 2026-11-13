---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.hasPropertyOnEverySmoothDiagram_iff_some, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_iff_relative, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_iff_represented, AlgebraicGeometry.Stack.HasPropertyOnSomeSmoothDiagram, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_comp, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_comp_of_precomp, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_baseChange, AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_mono
statement: formalized
proof: formalized
---

# 101.16 Types of morphisms smooth local on source-and-target

Section 101.16 of the Stacks Project, [Tag 06FL](https://stacks.math.columbia.edu/tag/06FL). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06FM, a lemma

[Tag 06FM](https://stacks.math.columbia.edu/tag/06FM) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasPropertyOnEverySmoothDiagram_iff_some`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismEveryConverse.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismEveryConverse.lean#L457). The attribute's comment: “equivalence of parts (1) and (2)”.

> For a property `P` of morphisms of algebraic spaces over `S` which is smooth local on the
> source-and-target and a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`: every diagram of
> algebraic spaces over `f` with smooth vertical 1-morphisms whose comparison to the 2-fibre product
> is smooth has `P` on its top horizontal morphism if and only if some such diagram with left
> vertical 1-morphism surjective on objects does.

```lean
theorem hasPropertyOnEverySmoothDiagram_iff_some
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (f : 𝒳 ⟶ 𝒴) :
    HasPropertyOnEverySmoothDiagram B S hS P f ↔ HasPropertyOnSomeSmoothDiagram B S hS P f
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_iff_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismRelative.lean, line 667](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismRelative.lean#L667). The attribute's comment: “representable morphism”.

> **Stacks 06FM, the assertion for a representable morphism.** Let `P` be a property of
> morphisms of algebraic spaces over `S` smooth local on the source-and-target which is moreover
> stable under base change and local at the target for the fppf precoverage, and let `f : 𝒳 ⟶ 𝒴`
> be a 1-morphism of algebraic stacks over `S` representable by algebraic spaces. Then `f` passes
> the existential smooth-diagram test of condition (2) exactly when it has the relative property
> `P` in the sense of Stacks 03YK, i.e. of Properties of Stacks, Section 04XB.
>
> Algebraicity of the source is not used in either direction; it is kept because it is part of the
> statement of the tagged assertion.

```lean
theorem hasPropertyOnSomeSmoothDiagram_iff_relative
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    [(spaceProperty B S hS P).IsStableUnderBaseChange]
    [(spaceProperty B S hS P).IsLocalAtTarget
      (Space.Topology.fppf.precoverage.{u, v} B S hS)]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (_h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    HasPropertyOnSomeSmoothDiagram B S hS P f ↔
      HasRelativeProperty.{u, u, u + 1, v} B S hS (spaceProperty B S hS P) f hf
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_iff_represented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismRepresented.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismRepresented.lean#L252). The attribute's comment: “representable source and target”.

> **Stacks 06FM, the assertion for representable source and target.** For a property `P` of
> morphisms of algebraic spaces over `S` smooth local on the source-and-target, and a 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` whose source and target are representable by algebraic
> spaces `F` and `G`, the existential smooth-diagram test of condition (2) holds for `f` exactly
> when the induced morphism `F ⟶ G` of representing presheaves has `P`.
>
> Forward: the given diagram becomes a diagram of morphisms of algebraic spaces and criterion (3)
> of Stacks 06FA applies. Backward: test condition (2) on the diagram given by the two representing
> equivalences.

```lean
theorem hasPropertyOnSomeSmoothDiagram_iff_represented
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (_h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (_h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (eX : StacksRepresentableCFG.EquivalenceOver
      𝒳.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
    (eY : StacksRepresentableCFG.EquivalenceOver
      𝒴.val.p (presheafOfCategories (G ⋙ typeToCat)).p)
    (f : 𝒳 ⟶ 𝒴) :
    HasPropertyOnSomeSmoothDiagram B S hS P f ↔
      P (representingMap B S hS 𝒳 𝒴 F G eX eY f)
```

## Tag 06FN, a definition

[Tag 06FN](https://stacks.math.columbia.edu/tag/06FN) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasPropertyOnSomeSmoothDiagram`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphism.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphism.lean#L177). The attribute's comment: “the definition, as condition (2) of Stacks 06FM”.

> **Condition (2) of Stacks 06FM, and the definition of Stacks 06FN.** There is a
> 2-commutative square of algebraic spaces over `f` whose two vertical 1-morphisms are smooth,
> whose left vertical 1-morphism is surjective on objects, and whose top horizontal morphism of
> algebraic spaces has `P`.
>
> By **Stacks 06FN** this is what it means for a 1-morphism of algebraic stacks to *have the
> property* `P`, for `P` smooth local on the source-and-target: Stacks 06FN defines that notion by
> the equivalent conditions of Stacks 06FM, and
> `AlgebraicGeometry.Stack.hasPropertyOnEverySmoothDiagram_iff_some` is that equivalence, so either
> condition may serve as the definition. The existential one is taken, because it carries the
> diagram data its consumers need.

```lean
abbrev HasPropertyOnSomeSmoothDiagram
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴) :
    Prop
```

## Tag 06FP, a remark

[Tag 06FP](https://stacks.math.columbia.edu/tag/06FP) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismComp.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismComp.lean#L132).

> **Stacks 06FP.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> smooth local on the source-and-target and whose restriction to algebraic spaces is stable under
> composition. Then the induced property of 1-morphisms of algebraic stacks over `S` — the
> existential smooth-diagram criterion of **Stacks 06FM**, which is **Definition 06FN** — is
> stable under composition.
>
> The proof is the source's. Choose a smooth presentation `W ⟶ 𝒵`, surjective on objects, by an
> algebraic space; then a diagram over `g` whose right vertical 1-morphism is that presentation,
> which exists by condition (1) of Stacks 06FM — its left vertical 1-morphism is a smooth
> presentation `V ⟶ 𝒴` surjective on objects; then a diagram over `f` whose right vertical
> 1-morphism is *that* one. The two top horizontal morphisms `U ⟶ V` and `V ⟶ W` have `P` by
> condition (1), so their composite has `P` by hypothesis, and the outer square is a diagram over
> `f ≫ g` whose left vertical 1-morphism is the one of the diagram over `f` — smooth and
> surjective on objects — and whose right vertical 1-morphism is the presentation of `𝒵`.

```lean
theorem hasPropertyOnSomeSmoothDiagram_comp
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    (hcomp : ∀ {U V W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u},
      IsAlgebraicSpace B S hS U → IsAlgebraicSpace B S hS V → IsAlgebraicSpace B S hS W →
      ∀ (p : U ⟶ V) (q : V ⟶ W), P p → P q → P (p ≫ q))
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (h𝒵 : IsAlgebraicStack.{u, w} B S hS 𝒵.val)
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : HasPropertyOnSomeSmoothDiagram B S hS P f)
    (hg : HasPropertyOnSomeSmoothDiagram B S hS P g) :
    HasPropertyOnSomeSmoothDiagram B S hS P (f ≫ g)
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_comp_of_precomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCompGeneral.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCompGeneral.lean#L168).

> **Stacks 06FP.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under precomposition with a smooth morphism, stable under composition, and whose
> restriction to algebraic spaces is stable under base change. The property of 1-morphisms of
> categories fibred in groupoids over the big fppf site of `S` that **Stacks 06FN** attaches to `P`
> is stable under composition: if `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` both pass the existential
> smooth-diagram test of condition (2) of **Stacks 06FM**, then so does `f ≫ g`.
>
> Stacks 06FP assumes `P` smooth local on the source-and-target, which is what makes the property
> of Stacks 06FN well behaved; of its three clauses only precomposition-stability is used here, so
> the hypothesis is taken in that weaker form and
> `AlgebraicGeometry.Space.IsSmoothLocalOnSourceAndTarget.precomp` is what a caller holding the
> full condition supplies. No hypothesis is made on the three categories beyond their being fibred
> in groupoids: the diagram is built from the two given ones, so no presentation of `𝒵` is chosen.
> See the implementation notes of this module, which also compare this with the sibling
> `AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_comp`.

```lean
theorem hasPropertyOnSomeSmoothDiagram_comp_of_precomp
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hprecomp : ∀ {X₀ Y₀ Z₀ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
      (_hX : IsAlgebraicSpace B S hS X₀) (_hY : IsAlgebraicSpace B S hS Y₀)
      (_hZ : IsAlgebraicSpace B S hS Z₀) (p : X₀ ⟶ Y₀) (q : Y₀ ⟶ Z₀),
      Space.IsSmooth B S hS p → P q → P (p ≫ q))
    (hcomp : ∀ {X₀ Y₀ Z₀ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
      (_hX : IsAlgebraicSpace B S hS X₀) (_hY : IsAlgebraicSpace B S hS Y₀)
      (_hZ : IsAlgebraicSpace B S hS Z₀) (p : X₀ ⟶ Y₀) (q : Y₀ ⟶ Z₀),
      P p → P q → P (p ≫ q))
    [(spaceProperty B S hS P).IsStableUnderBaseChange]
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : HasPropertyOnSomeSmoothDiagram B S hS P f)
    (hg : HasPropertyOnSomeSmoothDiagram B S hS P g) :
    HasPropertyOnSomeSmoothDiagram B S hS P (f ≫ g)
```

## Tag 06FQ, a remark

[Tag 06FQ](https://stacks.math.columbia.edu/tag/06FQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismBaseChange.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismBaseChange.lean#L529).

> A property of morphisms of algebraic spaces over `S` which is smooth local on the
> source-and-target and whose restriction to algebraic spaces is stable under base change induces,
> through the existential smooth-diagram criterion of Stacks 06FM, a property of 1-morphisms of
> algebraic stacks over `S` stable under arbitrary 2-fibre-product base change.

```lean
theorem hasPropertyOnSomeSmoothDiagram_baseChange
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (_hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    [hbase : (spaceProperty B S hS P).IsStableUnderBaseChange]
    {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (Q : Bicategory.TwoCommSq g f)
    (hQ : Bicategory.IsTwoFibreProduct Q)
    (hf : HasPropertyOnSomeSmoothDiagram B S hS P f.hom) :
    HasPropertyOnSomeSmoothDiagram B S hS P Q.fst.hom
```

## Tag 06PS, a remark

[Tag 06PS](https://stacks.math.columbia.edu/tag/06PS) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismMonotone.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismMonotone.lean#L80).

> **Stacks 06PS.** An implication between two properties of morphisms of algebraic spaces
> over `S` induces the same implication for 1-morphisms of algebraic stacks over `S`: the
> existential smooth-diagram criterion of Stacks 06FM is monotone in the property it tests.
>
> The same diagram witnesses both: its top horizontal morphism is a morphism of algebraic spaces
> and has the first property, hence the second.

```lean
theorem hasPropertyOnSomeSmoothDiagram_mono
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P P' : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hPP' : ∀ {U V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u},
      IsAlgebraicSpace B S hS U → IsAlgebraicSpace B S hS V →
      ∀ (g : U ⟶ V), P g → P' g)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (hf : HasPropertyOnSomeSmoothDiagram B S hS P f) :
    HasPropertyOnSomeSmoothDiagram B S hS P' f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.16, Tag 06FL](https://stacks.math.columbia.edu/tag/06FL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
