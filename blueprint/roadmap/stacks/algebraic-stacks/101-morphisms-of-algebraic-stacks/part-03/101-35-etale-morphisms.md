---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsEtale, AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isDM_comp_of_isEtale, AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isDM_baseChange_of_isEtale, AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_of_isOpenImmersion, AlgebraicGeometry.Stack.isEtale_of_etaleOnEveryAlgebraicSpaceDiagram, AlgebraicGeometry.Stack.isDM_of_hasEtaleAlgebraicSpaceCoverAfterFppfBaseChange
statement: formalized
proof: formalized
---

# 101.35 Étale morphisms

Section 101.35 of the Stacks Project, [Tag 0CIK](https://stacks.math.columbia.edu/tag/0CIK). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CIL, a definition

[Tag 0CIL](https://stacks.math.columbia.edu/tag/0CIL) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean#L228).

> **Stacks 0CIL.** A 1-morphism of algebraic stacks over `S` is *étale* when it is
> Deligne–Mumford and its universal étale-smooth diagram tests are étale morphisms of algebraic
> spaces, in the sense of `AlgebraicGeometry.Space.IsEtale` (**Stacks 03FR**).

```lean
abbrev IsEtale {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CIM, a lemma

[Tag 0CIM](https://stacks.math.columbia.edu/tag/0CIM) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismComp.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismComp.lean#L66).

> **Stacks 0CIM.** The composite of two étale 1-morphisms of algebraic stacks over `S` is
> étale, in the sense of **Stacks 0CIL**: it is Deligne–Mumford and passes the universal
> étale-smooth diagram test at étaleness of morphisms of algebraic spaces.
>
> This is **Stacks 0CIH** for the property `AlgebraicGeometry.Space.IsEtale`, which is
> étale-smooth local on the source-and-target (**Stacks 0CG3**) and stable under composition
> (**Stacks 0465**).

```lean
theorem isEtale_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    {f : 𝒳 ⟶ 𝒴} {g : 𝒴 ⟶ 𝒵}
    (hf : Stack.IsEtale B S hS f) (hg : Stack.IsEtale B S hS g) :
    Stack.IsEtale B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_comp_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismPermanence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismPermanence.lean#L94). The attribute's comment: “the Deligne–Mumford conjunct of the conclusion”.

> **The Deligne–Mumford conjunct of Stacks 0CIM.** A composite of two étale 1-morphisms of
> algebraic stacks over `S` is Deligne–Mumford.
>
> Étaleness of Stacks 0CIL contains the Deligne–Mumford condition of Stacks 04YW, and that
> condition is stable under composition by **Stacks 050K**.

```lean
theorem isDM_comp_of_isEtale {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : Stack.IsEtale B S hS f) (hg : Stack.IsEtale B S hS g) :
    Stack.IsDM B S hS (f ≫ g)
```

## Tag 0CIN, a lemma

[Tag 0CIN](https://stacks.math.columbia.edu/tag/0CIN) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismBaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismBaseChange.lean#L116).

> **Stacks 0CIN.** A base change of an étale 1-morphism of algebraic stacks over `S` is étale:
> if `f : 𝒳 ⟶ 𝒴` is étale and `Q` is any 2-fibre product of a cospan `(g : 𝒴' ⟶ 𝒴, f)`, then
> the projection `Q.fst : Q.pt ⟶ 𝒴'` is étale, both conjuncts of **Stacks 0CIL** included.
>
> The diagram of condition (2) of **Stacks 0CIF** for the Deligne–Mumford `f` is cut out by the
> surjective étale presentation of **Stacks 0CIA**, part (2), whose input, the substantial direction
> of **Stacks 06N3**, is `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM`.

```lean
theorem isEtale_baseChange {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    (hf : IsEtale B S hS f) :
    IsEtale B S hS Q.fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_baseChange_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismPermanence.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismPermanence.lean#L109). The attribute's comment: “the Deligne–Mumford conjunct of the conclusion”.

> **The Deligne–Mumford conjunct of Stacks 0CIN.** The projection to `𝒴'` of any 2-fibre
> product of a cospan `(g : 𝒴' ⟶ 𝒴, f : 𝒳 ⟶ 𝒴)` of 1-morphisms of algebraic stacks over `S` is
> Deligne–Mumford as soon as `f` is étale.
>
> Étaleness of Stacks 0CIL contains the Deligne–Mumford condition of Stacks 04YW, and that
> condition is inherited by base changes by **Stacks 050F**; a 2-fibre product of `(g, f)` is one
> of `(f, g)` with its two legs exchanged (**Stacks 003Q**), which turns the projection `Q.fst`
> into the second projection that Stacks 050F speaks about.

```lean
theorem isDM_baseChange_of_isEtale {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    (hf : Stack.IsEtale B S hS f) :
    Stack.IsDM B S hS Q.fst
```

## Tag 0CIP, a lemma

[Tag 0CIP](https://stacks.math.columbia.edu/tag/0CIP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleOpenImmersion.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleOpenImmersion.lean#L155).

> An open immersion of algebraic stacks over `S` is étale in the sense of Stacks 0CIL.

```lean
theorem isEtale_of_isOpenImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsOpenImmersion B S hS f) :
    Stack.IsEtale B S hS f
```

## Tag 0CIQ, a lemma

[Tag 0CIQ](https://stacks.math.columbia.edu/tag/0CIQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEtale_of_etaleOnEveryAlgebraicSpaceDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterion.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterion.lean#L110). The attribute's comment: “the implication (2) => (1)”.

> A Deligne–Mumford 1-morphism of algebraic stacks whose every algebraic-space diagram with
> étale comparisons has étale top horizontal morphism is étale.

```lean
theorem isEtale_of_etaleOnEveryAlgebraicSpaceDiagram
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : EtaleOnEveryAlgebraicSpaceDiagram B S hS f) : IsEtale B S hS f
```

**`AlgebraicGeometry.Stack.isDM_of_hasEtaleAlgebraicSpaceCoverAfterFppfBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterion.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterion.lean#L144). The attribute's comment: “the Deligne-Mumford half of the implication (3) => (1), for a site containing the terminal scheme”.

> If the big fppf site contains the terminal scheme, a 1-morphism `f` of algebraic stacks
> satisfying `AlgebraicGeometry.Stack.HasEtaleAlgebraicSpaceCoverAfterFppfBaseChange` is
> Deligne–Mumford.

```lean
theorem isDM_of_hasEtaleAlgebraicSpaceCoverAfterFppfBaseChange
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : HasEtaleAlgebraicSpaceCoverAfterFppfBaseChange B S hS f) : IsDM B S hS f
```

**`AlgebraicGeometry.Stack.isEtale_tfae_algebraicSpaceCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterionEquivalence.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleAlgebraicSpaceCriterionEquivalence.lean#L58).

> **Stacks 0CIQ.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
>
> 1. `f` is étale, `AlgebraicGeometry.Stack.IsEtale` (**Stacks 0CIL**);
> 2. `f` is Deligne–Mumford and for every `V ⟶ 𝒴` with `V` an algebraic space and every étale
>    `U ⟶ V ×_𝒴 𝒳` with `U` an algebraic space, `U ⟶ V` is étale,
>    `AlgebraicGeometry.Stack.EtaleOnEveryAlgebraicSpaceDiagram`;
> 3. there are a surjective, flat, locally finitely presented `W ⟶ 𝒴` with `W` an algebraic space
>    and a surjective étale `T ⟶ W ×_𝒴 𝒳` with `T` an algebraic space such that `T ⟶ W` is étale,
>    `AlgebraicGeometry.Stack.HasEtaleAlgebraicSpaceCoverAfterFppfBaseChange`.

```lean
theorem isEtale_tfae_algebraicSpaceCharts
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    List.TFAE [IsEtale B S hS f, EtaleOnEveryAlgebraicSpaceDiagram B S hS f,
      HasEtaleAlgebraicSpaceCoverAfterFppfBaseChange B S hS f]
```

## Tag 0CIR, a lemma

[Tag 0CIR](https://stacks.math.columbia.edu/tag/0CIR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_of_isEtale_over_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismBetweenEtaleStacks.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleMorphismBetweenEtaleStacks.lean#L52).

> **Stacks 0CIR.** Let `𝒳` and `𝒴` be algebraic stacks étale over an algebraic stack `𝒵`, with
> structure 1-morphisms `p : 𝒳 ⟶ 𝒵` and `q : 𝒴 ⟶ 𝒵`. Any 1-morphism `f : 𝒳 ⟶ 𝒴` over `𝒵`, i.e.
> with a 2-isomorphism `η : p ≅ f ≫ q`, is étale in the sense of Stacks 0CIL: Deligne–Mumford, and
> étale on every diagram of its universal étale-smooth test.
>
> This is
> `AlgebraicGeometry.Stack.isEtale_of_isEtale_over_base_of_isDeligneMumfordStack_twoFibreProduct`
> with its étale charts supplied by **Stacks 0CIA**, part (2),
> `Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM_algebraicSpace`.

```lean
theorem isEtale_of_isEtale_over_base {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒵) (q : 𝒴 ⟶ 𝒵) (η : p ≅ f ≫ q)
    (hp : Stack.IsEtale B S hS p) (hq : Stack.IsEtale B S hS q) : Stack.IsEtale B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_of_isEtale_over_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean#L191). The attribute's comment: “the Deligne-Mumford conjunct of the conclusion: a morphism between two stacks etale over a base is DM. The remaining conjunct of Tag 0CIL, the universal etale-smooth diagram condition, is not proved here”.

> **The Deligne–Mumford conjunct of Stacks 0CIR.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over `𝒵` whose structural 1-morphism `p : 𝒳 ⟶ 𝒵` is étale is Deligne–Mumford.
>
> Being over `𝒵` means `p ≅ f ≫ q`, so `f ≫ q` is Deligne–Mumford because `p` is étale, and
> Stacks 050M, part (1), cancels the second factor.

```lean
theorem isDM_of_isEtale_over_base {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒵) (q : 𝒴 ⟶ 𝒵) (η : p ≅ f ≫ q)
    (hp : Stack.IsEtale B S hS p) : Stack.IsDM B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.35, Tag 0CIK](https://stacks.math.columbia.edu/tag/0CIK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
