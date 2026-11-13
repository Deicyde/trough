---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_fibredCategory, AlgebraicGeometry.BigFppfOver.isLimitPreservingOnObjects_baseChange, AlgebraicGeometry.BigFppfOver.isLimitPreservingOnObjects_comp, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_iff_isLocallyOfFinitePresentation, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isOpenImmersion_of_univLE, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_limitPreservingOnObjects, AlgebraicGeometry.Stack.hasRelativeProperty_of_affine_locallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 97.5 Limit preserving on objects

Section 97.5 of the Stacks Project, [Tag 06CT](https://stacks.math.columbia.edu/tag/06CT). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06CU, an equation

[Tag 06CU](https://stacks.math.columbia.edu/tag/06CU) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean#L67).

> **Stacks 06CU.** A morphism of categories fibred in groupoids is limit preserving on
> objects: every comparison over an affine inverse limit descends, with the comparison square
> commuting.

```lean
def IsLimitPreservingOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : CatFiberedInGroupoids (BigFppfOver B S hS)) (p : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_fibredCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/LimitPreservingPresheafStack.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/LimitPreservingPresheafStack.lean#L71). The attribute's comment: “the criterion for the category fibred in sets attached to a set-valued presheaf: limit preservation on objects of its structure morphism follows from descent of the presheaf's sections along inverse limits of affine objects”.

> If every section of `F` over an inverse limit of affine objects of the site descends to a
> stage below a prescribed index, then the structure morphism of the category `𝒮_F` fibred in sets
> attached to `F` is limit preserving on objects.

```lean
public theorem isLimitPreservingOnObjects_fibredCategory (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : DescendsOnAffineLimits.{u, v, w} B S hS F) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, v, w} B S hS
      (fibredCategory B S hS F)
      (Deformation.Artin.Approximation.baseFiberedCategory B S hS)
      (Deformation.Artin.Approximation.structureMorphism B S hS
        (fibredCategory B S hS F))
```

## Tag 06CV, a lemma

[Tag 06CV](https://stacks.math.columbia.edu/tag/06CV) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isLimitPreservingOnObjects_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean#L127).

> **Stacks 06CV.** Limit preservation on objects is stable under base change.

```lean
theorem isLimitPreservingOnObjects_baseChange
    (hp : IsLimitPreservingOnObjects.{u, v, w} B S hS 𝒳 𝒴 p) :
    IsLimitPreservingOnObjects.{u, v, w} B S hS
      (twoFibreProduct B S hS 𝒳 𝒴 𝒵 p q) 𝒵
      (twoFibreProductSnd B S hS 𝒳 𝒴 𝒵 p q)
```

## Tag 06CW, a lemma

[Tag 06CW](https://stacks.math.columbia.edu/tag/06CW) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isLimitPreservingOnObjects_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LimitPreservingOnObjects.lean#L286).

> **Stacks 06CW.** The composite of two morphisms of categories fibred in groupoids that are
> limit preserving on objects is limit preserving on objects.

```lean
theorem isLimitPreservingOnObjects_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : IsLimitPreservingOnObjects.{u, v, w} B S hS 𝒳 𝒴 p)
    (hq : IsLimitPreservingOnObjects.{u, v, w} B S hS 𝒴 𝒵 q) :
    IsLimitPreservingOnObjects.{u, v, w} B S hS 𝒳 𝒵 (p ≫ q)
```

## Tag 06CX, a lemma

[Tag 06CX](https://stacks.math.columbia.edu/tag/06CX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_iff_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingFinitePresentation.lean, line 883](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingFinitePresentation.lean#L883). The attribute's comment: “index categories in the universe of the schemes”.

> **Stacks 06CX.** A 1-morphism of categories fibred in groupoids over the big fppf site of `S`
> which is representable by algebraic spaces is limit preserving on objects exactly when it is
> locally of finite presentation in the sense of Stacks 03YK: every algebraic space representing a
> base change of it along a scheme-valued point of the target has locally finitely presented
> structural morphism.

```lean
theorem isLimitPreservingOnObjects_iff_isLocallyOfFinitePresentation
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : CatFiberedInGroupoids (AlgebraicGeometry.BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴)
    (hp : AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom) :
    AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u} B S hS 𝒳 𝒴 p ↔
      ∀ (U : AlgebraicGeometry.BigFppfOver B S hS)
        (y : AlgebraicGeometry.BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
        (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
        (F : (AlgebraicGeometry.BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : AlgebraicGeometry.IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
            (CatFiberedInGroupoids.homFunctor p))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        AlgebraicGeometry.Space.IsLocallyOfFinitePresentation B S hS
          (AlgebraicGeometry.algebraicSpaceMap B S hS U
            ((AlgebraicGeometry.spacesOverSmallerBaseFunctor
              B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

## Tag 06CY, a lemma

[Tag 06CY](https://stacks.math.columbia.edu/tag/06CY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isOpenImmersion_of_univLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingOpenImmersion.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingOpenImmersion.lean#L168). The attribute's comment: “index categories range over all cofiltered categories whose objects and morphisms lie in universes bounded by that of the schemes, which covers the directed sets of the source”.

> **Stacks 06CY.** A 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces and an open immersion in the sense of Stacks 04XB
> is limit preserving on objects, for every index category whose objects and morphisms form sets,
> that is, live in universes `vI` and `wI` bounded by the universe `u` of the schemes.
>
> The directed systems of the source are sets, so these are exactly its index categories. Such an
> index category is equivalent to one in the universe `u`, and the condition there is
> `AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isOpenImmersion`; the transport is
> `AlgebraicGeometry.BigFppfOver.isLimitPreservingOnObjects_of_univLE`.

```lean
theorem isLimitPreservingOnObjects_of_isOpenImmersion_of_univLE
    [UnivLE.{vI, u}] [UnivLE.{wI, u}]
    (p : 𝒳 ⟶ 𝒴) (hp : IsRepresentableByAlgebraicSpaces B S hS p.hom)
    (hopen : IsOpenImmersion B S hS p) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, vI, wI} B S hS 𝒳 𝒴 p
```

## Tag 07WH, a lemma

[Tag 07WH](https://stacks.math.columbia.edu/tag/07WH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_limitPreservingOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingOnObjectsCriteria/Representability.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingOnObjectsCriteria/Representability.lean#L572).

> **Stacks 07WH.** Let `S` be a scheme of a big fppf site, let `T` be an object of the big fppf
> site of `S` and put `κ = size T`. A 1-morphism `f : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over
> the big fppf site of `S` is representable by algebraic spaces as soon as
>
> * the structure morphism `𝒴 ⟶ (Sch/S)_{fppf}` is limit preserving on objects,
> * for every affine `V` locally of finite presentation over `S` and every point `y` of `𝒴` over
>   `V`, the 2-fibre product `(Sch/V)_{fppf} ×_{y, 𝒴} 𝒳` is representable by an algebraic space
>   carrying a surjective étale atlas by a scheme of size at most `κ`, and
> * `𝒳` and `𝒴` are stacks in groupoids for the big Zariski topology over `S`.
>
> The bound by the size of a single object of the site is the source's set-theoretic hypothesis; it
> is what makes the coproduct of the charts of an open cover again an object of the site.

```lean
public theorem isRepresentableByAlgebraicSpaces_of_limitPreservingOnObjects
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (T : AlgebraicGeometry.BigFppfOver B S hS)
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (AlgebraicGeometry.BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴)
    (hlimit : AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒴
      (AlgebraicGeometry.Stack.terminalCFG B S hS)
      (Bicategory.InducedBicategory.mkHom (AlgebraicGeometry.Stack.toTerminalCFG B S hS 𝒴)))
    (hlocal : ∀ (U : AlgebraicGeometry.BigFppfOver B S hS),
      IsAffine U.left.1 →
      LocallyOfFinitePresentation (B.inclusion.map U.hom) →
      let 𝒰 := AlgebraicGeometry.BigFppfOver B U.left.1 U.left.2
      let p𝒰 : 𝒰 ⥤ AlgebraicGeometry.BigFppfOver B S hS := Over.map U.hom
      ∀ (y : 𝒰 ⥤ 𝒴.val.obj) (_hy : y ⋙ 𝒴.val.p = p𝒰),
        ∃ F : 𝒰ᵒᵖ ⥤ Type u,
          AlgebraicGeometry.IsAlgebraicSpace B U.left.1 U.left.2 F ∧
          Nonempty (StacksRepresentableCFG.EquivalenceOver
            (TwoFibreProductOver.fst p𝒰 𝒳.val.p 𝒴.val.p y
              (CatFiberedInGroupoids.homFunctor f))
            (presheafOfCategories (F ⋙ typeToCat)).p) ∧
          ∃ (A : 𝒰) (a : yoneda.obj A ⟶ F),
            A.left.1.size ≤ T.left.1.size ∧
            (MorphismProperty.presheaf
              (MorphismProperty.inverseImage
                (@Surjective.{u} : MorphismProperty Scheme.{u})
                (AlgebraicGeometry.BigFppfOver.toScheme B U.left.1 U.left.2))) a ∧
            (MorphismProperty.presheaf
              (MorphismProperty.inverseImage
                (@Etale.{u} : MorphismProperty Scheme.{u})
                (AlgebraicGeometry.BigFppfOver.toScheme B U.left.1 U.left.2))) a)
    (h𝒳 : 𝒳.val.p.IsStackInGroupoids.{u + 1}
      ((AlgebraicGeometry.BigFppfSite.zariskiTopology B).over (B.obj hS)))
    (h𝒴 : 𝒴.val.p.IsStackInGroupoids.{u + 1}
      ((AlgebraicGeometry.BigFppfSite.zariskiTopology B).over (B.obj hS))) :
    AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom
```

## Tag 07WI, a lemma

[Tag 07WI](https://stacks.math.columbia.edu/tag/07WI) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_of_affine_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentable.lean, line 2180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentable.lean#L2180).

> A base-change-stable, fppf-local property of a representable morphism can
> be checked on affine bases locally of finite presentation when the target is
> limit preserving on objects.

```lean
public theorem hasRelativeProperty_of_affine_locallyOfFinitePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hlimit : BigFppfOver.IsLimitPreservingOnObjects.{u, max u vI, max u wI, u, u + 1}
      B S hS 𝒴 (terminalCFG B S hS)
      (Bicategory.InducedBicategory.mkHom
        (toTerminalCFG B S hS 𝒴)))
    (hlocal : ∀ (U : BigFppfOver B S hS),
      IsAffine U.left.1 →
      LocallyOfFinitePresentation (B.inclusion.map U.hom) →
      ∀ (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
        (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        P (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor
            B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩))) :
    HasRelativeProperty B S hS P f hf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.5, Tag 06CT](https://stacks.math.columbia.edu/tag/06CT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
