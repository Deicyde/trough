---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedKunnethExt.kunnethExtMap, Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_fibreProduct, Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_cartesian
statement: formalized
proof: formalized
---

# 36.25 Künneth formula for Ext

Section 36.25 of the Stacks Project, [Tag 0FXX](https://stacks.math.columbia.edu/tag/0FXX). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FXY, an equation

[Tag 0FXY](https://stacks.math.columbia.edu/tag/0FXY) in the Stacks Project.

**`Stacks.Cohomology.DerivedKunnethExt.kunnethExtMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMapForExt.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMapForExt.lean#L255).

> **The Künneth morphism for Ext**
> `Ra_*R SheafHom(K, K') ⊗^L_{𝒪_S} Rb_*R SheafHom(M, M') ⟶ Rf_*(R SheafHom(K ⊠ M, K' ⊠ M'))`,
> Equation 36.25.0.1: the relative Künneth morphism of Stacks 0FLP at the two derived internal
> homs, followed by the pushforward of
> `Stacks.Cohomology.DerivedKunnethExt.boxSheafHomMap`.  It is defined for arbitrary
> `K, K' ∈ D(𝒪_X)` and `M, M' ∈ D(𝒪_Y)`.

```lean
def kunnethExtMap (K K' : DerivedCategory (Mod X.sheaf))
    (M M' : DerivedCategory (Mod Y.sheaf)) :
    tensorObj S ((derivedPushforwardFunctor a).obj (sheafHomObj X K K'))
        ((derivedPushforwardFunctor b).obj (sheafHomObj Y M M')) ⟶
      (derivedPushforwardFunctor f).obj
        (sheafHomObj W (boxProd p q K M) (boxProd p q K' M'))
```

## Tag 0FXZ, a lemma

[Tag 0FXZ](https://stacks.math.columbia.edu/tag/0FXZ) in the Stacks Project.

**`Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtFibreProduct.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtFibreProduct.lean#L61).

> Let `a : X ⟶ S` and `b : Y ⟶ S` be quasi-compact and quasi-separated morphisms of schemes,
> and let `X` and `Y` be Tor independent over `S`. Let `W = X ×_S Y` with its two projections `p`
> and `q` and `f = p ≫ a`. If `K ∈ D(𝒪_X)` is perfect, `K' ∈ D_QCoh(𝒪_X)`, `M ∈ D(𝒪_Y)` is perfect
> and `M' ∈ D_QCoh(𝒪_Y)`, then the Künneth morphism for Ext (Equation 36.25.0.1)
>
> `Ra_*R𝓗om(K, K') ⊗^𝐋_{𝒪_S} Rb_*R𝓗om(M, M') ⟶ Rf_*(R𝓗om(K ⊠ M, K' ⊠ M'))`
>
> is an isomorphism.

```lean
theorem isIso_kunnethExtMap_fibreProduct
    [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (hTor : AlgebraicGeometry.TorIndependent a b)
    (K K' : DerivedCategory X.Modules) (M M' : DerivedCategory Y.Modules)
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (hK' : IsDQCoh (R := X.ringCatSheaf) K')
    (hM : RingedSpace.IsPerfect (X := Y.toRingedSpace) M)
    (hM' : IsDQCoh (R := Y.ringCatSheaf) M') :
    IsIso (kunnethExtMap a.toLRSHom.toShHom b.toLRSHom.toShHom
      (pullback.fst a b).toLRSHom.toShHom (pullback.snd a b).toLRSHom.toShHom
      (pullback.fst a b ≫ a).toLRSHom.toShHom rfl
      (Stacks.Cohomology.GlobalKunneth.toShHom_pullback_condition a b) K K' M M')
```

**`Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtIsomorphism.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtIsomorphism.lean#L245). The attribute's comment: “at an arbitrary cartesian square of schemes”.

> Let `a : X ⟶ S` and `b : Y ⟶ S` be quasi-compact and quasi-separated morphisms of schemes,
> and let `X` and `Y` be Tor independent over `S`.  Let `p : W ⟶ X` and `q : W ⟶ Y` make `W` a
> fibre product of `a` and `b`, and let `f = p ≫ a`.  If `K ∈ D(𝒪_X)` is perfect,
> `K' ∈ D_QCoh(𝒪_X)`, `M ∈ D(𝒪_Y)` is perfect and `M' ∈ D_QCoh(𝒪_Y)`, then the Künneth morphism
> for Ext of Stacks 0FXY
>
> `Ra_*R SheafHom(K, K') ⊗^𝐋_{𝒪_S} Rb_*R SheafHom(M, M') ⟶ Rf_*(R SheafHom(K ⊠ M, K' ⊠ M'))`
>
> is an isomorphism.

```lean
theorem isIso_kunnethExtMap_cartesian (hW : IsPullback p q a b)
    [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (htor : AlgebraicGeometry.TorIndependent a b)
    (K K' : DerivedCategory X.Modules) (M M' : DerivedCategory Y.Modules)
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (hK' : IsDQCoh (R := X.ringCatSheaf) K')
    (hM : RingedSpace.IsPerfect (X := Y.toRingedSpace) M)
    (hM' : IsDQCoh (R := Y.ringCatSheaf) M') :
    IsIso (kunnethExtMap a.toLRSHom.toShHom b.toLRSHom.toShHom p.toLRSHom.toShHom
      q.toLRSHom.toShHom (p ≫ a).toLRSHom.toShHom rfl (toShHom_isPullback_w a b p q hW)
      K K' M M')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.25, Tag 0FXX](https://stacks.math.columbia.edu/tag/0FXX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
