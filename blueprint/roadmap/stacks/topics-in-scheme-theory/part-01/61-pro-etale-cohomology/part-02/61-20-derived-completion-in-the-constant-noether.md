---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.derivedCompletion_eq_rlim_constantAdicTower, Stacks.ModuleSheaf.exists_leftAdjoint_isDerivedLimitWithProjections_derivedReductionTower, Stacks.ModuleSheaf.isDerivedComplete_iff_isDerivedLimitWithProjections_derivedReductionTower, MorphismOfTopoi.isDerivedComplete_constantDerivedPushforward, MorphismOfTopoi.constantDerivedCompletePullbackPushforwardAdjunction, MorphismOfTopoi.isIso_derivedCompletionComparison_constantDerivedPushforward, MorphismOfTopoi.isDerivedLimit_constantAdicTower_constantDerivedPushforward, MorphismOfTopoi.isDerivedLimit_constantAdicTower_constantDerivedCompletePullback
statement: formalized
proof: formalized
---

# 61.20 Derived completion in the constant Noetherian case

Section 61.20 of the Stacks Project, [Tag 099L](https://stacks.math.columbia.edu/tag/099L). 2 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 099M, a lemma

[Tag 099M](https://stacks.math.columbia.edu/tag/099M) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCompletion_eq_rlim_constantAdicTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantNoetherianCompletion.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantNoetherianCompletion.lean#L466).

> Let `𝒞` be a site, let `Λ` be a Noetherian ring and let `I ⊂ Λ` be an ideal. The left adjoint
> `K ↦ K^∧` of the inclusion of the objects of `D(𝒞, Λ)` derived complete along `IΛ̲`
> ([Stacks, Tag 099F]) sends `K` to `R lim (K ⊗^𝐋_Λ (Λ/Iⁿ)̲)`; and `K` is derived complete exactly
> when `K = R lim (K ⊗^𝐋_Λ (Λ/Iⁿ)̲)`.

```lean
theorem derivedCompletion_eq_rlim_constantAdicTower
    (K : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O))) :
    IsDerivedLimit (constantAdicTower J Λ I K)
        ((derivedCompletion (constant J Λ) (constantIdealSheaf J Λ I)).obj K) ∧
      (IsDerivedComplete.{u, u, u, u} (constant J Λ) (constantIdealSheaf J Λ I) K ↔
        IsDerivedLimit (constantAdicTower J Λ I K) K)
```

**`Stacks.ModuleSheaf.exists_leftAdjoint_isDerivedLimitWithProjections_derivedReductionTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/DerivedTensorModuleSheaf/DerivedCompletion.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/DerivedTensorModuleSheaf/DerivedCompletion.lean#L84). The attribute's comment: “the left adjoint is `K ↦ R lim (K ⊗^L Λ/Iⁿ)`”.

> **The derived completion functor in the constant Noetherian case.** The inclusion of the
> derived complete objects of `D(C, Λ)` has a left adjoint `K ↦ K^∧`, where `K^∧` is a derived limit
> `R lim (K ⊗_Λ^L \underline{Λ/Iⁿ})` with projections natural in `K`, whose composites with the
> unit `K → K^∧` are the reductions `K → K ⊗_Λ^L \underline{Λ/Iⁿ}`.

```lean
theorem exists_leftAdjoint_isDerivedLimitWithProjections_derivedReductionTower :
    let P : ObjectProperty (DerivedCategory (Sheaf J (ModuleCat.{w} Λ))) :=
      fun K ↦ IsDerivedComplete I K
    ∃ (Lf : DerivedCategory (Sheaf J (ModuleCat.{w} Λ)) ⥤ P.FullSubcategory) (adj : Lf ⊣ P.ι)
      (π : ∀ n : ℕ, Lf ⋙ P.ι ⟶
        derivedReductionTowerFunctor J Λ I ⋙ (evaluation ℕᵒᵖ _).obj ⟨n⟩),
      (∀ K, IsDerivedLimitWithProjections (derivedReductionTower J Λ I K) ((Lf ⋙ P.ι).obj K)
        fun n ↦ (π n).app K) ∧
      ∀ K (n : ℕ), adj.unit.app K ≫ (π n).app K = (derivedReductionMap J Λ I K).app ⟨n⟩
```

**`Stacks.ModuleSheaf.isDerivedComplete_iff_isDerivedLimitWithProjections_derivedReductionTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/DerivedTensorModuleSheaf/DerivedCompletion.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/DerivedTensorModuleSheaf/DerivedCompletion.lean#L101). The attribute's comment: “in particular: `K` is complete iff `K = R lim (K ⊗^L Λ/Iⁿ)`”.

> **`K` is derived complete if and only if `K = R lim (K ⊗_Λ^L \underline{Λ/Iⁿ})`**, i.e.
> `K`, with the reductions `K → K ⊗_Λ^L \underline{Λ/Iⁿ}`, is a derived limit of the reductions.

```lean
theorem isDerivedComplete_iff_isDerivedLimitWithProjections_derivedReductionTower
    (K : DerivedCategory (Sheaf J (ModuleCat.{w} Λ))) :
    IsDerivedComplete I K ↔ IsDerivedLimitWithProjections (derivedReductionTower J Λ I K) K
      fun n ↦ (derivedReductionMap J Λ I K).app ⟨n⟩
```

## Tag 099N, a lemma

[Tag 099N](https://stacks.math.columbia.edu/tag/099N) in the Stacks Project.

**`MorphismOfTopoi.isDerivedComplete_constantDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantPushforwardCompletion.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantPushforwardCompletion.lean#L350). The attribute's comment: “(1)”.

> **`Rf_*` preserves derived completeness.** Let `Λ` be a Noetherian ring, `I ⊂ Λ` an ideal and
> `f : Sh(𝒟) ⟶ Sh(𝒞)` a morphism of topoi. If `E` in `D(𝒟, Λ)` is derived complete along `IΛ̲`, so
> is `Rf_*E` in `D(𝒞, Λ)`.

```lean
theorem isDerivedComplete_constantDerivedPushforward
    (E : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.constant K Λ).O)))
    (hE : RingedSite.IsDerivedComplete.{u, u, u, u} (RingedSite.constant K Λ)
      (RingedSite.constantIdealSheaf K Λ I) E) :
    RingedSite.IsDerivedComplete.{u, u, u, u} (RingedSite.constant J Λ)
      (RingedSite.constantIdealSheaf J Λ I) ((constantDerivedPushforward Λ f).obj E)
```

**`MorphismOfTopoi.constantDerivedCompletePullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean#L126). The attribute's comment: “(2)”.

> **[Stacks, Tag 099N], part (2).** Let `Λ` be a Noetherian ring, `I ⊂ Λ` an ideal and
> `f : Sh(𝒟) ⟶ Sh(𝒞)` a morphism of topoi. The functor `Rf_* : D_comp(𝒟, Λ) ⥤ D_comp(𝒞, Λ)` has
> a left adjoint `Lf^*_comp : D_comp(𝒞, Λ) ⥤ D_comp(𝒟, Λ)`, which is `Lf^*` followed by derived
> completion (`MorphismOfTopoi.constantDerivedCompletePullback_comp_ι`).

```lean
def constantDerivedCompletePullbackPushforwardAdjunction :
    constantDerivedCompletePullback Λ I f ⊣ constantDerivedCompletePushforward Λ I f
```

**`MorphismOfTopoi.isIso_derivedCompletionComparison_constantDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean#L134). The attribute's comment: “(3)”.

> **[Stacks, Tag 099N], part (3).** Let `Λ` be a Noetherian ring, `I ⊂ Λ` an ideal and
> `f : Sh(𝒟) ⟶ Sh(𝒞)` a morphism of topoi. `Rf_*` commutes with derived completion: the canonical
> comparison `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`, natural in `K` in `D(𝒟, Λ)`, is an isomorphism.

```lean
theorem isIso_derivedCompletionComparison_constantDerivedPushforward :
    IsIso (RingedSite.derivedCompletionComparison (RingedSite.constantIdealSheaf K Λ I)
      (RingedSite.constantIdealSheaf J Λ I) (constantDerivedPushforward Λ f)
      (fun E hE => isDerivedComplete_constantDerivedPushforward Λ f I E hE))
```

**`MorphismOfTopoi.isDerivedLimit_constantAdicTower_constantDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean#L146). The attribute's comment: “(4)”.

> **[Stacks, Tag 099N], part (4).** Let `Λ` be a Noetherian ring, `I ⊂ Λ` an ideal and
> `f : Sh(𝒟) ⟶ Sh(𝒞)` a morphism of topoi. For `K` in `D_comp(𝒟, Λ)`,
> `Rf_*K = R lim Rf_*(K ⊗^𝐋_Λ (Λ/Iⁿ)̲)`: `Rf_*K` is a derived limit of the tower
> `n ↦ Rf_*(K ⊗^𝐋_Λ (Λ/Iⁿ)̲)`.

```lean
theorem isDerivedLimit_constantAdicTower_constantDerivedPushforward
    (E : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.constant K Λ).O)))
    (hE : RingedSite.IsDerivedComplete.{u, u, u, u} (RingedSite.constant K Λ)
      (RingedSite.constantIdealSheaf K Λ I) E) :
    IsDerivedLimit (RingedSite.constantAdicTower K Λ I E ⋙ constantDerivedPushforward Λ f)
      ((constantDerivedPushforward Λ f).obj E)
```

**`MorphismOfTopoi.isDerivedLimit_constantAdicTower_constantDerivedCompletePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/ConstantToposCompletion.lean#L178). The attribute's comment: “(5)”.

> **[Stacks, Tag 099N], part (5).** Let `Λ` be a Noetherian ring, `I ⊂ Λ` an ideal and
> `f : Sh(𝒟) ⟶ Sh(𝒞)` a morphism of topoi. For `M` in `D_comp(𝒞, Λ)`,
> `Lf^*_comp M = R lim Lf^*(M ⊗^𝐋_Λ (Λ/Iⁿ)̲)`: `Lf^*_comp M` is a derived limit of the tower
> `n ↦ Lf^*(M ⊗^𝐋_Λ (Λ/Iⁿ)̲)`.

```lean
theorem isDerivedLimit_constantAdicTower_constantDerivedCompletePullback
    (M : ObjectProperty.FullSubcategory (RingedSite.IsDerivedComplete.{u, u, u, u}
      (RingedTopos.constant J Λ).toRingedSite (RingedSite.constantIdealSheaf J Λ I))) :
    IsDerivedLimit (RingedSite.constantAdicTower J Λ I M.1 ⋙ constantDerivedPullback Λ f)
      ((constantDerivedCompletePullback Λ I f).obj M).1
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_derivedPushforward_adicReductionTower_of_proIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardAdicLimit.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardAdicLimit.lean#L167). The attribute's comment: “part (4), for an arbitrary ringed site and `ℐ'` the ideal sheaf generated by finitely many global sections, in place of the source's constant Noetherian coefficients `(𝒞, Λ)`, and with the tower of adic quotients taken on the source site. ASSUMED: the pro-isomorphism `a` in `D(𝒪')` of the dual Koszul tower with the tower `n ↦ 𝒪'/ℐ'ⁿ⁺¹`, which is the one hypothesis of this library's form of [Stacks, Tag 099M] and which the source derives from [Stacks, Tag 0921] over a Noetherian coefficient ring; and, carried from [Stacks, Tag 0A0E], the instance `HasCoproduct` for the Koszul system, which is automatic in the source”.

> **Part (4) of [Stacks, Tag 099N], granted the pro-isomorphism of towers of
> [Stacks, Tag 099M].** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed sites, let
> `g_1, …, g_r` be global sections of `𝒪'` and let `ℐ' = (g_1, …, g_r)`. Suppose the tower
> `n ↦ Kₙ^∨` of duals of the Koszul complexes on the powers of the `g_i` is isomorphic, as a
> pro-object of `D(𝒪')`, to the tower `n ↦ 𝒪'/ℐ'ⁿ⁺¹`. Then for every `K` in `D(𝒪')` derived
> complete along `ℐ'`,
>
> `Rf_*K = R lim Rf_*(K ⊗^𝐋_{𝒪'} 𝒪'/ℐ'ⁿ⁺¹)`.
>
> This is the source's proof: Tag 099M in criterion form,
> `isDerivedComplete_iff_isDerivedLimit_adicReductionTower_of_proIso`, exhibits `K` itself as a
> derived limit of the tower of its adic reductions, and [Stacks, Tag 0A07],
> `Stacks.Cohomology.DerivedPushforwardOnRingedTopoi.isDerivedLimit_map_derivedPushforward`,
> carries a derived limit along `Rf_*`.

```lean
theorem isDerivedLimit_derivedPushforward_adicReductionTower_of_proIso
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct ((koszulPowerSystem X g ⋙ DerivedCategory.Q).obj)]
    (hK : IsDerivedComplete.{u, u, u, u} X (idealOfGlobalSections X g) K)
    (a : InverseSequence.ProIso (koszulPowerDualSystem X g)
      (adicQuotientDerivedTower X (idealOfGlobalSections X g))) :
    IsDerivedLimit (adicReductionTower X (idealOfGlobalSections X g) K ⋙
        derivedPushforward.{u} f.toRingedToposSiteHom)
      ((derivedPushforward.{u} f.toRingedToposSiteHom).obj K)
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_adicReductionTower_derivedCompletePullback_of_proIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardAdicLimit.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardAdicLimit.lean#L207). The attribute's comment: “part (5), at the generality of part (4) — an arbitrary ringed site, `ℐ'` generated by finitely many global sections, and the tower of adic quotients formed on the source site, where the source's `n ↦ Lf^*(M ⊗^𝐋 Λ/Iⁿ)` becomes `n ↦ Lf^*M ⊗^𝐋_{𝒪'} 𝒪'/ℐ'ⁿ⁺¹`. ASSUMED: exactly what part (4) assumes — the pro-isomorphism `a` and the `HasCoproduct` instance — and nothing else”.

> **Part (5) of [Stacks, Tag 099N], granted the pro-isomorphism of towers of
> [Stacks, Tag 099M].** In the situation of
> `isDerivedLimit_derivedPushforward_adicReductionTower_of_proIso`, and for an arbitrary sheaf of
> ideals `ℐ ⊂ 𝒪` on the base, the completed pullback `Lf^*_comp M` of
> `AlgebraicGeometry.RingedSite.derivedCompletePullback` — that is `Lf^*` followed by derived
> completion along `ℐ'` — of an object `M` of `D_comp(𝒪, ℐ)` satisfies
>
> `Lf^*_comp M = R lim (Lf^*M ⊗^𝐋_{𝒪'} 𝒪'/ℐ'ⁿ⁺¹)`.
>
> The source writes the tower as `n ↦ Lf^*(M ⊗^𝐋 Λ/Iⁿ)`, which with its constant coefficients is
> the same system: `Lf^*` commutes with `⊗^𝐋` by [Stacks, Tag 07A4] and fixes the constant sheaf
> `Λ/Iⁿ`. Here the reductions are formed on the source site to begin with, so what is proved is
> Tag 099M in formula form,
> `isDerivedLimit_adicReductionTower_completionFunctor_of_proIso`, at the object `Lf^*M`, whose
> completion is `Lf^*_comp M` by definition. The completion there is named by the Čech functor of
> [Stacks, Tag 099B] and here by the reflector of [Stacks, Tag 099F]; the two are identified by
> `AlgebraicGeometry.RingedSite.exists_iso_derivedCompletion_completionFunctor`, and the derived
> limit crosses that isomorphism by
> `CategoryTheory.Pretriangulated.IsDerivedLimit.of_objIso`.

```lean
theorem isDerivedLimit_adicReductionTower_derivedCompletePullback_of_proIso
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    [HasCoproduct ((koszulPowerSystem X g ⋙ DerivedCategory.Q).obj)]
    (M : ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} Y I))
    (a : InverseSequence.ProIso (koszulPowerDualSystem X g)
      (adicQuotientDerivedTower X (idealOfGlobalSections X g))) :
    letI := isRightAdjoint_ι_isDerivedComplete_idealOfGlobalSections X g
    IsDerivedLimit
      (adicReductionTower X (idealOfGlobalSections X g)
        ((derivedPullback.{u} f.toRingedToposSiteHom).obj M.1))
      ((derivedCompletePullback f I (idealOfGlobalSections X g)).obj M).1
```

**`AlgebraicGeometry.RingedSite.derivedCompletePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L246). The attribute's comment: “part (1), for an arbitrary ringed site in place of the source's constant Noetherian coefficients `(𝒞, Λ)`”.

> **The first statement of [Stacks, Tag 099K], for a morphism of ringed sites.** `Rf_*` as a
> functor `D_comp(𝒪', ℐ') ⥤ D_comp(𝒪, ℐ)`: the derived direct image of a derived-complete object is
> derived complete, by [Stacks, Tag 099J]. The tag is registered for a morphism of ringed topoi, on
> `AlgebraicGeometry.RingedToposHom.isDerivedComplete_derivedPushforward`.
>
> This is also part (1) of [Stacks, Tag 099N], stated for an arbitrary ringed site rather than for
> the constant Noetherian coefficients `(𝒞, Λ)` of that tag. The identification of `D(𝒞, Λ)` with
> `D(𝒪)` for the constant sheaf of rings `Λ` is not formalized in this library, so what is proved
> is the statement at a generality containing the source's, not a composite with that
> identification.

```lean
def derivedCompletePushforward :
    ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I') ⥤
      ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} Y I)
```

**`AlgebraicGeometry.RingedSite.derivedCompletePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L268). The attribute's comment: “part (2), the functor `Lf^*_comp`, for an arbitrary ringed site in place of the source's constant Noetherian coefficients, and for every `ℐ'` whose derived-complete objects are reflective in `D(𝒪')` — which [Stacks, Tag 099F] gives for an ideal sheaf of finite type”.

> **The left adjoint of [Stacks, Tag 099K], for a reflective `D_comp(𝒪', ℐ')`.** `Lf^*_comp`,
> that is `Lf^*` followed by derived completion, as a functor `D_comp(𝒪, ℐ) ⥤ D_comp(𝒪', ℐ')`.
>
> The source reaches the derived completion functor from "`ℐ'` of finite type" through
> [Stacks, Tag 099F]. What this construction consumes is that conclusion alone — that the
> inclusion of the derived-complete objects has a left adjoint — so that is what the statement
> asks for; for an `ℐ'` of finite type the instance of [Stacks, Tag 099F],
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete`, supplies it. This is also
> part (2) of [Stacks, Tag 099N], at the generality of part (1).

```lean
def derivedCompletePullback :
    ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} Y I) ⥤
      ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I')
```

**`AlgebraicGeometry.RingedSite.derivedCompletePullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L295). The attribute's comment: “part (2), the adjunction, at the generality named on `derivedCompletePullback`; parts (4) and (5) are in `PushforwardAdicLimit.lean`”.

> **The adjunction of [Stacks, Tag 099K], for a reflective `D_comp(𝒪', ℐ')`.** On the
> derived-complete objects, `Lf^*` followed by derived completion is left adjoint to `Rf_*`. This
> is the source's chain `Hom(K, Rf_*M) = Hom(Lf^*K, M) = Hom(Lf^*_comp K, M)`: the composite of
> the adjunction `Lf^* ⊣ Rf_*` of [Stacks, Tag 07A6] with the reflector adjunction of
> [Stacks, Tag 099F], restricted along the fully faithful inclusion of `D_comp(𝒪, ℐ)` into
> `D(𝒪)`.
>
> The `@[stacks 099K]` registration of this second statement is on the statement for a morphism
> of ringed topoi, `AlgebraicGeometry.RingedToposHom.derivedCompletePullbackPushforwardAdjunction`
> of `PushforwardCompletionTopos.lean`.
>
> This is also part (2) of [Stacks, Tag 099N]. Parts (4) and (5) of that tag, the formulas
> `Rf_*K = R lim Rf_*(K ⊗^L Λ/Iⁿ)` and `Lf^*_comp M = R lim Lf^*(M ⊗^L Λ/Iⁿ)`, are proved in
> `PushforwardAdicLimit.lean` of this directory, as
> `AlgebraicGeometry.RingedSite.isDerivedLimit_derivedPushforward_adicReductionTower_of_proIso`
> and
> `AlgebraicGeometry.RingedSite.isDerivedLimit_adicReductionTower_derivedCompletePullback_of_proIso`;
> each carries the single hypothesis of this library's form of [Stacks, Tag 099M], a
> pro-isomorphism of the dual Koszul tower with the tower of adic quotients.

```lean
def derivedCompletePullbackPushforwardAdjunction :
    derivedCompletePullback f I I' ⊣ derivedCompletePushforward f I I' hI
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L440). The attribute's comment: “part (3), for a derived-complete object and an arbitrary ringed site”.

> **[Stacks, Tag 0A0G] at a derived-complete object.** For `K` in `D_comp(𝒪', ℐ')` the
> canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible, so `Rf_*(K^∧) = Rf_*K = (Rf_*K)^∧`: the
> unit `K ⟶ K^∧` is invertible on a derived-complete `K`.
>
> The general case of Tag 0A0G, for an arbitrary `K`, is proved at the tag's own data — a sheaf
> of ideals `ℐ ⊂ 𝒪` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X` — by
> `isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType` of
> `PushforwardCommutesCompletionLocalToGlobal.lean`. Equation 52.7.0.1 of [Stacks, Tag 0A0I], in
> its own setting of a morphism of schemes and a quasi-coherent sheaf of ideals of finite type, is
> `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf` of
> `PushforwardCommutesCompletionFiniteType.lean`. The statement here is the case of an independent
> pair of sheaves of ideals subject only to the relation of [Stacks, Tag 099J], at a
> derived-complete object. It also carries part (3) of
> [Stacks, Tag 099N], with the restrictions named on `derivedCompletePushforward`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_isDerivedComplete
    {K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : IsDerivedComplete.{u, u, u, u} X I' K) :
    IsIso ((derivedCompletionPushforwardComparison f I I' hI).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.20, Tag 099L](https://stacks.math.columbia.edu/tag/099L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
