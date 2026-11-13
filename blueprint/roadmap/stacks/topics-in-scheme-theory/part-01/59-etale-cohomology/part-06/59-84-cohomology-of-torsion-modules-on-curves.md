---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_coprime, Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_isProper, Stacks.EtaleCohomology.TorsionModules.finite_etaleCohomology_constantSheaf, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward_of_isFinite, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero_of_dense, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_coprime, Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isProper, Stacks.Cohomology.module_finite_cohomology_of_shortExact
statement: formalized
proof: formalized
---

# 59.84 Cohomology of torsion modules on curves

Section 59.84 of the Stacks Project, [Tag 0GJB](https://stacks.math.columbia.edu/tag/0GJB). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GJC, a lemma

[Tag 0GJC](https://stacks.math.columbia.edu/tag/0GJC) in the Stacks Project.

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean#L103). The attribute's comment: “part (1): n prime to char(k)”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_constantSheaf_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveConstantCoefficientsFinite.lean#L126). The attribute's comment: “part (2): X proper over k”.

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

**`Stacks.EtaleCohomology.TorsionModules.finite_etaleCohomology_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveTorsionStatementsHold.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/CurveTorsionStatementsHold.lean#L62). The attribute's comment: “both parts: n prime to char(k), or X proper”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_pushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean#L180). The attribute's comment: “stated for an arbitrary ring Λ and an arbitrary finite morphism f of the big étale site, for sheaves of Λ-modules on the small étale sites of Tag 021B; the source's further hypotheses (Λ Noetherian, k algebraically closed, X and Y separated of finite type over k of dimension at most one) are unused by its proof and dropped”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_iff_extensionByZero_of_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpenCurve.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/RestrictToDenseOpenCurve.lean#L132).

> **Stacks Project, Tag 0GJE.** Let `Λ` be a Noetherian ring, `k` an algebraically closed
> field, `X` a separated scheme of finite type over `k` of dimension at most one, `ℱ` a
> constructible sheaf of `Λ`-modules on `X_étale`, and `j : X' ⟶ X` the inclusion of a dense open
> subscheme. Then `H^q_étale(X, ℱ)` is a finite `Λ`-module if and only if
> `H^q_étale(X, j_!j^{-1}ℱ)` is a finite `Λ`-module.
>
> "Separated of finite type over `k`" is `IsSeparated p`, `LocallyOfFiniteType p` and
> `QuasiCompact p` for the structure morphism `p`, "of dimension at most one" is
> `topologicalKrullDim X ≤ 1`, and constructibility is `IsConstructibleEtaleSiteModuleSheaf`
> (Tag 03RW, read on the small étale site). The proof discharges the localization sequence
> (`openClosedModuleShortComplex_shortExact`) and the cohomology of the closed part, and applies
> `module_finite_cohomology_iff_extensionByZero`.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean#L85). The attribute's comment: “part (1): n prime to char(k)”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FiniteCohomologyUnconditional.lean#L113). The attribute's comment: “part (2): X proper over k”.

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

**`Stacks.Cohomology.module_finite_cohomology_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FiniteCohomologyOfShortExact.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FiniteCohomologyOfShortExact.lean#L52).

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_coprime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean#L300). The attribute's comment: “part (1): ℓ prime to char(k)”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_cohomology_extensionByZero_of_isFiniteTypeLocallyConstant_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/LocallyConstantCoefficients/FiniteCohomologyExtensionByZero.lean#L325). The attribute's comment: “part (2): X proper over k”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 585](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L585). The attribute's comment: “part (1): F torsion prime to char(k)”. References: SGA 5 VI (3.1), “partial”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L603). The attribute's comment: “part (2): X proper”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isPrimeToCharacteristicTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 585](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L585). References: SGA 5 VI (3.1), “partial”.

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

**`Stacks.EtaleCohomology.TorsionModules.module_finite_etaleCohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModules/ConstructibleCurveCohomology.lean#L603).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
