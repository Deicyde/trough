---
declaration: section
origin: cited
lean: AlgebraicGeometry.BaseChangeDiagram, AlgebraicGeometry.BaseChangeDiagram.pulledBack, AlgebraicGeometry.BaseChangeDiagram.derivedPushforward, AlgebraicGeometry.BaseChangeDiagram.derivedPushforward', Stacks.AlgebraicGeometry.AffineBaseChangeIso.isIso_baseChangeNatTrans_of_isAffineHom, Stacks.AlgebraicGeometry.AffinePushforward.pushforward_isQuasicoherent_of_isAffineHom, Stacks.Tag02KGDerivedComparison.isIso_rightDerivedFunctorPlusUnit_app_of_isAffineHom, Stacks.AlgebraicGeometry.FlatBaseChangeDerived.isIso_baseChangeMap_of_flat
statement: formalized
proof: formalized
---

# 30.5 Cohomology and base change, I

Section 30.5 of the Stacks Project, [Tag 02KE](https://stacks.math.columbia.edu/tag/02KE). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02KF, an equation

[Tag 02KF](https://stacks.math.columbia.edu/tag/02KF) in the Stacks Project.

**`AlgebraicGeometry.BaseChangeDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean#L54). The attribute's comment: “the cartesian square and quasi-coherent module”.

> **Stacks Project, Tag 02KF.** The base-change diagram: a cartesian square of schemes,
> together with the quasi-coherent module `𝓕` on `X`.

```lean
structure BaseChangeDiagram
```

**`AlgebraicGeometry.BaseChangeDiagram.pulledBack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean#L71). The attribute's comment: “the pulled-back module”.

> The module `𝓕' = (g')^*𝓕` in the base-change diagram.

```lean
noncomputable abbrev pulledBack (d : BaseChangeDiagram) : d.X'.Modules
```

**`AlgebraicGeometry.BaseChangeDiagram.derivedPushforward`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean#L76). The attribute's comment: “the lower-right derived direct image”.

> The total derived direct image `Rf_*𝓕` in the base-change diagram.

```lean
noncomputable abbrev derivedPushforward (d : BaseChangeDiagram) :
    DerivedCategory.Plus d.S.Modules
```

**`AlgebraicGeometry.BaseChangeDiagram.derivedPushforward'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/EulerChar/BaseChange.lean#L83). The attribute's comment: “the lower-left derived direct image”.

> The total derived direct image `Rf'_*𝓕'` in the base-change diagram.

```lean
noncomputable abbrev derivedPushforward' (d : BaseChangeDiagram) :
    DerivedCategory.Plus d.S'.Modules
```

## Tag 02KG, a lemma

[Tag 02KG](https://stacks.math.columbia.edu/tag/02KG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineBaseChangeIso.isIso_baseChangeNatTrans_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineBaseChangeIso/Reduction.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineBaseChangeIso/Reduction.lean#L176). The attribute's comment: “affine base change”.

> **The base-change assertion of Stacks Tag 02KG.**  The base-change morphism of a cartesian
> square of schemes whose right-hand morphism is affine is invertible at every quasi-coherent
> module.

```lean
theorem isIso_baseChangeNatTrans_of_isAffineHom (hw : IsPullback g' f' f g) [IsAffineHom f]
    (F : X.Modules) [F.IsQuasicoherent] :
    IsIso ((AffinePushforward.baseChangeNatTrans hw.w).app F)
```

**`Stacks.AlgebraicGeometry.AffinePushforward.pushforward_isQuasicoherent_of_isAffineHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffinePushforward/Basic.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffinePushforward/Basic.lean#L251). The attribute's comment: “quasi-coherence of the direct image”.

> **Stacks Project, Tag 02KG.** The direct image of a quasi-coherent module along an affine
> morphism is quasi-coherent.

```lean
instance pushforward_isQuasicoherent_of_isAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) [IsAffineHom f] [F.IsQuasicoherent] :
    ((Scheme.Modules.pushforward f).obj F).IsQuasicoherent
```

**`Stacks.Tag02KGDerivedComparison.isIso_rightDerivedFunctorPlusUnit_app_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedComparison/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedComparison/Basic.lean#L83). The attribute's comment: “comparison with the derived direct image”. References: EGA III (1.3.2).

> **[Stacks, Tag 02KG], comparison with the derived direct image.** For an affine morphism
> `f : X ⟶ S` of schemes and a quasi-coherent `𝒪_X`-module `F`, the canonical map from the ordinary
> direct image `f_* F`, placed in degree zero, to the total derived direct image `R f_*(F[0])` is an
> isomorphism. Equivalently: a quasi-coherent module has no higher direct images along an affine
> morphism, so the unit of `R f_*` is already invertible on degree-zero complexes.
>
> This is `Stacks.AffineHigherDirectImage.rightAcyclic_pushforward`, [Stacks, Tag 01XC], read at the
> unfolding of `CategoryTheory.Functor.rightAcyclic`.

```lean
theorem isIso_rightDerivedFunctorPlusUnit_app_of_isAffineHom
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) [IsAffineHom f] [F.IsQuasicoherent] :
    IsIso ((Scheme.Modules.pushforward f).rightDerivedFunctorPlusUnith.app
      ((HomotopyCategory.Plus.singleFunctor X.Modules 0).obj F))
```

## Tag 02KH, a lemma

[Tag 02KH](https://stacks.math.columbia.edu/tag/02KH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FlatBaseChangeDerived.isIso_baseChangeMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean#L76). The attribute's comment: “part (1): the base change map of Tag 02N7 is an isomorphism in D⁺(𝒪\_\{S'}), hence in every degree i”.

> **Flat base change in the derived category ([Stacks, Tag 02KH], part (1)).** For a cartesian
> square of schemes with `g` flat and `f` quasi-compact and quasi-separated, and a quasi-coherent
> `𝒪_X`-module `ℱ`, the base change map `g^* Rf_* ℱ ⟶ Rf'_* (g')^* ℱ` of [Stacks, Tag 02N7] is an
> isomorphism in `D⁺(𝒪_{S'})`. Taking cohomology sheaves, the base change maps
> `g^* R^i f_* ℱ ⟶ R^i f'_* (g')^* ℱ` are isomorphisms for every `i`
> (`isIso_higherBaseChangeMap`).

```lean
theorem isIso_baseChangeMap_of_flat (H : IsPullback g' f' f g) [Flat g] [QuasiCompact f]
    [QuasiSeparated f] (F : X.Modules) [F.IsQuasicoherent] :
    IsIso ((Stacks.Cohomology.FlatBaseChange.baseChangeMap f.toLRSHom.toShHom
      f'.toLRSHom.toShHom g.toLRSHom.toShHom g'.toLRSHom.toShHom
      (congrArg (fun h => h.toLRSHom.toShHom) H.w) (isFlat_toShHom g)
      (isFlat_toShHom_of_isPullback H)).app ((DerivedCategory.Plus.singleFunctor _ 0).obj F))
```

**`Stacks.AlgebraicGeometry.FlatBaseChangeDerived.isIso_higherBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean#L118). The attribute's comment: “part (1), in each degree i”.

> **[Stacks, Tag 02KH], part (1).** For a cartesian square of schemes with `g` flat and `f`
> quasi-compact and quasi-separated, and a quasi-coherent `𝒪_X`-module `ℱ`, the base change map
> `g^* R^i f_* ℱ ⟶ R^i f'_* (g')^* ℱ` is an isomorphism for every `i`.

```lean
theorem isIso_higherBaseChangeMap (H : IsPullback g' f' f g) [Flat g] [QuasiCompact f]
    [QuasiSeparated f] (F : X.Modules) [F.IsQuasicoherent] (i : ℤ) :
    IsIso (higherBaseChangeMap H F i)
```

**`Stacks.AlgebraicGeometry.FlatBaseChangeDerived.cohomologyBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/Derived/FlatBaseChange.lean#L169). The attribute's comment: “part (2)”.

> **[Stacks, Tag 02KH], part (2).** For a cartesian square of schemes with `S` and `S'`
> affine, `g` flat and `f` quasi-compact and quasi-separated, and a quasi-coherent `𝒪_X`-module
> `ℱ`,
>
> `H^i(X, ℱ) ⊗_{Γ(S, 𝒪_S)} Γ(S', 𝒪_{S'}) ≅ H^i(X', (g')^* ℱ)`
>
> as `Γ(S', 𝒪_{S'})`-modules, for every `i`. The isomorphism is the one given by the base change
> map of [Stacks, Tag 02N7]: it is the global sections over `S'` of the isomorphism
> `g^* R^i f_* ℱ ≅ R^i f'_* (g')^* ℱ` of part (1), read through the identifications
> `H^i(X, ℱ) = Γ(S, R^i f_* ℱ)` of [Stacks, Tag 01XK] (for `f` and for `f'`) and
> `Γ(S', g^* 𝒢) = Γ(S, 𝒢) ⊗_{Γ(S, 𝒪_S)} Γ(S', 𝒪_{S'})` for the quasi-coherent
> `𝒢 = R^i f_* ℱ` ([Stacks, Tag 01XJ]).

```lean
def cohomologyBaseChangeIso (H : IsPullback g' f' f g) [IsAffine S] [IsAffine S'] [Flat g]
    [QuasiCompact f] [QuasiSeparated f] (F : X.Modules) [F.IsQuasicoherent] (i : ℤ) :
    (ModuleCat.extendScalars g.appTop.hom).obj (cohomologyOver f F i) ≅
      cohomologyOver f' ((Scheme.Modules.pullback g').obj F) i
```

## Tag 0CKW, a lemma

[Tag 0CKW](https://stacks.math.columbia.edu/tag/0CKW) in the Stacks Project.

**`Stacks.Tag0CKW.isIso_cohomologyBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/FiniteLocallyFreeCanonical.lean, line 861](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/FiniteLocallyFreeCanonical.lean#L861).

> **Finite locally free base change.** For a cartesian square of schemes
>
> ```
> Y --p--> X
> |        |
> k        iX
> v        v
> T --q--> S
> ```
>
> with `S = Spec A` and `T = Spec B` affine and `q` finite locally free, and for every
> quasi-coherent `𝒪_X`-module `F` and every `n`, the canonical map
> `Hⁿ(X, F) ⊗_A B ⟶ Hⁿ(Y, p^* F)`, `x ⊗ b ↦ b • p^* x`, is an isomorphism of `B`-modules, for
> an arbitrary scheme `X`.
>
> The map is `cohomologyBaseChangeMap`, the `B`-linear extension of the pullback map
> `cohomologyPullback`.

```lean
theorem isIso_cohomologyBaseChangeMap [Stacks.Morphisms.IsFiniteLocallyFree q]
    (F : X.Modules) [F.IsQuasicoherent] (n : ℕ) :
    IsIso (cohomologyBaseChangeMap H F n)
```

**`Stacks.Tag0CKW.isIso_cohomologyBaseChangeMap_of_isFiniteLocallyFree_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/FiniteLocallyFreeCanonical.lean, line 883](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FlatBaseChangeCohomology/FiniteLocallyFreeCanonical.lean#L883). The attribute's comment: “as stated: B a finite locally free A-module”.

> **Finite locally free base change.** Let `φ : A ⟶ B` be a ring map making `B` a finite
> locally free `A`-module, and consider a cartesian square of schemes
>
> ```
> Y ------p-----> X
> |               |
> k               iX
> v               v
> Spec B --> Spec A
> ```
>
> with bottom arrow `Spec φ`. For every quasi-coherent `𝒪_X`-module `F` and every `n`, the canonical
> map `Hⁿ(X, F) ⊗_A B ⟶ Hⁿ(Y, p^* F)`, `x ⊗ b ↦ b • p^* x`, is an isomorphism of `B`-modules; here
> `A` and `B` act through `Γ(Spec A, 𝒪)` and `Γ(Spec B, 𝒪)`, and `X` is an arbitrary scheme.

```lean
theorem isIso_cohomologyBaseChangeMap_of_isFiniteLocallyFree_module {A B : CommRingCat.{u}}
    (φ : A ⟶ B) {X Y : Scheme.{u}} {iX : X ⟶ Spec A} {p : Y ⟶ X} {k : Y ⟶ Spec B}
    (H : IsPullback p k iX (Spec.map φ))
    (hB : letI := φ.hom.toAlgebra; Module.IsFiniteLocallyFree A B)
    (F : X.Modules) [F.IsQuasicoherent] (n : ℕ) :
    IsIso (cohomologyBaseChangeMap H F n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.5, Tag 02KE](https://stacks.math.columbia.edu/tag/02KE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
