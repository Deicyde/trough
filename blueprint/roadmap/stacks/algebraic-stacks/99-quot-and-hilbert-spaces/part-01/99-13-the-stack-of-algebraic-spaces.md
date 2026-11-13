---
declaration: section
origin: cited
lean: AlgebraicGeometry.cartesianProperFlatInclusion, AlgebraicGeometry.fullyFaithfulCartesianProperFlatInclusion, AlgebraicGeometry.cartesianProperFlatInclusion_comp_cartesianFiniteTypeProjection, AlgebraicGeometry.CartesianFiniteTypeSpaces, AlgebraicGeometry.cartesianFiniteTypeProjection, AlgebraicGeometry.isProperFlatSpace, AlgebraicGeometry.CartesianProperFlatSpaces, AlgebraicGeometry.cartesianProperFlatProjection
statement: formalized
proof: formalized
---

# 99.13 The stack of algebraic spaces

Section 99.13 of the Stacks Project, [Tag 0D1D](https://stacks.math.columbia.edu/tag/0D1D). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D1D, the section

[Tag 0D1D](https://stacks.math.columbia.edu/tag/0D1D) in the Stacks Project.

**`AlgebraicGeometry.cartesianProperFlatInclusion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L130). The attribute's comment: “the subcategory of finitely presented, flat and proper families”.

> **Stacks 0D1D.** The inclusion
> `Spaces'_{fp, flat, proper} ⊂ Spaces'_{ft}` of the families of algebraic spaces that are of
> finite presentation, flat and proper over their base scheme into all the finite-type families,
> both taken with cartesian morphisms only.

```lean
abbrev cartesianProperFlatInclusion :
    CartesianProperFlatSpaces B S hS ⥤ CartesianFiniteTypeSpaces B S hS
```

**`AlgebraicGeometry.fullyFaithfulCartesianProperFlatInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L139). The attribute's comment: “the subcategory is full”.

> **Stacks 0D1D.** The subcategory `Spaces'_{fp, flat, proper}` of `Spaces'_{ft}` is *full*:
> a cartesian morphism of finite-type families whose source and target are of finite presentation,
> flat and proper is a morphism of `Spaces'_{fp, flat, proper}`, with no further condition.

```lean
def fullyFaithfulCartesianProperFlatInclusion :
    (cartesianProperFlatInclusion B S hS).FullyFaithful
```

**`AlgebraicGeometry.cartesianProperFlatInclusion_comp_cartesianFiniteTypeProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L147). The attribute's comment: “the projection of the subcategory is the restriction of the projection”.

> **Stacks 0D1D.** The projection `p'_{fp, flat, proper}` is the restriction of the projection
> `p'_{ft}` to the subcategory `Spaces'_{fp, flat, proper}`.

```lean
theorem cartesianProperFlatInclusion_comp_cartesianFiniteTypeProjection :
    cartesianProperFlatInclusion B S hS ⋙ cartesianFiniteTypeProjection B S hS =
      cartesianProperFlatProjection B S hS
```

Declarations registered for the tag:

- [`AlgebraicGeometry.CartesianFiniteTypeSpaces`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L147), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L156) (StacksFrontier): “the category of finite-type families”.
- [`AlgebraicGeometry.cartesianFiniteTypeProjection`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L153), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L159) (StacksFrontier): “the projection to the big fppf site”.
- [`AlgebraicGeometry.isProperFlatSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L168), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L162) (StacksFrontier): “the finitely presented, flat and proper condition”.
- [`AlgebraicGeometry.CartesianProperFlatSpaces`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L194), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L165) (StacksFrontier): “the category of finitely presented, flat and proper families”.
- [`AlgebraicGeometry.cartesianProperFlatProjection`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L201), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpaces.lean#L168) (StacksFrontier): “the projection of the subcategory to the big fppf site”.

## Tag 0D1E, a lemma

[Tag 0D1E](https://stacks.math.columbia.edu/tag/0D1E) in the Stacks Project.

**`AlgebraicGeometry.cartesianFiniteTypeProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L160). The attribute's comment: “finite-type families”.

> Finite-type algebraic spaces over varying base schemes, with cartesian squares as morphisms,
> form a category fibred in groupoids over the big fppf site of `S`.

```lean
theorem cartesianFiniteTypeProjection_isFiberedInGroupoids :
    (cartesianFiniteTypeProjection B S hS).IsFiberedInGroupoids
```

**`AlgebraicGeometry.cartesianProperFlatProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CartesianFamilies.lean#L209). The attribute's comment: “finitely presented, flat and proper families”.

> Algebraic spaces whose structure morphism is of finite presentation, flat and proper over a
> varying base scheme, with cartesian squares as morphisms, form a category fibred in groupoids over
> the big fppf site of `S`.

```lean
theorem cartesianProperFlatProjection_isFiberedInGroupoids :
    (cartesianProperFlatProjection B S hS).IsFiberedInGroupoids
```

## Tag 0D1F, a lemma

[Tag 0D1F](https://stacks.math.columbia.edu/tag/0D1F) in the Stacks Project.

**`AlgebraicGeometry.Space.hasAlgebraicIsomFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonal.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonal.lean#L512). The attribute's comment: “the Isom functor of two finitely presented, flat and proper families is an algebraic space, which is criterion (2) of Stacks 045G for the diagonal”.

> Criterion (2) of Stacks 045G in concrete form: the isomorphism functor of two finitely
> presented, flat and proper families over a scheme of the site is an algebraic space.

```lean
theorem hasAlgebraicIsomFunctors :
    HasAlgebraicIsomFunctors B S hS
```

**`AlgebraicGeometry.Space.hasRepresentableDiagonal_properFlatSpacesStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonal.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonal.lean#L540). The attribute's comment: “the diagonal is representable by algebraic spaces”.

> **Stacks 0D1F.** The diagonal
>
> ```text
>   Spaces'_{fp, flat, proper} ⟶ Spaces'_{fp, flat, proper} × Spaces'_{fp, flat, proper}
> ```
>
> is representable by algebraic spaces, assuming that the isomorphism presheaf of the fibre of the
> stack over a scheme `U` is algebraic whenever the isomorphism functors `Isom_U(Z, X)` of finitely
> presented, flat and proper families over `U` are (`hcmp`).

```lean
theorem hasRepresentableDiagonal_properFlatSpacesStack
    (hcmp : HasAlgebraicIsomFunctors B S hS →
      Stack.IsAlgebraicSpaceIsomPresheaf B S hS (properFlatSpacesStack B S hS)) :
    Stack.HasRepresentableDiagonal B S hS (properFlatSpacesStack B S hS)
```

**`AlgebraicGeometry.Space.properFlatSpacesStack_hasRepresentableDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonalUnconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesDiagonalUnconditional.lean#L69). The attribute's comment: “the diagonal is representable by algebraic spaces; Stacks 0D01 is proved, `AlgebraicGeometry.Space.hasHilbertModels`”.

> **The diagonal of `Spaces'_{fp, flat, proper}` is representable by algebraic spaces.** The
> diagonal
>
> ```text
>   Spaces'_{fp, flat, proper} ⟶ Spaces'_{fp, flat, proper} × Spaces'_{fp, flat, proper}
> ```
>
> of the stack of Stacks 0D1D over the big fppf site of `S` is representable by algebraic spaces.

```lean
theorem properFlatSpacesStack_hasRepresentableDiagonal :
    Stack.HasRepresentableDiagonal B S hS (properFlatSpacesStack B S hS)
```

## Tag 0D1G, a lemma

[Tag 0D1G](https://stacks.math.columbia.edu/tag/0D1G) in the Stacks Project.

**`AlgebraicGeometry.cartesianFiniteTypeProjection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean#L110). The attribute's comment: “Spaces'\_ft is fibred in groupoids and a stack (Stacks 02ZJ (3))”.

> **Stacks 0D1G**, the finite-type families, in the form of Stacks 02ZJ (3): `Spaces'_ft` is
> fibred in groupoids and is a stack over the big fppf site of `S` (Stacks 026F).

```lean
theorem cartesianFiniteTypeProjection_isStack :
    (cartesianFiniteTypeProjection B S hS).IsFiberedInGroupoids ∧
      (cartesianFiniteTypeProjection B S hS).IsStack (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.cartesianProperFlatProjection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean#L336). The attribute's comment: “Spaces'\_\{fp, flat, proper} is fibred in groupoids and a stack (Stacks 02ZJ (3))”.

> **Stacks 0D1G**, the finitely presented, flat and proper families, in the form of Stacks 02ZJ
> (3): `Spaces'_{fp, flat, proper}` is fibred in groupoids and is a stack over the big fppf site of
> `S` (Stacks 026F).

```lean
theorem cartesianProperFlatProjection_isStack :
    (cartesianProperFlatProjection B S hS).IsFiberedInGroupoids ∧
      (cartesianProperFlatProjection B S hS).IsStack (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.stackOfSpaces_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean#L346).

> **Stacks 0D1G.** The category `Spaces'_ft` is a stack in groupoids over the big fppf site of
> `S`, and so is `Spaces'_{fp, flat, proper}` (Stacks 02ZI).

```lean
theorem stackOfSpaces_isStackInGroupoids.{w} :
    (cartesianFiniteTypeProjection B S hS).IsStackInGroupoids.{w}
        (BigFppfOver.topology B S hS) ∧
      (cartesianProperFlatProjection B S hS).IsStackInGroupoids.{w}
        (BigFppfOver.topology B S hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.cartesianFiniteTypeProjection_isStackInGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesGroupoid.lean#L393), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean#L94) (StacksFrontier): “Spaces'\_ft is a stack in groupoids (Stacks 02ZI)”.
- [`AlgebraicGeometry.cartesianProperFlatProjection_isStackInGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesGroupoid.lean#L415), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesStack.lean#L329) (StacksFrontier): “Spaces'\_\{fp, flat, proper} is a stack in groupoids (Stacks 02ZI)”.

## Tag 0E93, a lemma

[Tag 0E93](https://stacks.math.columbia.edu/tag/0E93) in the Stacks Project.

**`AlgebraicGeometry.SpacesOverSpace.finiteTypeBaseChange_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean#L109). The attribute's comment: “the first equivalence: finite type morphisms X ⟶ T and functors 𝒮\_T ⟶ Spaces'\_ft”.

> **Stacks 0E93**, the first equivalence: finite type morphisms of algebraic spaces `X ⟶ T`,
> with isomorphisms over `T`, are equivalent through base change to the functors over the site from
> the algebraic stack `𝒮_T` of `T` to the stack `Spaces'_ft` of finite type families of algebraic
> spaces.

```lean
theorem finiteTypeBaseChange_isEquivalence : (finiteTypeBaseChange B S hS T).IsEquivalence
```

**`AlgebraicGeometry.SpacesOverSpace.properFlatBaseChange_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean#L119). The attribute's comment: “the second equivalence: finitely presented, flat and proper morphisms X ⟶ T and functors 𝒮\_T ⟶ Spaces'\_\{fp, flat, proper}”.

> **Stacks 0E93**, the second equivalence: finitely presented, flat and proper morphisms of
> algebraic spaces `X ⟶ T`, with isomorphisms over `T`, are equivalent through base change to the
> functors over the site from the algebraic stack `𝒮_T` of `T` to the stack
> `Spaces'_{fp, flat, proper}` of finitely presented, flat and proper families.

```lean
theorem properFlatBaseChange_isEquivalence : (properFlatBaseChange B S hS T).IsEquivalence
```

**`AlgebraicGeometry.SpacesOverSpace.spacesOverSpace_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/SpacesOverSpaceEquivalence.lean#L128). The attribute's comment: “both equivalences”.

> **Stacks 0E93.** Base change along the points of an algebraic space `T` gives an equivalence
> of finite type morphisms `X ⟶ T` with the functors over the site from `𝒮_T` to `Spaces'_ft`, and an
> equivalence of finitely presented, flat and proper morphisms `X ⟶ T` with the functors over the
> site from `𝒮_T` to `Spaces'_{fp, flat, proper}`.

```lean
theorem spacesOverSpace_isEquivalence :
    (finiteTypeBaseChange B S hS T).IsEquivalence ∧
      (properFlatBaseChange B S hS T).IsEquivalence
```

## Tag 0D1H, a remark

[Tag 0D1H](https://stacks.math.columbia.edu/tag/0D1H) in the Stacks Project.

**`AlgebraicGeometry.CartesianFiniteTypeSpacesOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean#L196). The attribute's comment: “the category of finite-type families over a base algebraic space”.

> **Stacks 0D1H.** The category `Z-Spaces'_{ft}` of finite-type families of algebraic spaces
> over a fixed algebraic space `Z`: an object is a finite-type family `X ⟶ T` of algebraic spaces
> together with a morphism from its base scheme to `Z`, and a morphism is a cartesian morphism of
> families commuting with those morphisms.

```lean
abbrev CartesianFiniteTypeSpacesOver
```

**`AlgebraicGeometry.isEquivalence_cartesianFiniteTypeSpacesOverToTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean#L227). The attribute's comment: “the 2-fibre product square for finite-type families”.

> **Stacks 0D1H** for finite-type families. The absolute and the relative categories of
> finite-type families of algebraic spaces form a 2-fibre product square over the big fppf site of
> `S`: the canonical comparison from the finite-type families over `Z` to the 2-fibre product of
> the finite-type families with the schemes over `Z` is an equivalence.

```lean
theorem isEquivalence_cartesianFiniteTypeSpacesOverToTwoFibreProduct :
    (cartesianFiniteTypeSpacesOverToTwoFibreProduct B S hS Z).IsEquivalence
```

**`AlgebraicGeometry.CartesianProperFlatSpacesOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean#L237). The attribute's comment: “the category of finitely presented, flat and proper families over a base space”.

> **Stacks 0D1H.** The category `Z-Spaces'_{fp, flat, proper}` of finitely presented, flat and
> proper families of algebraic spaces over a fixed algebraic space `Z`: an object is such a family
> `X ⟶ T` together with a morphism from its base scheme to `Z`, and a morphism is a cartesian
> morphism of families commuting with those morphisms.

```lean
abbrev CartesianProperFlatSpacesOver
```

**`AlgebraicGeometry.isEquivalence_cartesianProperFlatSpacesOverToTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/FamiliesOverBaseSpace.lean#L268). The attribute's comment: “the 2-fibre product square for finitely presented, flat and proper families”.

> **Stacks 0D1H** for finitely presented, flat and proper families. The absolute and the
> relative categories of finitely presented, flat and proper families of algebraic spaces form a
> 2-fibre product square over the big fppf site of `S`: the canonical comparison from such families
> over `Z` to the 2-fibre product of such families with the schemes over `Z` is an equivalence.

```lean
theorem isEquivalence_cartesianProperFlatSpacesOverToTwoFibreProduct :
    (cartesianProperFlatSpacesOverToTwoFibreProduct B S hS Z).IsEquivalence
```

## Tag 0D1I, a lemma

[Tag 0D1I](https://stacks.math.columbia.edu/tag/0D1I) in the Stacks Project.

**`AlgebraicGeometry.isLimitPreserving_cartesianProperFlatFiberedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesLimitPreservingUnconditional.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StackOfSpacesLimitPreservingUnconditional.lean#L187). The attribute's comment: “over the big fppf site of an arbitrary base scheme `S`; the source's `Sch_fppf` is `S = Spec(ℤ)`”.

> The stack `p'_{fp, flat, proper} : Spaces'_{fp, flat, proper} ⟶ Sch_fppf` of finitely
> presented, flat and proper families of algebraic spaces is limit preserving (Stacks 07XL): for
> every directed inverse system of affine schemes `Tᵢ` of the site with limit `T` in the site, base
> change is an equivalence from the colimit of the fibre categories over the `Tᵢ` to the fibre
> category over `T`.
>
> The base is the big fppf site of an arbitrary scheme `S` of the site, which recovers `Sch_fppf` at
> `S = Spec(ℤ)`; the index categories are those of the scheme universe, the smallness of the directed
> sets of Stacks 07XL.

```lean
theorem isLimitPreserving_cartesianProperFlatFiberedCategory
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u + 1} B S hS
      (cartesianProperFlatFiberedCategory B S hS)
```

## Tag 0D1J, a lemma

[Tag 0D1J](https://stacks.math.columbia.edu/tag/0D1J) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushoutRS`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProperPushoutGluingUnconditional.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProperPushoutGluingUnconditional.lean#L44).

> **[Stacks Project, Tag 0D1J].** For every pushout `S' = S ⨿_T T'` of schemes of the site
> along a thickening `T ⟶ T'` and an affine morphism `T ⟶ S`, the canonical restriction functor
> from the finitely presented, flat and proper algebraic spaces over `S'` to the compatible pairs
> of such spaces over `S` and `T'` is an equivalence.

```lean
def properPushoutRS : ProperPushoutRS B S₀ hS₀
```

## Tag 0D1K, a lemma

[Tag 0D1K](https://stacks.math.columbia.edu/tag/0D1K) in the Stacks Project.

**`AlgebraicGeometry.ProperFlatSpaceDeformation.finiteDimensional_predeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProperFlatStackFiniteDimensional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatStackFiniteDimensional.lean#L69). The attribute's comment: “(1): for a field k of finite type over Z and an object x of Spaces'\_\{fp,flat,proper} over Spec k, the predeformation category F\_\{X,k,x} over C\_Z is a deformation category whose tangent space T F\_\{X,k,x} and infinitesimal automorphisms Inf(F\_\{X,k,x}) (Section 07WY) are finite dimensional”.

> Let `k` be a field of finite type over `ℤ` and let `x = (X → Spec k)` be an object of
> `𝒳 = Spaces'_{fp, flat, proper}` over `Spec k`. Then the predeformation category `𝓕_{𝒳,k,x}` of
> Stacks 07T2, over `𝒞_ℤ`, is a deformation category, its tangent space `T𝓕_{𝒳,k,x}` is a
> finite-dimensional `k`-vector space, and so are its infinitesimal automorphisms
> `Inf(𝓕_{𝒳,k,x})` (Stacks 07WY), at every object of the special fibre and for every choice of its
> pushforwards.
>
> The stack is formed over the big fppf site of `Spec ℤ`, and `𝓕_{𝒳,k,x}` over `𝒞_Λ` with `Λ = ℤ`,
> `Spec Λ = Spec ℤ` the affine open of the base containing the image of `Spec k` (Stacks 07T2).

```lean
theorem finiteDimensional_predeformationCategory {k : Type u} [Field k]
    [Algebra (ULift.{u} ℤ) k] [Algebra.FiniteType (ULift.{u} ℤ) k]
    (x : CartesianProperFlatSpaces B integerBase hZ)
    (hx : (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion).obj x =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap (ULift.{u} ℤ) k)) ≫ 𝟙 integerBase)) :
    ∃ hD : IsDeformationCategory.{u, u, u} (predeformationCategory (𝟙 integerBase)
        (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion) x hx).projection,
      (letI : Fact (IsPredeformationCategory (BasedCategory.ofFunctor (predeformationCategory
          (𝟙 integerBase) (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion)
            x hx).projection).p) := ⟨hD.predeformation⟩;
        letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
          (isomorphismClasses (BasedCategory.ofFunctor (predeformationCategory (𝟙 integerBase)
            (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion) x
              hx).projection) hD.predeformation.cofibered))) := ⟨tangentConditionS2.{u, u, u} hD⟩;
        FiniteDimensional k (artinianTangentSpace (ULift.{u} ℤ) k
          (isomorphismClasses (BasedCategory.ofFunctor (predeformationCategory (𝟙 integerBase)
            (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion) x
              hx).projection) hD.predeformation.cofibered))) ∧
      ∀ y, (predeformationCategory (𝟙 integerBase)
          (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion) x
            hx).projection.obj y = residueFieldObject.{u, u, u} (ULift.{u} ℤ) k →
        ∀ PF : ChosenPushforwardsAt (predeformationCategory (𝟙 integerBase)
            (cartesianProperFlatProjection B integerBase hZ ⋙ Over.post B.inclusion) x
              hx).projection y,
          FiniteDimensional k ↥((infinitesimalAutomorphismLinearLift.{u, u, u} PF
            hD.satisfiesRS).functor.obj (FGModuleCat.of k (ULift.{u} k)))
```

**`AlgebraicGeometry.ProperFlatSpaceDeformation.finiteDimensional_tangentFunctor_infinitesimalAutomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProperFlatStackFiniteDimensional.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatStackFiniteDimensional.lean#L114). The attribute's comment: “(2): for an object x of Spaces'\_\{fp,flat,proper} over a field k, the functors T\_x and Inf\_x of Stacks 07Y9 exist (the stack satisfies RS* by 0D1J) and T\_x(k) and Inf\_x(k) are finite dimensional; both finiteness statements hold for every k-linear functor carrying the identifications of 07Y9”.

> Let `k` be a field and let `x = (X → Spec k)` be an object of
> `𝒳 = Spaces'_{fp, flat, proper}` over `Spec k`. Then the tangent functor `T_x` and the functor of
> infinitesimal automorphisms `Inf_x` of Stacks 07Y9 (Section 07Y6) exist — `𝒳` satisfies (RS*) by
> Stacks 0D1J — and `T_x(k)` and `Inf_x(k)` are finite-dimensional `k`-vector spaces.
>
> Each functor is stated as a structure (`TangentFunctorData`,
> `InfinitesimalAutomorphismFunctorData`) carrying a `k`-linear functor on the site modules together
> with its identification with the isomorphism classes of lifts of `x`, respectively with the
> infinitesimal automorphisms of the trivial lifts of `x`, natural in the module. The statement gives
> that such a functor exists and that the value at `k` of *every* such functor is finite-dimensional,
> so it holds for the functors `T_x` and `Inf_x` of Stacks 07Y9, which are determined by these
> identifications. No condition on `k` is assumed.

```lean
theorem finiteDimensional_tangentFunctor_infinitesimalAutomorphismFunctor {k : Type u} [Field k]
    (toS : Spec (.of k) ⟶ integerBase) (hk : B.Contains (Spec (.of k)))
    (x : CartesianProperFlatSpaces B integerBase hZ)
    (hx : (cartesianProperFlatProjection B integerBase hZ).obj x =
      algebraOver k B integerBase hZ toS hk) :
    (Nonempty (TangentFunctorData k B integerBase hZ toS hk
        (cartesianProperFlatProjection B integerBase hZ) x hx) ∧
      ∀ T : TangentFunctorData k B integerBase hZ toS hk
          (cartesianProperFlatProjection B integerBase hZ) x hx,
        FiniteDimensional k (T.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k)))) ∧
    (Nonempty (InfinitesimalAutomorphismFunctorData k B integerBase hZ toS hk
        (cartesianProperFlatProjection B integerBase hZ) x hx
        (cartesianProperFlatProjection_isFiberedInGroupoids B integerBase hZ)) ∧
      ∀ I : InfinitesimalAutomorphismFunctorData k B integerBase hZ toS hk
          (cartesianProperFlatProjection B integerBase hZ) x hx
          (cartesianProperFlatProjection_isFiberedInGroupoids B integerBase hZ),
        FiniteDimensional k (I.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k))))
```

## Tag 0D3X, a lemma

[Tag 0D3X](https://stacks.math.columbia.edu/tag/0D3X) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.openVersalityOf_cartesianProperFlat`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatOpennessOfVersalityOfDiagonal.lean#L110), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/ProperFlatOpennessOfVersalityTags.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatOpennessOfVersalityTags.lean#L26) (StacksFrontier): “both assertions: over any locally Noetherian base scheme, in particular `Spec(ℤ)` and, after base change, any Noetherian scheme `S`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.13, Tag 0D1D](https://stacks.math.columbia.edu/tag/0D1D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
