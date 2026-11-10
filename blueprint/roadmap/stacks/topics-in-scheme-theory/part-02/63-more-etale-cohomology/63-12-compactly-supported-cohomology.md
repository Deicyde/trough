---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.compactlySupportedCohomology, Stacks.EtaleCohomology.compactlySupportedCohomologyTorsion, Stacks.EtaleCohomology.compactlySupportedCohomologyGroup, Stacks.EtaleCohomology.compactlySupportedCohomologyUnbounded, Stacks.EtaleCohomology.compactlySupportedCohomologyGroupUnbounded, Stacks.EtaleCohomology.compactlySupportedCohomologyBaseChangeIso, Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedBaseChangeIso, Stacks.EtaleCohomology.nonempty_compactlySupportedCohomologyGroup_zero_iso
statement: formalized
proof: formalized
---

# 63.12 Compactly supported cohomology

Section 63.12 of the Stacks Project, [Tag 0GJY](https://stacks.math.columbia.edu/tag/0GJY). 5 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GJZ, a definition

[Tag 0GJZ](https://stacks.math.columbia.edu/tag/0GJZ) in the Stacks Project.

**`Stacks.EtaleCohomology.compactlySupportedCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean#L98). The attribute's comment: “RΓ_c(X, K) = RΓ(Spec k, Rf_! K)”. References: SGA 7 XXII (3.4).

> **Stacks Project, Tag 0GJZ.** The cohomology with compact support
> `RΓ_c(X, K) = RΓ(Spec k, Rf_! K)` of a bounded below complex of sheaves of `Λ`-modules on the
> small étale site of a separated finite type `k`-scheme `X`, through a compactification `j`.

```lean
abbrev compactlySupportedCohomology (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ] :
    DerivedCategory.Plus (EtaleModules.{u, r} Λ X) ⥤
      DerivedCategory.Plus (ModuleCat.{max (u + 1) r} Λ)
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTorsion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean#L107). The attribute's comment: “RΓ_c on D⁺_tors”.

> **Stacks Project, Tag 0GJZ.** Cohomology with compact support on the subcategory
> `D⁺_tors(X_étale, Λ)` of bounded below complexes with torsion cohomology sheaves, which is the
> domain the source states the definition on.

```lean
abbrev compactlySupportedCohomologyTorsion (j : CompactificationOf (Over.mk f))
    (Λ : Type r) [Ring Λ] :
    (isTorsionPlus.{u, r} Λ X).FullSubcategory ⥤
      DerivedCategory.Plus (ModuleCat.{max (u + 1) r} Λ)
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomology.lean#L116). The attribute's comment: “H^i_c(X, K) = H^i(RΓ_c(X, K))”.

> **Stacks Project, Tag 0GJZ.** The compactly supported cohomology module
> `H^i_c(X, K) = H^i(RΓ_c(X, K))`.

```lean
abbrev compactlySupportedCohomologyGroup (j : CompactificationOf (Over.mk f))
    (Λ : Type r) [Ring Λ] (i : ℤ) :
    DerivedCategory.Plus (EtaleModules.{u, r} Λ X) ⥤ ModuleCat.{max (u + 1) r} Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnbounded`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyUnbounded.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyUnbounded.lean#L237). The attribute's comment: “RΓ_c(X, K) = RΓ(Spec k, Rf_! K) on D(X_étale, Λ)”. References: SGA 4½ Rapport (3.6); SGA 7 XXII (3.4), “more general”.

> The cohomology with compact support `RΓ_c(X, K) = RΓ(Spec k, Rf_! K)` of an arbitrary
> complex of sheaves of `Λ`-modules on the small étale site of a separated finite type `k`-scheme
> `X`, through a compactification `j`.

```lean
abbrev compactlySupportedCohomologyUnbounded (j : CompactificationOf (Over.mk f))
    (Λ : Type r) [Ring Λ] :
    DerivedCategory (EtaleModules.{u, r} Λ X) ⥤ DerivedCategory (ModuleCat.{max (u + 1) r} Λ)
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyGroupUnbounded`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyUnbounded.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyUnbounded.lean#L246). The attribute's comment: “H^i_c(X, K) = H^i(RΓ_c(X, K)) on D(X_étale, Λ)”.

> The compactly supported cohomology module `H^i_c(X, K) = H^i(RΓ_c(X, K))` of an arbitrary
> complex `K` in `D(X_étale, Λ)`.

```lean
abbrev compactlySupportedCohomologyGroupUnbounded (j : CompactificationOf (Over.mk f))
    (Λ : Type r) [Ring Λ] (i : ℤ) :
    DerivedCategory (EtaleModules.{u, r} Λ X) ⥤ ModuleCat.{max (u + 1) r} Λ
```

## Tag 0GK0, a lemma

[Tag 0GK0](https://stacks.math.columbia.edu/tag/0GK0) in the Stacks Project.

**`Stacks.EtaleCohomology.compactlySupportedCohomologyBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChange.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChange.lean#L163). The attribute's comment: “(Rf_! K)_ȳ ≅ RΓ_c(X_ȳ, K|_{X_ȳ}), with (Rf_! K)_ȳ = RΓ(Spec k, ȳ⁻¹ Rf_! K)”. References: SGA 4 XVIII (0.1), “special case”; SGA 4½ Arcata (4.5.4), “more general”.

> **Stacks Project, Tag 0GK0**, the cohomology form, for a base change to a field. For a
> cartesian square of schemes with `Y' = Spec k` (for instance a geometric point
> `ȳ : Spec k ⟶ Y`, `k` separably closed), a compactification `j` of `X` over `Y` and
> `K ∈ D⁺_tors(X_étale, Λ)`: `RΓ(Spec k, g⁻¹ Rf_! K)`, which for `k` separably closed is the stalk
> `(Rf_! K)_ȳ`, is the compactly supported cohomology `RΓ_c(X', (g')⁻¹ K)` of the fibre
> `X' = X ×_Y Spec k`, computed with the base change of `j`.

```lean
def compactlySupportedCohomologyBaseChangeIso {k : Type u} [Field k] {X Y X' : Scheme.{u}}
    {f : X ⟶ Y} {g : Spec (.of k) ⟶ Y} {g' : X' ⟶ X} {f' : X' ⟶ Spec (.of k)}
    [LocallyOfFiniteType f'] [QuasiCompact f'] [IsSeparated f'] (sq : IsPullback g' f' f g)
    (j : CompactificationOf (Over.mk f)) (K : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X))
    (hK : isTorsionPlus.{u, 0} Λ X K) :
    (etaleModuleDerivedGlobalSections.{u, 0} Λ (Spec (.of k))).obj
        ((etaleModuleDerivedInverseImagePlus.{u, 0} Λ g).obj
          ((derivedLowerShriek.{u, 0} f j Λ).obj K)) ≅
      (compactlySupportedCohomology.{u, 0} k f' (j.baseChange sq) Λ).obj
        ((etaleModuleDerivedInverseImagePlus.{u, 0} Λ g').obj K)
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeFibreUnbounded.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeFibreUnbounded.lean#L65). The attribute's comment: “(Rf_! K)_ȳ ≅ RΓ_c(X_ȳ, K|_{X_ȳ}) for K ∈ D(X_étale, Λ), Λ torsion”. References: SGA 4 XVII (5.2.2), “special case”; SGA 4 XVII (7.3.7), “special case”; SGA 4 XVIII (0.1), “special case”; SGA 4½ Arcata (4.5.4), “special case”.

> **Stacks Project, Tag 0GK0**, the case of `D(X_étale, Λ)` for a torsion ring `Λ`. For a
> cartesian square of schemes with `Y' = Spec k` (for instance a geometric point
> `ȳ : Spec k ⟶ Y`, `k` separably closed), a compactification `j` of `X` over `Y`, a ring `Λ` with
> `m = 0` in `Λ` for some `m > 0`, and an arbitrary `K ∈ D(X_étale, Λ)`:
> `RΓ(Spec k, g⁻¹ Rf_! K)`, which for `k` separably closed is the stalk `(Rf_! K)_ȳ`, is the
> compactly supported cohomology `RΓ_c(X', (g')⁻¹ K)` of the fibre `X' = X ×_Y Spec k`, computed
> with the base change of `j`. Together with
> `Stacks.EtaleCohomology.compactlySupportedCohomologyBaseChangeIso` (the case of
> `D⁺_tors(X_étale, Λ)`) this is the whole tag.

```lean
def compactlySupportedCohomologyUnboundedBaseChangeIso
    (K : DerivedCategory (EtaleModules.{u, 0} Λ X)) :
    (etaleModuleDerivedGlobalSectionsUnbounded.{u, 0} Λ (Spec (.of k))).obj
        ((etaleModuleDerivedInverseImage.{u, 0} Λ g).obj
          ((derivedLowerShriekUnbounded.{u, 0} f j Λ).obj K)) ≅
      (compactlySupportedCohomologyUnbounded.{u, 0} k f' (j.baseChange sq) Λ).obj
        ((etaleModuleDerivedInverseImage.{u, 0} Λ g').obj K)
```

## Tag 0GK1, a lemma

[Tag 0GK1](https://stacks.math.columbia.edu/tag/0GK1) in the Stacks Project.

**`Stacks.EtaleCohomology.nonempty_compactlySupportedCohomologyGroup_zero_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZero.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZero.lean#L263). The attribute's comment: “the Definition 0GJZ side only: H^0_c(X, F) is H^0 of the extension by zero on a compactification”.

> The zeroth compactly supported cohomology group of a sheaf of `Λ`-modules `ℱ` on a `k`-scheme
> `X`, placed in degree zero, is the group of global sections of the extension by zero `j_!ℱ` on a
> compactification `j : X ⟶ X̄` of `X` over `k`.
>
> This is the half of Tag 0GK1 that concerns Definition 0GJZ; the source's torsion hypothesis is not
> used.  Tag 0GK1 itself is
> `Stacks.EtaleCohomology.nonempty_addEquiv_compactlySupportedCohomologyGroup_zero`.

```lean
theorem nonempty_compactlySupportedCohomologyGroup_zero_iso
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ]
    (F : EtaleModules.{u, r} Λ X) :
    Nonempty ((compactlySupportedCohomologyGroup.{u, r} k f j Λ 0).obj
        ((DerivedCategory.Plus.singleFunctor (EtaleModules.{u, r} Λ X) 0).obj F) ≅
      (etaleModuleGlobalSections.{u, r} Λ j.space).obj
        ((etaleModuleExtensionByZero.{u, r} Λ j.immersion).obj F))
```

**`Stacks.EtaleCohomology.nonempty_addEquiv_compactlySupportedCohomologyGroup_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZeroComparison.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactlySupportedCohomologyZeroComparison.lean#L306).

> **Stacks Project, Tag 0GK1.** Let `X` be a separated scheme of finite type over a field `k`
> and let `ℱ` be an abelian sheaf on `X_étale`, that is a sheaf of `ℤ`-modules. The group
> `H⁰_c(X, ℱ)` of Definition 0GJZ, the zeroth cohomology of `RΓ_c(X, ℱ) = RΓ(Spec k, Rf_!ℱ)`
> formed with a compactification `j : X ⟶ X̄`, agrees with the group `H⁰_c(X, ℱ)` of Definition
> 0F72 of sections of `ℱ` with support proper over `k`, the latter taken on the small étale site of
> Tag 021B inside any big étale site `B` containing `X`, on which `ℱ` is read through
> `AlgebraicGeometry.SmallEtale.etaleModulesIntEquivalence`.
>
> Both groups are `H⁰(X̄, j_!ℱ)`: the first by
> `Stacks.EtaleCohomology.nonempty_compactlySupportedCohomologyGroup_zero_iso`, the second by Tags
> 0F75 and 0F73. The source's torsion hypothesis is not used.

```lean
theorem nonempty_addEquiv_compactlySupportedCohomologyGroup_zero
    (j : CompactificationOf (Over.mk f)) (B : BigEtaleSite.{u}) (hX : B.Contains X)
    (F : EtaleModules.{u, 0} ℤ X) :
    Nonempty ((compactlySupportedCohomologyGroup.{u, 0} k f j ℤ 0).obj
        ((DerivedCategory.Plus.singleFunctor (EtaleModules.{u, 0} ℤ X) 0).obj F) ≃+
      SmallEtale.compactlySupportedSections k X f B hX
        ((SmallEtale.etaleModulesIntEquivalence B X hX).functor.obj F))
```

## Tag 0GKR, a lemma

[Tag 0GKR](https://stacks.math.columbia.edu/tag/0GKR) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_compactlySupportedCohomologyGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CompactSupportCurveFiniteness.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CompactSupportCurveFiniteness.lean#L187). References: SGA 4 XVII (5.3.8), “special case”.

> Let `k` be an algebraically closed field, `X` a separated scheme of finite type over `k` of
> dimension at most one, `Λ` a Noetherian ring, and `F` a constructible sheaf of `Λ`-modules on
> `X_étale` which is torsion. Then `H^q_c(X, F)` is a finite `Λ`-module for every `q`.
>
> `H^q_c(X, F)` is `Stacks.EtaleCohomology.compactlySupportedCohomologyGroup` of Definition 0GJZ, the
> `q`-th cohomology of `RΓ(Spec k, Rf̄_* j_! F)`, at `F` placed in degree zero; the statement holds
> for every compactification `j : X ⟶ X̄` of `X` over `k`, through which it is computed.
> Constructibility is `Stacks.EtaleCohomology.IsBigSiteConstructibleEtaleModule` (Tag 03RW (3), read
> on the small étale site of Tag 021B of a big étale site `B` containing `X`) and torsion is
> `Stacks.EtaleCohomology.IsTorsionEtaleModule`.

```lean
theorem module_finite_compactlySupportedCohomologyGroup {k : Type u} [Field k] [IsAlgClosed k]
    (B : BigEtaleSite.{u}) (X : B.Scheme) (f : X.obj ⟶ Spec (.of k)) [IsSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] (hdim : topologicalKrullDim X.obj ≤ 1)
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ]
    (F : EtaleModules.{u, r} Λ X.obj) (hc : IsBigSiteConstructibleEtaleModule B X Λ F)
    (ht : IsTorsionEtaleModule.{u, r} Λ X.obj F) (q : ℤ) :
    Module.Finite Λ ((compactlySupportedCohomologyGroup.{u, r} k f j Λ q).obj
      ((DerivedCategory.Plus.singleFunctor (EtaleModules.{u, r} Λ X.obj) 0).obj F))
```

## Tag 0GKS, a remark

[Tag 0GKS](https://stacks.math.columbia.edu/tag/0GKS) in the Stacks Project.

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTraceOfWeighting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L205). The attribute's comment: “case (4), K in D⁺_tors(Y_étale, Λ): the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K), natural in K, defined as RΓ(Spec k, Rp_! f⁻¹K) = RΓ(Spec k, Rq_! f_! f⁻¹K) ⟶ RΓ(Spec k, Rq_! K) with Rq_! ∘ f_! = Rp_! by 0F7J and the trace Tr_{f,w,K}; f quasi-finite, w a weighting of f, X and Y separated of finite type over the field k, p = f ≫ q”. References: SGA 4 XVII (6.2.7), “more general”.

> **Stacks Project, Tag 0GKS**, case (4), on `D⁺_tors`. For `f : X ⟶ Y` a quasi-finite
> morphism of separated schemes of finite type over a field `k` and `w` a weighting of `f`, the
> natural map
>
> `RΓ_c(X, f^{-1}K) = RΓ(Spec k, Rp_! f^{-1}K) = RΓ(Spec k, Rq_! f_! f^{-1}K)`
> `  ⟶ RΓ(Spec k, Rq_! K) = RΓ_c(Y, K)`
>
> of `K ∈ D⁺_tors(Y_étale, Λ)`: the middle identification is [Stacks, Tag 0F7J]
> (`Stacks.EtaleCohomology.derivedLowerShriekCompIsoUniv`), with `f_! = Rf_!` computed through a
> compactification of `f` finite over `Y`, and the arrow is `RΓ(Spec k, Rq_! Tr_{f, w, K})` for the
> trace map `Stacks.EtaleCohomology.derivedLowerShriekWeightedTrace`.

```lean
def compactlySupportedCohomologyTraceOfWeighting [LocallyQuasiFinite f] :
    (isTorsionPlus.{u, u} Λ Y).ι ⋙ etaleModuleDerivedInverseImagePlus.{u, u} Λ f ⋙
        compactlySupportedCohomology.{u, u} k (f ≫ q) jp Λ ⟶
      (isTorsionPlus.{u, u} Λ Y).ι ⋙ compactlySupportedCohomology.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedTraceOfWeighting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L236). The attribute's comment: “case (4), K in D(Y_étale, Λ) with Λ torsion: the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K), natural in K, defined as RΓ(Spec k, Rp_! f⁻¹K) = RΓ(Spec k, Rq_! f_! f⁻¹K) ⟶ RΓ(Spec k, Rq_! K) with Rq_! ∘ f_! = Rp_! by 0F7J and the trace Tr_{f,w,K}”. References: SGA 4 XVII (6.2.7), “partial”.

> **Stacks Project, Tag 0GKS**, case (4), on `D(Y_étale, Λ)` for a torsion ring `Λ`: the
> natural map `RΓ_c(X, f^{-1}K) ⟶ RΓ_c(Y, K)` of `K ∈ D(Y_étale, Λ)`, through
> `Rp_! = Rq_! ∘ f_!` ([Stacks, Tag 0F7J],
> `Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompIso`) and `RΓ(Spec k, Rq_! Tr_{f, w, K})`
> for the trace map `Stacks.EtaleCohomology.derivedLowerShriekUnboundedWeightedTrace`.

```lean
def compactlySupportedCohomologyUnboundedTraceOfWeighting [LocallyQuasiFinite f] :
    (etaleModuleInverseImage.{u, u} Λ f).mapDerivedCategory ⋙
        compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ ⟶
      compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyConstantTraceOfWeighting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L275). The attribute's comment: “case (4), the arrow Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ) for a torsion ring Λ”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (4), the constant coefficients: for a torsion ring `Λ`,
> `Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ)`, the map `RΓ_c(X, f^{-1}Λ) ⟶ RΓ_c(Y, Λ)` at the constant sheaf
> `Λ` read through `f^{-1}Λ_Y = Λ_X`.

```lean
def compactlySupportedCohomologyConstantTraceOfWeighting [LocallyQuasiFinite f] :
    (compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ X) 0).obj
          ((constantSheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ)))) ⟶
      (compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ Y) 0).obj
          ((constantSheaf Y.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ))))
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTraceOfEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L307). The attribute's comment: “case (1), f étale, K in D⁺_tors(Y_étale, Λ): the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (1), on `D⁺_tors`: `f` étale. The weighting is the
> canonical one of [Stacks, Tag 0GKI].

```lean
def compactlySupportedCohomologyTraceOfEtale [Etale f] :
    (isTorsionPlus.{u, u} Λ Y).ι ⋙ etaleModuleDerivedInverseImagePlus.{u, u} Λ f ⋙
        compactlySupportedCohomology.{u, u} k (f ≫ q) jp Λ ⟶
      (isTorsionPlus.{u, u} Λ Y).ι ⋙ compactlySupportedCohomology.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTraceOfFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L318). The attribute's comment: “case (2), f flat and quasi-finite, K in D⁺_tors(Y_étale, Λ): the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”. References: SGA 4 XVII (6.2.7), “partial”.

> **Stacks Project, Tag 0GKS**, case (2), on `D⁺_tors`: `f` flat and quasi-finite. The
> weighting is the canonical one of [Stacks, Tag 0GKI].

```lean
def compactlySupportedCohomologyTraceOfFlat [Flat f] [LocallyQuasiFinite f] :
    (isTorsionPlus.{u, u} Λ Y).ι ⋙ etaleModuleDerivedInverseImagePlus.{u, u} Λ f ⋙
        compactlySupportedCohomology.{u, u} k (f ≫ q) jp Λ ⟶
      (isTorsionPlus.{u, u} Λ Y).ι ⋙ compactlySupportedCohomology.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedTraceOfEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L329). The attribute's comment: “case (1), f étale, K in D(Y_étale, Λ) with Λ torsion: the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (1), on `D(Y_étale, Λ)` for a torsion ring `Λ`.

```lean
def compactlySupportedCohomologyUnboundedTraceOfEtale [Etale f] :
    (etaleModuleInverseImage.{u, u} Λ f).mapDerivedCategory ⋙
        compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ ⟶
      compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedTraceOfFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L340). The attribute's comment: “case (2), f flat and quasi-finite, K in D(Y_étale, Λ) with Λ torsion: the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (2), on `D(Y_étale, Λ)` for a torsion ring `Λ`.

```lean
def compactlySupportedCohomologyUnboundedTraceOfFlat [Flat f] [LocallyQuasiFinite f] :
    (etaleModuleInverseImage.{u, u} Λ f).mapDerivedCategory ⋙
        compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ ⟶
      compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyConstantTraceOfEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L352). The attribute's comment: “case (1), f étale: the arrow Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ) for a torsion ring Λ”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (1), the arrow `Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ)` for `f`
> étale and `Λ` torsion.

```lean
def compactlySupportedCohomologyConstantTraceOfEtale [Etale f] :
    (compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ X) 0).obj
          ((constantSheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ)))) ⟶
      (compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ Y) 0).obj
          ((constantSheaf Y.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ))))
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyConstantTraceOfFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L369). The attribute's comment: “case (2), f flat and quasi-finite: the arrow Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ) for a torsion ring Λ”. References: SGA 4 XVII (6.2.7), “special case”.

> **Stacks Project, Tag 0GKS**, case (2), the arrow `Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ)` for `f`
> flat and quasi-finite and `Λ` torsion.

```lean
def compactlySupportedCohomologyConstantTraceOfFlat [Flat f] [LocallyQuasiFinite f] :
    (compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ X) 0).obj
          ((constantSheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ)))) ⟶
      (compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ Y) 0).obj
          ((constantSheaf Y.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ))))
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTraceOfGeometricallyUnibranch`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L402). The attribute's comment: “case (3), f quasi-finite and Y geometrically unibranch, K in D⁺_tors(Y_étale, Λ): the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”.

> **Stacks Project, Tag 0GKS**, case (3), on `D⁺_tors`: `f` quasi-finite and `Y` geometrically
> unibranch. The weighting is the generic separable degree of [Stacks, Tag 0GKJ].

```lean
def compactlySupportedCohomologyTraceOfGeometricallyUnibranch [LocallyQuasiFinite f] :
    (isTorsionPlus.{u, u} Λ Y).ι ⋙ etaleModuleDerivedInverseImagePlus.{u, u} Λ f ⋙
        compactlySupportedCohomology.{u, u} k (f ≫ q) jp Λ ⟶
      (isTorsionPlus.{u, u} Λ Y).ι ⋙ compactlySupportedCohomology.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyUnboundedTraceOfGeometricallyUnibranch`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L413). The attribute's comment: “case (3), f quasi-finite and Y geometrically unibranch, K in D(Y_étale, Λ) with Λ torsion: the map RΓ_c(X, f⁻¹K) ⟶ RΓ_c(Y, K)”.

> **Stacks Project, Tag 0GKS**, case (3), on `D(Y_étale, Λ)` for a torsion ring `Λ`.

```lean
def compactlySupportedCohomologyUnboundedTraceOfGeometricallyUnibranch [LocallyQuasiFinite f] :
    (etaleModuleInverseImage.{u, u} Λ f).mapDerivedCategory ⋙
        compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ ⟶
      compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyConstantTraceOfGeometricallyUnibranch`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/Covariance.lean#L425). The attribute's comment: “case (3), f quasi-finite and Y geometrically unibranch: the arrow Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ) for a torsion ring Λ”.

> **Stacks Project, Tag 0GKS**, case (3), the arrow `Tr_f : RΓ_c(X, Λ) ⟶ RΓ_c(Y, Λ)` for `f`
> quasi-finite, `Y` geometrically unibranch and `Λ` torsion.

```lean
def compactlySupportedCohomologyConstantTraceOfGeometricallyUnibranch [LocallyQuasiFinite f] :
    (compactlySupportedCohomologyUnbounded.{u, u} k (f ≫ q) jp Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ X) 0).obj
          ((constantSheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ)))) ⟶
      (compactlySupportedCohomologyUnbounded.{u, u} k q jq Λ).obj
        ((DerivedCategory.singleFunctor (EtaleModules.{u, u} Λ Y) 0).obj
          ((constantSheaf Y.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj
            (ModuleCat.of Λ (ULift.{u + 1} Λ))))
```

**`Stacks.EtaleCohomology.derivedLowerShriekWeightedTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/DerivedTrace.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/DerivedTrace.lean#L102). The attribute's comment: “the trace map Tr_{f,w,K} : f_! f^{-1} K ⟶ K for K in D⁺(Y_étale, Λ), natural in K, for a weighting w of f and Rf_! = f_! computed through a compactification of f finite over Y (Zariski's main theorem, 05K0, provides one for f quasi-finite separated over a qcqs Y)”.

> **The trace map `Tr_{f, w, K} : Rf_! f^{-1}K ⟶ K` on `D⁺(Y_étale, Λ)`** ([Stacks, Tag 0GKS],
> from [Stacks, Tag 0GKH] (3)), for a weighting `w` of `f` and `Rf_!` computed through a
> compactification of `f` finite over `Y`: the derived form of the trace
> `Stacks.EtaleCohomology.etaleModuleCompactificationTrace`, through
> `Rf_! = f̄_* ∘ j_!` ([Stacks, Tag 0GKM]). It is natural in `K`.

```lean
def derivedLowerShriekWeightedTrace :
    etaleModuleDerivedInverseImagePlus.{u, u} Λ f ⋙ derivedLowerShriek.{u, u} f jf Λ ⟶
      𝟭 (DerivedCategory.Plus (EtaleModules.{u, u} Λ Y))
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedWeightedTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/DerivedTrace.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportCovariance/DerivedTrace.lean#L128). The attribute's comment: “the trace map Tr_{f,w,K} : f_! f^{-1} K ⟶ K for K in D(Y_étale, Λ), natural in K, for a weighting w of f and Rf_! = f_! computed through a compactification of f finite over Y”.

> **The trace map `Tr_{f, w, K} : Rf_! f^{-1}K ⟶ K` on `D(Y_étale, Λ)`** ([Stacks, Tag 0GKS],
> from [Stacks, Tag 0GKH] (3)), for a weighting `w` of `f` and `Rf_!` computed through a
> compactification of `f` finite over `Y`. It is natural in `K`.

```lean
def derivedLowerShriekUnboundedWeightedTrace :
    (etaleModuleInverseImage.{u, u} Λ f).mapDerivedCategory ⋙
        derivedLowerShriekUnbounded.{u, u} f jf Λ ⟶
      𝟭 (DerivedCategory (EtaleModules.{u, u} Λ Y))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.12, Tag 0GJY](https://stacks.math.columbia.edu/tag/0GJY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
