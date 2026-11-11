---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.Tag01XLDerivedIso.relativeCechIsoDerivedPushforward, Stacks.AlgebraicGeometry.RelativeCech.relativeCechPresheaf, Stacks.AlgebraicGeometry.RelativeCechComplex.relativeCechComplex, Stacks.AlgebraicGeometry.RelativeCechComplex.relativeCechComplex_obj_isQuasicoherent, Stacks.AlgebraicGeometry.RelativeCechBaseChange.baseChangeRelativeCechIsoDerivedPushforward, Stacks.AlgebraicGeometry.RelativeCechBaseChange.baseChangeRelativeCechComplexIsoOfIsAffineHom, Stacks.AlgebraicGeometry.UniversalPushforward.universalPushforwardComplexOfQuasiSeparated, Stacks.AlgebraicGeometry.UniversalPushforward.universalPushforwardComplex
statement: formalized
proof: formalized
---

# 30.7 Cohomology and base change, II

Section 30.7 of the Stacks Project, [Tag 071M](https://stacks.math.columbia.edu/tag/071M). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01XL, a lemma

[Tag 01XL](https://stacks.math.columbia.edu/tag/01XL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag01XLDerivedIso.relativeCechIsoDerivedPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedIso/Leray.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedIso/Leray.lean#L275). The attribute's comment: “the derived isomorphism”.

> **The relative Čech complex of [Stacks, Tag 01XL] computes `Rf_*ℱ`.**  In `D⁺(S)`,
>
> `Č ⁼(𝒰, f, ℱ) ≅ Rf_*ℱ`,
>
> functorially in the quasi-coherent `𝒪_X`-module `ℱ`.  The hypotheses are those of
> [Stacks, Tag 01XL]: `T` a finite affine open cover of `X` — so `X` is quasi-compact and covered
> by finitely many affine opens — and `X`, `S` of affine diagonal.  Nothing is assumed about `f`.
>
> This is `relativeCechComputesDerivedPushforward` composed with the resolution
> `ℱ[0] ≅ 𝔠 ⁼(𝒰, ℱ)` of [Stacks, Tag 02FU].

```lean
noncomputable def relativeCechIsoDerivedPushforward (f : X ⟶ S) (T : X.AffineOpenCover.{u, u})
    [Fintype T.I₀]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from S))] :
    relativeCechComplex f T ⋙ HomotopyCategory.Plus.quotient S.Modules ⋙
        DerivedCategory.Plus.Qh ≅
      ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf) ⋙
        DerivedCategory.Plus.singleFunctor X.Modules 0 ⋙
          (Scheme.Modules.pushforward f).rightDerivedFunctorPlus
```

**`Stacks.AlgebraicGeometry.RelativeCech.relativeCechPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCech/Basic.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCech/Basic.lean#L329). The attribute's comment: “the coefficient presheaf”.

> The coefficient presheaf of the relative Čech complex of Tag 01XL: the functor sending a
> quasi-coherent `𝒪_X`-module `F` to the presheaf on `Over X` whose value at `A`, with structure
> morphism `a`, is `(a ≫ f)_* a^* F`, with the canonical restriction maps.

```lean
public noncomputable def relativeCechPresheaf (f : X ⟶ S) :
    (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      ((Over X)ᵒᵖ ⥤ S.Modules)
```

**`Stacks.AlgebraicGeometry.RelativeCechComplex.relativeCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/Basic.lean#L72). The attribute's comment: “the complex”.

> **The bounded-below relative Čech complex of a finite affine open cover (Stacks 01XL).**
> The alternating Čech complex, for the family `Over.mk (T.f i)` in `Over X`, of the coefficient
> presheaf of `f`, extended from `ℕ`-indexing to `ℤ`-indexing and regarded as a bounded-below
> complex.

```lean
public noncomputable def relativeCechComplex (f : X ⟶ S) (T : X.AffineOpenCover)
    [Fintype T.I₀] :
    (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      CochainComplex.Plus S.Modules
```

**`Stacks.AlgebraicGeometry.RelativeCechComplex.relativeCechComplex_obj_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/Quasicoherent.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/Quasicoherent.lean#L113). The attribute's comment: “quasi-coherence of the terms”. References: EGA III (1.4.9), “affine diagonal”.

> **Stacks Project, Tag 01XL:** every term of the relative Čech complex of a finite affine
> open cover is a quasi-coherent `𝒪_S`-module.

```lean
public theorem relativeCechComplex_obj_isQuasicoherent (f : X ⟶ S) (T : X.AffineOpenCover)
    [Fintype T.I₀]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from S))]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) (p : ℤ) :
    (((relativeCechComplex f T).obj F).obj.X p).IsQuasicoherent
```

## Tag 01XM, a lemma

[Tag 01XM](https://stacks.math.columbia.edu/tag/01XM) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeCechBaseChange.baseChangeRelativeCechIsoDerivedPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/BaseChangeDerived.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/BaseChangeDerived.lean#L308). The attribute's comment: “the canonical isomorphism”.

> **[Stacks, Tag 01XM], the canonical isomorphism.**  For a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> S' --g-->  S
> ```
> with `X` and `S` of affine diagonal, a finite affine open cover `𝒰` of `X` and a quasi-coherent
> `𝒪_X`-module `ℱ`, there is a canonical isomorphism
>
> `g^* Č ⁼(𝒰, f, ℱ) ≅ Rf'_* (g')^*ℱ`
>
> in `D⁺(S')`: the termwise inverse image of the relative Čech complex is the relative Čech complex
> of the cover `X' = ⋃ Uᵢ ×_X X'` (the base change map of [Stacks, Tag 02KG] on each finite
> intersection), whose finite intersections are affine over `X'` and over `S'`, so that it computes
> `Rf'_*` as in [Stacks, Tag 01XL].

```lean
noncomputable def baseChangeRelativeCechIsoDerivedPushforward :
    DerivedCategory.Plus.Qh.obj ((HomotopyCategory.Plus.quotient S'.Modules).obj
        ((Scheme.Modules.pullback g).mapCochainComplexPlus.obj
          ((relativeCechComplex f T).obj F))) ≅
      (Scheme.Modules.pushforward f').rightDerivedFunctorPlus.obj
        ((DerivedCategory.Plus.singleFunctor X'.Modules 0).obj
          ((Scheme.Modules.pullback g').obj F.obj))
```

**`Stacks.AlgebraicGeometry.RelativeCechBaseChange.baseChangeRelativeCechComplexIsoOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/BaseChangeDerived.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/BaseChangeDerived.lean#L358). The attribute's comment: “the affine case”.

> **[Stacks, Tag 01XM], the affine case.**  For a cartesian square as in
> `baseChangeRelativeCechIsoDerivedPushforward` with `g : S' ⟶ S` affine, the members
> `U'ᵢ = (g')^{-1}(Uᵢ) = Uᵢ ×_X X'` of the inverse-image cover `𝒰'` are affine, and the termwise
> inverse image of the relative Čech complex is the relative Čech complex of this affine open cover:
>
> `g^* Č ⁼(𝒰, f, ℱ) ≅ Č ⁼(𝒰', f', (g')^*ℱ)`
>
> as bounded below complexes of `𝒪_{S'}`-modules.

```lean
noncomputable def baseChangeRelativeCechComplexIsoOfIsAffineHom [IsAffineHom g] :
    letI : IsAffineHom g' := MorphismProperty.of_isPullback hw.flip inferInstance
    (Scheme.Modules.pullback g).mapCochainComplexPlus.obj ((relativeCechComplex f T).obj F) ≅
      (relativeCechComplex f' (inverseImageAffineOpenCover g' T)).obj (pullbackQcohObj g' F)
```

## Tag 01XN, a lemma

[Tag 01XN](https://stacks.math.columbia.edu/tag/01XN) in the Stacks Project.

**`Stacks.AlgebraicGeometry.UniversalPushforward.universalPushforwardComplexOfQuasiSeparated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/HypercoveringDerivedPushforward.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/HypercoveringDerivedPushforward.lean#L373).

> **Stacks Project, Tag 01XN.**  Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes with `S` quasi-compact and separated, and let `𝓕` be a quasi-coherent
> `𝒪_X`-module.  There is a bounded below complex `𝓚⁼` of quasi-coherent `𝒪_S`-modules such that
> for every morphism `g : S' ⟶ S` the complex `g^*𝓚⁼` represents `Rf'_*𝓕'` in `D⁺(S')`, with the
> notation of the cartesian square of [Stacks, Tag 02KF].
>
> The complex is `𝓚⁼(K, f, 𝓕) = ( ∏_{i ∈ I₀} f_{i,*}𝓕|_{U_i} ⟶ ∏_{i ∈ I₁} f_{i,*}𝓕|_{U_i} ⟶ ⋯ )`
> for a hypercovering `K = (I, {U_i})` of `X` finite in every degree by affine opens
> (`exists_finite_affine_hypercovering_isAffineHom`, [Stacks, Tag 01H7]); its terms are
> quasi-coherent because each `f_i : U_i ⟶ S` is affine, `S` being separated, and the
> base-change isomorphisms are `nonempty_baseChangeIso`.

```lean
def universalPushforwardComplexOfQuasiSeparated (f : X ⟶ S) [QuasiCompact f]
    [QuasiSeparated f] [CompactSpace S] [S.IsSeparated]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    UniversalPushforwardComplex f F
```

**`Stacks.AlgebraicGeometry.UniversalPushforward.universalPushforwardComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforward.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforward.lean#L488). The attribute's comment: “for an affine morphism”.

> **Stacks Project, Tag 01XN, for an affine morphism.**  Let `f : X ⟶ S` be an affine morphism
> of schemes and `𝓕` a quasi-coherent `𝒪_X`-module.  Then `f_*𝓕` placed in degree zero is a bounded
> below complex of quasi-coherent `𝒪_S`-modules whose ordinary inverse image along *every*
> `g : S' ⟶ S` represents `Rf'_*𝓕'` in `D⁺(S')`, with the notation of the cartesian square of
> [Stacks, Tag 02KF].
>
> The three fields are discharged separately.  The complex is the single complex, so its terms are
> `f_*𝓕` in degree zero — quasi-coherent because `f` is affine ([Stacks, Tag 01XD]) — and zero
> objects elsewhere.  The base-change isomorphism for every `g` is `affineBaseChangeSingleIso`:
> affineness is stable under base change, so no hypothesis on `S'` is needed and the universal
> quantification over `g` is genuine.

```lean
noncomputable def universalPushforwardComplex (f : X ⟶ S) [IsAffineHom f]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    UniversalPushforwardComplex f F
```

**`Stacks.AlgebraicGeometry.UniversalPushforward.nonempty_universalPushforwardComplex_of_isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforwardAffineDiagonal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforwardAffineDiagonal.lean#L96). The attribute's comment: “for a source of affine diagonal”.

> Let `f : X ⟶ S` be a quasi-compact, quasi-separated morphism of schemes, let `S` be
> quasi-compact and separated and let `𝓕` be a quasi-coherent `𝒪_X`-module. If `X` has affine
> diagonal then there is a bounded below complex `𝓚⁼` of quasi-coherent `𝒪_S`-modules such that
> for every `g : S' ⟶ S` the ordinary inverse image `g^*𝓚⁼` represents `Rf'_*𝓕'` in `D⁺(S')`.

```lean
theorem nonempty_universalPushforwardComplex_of_isAffineHom_diagonal (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] [S.IsSeparated]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    Nonempty (UniversalPushforwardComplex f F)
```

**`Stacks.AlgebraicGeometry.UniversalPushforward.nonempty_universalPushforwardComplex_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforwardAffineDiagonal.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeCechComplex/UniversalPushforwardAffineDiagonal.lean#L109). The attribute's comment: “for a separated morphism”.

> Let `f : X ⟶ S` be a quasi-compact, separated morphism of schemes, let `S` be quasi-compact
> and separated and let `𝓕` be a quasi-coherent `𝒪_X`-module. Then there is a bounded below
> complex `𝓚⁼` of quasi-coherent `𝒪_S`-modules such that for every `g : S' ⟶ S` the ordinary
> inverse image `g^*𝓚⁼` represents `Rf'_*𝓕'` in `D⁺(S')`.

```lean
theorem nonempty_universalPushforwardComplex_of_isSeparated (f : X ⟶ S)
    [QuasiCompact f] [IsSeparated f] [CompactSpace S] [S.IsSeparated]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    Nonempty (UniversalPushforwardComplex f F)
```

## Tag 0GN5, a lemma

[Tag 0GN5](https://stacks.math.columbia.edu/tag/0GN5) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ModuleBaseChange.isIso_degreewiseComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatModuleCohomologyBaseChange/QuasiSeparated.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FlatModuleCohomologyBaseChange/QuasiSeparated.lean#L381).

> **[Stacks, Tag 0GN5].**  Let
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> be a cartesian square of schemes with `f` quasi-compact and quasi-separated, let `G` be a
> quasi-coherent `𝒪_{S'}`-module flat over `S` and let `F` be a quasi-coherent `𝒪_X`-module.  Then
> the degreewise comparison
>
> `Φ(R ⁱ f_* F) ⟶ R ⁱ f'_*(Ψ F)`
>
> of the two coefficient functors `Φ : M ↦ g^*M ⊗ G` and `Ψ : F ↦ (g')^*F ⊗ (f')^*G` is an
> isomorphism in every degree `i`.

```lean
theorem isIso_degreewiseComparison_app (H : IsPullback g' f' f g)
    [QuasiCompact f] [QuasiSeparated f]
    (G : SheafOfModules.{u} (structureSheafRing S'.toRingedSpace)) [G.IsQuasicoherent]
    (hG : AlgebraicGeometry.IsFlatOver g.toLRSHom.toShHom G)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    (i : ℕ) :
    IsIso ((degreewiseComparison H G hG i).app F)
```

**`Stacks.Cohomology.DerivedTensorBaseChange.tensorBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L181). The attribute's comment: “the canonical map from left to right, in the derived category”.

> **The left-to-right map of [Stacks, Tag 0GN5]** attached to a commutative square of ringed
> spaces:
>
> `G ⊗^L_{𝒪_{S'}} Lg^*Rf_*F ⟶ Rf'_*(L(f')^*G ⊗^L_{𝒪_{X'}} L(g')^*F)`.
>
> It is the adjunction unit `G ⟶ Rf'_*L(f')^*G` of Stacks 079W in the first tensor factor and the
> derived base change map of Stacks 08HY in the second, followed by the relative cup product of
> Stacks 0B68 for `f'`.

```lean
def tensorBaseChangeMap (G : DerivedCategory (SheafOfModules.{u} (structureSheafRing S')))
    (F : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((derivedTensorProductFunctor S'.sheaf).obj G).obj
        ((derivedPullback g).obj ((derivedPushforward f).obj F)) ⟶
      (derivedPushforward f').obj
        (((derivedTensorProductFunctor X'.sheaf).obj ((derivedPullback f').obj G)).obj
          ((derivedPullback g').obj F))
```

**`Stacks.Cohomology.DerivedTensorBaseChange.tensorBaseChangeMap_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L207). The attribute's comment: “naturality of the canonical map in the module on the base”.

> The map of [Stacks, Tag 0GN5] is natural in the derived module on the base `S'`.

```lean
theorem tensorBaseChangeMap_naturality_left
    {G G' : DerivedCategory (SheafOfModules.{u} (structureSheafRing S'))} (w : G ⟶ G')
    (F : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((derivedTensorProductFunctor S'.sheaf).map w).app
          ((derivedPullback g).obj ((derivedPushforward f).obj F)) ≫
        tensorBaseChangeMap g' f' f g sq G' F =
      tensorBaseChangeMap g' f' f g sq G F ≫
        (derivedPushforward f').map
          (((derivedTensorProductFunctor X'.sheaf).map ((derivedPullback f').map w)).app
            ((derivedPullback g').obj F))
```

**`Stacks.Cohomology.DerivedTensorBaseChange.tensorBaseChangeMap_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L224). The attribute's comment: “naturality of the canonical map in the module upstairs”.

> The map of [Stacks, Tag 0GN5] is natural in the derived module on `X`.

```lean
theorem tensorBaseChangeMap_naturality_right
    (G : DerivedCategory (SheafOfModules.{u} (structureSheafRing S')))
    {F F' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))} (u : F ⟶ F') :
    ((derivedTensorProductFunctor S'.sheaf).obj G).map
          ((derivedPullback g).map ((derivedPushforward f).map u)) ≫
        tensorBaseChangeMap g' f' f g sq G F' =
      tensorBaseChangeMap g' f' f g sq G F ≫
        (derivedPushforward f').map
          (((derivedTensorProductFunctor X'.sheaf).obj ((derivedPullback f').obj G)).map
            ((derivedPullback g').map u))
```

**`Stacks.Cohomology.DerivedTensorBaseChange.schemeTensorBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L259). The attribute's comment: “the canonical map from left to right, for a cartesian square of schemes”.

> **The left-to-right map of [Stacks, Tag 0GN5]** for the cartesian square of schemes of
> [Stacks, Tag 02KF]:
>
> `G ⊗^L_{𝒪_{S'}} Lg^*Rf_*F ⟶ Rf'_*(L(f')^*G ⊗^L_{𝒪_{X'}} L(g')^*F)`.
>
> It is the map above at the underlying ringed spaces.

```lean
def schemeTensorBaseChangeMap (H : IsPullback g' f' f g) (G : DerivedCategory S'.Modules)
    (F : DerivedCategory X.Modules) :
    ((derivedTensorProductFunctor S'.toRingedSpace.sheaf).obj G).obj
        ((derivedPullback g.toLRSHom.toShHom).obj
          ((derivedPushforward f.toLRSHom.toShHom).obj F)) ⟶
      (derivedPushforward f'.toLRSHom.toShHom).obj
        (((derivedTensorProductFunctor X'.toRingedSpace.sheaf).obj
            ((derivedPullback f'.toLRSHom.toShHom).obj G)).obj
          ((derivedPullback g'.toLRSHom.toShHom).obj F))
```

**`Stacks.Cohomology.DerivedTensorBaseChange.schemeTensorBaseChangeMap_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L278). The attribute's comment: “naturality for a cartesian square of schemes, in the module on the base”.

> The map of [Stacks, Tag 0GN5] for a cartesian square of schemes is natural in the derived
> module on the base `S'`.

```lean
theorem schemeTensorBaseChangeMap_naturality_left (H : IsPullback g' f' f g)
    {G G' : DerivedCategory S'.Modules} (w : G ⟶ G') (F : DerivedCategory X.Modules) :
    ((derivedTensorProductFunctor S'.toRingedSpace.sheaf).map w).app
          ((derivedPullback g.toLRSHom.toShHom).obj
            ((derivedPushforward f.toLRSHom.toShHom).obj F)) ≫
        schemeTensorBaseChangeMap H G' F =
      schemeTensorBaseChangeMap H G F ≫
        (derivedPushforward f'.toLRSHom.toShHom).map
          (((derivedTensorProductFunctor X'.toRingedSpace.sheaf).map
            ((derivedPullback f'.toLRSHom.toShHom).map w)).app
              ((derivedPullback g'.toLRSHom.toShHom).obj F))
```

**`Stacks.Cohomology.DerivedTensorBaseChange.schemeTensorBaseChangeMap_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/TensorBaseChangeMap.lean#L294). The attribute's comment: “naturality for a cartesian square of schemes, in the module upstairs”.

> The map of [Stacks, Tag 0GN5] for a cartesian square of schemes is natural in the derived
> module on `X`.

```lean
theorem schemeTensorBaseChangeMap_naturality_right (H : IsPullback g' f' f g)
    (G : DerivedCategory S'.Modules) {F F' : DerivedCategory X.Modules} (u : F ⟶ F') :
    ((derivedTensorProductFunctor S'.toRingedSpace.sheaf).obj G).map
          ((derivedPullback g.toLRSHom.toShHom).map
            ((derivedPushforward f.toLRSHom.toShHom).map u)) ≫
        schemeTensorBaseChangeMap H G F' =
      schemeTensorBaseChangeMap H G F ≫
        (derivedPushforward f'.toLRSHom.toShHom).map
          (((derivedTensorProductFunctor X'.toRingedSpace.sheaf).obj
            ((derivedPullback f'.toLRSHom.toShHom).obj G)).map
              ((derivedPullback g'.toLRSHom.toShHom).map u))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.7, Tag 071M](https://stacks.math.columbia.edu/tag/071M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
