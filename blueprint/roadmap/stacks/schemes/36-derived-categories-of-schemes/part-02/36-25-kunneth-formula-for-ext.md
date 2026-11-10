---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedKunnethExt.kunnethExtMap, Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_fibreProduct, Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_cartesian
statement: formalized
proof: formalized
---

# 36.25 Künneth formula for Ext

Section 36.25 of the Stacks Project, [Tag 0FXX](https://stacks.math.columbia.edu/tag/0FXX). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FXY, an equation

[Tag 0FXY](https://stacks.math.columbia.edu/tag/0FXY) in the Stacks Project.

**`Stacks.Cohomology.DerivedKunnethExt.kunnethExtMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMapForExt.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMapForExt.lean#L255).

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

**`Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtFibreProduct.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtFibreProduct.lean#L61).

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

**`Stacks.Cohomology.DerivedKunnethExt.isIso_kunnethExtMap_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtIsomorphism.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethExtIsomorphism.lean#L279). The attribute's comment: “for a and b quasi-compact and quasi-separated, X and Y Tor independent over S, K and M perfect and K', M' in D_QCoh, the Künneth morphism for Ext of Tag 0FXY at a cartesian square of schemes is invertible. Both steps of the source's two-step proof are carried as explicit hypotheses and the source's geometric hypotheses are consequently not consumed: hkunneth is the invertibility of the relative Künneth morphism of Tag 0FLP at the pair (RSheafHom(K,K'), RSheafHom(M,M')), which is Tag 0FLQ. That tag is carried, for this same kunnethMap, by isIso_kunnethMap_of_projectionFormulas_of_baseChange, but itself only conditionally, on four named inputs: the projection formula of Tag 08EU for a and for p, the Tor-independent base-change comparison of Tag 08IB for the square, and the Tag 079U/0D5S monoidality coherence. So hkunneth is exactly that carrier's conclusion and is obtainable from it once those four are supplied; it is carried here as one hypothesis rather than four. Perfectness of K and M does not discharge them, because 0FLQ is applied to RSheafHom(K,K') and RSheafHom(M,M'), which for K' and M' merely in D_QCoh are quasi-coherent and not perfect. And hbox is the invertibility of the canonical comparison Lp^*RSheafHom(K,K') (x)^L Lq^*RSheafHom(M,M') -> RSheafHom(K [x] M, K' [x] M'), which is where the source uses perfectness, through the identification RSheafHom(K,K') = K' (x)^L K^dual of Cohomology Tag 08DQ, of which the repository carries only the statement that the dual of a perfect object is perfect, and which also absorbs the parenthetical verification the source omits that the identifications give the same map. What is proved here is that the two steps suffice, which in the source is the word `hence`”.

> **Stacks 0FXZ.**  Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes which are
> quasi-compact and quasi-separated, let `X` and `Y` be Tor independent over `S`, and let
> `W = X ×_S Y` with its two projections `p` and `q`.  If `K ∈ D(𝒪_X)` is perfect,
> `K' ∈ D_{QCoh}(𝒪_X)`, `M ∈ D(𝒪_Y)` is perfect and `M' ∈ D_{QCoh}(𝒪_Y)`, then the Künneth
> morphism for Ext of Stacks 0FXY,
>
> `Ra_*R SheafHom(K, K') ⊗^𝐋_{𝒪_S} Rb_*R SheafHom(M, M') ⟶ Rf_*(R SheafHom(K ⊠ M, K' ⊠ M'))`,
>
> is an isomorphism.
>
> The two steps of the source's proof are carried as the hypotheses `hkunneth` and `hbox`, and
> the geometric hypotheses are therefore not consumed; the implementation notes of this file say
> what each of the two steps is, why neither is available in the library, and where the
> verification the source omits sits.  `hkunneth` is Stacks 0FLQ at the pair of derived internal
> homs and `hbox` is the identification of Cohomology, Stacks 08DQ together with that
> verification.

```lean
theorem isIso_kunnethExtMap_cartesian (hW : IsPullback p q a b)
    [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (_htor : AlgebraicGeometry.TorIndependent a b)
    (K K' : DerivedCategory X.Modules) (M M' : DerivedCategory Y.Modules)
    (_hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (_hK' : IsDQCoh (R := X.ringCatSheaf) K')
    (_hM : RingedSpace.IsPerfect (X := Y.toRingedSpace) M)
    (_hM' : IsDQCoh (R := Y.ringCatSheaf) M')
    (hkunneth : IsIso (Stacks.Cohomology.DerivedKunneth.kunnethMap a.toLRSHom.toShHom
      b.toLRSHom.toShHom p.toLRSHom.toShHom q.toLRSHom.toShHom (p ≫ a).toLRSHom.toShHom rfl
      (toShHom_isPullback_w a b p q hW)
      (sheafHomObj X.toRingedSpace K K') (sheafHomObj Y.toRingedSpace M M')))
    (hbox : IsIso (boxSheafHomMap p.toLRSHom.toShHom q.toLRSHom.toShHom K K' M M')) :
    IsIso (kunnethExtMap a.toLRSHom.toShHom b.toLRSHom.toShHom p.toLRSHom.toShHom
      q.toLRSHom.toShHom (p ≫ a).toLRSHom.toShHom rfl (toShHom_isPullback_w a b p q hW)
      K K' M M')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.25, Tag 0FXX](https://stacks.math.columbia.edu/tag/0FXX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
