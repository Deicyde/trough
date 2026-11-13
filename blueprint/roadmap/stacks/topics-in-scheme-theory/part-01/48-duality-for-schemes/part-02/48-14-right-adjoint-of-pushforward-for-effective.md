---
declaration: section
origin: cited
lean: Stacks.Divisors.normalSheafShiftIsoDerivedSheafHomExactSupport, Stacks.Divisors.isIso_normalSheafShiftToDerivedSheafHomExactSupport, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap_mate, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap_unique, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomNatTrans, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.commShift_derivedPullbackTensorSheafHomNatTrans, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomTriangleHom
statement: formalized
proof: formalized
---

# 48.14 Right adjoint of pushforward for effective Cartier divisors

Section 48.14 of the Stacks Project, [Tag 0B4A](https://stacks.math.columbia.edu/tag/0B4A). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B4B, a lemma

[Tag 0B4B](https://stacks.math.columbia.edu/tag/0B4B) in the Stacks Project.

**`Stacks.Divisors.normalSheafShiftIsoDerivedSheafHomExactSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDerivedSheafHomIso.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDerivedSheafHomIso.lean#L527). The attribute's comment: “the isomorphism 𝒩[-1] ≅ R ℰom(𝒪\_D, 𝒪\_X), which is what the tag asserts; it is not identified with the canonical comparison morphism Stacks.Divisors.normalSheafShiftToDerivedSheafHomExactSupport”.

> **[Stacks, Tag 0B4B].** For `X` a scheme and `D ⊆ X` an effective Cartier divisor with
> closed immersion `i : D ⟶ X` and normal sheaf `𝒩 = 𝒩_{D/X}`, there is an isomorphism
>
> `𝒩[-1] ≅ R ℰom(𝒪_D, 𝒪_X)` in `D(𝒪_D)`,
>
> where `R ℰom(𝒪_D, -)` is the right adjoint of derived pushforward of [Stacks, Tag 0A76].
>
> This is `Stacks.Divisors.derivedSheafHomExactSupportIsoNormalShift` precomposed with the
> normal-sheaf clause of [Stacks, Tag 0B3P] (`Stacks.Divisors.normalSheafIsoInvertibleSheaf`),
> which identifies `𝒩_{D/X}` with `i^* 𝒪_X(D)` — the description of `𝒩` the source fixes before
> stating the lemma. See the module documentation for the proof.
>
> This isomorphism is constructed independently of the canonical comparison morphism
> `Stacks.Divisors.normalSheafShiftToDerivedSheafHomExactSupport`; that the comparison morphism is
> itself invertible is `Stacks.Divisors.isIso_normalSheafShiftToDerivedSheafHomExactSupport`.

```lean
def normalSheafShiftIsoDerivedSheafHomExactSupport :
    (DerivedCategory.singleFunctor D.subscheme.Modules 1).obj (normalSheaf D.subschemeι) ≅
      (closedQuotient D).derivedSheafHomExactSupport.obj
        ((DerivedCategory.singleFunctor X.Modules 0).obj (structureModule X))
```

**`Stacks.Divisors.isIso_normalSheafShiftToDerivedSheafHomExactSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualTriangleFirstMapSectionsCore.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualTriangleFirstMapSectionsCore.lean#L186).

> **[Stacks, Tag 0B4B].** For an effective Cartier divisor `D ⊆ X` the canonical comparison
> morphism
>
> `𝒩_{D/X}[-1] ⟶ R ℰom_{𝒪_X}(𝒪_D, 𝒪_X)`
>
> in `D(𝒪_D)` is an isomorphism.
>
> This is `Stacks.Divisors.isIso_normalSheafShiftToDerivedSheafHomExactSupport_of_sectionsCore`
> with its hypothesis supplied by
> `…ClosedQuotientMorphismOfRingedSpaces.sheafHomPushforwardSectionsCore`.

```lean
theorem isIso_normalSheafShiftToDerivedSheafHomExactSupport :
    IsIso (normalSheafShiftToDerivedSheafHomExactSupport D)
```

## Tag 0B4C, an equation

[Tag 0B4C](https://stacks.math.columbia.edu/tag/0B4C) in the Stacks Project.

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean#L205). The attribute's comment: “the canonical map, defined for every complex”.

> **Stacks Project, Tag 0B4C.** The canonical map
>
> `Li^*K ⊗^L_{𝒪_Z} R ℰom(𝒪_Z, 𝒪_X) ⟶ R ℰom(𝒪_Z, K)`
>
> in `D(𝒪_Z)`: the map corresponding to `derivedPullbackTensorSheafHomMateMap` under the
> adjunction `i_* ⊣ R ℰom(𝒪_Z, -)` of [Stacks, Tag 0A76].

```lean
def derivedPullbackTensorSheafHomMap
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X))) :
    S.derivedPullbackTensorSheafHom.obj K ⟶ S.derivedSheafHomExactSupport.obj K
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean#L214). The attribute's comment: “the adjunction equation characterizing the canonical map”.

> **Stacks Project, Tag 0B4C.** The adjunction equation characterizing the canonical map:
> pushing it forward and composing with the counit of [Stacks, Tag 0A76] gives the displayed
> composite. This is what "adjoint to" means in the source.

```lean
theorem derivedPullbackTensorSheafHomMap_mate
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X))) :
    (modulePushforward S.i).mapDerivedCategory.map
          (S.derivedPullbackTensorSheafHomMap K) ≫
        S.derivedSheafHomAdjunction.counit.app K =
      S.derivedPullbackTensorSheafHomMateMap K
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMap.lean#L229). The attribute's comment: “uniqueness of the canonical map subject to the adjunction equation”.

> **Stacks Project, Tag 0B4C.** The adjunction equation determines the canonical map: no
> other morphism of that type satisfies it. Together with
> `derivedPullbackTensorSheafHomMap_mate` this is the canonicality the source asserts.

```lean
theorem derivedPullbackTensorSheafHomMap_unique
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X)))
    (τ : S.derivedPullbackTensorSheafHom.obj K ⟶ S.derivedSheafHomExactSupport.obj K)
    (hτ : (modulePushforward S.i).mapDerivedCategory.map τ ≫
        S.derivedSheafHomAdjunction.counit.app K =
      S.derivedPullbackTensorSheafHomMateMap K) :
    τ = S.derivedPullbackTensorSheafHomMap K
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean#L263). The attribute's comment: “the canonical map, functorial in the complex, as a morphism of functors”.

> **[Stacks, Tag 0B4C], the canonical map as a morphism of functors**
> `Li^*(-) ⊗^L R ℰom(𝒪_Z, 𝒪_X) ⟶ R ℰom(𝒪_Z, -)` of `D(𝒪_X) ⥤ D(𝒪_Z)`. Its component at `K` is
> `derivedPullbackTensorSheafHomMap K` and its naturality is
> `derivedPullbackTensorSheafHomMap_natural`.

```lean
def derivedPullbackTensorSheafHomNatTrans :
    S.derivedPullbackTensorSheafHom ⟶ S.derivedSheafHomExactSupport
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.commShift_derivedPullbackTensorSheafHomNatTrans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean, line 591](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean#L591). The attribute's comment: “compatible with distinguished triangles: the canonical map, functorial in the complex, commutes with the shift”.

> **[Stacks, Tag 0B4C], compatibility with distinguished triangles.** The canonical map
> `Li^*K ⊗^L R ℰom(𝒪_Z, 𝒪_X) ⟶ R ℰom(𝒪_Z, K)`, as a morphism of functors of `K`, commutes with the
> shift: `Li^*` carries its commutation as a total left derived functor
> (`Stacks.Cohomology.KFlatDerivedPullback.derivedPullback_commShift`) and the derived tensor
> product the one of its structure (`tensorRightFunctorCommShift`), so that the source carries
> `derivedPullbackTensorSheafHomCommShift`, and `R ℰom(𝒪_Z, -)` carries the commutation
> `derivedSheafHomExactSupportCommShift` it has as the right adjoint of the exact functor `i_*`.
> Both functors are exact for these commutations (`isTriangulated_derivedPullbackTensorSheafHom`,
> `isTriangulated_derivedSheafHomExactSupport`), and the map carries every triangle to a morphism of
> the image triangles (`derivedPullbackTensorSheafHomTriangleHom`).

```lean
theorem commShift_derivedPullbackTensorSheafHomNatTrans :
    NatTrans.CommShift S.derivedPullbackTensorSheafHomNatTrans ℤ
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedPullbackTensorSheafHomTriangleHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedTensorHomMapTriangles.lean#L620). The attribute's comment: “compatible with distinguished triangles: the canonical map is a morphism of the image triangles”.

> **[Stacks, Tag 0B4C], the map of triangles.** For every triangle `T` of `D(𝒪_X)`, the
> components of the canonical map at its three vertices form a morphism from the image of `T`
> under `K ↦ Li^*K ⊗^L R ℰom(𝒪_Z, 𝒪_X)` to its image under `R ℰom(𝒪_Z, -)`; for a distinguished
> `T` both images are distinguished (`isTriangulated_derivedPullbackTensorSheafHom`,
> `isTriangulated_derivedSheafHomExactSupport`).

```lean
def derivedPullbackTensorSheafHomTriangleHom
    (T : Pretriangulated.Triangle
      (DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X)))) :
    S.derivedPullbackTensorSheafHom.mapTriangle.obj T ⟶
      S.derivedSheafHomExactSupport.mapTriangle.obj T
```

## Tag 0AA4, a lemma

[Tag 0AA4](https://stacks.math.columbia.edu/tag/0AA4) in the Stacks Project.

**`Stacks.Divisors.normalTensorDerivedSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDerivedSheafHom.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDerivedSheafHom.lean#L270). The attribute's comment: “the canonical map Li^*K ⊗ᴸ 𝒩[-1] ⟶ R ℰom(𝒪\_D, K) only, unconditionally; that the map is an isomorphism is not proved, since that needs the isomorphism assertion of Tag 0B4B, which this file states only as a map, and functoriality in K is not proved either”.

> **[Stacks, Tag 0AA4], the canonical map**
>
> `Li^*K ⊗^L_{𝒪_D} 𝒩[-1] ⟶ R ℰom(𝒪_D, K)` in `D(𝒪_D)`,
>
> for `K` in `D(𝒪_X)`: the canonical map (48.14.1.1) of [Stacks, Tag 0B4C] precomposed with the
> comparison morphism `𝒩[-1] ⟶ R ℰom(𝒪_D, 𝒪_X)` of [Stacks, Tag 0B4B] tensored with `Li^*K`.
> This is the composite the source forms; that it is an isomorphism is
> `Stacks.Divisors.isIso_normalTensorDerivedSheafHomMap`, and that it is natural in `K` is
> `Stacks.Divisors.normalTensorDerivedSheafHomMap_natural`.

```lean
def normalTensorDerivedSheafHomMap
    (K : DerivedCategory X.Modules) :
    (normalTensorDerivedPullback D).obj K ⟶
      (closedQuotient D).derivedSheafHomExactSupport.obj K
```

**`Stacks.Divisors.normalTensorDerivedSheafHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierNormalTensorIso.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierNormalTensorIso.lean#L155).

> **[Stacks, Tag 0AA4].** Let `X` be a scheme and `D ⊆ X` an effective Cartier divisor, with
> closed immersion `i : D ⟶ X` and normal sheaf `𝒩`. Then the map (48.14.1.1) of
> [Stacks, Tag 0B4C] combined with the isomorphism `R ℰom(𝒪_D, 𝒪_X) ≅ 𝒩[-1]` of
> [Stacks, Tag 0B4B] defines an isomorphism
>
> `Li^*K ⊗^L_{𝒪_D} 𝒩[-1] ⟶ R ℰom(𝒪_D, K)`
>
> functorial in `K` in `D(𝒪_X)`.
>
> The isomorphism of functors `D(𝒪_X) ⥤ D(𝒪_D)` below has as component at `K` exactly the
> composite `Stacks.Divisors.normalTensorDerivedSheafHomMap` the source forms
> (`Stacks.Divisors.normalTensorDerivedSheafHomIso_hom_app`): the comparison morphism
> `𝒩[-1] ⟶ R ℰom(𝒪_D, 𝒪_X)` of [Stacks, Tag 0B4B] tensored with `Li^*K`, followed by the map of
> [Stacks, Tag 0B4C]. Here `𝒩` is the normal sheaf `Stacks.Divisors.normalSheaf` of the closed
> immersion, `R ℰom(𝒪_D, -)` is the right adjoint of derived pushforward of [Stacks, Tag 0A76],
> and `Li^*` and `⊗^L` are the derived pullback and derived tensor product of the library.

```lean
def normalTensorDerivedSheafHomIso :
    normalTensorDerivedPullback D ≅ (closedQuotient D).derivedSheafHomExactSupport
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.14, Tag 0B4A](https://stacks.math.columbia.edu/tag/0B4A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
