---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.TopDegreeBaseChange.affineTopDegreeTensorBaseChangeIso, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isIso_topDirectImageBaseChangeMap, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_rightDerivedPlus_pushforward_baseChange, Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorCohomologyIso, Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorCohomologyLinearEquiv, Stacks.AlgebraicGeometry.TopDegreeBaseChange.isIso_higherDirectImageTensorMap, Stacks.AlgebraicGeometry.TopDegreeBaseChange.topDirectImageTensorComparison, Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorSheafIso
statement: formalized
proof: formalized
---

# 32.19 Base change in top degree

Section 32.19 of the Stacks Project, [Tag 0EX2](https://stacks.math.columbia.edu/tag/0EX2). 4 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EX3, a lemma

[Tag 0EX3](https://stacks.math.columbia.edu/tag/0EX3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.affineTopDegreeTensorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/AffineBaseChangeQuasicoherent.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/AffineBaseChangeQuasicoherent.lean#L203). The attribute's comment: “(c) for an affine base change over an affine base, at an arbitrary quasi-coherent module; the comparison is proved linear over the base ring and not over the base-changed ring, and no canonical base-change map is constructed”.

> **Conclusion (c) of [Stacks, Tag 0EX3] for an affine base change over an affine base, at an
> arbitrary quasi-coherent module**: `Hᵈ(X, F) ⊗_R B ≅ Hᵈ(X_B, q^* F)`.
>
> Over an affine base the source obtains (c) from (b), and over an affine base (b) is the
> Eilenberg-Watts identity `affineTopDegreeTensorCohomologyIso`: `M ↦ Hᵈ(X, F ⊗ p^* M~)` is
> tensoring with `Hᵈ(X, F)`. Reading it at `M = B` and composing with
> `affineTopDegreeFunctorObjBaseRingIso` gives the displayed identification, with no base-change
> morphism constructed and no invertibility to prove.

```lean
def affineTopDegreeTensorBaseChangeIso
    (F : (_root_.SheafOfModules.isQuasicoherent W.left.ringCatSheaf).FullSubcategory)
    (hvan : ∀ G : W.left.Modules, G.IsQuasicoherent →
      IsZero (((moduleGlobalSections W.left).rightDerivedPlus ((d : ℤ) + 1)).obj G))
    {B : CommRingCat.{u}} (φ : CommRingCat.of R ⟶ B) {ZB : Scheme.{u}}
    (q : ZB ⟶ W.left) (pB : ZB ⟶ Spec B)
    (sq : IsPullback pB q (Spec.map φ) W.hom) :
    (MonoidalCategory.tensorLeft
        ((ModuleCat.restrictScalars (algebraMap R Γ(W.left, ⊤))).obj
          ((qcohCohomology W.left d).obj F))).obj
        ((ModuleCat.restrictScalars φ.hom).obj (ModuleCat.of B B)) ≅
      (ModuleCat.restrictScalars (algebraMap R Γ(W.left, ⊤))).obj
        ((ModuleCat.restrictScalars q.appTop.hom).obj
          (((moduleGlobalSections ZB).rightDerived d).obj
            ((Scheme.Modules.pullback q).obj (show W.left.Modules from F.obj))))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isIso_topDirectImageBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/BaseChangeTopDegreeConclusion.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/BaseChangeTopDegreeConclusion.lean#L68). The attribute's comment: “(c)”.

> **Conclusion (c) of [Stacks, Tag 0EX3]: formation of `R^d f'_* 𝓕'` commutes with arbitrary
> further base change.** For a top-degree base-change situation `S` (a morphism `f : X ⟶ Y` of
> quasi-compact quasi-separated schemes whose higher direct images of quasi-coherent modules vanish
> above `d`, and a base change `f' : X' ⟶ Y'` of it), every further cartesian square
> `X'' --h'--> X'`, `X'' --f''--> Y''`, `Y'' --h--> Y'` and every quasi-coherent `𝒪_{X'}`-module
> `𝓕'`, the canonical map `γ : h^* R^d f'_* 𝓕' ⟶ R^d f''_* (h')^* 𝓕'` is an isomorphism.

```lean
theorem isIso_topDirectImageBaseChangeMap
    (S : Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.{u})
    (F' : S.X'.Modules) [F'.IsQuasicoherent]
    (h' : X'' ⟶ S.X') (f'' : X'' ⟶ Y'') (h : Y'' ⟶ S.Y') (sq : IsPullback h' f'' S.f' h) :
    IsIso (topDirectImageBaseChangeMap S F' h' f'' h (toShHom_comm_of_isPullback h' f'' h sq))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_rightDerivedPlus_pushforward_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/BaseChangeVanishing.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/BaseChangeVanishing.lean#L202). The attribute's comment: “(a)”.

> **Conclusion (a) of [Stacks, Tag 0EX3].** In a top-degree base-change situation the higher
> direct images along the base-changed morphism `f'` of a quasi-coherent module vanish above the
> degree `d`.
>
> `isZero_rightDerivedPlus_pushforward_of_affineCase` reduces this to the case of a cartesian
> square whose two bases are affine, which it carried as the hypothesis `haffine`; that case is
> `isZero_rightDerivedPlus_pushforward_baseChange_of_isAffine`, so the conclusion is now
> unconditional.
>
> The degree `d` of a situation is a natural number, so `d < j` makes `j` nonnegative and the
> integer-to-natural crossing the affine case asks for is available.

```lean
theorem isZero_rightDerivedPlus_pushforward_baseChange
    (S : Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.{u})
    (i : ℤ) (hi : (S.d : ℤ) < i) (F' : S.X'.Modules) [F'.IsQuasicoherent] :
    IsZero (((Scheme.Modules.pushforward S.f').rightDerivedPlus i).obj F')
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/EilenbergWattsUnitor.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/EilenbergWattsUnitor.lean#L269). The attribute's comment: “(b) over an affine base, as an isomorphism of functors”.

> **The affine case of [Stacks, Tag 0EX3] (b) in the source's own form.** For a top-degree
> base-change situation whose base `Y'` is affine and a quasi-coherent module `F` on `X'`, the
> endofunctor `M ↦ H^d(X', F ⊗ (f')^* M~)` of `Γ(Y', ⊤)`-modules **is** tensoring with
> `H^d(X', F)`.
>
> This strengthens `topDegreeTensorIso`, which names the module only as `Φ(Γ(Y', ⊤))`; the two are
> interchanged by `topDegreeFunctorObjSelfIso`.

```lean
def topDegreeTensorCohomologyIso :
    MonoidalCategory.tensorLeft (S.topDegreeCohomology F) ≅ S.topDegreeFunctor F
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorCohomologyLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/EilenbergWattsUnitor.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/EilenbergWattsUnitor.lean#L279). The attribute's comment: “(b) over an affine base, the displayed tensor identity”.

> **The affine case of [Stacks, Tag 0EX3] (b), module by module, in the source's own form**: a
> `Γ(Y', ⊤)`-linear equivalence `H^d(X', F) ⊗_{R'} M ≃ₗ H^d(X', F ⊗ (f')^* M~)`, natural in `M` by
> `topDegreeTensorCohomologyIso`. This is the displayed equation of the source.

```lean
def topDegreeTensorCohomologyLinearEquiv (M : ModuleCat.{u} S.affineBaseRing) :
    (S.topDegreeCohomology F) ⊗[S.affineBaseRing] M ≃ₗ[S.affineBaseRing]
      (S.topDegreeFunctor F).obj M
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isIso_higherDirectImageTensorMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TensorComparisonBase.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TensorComparisonBase.lean#L267). The attribute's comment: “(b)”.

> **Conclusion (b) of [Stacks, Tag 0EX3].**  For a top-degree base-change situation, a
> quasi-coherent module `F'` on `X'` and a quasi-coherent module `G` on the base `Y'`, the
> canonical map
>
> `R^d f'_* F' ⊗_{𝒪_{Y'}} G ⟶ R^d f'_*(F' ⊗_{𝒪_{X'}} (f')^* G)`
>
> is an isomorphism.  The base carries no hypothesis: invertibility is local on it, the affine
> opens cover it, and over an affine open the Eilenberg-Watts argument of
> `TensorComparisonAffineRigidity.lean` applies to the restricted canonical map.

```lean
theorem isIso_higherDirectImageTensorMap (G : S.Y'.Modules) [G.IsQuasicoherent] :
    IsIso (higherDirectImageTensorMap S.f' F' G S.d)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.topDirectImageTensorComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TensorComparisonBase.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TensorComparisonBase.lean#L285). The attribute's comment: “(b)”.

> **Conclusion (b) of [Stacks, Tag 0EX3], as the isomorphism the tag asserts.**  For a
> top-degree base-change situation and quasi-coherent modules `F'` on `X'` and `G` on the base,
>
> `R^d f'_*(F' ⊗_{𝒪_{X'}} (f')^* G) ≅ R^d f'_* F' ⊗_{𝒪_{Y'}} G`,
>
> whose inverse satisfies the canonicity condition
> `Stacks.AlgebraicGeometry.TopDegreeBaseChange.IsHigherDirectImageTensorMap` of the tag, so by
> `eq_of_isHigherDirectImageTensorMap` it is the only candidate.

```lean
def topDirectImageTensorComparison (G : S.Y'.Modules) [G.IsQuasicoherent] :
    { e : ((Scheme.Modules.pushforward S.f').rightDerivedPlus (S.d : ℤ)).obj
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨S.X'.toRingedSpace.presheaf, S.X'.toRingedSpace.IsSheaf⟩).obj F').obj
              ((Scheme.Modules.pullback S.f').obj G))) ≅
      (((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨S.Y'.toRingedSpace.presheaf, S.Y'.toRingedSpace.IsSheaf⟩).obj
            (((Scheme.Modules.pushforward S.f').rightDerivedPlus (S.d : ℤ)).obj F')).obj G) //
      IsHigherDirectImageTensorMap S.f' F' G S.d e.inv }
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.topDegreeTensorSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TopDegreeTensorProjection.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/TopDegreeTensorProjection.lean#L402). The attribute's comment: “(b)”.

> **Conclusion (b) of [Stacks, Tag 0EX3].** In a top-degree base-change situation, for `F'`
> quasi-coherent on `X'` and `G'` quasi-coherent on `Y'`,
>
> `Rᵈ f'_*(F' ⊗_{𝒪_{X'}} (f')^* G') ≅ Rᵈ f'_* F' ⊗_{𝒪_{Y'}} G'`.
>
> No hypothesis is placed on `Y'`: the base-changed morphism `f'` is quasi-compact and
> quasi-separated (`quasiCompact_f'`, `quasiSeparated_f'`) and its higher direct images vanish
> above `d` by conclusion (a), `isZero_rightDerivedPlus_pushforward_baseChange`, so this is
> `Stacks.AlgebraicGeometry.TopDegreeBaseChange.topDegreeTensorIso` for `f'`. Over an affine `Y'`
> the same conclusion is read on global sections by `TopDegreeBaseChangeSituation.topDegreeTensorIso`
> (`EilenbergWattsSituation.lean`).

```lean
def topDegreeTensorSheafIso
    (F' : SheafOfModules.{u} (structureSheafRing S.X'.toRingedSpace)) [F'.IsQuasicoherent]
    (G' : SheafOfModules.{u} (structureSheafRing S.Y'.toRingedSpace)) [G'.IsQuasicoherent] :
    (homologyFunctor (SheafOfModules.{u} (structureSheafRing S.Y'.toRingedSpace)) (S.d : ℤ)).obj
        ((derivedPushforward S.f'.toLRSHom.toShHom).obj
          ((singleFunctor (SheafOfModules.{u} (structureSheafRing S.X'.toRingedSpace)) 0).obj
            (((Stacks.SheafOfModules.Tensor.sheafTensor S.X'.toRingedSpace.sheaf).obj F').obj
              ((RingedSpaceModuleAdjunction.modulePullback S.f'.toLRSHom.toShHom).obj G')))) ≅
      ((Stacks.SheafOfModules.Tensor.sheafTensor S.Y'.toRingedSpace.sheaf).obj
        ((homologyFunctor (SheafOfModules.{u} (structureSheafRing S.Y'.toRingedSpace))
            (S.d : ℤ)).obj
          ((derivedPushforward S.f'.toLRSHom.toShHom).obj
            ((singleFunctor (SheafOfModules.{u} (structureSheafRing S.X'.toRingedSpace)) 0).obj
              F')))).obj
        G'
```

## Tag 0E7D, a lemma

[Tag 0E7D](https://stacks.math.columbia.edu/tag/0E7D) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_stalk_rightDerivedPlus_of_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionStalkVanishing.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionStalkVanishing.lean#L65). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0E7D] part (1).** For `f : X ⟶ Y` proper, `y ∈ Y` whose fibre has topological
> Krull dimension at most `d`, and `F` quasi-coherent, the stalk at `y` of `Rⁱ f_* F` vanishes for
> every `i > d`.
>
> This is `isZero_stalk_rightDerivedPlus_of_cohomology_vanishing` with its hypothesis supplied by
> `cohomology_vanishing_of_forall_topologicalKrullDim_fiber_le`.

```lean
theorem isZero_stalk_rightDerivedPlus_of_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y) (d : ℕ)
    (hdim : topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞))
    (F : X.Modules) [F.IsQuasicoherent] (i : ℤ) (hi : (d : ℤ) < i) :
    IsZero ((((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F).presheaf.stalk y)
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isAffineOpen_topDegreeBaseChange_of_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionStalkVanishing.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionStalkVanishing.lean#L86). The attribute's comment: “part (2): the hypotheses of Tag 0EX3 and its conclusions (a) and (b)”.

> **[Stacks, Tag 0E7D] part (2).** For `f : X ⟶ Y` proper and `y ∈ Y` whose fibre has
> topological Krull dimension at most `d`, the point `y` has an affine open neighbourhood `V` such
> that `f ∣_ V : f ⁻¹ V ⟶ V` and `d` satisfy
>
> * the hypotheses of [Stacks, Tag 0EX3]: `f ⁻¹ V` and `V` are quasi-compact and
>   quasi-separated, and `Rⁱ (f ∣_ V)_* F = 0` for `i > d` and every quasi-coherent `F`;
> * conclusion (a) of [Stacks, Tag 0EX3]: for every cartesian square
>   `X' ⟶ f ⁻¹ V`, `f' : X' ⟶ Y'`, `Y' ⟶ V`, `Rⁱ f'_* F' = 0` for `i > d` and every
>   quasi-coherent `F'` on `X'`;
> * conclusion (b) of [Stacks, Tag 0EX3]: for every such square and quasi-coherent `F'` on `X'`
>   and `G'` on `Y'`, `Rᵈ f'_*(F' ⊗ (f')^* G') ≅ Rᵈ f'_* F' ⊗ G'`, with `Rᵈ f'_*` read as the
>   degree-`d` cohomology of the derived direct image of a module placed in degree `0`.

```lean
theorem exists_isAffineOpen_topDegreeBaseChange_of_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y) (d : ℕ)
    (hdim : topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞)) :
    ∃ V : Y.Opens,
      y ∈ V ∧ IsAffineOpen V ∧
      CompactSpace (f ⁻¹ᵁ V).toScheme ∧
      QuasiSeparatedSpace (f ⁻¹ᵁ V).toScheme ∧
      CompactSpace V.toScheme ∧ QuasiSeparatedSpace V.toScheme ∧
      (∀ (i : ℤ), (d : ℤ) < i →
        ∀ (F : (f ⁻¹ᵁ V).toScheme.Modules), F.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward (f ∣_ V)).rightDerivedPlus i).obj F)) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (i : ℤ), (d : ℤ) < i → ∀ (F' : X'.Modules), F'.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward f').rightDerivedPlus i).obj F')) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (F' : SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)), F'.IsQuasicoherent →
        ∀ (G' : SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)), G'.IsQuasicoherent →
          Nonempty ((DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
              ((derivedPushforward f'.toLRSHom.toShHom).obj
                ((DerivedCategory.singleFunctor
                  (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj
                  (((Stacks.SheafOfModules.Tensor.sheafTensor X'.toRingedSpace.sheaf).obj F').obj
                    ((RingedSpaceModuleAdjunction.modulePullback f'.toLRSHom.toShHom).obj
                      G')))) ≅
            ((Stacks.SheafOfModules.Tensor.sheafTensor Y'.toRingedSpace.sheaf).obj
              ((DerivedCategory.homologyFunctor
                (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
                ((derivedPushforward f'.toLRSHom.toShHom).obj
                  ((DerivedCategory.singleFunctor
                    (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj F')))).obj
              G'))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isAffineOpen_topDegreeBaseChangeConclusions_of_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionTopDegreeConclusions.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionTopDegreeConclusions.lean#L85). The attribute's comment: “part (2), with all conclusions of Tag 0EX3”.

> **[Stacks, Tag 0E7D] part (2), with every conclusion of Tag 0EX3.** For `f : X ⟶ Y` proper
> and `y ∈ Y` whose fibre has topological Krull dimension at most `d`, the point `y` has an affine
> open neighbourhood `V` such that `f ∣_ V : f ⁻¹ V ⟶ V` and `d` satisfy the hypotheses of
> [Stacks, Tag 0EX3] (`f ⁻¹ V` and `V` quasi-compact and quasi-separated, `Rⁱ (f ∣_ V)_* F = 0` for
> `i > d` and quasi-coherent `F`) and, for every cartesian square `X' ⟶ f ⁻¹ V`, `f' : X' ⟶ Y'`,
> `Y' ⟶ V`, its conclusions:
>
> * (a) `Rⁱ f'_* F' = 0` for `i > d` and every quasi-coherent `F'` on `X'`;
> * (b) `Rᵈ f'_*(F' ⊗ (f')^* G') ≅ Rᵈ f'_* F' ⊗ G'` for quasi-coherent `F'` on `X'` and `G'` on
>   `Y'`;
> * (c) for every further cartesian square `X'' ⟶ X'`, `f'' : X'' ⟶ Y''`, `h : Y'' ⟶ Y'` and every
>   quasi-coherent `F'` on `X'`, the canonical map `h^* Rᵈ f'_* F' ⟶ Rᵈ f''_* (h')^* F'` is an
>   isomorphism.

```lean
theorem exists_isAffineOpen_topDegreeBaseChangeConclusions_of_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y) (d : ℕ)
    (hdim : topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞)) :
    letI : ∀ (C : Type (u + 1)) [Category.{u} C] [Abelian C], HasDerivedCategory.{u + 1} C :=
      fun C _ _ => HasDerivedCategory.standard C
    ∃ (V : Y.Opens) (_ : y ∈ V) (_ : IsAffineOpen V)
      (hcX : CompactSpace (f ⁻¹ᵁ V).toScheme) (hqX : QuasiSeparatedSpace (f ⁻¹ᵁ V).toScheme)
      (hcY : CompactSpace V.toScheme) (hqY : QuasiSeparatedSpace V.toScheme)
      (hvan : ∀ (i : ℤ), (d : ℤ) < i →
        ∀ (F : (f ⁻¹ᵁ V).toScheme.Modules), F.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward (f ∣_ V)).rightDerivedPlus i).obj F)),
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (i : ℤ), (d : ℤ) < i → ∀ (F' : X'.Modules), F'.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward f').rightDerivedPlus i).obj F')) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (F' : SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)), F'.IsQuasicoherent →
        ∀ (G' : SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)), G'.IsQuasicoherent →
          Nonempty ((DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
              ((derivedPushforward f'.toLRSHom.toShHom).obj
                ((DerivedCategory.singleFunctor
                  (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj
                  (((Stacks.SheafOfModules.Tensor.sheafTensor X'.toRingedSpace.sheaf).obj F').obj
                    ((RingedSpaceModuleAdjunction.modulePullback f'.toLRSHom.toShHom).obj
                      G')))) ≅
            ((Stacks.SheafOfModules.Tensor.sheafTensor Y'.toRingedSpace.sheaf).obj
              ((DerivedCategory.homologyFunctor
                (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
                ((derivedPushforward f'.toLRSHom.toShHom).obj
                  ((DerivedCategory.singleFunctor
                    (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj F')))).obj
              G')) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme) (sq : IsPullback g' f' (f ∣_ V) g),
        let S : Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.{u} :=
          { X := (f ⁻¹ᵁ V).toScheme, Y := V.toScheme, f := f ∣_ V, d := d
            isCompact_X := hcX, isQuasiSeparated_X := hqX
            isCompact_Y := hcY, isQuasiSeparated_Y := hqY
            vanishes_above := hvan
            X' := X', Y' := Y', g' := g', f' := f', g := g, isPullback := sq }
        ∀ (F' : X'.Modules) [F'.IsQuasicoherent]
          {X'' Y'' : Scheme.{u}} (h' : X'' ⟶ X') (f'' : X'' ⟶ Y'') (h : Y'' ⟶ Y')
          (sq' : IsPullback h' f'' f' h),
        IsIso (topDirectImageBaseChangeMap S F' h' f'' h
          (toShHom_comm_of_isPullback (S := S) h' f'' h sq')))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.stalkVanishing_and_topDegreeBaseChange_of_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionTopDegreeConclusions.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/FibreDimensionTopDegreeConclusions.lean#L144).

> **[Stacks, Tag 0E7D].** For `f : X ⟶ Y` proper and `y ∈ Y` whose fibre has topological
> Krull dimension at most `d`: (1) the stalk at `y` of `Rⁱ f_* F` vanishes for every `i > d` and
> every quasi-coherent `F`; (2) `y` has an affine open neighbourhood `V` such that `f ∣_ V` and `d`
> satisfy the hypotheses and all three conclusions of [Stacks, Tag 0EX3], as in
> `exists_isAffineOpen_topDegreeBaseChangeConclusions_of_topologicalKrullDim_fiber_le`.

```lean
theorem stalkVanishing_and_topDegreeBaseChange_of_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y) (d : ℕ)
    (hdim : topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞)) :
    letI : ∀ (C : Type (u + 1)) [Category.{u} C] [Abelian C], HasDerivedCategory.{u + 1} C :=
      fun C _ _ => HasDerivedCategory.standard C
    (∀ (F : X.Modules), F.IsQuasicoherent → ∀ (i : ℤ), (d : ℤ) < i →
      IsZero ((((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F).presheaf.stalk y)) ∧
    ∃ (V : Y.Opens) (_ : y ∈ V) (_ : IsAffineOpen V)
      (hcX : CompactSpace (f ⁻¹ᵁ V).toScheme) (hqX : QuasiSeparatedSpace (f ⁻¹ᵁ V).toScheme)
      (hcY : CompactSpace V.toScheme) (hqY : QuasiSeparatedSpace V.toScheme)
      (hvan : ∀ (i : ℤ), (d : ℤ) < i →
        ∀ (F : (f ⁻¹ᵁ V).toScheme.Modules), F.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward (f ∣_ V)).rightDerivedPlus i).obj F)),
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (i : ℤ), (d : ℤ) < i → ∀ (F' : X'.Modules), F'.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward f').rightDerivedPlus i).obj F')) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme), IsPullback g' f' (f ∣_ V) g →
        ∀ (F' : SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)), F'.IsQuasicoherent →
        ∀ (G' : SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)), G'.IsQuasicoherent →
          Nonempty ((DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
              ((derivedPushforward f'.toLRSHom.toShHom).obj
                ((DerivedCategory.singleFunctor
                  (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj
                  (((Stacks.SheafOfModules.Tensor.sheafTensor X'.toRingedSpace.sheaf).obj F').obj
                    ((RingedSpaceModuleAdjunction.modulePullback f'.toLRSHom.toShHom).obj
                      G')))) ≅
            ((Stacks.SheafOfModules.Tensor.sheafTensor Y'.toRingedSpace.sheaf).obj
              ((DerivedCategory.homologyFunctor
                (SheafOfModules.{u} (structureSheafRing Y'.toRingedSpace)) (d : ℤ)).obj
                ((derivedPushforward f'.toLRSHom.toShHom).obj
                  ((DerivedCategory.singleFunctor
                    (SheafOfModules.{u} (structureSheafRing X'.toRingedSpace)) 0).obj F')))).obj
              G')) ∧
      (∀ {X' Y' : Scheme.{u}} (g' : X' ⟶ (f ⁻¹ᵁ V).toScheme) (f' : X' ⟶ Y')
          (g : Y' ⟶ V.toScheme) (sq : IsPullback g' f' (f ∣_ V) g),
        let S : Stacks.AlgebraicGeometry.TopDegreeBaseChangeSituation.{u} :=
          { X := (f ⁻¹ᵁ V).toScheme, Y := V.toScheme, f := f ∣_ V, d := d
            isCompact_X := hcX, isQuasiSeparated_X := hqX
            isCompact_Y := hcY, isQuasiSeparated_Y := hqY
            vanishes_above := hvan
            X' := X', Y' := Y', g' := g', f' := f', g := g, isPullback := sq }
        ∀ (F' : X'.Modules) [F'.IsQuasicoherent]
          {X'' Y'' : Scheme.{u}} (h' : X'' ⟶ X') (f'' : X'' ⟶ Y'') (h : Y'' ⟶ Y')
          (sq' : IsPullback h' f'' f' h),
        IsIso (topDirectImageBaseChangeMap S F' h' f'' h
          (toShHom_comm_of_isPullback (S := S) h' f'' h sq')))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.exists_isAffineOpen_vanishing_of_fiber_dimension_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ZeroDimensionalFibres.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ZeroDimensionalFibres.lean#L138). The attribute's comment: “part (2) for fibre dimension at most `0`, with no further hypothesis”.

> **[Stacks, Tag 0E7D] part (2) for a proper morphism with zero-dimensional fibres**, with
> no hypothesis beyond the tag's own. The point `y` has an affine open neighbourhood `V` such
> that `f ∣_ V` and `0` satisfy the hypotheses of [Stacks, Tag 0EX3] — the two finiteness
> conditions and the vanishing of the higher direct images above the degree — whose
> conclusions are then available unconditionally from
> `StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/SituationBaseChange.lean`.
>
> This is `exists_isAffineOpen_vanishing_of_cohomology_vanishing` at `d = 0`, with its
> hypothesis `hcoh` discharged by
> `cohomology_vanishing_of_forall_topologicalKrullDim_fiber_le_zero`.
>
> The part string records that the fibre bound is `0`, not an arbitrary `d`.

```lean
theorem exists_isAffineOpen_vanishing_of_fiber_dimension_le_zero
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((0 : ℕ) : WithBot ℕ∞)) :
    ∃ V : Y.Opens,
      y ∈ V ∧ IsAffineOpen V ∧
      CompactSpace (f ⁻¹ᵁ V).toScheme ∧
      QuasiSeparatedSpace (f ⁻¹ᵁ V).toScheme ∧
      CompactSpace V.toScheme ∧ QuasiSeparatedSpace V.toScheme ∧
      (∀ (i : ℤ), ((0 : ℕ) : ℤ) < i →
        ∀ (F : (f ⁻¹ᵁ V).toScheme.Modules), F.IsQuasicoherent →
          IsZero (((Scheme.Modules.pushforward (f ∣_ V)).rightDerivedPlus i).obj F))
```

**`Stacks.AlgebraicGeometry.TopDegreeBaseChange.isZero_stalk_rightDerivedPlus_of_fiber_dimension_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ZeroDimensionalFibres.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/ZeroDimensionalFibres.lean#L162). The attribute's comment: “part (1) for fibre dimension at most `0`, with no further hypothesis”.

> **[Stacks, Tag 0E7D] part (1) for a proper morphism with zero-dimensional fibres**, with
> no hypothesis beyond the tag's own: the stalk at `y` of `Rⁱ f_* F` vanishes in every
> positive degree, for every quasi-coherent `F`.
>
> This is `isZero_stalk_rightDerivedPlus_of_cohomology_vanishing` at `d = 0`, with its
> hypothesis `hcoh` discharged by
> `cohomology_vanishing_of_forall_topologicalKrullDim_fiber_le_zero`.
>
> The part string records that the fibre bound is `0`, not an arbitrary `d`.

```lean
theorem isZero_stalk_rightDerivedPlus_of_fiber_dimension_le_zero
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y)
    (hdim : topologicalKrullDim (f.fiber y) ≤ ((0 : ℕ) : WithBot ℕ∞))
    (F : X.Modules) [F.IsQuasicoherent] (i : ℤ) (hi : 0 < i) :
    IsZero ((((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F).presheaf.stalk y)
```

## Tag 0EX4, a lemma

[Tag 0EX4](https://stacks.math.columbia.edu/tag/0EX4) in the Stacks Project.

**`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.isQuasicoherent_rightDerived_of_isProper`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/Qcqs.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/Qcqs.lean#L505). The attribute's comment: “quasi-coherence”.

> **Stacks Project, Tag 0EX4 (quasi-coherence).** Higher direct images of a quasi-coherent
> module under a proper morphism are quasi-coherent: a proper morphism is quasi-compact and
> quasi-separated, and properness is used for nothing else.

```lean
instance isQuasicoherent_rightDerived_of_isProper {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    (F : X.Modules) [F.IsQuasicoherent] (i : ℕ) :
    (((Scheme.Modules.pushforward f).rightDerived i).obj F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.Tag0EX4ProperQcoh.isQuasicoherent_rightDerived_of_isProper`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperQcoh/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperQcoh/Basic.lean#L90). The attribute's comment: “quasi-coherence”.

> **Stacks Project, Tag 0EX4 (quasi-coherence).** Let `f : X ⟶ Y` be a proper morphism of
> schemes and let `F` be a quasi-coherent `𝒪_X`-module. Then the higher direct image `R ⁱ f_* F` is
> a quasi-coherent `𝒪_Y`-module, in every degree `i : ℕ`.
>
> A proper morphism is quasi-compact and quasi-separated, so this is `isQuasicoherent_rightDerived`;
> properness is not otherwise used, and neither is any bound on the degree or on the dimension of
> the fibres.

```lean
instance isQuasicoherent_rightDerived_of_isProper [IsProper f] [F.IsQuasicoherent] :
    (((Scheme.Modules.pushforward f).rightDerived i).obj F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.TopDegreeFiniteType.isFiniteType_rightDerived_of_isProper_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/NoetherianBaseUnconditional.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/NoetherianBaseUnconditional.lean#L72). The attribute's comment: “finite-type clause only, and only over a locally Noetherian base; there in every degree and with no hypothesis on the fibres. An arbitrary base is not covered.”.

> **The finite-type clause of [Stacks, Tag 0EX4] over a locally Noetherian base.** For
> `f : X ⟶ Y` proper with `Y` locally Noetherian and `F` quasi-coherent of finite type, the
> `𝒪_Y`-module `R ᵈ f_* F` is of finite type in every degree `d`, with no bound on the fibres
> of `f`.

```lean
theorem isFiniteType_rightDerived_of_isProper_of_isLocallyNoetherian {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsProper f] [IsLocallyNoetherian Y] (F : X.Modules) [F.IsQuasicoherent]
    [F.IsFiniteType] (d : ℕ) :
    (((Scheme.Modules.pushforward f).rightDerived d).obj F).IsFiniteType
```

**`Stacks.AlgebraicGeometry.TopDegreeFiniteType.isQuasicoherent_isFiniteType_rightDerived_of_isProper_of_forall_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/Unconditional.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/Unconditional.lean#L238). The attribute's comment: “both clauses at an ARBITRARY base, every d; the conclusion read as the 𝒪\_Y-module R ᵈ f\_* F, the source's 𝒪\_X being a typo”.

> **[Stacks, Tag 0EX4].** For `f : X ⟶ Y` proper all of whose fibres have dimension at most
> `d`, and `F` a quasi-coherent `𝒪_X`-module of finite type, the `𝒪_Y`-module `R ᵈ f_* F` is
> quasi-coherent of finite type. The base is arbitrary.
>
> The source prints the conclusion as an `𝒪_X`-module; `R ᵈ f_* F` is a sheaf on `Y`, and the
> `𝒪_Y`-reading is the one the source's own proof uses.
>
> Both clauses of the tag in one statement: quasi-coherence is
> `…ProperQcoh.isQuasicoherent_rightDerived_of_isProper`, found by instance search because a proper
> morphism is quasi-compact and quasi-separated, and finite type is
> `isFiniteType_rightDerived_of_isProper_of_forall_topologicalKrullDim_fiber_le`.

```lean
theorem isQuasicoherent_isFiniteType_rightDerived_of_isProper_of_forall_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (d : ℕ)
    (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞))
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    (((Scheme.Modules.pushforward f).rightDerived d).obj F).IsQuasicoherent ∧
      (((Scheme.Modules.pushforward f).rightDerived d).obj F).IsFiniteType
```

## Tag 0EX5, a lemma

[Tag 0EX5](https://stacks.math.columbia.edu/tag/0EX5) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TopDegreeFiniteType.isFinitePresentation_rightDerived_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/FinitePresentationModelDischarge.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeFiniteType/FinitePresentationModelDischarge.lean#L220). The attribute's comment: “conclusion read as the 𝒪\_Y-module R ᵈ f\_* F, the source's 𝒪\_X being a typo”. References: EGA III (2.4.1), “Clause (i), special case”.

> **[Stacks, Tag 0EX5].** Let `f : X ⟶ Y` be proper and of finite presentation with every
> fibre of dimension at most `d`, and let `F` be an `𝒪_X`-module of finite presentation. Then the
> `𝒪_Y`-module `R ᵈ f_* F` is of finite presentation.
>
> No hypothesis is carried: `Y` is an arbitrary scheme, in particular not assumed locally
> Noetherian, and nothing about Noetherian models or about base change is assumed.
>
> The proof is the source's, which is the proof of [Stacks, Tag 0EX4] with the third paragraph
> skipped, and it is now assembled from three pieces that are each unconditional:
>
> * the conclusion is local on `Y`, so `Y` may be taken affine, and over an affine base the
>   situation descends to an affine **Noetherian** stage together with the fibre bound and the
>   module, over which the higher direct images vanish above `d` — this is
>   `isFinitePresentation_rightDerived_of_topDegreeBaseChange` above;
> * over that stage the top higher direct image of the base change is of finite presentation —
>   `…AffineBaseChangeProjection.isFinitePresentation_rightDerived_pullback_of_noetherianModel`,
>   the Eilenberg–Watts argument of [Stacks, Tag 0EX3] (b) applied at `Γ(Y, ⊤)`.
>
> The conclusion is read as the statement about the `𝒪_Y`-module `R ᵈ f_* F`; the source prints
> `𝒪_X`, which is a typo, the higher direct image being a sheaf on `Y`.

```lean
theorem isFinitePresentation_rightDerived_of_finitePresentation
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (hfp : AlgebraicGeometry.FinitePresentation f)
    (d : ℕ) (hdim : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞))
    (F : X.Modules) [F.IsFinitePresentation] :
    (((Scheme.Modules.pushforward f).rightDerived d).obj F).IsFinitePresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.19, Tag 0EX2](https://stacks.math.columbia.edu/tag/0EX2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
