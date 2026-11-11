---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_coprime, Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_isProper, Stacks.EtaleCohomology.TorsionModules.finite_etaleCohomology_constantSheaf, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward_of_isFinite, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero_of_dense, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_coprime
statement: formalized
proof: formalized
---

# 59.84 Cohomology of torsion modules on curves

Section 59.84 of the Stacks Project, [Tag 0GJB](https://stacks.math.columbia.edu/tag/0GJB). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GJC, a lemma

[Tag 0GJC](https://stacks.math.columbia.edu/tag/0GJC) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean#L103). The attribute's comment: “part (1): n prime to char(k)”.

> **Stacks Project, Tag 0GJC, part (1).** Let `Λ` be a Noetherian ring, `M` a finite
> `Λ`-module annihilated by an integer `n > 0`, `k` an algebraically closed field and `X` a
> separated scheme of finite type over `k` of dimension at most one. If `n` is prime to the
> characteristic of `k`, then `H^q(X, M̲)` is a finite `Λ`-module for every `q`.
>
> Here `X` is a scheme with a separated, locally of finite type and quasi-compact structure morphism
> `π : X ⟶ Spec k`, the dimension is the Krull dimension of the underlying space, `M̲` is the
> constant sheaf of `Λ`-modules on `X_étale` and `H^q(X, M̲)` is the `q`-th right derived functor
> of global sections of sheaves of `Λ`-modules on `X_étale`. "Prime to the characteristic" is read
> with the exponential characteristic, so that it is no condition in characteristic zero.
>
> The proof is the source's (`module_finite_etaleCohomology_constantSheaf`), with the input
> Tag 03SC supplied by `curveTorsionCohomologyStatement_holds`.

```lean
theorem module_finite_etaleCohomology_constantSheaf_of_coprime
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] (hX : topologicalKrullDim X ≤ 1)
    (M : ModuleCat.{max (u + 1) r} Λ) [Module.Finite Λ M] (n : ℕ) (hn : 0 < n)
    (hM : ∀ m : M, n • m = 0) (hnk : n.Coprime (ringExpChar k)) (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((constantSheaf X.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).obj M))
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean#L126). The attribute's comment: “part (2): X proper over k”.

> **Stacks Project, Tag 0GJC, part (2).** Let `Λ` be a Noetherian ring, `M` a finite
> `Λ`-module annihilated by an integer `n > 0`, `k` an algebraically closed field and `X` a
> separated scheme of finite type over `k` of dimension at most one. If `X` is proper over `k`,
> then `H^q(X, M̲)` is a finite `Λ`-module for every `q`.
>
> Here `X` is a scheme with a separated, locally of finite type and quasi-compact structure morphism
> `π : X ⟶ Spec k`, the dimension is the Krull dimension of the underlying space, `M̲` is the
> constant sheaf of `Λ`-modules on `X_étale` and `H^q(X, M̲)` is the `q`-th right derived functor
> of global sections of sheaves of `Λ`-modules on `X_étale`.
>
> The proof is the source's (`module_finite_etaleCohomology_constantSheaf`), with the input
> Tag 03SC supplied by `curveTorsionCohomologyStatement_holds`.

```lean
theorem module_finite_etaleCohomology_constantSheaf_of_isProper
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] [IsProper π]
    (hX : topologicalKrullDim X ≤ 1) (M : ModuleCat.{max (u + 1) r} Λ) [Module.Finite Λ M]
    (n : ℕ) (hn : 0 < n) (hM : ∀ m : M, n • m = 0) (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((constantSheaf X.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).obj M))
```

**`Stacks.EtaleCohomology.TorsionModules.finite_etaleCohomology_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveTorsionStatementsHold.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveTorsionStatementsHold.lean#L62). The attribute's comment: “both parts: n prime to char(k), or X proper”.

> **Stacks Project, Tag 0GJC.** Let `Λ` be a Noetherian ring, `M` a finite `Λ`-module
> annihilated by an integer `n > 0`, `k` an algebraically closed field and `X` a separated scheme of
> finite type over `k` of dimension at most one. Then `H^q_étale(X, M̲)` is a finite `Λ`-module for
> every `q`
>
> 1. if `n` is prime to the characteristic of `k`, and
> 2. if `X` is proper over `k`.
>
> The two parts are the two sides of the disjunction `n.Coprime (ringExpChar k) ∨ IsProper π`; the
> exponential characteristic makes the coprimality condition vacuous in characteristic zero, as in
> the source. This is
> `Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf` with its
> input, the statement of Tag 03SC, discharged by
> `Stacks.EtaleCohomology.curveTorsionCohomologyStatement_holds`.

```lean
theorem finite_etaleCohomology_constantSheaf
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] (hX : topologicalKrullDim X ≤ 1)
    (M : ModuleCat.{max (u + 1) r} Λ) [Module.Finite Λ M] (n : ℕ) (hn : 0 < n)
    (hM : ∀ m : M, n • m = 0) (hnp : n.Coprime (ringExpChar k) ∨ IsProper π) (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((constantSheaf X.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).obj M))
```

## Tag 0GJD, a lemma

[Tag 0GJD](https://stacks.math.columbia.edu/tag/0GJD) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforward.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforward.lean#L227). The attribute's comment: “granted Tag 03QP for sheaves of Λ-modules, as the hypothesis h03QP”.

> **Stacks Project, Tag 0GJD**, granted Tag 03QP for sheaves of `Λ`-modules as the hypothesis
> `h03QP`.
>
> Let `Λ` be a ring, let `f : X ⟶ Y` be a morphism of a big étale site whose underlying morphism
> of schemes is finite, and let `ℱ` be a sheaf of `Λ`-modules on the small étale site of `X`. If
> `H^q_étale(X, ℱ)` is a finite `Λ`-module, then so is `H^q_étale(Y, f_*ℱ)`.
>
> The hypothesis `h03QP` is the general statement of part (2) of Stacks 03QP for sheaves of
> `Λ`-modules: for *every* morphism of the big étale site with finite underlying morphism of
> schemes, *every* sheaf of `Λ`-modules on its source and *every* positive degree, the higher
> direct image vanishes. It is a different tag from the one being proved, it quantifies over all
> of its own inputs, and it is instantiated only inside the proof, at `f` and `ℱ`. Nothing about
> `H^q_étale(Y, f_*ℱ)` — the conclusion — is assumed.
>
> The remaining hypotheses of the source statement (`Λ` Noetherian, `k` algebraically closed,
> `X` and `Y` separated of finite type over `k` of dimension at most one) are not needed: the
> source's proof does not use them, and neither does this one.

```lean
theorem module_finite_cohomology_pushforward
    [∀ Z : B.Scheme,
      HasSheafify (SmallEtale.topology B Z.obj Z.property) (ModuleCat.{max (u + 1) w} Λ)]
    [∀ Z : B.Scheme, HasInjectiveResolutions
      (Sheaf (SmallEtale.topology B Z.obj Z.property) (ModuleCat.{max (u + 1) w} Λ))]
    [∀ (Z W : B.Scheme) (g : Z ⟶ W), (modulePushforward.{u, w} B Λ g).IsRightAdjoint]
    (h03QP : ∀ (Z W : B.Scheme) (g : Z ⟶ W), IsFinite (B.inclusion.map g) →
      ∀ (𝒢 : Sheaf (SmallEtale.topology B Z.obj Z.property) (ModuleCat.{max (u + 1) w} Λ))
        (q : ℕ), 0 < q → IsZero (((modulePushforward.{u, w} B Λ g).rightDerived q).obj 𝒢))
    (hf : IsFinite (B.inclusion.map f))
    (ℱ : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w} Λ))
    (q : ℕ)
    (hfin : Module.Finite Λ (((moduleGlobalSections.{u, w} B Λ X).rightDerived q).obj ℱ)) :
    Module.Finite Λ (((moduleGlobalSections.{u, w} B Λ Y).rightDerived q).obj
      ((modulePushforward.{u, w} B Λ f).obj ℱ))
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean#L179). The attribute's comment: “stated for an arbitrary ring Λ and an arbitrary finite morphism f of the big étale site; the source's further hypotheses (Λ Noetherian, k algebraically closed, X and Y separated of finite type over k of dimension at most one) are unused by its proof and dropped”.

> **Stacks Project, Tag 0GJD.** Let `Λ` be a ring, let `f : X ⟶ Y` be a morphism of a big étale
> site whose underlying morphism of schemes is finite, and let `ℱ` be a sheaf of `Λ`-modules on the
> small étale site of `X`. If `H^q_étale(X, ℱ)` is a finite `Λ`-module, then so is
> `H^q_étale(Y, f_*ℱ)`.
>
> The source states this for `Λ` Noetherian, `k` an algebraically closed field and `f` a finite
> morphism of separated schemes of finite type over `k` of dimension at most one. None of that is
> used by the source's proof, and none of it is assumed here: the source's statement is the special
> case in which those hypotheses hold. The proof is the source's: the higher direct images
> of `f` vanish (`isZero_rightDerived_modulePushforward_of_isIntegralHom`, Stacks 03QP), so the
> Leray spectral sequence collapses to `H^q_étale(X, ℱ) ≅ H^q_étale(Y, f_*ℱ)`
> (`moduleCohomologyPushforwardIso`, Stacks 0733), and finiteness transports along it.

```lean
theorem module_finite_cohomology_pushforward_of_isFinite [IsFinite (B.inclusion.map f)]
    (ℱ : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w r} Λ))
    (q : ℕ)
    (hfin : Module.Finite Λ
      (((moduleGlobalSections.{u, max w r} B Λ X).rightDerived q).obj ℱ)) :
    Module.Finite Λ (((moduleGlobalSections.{u, max w r} B Λ Y).rightDerived q).obj
      ((modulePushforward.{u, max w r} B Λ f).obj ℱ))
```

## Tag 0GJE, a lemma

[Tag 0GJE](https://stacks.math.columbia.edu/tag/0GJE) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpen.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpen.lean#L261). The attribute's comment: “granted 095L for Λ-module sheaves as h095L; closed part's cohomology as h0, hpos”.

> **Stacks Project, Tag 0GJE**, granted Tag 095L for sheaves of `Λ`-modules as the hypothesis
> `h095L`, and the cohomology of `i_*i^{-1}ℱ` as the hypotheses `h0` and `hpos`.
>
> Let `Λ` be a Noetherian ring, let `X` be a scheme, let `j : X' ⟶ X` be an open immersion and let
> `i : Z ⟶ X` be a closed immersion whose image is the complement of the image of `j`. Let `ℱ` be
> a sheaf of `Λ`-modules on `X_étale`. If `H^0_étale(X, i_*i^{-1}ℱ)` is a finite `Λ`-module and
> `H^q_étale(X, i_*i^{-1}ℱ) = 0` for `q > 0`, then for every `q`
>
>   `H^q_étale(X, ℱ)` is a finite `Λ`-module  ↔  `H^q_étale(X, j_!j^{-1}ℱ)` is a finite
>   `Λ`-module.
>
> The hypothesis `h095L` is the general statement of Tag 095L for sheaves of `Λ`-modules: for
> *every* scheme, *every* closed immersion into it, *every* open immersion onto the complement and
> *every* sheaf of `Λ`-modules, the localization short complex exists and is short exact. It is a
> different tag, it quantifies over all of its own inputs, it is instantiated only inside the
> proof, and it says nothing about cohomology or finiteness.
>
> The hypotheses `h0` and `hpos` are not a Stacks tag. They are the cohomological consequence of
> the geometric hypotheses of the source — `X` separated of finite type of dimension at most one
> over an algebraically closed field, `X'` dense, `ℱ` constructible — and are the part of Tag 0GJE
> this declaration does **not** prove; see the implementation notes of this file for the chain of
> four absent results they stand in for. They concern `i_*i^{-1}ℱ` only, and so are independent of
> the conclusion, which concerns `ℱ` and `j_!j^{-1}ℱ`.

```lean
theorem module_finite_cohomology_iff_extensionByZero
    {X Z X' : Scheme.{u}} (i : Z ⟶ X) (j : X' ⟶ X) [IsClosedImmersion i] [IsOpenImmersion j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ)
    (h095L : ∀ {W Z' U' : Scheme.{u}} (i' : Z' ⟶ W) (j' : U' ⟶ W) [IsClosedImmersion i']
        [IsOpenImmersion j'], Set.range j'.base = (Set.range i'.base)ᶜ →
      ∀ 𝒢 : Sheaf W.smallEtaleTopology (ModuleCat.{max (u + 1) w r} Λ),
        ∃ hz : (moduleExtensionByZeroAdj.{u, w, r} Λ j').counit.app 𝒢 ≫
            (moduleInverseImageDirectImageAdj.{u, w, r} Λ i').unit.app 𝒢 = 0,
          (openClosedModuleShortComplex.{u, w, r} Λ i' j' 𝒢 hz).ShortExact)
    (ℱ : Sheaf X.smallEtaleTopology (ModuleCat.{max (u + 1) w r} Λ))
    (h0 : Module.Finite Λ ((moduleEtaleCohomology.{u, w, r} Λ X 0).obj
      ((moduleDirectImage.{u, w, r} Λ i).obj ((moduleInverseImage.{u, w, r} Λ i).obj ℱ))))
    (hpos : ∀ q, 0 < q → IsZero ((moduleEtaleCohomology.{u, w, r} Λ X q).obj
      ((moduleDirectImage.{u, w, r} Λ i).obj ((moduleInverseImage.{u, w, r} Λ i).obj ℱ))))
    (q : ℕ) :
    Module.Finite Λ ((moduleEtaleCohomology.{u, w, r} Λ X q).obj ℱ) ↔
      Module.Finite Λ ((moduleEtaleCohomology.{u, w, r} Λ X q).obj
        ((moduleExtensionByZero.{u, w, r} Λ j).obj
          ((moduleRestriction.{u, w, r} Λ j).obj ℱ)))
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero_of_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpenCurve.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpenCurve.lean#L125).

> **Stacks Project, Tag 0GJE.** Let `Λ` be a Noetherian ring, `k` an algebraically closed
> field, `X` a separated scheme of finite type over `k` of dimension at most one, `ℱ` a
> constructible sheaf of `Λ`-modules on `X_étale`, and `j : X' ⟶ X` the inclusion of a dense open
> subscheme. Then `H^q_étale(X, ℱ)` is a finite `Λ`-module if and only if
> `H^q_étale(X, j_!j^{-1}ℱ)` is a finite `Λ`-module.

```lean
theorem module_finite_cohomology_iff_extensionByZero_of_dense
    (B : BigEtaleSite.{u}) (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ]
    {k : Type u} [Field k] [IsAlgClosed k]
    (X : B.Scheme) (p : X.obj ⟶ Spec (CommRingCat.of k))
    [IsSeparated p] [LocallyOfFiniteType p] [QuasiCompact p]
    (hdim : topologicalKrullDim X.obj ≤ 1)
    (ℱ : Sheaf X.obj.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ))
    (hℱ : IsConstructibleEtaleSiteModuleSheaf B X Λ ℱ)
    {X' : Scheme.{u}} (j : X' ⟶ X.obj) [IsOpenImmersion j]
    (hdense : Dense (Set.range j.base)) (q : ℕ) :
    Module.Finite Λ ((moduleEtaleCohomology.{u, r, r} Λ X.obj q).obj ℱ) ↔
      Module.Finite Λ ((moduleEtaleCohomology.{u, r, r} Λ X.obj q).obj
        ((moduleExtensionByZero.{u, r, r} Λ j).obj
          ((moduleRestriction.{u, r, r} Λ j).obj ℱ)))
```

## Tag 0GJF, a lemma

[Tag 0GJF](https://stacks.math.columbia.edu/tag/0GJF) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean#L86). The attribute's comment: “part (1): n prime to char(k)”.

> **Stacks Project, Tag 0GJF, part (1).** Let `Λ` be a Noetherian ring, let `M` be a finite
> `Λ`-module annihilated by an integer `n > 0`, let `k` be an algebraically closed field, let `X`
> be a separated scheme of finite type over `k` of dimension at most one, and let `j : U ⟶ X` be
> an open immersion. If `n` is prime to the characteristic of `k`, then `H^q_étale(X, j_!M̲)` is a
> finite `Λ`-module for every `q`.
>
> Here `X` is a scheme with a separated, locally of finite type and quasi-compact structure
> morphism `π : X ⟶ Spec k`, the dimension is the Krull dimension of the underlying space, `M̲` is
> the constant sheaf of `Λ`-modules on `U_étale`, `j_!` is extension by zero and `H^q` is the
> `q`-th right derived functor of global sections of sheaves of `Λ`-modules on `X_étale`. "Prime
> to the characteristic" is read with the exponential characteristic, so that it is no condition
> in characteristic zero.

```lean
theorem module_finite_cohomology_extensionByZero_of_coprime
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] (hX : topologicalKrullDim X ≤ 1)
    (M : ModuleCat.{max (u + 1) r} Λ) [Module.Finite Λ M] (n : ℕ) (hn : 0 < n)
    (hM : ∀ m : M, n • m = 0) (hnk : n.Coprime (ringExpChar k))
    {U : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((etaleModuleExtensionByZero.{u, r} Λ j).obj
        ((constantSheaf U.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).obj M)))
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean#L114). The attribute's comment: “part (2): X proper over k”.

> **Stacks Project, Tag 0GJF, part (2).** Let `Λ` be a Noetherian ring, let `M` be a finite
> `Λ`-module annihilated by an integer `n > 0`, let `k` be an algebraically closed field, let `X`
> be a separated scheme of finite type over `k` of dimension at most one, and let `j : U ⟶ X` be
> an open immersion. If `X` is proper over `k`, then `H^q_étale(X, j_!M̲)` is a finite
> `Λ`-module for every `q`.
>
> Here `X` is a scheme with a separated, locally of finite type and quasi-compact structure
> morphism `π : X ⟶ Spec k`, the dimension is the Krull dimension of the underlying space, `M̲` is
> the constant sheaf of `Λ`-modules on `U_étale`, `j_!` is extension by zero and `H^q` is the
> `q`-th right derived functor of global sections of sheaves of `Λ`-modules on `X_étale`.

```lean
theorem module_finite_cohomology_extensionByZero_of_isProper
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] [IsProper π]
    (hX : topologicalKrullDim X ≤ 1) (M : ModuleCat.{max (u + 1) r} Λ) [Module.Finite Λ M]
    (n : ℕ) (hn : 0 < n) (hM : ∀ m : M, n • m = 0)
    {U : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((etaleModuleExtensionByZero.{u, r} Λ j).obj
        ((constantSheaf U.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).obj M)))
```

## Tag 0GJG, a lemma

[Tag 0GJG](https://stacks.math.columbia.edu/tag/0GJG) in the Stacks Project.

**`Stacks.Cohomology.module_finite_cohomology_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FiniteCohomologyOfShortExact.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FiniteCohomologyOfShortExact.lean#L52).

> **Stacks Project, Tag 0GJG.** In a short exact sequence of coefficient sheaves,
> the middle sheaf has finite cohomology in degree `q` if both outer sheaves do.

```lean
public theorem module_finite_cohomology_of_shortExact
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ]
    [HasSheafify J (ModuleCat.{w} Λ)]
    [HasInjectiveResolutions (Sheaf J (ModuleCat.{w} Λ))]
    [HasGlobalSectionsFunctor J (ModuleCat.{w} Λ)]
    [(Sheaf.Γ J (ModuleCat.{w} Λ)).Additive]
    (S : ShortComplex (Sheaf J (ModuleCat.{w} Λ))) (hS : S.ShortExact)
    (q : ℕ)
    (h₁ : Module.Finite Λ (((Sheaf.Γ J (ModuleCat.{w} Λ)).rightDerived q).obj S.X₁))
    (h₃ : Module.Finite Λ (((Sheaf.Γ J (ModuleCat.{w} Λ)).rightDerived q).obj S.X₃)) :
    Module.Finite Λ (((Sheaf.Γ J (ModuleCat.{w} Λ)).rightDerived q).obj S.X₂)
```

## Tag 0GJH, a lemma

[Tag 0GJH](https://stacks.math.columbia.edu/tag/0GJH) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean#L300). The attribute's comment: “part (1): ℓ prime to char(k)”.

> **Stacks Project, Tag 0GJH, part (1).** Let `Λ` be a Noetherian ring, let `k` be an
> algebraically closed field, let `X` be a separated scheme of finite type over `k` of dimension at
> most one, let `j : U ⟶ X` be an open immersion with `U` connected, let `ℓ` be a prime number
> prime to the characteristic of `k`, let `n > 0` and let `𝒢` be a finite type, locally constant
> sheaf of `Λ`-modules on `U_étale` annihilated by `ℓ ^ n`. Then `H^q_étale(X, j_! 𝒢)` is a finite
> `Λ`-module for every `q`.
>
> "Separated of finite type over `k`" is `IsSeparated π`, `LocallyOfFiniteType π` and
> `QuasiCompact π` for the structure morphism `π : X ⟶ Spec k`, and "of dimension at most one" is
> `topologicalKrullDim X ≤ 1`. "Prime to the characteristic" is read with the exponential
> characteristic, so it is no condition in characteristic zero. `H^q_étale(X, -)` is the `q`-th
> right derived functor of global sections of sheaves of `Λ`-modules on `X_étale`. The connectedness
> of `U` is a hypothesis of the source and is kept; the proof does not use it.

```lean
theorem module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_coprime
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π]
    (hX : topologicalKrullDim X ≤ 1) {U : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j]
    [ConnectedSpace U] {ℓ n : ℕ} (hℓ : ℓ.Prime) (hn : 0 < n) (hℓk : ℓ.Coprime (ringExpChar k))
    (G : EtaleModules.{u, r} Λ U)
    (hG : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r}
      U.smallEtaleTopology Λ G)
    (hGn : ℓ ^ n • 𝟙 G = 0) (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((etaleModuleExtensionByZero.{u, r} Λ j).obj G))
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean#L325). The attribute's comment: “part (2): X proper over k”.

> **Stacks Project, Tag 0GJH, part (2).** Let `Λ` be a Noetherian ring, let `k` be an
> algebraically closed field, let `X` be a proper scheme over `k` of dimension at most one (proper
> implies separated and of finite type), let `j : U ⟶ X` be an open immersion with `U` connected,
> let `ℓ` be a prime number, let `n > 0` and let `𝒢` be a finite type, locally constant sheaf of
> `Λ`-modules on `U_étale` annihilated by `ℓ ^ n`. Then `H^q_étale(X, j_! 𝒢)` is a finite
> `Λ`-module for every `q`.
>
> The encoding is that of part (1),
> `module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_coprime`, with the
> coprimality hypothesis replaced by `IsProper π`.

```lean
theorem module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_isProper
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (π : X ⟶ Spec (.of k))
    [IsSeparated π] [LocallyOfFiniteType π] [QuasiCompact π] [IsProper π]
    (hX : topologicalKrullDim X ≤ 1) {U : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j]
    [ConnectedSpace U] {ℓ n : ℕ} (hℓ : ℓ.Prime) (hn : 0 < n) (G : EtaleModules.{u, r} Λ U)
    (hG : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r}
      U.smallEtaleTopology Λ G)
    (hGn : ℓ ^ n • 𝟙 G = 0) (q : ℕ) :
    Module.Finite Λ (((etaleModuleGlobalSections.{u, r} Λ X).rightDerived q).obj
      ((etaleModuleExtensionByZero.{u, r} Λ j).obj G))
```

## Tag 0GJI, a theorem

[Tag 0GJI](https://stacks.math.columbia.edu/tag/0GJI) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L585). The attribute's comment: “part (1): F torsion prime to char(k)”. References: SGA 5 VI (3.1), “partial”.

> **Stacks Project, Tag 0GJI, part (1) (Tag 0GJJ).** Let `Λ` be a Noetherian ring, `k` an
> algebraically closed field, `X` a separated scheme of finite type over `k` of dimension at most
> one, and `F` a constructible sheaf of `Λ`-modules on `X_étale` which is torsion prime to the
> characteristic of `k`. Then `H^q_étale(X, F)` is a finite `Λ`-module for every `q`.
>
> "Torsion prime to `char(k)`" is `Stacks.Torsion.IsPrimeToCharacteristicTorsion` of the underlying
> abelian sheaf at the exponential characteristic of `k`: every local section is, locally, killed by
> a positive integer prime to it. It implies that `F` is torsion, and in characteristic zero it is
> exactly that. Constructibility is `Stacks.EtaleCohomology.IsBigSiteConstructibleEtaleModule`
> (Tag 03RW (3), read on the small étale site of Tag 021B of a big étale site `B` containing `X`).

```lean
theorem module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion
    (F : EtaleModules.{u, r} Λ X.obj) (hc : IsBigSiteConstructibleEtaleModule B X Λ F)
    (ht : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.obj.smallEtaleTopology (ringExpChar k)
      ((etaleModuleForgetAb.{u, r} Λ X.obj).obj F)) (q : ℕ) :
    Module.Finite Λ
      (((Sheaf.Γ X.obj.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).rightDerived q).obj F)
```

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L603). The attribute's comment: “part (2): X proper”.

> **Stacks Project, Tag 0GJI, part (2) (Tag 0GJK).** Let `Λ` be a Noetherian ring, `k` an
> algebraically closed field, `X` a proper scheme over `k` of dimension at most one, and `F` a
> constructible sheaf of `Λ`-modules on `X_étale` which is torsion. Then `H^q_étale(X, F)` is a
> finite `Λ`-module for every `q`.
>
> Torsion is `Stacks.EtaleCohomology.IsTorsionEtaleModule`: every local section is, locally, killed
> by a positive integer.

```lean
theorem module_finite_etaleCohomology_of_isProper [IsProper π]
    (F : EtaleModules.{u, r} Λ X.obj) (hc : IsBigSiteConstructibleEtaleModule B X Λ F)
    (ht : IsTorsionEtaleModule.{u, r} Λ X.obj F) (q : ℕ) :
    Module.Finite Λ
      (((Sheaf.Γ X.obj.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).rightDerived q).obj F)
```

## Tag 0GJJ, an item

[Tag 0GJJ](https://stacks.math.columbia.edu/tag/0GJJ) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L585). References: SGA 5 VI (3.1), “partial”.

> **Stacks Project, Tag 0GJI, part (1) (Tag 0GJJ).** Let `Λ` be a Noetherian ring, `k` an
> algebraically closed field, `X` a separated scheme of finite type over `k` of dimension at most
> one, and `F` a constructible sheaf of `Λ`-modules on `X_étale` which is torsion prime to the
> characteristic of `k`. Then `H^q_étale(X, F)` is a finite `Λ`-module for every `q`.
>
> "Torsion prime to `char(k)`" is `Stacks.Torsion.IsPrimeToCharacteristicTorsion` of the underlying
> abelian sheaf at the exponential characteristic of `k`: every local section is, locally, killed by
> a positive integer prime to it. It implies that `F` is torsion, and in characteristic zero it is
> exactly that. Constructibility is `Stacks.EtaleCohomology.IsBigSiteConstructibleEtaleModule`
> (Tag 03RW (3), read on the small étale site of Tag 021B of a big étale site `B` containing `X`).

```lean
theorem module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion
    (F : EtaleModules.{u, r} Λ X.obj) (hc : IsBigSiteConstructibleEtaleModule B X Λ F)
    (ht : Stacks.Torsion.IsPrimeToCharacteristicTorsion X.obj.smallEtaleTopology (ringExpChar k)
      ((etaleModuleForgetAb.{u, r} Λ X.obj).obj F)) (q : ℕ) :
    Module.Finite Λ
      (((Sheaf.Γ X.obj.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).rightDerived q).obj F)
```

## Tag 0GJK, an item

[Tag 0GJK](https://stacks.math.columbia.edu/tag/0GJK) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L603).

> **Stacks Project, Tag 0GJI, part (2) (Tag 0GJK).** Let `Λ` be a Noetherian ring, `k` an
> algebraically closed field, `X` a proper scheme over `k` of dimension at most one, and `F` a
> constructible sheaf of `Λ`-modules on `X_étale` which is torsion. Then `H^q_étale(X, F)` is a
> finite `Λ`-module for every `q`.
>
> Torsion is `Stacks.EtaleCohomology.IsTorsionEtaleModule`: every local section is, locally, killed
> by a positive integer.

```lean
theorem module_finite_etaleCohomology_of_isProper [IsProper π]
    (F : EtaleModules.{u, r} Λ X.obj) (hc : IsBigSiteConstructibleEtaleModule B X Λ F)
    (ht : IsTorsionEtaleModule.{u, r} Λ X.obj F) (q : ℕ) :
    Module.Finite Λ
      (((Sheaf.Γ X.obj.smallEtaleTopology (ModuleCat.{max (u + 1) r} Λ)).rightDerived q).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.84, Tag 0GJB](https://stacks.math.columbia.edu/tag/0GJB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
