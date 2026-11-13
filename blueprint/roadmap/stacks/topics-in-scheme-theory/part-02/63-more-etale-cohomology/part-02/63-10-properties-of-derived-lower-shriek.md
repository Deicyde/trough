---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.preservesColimitsOfShape_derivedLowerShriekUnbounded, Stacks.EtaleCohomology.preservesColimit_derivedLowerShriek_of_isGE, Stacks.EtaleCohomology.DerivedUpperShriek.preservesColimit_derivedLowerShriek_of_isGE, Stacks.EtaleCohomology.DerivedUpperShriek.preservesColimitsOfShape_derivedLowerShriek, Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.preservesColimitsOfShape_derivedLowerShriek, Stacks.Cohomology.Localization.preservesColimitsOfSize_derivedExtensionByZero, Stacks.EtaleCohomology.exists_bounded_derivedLowerShriek, AlgebraicGeometry.SmallEtale.nonempty_derivedLowerShriek_iso_fShriek
statement: formalized
proof: formalized
---

# 63.10 Properties of derived lower shriek

Section 63.10 of the Stacks Project, [Tag 0G28](https://stacks.math.columbia.edu/tag/0G28). 9 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G29, a lemma

[Tag 0G29](https://stacks.math.columbia.edu/tag/0G29) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesColimitsOfShape_derivedLowerShriekUnbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean#L115). The attribute's comment: “(2) for Λ a torsion ring in any universe, on D(X\_étale, Λ): Rf\_! = Rf̄\_* ∘ j\_! commutes with direct sums. The base declarations of (2) assume the proper case (Tag 0F0D); here it is proved”.

> **[Stacks, Tag 0G29] (2).** Let `Λ` be a torsion ring and let
> `Rf_! = Rf̄_* ∘ Rj_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` be the derived lower shriek of a
> compactification `f = f̄ ∘ j`. Then `Rf_!` commutes with direct sums.

```lean
theorem preservesColimitsOfShape_derivedLowerShriekUnbounded
    (j : CompactificationOf (Over.mk f)) (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0)
    (I : Type (max (u + 1) r)) :
    PreservesColimitsOfShape (Discrete I) (derivedLowerShriekUnbounded.{u, r} f j Λ)
```

**`Stacks.EtaleCohomology.preservesColimit_derivedLowerShriek_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean#L141). The attribute's comment: “(1) Rf\_!(⨁ K\_i) = ⨁ Rf\_! K\_i for a family of D⁺(X\_étale, Λ) with common lower bound a, Λ a ring in any universe; the base declaration of (1) assumes Tags 08FJ, 03S5 and 0GIW, here they are proved”.

> **[Stacks, Tag 0G29] (1).** Let `f : X ⟶ Y` be a finite type separated morphism of
> quasi-compact and quasi-separated schemes, let `Λ` be a ring, in any universe, and let
> `Rf_! = R(fbar)_* ∘ j_!` be the derived lower shriek of a compactification `j` of `f`, on bounded
> below derived categories. Let `K : I → D⁺(X_étale, Λ)` be a family of objects and `a : ℤ` such
> that `H^n(K i) = 0` for `n < a` and all `i`. Then `Rf_!(⨁ i, K i) = ⨁ i, Rf_!(K i)`.
>
> The source states this for `K i` in `D⁺_tors(X_étale, Λ)`; no torsion hypothesis is used, so it is
> stated for all of `D⁺(X_étale, Λ)`. The three inputs of the source's proof are proved: the
> adjunction `j_! ⊣ j^{-1}` ([Stacks, Tag 08FJ],
> `Stacks.EtaleCohomology.etaleModuleDerivedExtensionByZeroAdj`), that `j_!` preserves the lower
> bound (a right derived functor does), and [Stacks, Tag 0GIW] for the proper morphism `fbar`
> (`Stacks.EtaleCohomology.preservesColimit_etaleModuleDerivedDirectImage_of_isGE`, whose input
> [Stacks, Tag 09Z1] is
> `preservesColimitsOfShape_discrete_rightDerived_etaleModuleDirectImage_univ`).

```lean
theorem preservesColimit_derivedLowerShriek_of_isGE {X Y : Scheme.{u}} {f : X ⟶ Y}
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (j : CompactificationOf (Over.mk f)) {I : Type (max (u + 1) r)}
    (K : I → DerivedCategory.Plus (EtaleModules.{u, r} Λ X)) (a : ℤ) (hK : ∀ i, (K i).IsGE a) :
    PreservesColimit (Discrete.functor K) (derivedLowerShriek.{u, r} f j Λ)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.preservesColimit_derivedLowerShriek_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean#L127). The attribute's comment: “(1) Rf\_!(⨁ K\_i) = ⨁ Rf\_! K\_i for a family with common lower bound a”.

> **[Stacks, Tag 0G29] (1).** Let `f : X ⟶ Y` be a finite type separated morphism of
> quasi-compact and quasi-separated schemes, let `Λ` be a ring, let `j` be a compactification of
> `f` and let `Rf_! = R(fbar)_* ∘ j_!` be the derived lower shriek it determines.  Let
> `K : I → D⁺(X_étale, Λ)` be a family of objects and let `a : ℤ` be such that `H^n(K i) = 0`
> for `n < a` and all `i`, that is `(K i).IsGE a`.  Then
> `Rf_!(⨁ i, K i) = ⨁ i, Rf_!(K i)`.
>
> The three inputs are the ones the source cites.  `adjImmersion` is the adjunction
> `j_! ⊣ j^{-1}` of [Stacks, Tag 08FJ]; from it, and not from any further hypothesis, `j_!`
> commutes with the direct sum.  `hShriekGE` is exactness of extension by zero,
> [Stacks, Tag 03S5], in the form that `j_!` preserves the lower bound, so that
> [Stacks, Tag 0GIW] applies to the family `j_! (K i)`.  `hProper` is [Stacks, Tag 0GIW] itself
> for the proper — hence quasi-compact and quasi-separated — morphism `fbar = j.toBase`.

```lean
theorem preservesColimit_derivedLowerShriek_of_isGE {X Y : Scheme.{u}} {f : X ⟶ Y}
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ]
    {I : Type w} (K : I → DerivedCategory.Plus (EtaleModules.{u, r} Λ X))
    (a : ℤ) (hK : ∀ i, (K i).IsGE a)
    {Uj : DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X)}
    (adjImmersion : etaleModuleDerivedExtensionByZero.{u, r} Λ j.immersion ⊣ Uj)
    (hShriekGE : ∀ (b : ℤ) (M : DerivedCategory.Plus (EtaleModules.{u, r} Λ X)), M.IsGE b →
      ((etaleModuleDerivedExtensionByZero.{u, r} Λ j.immersion).obj M).IsGE b)
    (hProper : ∀ L : I → DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space),
      (∀ i, (L i).IsGE a) →
      PreservesColimit (Discrete.functor L)
        (etaleModuleDerivedDirectImage.{u, r} Λ j.toBase)) :
    PreservesColimit (Discrete.functor K) (derivedLowerShriek.{u, r} f j Λ)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.preservesColimitsOfShape_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean#L171). The attribute's comment: “(2) for Λ torsion, Rf\_! = R(fbar)\_* ∘ j\_! commutes with direct sums”.

> **[Stacks, Tag 0G29] (2).** Let `Λ` be a torsion ring and let
> `Rf_! = R(fbar)_* ∘ j_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` be the derived lower shriek of a
> compactification `f = fbar ∘ j` of a finite type separated morphism of quasi-compact and
> quasi-separated schemes.  Then `Rf_!` commutes with direct sums of every shape.
>
> The two inputs are the ones the source cites: `adjImmersion` is the adjunction `j_! ⊣ j^{-1}`
> of [Stacks, Tag 08FJ] for the open immersion `j`, and `hProper` is [Stacks, Tag 0F0D], that
> `R(fbar)_*` commutes with direct sums for a torsion coefficient ring.  That a left adjoint
> commutes with direct sums, and that the composite therefore does, is proved.

```lean
theorem preservesColimitsOfShape_derivedLowerShriek {DU : Type u₁} [Category.{v₁} DU]
    {DX : Type u₂} [Category.{v₂} DX] {DY : Type u₃} [Category.{v₃} DY]
    {shriek : DU ⥤ DX} {Uj : DX ⥤ DU} (adjImmersion : shriek ⊣ Uj)
    (pushforwardFbar : DX ⥤ DY) (I : Type w)
    (hProper : PreservesColimitsOfShape (Discrete I) pushforwardFbar) :
    PreservesColimitsOfShape (Discrete I) (shriek ⋙ pushforwardFbar)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.preservesColimitsOfShape_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/DirectSums.lean#L193). The attribute's comment: “(2) for a CompactificationData: Rf\_! commutes with direct sums”.

> **[Stacks, Tag 0G29] (2) for the derived lower shriek of a `CompactificationData`.**  The
> functor `Rf_! = R(fbar)_* ∘ j_!` read off a compactification commutes with direct sums of
> every shape, given the adjunction `j_! ⊣ j^{-1}` of [Stacks, Tag 08FJ] and
> [Stacks, Tag 0F0D] for `R(fbar)_*`.
>
> This is the form that discharges the hypothesis of
> `Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.isLeftAdjoint_derivedLowerShriek`,
> which is [Stacks, Tag 0G2C].

```lean
theorem preservesColimitsOfShape_derivedLowerShriek {DU : Type u₁} [Category.{v₁} DU]
    {DX : Type u₂} [Category.{v₂} DX] {DY : Type u₃} [Category.{v₃} DY]
    (data : CompactificationData DU DX DY) {Uj : DX ⥤ DU} (adjImmersion : data.shriek ⊣ Uj)
    (I : Type w)
    (hProper : PreservesColimitsOfShape (Discrete I) data.pushforwardFbar) :
    PreservesColimitsOfShape (Discrete I) data.derivedLowerShriek
```

**`Stacks.Cohomology.Localization.preservesColimitsOfSize_derivedExtensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedExtensionByZeroDirectSums.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedExtensionByZeroDirectSums.lean#L54). The attribute's comment: “the open immersion case of the proof: j\_! commutes with direct sums”.

> **The open immersion case of the proof of [Stacks, Tag 0G29].** On the unbounded derived
> categories of sheaves of modules over a ringed site, extension by zero along the localization
> at an object commutes with direct sums — indeed with all colimits — because it is a left
> adjoint of restriction, which is [Stacks, Tag 08FJ],
> `Stacks.Cohomology.Localization.derivedExtensionByZeroRestrictionAdjunction`.
>
> The source of [Stacks, Tag 0G29] reduces the commutation of `Rf_!` with direct sums to this
> statement for an open immersion and to [Stacks, Tag 0GIW] or [Stacks, Tag 0F0D] for a proper
> morphism; this is the half of the reduction that is available outright.

```lean
theorem preservesColimitsOfSize_derivedExtensionByZero (X : RingedSite.{u, u, u}) (U : X.C) :
    PreservesColimitsOfSize.{w, w'}
      (SheafOfModules.pullback.{u} (F := Over.forget U)
        (𝟙 (((Stacks.SheafOfModules.Tensor.ringSheaf X.O)).over U))).mapDerivedCategory
```

## Tag 0G2A, a lemma

[Tag 0G2A](https://stacks.math.columbia.edu/tag/0G2A) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_bounded_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/BoundednessUnbounded.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/BoundednessUnbounded.lean#L215). The attribute's comment: “all three parts, for E in D+\_tors(X, Lambda) (Rf\_! = derivedLowerShriek on D+) and, when Lambda is torsion, for E in D(X, Lambda) (Rf\_! = derivedLowerShriekUnbounded), with one N for both; part (3) is the conjunction of its lower and upper bound halves, which is the source's statement for all -infinity <= a <= b <= infinity”.

> **[Stacks, Tag 0G2A].** Let `f : X ⟶ Y` be a morphism of schemes with `Y` quasi-compact,
> `j` a compactification of `X` over `Y` (through which `Rf_! = Rf̄_* ∘ Rj_!` is defined), and `Λ`
> a ring. There is an integer `N` such that for `E ∈ D⁺_tors(X_étale, Λ)`, and, when `Λ` is
> torsion, for `E ∈ D(X_étale, Λ)`:
>
> 1. `Hⁱ(Rf_!(τ_{≤ a} E)) ⟶ Hⁱ(Rf_! E)` is an isomorphism for `i ≤ a`;
> 2. `Hⁱ(Rf_! E) ⟶ Hⁱ(Rf_!(τ_{≥ b - N} E))` is an isomorphism for `i ≥ b`;
> 3. if `Hⁱ(E) = 0` for `i ∉ [a, b]` then `Hⁱ(Rf_! E) = 0` for `i ∉ [a, b + N]`; stated as the two
>    implications `E ≥ a ⇒ Rf_! E ≥ a` and `E ≤ b ⇒ Rf_! E ≤ b + N`, which together are part (3)
>    for all `-∞ ≤ a ≤ b ≤ ∞`.
>
> [Stacks, Tag 0G2A] assumes `f` separated of finite type and `X`, `Y` quasi-compact and
> quasi-separated; here the compactification `j` is given, and only quasi-compactness of `Y` is
> used.

```lean
theorem exists_bounded_derivedLowerShriek [CompactSpace Y] :
    ∃ N : ℕ,
      (∀ E : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X), isTorsionPlus.{u, 0} Λ X E →
        (∀ a i : ℤ, i ≤ a → IsIso ((DerivedCategory.Plus.homologyFunctor _ i).map
            ((derivedLowerShriek.{u, 0} f j Λ).map
              ((DerivedCategory.Plus.TStructure.t.truncLEι a).app E)))) ∧
          (∀ b i : ℤ, b ≤ i → IsIso ((DerivedCategory.Plus.homologyFunctor _ i).map
            ((derivedLowerShriek.{u, 0} f j Λ).map
              ((DerivedCategory.Plus.TStructure.t.truncGEπ (b - N)).app E)))) ∧
          (∀ a : ℤ, E.IsGE a → ((derivedLowerShriek.{u, 0} f j Λ).obj E).IsGE a) ∧
          ∀ b : ℤ, E.IsLE b →
            (DerivedCategory.Plus.ι.obj ((derivedLowerShriek.{u, 0} f j Λ).obj E)).IsLE
              (b + N)) ∧
      ((∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) → ∀ E : DerivedCategory (EtaleModules.{u, 0} Λ X),
        (∀ a i : ℤ, i ≤ a → IsIso ((DerivedCategory.homologyFunctor _ i).map
            ((derivedLowerShriekUnbounded.{u, 0} f j Λ).map
              ((DerivedCategory.TStructure.t.truncLEι a).app E)))) ∧
          (∀ b i : ℤ, b ≤ i → IsIso ((DerivedCategory.homologyFunctor _ i).map
            ((derivedLowerShriekUnbounded.{u, 0} f j Λ).map
              ((DerivedCategory.TStructure.t.truncGEπ (b - N)).app E)))) ∧
          (∀ a : ℤ, E.IsGE a → ((derivedLowerShriekUnbounded.{u, 0} f j Λ).obj E).IsGE a) ∧
          ∀ b : ℤ, E.IsLE b →
            ((derivedLowerShriekUnbounded.{u, 0} f j Λ).obj E).IsLE (b + N))
```

## Tag 0GKM, a lemma

[Tag 0GKM](https://stacks.math.columbia.edu/tag/0GKM) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.nonempty_derivedLowerShriek_iso_fShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekCompactificationComparison.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekCompactificationComparison.lean#L421). The attribute's comment: “Rf\_! on D⁺\_tors(X\_étale, Λ), any ring Λ, any compactification”.

> **Stacks 0GKM** for the functors `Rf_! : D⁺_tors(X_étale, Λ) ⥤ D⁺_tors(Y_étale, Λ)` of
> Stacks 0F7H. Let `f : X ⟶ Y` be a quasi-finite separated morphism of schemes with `Y`
> quasi-compact and quasi-separated (so `X` is too), and `Λ` a ring. For every compactification
> `j : X ⟶ X̄` of `X` over `Y`, the functor `Rf_! = R f̄_* ∘ j_!` agrees with the restriction to
> `D⁺_tors(X_étale, Λ)` of the functor `f_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Stacks 0F5M.
>
> The direct image with compact support `f_!` of Stacks 0F6R is constructed on the small étale sites
> of a big étale site `B` (Stacks 021A); it is read on Mathlib's small étale sites, where `Rf_!`
> lives, through `AlgebraicGeometry.SmallEtale.etaleModulesFShriek`, and any big étale site
> containing `X` and `Y` may be used (one exists: `AlgebraicGeometry.BigEtaleSite.ofSet`).
> Quasi-finiteness is Stacks 02NG: locally quasi-finite, locally of finite type and quasi-compact
> together.

```lean
theorem nonempty_derivedLowerShriek_iso_fShriek (j : CompactificationOf (Over.mk f)) :
    Nonempty ((isTorsionPlus.{u, u} Λ X).ι ⋙ derivedLowerShriek.{u, u} f j Λ ⋙
        DerivedCategory.Plus.ι ≅
      (isTorsionPlus.{u, u} Λ X).ι ⋙ DerivedCategory.Plus.ι ⋙
        (etaleModulesFShriek B Λ
          (ObjectProperty.homMk f : B.obj X hX ⟶ B.obj Y hY)).mapDerivedCategory)
```

**`AlgebraicGeometry.SmallEtale.nonempty_derivedLowerShriekUnbounded_iso_fShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekCompactificationComparison.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekCompactificationComparison.lean#L447). The attribute's comment: “Rf\_! on D(X\_étale, Λ), Λ a torsion ring, any compactification”.

> **Stacks 0GKM** for the functors `Rf_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Stacks 0F7H,
> `Λ` a torsion ring. Let `f : X ⟶ Y` be a quasi-finite separated morphism of schemes with `Y`
> quasi-compact and quasi-separated (so `X` is too). For every compactification `j : X ⟶ X̄` of
> `X` over `Y`, the functor `Rf_! = R f̄_* ∘ j_!` agrees with the functor
> `f_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Stacks 0F5M.
>
> As in `AlgebraicGeometry.SmallEtale.nonempty_derivedLowerShriek_iso_fShriek`, `f_!` is read on
> Mathlib's small étale sites through `AlgebraicGeometry.SmallEtale.etaleModulesFShriek`, for any
> big étale site containing `X` and `Y`. A torsion ring is one in which `m • 1 = 0` for some
> `m > 0`.

```lean
theorem nonempty_derivedLowerShriekUnbounded_iso_fShriek (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0)
    (j : CompactificationOf (Over.mk f)) :
    Nonempty (derivedLowerShriekUnbounded.{u, u} f j Λ ≅
      (etaleModulesFShriek B Λ
        (ObjectProperty.homMk f : B.obj X hX ⟶ B.obj Y hY)).mapDerivedCategory)
```

## Tag 0GKN, a lemma

[Tag 0GKN](https://stacks.math.columbia.edu/tag/0GKN) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_distTriang_derivedLowerShriek_mayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/MayerVietoris.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/MayerVietoris.lean#L300).

> Let `f : X ⟶ Y` be a morphism of schemes with a compactification `j : X ⟶ X̄`, so that
> `Rf_! = R(f̄)_* ∘ Rj_!` is defined (`Stacks.EtaleCohomology.derivedLowerShriek` on `D⁺`,
> `Stacks.EtaleCohomology.derivedLowerShriekUnbounded` on `D`), and let `U` and `V` be opens of `X`
> with `X = U ∪ V`. Denote `a : U ⟶ Y`, `b : V ⟶ Y` and `c : U ∩ V ⟶ Y` the restrictions of `f`,
> with the compactifications induced by `j`. Let `Λ` be a ring. For `K` in `D⁺(X_étale, Λ)`, and
> also for `K` in `D(X_étale, Λ)`, there is a distinguished triangle
> `Rc_!(K|_{U ∩ V}) ⟶ Ra_!(K|_U) ⊕ Rb_!(K|_V) ⟶ Rf_! K ⟶ Rc_!(K|_{U ∩ V})[1]`
> in `D⁺(Y_étale, Λ)`, respectively `D(Y_étale, Λ)`.

```lean
theorem exists_distTriang_derivedLowerShriek_mayerVietoris :
    (∀ K : DerivedCategory.Plus (EtaleModules.{u, r} Λ X),
      ∃ (α : (derivedLowerShriek.{u, r} ((U ⊓ V).ι ≫ f) (j.restrictOpen (U ⊓ V).ι) Λ).obj
            ((etaleModuleDerivedRestriction.{u, r} Λ (U ⊓ V).ι).obj K) ⟶
          (derivedLowerShriek.{u, r} (U.ι ≫ f) (j.restrictOpen U.ι) Λ).obj
              ((etaleModuleDerivedRestriction.{u, r} Λ U.ι).obj K) ⊞
            (derivedLowerShriek.{u, r} (V.ι ≫ f) (j.restrictOpen V.ι) Λ).obj
              ((etaleModuleDerivedRestriction.{u, r} Λ V.ι).obj K))
        (β : _ ⟶ (derivedLowerShriek.{u, r} f j Λ).obj K) (γ : _ ⟶ _⟦(1 : ℤ)⟧),
        Triangle.mk α β γ ∈ distTriang (DerivedCategory.Plus (EtaleModules.{u, r} Λ Y))) ∧
    (∀ K : DerivedCategory (EtaleModules.{u, r} Λ X),
      ∃ (α : (derivedLowerShriekUnbounded.{u, r} ((U ⊓ V).ι ≫ f)
              (j.restrictOpen (U ⊓ V).ι) Λ).obj
            ((etaleModuleRestriction.{u, r} Λ (U ⊓ V).ι).mapDerivedCategory.obj K) ⟶
          (derivedLowerShriekUnbounded.{u, r} (U.ι ≫ f) (j.restrictOpen U.ι) Λ).obj
              ((etaleModuleRestriction.{u, r} Λ U.ι).mapDerivedCategory.obj K) ⊞
            (derivedLowerShriekUnbounded.{u, r} (V.ι ≫ f) (j.restrictOpen V.ι) Λ).obj
              ((etaleModuleRestriction.{u, r} Λ V.ι).mapDerivedCategory.obj K))
        (β : _ ⟶ (derivedLowerShriekUnbounded.{u, r} f j Λ).obj K) (γ : _ ⟶ _⟦(1 : ℤ)⟧),
        Triangle.mk α β γ ∈ distTriang (DerivedCategory (EtaleModules.{u, r} Λ Y)))
```

## Tag 0GKP, a lemma

[Tag 0GKP](https://stacks.math.columbia.edu/tag/0GKP) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_distTriang_derivedLowerShriek_openClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/OpenClosedTriangle.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/OpenClosedTriangle.lean#L190).

> **[Stacks, Tag 0GKP].** Let `f : X ⟶ Y` be a morphism of schemes, quasi-compact, with a
> compactification `j : X ⟶ X̄` over `Y` (for instance `f` finite type and separated with `X` and
> `Y` quasi-compact and quasi-separated), let `j_U : U ⟶ X` be an open immersion and `i : Z ⟶ X` a
> closed immersion with complementary images, and let `g = f ∘ j_U` and `h = f ∘ i` be the
> restrictions of `f`. Let `Λ` be a ring. Then
>
> * for every `K` in `D⁺(X_étale, Λ)`, in particular for every `K` in `D⁺_tors(X_étale, Λ)`, and
> * for every `K` in `D(X_étale, Λ)`, in particular when `Λ` is torsion,
>
> there is a distinguished triangle `Rg_!(K|_U) ⟶ Rf_! K ⟶ Rh_!(K|_Z) ⟶ Rg_!(K|_U)[1]` in
> `D⁺(Y_étale, Λ)`, respectively `D(Y_étale, Λ)`. Here `Rf_! = R f̄_* ∘ j_!` is computed through
> `j`, and `Rg_!` and `Rh_!` through the compactifications `j` induces on `U` and on `Z`
> (`AlgebraicGeometry.CompactificationOf.restrictOpen` and
> `AlgebraicGeometry.CompactificationOf.restrictClosed`).

```lean
theorem exists_distTriang_derivedLowerShriek_openClosed :
    (∀ K : DerivedCategory.Plus (EtaleModules.{u, r} Λ X),
      ∃ (a : (derivedLowerShriek.{u, r} (jU ≫ f) (j.restrictOpen jU) Λ).obj
            ((etaleModuleRestriction.{u, r} Λ jU).mapDerivedCategoryPlus.obj K) ⟶
          (derivedLowerShriek.{u, r} f j Λ).obj K)
        (b : (derivedLowerShriek.{u, r} f j Λ).obj K ⟶
          (derivedLowerShriek.{u, r} (i ≫ f) (j.restrictClosed i) Λ).obj
            ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategoryPlus.obj K))
        (c : (derivedLowerShriek.{u, r} (i ≫ f) (j.restrictClosed i) Λ).obj
            ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategoryPlus.obj K) ⟶
          ((derivedLowerShriek.{u, r} (jU ≫ f) (j.restrictOpen jU) Λ).obj
            ((etaleModuleRestriction.{u, r} Λ jU).mapDerivedCategoryPlus.obj K))⟦(1 : ℤ)⟧),
        Triangle.mk a b c ∈ distTriang _) ∧
    (∀ K : DerivedCategory (EtaleModules.{u, r} Λ X),
      ∃ (a : (derivedLowerShriekUnbounded.{u, r} (jU ≫ f) (j.restrictOpen jU) Λ).obj
            ((etaleModuleRestriction.{u, r} Λ jU).mapDerivedCategory.obj K) ⟶
          (derivedLowerShriekUnbounded.{u, r} f j Λ).obj K)
        (b : (derivedLowerShriekUnbounded.{u, r} f j Λ).obj K ⟶
          (derivedLowerShriekUnbounded.{u, r} (i ≫ f) (j.restrictClosed i) Λ).obj
            ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategory.obj K))
        (c : (derivedLowerShriekUnbounded.{u, r} (i ≫ f) (j.restrictClosed i) Λ).obj
            ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategory.obj K) ⟶
          ((derivedLowerShriekUnbounded.{u, r} (jU ≫ f) (j.restrictOpen jU) Λ).obj
            ((etaleModuleRestriction.{u, r} Λ jU).mapDerivedCategory.obj K))⟦(1 : ℤ)⟧),
        Triangle.mk a b c ∈ distTriang _)
```

## Tag 0GKQ, a lemma

[Tag 0GKQ](https://stacks.math.columbia.edu/tag/0GKQ) in the Stacks Project.

**`Stacks.EtaleCohomology.nonempty_derivedLowerShriek_inverseImage_iso_of_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ThickeningInvariance.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ThickeningInvariance.lean#L145).

> Let `f' : X' ⟶ Y` be a quasi-compact morphism of schemes with a compactification `j'` over
> `Y` (for instance `f'` finite type and separated with `X'` and `Y` quasi-compact and
> quasi-separated), let `i : X ⟶ X'` be a thickening (a surjective closed immersion, [Stacks,
> Tag 04EX]) and `f = f' ∘ i`. Let `Λ` be a ring. Then
>
> * for every `K'` in `D⁺(X'_étale, Λ)`, in particular for every `K'` in `D⁺_tors(X'_étale, Λ)`,
>   `Rf_! i⁻¹ K' ≅ Rf'_! K'`, and
> * for every `K'` in `D(X'_étale, Λ)`, in particular when `Λ` is torsion, `Rf_! i⁻¹ K' ≅ Rf'_! K'`.
>
> Here `Rf'_! = R f̄'_* ∘ j'_!` is computed through `j'` and `Rf_!` through the compactification
> `j'` induces on `X` (`AlgebraicGeometry.CompactificationOf.restrictClosed`).

```lean
theorem nonempty_derivedLowerShriek_inverseImage_iso_of_thickening :
    (∀ K' : DerivedCategory.Plus (EtaleModules.{u, r} Λ X'),
      Nonempty ((derivedLowerShriek.{u, r} (i ≫ f') (j'.restrictClosed i) Λ).obj
          ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategoryPlus.obj K') ≅
        (derivedLowerShriek.{u, r} f' j' Λ).obj K')) ∧
    (∀ K' : DerivedCategory (EtaleModules.{u, r} Λ X'),
      Nonempty ((derivedLowerShriekUnbounded.{u, r} (i ≫ f') (j'.restrictClosed i) Λ).obj
          ((etaleModuleInverseImage.{u, r} Λ i).mapDerivedCategory.obj K') ≅
        (derivedLowerShriekUnbounded.{u, r} f' j' Λ).obj K'))
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedThickeningIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/LowerShriekComposition.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/LowerShriekComposition.lean#L567).

> **Stacks Project, Tag 0GKQ.** Let `f' : X' ⟶ Y` be a separated morphism of finite type of
> quasi-compact and quasi-separated schemes, `i : X ⟶ X'` a thickening (a closed immersion which is
> surjective) and `f = f' ∘ i`. Let `Λ` be a ring. Then `Rf_! ∘ i⁻¹ ≅ Rf'_!` on `D(X'_étale, Λ)`,
> hence on `D⁺_{tors}(X'_étale, Λ)` and, for `Λ` torsion, on `D(X'_étale, Λ)`. Here `Rf'_!` is
> computed through a compactification `j'` of `f'` and `Rf_!` through the compactification
> `j'.restrictClosed i` of `f` that `j'` induces on `X`, as for Tags 0GKN and 0GKP.
>
> Here `Rf_! = Rf'_! ∘ Ri_! = Rf'_! ∘ i_*`
> (`Stacks.EtaleCohomology.derivedLowerShriekUnboundedRestrictClosedIso`), and `i⁻¹` and `i_*`
> are inverse equivalences by the topological invariance of the small étale site
> (`Stacks.EtaleCohomology.isDenseSubsite_of_universalHomeomorphism`).

```lean
def derivedLowerShriekUnboundedThickeningIso :
    etaleModuleDerivedInverseImageGeneral.{u, r} Λ i ⋙
        derivedLowerShriekUnbounded.{u, r} (i ≫ f') (j'.restrictClosed i) Λ ≅
      derivedLowerShriekUnbounded.{u, r} f' j' Λ
```

## Tag 0GL5, a lemma

[Tag 0GL5](https://stacks.math.columbia.edu/tag/0GL5) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_derivedLowerShriekUnboundedTensorMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/TorsionProjectionFormula.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/TorsionProjectionFormula.lean#L70).

> **[Stacks, Tag 0GL5].** Let `f : X ⟶ Y` be a separated finite type morphism of quasi-compact
> and quasi-separated schemes and let `Λ` be a torsion ring (`n = 0` in `Λ` for some `n ≥ 1`). Then
> `f` has a compactification `j : X ⟶ X̄` over `Y`, and for every compactification `j`, every
> `E ∈ D(X_étale, Λ)` and every `K ∈ D(Y_étale, Λ)` the canonical map
> `Rf_!E ⊗^L_Λ K ⟶ Rf_!(E ⊗^L_Λ f^{-1}K)`, with `Rf_! = Rf̄_* ∘ j_!` computed through `j`, is an
> isomorphism in `D(Y_étale, Λ)`.

```lean
theorem isIso_derivedLowerShriekUnboundedTensorMap (Λ : Type) [CommRing Λ] (n : ℕ) (hn : 0 < n)
    (hΛ : (n : Λ) = 0) {X Y : Scheme.{u}} (f : X ⟶ Y) [CompactSpace X] [QuasiSeparatedSpace X]
    [CompactSpace Y] [QuasiSeparatedSpace Y] [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (E : DerivedCategory (EtaleModules.{u, 0} Λ X))
        (K : DerivedCategory (EtaleModules.{u, 0} Λ Y)),
        IsIso (derivedLowerShriekUnboundedTensorMap.{u, 0} Λ j E K)
```

## Tag 0GL6, a remark

[Tag 0GL6](https://stacks.math.columbia.edu/tag/0GL6) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_derivedLowerShriekUnboundedExtendScalarsMap_of_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekExtendScalarsHeldInputs.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekExtendScalarsHeldInputs.lean#L123). The attribute's comment: “diagram (2): Rf\_! commutes with - ⊗^L\_\{Λ₁} Λ₂”. References: SGA 4 XVII (5.2.2), “special case”.

> **The second diagram of [Stacks, Remark 0GL6].**  Let `φ : Λ₁ → Λ₂` be a homomorphism of
> commutative rings with `Λ₁` torsion, `f : X ⟶ Y` a morphism of schemes with `Y` quasi-compact and
> `j` a compactification of `X` over `Y`, so that `Rf_! = R(f̄)_* ∘ j_!` as in [Stacks, Tag 0F7H].
> Then the comparison `Rf_!(E) ⊗^L_{Λ₁} Λ₂ ⟶ Rf_!(E ⊗^L_{Λ₁} Λ₂)`, natural in
> `E ∈ D(X_étale, Λ₁)`, is an isomorphism: the square of `Rf_!` and `- ⊗^L_{Λ₁} Λ₂` commutes.
>
> This is `isIso_derivedLowerShriekUnboundedExtendScalarsMap_of_properBaseChange` applied to the
> proper base change theorem, [Stacks, Tag 095T]
> (`Stacks.EtaleCohomology.isIso_etaleAbelianSheafDerivedBaseChange_of_isProper`).

```lean
theorem isIso_derivedLowerShriekUnboundedExtendScalarsMap_of_torsion
    (hΛ₁ : ∀ x : Λ₁, ∃ n : ℕ, 0 < n ∧ (n : Λ₁) * x = 0)
    {X Y : Scheme.{u}} [CompactSpace Y] (f : X ⟶ Y) (j : CompactificationOf (Over.mk f)) :
    IsIso (derivedLowerShriekUnboundedExtendScalarsMap.{u, r} φ f j)
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnbounded_commutes_restrictScalars_and_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekExtendScalarsHeldInputs.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekExtendScalarsHeldInputs.lean#L141).

> **[Stacks, Remark 0GL6], both diagrams.**  Let `φ : Λ₁ → Λ₂` be a homomorphism of commutative
> rings with `Λ₁` torsion, `f : X ⟶ Y` a morphism of schemes with `Y` quasi-compact and `j` a
> compactification of `X` over `Y`, so that `Rf_! = R(f̄)_* ∘ j_!` as in [Stacks, Tag 0F7H].  Then
> 1. `Rf_!` commutes with restriction of coefficients: `res_φ ∘ Rf_! ≅ Rf_! ∘ res_φ` as functors
>    `D(X_étale, Λ₂) ⥤ D(Y_étale, Λ₁)` (`derivedLowerShriekUnboundedRestrictScalarsIso`);
> 2. `Rf_!` commutes with derived extension of coefficients:
>    `Rf_!(-) ⊗^L_{Λ₁} Λ₂ ≅ Rf_!(- ⊗^L_{Λ₁} Λ₂)` as functors `D(X_étale, Λ₁) ⥤ D(Y_étale, Λ₂)`
>    (`isIso_derivedLowerShriekUnboundedExtendScalarsMap_of_torsion`).

```lean
theorem derivedLowerShriekUnbounded_commutes_restrictScalars_and_extendScalars
    (hΛ₁ : ∀ x : Λ₁, ∃ n : ℕ, 0 < n ∧ (n : Λ₁) * x = 0)
    {X Y : Scheme.{u}} [CompactSpace Y] (f : X ⟶ Y) (j : CompactificationOf (Over.mk f)) :
    Nonempty (derivedLowerShriekUnbounded.{u, r} f j Λ₂ ⋙
        etaleModuleDerivedRestrictScalars.{u, r} φ Y ≅
      etaleModuleDerivedRestrictScalars.{u, r} φ X ⋙ derivedLowerShriekUnbounded.{u, r} f j Λ₁) ∧
    Nonempty (derivedLowerShriekUnbounded.{u, r} f j Λ₁ ⋙
        etaleModuleDerivedExtendScalars.{u, r} φ Y ≅
      etaleModuleDerivedExtendScalars.{u, r} φ X ⋙ derivedLowerShriekUnbounded.{u, r} f j Λ₂)
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedRestrictScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekRestrictScalars.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CoefficientChange/LowerShriekRestrictScalars.lean#L208). The attribute's comment: “the first of the two diagrams: Rf\_! commutes with restriction of coefficients res\_φ along φ : Λ₁ → Λ₂, for a chosen compactification. The second diagram, that Rf\_! commutes with - ⊗^L\_\{Λ₁} Λ₂, is isIso\_derivedLowerShriekUnboundedExtendScalarsMap\_of\_torsion.”.

> **The first diagram of [Stacks, Remark 0GL6].**  Cohomology with compact support commutes
> with restriction of coefficients: for a compactification `j` of `X` over `Y` and
> `Rf_! = R(f̄)_* ∘ Rj_!` the resulting functor on unbounded derived categories, restricting the
> coefficients along `φ : Λ₁ → Λ₂` before or after `Rf_!` gives canonically isomorphic functors.
>
> The second diagram asserted in the same remark, that `Rf_!` commutes with
> `- ⊗^L_{Λ₁} Λ₂`, is
> `Stacks.EtaleCohomology.isIso_derivedLowerShriekUnboundedExtendScalarsMap_of_torsion`; see the
> module docstring.
>
> No separatedness, finite type or quasi-compactness hypothesis on `f` appears: the source needs
> them only to produce the compactification, which is data here, so this is more general than the
> source's phrasing.  Neither coefficient ring is assumed torsion, for the same reason — the
> torsion hypothesis of the remark is consumed by Tag 0GL5, which only the second diagram uses.

```lean
def derivedLowerShriekUnboundedRestrictScalarsIso {X Y : Scheme.{u}} (f : X ⟶ Y)
    (j : CompactificationOf (Over.mk f)) :
    derivedLowerShriekUnbounded.{u, r} f j Λ₂ ⋙
        etaleModuleDerivedRestrictScalars.{u, r} φ Y ≅
      etaleModuleDerivedRestrictScalars.{u, r} φ X ⋙ derivedLowerShriekUnbounded.{u, r} f j Λ₁
```

## Tag 0GL7, a remark

[Tag 0GL7](https://stacks.math.columbia.edu/tag/0GL7) in the Stacks Project.

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.lowerShriekHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean#L347). The attribute's comment: “the canonical map α, for a chosen compactification, at abstract compactification data; its instance at the étale derived categories, which is the faithful registration of 0GL7, is `Stacks.EtaleCohomology.etaleLowerShriekHomMap`”.

> **The canonical map `α` of [Stacks, Tag 0GL7]**,
>
> `α : Rf_*RHom_Λ(K, L) ⟶ RHom_Λ(Rf_!K, Rf_!L)`,
>
> for a chosen compactification `f = f̄ ∘ j`. It is `γ ∘ Rf̄_*β`, with `Rf_! = Rf̄_*j_!` and
> `Rf_* = Rf̄_*Rj_*`.

```lean
def lowerShriekHomMap (K L : DU) :
    data.derivedPushforward.obj ((data.homU.obj (op K)).obj L) ⟶
      (data.homY.obj (op (data.derivedLowerShriek.obj K))).obj
        (data.derivedLowerShriek.obj L)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.lowerShriekHomMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean#L358). The attribute's comment: “the factorisation α = γ ∘ Rf̄\_*β, at abstract compactification data; at the étale derived categories it is `Stacks.EtaleCohomology.etaleLowerShriekHomMap_eq`”.

> **`α = γ ∘ Rf̄_*β`**, the factorisation along the chosen compactification by which the
> canonical map of [Stacks, Tag 0GL7] is defined.

```lean
theorem lowerShriekHomMap_eq (K L : DU) :
    data.lowerShriekHomMap K L =
      data.pushforwardFbar.map (data.openImmersionHomMap K L) ≫
        data.pushforwardHomMap (data.shriek.obj K) (data.shriek.obj L)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.lowerShriekHomMap_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean#L368). The attribute's comment: “functoriality of α in L, at abstract compactification data; at the étale derived categories it is `Stacks.EtaleCohomology.etaleLowerShriekHomMap_naturality_target`”.

> **The canonical map of [Stacks, Tag 0GL7] is covariant in `L`**, one half of the
> functoriality the source asserts.

```lean
theorem lowerShriekHomMap_naturality_target (K : DU) {L L' : DU} (l : L ⟶ L') :
    data.derivedPushforward.map ((data.homU.obj (op K)).map l) ≫
        data.lowerShriekHomMap K L' =
      data.lowerShriekHomMap K L ≫
        (data.homY.obj (op (data.derivedLowerShriek.obj K))).map
          (data.derivedLowerShriek.map l)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.lowerShriekHomMap_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/Compactification.lean#L383). The attribute's comment: “functoriality of α in K, at abstract compactification data; at the étale derived categories it is `Stacks.EtaleCohomology.etaleLowerShriekHomMap_naturality_source`”.

> **The canonical map of [Stacks, Tag 0GL7] is contravariant in `K`**, the other half of the
> functoriality the source asserts.

```lean
theorem lowerShriekHomMap_naturality_source {K K' : DU} (k : K' ⟶ K) (L : DU) :
    data.derivedPushforward.map ((data.homU.map k.op).app L) ≫
        data.lowerShriekHomMap K' L =
      data.lowerShriekHomMap K L ≫
        (data.homY.map (data.derivedLowerShriek.map k).op).app
          (data.derivedLowerShriek.obj L)
```

**`Stacks.EtaleCohomology.etaleLowerShriekHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean#L117). The attribute's comment: “the canonical map α on étale derived categories, for a compactification of f; β is built from 08J8, 0GL1 and j^\{-1}Rj\_* = id, γ from 0B6C/0B6D, Rf\_* = Rf̄\_* Rj\_* by Leray”.

> **The canonical map `α` of [Stacks, Tag 0GL7]**,
>
> `α : Rf_*RHom_Λ(K, L) ⟶ RHom_Λ(Rf_!K, Rf_!L)`,
>
> for `K`, `L` in `D(X_étale, Λ)`, with `Rf_! = Rf̄_* ∘ j_!` computed through the compactification
> `j`: Leray `Rf_* = Rf̄_* ∘ Rj_*`, followed by `Rf̄_*β` and by the map `γ` of
> [Stacks, Tag 0B6D] for `f̄`.

```lean
def etaleLowerShriekHomMap (K L : DerivedCategory (EtaleModules.{u, r} Λ X)) :
    (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f).obj
        (((etaleDerivedHom.{u, r} Λ X).obj (op K)).obj L) ⟶
      ((etaleDerivedHom.{u, r} Λ Y).obj (op ((derivedLowerShriekUnbounded.{u, r} f j Λ).obj K))).obj
        ((derivedLowerShriekUnbounded.{u, r} f j Λ).obj L)
```

**`Stacks.EtaleCohomology.etaleLowerShriekHomMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean#L129). The attribute's comment: “α = γ ∘ Rf̄\_*β (after Leray), on étale derived categories”.

> **`α = γ ∘ Rf̄_*β`**, preceded by Leray `Rf_* = Rf̄_* ∘ Rj_*`: the factorization of the
> canonical map of [Stacks, Tag 0GL7] along the compactification, with `β` the open-immersion map
> and `γ` the direct-image map of [Stacks, Tag 0B6D].

```lean
theorem etaleLowerShriekHomMap_eq (K L : DerivedCategory (EtaleModules.{u, r} Λ X)) :
    etaleLowerShriekHomMap.{u, r} Λ f j K L =
      (etaleCompactificationLerayIso.{u, r} Λ f j).hom.app _ ≫
        (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ j.toBase).map
          ((etaleCompactificationData.{u, r} Λ f j).openImmersionHomMap K L) ≫
        (etaleCompactificationData.{u, r} Λ f j).pushforwardHomMap
          ((etaleModuleDerivedExtensionByZeroUnbounded.{u, r} Λ j.immersion).obj K)
          ((etaleModuleDerivedExtensionByZeroUnbounded.{u, r} Λ j.immersion).obj L)
```

**`Stacks.EtaleCohomology.etaleLowerShriekHomMap_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean#L147). The attribute's comment: “functoriality of α in L, on étale derived categories”.

> **The canonical map of [Stacks, Tag 0GL7] is covariant in `L`.**

```lean
theorem etaleLowerShriekHomMap_naturality_target (K : DerivedCategory (EtaleModules.{u, r} Λ X))
    {L L' : DerivedCategory (EtaleModules.{u, r} Λ X)} (l : L ⟶ L') :
    (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f).map
        (((etaleDerivedHom.{u, r} Λ X).obj (op K)).map l) ≫
          etaleLowerShriekHomMap.{u, r} Λ f j K L' =
      etaleLowerShriekHomMap.{u, r} Λ f j K L ≫
        ((etaleDerivedHom.{u, r} Λ Y).obj
            (op ((derivedLowerShriekUnbounded.{u, r} f j Λ).obj K))).map
          ((derivedLowerShriekUnbounded.{u, r} f j Λ).map l)
```

**`Stacks.EtaleCohomology.etaleLowerShriekHomMap_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean#L162). The attribute's comment: “functoriality of α in K, on étale derived categories”.

> **The canonical map of [Stacks, Tag 0GL7] is contravariant in `K`.**

```lean
theorem etaleLowerShriekHomMap_naturality_source {K K' : DerivedCategory (EtaleModules.{u, r} Λ X)}
    (k : K' ⟶ K) (L : DerivedCategory (EtaleModules.{u, r} Λ X)) :
    (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f).map
        (((etaleDerivedHom.{u, r} Λ X).map k.op).app L) ≫ etaleLowerShriekHomMap.{u, r} Λ f j K' L =
      etaleLowerShriekHomMap.{u, r} Λ f j K L ≫
        ((etaleDerivedHom.{u, r} Λ Y).map ((derivedLowerShriekUnbounded.{u, r} f j Λ).map k).op).app
          ((derivedLowerShriekUnbounded.{u, r} f j Λ).obj L)
```

**`Stacks.EtaleCohomology.etaleLowerShriekHomNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/LowerShriekHomMap.lean#L178). The attribute's comment: “the canonical map α : Rf\_*RHom(K, L) ⟶ RHom(Rf\_!K, Rf\_!L) on étale derived categories, functorial in K and L, for a compactification of f”.

> **The canonical map of [Stacks, Tag 0GL7], functorial in `K` and `L`**: `α` as a natural
> transformation between the bifunctors `(K, L) ↦ Rf_*RHom_Λ(K, L)` and
> `(K, L) ↦ RHom_Λ(Rf_!K, Rf_!L)` on `D(X_étale, Λ)ᵒᵖ × D(X_étale, Λ)`.

```lean
def etaleLowerShriekHomNatTrans :
    etaleDerivedHom.{u, r} Λ X ⋙
        (Functor.whiskeringRight _ _ _).obj (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f) ⟶
      (derivedLowerShriekUnbounded.{u, r} f j Λ).op ⋙ etaleDerivedHom.{u, r} Λ Y ⋙
        (Functor.whiskeringLeft _ _ _).obj (derivedLowerShriekUnbounded.{u, r} f j Λ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.10, Tag 0G28](https://stacks.math.columbia.edu/tag/0G28)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
