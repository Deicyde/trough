---
declaration: section
origin: cited
lean: AlgebraicGeometry.ExtendingFunctors.extension_hom_unique, AlgebraicGeometry.ExtendingFunctors.extension_iso_unique, AlgebraicGeometry.ExtendingFunctors.exists_unique_extension, AlgebraicGeometry.ExtendingFunctors.isZariskiSheaf_extension, AlgebraicGeometry.exists_isStandardCovering_of_isLimit, AlgebraicGeometry.exists_standardZariskiCovering_of_isLimit, AlgebraicGeometry.exists_standardEtaleCovering_of_isLimit, AlgebraicGeometry.exists_standardSmoothCovering_of_isLimit
statement: formalized
proof: formalized
---

# 34.13 Extending functors

Section 34.13 of the Stacks Project, [Tag 0EUV](https://stacks.math.columbia.edu/tag/0EUV). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EUW, a lemma

[Tag 0EUW](https://stacks.math.columbia.edu/tag/0EUW) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.extension_hom_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctors.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctors.lean#L304). The attribute's comment: “uniqueness: a morphism between two extensions satisfying the analogues of (a) and (b) is determined by the identifications of their restrictions with the original functor”.

> **Stacks 0EUW.** The extension of `F` to `Sch/S` is unique: a morphism between two extensions
> of `F` which both satisfy the analogues of (a) and (b) is determined by its restriction to the
> full subcategory.

```lean
theorem extension_hom_unique {P : ObjectProperty (Over S)}
    (_hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    {F : P.FullSubcategoryᵒᵖ ⥤ Type w}
    (_haF : IsZariskiSheafOnSubcategory P F)
    (_hbF : PreservesAffineLimitsOnSubcategory P F)
    {F₁ F₂ : (Over S)ᵒᵖ ⥤ Type w}
    (_ha₁ : IsZariskiSheaf F₁) (hb₁ : PreservesAffineLimits F₁)
    (ha₂ : IsZariskiSheaf F₂) (_hb₂ : PreservesAffineLimits F₂)
    {α : P.ι.op ⋙ F₁ ≅ F} {β : P.ι.op ⋙ F₂ ≅ F} (θ θ' : F₁ ⟶ F₂)
    (hθ : Functor.whiskerLeft P.ι.op θ ≫ β.hom = α.hom)
    (hθ' : Functor.whiskerLeft P.ι.op θ' ≫ β.hom = α.hom) :
    θ = θ'
```

**`AlgebraicGeometry.ExtendingFunctors.extension_iso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctors.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctors.lean#L327). The attribute's comment: “uniqueness: two extensions satisfying the analogues of (a) and (b) admit at most one isomorphism compatible with the identifications of their restrictions with the original functor”.

> **Stacks 0EUW.** The extension of `F` to `Sch/S` is unique: two extensions of `F` which both
> satisfy the analogues of (a) and (b) admit at most one isomorphism compatible with the
> identifications of their restrictions with `F`.

```lean
theorem extension_iso_unique {P : ObjectProperty (Over S)}
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    {F : P.FullSubcategoryᵒᵖ ⥤ Type w}
    (haF : IsZariskiSheafOnSubcategory P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F)
    {F₁ F₂ : (Over S)ᵒᵖ ⥤ Type w}
    (ha₁ : IsZariskiSheaf F₁) (hb₁ : PreservesAffineLimits F₁)
    (ha₂ : IsZariskiSheaf F₂) (hb₂ : PreservesAffineLimits F₂)
    {α : P.ι.op ⋙ F₁ ≅ F} {β : P.ι.op ⋙ F₂ ≅ F} (ε ε' : F₁ ≅ F₂)
    (hε : Functor.whiskerLeft P.ι.op ε.hom ≫ β.hom = α.hom)
    (hε' : Functor.whiskerLeft P.ι.op ε'.hom ≫ β.hom = α.hom) :
    ε = ε'
```

**`AlgebraicGeometry.ExtendingFunctors.exists_unique_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsLimits/Uniqueness.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsLimits/Uniqueness.lean#L610).

> **Stacks 0EUW.** For a scheme `S` and a full subcategory `𝒞` of `Sch/S` which contains, up to
> isomorphism, the affine opens of its objects and the affine schemes of finite presentation over
> the affine opens of `S`, a functor `F : 𝒞ᵒᵖ ⥤ Set` which is a Zariski sheaf and takes directed
> inverse limits of affine objects to filtered colimits extends to `Sch/S` in a unique way: there
> is a functor `F'` on `Sch/S` which is a Zariski sheaf, takes directed inverse limits of affine
> schemes over `S` to filtered colimits, restricts to `F` on `𝒞`, and is isomorphic to any other
> functor with these three properties.

```lean
theorem exists_unique_extension (hP1 : HasAffineOpens P)
    (hP2 : HasFinitePresentationAffines P)
    {F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1))}
    (haF : IsZariskiSheafOnSubcategory P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F) :
    ∃ (F' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))) (_ : IsZariskiSheaf F')
      (_ : PreservesAffineLimits F') (_ : P.ι.op ⋙ F' ≅ F),
      ∀ (F'' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))), IsZariskiSheaf F'' →
        PreservesAffineLimits F'' → (P.ι.op ⋙ F'' ≅ F) → Nonempty (F' ≅ F'')
```

**`AlgebraicGeometry.ExtendingFunctors.isZariskiSheaf_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsSheaf/ZariskiSheaf.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsSheaf/ZariskiSheaf.lean#L156). The attribute's comment: “the analogue of condition (a) for the extension `AlgebraicGeometry.ExtendingFunctors.extension`: the extension is a Zariski sheaf on `Sch/S`”.

> **The analogue of condition (a) of Stacks 0EUW for the extension.** The extension is a
> Zariski sheaf on `Sch/S`: its value at `X` is the limit of the colimit formula over the affine
> objects over affine opens of `S` mapping to `X`, and a section is built over each such object by
> gluing, using the sheaf condition for the colimit formula on affine objects.

```lean
theorem isZariskiSheaf_extension (hP1 : HasAffineOpens P)
    (hP2 : HasFinitePresentationAffines P) (haF : IsZariskiSheafOnSubcategory P F) :
    IsZariskiSheaf (extension P F)
```

## Tag 049N, a lemma

[Tag 049N](https://stacks.math.columbia.edu/tag/049N) in the Stacks Project.

**`AlgebraicGeometry.exists_isStandardCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringLimitDescent.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/StandardCoveringLimitDescent.lean#L75). The attribute's comment: “covering\_existence, stated once for AlgebraicGeometry.IsStandardCovering rather than separately in the idiom native to each of the five topologies”.

> **Stacks 049N (1), uniformly in the topology.** Let `T = lim Tᵢ` be an affine scheme written
> as an inverse limit of a cofiltered system of affine schemes. A standard `τ`-covering of `T` is,
> member by member, the base change along `T ⟶ Tᵢ` of a standard `τ`-covering of `Tᵢ` for some
> stage `i`, for each of the five topologies.

```lean
theorem exists_isStandardCovering_of_isLimit (τ : CoveringTopology)
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [IsAffine c.pt] [∀ i, IsAffine (D.obj i)]
    {J : Type w} (U : J → Scheme.{u}) (f : ∀ j, U j ⟶ c.pt)
    (h : IsStandardCovering τ U f) :
    ∃ (i : I) (Uᵢ : J → Scheme.{u}) (fᵢ : ∀ j, Uᵢ j ⟶ D.obj i),
      IsStandardCovering τ Uᵢ fᵢ ∧
        ∀ j : J, Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (fᵢ j)) ≅
          Over.mk (f j))
```

**`AlgebraicGeometry.exists_standardZariskiCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean#L743). The attribute's comment: “covering\_existence”.

> A finite standard Zariski covering of an affine inverse limit descends to a
> standard Zariski covering at some stage.

```lean
theorem exists_standardZariskiCovering_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [IsAffine c.pt] [∀ i, IsAffine (D.obj i)]
    (𝒰 : c.pt.Cover.{w} Scheme.zariskiPrecoverage)
    (h𝒰 : AlgebraicGeometry.IsStandardZariskiCovering 𝒰) :
    ∃ (i : I) (𝒰ᵢ : (D.obj i).Cover.{w} Scheme.zariskiPrecoverage)
      (_h𝒰ᵢ : AlgebraicGeometry.IsStandardZariskiCovering 𝒰ᵢ)
      (e : 𝒰.I₀ ≃ 𝒰ᵢ.I₀),
      ∀ j : 𝒰.I₀,
        Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (𝒰ᵢ.f (e j))) ≅
          Over.mk (𝒰.f j))
```

**`AlgebraicGeometry.exists_standardEtaleCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean, line 807](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean#L807). The attribute's comment: “covering\_existence”.

> A finite standard étale covering of an affine inverse limit descends to a
> standard étale covering at some stage.

```lean
theorem exists_standardEtaleCovering_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [IsAffine c.pt] [∀ i, IsAffine (D.obj i)]
    (𝒰 : c.pt.AffineCover.{w} @Etale) [Finite 𝒰.I₀] :
    ∃ (i : I) (𝒰ᵢ : (D.obj i).AffineCover.{w} @Etale)
      (_ : Finite 𝒰ᵢ.I₀) (e : 𝒰.I₀ ≃ 𝒰ᵢ.I₀),
      ∀ j : 𝒰.I₀,
        Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (𝒰ᵢ.f (e j))) ≅
          Over.mk (𝒰.f j))
```

**`AlgebraicGeometry.exists_standardSmoothCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean, line 850](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean#L850). The attribute's comment: “covering\_existence”.

> A finite standard smooth covering of an affine inverse limit descends to a
> standard smooth covering at some stage.

```lean
theorem exists_standardSmoothCovering_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [IsAffine c.pt] [∀ i, IsAffine (D.obj i)]
    {J : Type w} [Finite J]
    (U : J → Scheme.{u}) [∀ j, IsAffine (U j)]
    (f : ∀ j, U j ⟶ c.pt)
    (hf : IsStandardSmoothCovering U f) :
    ∃ (i : I) (Uᵢ : J → Scheme.{u})
      (hUᵢ : ∀ j, IsAffine (Uᵢ j)) (fᵢ : ∀ j, Uᵢ j ⟶ D.obj i),
      (letI : ∀ j, IsAffine (Uᵢ j) := hUᵢ
       IsStandardSmoothCovering Uᵢ fᵢ) ∧
        ∀ j : J,
          Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (fᵢ j)) ≅
            Over.mk (f j))
```

**`AlgebraicGeometry.exists_standardSyntomicCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean, line 880](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean#L880). The attribute's comment: “covering\_existence”.

> A finite standard syntomic covering of an affine inverse limit descends to a
> standard syntomic covering at some stage.

```lean
theorem exists_standardSyntomicCovering_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ i, IsAffine (D.obj i)]
    {J : Type w} (U : J → Scheme.{u}) (f : ∀ j, U j ⟶ c.pt)
    (hf : IsStandardSyntomicCovering U f) :
    ∃ (i : I) (Uᵢ : J → Scheme.{u}) (fᵢ : ∀ j, Uᵢ j ⟶ D.obj i),
      IsStandardSyntomicCovering Uᵢ fᵢ ∧
        ∀ j : J,
          Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (fᵢ j)) ≅
            Over.mk (f j))
```

**`AlgebraicGeometry.exists_standardFppfCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean, line 912](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringExistence.lean#L912). The attribute's comment: “covering\_existence”.

> A finite standard fppf covering of an affine inverse limit descends to a
> standard fppf covering at some stage.

```lean
theorem exists_standardFppfCovering_of_isLimit
    {I : Type v} [Category.{v} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ i, IsAffine (D.obj i)]
    {J : Type w} (U : J → Scheme.{u}) (f : ∀ j, U j ⟶ c.pt)
    (hf : IsStandardFppfCovering U f) :
    ∃ (i : I) (Uᵢ : J → Scheme.{u}) (fᵢ : ∀ j, Uᵢ j ⟶ D.obj i),
      IsStandardFppfCovering Uᵢ fᵢ ∧
        ∀ j : J,
          Nonempty ((Over.pullback (c.π.app i)).obj (Over.mk (fᵢ j)) ≅
            Over.mk (f j))
```

**`AlgebraicGeometry.eventually_familyHom_eq_of_baseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringMorphisms.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringMorphisms.lean#L99). The attribute's comment: “covering\_morphism\_equality”. References: SGA 3 VIB (10.0), “(i)”; SGA 4 VII (5.2), “a, special case”.

> Equality of morphisms of finite families of affine, flat, finitely presented
> schemes over a limit holds already at some finite stage.

```lean
theorem eventually_familyHom_eq_of_baseChange_eq
    {I : Type v} [Category.{a} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    (hD : ∀ i, IsAffine (D.obj i)) (i : I)
    (E : PreZeroHypercover.{w} (D.obj i))
    (F : PreZeroHypercover.{w'} (D.obj i)) [Finite E.I₀]
    (hE : ∀ j, IsAffineFlatOfFinitePresentation (Over.mk (E.f j)))
    (hF : ∀ j, IsAffineFlatOfFinitePresentation (Over.mk (F.f j)))
    (f g : E.Hom F) (hfg : FamilyHom.BaseChangeEq (c.π.app i) E F f g) :
    ∃ (j : I) (e : j ⟶ i), FamilyHom.BaseChangeEq (D.map e) E F f g
```

**`AlgebraicGeometry.exists_familyHom_after_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringMorphisms.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/CoveringMorphisms.lean#L263). The attribute's comment: “covering\_morphisms”.

> A morphism of finite standard covering families of an affine inverse limit
> descends to a morphism at a finite stage, with its given index map unchanged.

```lean
theorem exists_familyHom_after_baseChange
    {I : Type v} [Category.{a} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    (hD : ∀ i, IsAffine (D.obj i)) (i : I)
    (E : PreZeroHypercover.{w} (D.obj i))
    (F : PreZeroHypercover.{w'} (D.obj i))
    [Finite E.I₀]
    (hE : ∀ k, IsAffineFlatOfFinitePresentation (Over.mk (E.f k)))
    (hF : ∀ k, IsAffineFlatOfFinitePresentation (Over.mk (F.f k)))
    (f : (E.pullback₂ (c.π.app i)).Hom (F.pullback₂ (c.π.app i))) :
    ∃ (j : I) (e : j ⟶ i)
      (g : (E.pullback₂ (D.map e)).Hom (F.pullback₂ (D.map e))),
      g.s₀ = f.s₀ ∧ ∀ k : E.I₀,
        ∃ (α : (Over.pullback (c.π.app j)).obj
            ((Over.pullback (D.map e)).obj (Over.mk (E.f k))) ≅
              (Over.pullback (c.π.app i)).obj (Over.mk (E.f k)))
          (β : (Over.pullback (c.π.app j)).obj
            ((Over.pullback (D.map e)).obj (Over.mk (F.f (g.s₀ k)))) ≅
              (Over.pullback (c.π.app i)).obj (Over.mk (F.f (g.s₀ k)))),
          (α.hom.left ≫ pullback.fst (E.f k) (c.π.app i) =
            pullback.fst ((Over.pullback (D.map e)).obj (Over.mk (E.f k))).hom
              (c.π.app j) ≫ pullback.fst (E.f k) (D.map e)) ∧
          (β.hom.left ≫ pullback.fst (F.f (g.s₀ k)) (c.π.app i) =
            pullback.fst ((Over.pullback (D.map e)).obj
              (Over.mk (F.f (g.s₀ k)))).hom (c.π.app j) ≫
                pullback.fst (F.f (g.s₀ k)) (D.map e)) ∧
          HEq (α.hom.left ≫ f.h₀ k)
            (((Over.pullback (c.π.app j)).map
              (show Over.mk ((E.pullback₂ (D.map e)).f k) ⟶
                  Over.mk ((F.pullback₂ (D.map e)).f (g.s₀ k)) from
                Over.homMk (g.h₀ k) (g.w₀ k))).left ≫ β.hom.left)
```

## Tag 0GDW, a lemma

[Tag 0GDW](https://stacks.math.columbia.edu/tag/0GDW) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_extension_of_isStandardAffineSheafOnSubcategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean, line 726](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean#L726). The attribute's comment: “for each of the five topologies Zariski, étale, smooth, syntomic and fppf: the extension F' of a functor F satisfying conditions (a), (b) and (c), from a full subcategory of Sch/S satisfying conditions (1) and (2) of Tag 0EUW, satisfies the sheaf condition for every τ-covering of Sch/S”.

> **Stacks 0GDW.** Let `S` be a scheme, let `𝒞` be a full subcategory of `Sch/S` satisfying
> conditions (1) and (2) of Stacks 0EUW and let `F : 𝒞ᵒᵖ ⥤ Set` satisfy conditions (a), (b) and
> (c). Then the extension `F' = AlgebraicGeometry.ExtendingFunctors.extension` of `F` to `Sch/S` is
> a sheaf for each of the five topologies — Zariski, étale, smooth, syntomic and fppf.
>
> The proof follows the source: the restricted sheaf condition for the extension, on the standard
> `τ`-coverings of the affine objects of `Sch/S` lying over an affine open of `S`, is deduced from
> condition (c) by `AlgebraicGeometry.ExtendingFunctors.isStandardAffineSheaf_extension` (the
> special case of the source's proof), and the general case is
> `AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_of_isStandardAffineSheaf`, applied to the
> extension, which is a Zariski sheaf by condition (a).

```lean
theorem isCoveringSheaf_extension_of_isStandardAffineSheafOnSubcategory (τ : CoveringTopology)
    (P : ObjectProperty (Over S)) (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1)))
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    (haF : IsZariskiSheafOnSubcategory P F) (hbF : PreservesAffineLimitsOnSubcategory P F)
    (hcF : IsStandardAffineSheafOnSubcategory.{max w (u + 1), u, v} τ P F) :
    IsCoveringSheaf.{max w (u + 1), u, v} τ (extension P F)
```

## Tag 0EUX, a lemma

[Tag 0EUX](https://stacks.math.columbia.edu/tag/0EUX) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_zariski_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsCoveringSheaf.lean, line 606](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsCoveringSheaf.lean#L606). The attribute's comment: “τ = Zariski”.

> **Stacks 0EUX for `τ = Zariski`.** Let `S` be a scheme, let `𝒞` be a full subcategory of
> `Sch/S` satisfying conditions (1) and (2) of Stacks 0EUW — the big Zariski site `(Sch/S)_Zar` is
> such a subcategory — and let `F : 𝒞ᵒᵖ ⥤ Set` be a Zariski sheaf on `𝒞`. Then the extension `F'`
> of `F` to all schemes over `S` satisfies the sheaf condition for all Zariski coverings.
>
> Property (b) of Stacks 0EUW, which the source assumes, is not needed for this clause: the
> extension is a Zariski sheaf whatever `F` does to directed limits of affines, and a Zariski sheaf
> is a sheaf for every Zariski covering. It is property (b) that makes
> `AlgebraicGeometry.ExtendingFunctors.extension` deserve the name `F'`, by identifying its
> restriction to `𝒞` with `F`; the conclusion below is about that same functor, assumed or not.

```lean
theorem isCoveringSheaf_zariski_extension (P : ObjectProperty (Over S))
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1)))
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    (hF : IsCoveringSheafOnSubcategory.{max w (u + 1), u, u} .zariski P F) :
    IsCoveringSheaf.{max w (u + 1), u, v} .zariski (extension P F)
```

**`AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean, line 798](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean#L798). The attribute's comment: “all five topologies: Zariski, étale, smooth, syntomic and fppf”.

> **Stacks 0EUX.** Let `τ` be one of Zariski, étale, smooth, syntomic and fppf, let `S` be a
> scheme, let `𝒞` be a full subcategory of `Sch/S` satisfying conditions (1) and (2) of Stacks
> 0EUW — the big site `(Sch/S)_τ` is such a subcategory — and let `F : 𝒞ᵒᵖ ⥤ Set` be a `τ`-sheaf
> on `𝒞` satisfying property (b) of Stacks 0EUW. Then the extension `F'` of `F` to all schemes over
> `S` satisfies the sheaf condition for all `τ`-coverings.
>
> This is the unconditional form of
> `AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory`,
> which carries the sheaf condition of the extension for the standard `τ`-coverings of the affine
> objects of `Sch/S` lying over an affine open of `S` as a hypothesis only because that condition
> is proved in this file, which sits above it in the import order. The ingredients are conditions
> (a) and (c) of Stacks 0GDW, which a `τ`-sheaf on `𝒞` satisfies by
> `AlgebraicGeometry.ExtendingFunctors.isZariskiSheafOnSubcategory_of_isCoveringSheafOnSubcategory`
> and `ExtendingFunctors.isStandardAffineSheafOnSubcategory_of_isCoveringSheafOnSubcategory`, and
> Stacks 0GDW itself,
> `ExtendingFunctors.isCoveringSheaf_extension_of_isStandardAffineSheafOnSubcategory`.
>
> Condition (a) is read on open coverings indexed by the points of a scheme, so the `τ`-sheaf
> condition is asked of `F` for index types of `Type (max u v)`, where `u` is the universe of the
> objects of `Sch/S` and `Type v` is the universe of the index types for which the conclusion is
> drawn. For `v = u` — the case of the big site `(Sch/S)_τ`, whose coverings are indexed in the
> universe of its objects, which is the situation of the source — hypothesis and conclusion are
> both read on index types of `Type u`.

```lean
theorem isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory'
    (τ : CoveringTopology) (P : ObjectProperty (Over S))
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1)))
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    (hF : IsCoveringSheafOnSubcategory.{max w (u + 1), u, max u v} τ P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F) :
    IsCoveringSheaf.{max w (u + 1), u, v} τ (extension P F)
```

**`AlgebraicGeometry.ExtendingFunctors.isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory_of_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean, line 827](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsStandardAffineInterchange.lean#L827). The attribute's comment: “all five topologies, for coverings indexed in the universe of the objects of Sch/S, which is the big site of the source”.

> **Stacks 0EUX for the big site.** Let `τ` be one of Zariski, étale, smooth, syntomic and
> fppf, let `S` be a scheme, let `𝒞` be a full subcategory of `Sch/S` satisfying conditions (1)
> and (2) of Stacks 0EUW, and let `F : 𝒞ᵒᵖ ⥤ Set` be a `τ`-sheaf on `𝒞` satisfying property (b)
> of Stacks 0EUW. Then the extension `F'` of `F` to all schemes over `S` satisfies the sheaf
> condition for all `τ`-coverings.
>
> This is
> `ExtendingFunctors.isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory'`
> read on index types of `Type u`, the universe of the objects of `Sch/S`. That is the situation
> of the source: the subcategory it takes is the big site `(Sch/S)_τ`, whose covering families are
> indexed in the universe of its own objects, so the `τ`-sheaf condition hypothesis and the sheaf
> condition concluded are read on the same index types.

```lean
theorem isCoveringSheaf_extension_of_isCoveringSheafOnSubcategory_of_univ
    (τ : CoveringTopology) (P : ObjectProperty (Over S))
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1)))
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    (hF : IsCoveringSheafOnSubcategory.{max w (u + 1), u, u} τ P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F) :
    IsCoveringSheaf.{max w (u + 1), u, u} τ (extension P F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.13, Tag 0EUV](https://stacks.math.columbia.edu/tag/0EUV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
