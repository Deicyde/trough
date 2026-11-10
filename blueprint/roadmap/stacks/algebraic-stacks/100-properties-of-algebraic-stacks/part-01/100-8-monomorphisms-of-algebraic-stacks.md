---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism, AlgebraicStacks.isMonomorphism_fst_twoFibreProductSquareAlgebraicStacks, AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_comp, AlgebraicGeometry.Stack.mono_hom_representingMaps_of_full_and_faithful, AlgebraicGeometry.Stack.mono_representingMaps_of_full_and_faithful, AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_of_full_and_faithful, AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_tfae_of_bootstrap, AlgebraicGeometry.Stack.AlgebraicStacks.full_and_faithful_homFunctor_of_isMonomorphism
statement: formalized
proof: formalized
---

# 100.8 Monomorphisms of algebraic stacks

Section 100.8 of the Stacks Project, [Tag 04ZV](https://stacks.math.columbia.edu/tag/04ZV). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04ZW, a definition

[Tag 04ZW](https://stacks.math.columbia.edu/tag/04ZW) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean#L109).

> **Stacks 04ZW.** A 1-morphism of algebraic stacks over `S` is a *monomorphism* when it is
> representable by algebraic spaces and every algebraic space representing one of its base changes
> along a scheme-valued point of the target has structural morphism a monomorphism of algebraic
> spaces over `S`.
>
> This is `AlgebraicGeometry.Stack.HasRelativeProperty` (**Stacks 03YK**, the Section 04XB notion
> the source refers to) at the monomorphisms, written out rather than invoked; see the
> implementation notes.

```lean
abbrev AlgebraicStacks.IsMonomorphism
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 04ZX, a lemma

[Tag 04ZX](https://stacks.math.columbia.edu/tag/04ZX) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicStacks.isMonomorphism_fst_twoFibreProductSquareAlgebraicStacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicStacks.isMonomorphism_fst_twoFibreProductSquareAlgebraicStacks#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismPermanence.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismPermanence.lean#L82) (StacksFrontier).

## Tag 04ZY, a lemma

[Tag 04ZY](https://stacks.math.columbia.edu/tag/04ZY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismPermanence.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismPermanence.lean#L65).

> **Stacks 04ZY.** A composite of monomorphisms of algebraic stacks over `S` (**Stacks 04ZW**)
> is a monomorphism.

```lean
theorem isMonomorphism_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsMonomorphism B S hS f) (hg : IsMonomorphism B S hS g) :
    IsMonomorphism B S hS (f ≫ g)
```

## Tag 04ZZ, a lemma

[Tag 04ZZ](https://stacks.math.columbia.edu/tag/04ZZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.mono_hom_representingMaps_of_full_and_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean#L198). The attribute's comment: “(2) implies (1), the monomorphism clause for categories fibred in groupoids”.

> **The implication (2) ⟹ (1) of Stacks 04ZZ.** A fully faithful 1-morphism `j : 𝒳 ⟶ 𝒴` of
> categories fibred in groupoids over the big fppf site of `S` is a monomorphism in the sense of
> Stacks 04XB: every algebraic space representing a base change of `j` along a scheme-valued point
> of `𝒴` has monomorphic structural morphism.
>
> This is the converse of
> `AlgebraicGeometry.Stack.full_and_faithful_homFunctor_of_mono_representingMaps`, and it carries
> no representability hypothesis.

```lean
theorem mono_hom_representingMaps_of_full_and_faithful
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (j : 𝒳 ⟶ 𝒴)
    (hfull : (CatFiberedInGroupoids.homFunctor j).Full)
    (hfaithful : (CatFiberedInGroupoids.homFunctor j).Faithful)
    (U : BigFppfOver B S hS)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
    (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
    (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B U.left.1 U.left.2 F)
    (he : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
        (CatFiberedInGroupoids.homFunctor j))
      (presheafOfCategories (F ⋙ typeToCat)).p)) :
    Mono (algebraicSpaceMap B S hS U
      ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.mono_representingMaps_of_full_and_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean#L222). The attribute's comment: “(2) implies (1), the monomorphism clause read in the category of algebraic spaces over S”.

> **The implication (2) ⟹ (1) of Stacks 04ZZ, in the category of algebraic spaces.** This is
> `AlgebraicGeometry.Stack.mono_hom_representingMaps_of_full_and_faithful` read in the category of
> algebraic spaces over `S`, which is the form the relative properties of Stacks 03YK — and hence
> `AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism` — are stated in.

```lean
theorem mono_representingMaps_of_full_and_faithful
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (j : 𝒳 ⟶ 𝒴)
    (hfull : (CatFiberedInGroupoids.homFunctor j).Full)
    (hfaithful : (CatFiberedInGroupoids.homFunctor j).Faithful)
    (U : BigFppfOver B S hS)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
    (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
    (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B U.left.1 U.left.2 F)
    (he : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
        (CatFiberedInGroupoids.homFunctor j))
      (presheafOfCategories (F ⋙ typeToCat)).p)) :
    Mono (algebraicSpaceMap B S hS U
      ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_of_full_and_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FullyFaithfulMonomorphism.lean#L251). The attribute's comment: “(2) implies (1) for 1-morphisms of algebraic stacks”.

> **The implication (2) ⟹ (1) of Stacks 04ZZ, for a 1-morphism of algebraic stacks.** A fully
> faithful 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is a monomorphism in the sense of
> **Stacks 04ZW**.
>
> The representability conjunct of `AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism` is the
> implication (2) ⟹ (3) of Stacks 04Y5,
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_faithful`;
> the monomorphy conjunct is `AlgebraicGeometry.Stack.mono_representingMaps_of_full_and_faithful`.

```lean
theorem isMonomorphism_of_full_and_faithful
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hfull : (CatFiberedInGroupoids.homFunctor f.hom).Full)
    (hfaithful : (CatFiberedInGroupoids.homFunctor f.hom).Faithful) :
    AlgebraicStacks.IsMonomorphism B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_tfae_of_bootstrap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismEquivalentConditions.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismEquivalentConditions.lean#L217).

> **Stacks 04ZZ.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following
> are equivalent:
>
> 1. `f` is a monomorphism (Stacks 04ZW);
> 2. `f` is fully faithful;
> 3. the diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` is an equivalence;
> 4. there are an algebraic space `W` and a surjective, flat, locally finitely presented
>    `W ⟶ 𝒴` such that `V = 𝒳 ×_𝒴 W` is an algebraic space and `V ⟶ W` is a monomorphism.
>
> (1) ⟹ (2) is Stacks 05UK, (2) ⟺ (3) is Stacks 04Z7, (2) ⟹ (1) is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_of_full_and_faithful` (through
> Stacks 04Y5), (1) ⟹ (4) is
> `AlgebraicGeometry.Stack.AlgebraicStacks.hasMonomorphicFppfSpaceBaseChange_of_isMonomorphism` and
> (4) ⟹ (2) is `full_and_faithful_homFunctor_of_hasMonomorphicFppfSpaceBaseChange`.

```lean
theorem isMonomorphism_tfae_of_bootstrap (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [IsMonomorphism B S hS f,
        (CatFiberedInGroupoids.homFunctor f.hom).Full ∧
          (CatFiberedInGroupoids.homFunctor f.hom).Faithful,
        (CatFiberedInGroupoids.homFunctor
          (relativeDiagonalAlgebraicStacks B S hS f).hom).IsEquivalence,
        HasMonomorphicFppfSpaceBaseChange B S hS f]
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.full_and_faithful_homFunctor_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismFullyFaithful.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismFullyFaithful.lean#L333). The attribute's comment: “the implication (1) ⟹ (2): a monomorphism of algebraic stacks is fully faithful”.

> **The implication (1) ⟹ (2) of Stacks 04ZZ: a monomorphism of algebraic stacks is fully
> faithful.** A 1-morphism of algebraic stacks over `S` which is a monomorphism in the sense of
> **Stacks 04ZW** has fully faithful underlying functor.
>
> This is `AlgebraicGeometry.Stack.full_and_faithful_homFunctor_of_mono_representingMaps`
> (**Stacks 05UK** with Stacks 003Z) read in the 2-category of algebraic stacks of Stacks 03YP. The
> representability witness is the first conjunct of Stacks 04ZW, and its second conjunct gives the
> monomorphy of each representing structural morphism in the category of algebraic spaces over `S`,
> which **Stacks 042M** turns into monomorphy of the underlying morphism of presheaves.

```lean
theorem full_and_faithful_homFunctor_of_isMonomorphism (f : 𝒳 ⟶ 𝒴)
    (hf : IsMonomorphism B S hS f) :
    (CatFiberedInGroupoids.homFunctor f.hom).Full ∧
      (CatFiberedInGroupoids.homFunctor f.hom).Faithful
```

## Tag 0500, a lemma

[Tag 0500](https://stacks.math.columbia.edu/tag/0500) in the Stacks Project.

**`AlgebraicGeometry.Stack.pointsMap_injective_of_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsInjective.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsInjective.lean#L37).

> A monomorphism of algebraic stacks induces an injective map on points.

```lean
public theorem pointsMap_injective_of_fullyFaithful
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴)
    [Functor.Full (CatFiberedInGroupoids.homFunctor f.hom)]
    [Functor.Faithful (CatFiberedInGroupoids.homFunctor f.hom)] :
    Function.Injective
      (pointsMap B S hS 𝒳.val.val
        (Classical.choose 𝒳.property) (Classical.choose 𝒴.property) f.hom.hom)
```

## Tag 0CBB, a lemma

[Tag 0CBB](https://stacks.math.columbia.edu/tag/0CBB) in the Stacks Project.

**`AlgebraicGeometry.Stack.isTwoFibreProduct_monomorphismDiagonalSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDiagonalSquare.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDiagonalSquare.lean#L171).

> **Stacks 0CBB.** Let `f : 𝒳 ⟶ 𝒳'` and `g : 𝒳' ⟶ 𝒴` be 1-morphisms of algebraic stacks over
> `S`. If `f` is a monomorphism (Stacks 04ZW), then the canonical square
>
> ```text
>   𝒳  --Δ_{𝒳/𝒴}-->  𝒳 ×_𝒴 𝒳
>   |                     |
>  f|                     | f × f
>   v                     v
>   𝒳' --Δ_{𝒳'/𝒴}--> 𝒳' ×_𝒴 𝒳'
> ```
>
> `AlgebraicGeometry.Stack.monomorphismDiagonalSquare` is a 2-fibre product in the 2-category of
> algebraic stacks over `(Sch/S)_fppf`.
>
> This is the source's proof: `𝒳 = 𝒳 ×_{𝒳'} 𝒳` by **Stacks 04ZZ**, the relative diagonal of the
> monomorphism `f` being an equivalence, and the square is then the 2-cartesian square of
> **Stacks 04Z1** precomposed with that equivalence.

```lean
def isTwoFibreProduct_monomorphismDiagonalSquare (f : 𝒳 ⟶ 𝒳') (g : 𝒳' ⟶ 𝒴)
    (hf : AlgebraicStacks.IsMonomorphism B S hS f) :
    IsTwoFibreProduct (monomorphismDiagonalSquare B S hS f g)
```

**`CategoryTheory.Limits.CategoricalPullback.isEquivalence_monomorphism_diagonalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/MonomorphismDiagonal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/MonomorphismDiagonal.lean#L94).

> **Stacks 0CBB.** The square from the relative diagonal of a fully faithful functor `f` to
> the relative diagonal of `f ⋙ g` is a 2-fibre product square: the induced functor into the
> explicit 2-fibre product is an equivalence.
>
> It is the composite of the relative diagonal of `f`, an equivalence because `f` is fully
> faithful, with the Stacks 04Z1 comparison functor.

```lean
theorem isEquivalence_monomorphism_diagonalComparison
    {X X' Y : Type*} [Category X] [Category X'] [Category Y]
    (f : X ⥤ X') (g : X' ⥤ Y) (hf : f.Full ∧ f.Faithful) :
    (relativeDiagonal f ⋙ toRelativeDiagonalPullback f f g).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.8, Tag 04ZV](https://stacks.math.columbia.edu/tag/04ZV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
