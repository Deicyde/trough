---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.isConstructible_moduleFShriekDerivedFunctor, Stacks.EtaleCohomology.isConstructible_moduleFShriekDerivedFunctor_general, Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_constantSheaf, Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_openAffineLine, Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_affineLine, Stacks.EtaleCohomology.isConstructibleTorsion_homology_derivedLowerShriek_of_isConstructible, Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_of_isConstructible
statement: formalized
proof: formalized
---

# 63.14 Complexes with constructible cohomology

Section 63.14 of the Stacks Project, [Tag 0GK2](https://stacks.math.columbia.edu/tag/0GK2). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GK3, a lemma

[Tag 0GK3](https://stacks.math.columbia.edu/tag/0GK3) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructible_moduleFShriekDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/QuasiFiniteShriek.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/QuasiFiniteShriek.lean#L179). The attribute's comment: “the source's reduction of the tag to its sheaf-level case, which is carried as hShriekSheaf: granted that a Λ-linear lift of f\_! takes constructible sheaves of Λ-modules to constructible sheaves for every locally quasi-finite morphism of finite presentation, the functor f\_! of Stacks 0F5N on unbounded derived categories sends D\_c into D\_c. The step from sheaves to complexes, exactness of f\_! and hence Hⁱ(f\_! K) ≅ f\_!(Hⁱ K), is proved”.

> **Stacks 0GK3**, granted the sheaf-level case. Let `Λ` be a Noetherian ring and let
> `f : X ⟶ Y` be a morphism of schemes which is locally quasi-finite and of finite presentation.
> If a complex `K` of étale sheaves of `Λ`-modules on `X` lies in `D_c(X_étale, Λ)`, then
> `f_! K` lies in `D_c(Y_étale, Λ)`, where `f_!` is the functor of Stacks 0F5N.
>
> The proof is the source's reduction. A `Λ`-linear lift of the direct image with compact support
> is exact, so it acts on the derived category termwise and `Hⁱ(f_! K) ≅ f_!(Hⁱ K)`; each `Hⁱ K` is
> constructible by hypothesis, and constructibility of its image under `f_!` is `hShriekSheaf`.
>
> `hShriekSheaf` is the sheaf-level form of this tag, quantified over every morphism of the big
> étale site that is locally quasi-finite and of finite presentation, every `Λ`-linear lift of its
> direct image with compact support and every sheaf of `Λ`-modules on its source; it mentions
> neither `f`, nor `fShriekMod`, nor `K`. See "What is carried" in the module documentation.

```lean
public theorem isConstructible_moduleFShriekDerivedFunctor
    (hShriekSheaf : ModuleFShriekConstructibleOnSheaves B Λ)
    (K : DerivedCategory (ModuleSheaf.{u, v, r} B X Λ)) (hK : IsConstructible B X Λ K) :
    IsConstructible B Y Λ ((moduleFShriekDerivedFunctor B Λ f fShriekMod hlift).obj K)
```

**`Stacks.EtaleCohomology.isConstructible_moduleFShriekDerivedFunctor_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/QuasiFiniteShriekUnconditional.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/QuasiFiniteShriekUnconditional.lean#L341). References: SGA 4 XVII (5.3.6), “Quasi-finite case”.

> **Stacks 0GK3.** Let `Λ` be a Noetherian ring and let `f : X ⟶ Y` be a morphism of schemes
> which is locally quasi-finite and of finite presentation. The functor
> `f_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Stacks 0F5N, induced by the direct image with compact
> support `AlgebraicGeometry.SmallEtale.fShriekMod` with coefficients in `Λ`, sends
> `D_c(X_étale, Λ)` into `D_c(Y_étale, Λ)`.

```lean
public theorem isConstructible_moduleFShriekDerivedFunctor_general
    (K : DerivedCategory (ModuleSheaf.{u, u, u + 1} B X Λ)) (hK : IsConstructible B X Λ K) :
    IsConstructible B Y Λ ((moduleFShriekDerivedFunctor B Λ f (fShriekMod.{u, u, u + 1} B Λ f)
      (fShriekModForgetIso.{u, u, u + 1} B Λ f)).obj K)
```

## Tag 0GKX, a lemma

[Tag 0GKX](https://stacks.math.columbia.edu/tag/0GKX) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityRegistration.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityRegistration.lean#L66). The attribute's comment: “S Noetherian (affine and finite-dimensional not needed); Rf\_! through any compactification j of f; Λ torsion as m = 0 in Λ for some m > 0”.

> **Stacks 0GKX.** Let `S` be a Noetherian scheme of `B`, `f : X ⟶ S` a separated, affine,
> smooth morphism of relative dimension `1`, `j` a compactification of `f` (through which
> `Rf_! = Rf̄_* ∘ j_!`), `Λ` a Noetherian ring which is torsion (`m = 0` in `Λ` for some `m > 0`),
> and `M` a finite `Λ`-module. Then every cohomology sheaf of `Rf_! M̲` is constructible. The source
> also assumes `S` affine of finite dimension, which is not needed.

```lean
theorem isConstructibleEtaleModule_homology_derivedLowerShriek_constantSheaf
    (B : BigEtaleSite.{u}) (S : B.Scheme) [IsNoetherian S.obj] {X : Scheme.{u}}
    (f : X ⟶ S.obj) [IsSeparated f] [IsAffineHom f] [SmoothOfRelativeDimension 1 f]
    (j : CompactificationOf (Over.mk f)) (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ]
    (m : ℕ) (hm : 0 < m) (hΛ : (m : Λ) = 0) (M : ModuleCat.{u + 1} Λ) (hM : Module.Finite Λ M)
    (k : ℤ) :
    IsBigSiteConstructibleEtaleModule B S Λ ((DerivedCategory.Plus.homologyFunctor _ k).obj
      ((derivedLowerShriek.{u, 0} f j Λ).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj
        ((constantSheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj M))))
```

## Tag 0GKY, a lemma

[Tag 0GKY](https://stacks.math.columbia.edu/tag/0GKY) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_openAffineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean#L145). The attribute's comment: “Y Noetherian affine (finite dimension not needed); U given with an open immersion ι : U ⟶ A¹\_Y; Λ torsion as m = 0 in Λ for some m > 0; Rf\_! through any compactification j of f”.

> **Stacks 0GKY.** Let `Y` be a Noetherian affine scheme of `B`, `Λ` a Noetherian ring which is
> torsion (`m = 0` in `Λ` for some `m > 0`), `ι : U ⟶ 𝔸¹_Y` an open immersion,
> `f = ι ≫ (𝔸¹_Y ⟶ Y)` the structure morphism of `U`, `j` a compactification of `f`, and `F` a
> finite type locally constant sheaf of `Λ`-modules on `U`. Then every cohomology sheaf of `Rf_! F`
> is constructible. The source also assumes `Y` of finite dimension, which is not needed.

```lean
theorem isConstructibleEtaleModule_homology_derivedLowerShriek_openAffineLine
    (Y : B.Scheme) [IsNoetherian Y.obj] [IsAffine Y.obj] (U : B.Scheme)
    (ι : U.obj ⟶ AffineSpace (ULift.{u} (Fin 1)) Y.obj) [IsOpenImmersion ι]
    (j : CompactificationOf (Over.mk (ι ≫ AffineSpace (ULift.{u} (Fin 1)) Y.obj ↘ Y.obj)))
    (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] (m : ℕ) (hm : 0 < m) (hΛ : (m : Λ) = 0)
    (F : EtaleModules.{u, 0} Λ U.obj)
    (hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant Λ U.obj.smallEtaleTopology F) (k : ℤ) :
    IsBigSiteConstructibleEtaleModule B Y Λ ((DerivedCategory.Plus.homologyFunctor _ k).obj
      ((derivedLowerShriek.{u, 0} _ j Λ).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj F)))
```

## Tag 0GKZ, a lemma

[Tag 0GKZ](https://stacks.math.columbia.edu/tag/0GKZ) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_affineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean#L127). The attribute's comment: “A¹\_Y given as X with an isomorphism ι : X ≅ A¹\_Y; Rf\_! through any compactification j of f”.

> **Stacks 0GKZ.** Let `Y` be an affine scheme of `B`, `Λ` a Noetherian ring, `ι : X ≅ 𝔸¹_Y`,
> `f = ι ≫ (𝔸¹_Y ⟶ Y)` the structure morphism, `j` a compactification of `f`, and `F` a
> constructible sheaf of `Λ`-modules on `X = 𝔸¹_Y` which is torsion. Then every cohomology sheaf of
> `Rf_! F` is constructible.

```lean
theorem isConstructibleEtaleModule_homology_derivedLowerShriek_affineLine
    (Y : B.Scheme) [IsAffine Y.obj] (X : B.Scheme)
    (ι : X.obj ⟶ AffineSpace (ULift.{u} (Fin 1)) Y.obj) [IsIso ι]
    (j : CompactificationOf (Over.mk (ι ≫ AffineSpace (ULift.{u} (Fin 1)) Y.obj ↘ Y.obj)))
    (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] (F : EtaleModules.{u, 0} Λ X.obj)
    (hF : IsBigSiteConstructibleEtaleModule B X Λ F) (ht : IsTorsionEtaleModule Λ X.obj F) (k : ℤ) :
    IsBigSiteConstructibleEtaleModule B Y Λ ((DerivedCategory.Plus.homologyFunctor _ k).obj
      ((derivedLowerShriek.{u, 0} _ j Λ).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj F)))
```

## Tag 0GL0, a theorem

[Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleTorsion_homology_derivedLowerShriek_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityTorsion.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityTorsion.lean#L49). The attribute's comment: “both cases: K in D+\_\{tors,c}(X, Λ), and K in D\_c(X, Λ) when Λ is torsion (m = 0 in Λ for some m > 0; Rf\_! on D(X, Λ) is derivedLowerShriekUnbounded); Rf\_! through any compactification j of f”.

> **Stacks 0GL0.** Let `f : X ⟶ Y` be a separated morphism of finite presentation of schemes of
> `B`, with `Y` quasi-compact and quasi-separated (hence so is `X`), `j` a compactification of `f`
> (through which `Rf_! = Rf̄_* ∘ j_!`), and `Λ` a Noetherian ring.
> 1. If `K ∈ D⁺(X_étale, Λ)` has constructible torsion cohomology sheaves, then so has `Rf_! K`,
>    i.e. `Rf_! K ∈ D⁺_{tors,c}(Y_étale, Λ)`.
> 2. If `Λ` is torsion and `K ∈ D(X_étale, Λ)` has constructible cohomology sheaves, so has
>    `Rf_! K`, i.e. `Rf_! K ∈ D_c(Y_étale, Λ)`.

```lean
theorem isConstructibleTorsion_homology_derivedLowerShriek_of_isConstructible
    {X Y : B.Scheme} [CompactSpace Y.obj] [QuasiSeparatedSpace Y.obj] (f : X.obj ⟶ Y.obj)
    [IsSeparated f] [LocallyOfFinitePresentation f] [QuasiCompact f]
    (j : CompactificationOf (Over.mk f)) (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] :
    (∀ K : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X.obj),
      (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ
          ((DerivedCategory.Plus.homologyFunctor _ q).obj K) ∧
        IsTorsionEtaleModule Λ X.obj ((DerivedCategory.Plus.homologyFunctor _ q).obj K)) →
      ∀ n : ℤ, IsBigSiteConstructibleEtaleModule B Y Λ
          ((DerivedCategory.Plus.homologyFunctor _ n).obj
            ((derivedLowerShriek.{u, 0} f j Λ).obj K)) ∧
        IsTorsionEtaleModule Λ Y.obj
          ((DerivedCategory.Plus.homologyFunctor _ n).obj
            ((derivedLowerShriek.{u, 0} f j Λ).obj K))) ∧
    ((∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) →
      ∀ K : DerivedCategory (EtaleModules.{u, 0} Λ X.obj),
        (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ
          ((DerivedCategory.homologyFunctor _ q).obj K)) →
        ∀ n : ℤ, IsBigSiteConstructibleEtaleModule B Y Λ ((DerivedCategory.homologyFunctor _ n).obj
          ((derivedLowerShriekUnbounded.{u, 0} f j Λ).obj K)))
```

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_homology_derivedLowerShriek_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ConstructibilityUnconditional.lean#L99). The attribute's comment: “both cases: K in D+\_\{tors,c}(X, Λ), and K in D\_c(X, Λ) when Λ is torsion (m = 0 in Λ for some m > 0; Rf\_! on D(X, Λ) is derivedLowerShriekUnbounded); Rf\_! through any compactification j of f”.

> **Stacks 0GL0.** Let `f : X ⟶ Y` be a separated morphism of finite presentation of schemes of
> `B`, with `Y` quasi-compact and quasi-separated (hence so is `X`), `j` a compactification of `f`
> (through which `Rf_! = Rf̄_* ∘ j_!`), and `Λ` a Noetherian ring.
> 1. If `K ∈ D⁺(X_étale, Λ)` has constructible torsion cohomology sheaves, so has `Rf_! K`.
> 2. If `Λ` is torsion and `K ∈ D(X_étale, Λ)` has constructible cohomology sheaves, so has
>    `Rf_! K`.

```lean
theorem isConstructibleEtaleModule_homology_derivedLowerShriek_of_isConstructible
    {X Y : B.Scheme} [CompactSpace Y.obj] [QuasiSeparatedSpace Y.obj] (f : X.obj ⟶ Y.obj)
    [IsSeparated f] [LocallyOfFinitePresentation f] [QuasiCompact f]
    (j : CompactificationOf (Over.mk f)) (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] :
    (∀ K : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X.obj),
      (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ
          ((DerivedCategory.Plus.homologyFunctor _ q).obj K) ∧
        IsTorsionEtaleModule Λ X.obj ((DerivedCategory.Plus.homologyFunctor _ q).obj K)) →
      ∀ n : ℤ, IsBigSiteConstructibleEtaleModule B Y Λ
        ((DerivedCategory.Plus.homologyFunctor _ n).obj ((derivedLowerShriek.{u, 0} f j Λ).obj
            K))) ∧
    ((∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) →
      ∀ K : DerivedCategory (EtaleModules.{u, 0} Λ X.obj),
        (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ ((DerivedCategory.homologyFunctor _ q).obj K)) →
        ∀ n : ℤ, IsBigSiteConstructibleEtaleModule B Y Λ ((DerivedCategory.homologyFunctor _ n).obj
          ((derivedLowerShriekUnbounded.{u, 0} f j Λ).obj K)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.14, Tag 0GK2](https://stacks.math.columbia.edu/tag/0GK2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
