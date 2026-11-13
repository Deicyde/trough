---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsFlatAt, AlgebraicGeometry.IsFlatOverAt, AlgebraicGeometry.Flat, AlgebraicGeometry.IsFlatOver, AlgebraicGeometry.isFlatOver_tfae, AlgebraicGeometry.isFlatOver_resLE, AlgebraicGeometry.flat_resLE, AlgebraicGeometry.flat_tfae
statement: formalized
proof: formalized
---

# 29.26 Flat morphisms

Section 29.26 of the Stacks Project, [Tag 01U2](https://stacks.math.columbia.edu/tag/01U2). 15 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01U3, a definition

[Tag 01U3](https://stacks.math.columbia.edu/tag/01U3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsFlatAt`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L38) (StacksFrontier): “part (1)”.
- [`AlgebraicGeometry.IsFlatOverAt`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L39) (StacksFrontier): “part (2)”.
- [`AlgebraicGeometry.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L40) (StacksFrontier): “part (3)”. References: EGA 0 (6.7.1); EGA IV (2.1.1); SGA 3 III (2.0), “partial”; SGA 7 VII (1.3.8), “flatness of p”.
- [`AlgebraicGeometry.IsFlatOver`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L80), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L45) (StacksFrontier): “part (4)”.

## Tag 01U4, a lemma

[Tag 01U4](https://stacks.math.columbia.edu/tag/01U4) in the Stacks Project.

**`AlgebraicGeometry.isFlatOver_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/QuasicoherentCriteria.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/QuasicoherentCriteria.lean#L586). The attribute's comment: “flatness characterization”.

> For a morphism of schemes `f : X ⟶ S` and a quasi-coherent module `F` on `X`, the following
> are equivalent:
> 1. `F` is flat over `S`;
> 2. for all affine opens `U` of `X` and `V` of `S` with `U ≤ f ⁻¹ᵁ V`, the sections `Γ(F, U)` are
>    flat over `Γ(S, V)`;
> 3. there is an open cover `V` of `S` and, for each `j`, an open cover `U` of `f ⁻¹ᵁ V j` such that
>    each restriction of `F` to `U i` is flat over `V j`;
> 4. there is an affine open cover `V` of `S` and, for each `j`, an affine open cover `U` of
>    `f ⁻¹ᵁ V j` such that each `Γ(F, U i)` is flat over `Γ(S, V j)`.

```lean
public theorem isFlatOver_tfae {X S : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) [F.IsQuasicoherent] :
    List.TFAE [
      IsFlatOver f.toLRSHom.toShHom F,
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : S.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
        let : Module Γ(S, V) Γ(F, U) :=
          Module.compHom Γ(F, U) (f.appLE V U hUV).hom
        Module.Flat Γ(S, V) Γ(F, U),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            ∀ i, IsFlatOver
              (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)).toLRSHom.toShHom
              (F.restrict (U i).ι),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i,
                let hUV : U i ≤ f ⁻¹ᵁ V j := (le_iSup U i).trans hU.le
                let : Module Γ(S, V j) Γ(F, U i) :=
                  Module.compHom Γ(F, U i) (f.appLE (V j) (U i) hUV).hom
                Module.Flat Γ(S, V j) Γ(F, U i)]
```

**`AlgebraicGeometry.isFlatOver_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/QuasicoherentCriteria.lean, line 696](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/QuasicoherentCriteria.lean#L696). The attribute's comment: “restriction to open subschemes”.

> A module flat over the target remains flat over any compatible open
> subscheme of the target after restriction to an open of the source.

```lean
public theorem isFlatOver_resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (F : X.Modules) (hF : IsFlatOver f.toLRSHom.toShHom F)
    (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V) :
    IsFlatOver (f.resLE V U hUV).toLRSHom.toShHom
      (F.restrict U.ι)
```

## Tag 01U5, a lemma

[Tag 01U5](https://stacks.math.columbia.edu/tag/01U5) in the Stacks Project.

**`AlgebraicGeometry.flat_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean#L64). The attribute's comment: “moreover: restriction to open subschemes”.

> If `f` is flat then so is its restriction `U → V` to any opens `U ⊆ X`, `V ⊆ S` with
> `f(U) ⊆ V`.

```lean
theorem flat_resLE {f : X ⟶ S} (hf : Flat f) (V : S.Opens) (U : X.Opens)
    (e : U ≤ f ⁻¹ᵁ V) : Flat (f.resLE V U e)
```

**`AlgebraicGeometry.flat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean#L76). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> Flatness of a morphism of schemes can be checked on all pairs of affine opens, on open
> coverings of target and preimages, or on affine such coverings.
>
> The source defines flatness of `f` by flatness of the local ring maps
> `𝒪_{S, f(x)} → 𝒪_{X, x}`; this agrees with `AlgebraicGeometry.Flat` by
> `AlgebraicGeometry.Flat.iff_flat_stalkMap`.

```lean
theorem flat_tfae (f : X ⟶ S) :
    List.TFAE [
      Flat f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Flat,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, Flat (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.Flat]
```

**`AlgebraicGeometry.flat_tfae_and_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Flat.lean#L96).

> The whole statement: the four characterizations of flatness agree, and flatness passes to
> restrictions to open subschemes.
>
> The source defines flatness of `f` by flatness of the local ring maps
> `𝒪_{S, f(x)} → 𝒪_{X, x}`; this agrees with `AlgebraicGeometry.Flat` by
> `AlgebraicGeometry.Flat.iff_flat_stalkMap`.

```lean
theorem flat_tfae_and_resLE (f : X ⟶ S) :
    List.TFAE [
      Flat f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.Flat,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, Flat (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.Flat] ∧
    (Flat f → ∀ (U : X.Opens) (V : S.Opens) (e : U ≤ f ⁻¹ᵁ V), Flat (f.resLE V U e))
```

## Tag 0FLM, a lemma

[Tag 0FLM](https://stacks.math.columbia.edu/tag/0FLM) in the Stacks Project.

**`AlgebraicGeometry.isFlatOver_pushforward_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/AffinePushforward.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/AffinePushforward.lean#L71).

> **Stacks Project, Tag 0FLM.** A quasi-coherent module on the source of an affine morphism is
> flat over a base scheme if and only if its direct image is.

```lean
public theorem isFlatOver_pushforward_iff {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [IsAffineHom f] (F : X.Modules) [F.IsQuasicoherent] :
    IsFlatOver (f ≫ g).toLRSHom.toShHom F ↔
      IsFlatOver g.toLRSHom.toShHom ((Scheme.Modules.pushforward f).obj F)
```

## Tag 01U6, a lemma

[Tag 01U6](https://stacks.math.columbia.edu/tag/01U6) in the Stacks Project.

**`AlgebraicGeometry.IsFlatOverAt.comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Module.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Module.lean#L43).

> Flatness of a module over a ringed space at a point is transitive along a
> flat morphism of target ringed spaces.

```lean
public lemma comp {X Y Z : RingedSpace.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf)) (x : X)
    (hF : AlgebraicGeometry.IsFlatOverAt f F x)
    (hY : AlgebraicGeometry.IsFlatAt g (f.hom.base x)) :
    AlgebraicGeometry.IsFlatOverAt (f ≫ g) F x
```

## Tag 01U7, a lemma

[Tag 01U7](https://stacks.math.columbia.edu/tag/01U7) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Flat.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L321) (StacksFrontier). References: EGA 0 (6.7.5), “Schemes (EGA preschemes)”; EGA IV (2.1.5), “global case Y' = Y”; EGA IV (2.1.6); EGA IV (2.2.11), “(iii), special case”; EGA IV (2.2.13), “(iii)”; EGA IV (6.6.1), “(i): flatness of h = g∘f”; EGA IV (7.3.5), “partial”; SGA 3 VIIB (1.3.3), “(i), special case”.

## Tag 01U8, a lemma

[Tag 01U8](https://stacks.math.columbia.edu/tag/01U8) in the Stacks Project.

**`AlgebraicGeometry.modulePullback_isFlatOverAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/BaseChange.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/BaseChange.lean#L167). The attribute's comment: “flatness at a point”. References: EGA IV (2.1.4), “pointwise statement”; SGA 3 V (7.4), “(i) base change”.

> The pullback of a quasi-coherent module which is flat over the base at the image of a point is
> flat over the new base at that point.

```lean
public lemma modulePullback_isFlatOverAt
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    (x' : X') (hF : AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F (g' x')) :
    AlgebraicGeometry.IsFlatOverAt f'.toLRSHom.toShHom
      ((modulePullback g'.toLRSHom.toShHom).obj F) x'
```

**`AlgebraicGeometry.modulePullback_isFlatOver`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/BaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/BaseChange.lean#L207). The attribute's comment: “global flatness”. References: EGA IV (2.1.4), “global module case”.

> The pullback of a quasi-coherent module flat over the base is flat over the new base.

```lean
public lemma modulePullback_isFlatOver
    {X S S' X' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (h : IsPullback g' f' f g)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    (hF : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F) :
    AlgebraicGeometry.IsFlatOver f'.toLRSHom.toShHom
      ((modulePullback g'.toLRSHom.toShHom).obj F)
```

## Tag 01U9, a lemma

[Tag 01U9](https://stacks.math.columbia.edu/tag/01U9) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Flat.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L324) (StacksFrontier). References: EGA III (7.7.2), “special case”; EGA III (7.9.7), “special case”; EGA IV (11.5.4), “necessity”; EGA IV (2.1.4); EGA IV (2.2.13), “(i)”; EGA IV (2.5.1), “special case”; EGA IV (20.6.9), “flatness of X' over S'”; EGA IV (21.15.9), “partial”; EGA IV (7.3.5), “partial”; SGA 3 III (0.13), “partial”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (11.1); SGA 3 VIB (2.1.2), “partial”; SGA 3 VIB (3.11), “fiber-flatness”; SGA 3 VIIB (1.3.3), “(iii), special case”; SGA 3 XIX (2.1); SGA 4 Vbis (3.3), “special case”; SGA 6 0 (2.9), “special case”; SGA 6 XII (2.3), “(a)”; SGA 6 XII (4.1), “(1)”; SGA 7 VII (1.3.8), “partial”.

## Tag 03HV, a lemma

[Tag 03HV](https://stacks.math.columbia.edu/tag/03HV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Flat.generalizingMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.generalizingMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L117) (StacksFrontier). References: EGA IV (2.3.4), “(i), special case”; EGA IV (2.3.5), “special case”.

## Tag 01UA, a lemma

[Tag 01UA](https://stacks.math.columbia.edu/tag/01UA) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_flat_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/UniversallyOpen.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/UniversallyOpen.lean#L144). References: EGA IV (15.2.1); EGA IV (2.4.6); SGA 3 VIB (4.3); SGA 3 XVI (2.1), “more general”; SGA 6 VIII (1.3), “more general”.

> **Stacks Project, Tag 01UA.** A flat morphism of schemes which is locally of finite
> presentation is universally open.

```lean
public theorem universallyOpen_of_flat_of_locallyOfFinitePresentation {X Y : Scheme.{u}}
    (f : X ⟶ Y) [Flat f] [LocallyOfFinitePresentation f] : UniversallyOpen f
```

## Tag 0CVT, a lemma

[Tag 0CVT](https://stacks.math.columbia.edu/tag/0CVT) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_isFlatOver_of_supp_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/UniversallyOpen.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/UniversallyOpen.lean#L114). References: EGA IV (11.3.1), “f|U open”; EGA IV (2.4.6).

> **Stacks Project, Tag 0CVT.** A morphism of schemes locally of finite presentation admitting
> a finite type quasi-coherent module of full support which is flat over the target is universally
> open.

```lean
public theorem universallyOpen_of_isFlatOver_of_supp_eq_univ {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFinitePresentation f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hsupp : SheafOfModules.supp F = Set.univ)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) : UniversallyOpen f
```

## Tag 02JY, a lemma

[Tag 02JY](https://stacks.math.columbia.edu/tag/02JY) in the Stacks Project.

**`AlgebraicGeometry.Flat.isOpen_iff_isOpen_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Submersive.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Submersive.lean#L38). The attribute's comment: “the open half: `T` is open if and only if `f ⁻¹' T` is open”.

> A subset of the target of a quasi-compact, surjective, flat morphism of schemes is open if and
> only if its preimage is open.

```lean
public theorem Flat.isOpen_iff_isOpen_preimage {T : Set Y} : IsOpen T ↔ IsOpen (f ⁻¹' T)
```

**`AlgebraicGeometry.Flat.isClosed_iff_isClosed_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Submersive.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Submersive.lean#L44). The attribute's comment: “the closed half: `T` is closed if and only if `f ⁻¹' T` is closed”.

> A subset of the target of a quasi-compact, surjective, flat morphism of schemes is closed if
> and only if its preimage is closed.

```lean
public theorem Flat.isClosed_iff_isClosed_preimage {T : Set Y} :
    IsClosed T ↔ IsClosed (f ⁻¹' T)
```

## Tag 02JZ, a lemma

[Tag 02JZ](https://stacks.math.columbia.edu/tag/02JZ) in the Stacks Project.

**`AlgebraicGeometry.flat_of_comp_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Descent.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/Descent.lean#L38). The attribute's comment: “descent of scheme flatness”.

> **Stacks Project, Tag 02JZ (second global consequence).** If `f : X ⟶ Y`
> is surjective and flat and `X` is flat over `S`, then `Y` is flat over `S`.

```lean
public theorem flat_of_comp_of_surjective_flat
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    [Surjective f] [Flat f] [Flat (f ≫ q)] : Flat q
```

**`AlgebraicGeometry.isFlatOverAt_iff_modulePullback_isFlatOverAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/PullbackFlatness.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/PullbackFlatness.lean#L53). The attribute's comment: “pointwise equivalence”.

> **Stacks Project, Tag 02JZ (pointwise assertion).** If `f : X ⟶ Y` is
> flat at `x`, then a module `G` on `Y` is flat over `S` at
> `f(x)` if and only if its pullback to `X` is flat over `S` at `x`.

```lean
public theorem isFlatOverAt_iff_modulePullback_isFlatOverAt
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    (G : SheafOfModules.{u} (structureSheafRing Y.toRingedSpace))
    (x : X) (hf : AlgebraicGeometry.IsFlatAt f.toLRSHom.toShHom x) :
      AlgebraicGeometry.IsFlatOverAt q.toLRSHom.toShHom G (f.base x) ↔
      AlgebraicGeometry.IsFlatOverAt (f ≫ q).toLRSHom.toShHom
        ((modulePullback f.toLRSHom.toShHom).obj G) x
```

**`AlgebraicGeometry.isFlatOver_iff_modulePullback_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/PullbackFlatness.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/PullbackFlatness.lean#L98). The attribute's comment: “global equivalence”.

> **Stacks Project, Tag 02JZ (first global consequence).** Pullback along a
> surjective flat morphism detects whether a module is flat over
> the base.

```lean
public theorem isFlatOver_iff_modulePullback_isFlatOver
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    (G : SheafOfModules.{u} (structureSheafRing Y.toRingedSpace))
    [Surjective f] [Flat f] :
    AlgebraicGeometry.IsFlatOver q.toLRSHom.toShHom G ↔
      AlgebraicGeometry.IsFlatOver (f ≫ q).toLRSHom.toShHom
        ((modulePullback f.toLRSHom.toShHom).obj G)
```

## Tag 07T9, a lemma

[Tag 07T9](https://stacks.math.columbia.edu/tag/07T9) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticFlatPullback.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticFlatPullback.lean#L70).

> The scheme-theoretic inverse image of the scheme-theoretic support of a finite type
> quasi-coherent module along a flat morphism is the scheme-theoretic support of its pullback.

```lean
theorem schemeTheoreticSupport_pullback {X Y : Scheme.{u}} (f : Y ⟶ X) [Flat f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    schemeTheoreticSupport ((Scheme.Modules.pullback f).obj F) =
      (schemeTheoreticSupport F).comap f
```

## Tag 081I, a lemma

[Tag 081I](https://stacks.math.columbia.edu/tag/081I) in the Stacks Project.

**`AlgebraicGeometry.ker_pullback_snd_eq_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/SchemeTheoreticImage.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/SchemeTheoreticImage.lean#L50). References: EGA IV (2.3.2).

> **Stacks Project, Tag 081I.** The defining ideal sheaf of the scheme-theoretic image of a
> quasi-compact morphism after flat base change is the inverse image of its defining ideal
> sheaf.

```lean
public theorem ker_pullback_snd_eq_comap {X Y V : Scheme.{u}}
    (f : X ⟶ Y) (g : V ⟶ Y) [Flat f] [QuasiCompact g] :
    (pullback.snd g f).ker = g.ker.comap f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.26, Tag 01U2](https://stacks.math.columbia.edu/tag/01U2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
