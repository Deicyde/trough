---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_isPerfect, AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_hasFiniteTorDimension, AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_isFlat
statement: formalized
proof: formalized
---

# 86.5 Right adjoint of pushforward and base change, II

Section 86.5 of the Stacks Project, [Tag 0E5H](https://stacks.math.columbia.edu/tag/0E5H). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E5I, a lemma

[Tag 0E5I](https://stacks.math.columbia.edu/tag/0E5I) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffinePerfect.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffinePerfect.lean#L53). The attribute's comment: “(2)”.

> **Stacks 0E5I (2).** For a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> Y' --g---> Y
> ```
> with `Y`, `Y'` affine, `Y` Noetherian, `f` proper and perfect, and `X`, `Y'` Tor independent over
> `Y`, the base change map `L(g')^* a(K) ⟶ a'(Lg^*K)` of Stacks 0E5D is an isomorphism for every
> `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_isPerfect
    {X Y X' Y' : AlgebraicSpaces B S hS} {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'} {g' : X' ⟶ X}
    (sq : IsPullback g' f' f g) (hf : IsProper B S hS f.hom) (hfp : IsPerfect B S hS f.hom)
    (hY : IsAffineSpace B S hS Y.1) (hYN : IsNoetherian B S hS hZ Y.1)
    (hY' : IsAffineSpace B S hS Y'.1) (hTor : TorIndependent X.2 Y'.2 Y.2 f.hom g.hom)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    IsIso ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sq
      (isQuasiCompactSpace_of_isQuasiCompact_hom_of_isAffineSpace B S hS f hf.2.1.2 hY)
      (isAbsolutelyQuasiSeparated_of_isQuasiSeparated_hom_of_isAffineSpace B S hS hZ f
        (isQuasiSeparated_of_isSeparated B S hS hf.1) hY)
      (isAbsolutelyQuasiSeparated_of_isAffineSpace B S hS hZ hY) hY'.isQuasiCompactSpace
      (isAbsolutelyQuasiSeparated_of_isAffineSpace B S hS hZ hY') hTor).app K)
```

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_hasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffineTorDimension.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffineTorDimension.lean#L68). The attribute's comment: “(3)”.

> **Stacks 0E5I (3).** Let `g : U' ⟶ U` be a morphism of affine schemes of finite Tor dimension,
> with `U` Noetherian, and consider a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> U' --g---> U
> ```
> with `f` proper and `X`, `U'` Tor independent over `U`. Then the base change map
> `L(g')^* a(K) ⟶ a'(Lg^*K)` of Stacks 0E5D is an isomorphism for every `K ∈ D^+_QCoh(𝒪_U)`.

```lean
theorem isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_hasFiniteTorDimension
    {U' U : BigFppfOver B S hS} [IsAffine ((BigFppfOver.toScheme B S hS).obj U)]
    [IsAffine ((BigFppfOver.toScheme B S hS).obj U')] (g₀ : U' ⟶ U)
    {X X' : AlgebraicSpaces B S hS} {f : X ⟶ ⟨yoneda.obj U, isAlgebraicSpace_yoneda B S hS U⟩}
    {f' : X' ⟶ ⟨yoneda.obj U', isAlgebraicSpace_yoneda B S hS U'⟩} {g' : X' ⟶ X}
    (sq : IsPullback g' f' f (representedSpaceMap B S hS g₀)) (hf : IsProper B S hS f.hom)
    (hY : IsNoetherian B S hS hZ (yoneda.obj U))
    (hTor : TorIndependent X.2 (isAlgebraicSpace_yoneda B S hS U')
      (isAlgebraicSpace_yoneda B S hS U) f.hom (representedSpaceMap B S hS g₀).hom)
    (hg : AlgebraicGeometry.Space.HasFiniteTorDimension (representedSpaceMap B S hS g₀))
    (K : QuasicoherentDerivedCategory.{u, u} B S hS (yoneda.obj U)
      (isAlgebraicSpace_yoneda B S hS U))
    (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    IsIso ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sq
      (isQuasiCompactSpace_of_isQuasiCompact_hom_of_isAffineSpace B S hS f hf.2.1.2
        (isAffineSpace_yoneda B S hS U inferInstance))
      (isAbsolutelyQuasiSeparated_of_isQuasiSeparated_hom_of_isAffineSpace B S hS hZ f
        (isQuasiSeparated_of_isSeparated B S hS hf.1) (isAffineSpace_yoneda B S hS U inferInstance))
      (isAbsolutelyQuasiSeparated_of_isAffineSpace B S hS hZ
        (isAffineSpace_yoneda B S hS U inferInstance))
      (isAffineSpace_yoneda B S hS U' inferInstance).isQuasiCompactSpace
      (isAbsolutelyQuasiSeparated_of_isAffineSpace B S hS hZ
        (isAffineSpace_yoneda B S hS U' inferInstance)) hTor).app K)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChangeMap_app_of_isFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffineIso.lean#L265), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffineTags.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChangeAffineTags.lean#L22) (StacksFrontier): “(1)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.5, Tag 0E5H](https://stacks.math.columbia.edu/tag/0E5H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
