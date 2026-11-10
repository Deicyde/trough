---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.mapLift_isPrincipalHomogeneous, AlgebraicGeometry.RingedSpaceThickening.exists_addTorsor_mapLift, AlgebraicGeometry.RingedSpaceThickening.isFlatOver_iff_baseToInfinitesimal_isIso, AlgebraicGeometry.RingedSpaceThickening.baseToSourceIdealTensor_isIso, AlgebraicGeometry.RingedSpaceThickening.sourceIdealActionImage_isIso, AlgebraicGeometry.RingedSpaceThickening.mapLift_isTorsor_tensor, AlgebraicGeometry.RingedSpaceThickening.exists_derivedMapLiftingObstruction, AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction
statement: formalized
proof: formalized
---

# 91.5 Infinitesimal deformations of modules on ringed spaces

Section 91.5 of the Stacks Project, [Tag 08LG](https://stacks.math.columbia.edu/tag/08LG). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08LH, a lemma

[Tag 08LH](https://stacks.math.columbia.edu/tag/08LH) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.mapLift_isPrincipalHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/MapLift.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/MapLift.lean#L360).

> **Stacks Project, Tag 08LH.** Let `i : X ⟶ X'` be a first-order thickening of ringed spaces
> with ideal `ℐ`, let `ℱ'` and `𝒢'` be `𝒪_{X'}`-modules and let `φ : i^* ℱ' ⟶ i^* 𝒢'`. If `φ`
> lifts to `X'`, its lifts form a principal homogeneous space under `Hom_{𝒪_X}(i^* ℱ', ℐ𝒢')`:
> any two lifts differ by exactly one element of that group.
>
> The difference of two lifts is killed by `𝒢' ⟶ i_* i^* 𝒢'`, so it factors uniquely through
> `ℐ𝒢'`, and `infinitesimalHomEquiv` turns that factorization into the translating element.

```lean
theorem mapLift_isPrincipalHomogeneous (hi : IsFirstOrderThickening i)
    (F' G' : SheafOfModules.{u} (structureSheafRing X'))
    (φ : (modulePullback i).obj F' ⟶ (modulePullback i).obj G')
    (_hne : Nonempty (MapLift i F' G' φ)) :
    ∀ φ₁ φ₂ : MapLift i F' G' φ,
      ∃! δ : InfinitesimalHom i F' G',
        infinitesimalHomEquiv i hi F' G' δ ≫ infinitesimalι i G' + φ₁.1 = φ₂.1
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_addTorsor_mapLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/MapLiftTorsor.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/MapLiftTorsor.lean#L168).

> **Stacks Project, Tag 08LH.** Let `i : X ⟶ X'` be a first-order thickening of ringed spaces
> with ideal `ℐ`, let `ℱ'` and `𝒢'` be `𝒪_{X'}`-modules, `ℱ = i^* ℱ'`, `𝒢 = i^* 𝒢'`, and let
> `φ : ℱ ⟶ 𝒢` be `𝒪_X`-linear. If the set of lifts of `φ` to an `𝒪_{X'}`-linear map
> `φ' : ℱ' ⟶ 𝒢'` (those with `i^* φ' = φ`) is nonempty, it is a principal homogeneous space under
> `Hom_{𝒪_X}(ℱ, ℐ𝒢')`, where `ℐ𝒢'` is the image of the ideal action `ℐ ⊗ 𝒢' ⟶ 𝒢'` read as an
> `𝒪_X`-module: there is a torsor structure in which `δ` acts on a lift `φ'` by adding the
> `𝒪_{X'}`-linear map `ℱ' ⟶ ℐ𝒢' ⟶ 𝒢'` corresponding to `δ`.

```lean
theorem exists_addTorsor_mapLift (hi : IsFirstOrderThickening i)
    (F' G' : SheafOfModules.{u} (structureSheafRing X'))
    (φ : (modulePullback i).obj F' ⟶ (modulePullback i).obj G')
    (hne : Nonempty (MapLift i F' G' φ)) :
    ∃ t : AddTorsor
        ((modulePullback i).obj F' ⟶ (modulePullback i).obj (Abelian.image (idealAction i G')))
        (MapLift i F' G' φ),
      ∀ (δ : (modulePullback i).obj F' ⟶
          (modulePullback i).obj (Abelian.image (idealAction i G')))
        (φ' : MapLift i F' G' φ),
        (t.vadd δ φ').1 =
          φ'.1 + idealMultipleHomEquiv i hi F' G' δ ≫ Abelian.image.ι (idealAction i G')
```

## Tag 08LI, a lemma

[Tag 08LI](https://stacks.math.columbia.edu/tag/08LI) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.isFlatOver_iff_baseToInfinitesimal_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean, line 1799](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean#L1799). The attribute's comment: “flatness criterion”. References: SGA 3 XV (2.7), “more general”.

> **Stacks Project, Tag 08LI.** For a strict morphism of first-order thickenings of ringed
> spaces and an `𝒪_{X'}`-module `ℱ'` whose restriction `ℱ = i^* ℱ'` is flat over `S`, the module
> `ℱ'` is flat over `S'` if and only if the canonical map `f^* 𝒥 ⊗_{𝒪_X} ℱ ⟶ ℐℱ'` is an
> isomorphism.
>
> One direction is `baseToInfinitesimal_isIso_of_isFlatOver`: flatness makes the ideal action
> injective, and the map in question is `i^*` of an epimorphism which that injectivity turns into
> an isomorphism. For the other, invertibility makes the action of `(f')^* 𝒥` on `ℱ'` a
> monomorphism, hence injective on every stalk after base change; the flatness of `ℱ` over `S`
> supplies the quotient hypothesis of the square-zero local criterion, and strictness is what
> identifies the relevant quotient of `𝒪_{X',x}` with `𝒪_{X,x}`.

```lean
theorem isFlatOver_iff_baseToInfinitesimal_isIso (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    (F' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF : AlgebraicGeometry.IsFlatOver D.f ((modulePullback D.i).obj F')) :
    AlgebraicGeometry.IsFlatOver D.f' F' ↔ IsIso (baseToInfinitesimal D F')
```

**`AlgebraicGeometry.RingedSpaceThickening.baseToSourceIdealTensor_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean, line 1886](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean#L1886). The attribute's comment: “first isomorphism in the final assertion”.

> **Stacks Project, Tag 08LI.** Under the hypotheses of the criterion and flatness of `ℱ'`
> over `S'`, the reduced canonical ideal map tensored with `ℱ` is an isomorphism: it is an
> epimorphism by strictness, and a monomorphism because the composite with the ideal action is
> one.

```lean
theorem baseToSourceIdealTensor_isIso (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    (F' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF : AlgebraicGeometry.IsFlatOver D.f ((modulePullback D.i).obj F'))
    (hF' : AlgebraicGeometry.IsFlatOver D.f' F') :
    IsIso (baseToSourceIdealTensor D F')
```

**`AlgebraicGeometry.RingedSpaceThickening.sourceIdealActionImage_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean, line 1906](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean#L1906). The attribute's comment: “second isomorphism in the final assertion”.

> **Stacks Project, Tag 08LI.** Under the hypotheses of the criterion and flatness of `ℱ'`
> over `S'`, the ideal action on the reduced source identifies `i^* ℐ ⊗_{𝒪_X} ℱ` with the ideal
> multiple `ℐℱ'`.

```lean
theorem sourceIdealActionImage_isIso (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    (F' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF : AlgebraicGeometry.IsFlatOver D.f ((modulePullback D.i).obj F'))
    (hF' : AlgebraicGeometry.IsFlatOver D.f' F') :
    IsIso (sourceIdealActionImage D F')
```

## Tag 08LJ, a lemma

[Tag 08LJ](https://stacks.math.columbia.edu/tag/08LJ) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.mapLift_isTorsor_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean, line 2039](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatCriterion.lean#L2039).

> **Stacks Project, Tag 08LJ.** Let `(f, f')` be a morphism of thickenings with `i` a first
> order thickening, let `ℱ'` and `𝒢'` be `𝒪_{X'}`-modules, set `ℱ = i^* ℱ'` and `𝒢 = i^* 𝒢'`,
> and let `φ : ℱ ⟶ 𝒢` be `𝒪_X`-linear. If `𝒢'` is flat over `S'` and `(f, f')` is strict, the
> lifts of `φ` to an `𝒪_{X'}`-linear `φ' : ℱ' ⟶ 𝒢'` form, when nonempty, a principal homogeneous
> space under `Hom_{𝒪_X}(ℱ, 𝒢 ⊗_{𝒪_X} f^* 𝒥)`, which acts through `infinitesimalTensorIso`: each
> `δ` translates a lift to a lift, and any two lifts are translated to one another by exactly one
> `δ`.
>
> The group acts because `i^*` is additive and kills a map through `ℐ𝒢'`, which is
> `modulePullback_map_add_comp_infinitesimalι`. That the action is simply transitive is **Stacks
> 08LH**, which gives the same conclusion for `Hom_{𝒪_X}(ℱ, ℐ𝒢')`, transported along **Stacks
> 08LI**, which identifies `ℐ𝒢'` with `𝒢 ⊗_{𝒪_X} f^* 𝒥`.

```lean
theorem mapLift_isTorsor_tensor (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (hs : D.IsStrict)
    (F' G' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hG' : AlgebraicGeometry.IsFlatOver D.f' G')
    (φ : (modulePullback D.i).obj F' ⟶ (modulePullback D.i).obj G')
    (hne : Nonempty (MapLift D.i F' G' φ)) :
    (∀ (δ : (modulePullback D.i).obj F' ⟶ restrictionTensorBaseIdeal D G')
        (φ₁ : MapLift D.i F' G' φ),
        (modulePullback D.i).map
            (infinitesimalHomEquiv D.i hi F' G'
                  (δ ≫ (infinitesimalTensorIso D hs G' hG').hom) ≫ infinitesimalι D.i G' +
                φ₁.1) =
          φ) ∧
      ∀ φ₁ φ₂ : MapLift D.i F' G' φ,
        ∃! δ : (modulePullback D.i).obj F' ⟶ restrictionTensorBaseIdeal D G',
          infinitesimalHomEquiv D.i hi F' G'
                (δ ≫ (infinitesimalTensorIso D hs G' hG').hom) ≫ infinitesimalι D.i G' + φ₁.1 =
              φ₂.1
```

## Tag 08LK, a lemma

[Tag 08LK](https://stacks.math.columbia.edu/tag/08LK) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.exists_derivedMapLiftingObstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DerivedLiftingObstruction.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DerivedLiftingObstruction.lean#L149).

> **Stacks Project, Tag 08LK.** Let `i : (X, 𝒪_X) ⟶ (X', 𝒪_{X'})` be a first order thickening
> of ringed spaces with ideal `ℐ`, let `ℱ'` and `𝒢'` be `𝒪_{X'}`-modules and let
> `φ : i^* ℱ' ⟶ i^* 𝒢'` be `𝒪_X`-linear. There is a class `o(φ) ∈ Ext¹_{𝒪_X}(Li^* ℱ', ℐ𝒢')`
> whose vanishing is necessary and sufficient for `φ` to lift to an `𝒪_{X'}`-linear map
> `ℱ' ⟶ 𝒢'`.

```lean
theorem exists_derivedMapLiftingObstruction (hi : IsFirstOrderThickening i)
    (F' G' : SheafOfModules.{u} (structureSheafRing X'))
    (φ : (modulePullback i).obj F' ⟶ (modulePullback i).obj G') :
    ∃ o : DerivedCategory.Ext
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback i).obj
          ((DerivedCategory.singleFunctor _ 0).obj F'))
        ((DerivedCategory.singleFunctor _ 0).obj (infinitesimalPartOnSource i G')) 1,
      (o = 0 ↔ Nonempty (MapLift i F' G' φ))
```

## Tag 08LL, a lemma

[Tag 08LL](https://stacks.math.columbia.edu/tag/08LL) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean#L405). The attribute's comment: “the obstruction class”.

> **Stacks Project, Tag 08LL.** The obstruction class
> `o(φ) ∈ Ext¹_{𝒪_X}(ℱ, 𝒢 ⊗_{𝒪_X} f^* 𝒥)` to lifting an `𝒪_X`-linear `φ : ℱ ⟶ 𝒢` between the
> restrictions of two `𝒪_{X'}`-modules flat over `S'`, across a strict morphism of thickenings
> whose upper arrow is a first order thickening.
>
> It is the class of **Stacks 08L6** for the two kernel extensions of **Stacks 08LM** and the
> pair `(φ, 1 ⊗ φ)`, carried into the source's group along the identification
> `idealTensorIsoRestrictionTensorBaseIdeal` of **Stacks 08LI**. Its vanishing criterion is
> `AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction_eq_zero_iff`.

```lean
noncomputable def mapLiftObstruction (hi : IsFirstOrderThickening D.i) (hs : D.IsStrict)
    (F' G' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF' : AlgebraicGeometry.IsFlatOver D.f' F')
    (hG' : AlgebraicGeometry.IsFlatOver D.f' G')
    (φ : (modulePullback D.i).obj F' ⟶ (modulePullback D.i).obj G') :
    CategoryTheory.Abelian.zExt ((modulePullback D.i).obj F')
      (restrictionTensorBaseIdeal D G') 1
```

**`AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean#L419). The attribute's comment: “the vanishing criterion”.

> **Stacks Project, Tag 08LL.** The vanishing of the obstruction class `o(φ)` is necessary and
> sufficient for `φ` to lift to an `𝒪_{X'}`-linear map `φ' : ℱ' ⟶ 𝒢'`, that is one with
> `i^* φ' = φ`.

```lean
theorem mapLiftObstruction_eq_zero_iff (hi : IsFirstOrderThickening D.i) (hs : D.IsStrict)
    (F' G' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF' : AlgebraicGeometry.IsFlatOver D.f' F')
    (hG' : AlgebraicGeometry.IsFlatOver D.f' G')
    (φ : (modulePullback D.i).obj F' ⟶ (modulePullback D.i).obj G') :
    mapLiftObstruction hi hs F' G' hF' hG' φ = 0 ↔ Nonempty (MapLift D.i F' G' φ)
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_mapLiftObstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/MapLiftObstruction.lean#L451).

> **Stacks Project, Tag 08LL.** Let `(f, f')` be a morphism of thickenings of ringed spaces
> whose upper arrow `i : X ⟶ X'` is a first order thickening, let `ℱ'` and `𝒢'` be
> `𝒪_{X'}`-modules, put `ℱ = i^* ℱ'` and `𝒢 = i^* 𝒢'`, and let `φ : ℱ ⟶ 𝒢` be `𝒪_X`-linear.
> Assume `ℱ'` and `𝒢'` are flat over `S'` and that `(f, f')` is strict. Then there exists
>
>     o(φ) ∈ Ext¹_{𝒪_X}(ℱ, 𝒢 ⊗_{𝒪_X} f^* 𝒥)
>
> whose vanishing is a necessary and sufficient condition for the existence of an `𝒪_{X'}`-linear
> map `φ' : ℱ' ⟶ 𝒢'` with `i^* φ' = φ`.
>
> The source asserts existence of the class, not uniqueness, and that is what is stated here; the
> class itself is `AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction` and its criterion
> `AlgebraicGeometry.RingedSpaceThickening.mapLiftObstruction_eq_zero_iff`.

```lean
theorem exists_mapLiftObstruction (hi : IsFirstOrderThickening D.i) (hs : D.IsStrict)
    (F' G' : SheafOfModules.{u} (structureSheafRing D.X'))
    (hF' : AlgebraicGeometry.IsFlatOver D.f' F')
    (hG' : AlgebraicGeometry.IsFlatOver D.f' G')
    (φ : (modulePullback D.i).obj F' ⟶ (modulePullback D.i).obj G') :
    ∃ o : CategoryTheory.Abelian.zExt ((modulePullback D.i).obj F')
        (restrictionTensorBaseIdeal D G') 1,
      (o = 0 ↔ Nonempty (MapLift D.i F' G' φ))
```

## Tag 08LM, a lemma

[Tag 08LM](https://stacks.math.columbia.edu/tag/08LM) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.flatLiftClassDifference_isPrincipalHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatLiftTorsor.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatLiftTorsor.lean#L148).

> Let `(f, f')` be a strict morphism of first order thickenings of ringed spaces and let `ℱ` be
> an `𝒪_X`-module flat over `S`. The isomorphism classes of pairs `(ℱ', α)` of an `𝒪_{X'}`-module
> `ℱ'` flat over `S'` and an isomorphism `α : i^* ℱ' ≅ ℱ` form a principal homogeneous space under
> `Ext¹_{𝒪_X}(ℱ, ℐ ⊗_{𝒪_X} ℱ)`: the difference
> `AlgebraicGeometry.RingedSpaceThickening.flatLiftClassDifference` is additive, and for every class
> `b` the map `a ↦ d(a, b)` is a bijection onto `Ext¹_{𝒪_X}(ℱ, ℐ ⊗_{𝒪_X} ℱ)`. When there is no flat
> lift both conditions hold vacuously.

```lean
theorem flatLiftClassDifference_isPrincipalHomogeneous (hi : IsFirstOrderThickening D.i)
    (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    {F : SheafOfModules.{u} (structureSheafRing D.X)} (hF : AlgebraicGeometry.IsFlatOver D.f F) :
    (∀ a b c : FlatLiftClass D F,
      flatLiftClassDifference hi hs F a b + flatLiftClassDifference hi hs F b c =
        flatLiftClassDifference hi hs F a c) ∧
      ∀ b : FlatLiftClass D F,
        Function.Bijective fun a : FlatLiftClass D F => flatLiftClassDifference hi hs F a b
```

## Tag 08LN, a lemma

[Tag 08LN](https://stacks.math.columbia.edu/tag/08LN) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_flatLift_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatLiftExistence.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatLiftExistence.lean#L516).

> **Stacks Project, Tag 08LN.** Let `(f, f')` be a strict morphism of first order thickenings
> of ringed spaces and let `ℱ` be an `𝒪_X`-module flat over `S`. There is an `𝒪_{X'}`-module `ℱ'`
> flat over `S'` with `i^* ℱ' ≅ ℱ` if and only if the canonical map
> `f^* 𝒥 ⊗_{𝒪_X} ℱ ⟶ ℐ ⊗_{𝒪_X} ℱ` is an isomorphism and the class
> `o(ℱ, ℐ ⊗_{𝒪_X} ℱ, 1) ∈ Ext²_{𝒪_X}(ℱ, ℐ ⊗_{𝒪_X} ℱ)` of **Stacks 08L8** is zero.
>
> The pair `(ℱ', α)` of the source is
> `AlgebraicGeometry.RingedSpaceThickening.FlatLift`, and the obstruction class is
> `AlgebraicGeometry.RingedSpaceThickening.obstructionClass` for the coefficient module
> `ℐ ⊗_{𝒪_X} ℱ` and the normalization `c = 1`.

```lean
theorem nonempty_flatLift_iff (D : MorphismOfThickenings.{u})
    [HasExt (SheafOfModules.{u} (structureSheafRing D.X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing D.X))]
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    (F : SheafOfModules.{u} (structureSheafRing D.X))
    (hF : AlgebraicGeometry.IsFlatOver D.f F) :
    Nonempty (FlatLift D F) ↔
      IsIso (baseIdealTensorComparison D F) ∧
        obstructionClass D.i hi F (idealTensor D F) (𝟙 (idealTensor D F)) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.5, Tag 08LG](https://stacks.math.columbia.edu/tag/08LG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
