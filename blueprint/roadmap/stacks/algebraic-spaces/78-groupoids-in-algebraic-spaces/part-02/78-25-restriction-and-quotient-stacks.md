---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.fullyFaithful_quotientStackMap_iff_isPullback, AlgebraicGeometry.Space.isLocallySurjective_source_pullback_snd, AlgebraicGeometry.Space.isLocallySurjective_source_pullback_of_isFppfCovering_mapObjects, AlgebraicGeometry.Space.isLocallySurjective_source_pullback_of_isFppfCovering_self, AlgebraicGeometry.Stack.quotientStackMap_isEquivalenceOver_iff, AlgebraicGeometry.Stack.isTwoFibreProduct_functorialitySquare_of_isPullback, AlgebraicGeometry.Stack.isTwoFibreProduct_presentationQuotientMapSquare
statement: formalized
proof: formalized
---

# 78.25 Restriction and quotient stacks

Section 78.25 of the Stacks Project, [Tag 046R](https://stacks.math.columbia.edu/tag/046R). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 046S, a lemma

[Tag 046S](https://stacks.math.columbia.edu/tag/046S) in the Stacks Project.

**`AlgebraicGeometry.Stack.fullyFaithful_quotientStackMap_iff_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/FullFaithfulness.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/FullFaithfulness.lean#L370).

> **Stacks 046S.** The induced morphism of quotient stacks `[f] : [U/R] ⟶ [U'/R']` is fully
> faithful if and only if `R` is the restriction of `R'` along `f : U ⟶ U'`, i.e. if and only if
> the square formed by the arrow map of `f` and the two source–target maps is cartesian.

```lean
public theorem fullyFaithful_quotientStackMap_iff_isPullback
    {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H) :
    Nonempty (quotientStackMap f).toFunctor.FullyFaithful ↔
      IsPullback f.toGroupoidHom.mapArrows
        (prod.lift G.toGroupoidInFunctors.source G.toGroupoidInFunctors.target)
        (prod.lift H.toGroupoidInFunctors.source H.toGroupoidInFunctors.target)
        (prod.map f.toGroupoidHom.mapObjects f.toGroupoidHom.mapObjects)
```

## Tag 046T, a lemma

[Tag 046T](https://stacks.math.columbia.edu/tag/046T) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallySurjective_source_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean#L132). The attribute's comment: “surjective\_object\_map”.

> **Stacks 046T.** A map on objects which is surjective as a map of fppf sheaves stays
> surjective after passing to the arrows of the target groupoid whose target lifts through it and
> taking their sources.

```lean
theorem isLocallySurjective_source_pullback_snd
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicSpaces C S hS} {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H)
    (hf : Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      f.toGroupoidHom.mapObjects) :
    Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      (pullback.snd f.toGroupoidHom.mapObjects H.target.hom ≫ H.source.hom)
```

**`AlgebraicGeometry.Space.isLocallySurjective_source_pullback_of_isFppfCovering_mapObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean#L162). The attribute's comment: “fppf\_object\_map”.

> **Stacks 046T.** If the map on objects of a morphism of groupoids in algebraic spaces is an
> fppf covering, then every object of the target groupoid is fppf-locally the source of an arrow
> whose target lifts to the source groupoid.

```lean
theorem isLocallySurjective_source_pullback_of_isFppfCovering_mapObjects
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    (G H : GroupoidInAlgebraicSpaces C S hS B)
    (f : GroupoidInAlgebraicSpaces.Hom G H)
    (hf : IsFppfCovering C S hS (fun _ : PUnit => G.objects.obj)
      (fun _ => f.toGroupoidHom.mapObjects)) :
    Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      (pullback.snd f.toGroupoidHom.mapObjects H.target.hom ≫ H.source.hom)
```

**`AlgebraicGeometry.Space.isLocallySurjective_source_pullback_of_isFppfCovering_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean#L178). The attribute's comment: “fppf\_saturation”.

> **Stacks 046T.** If the arrows of the target groupoid whose target lifts to the source
> groupoid form an fppf covering of the object space of the target through their sources, then that
> saturation map is surjective as a map of fppf sheaves.

```lean
theorem isLocallySurjective_source_pullback_of_isFppfCovering_self
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicSpaces C S hS} {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H)
    (hf : IsFppfCovering C S hS
      (fun _ : PUnit => pullback f.toGroupoidHom.mapObjects H.target.hom)
      (fun _ => pullback.snd f.toGroupoidHom.mapObjects H.target.hom ≫ H.source.hom)) :
    Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      (pullback.snd f.toGroupoidHom.mapObjects H.target.hom ≫ H.source.hom)
```

**`AlgebraicGeometry.Stack.quotientStackMap_isEquivalenceOver_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/RestrictionCoverings.lean#L496). The attribute's comment: “equivalence\_criterion”.

> **Stacks 046T.** The induced morphism of quotient stacks `[f] : [U/R] ⟶ [U'/R']` is an
> equivalence over the big fppf site if and only if (1) `(U, R, s, t, c)` is the restriction of
> `(U', R', s', t', c')` along `f : U ⟶ U'`, i.e. the square formed by the arrow map of `f` and the
> two source–target maps is cartesian, and (2) the saturation map
> `U ×_{f, U', t'} R' ⟶ R' ⟶ U'` is a surjection of fppf sheaves.

```lean
public theorem quotientStackMap_isEquivalenceOver_iff
    {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H) :
    Nonempty (Functor.IsEquivalenceOver (quotientStack G).p (quotientStack H).p
      (quotientStackMap f).toFunctor) ↔
      (IsPullback f.toGroupoidHom.mapArrows
          (prod.lift G.toGroupoidInFunctors.source G.toGroupoidInFunctors.target)
          (prod.lift H.toGroupoidInFunctors.source H.toGroupoidInFunctors.target)
          (prod.map f.toGroupoidHom.mapObjects f.toGroupoidHom.mapObjects) ∧
        Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
          ((GroupoidInAlgebraicSpaces.fiberProductSnd
              (ObjectProperty.homMk f.toGroupoidHom.mapObjects : G.objects ⟶ H.objects)
              H.target ≫ H.source).hom))
```

## Tag 04ZN, a lemma

[Tag 04ZN](https://stacks.math.columbia.edu/tag/04ZN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isTwoFibreProduct_functorialitySquare_of_isPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/FunctorialityComparisonSurjectivity.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/FunctorialityComparisonSurjectivity.lean#L523).

> **Stacks 04ZN.** Let `φ : (U, R, s, t, c) ⟶ (U', R', s', t', c')` be a morphism of groupoids in
> algebraic spaces over an algebraic space `B` over a scheme `S` of a big fppf site, and suppose the
> square formed by the two **source** maps,
>
> ```
> R ---f---> R'
> |          |
> s          s'
> v          v
> U ---f---> U'
> ```
>
> is cartesian. Then the square
>
> ```
> 𝒮_U ----π----> [U/R]
>  |              |
> 𝒮_f            [φ]
>  v              v
> 𝒮_{U'} --π'--> [U'/R']
> ```
>
> of the projections of Stacks 044R, the induced 1-morphism of Stacks 046Q and the 1-morphism of
> Stacks 0458 **is a 2-fibre product** in the 2-category of stacks in groupoids over the big fppf
> site.
>
> Both halves of the proof consume the cartesian source square and nothing else:
> `AlgebraicGeometry.Stack.functorialityComparison_full` for fullness of the comparison
> 1-morphism — and faithfulness is free — and
> `AlgebraicGeometry.Stack.locallyEssSurjOnFibers_functorialityComparison` for local essential
> surjectivity on fibres. The reduction of the 2-fibre product property to those two is
> `AlgebraicGeometry.Stack.isTwoFibreProduct_functorialitySquare`.

```lean
noncomputable def isTwoFibreProduct_functorialitySquare_of_isPullback (φ : Hom G G')
    (hφ : IsPullback φ.toGroupoidHom.mapArrows G.source.hom G'.source.hom
      φ.toGroupoidHom.mapObjects) :
    Bicategory.IsTwoFibreProduct (functorialitySquare φ)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_presentationQuotientMapSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationQuotientMapSquare.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PresentationQuotientMapSquare.lean#L287). The attribute's comment: “in the 2-category of algebraic stacks, for a morphism into a presenting groupoid”.

> **The square of a morphism into a presenting groupoid is a 2-fibre product.** Let `𝒳` be an
> algebraic stack over `S` presented by a smooth groupoid `(U, R, s, t, c)` (Stacks 04TI), and let
> `φ : (U', R', s', t', c') ⟶ (U, R, s, t, c)` be a morphism from a smooth groupoid in algebraic
> spaces whose square of source maps
>
> ```
> R' --φ--> R
> |s'       |s
> v         v
> U' --φ--> U
> ```
>
> is cartesian. Then the square
> `AlgebraicGeometry.Stack.presentationQuotientMapSquare`
>
> ```
> 𝒮_{U'} ------> [U'/R']
>   |               |
>   v               v
> 𝒮_U   ------>     𝒳
> ```
>
> is a 2-fibre product in the 2-category of algebraic stacks over `S` (Stacks 03YP).

```lean
noncomputable def isTwoFibreProduct_presentationQuotientMapSquare
    (hφ : IsPullback φ.toGroupoidHom.mapArrows G'.source.hom P.groupoid.source.hom
      φ.toGroupoidHom.mapObjects) :
    Bicategory.IsTwoFibreProduct (presentationQuotientMapSquare B S hS P hG' φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.25, Tag 046R](https://stacks.math.columbia.edu/tag/046R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
