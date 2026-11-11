---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.hasPropertyOnEveryEtaleSmoothDiagram_iff_some, AlgebraicGeometry.Stack.hasPropertyOnSomeEtaleSmoothDiagram_iff_relative, AlgebraicGeometry.Stack.hasPropertyOnSomeEtaleSmoothDiagram_iff_represented, AlgebraicGeometry.Stack.HasEtaleSmoothLocalProperty, AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_comp, AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_comp_of_isEtaleSmoothLocal, AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_snd_of_isTwoFibreProduct_of_isStableUnderBaseChange, AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_baseChange
statement: formalized
proof: formalized
---

# 101.34 Types of morphisms étale-smooth local on source-and-target

Section 101.34 of the Stacks Project, [Tag 0CIE](https://stacks.math.columbia.edu/tag/0CIE). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CIF, a lemma

[Tag 0CIF](https://stacks.math.columbia.edu/tag/0CIF) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasPropertyOnEveryEtaleSmoothDiagram_iff_some`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismDiagramTests.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismDiagramTests.lean#L68). The attribute's comment: “equivalence of parts (1) and (2)”.

> **Stacks 0CIF, the equivalence of conditions (1) and (2).** Let `P` be a property of
> morphisms of algebraic spaces over `S` which is étale-smooth local on the source-and-target, and
> let `f : 𝒳 ⟶ 𝒴` be a Deligne–Mumford 1-morphism of algebraic stacks over `S`. Then the following
> are equivalent:
>
> 1. for every 2-commutative square of algebraic spaces `h : U → V` over `f` with `V → 𝒴` smooth
>    and `U → 𝒳 ×_𝒴 V` étale, the morphism `h` has `P`;
> 2. for some such square with `U → 𝒳` surjective, the morphism `h` has `P`.

```lean
theorem hasPropertyOnEveryEtaleSmoothDiagram_iff_some
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsDM B S hS f) :
    HasPropertyOnEveryEtaleSmoothDiagram B S hS P f ↔
      HasPropertyOnSomeEtaleSmoothDiagram B S hS P f
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeEtaleSmoothDiagram_iff_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismRelativeConverse.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismRelativeConverse.lean#L373). The attribute's comment: “representable morphism”.

> **The third assertion of Stacks 0CIF.** For an étale-smooth local property `P` of morphisms of
> algebraic spaces over `S` which is stable under base change and local at the target for the fppf
> precoverage, and a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by algebraic
> spaces, the existential étale-smooth diagram test for `P` is equivalent to the relative property
> `P` of Stacks 03YK.
>
> This is the covering set of the key `"representable morphism"` of Stacks 0CIF: the key names a
> single asserted equivalence, and neither half of it alone asserts that equivalence.

```lean
theorem hasPropertyOnSomeEtaleSmoothDiagram_iff_relative
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, v} B S hS)]
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    HasPropertyOnSomeEtaleSmoothDiagram B S hS P f ↔
      HasRelativeProperty.{u, u, u + 1, v} B S hS P f.hom hf
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeEtaleSmoothDiagram_iff_represented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismRepresented.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismRepresented.lean#L547). The attribute's comment: “representable source and target”.

> **Stacks 0CIF, the assertion for representable source and target.** For a property `P` of
> morphisms of algebraic spaces over `S` which is étale-smooth local on the source-and-target, and
> a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` whose source and target are representable
> by algebraic spaces `F` and `G`, the existential étale-smooth diagram test holds for `f` exactly
> when the induced morphism `F ⟶ G` of representing presheaves has `P`.
>
> Forward: the given diagram becomes a square of morphisms of algebraic spaces whose comparison to
> the fibre product is étale, and Stacks 0CG1 applies. Backward: test the condition on the diagram
> given by the two representing equivalences.

```lean
theorem hasPropertyOnSomeEtaleSmoothDiagram_iff_represented :
    HasPropertyOnSomeEtaleSmoothDiagram B S hS P f ↔
      P (ObjectProperty.homMk (representingMap B S hS 𝒳.val 𝒴.val F G eX eY f.hom) :
        (⟨F, hF⟩ : AlgebraicSpaces B S hS) ⟶ ⟨G, hG⟩)
```

## Tag 0CIG, a definition

[Tag 0CIG](https://stacks.math.columbia.edu/tag/0CIG) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasEtaleSmoothLocalProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean#L189). The attribute's comment: “the property of a DM morphism of algebraic stacks induced by an etale-smooth local property P of morphisms of algebraic spaces: IsDM f together with the universal etale-smooth diagram test at P, which is condition (1) of Stacks 0CIF”.

> **Stacks 0CIG.** The property of Deligne–Mumford morphisms of algebraic stacks induced by an
> étale-smooth local property `P` of morphisms of algebraic spaces over `S`: the morphism is
> Deligne–Mumford and passes the universal étale-smooth diagram test at `P`.
>
> For an étale-smooth local `P` — `AlgebraicGeometry.Space.IsEtaleSmoothLocalOnSourceAndTarget`,
> **Stacks 0CFZ** — Stacks 0CIF identifies that test with the existential one.

```lean
abbrev HasEtaleSmoothLocalProperty
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CIH, a remark

[Tag 0CIH](https://stacks.math.columbia.edu/tag/0CIH) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismComp.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismComp.lean#L208). The attribute's comment: “with the substantial direction of Stacks 06N3 as the explicit hypothesis hForward (the structure theorem behind it, Stacks 06MD, 06N0, 06N2, 06G2, 06G3, is absent from the library); it enters only through Stacks 0CIA, which supplies the surjective etale presentations of the two 2-fibre products the source's argument chooses”.

> **Stacks 0CIH.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> étale-smooth local on the source-and-target and stable under composition. Then the property of
> Deligne–Mumford 1-morphisms of algebraic stacks over `S` which **Stacks 0CIG** induces from `P`
> is stable under composition.
>
> The composite is Deligne–Mumford by **Stacks 050K**. For the diagram test, take a smooth chart
> `W ⟶ 𝒵` surjective on objects, an étale chart `V ⟶ 𝒴 ×_𝒵 W` and an étale chart `U ⟶ 𝒳 ×_𝒴 V`,
> the last two by **Stacks 0CIA**; the morphisms `V ⟶ W` and `U ⟶ V` have `P`, hence so does
> `U ⟶ W`, and pasting the two 2-fibre products exhibits `U` as an étale chart of `𝒳 ×_𝒵 W`.

```lean
theorem hasEtaleSmoothLocalProperty_comp
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    (hcomp : ∀ {X Y Z : AlgebraicSpaces B S hS} (p : X ⟶ Y) (q : Y ⟶ Z), P p → P q → P (p ≫ q))
    (hT : B.Contains (⊤_ Scheme.{u}))
    (hForward : ExistsEtalePresentationOfIsAbsolutelyDM.{u, w} B S hS hT)
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : HasEtaleSmoothLocalProperty B S hS P f)
    (hg : HasEtaleSmoothLocalProperty B S hS P g) :
    HasEtaleSmoothLocalProperty B S hS P (f ≫ g)
```

**`AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_comp_of_isEtaleSmoothLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismCompUnconditional.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismCompUnconditional.lean#L58).

> **Stacks 0CIH.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> étale-smooth local on the source-and-target and stable under composition. Then the property of
> Deligne–Mumford 1-morphisms of algebraic stacks over `S` which **Stacks 0CIG** induces from `P`
> is stable under composition: if `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` are DM and have it, so does
> `f ≫ g`.
>
> This is `AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_comp` with its argument `hForward`
> discharged by the unconditional forward direction of **Stacks 06N3**,
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM`, at
> `AlgebraicGeometry.BigFppfSite.contains_terminal`.

```lean
theorem hasEtaleSmoothLocalProperty_comp_of_isEtaleSmoothLocal
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    (hcomp : ∀ {X Y Z : AlgebraicSpaces B S hS} (p : X ⟶ Y) (q : Y ⟶ Z), P p → P q → P (p ≫ q))
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : HasEtaleSmoothLocalProperty B S hS P f)
    (hg : HasEtaleSmoothLocalProperty B S hS P g) :
    HasEtaleSmoothLocalProperty B S hS P (f ≫ g)
```

## Tag 0CII, a remark

[Tag 0CII](https://stacks.math.columbia.edu/tag/0CII) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_snd_of_isTwoFibreProduct_of_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismBaseChange.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismBaseChange.lean#L65).

> **Stacks 0CII.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> étale-smooth local on the source-and-target and stable under base change. If a Deligne–Mumford
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` has the property of Stacks 0CIG induced by
> `P`, then so does its base change `𝒳 ×_𝒴 𝒵 ⟶ 𝒵` along any 1-morphism `g : 𝒵 ⟶ 𝒴`, the second
> projection of any 2-fibre product square of `(f, g)`.

```lean
theorem hasEtaleSmoothLocalProperty_snd_of_isTwoFibreProduct_of_isStableUnderBaseChange
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    [P.IsStableUnderBaseChange]
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (R : Bicategory.TwoCommSq f g) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : HasEtaleSmoothLocalProperty B S hS P f) :
    HasEtaleSmoothLocalProperty B S hS P R.snd
```

**`AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismBaseChangeStable.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphismBaseChangeStable.lean#L146). The attribute's comment: “for the canonical 2-fibre product square of Stacks 003Q, which is the shape the library version of Stacks 050F is stated at, and with the substantial direction of Stacks 06N3 as the explicit hypothesis hForward (the structure theorem behind it, Stacks 06MD, 06N0, 06N2, 06G2, 06G3, is absent from the library); it enters only through Stacks 0CIA, which supplies the surjective etale presentation the source's argument chooses”.

> **Stacks 0CII.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> étale-smooth local on the source-and-target and stable under base change. Then the property of
> Deligne–Mumford 1-morphisms of algebraic stacks over `S` that **Stacks 0CIG** induces from `P`
> is inherited by the base change of a 1-morphism along the canonical 2-fibre product square.
>
> The Deligne–Mumford condition on the base change is **Stacks 050F**, and the diagram of
> condition (2) of **Stacks 0CIF** is the source's: its top-left corner is `V' ×_V U` for a smooth
> presentation `V ⟶ 𝒴`, a surjective étale presentation `U ⟶ 𝒳 ×_𝒴 V` and a smooth presentation
> `V' ⟶ 𝒵 ×_𝒴 V`, and its top horizontal morphism is the base change of `U ⟶ V` along
> `V' ⟶ V`.

```lean
theorem hasEtaleSmoothLocalProperty_baseChange
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    [P.IsStableUnderBaseChange]
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hForward : ExistsEtalePresentationOfIsAbsolutelyDM.{u, w} B S hS hZ)
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : HasEtaleSmoothLocalProperty B S hS P f) :
    HasEtaleSmoothLocalProperty B S hS P
      (AlgebraicStacks.twoFibreProductSquare B S hS f g).snd
```

## Tag 0CIJ, a remark

[Tag 0CIJ](https://stacks.math.columbia.edu/tag/0CIJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasEtaleSmoothLocalProperty_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean#L206).

> **Stacks 0CIJ.** An implication between properties of morphisms of algebraic spaces over `S`
> also holds for the properties of 1-morphisms of algebraic stacks that Stacks 0CIG induces from
> them. No étale-smooth locality hypothesis on either property is needed.

```lean
theorem hasEtaleSmoothLocalProperty_mono
    {P P' : MorphismProperty (AlgebraicSpaces B S hS)} (hPP' : P ≤ P')
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : HasEtaleSmoothLocalProperty B S hS P f) :
    HasEtaleSmoothLocalProperty B S hS P' f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.34, Tag 0CIE](https://stacks.math.columbia.edu/tag/0CIE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
