---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.HigherDirectImageCoherent.exists_shortExact_coherent_of_supp_eq_union, Stacks.AlgebraicGeometry.IdealPowerSmul.hasSupportSplitting, Stacks.ClosedImmersion.exists_idealCoproduct_pushforward_mono_isIso_near_genericPoint, Stacks.AlgebraicGeometry.CoherentDevissage.exists_filtration_by_integral_ideal_pushforwards, Stacks.AlgebraicGeometry.CoherentDevissage.property_of_isCoherent, Stacks.AlgebraicGeometry.IrreducibleSupportDevissage.property_of_irreducible_support, Stacks.AlgebraicGeometry.CoherentDevissage.property_of_isCoherent_of_generic_stalk_of_nonempty, Stacks.AlgebraicGeometry.GenericRankOneDevissage.property_of_genericRankOne
statement: formalized
proof: formalized
---

# 30.12 Devissage of coherent sheaves

Section 30.12 of the Stacks Project, [Tag 01YC](https://stacks.math.columbia.edu/tag/01YC). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01YD, a lemma

[Tag 01YD](https://stacks.math.columbia.edu/tag/01YD) in the Stacks Project.

**`Stacks.AlgebraicGeometry.HigherDirectImageCoherent.exists_shortExact_coherent_of_supp_eq_union`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/SupportSeparation.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/SupportSeparation.lean#L241).

> **[Stacks, Tag 01YD].** A coherent module whose support is a union of two closed sets is an
> extension of coherent modules supported on those sets: there is a short exact sequence
> `0 ⟶ G' ⟶ F ⟶ G ⟶ 0` of coherent modules with `Supp G' ⊆ Z'` and `Supp G ⊆ Z`, and `F` is
> literally its middle term.

```lean
public theorem exists_shortExact_coherent_of_supp_eq_union
    (X : Scheme.{u}) [IsNoetherian X] (F : X.Modules) [_root_.SheafOfModules.IsCoherent F]
    (Z Z' : Set X) (hZ : IsClosed Z) (hZ' : IsClosed Z')
    (hF : SheafOfModules.supp F = Z ∪ Z') :
    ∃ (G' G : X.Modules) (f : G' ⟶ F) (g : F ⟶ G) (w : f ≫ g = 0),
      (ShortComplex.mk f g w).ShortExact ∧
        _root_.SheafOfModules.IsCoherent G' ∧ _root_.SheafOfModules.IsCoherent G ∧
        SheafOfModules.supp G' ⊆ Z' ∧ SheafOfModules.supp G ⊆ Z
```

**`Stacks.AlgebraicGeometry.IdealPowerSmul.hasSupportSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealPowerSmul/Splitting.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IdealPowerSmul/Splitting.lean#L78).

> **[Stacks, Tag 01YD].** A coherent module on a Noetherian scheme whose support is the union
> of two closed sets sits in a short exact sequence of coherent modules whose sub is supported in
> the first and whose quotient is supported in the second.

```lean
theorem hasSupportSplitting (X : Scheme.{u}) [IsNoetherian X] :
    DevissageNoetherian.HasSupportSplitting X
```

## Tag 01YE, a lemma

[Tag 01YE](https://stacks.math.columbia.edu/tag/01YE) in the Stacks Project.

**`Stacks.ClosedImmersion.exists_idealCoproduct_pushforward_mono_isIso_near_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IrreducibleDevissage/GenericIdealPushforward.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/IrreducibleDevissage/GenericIdealPushforward.lean#L226).

> **[Stacks, Tag 01YE].** Let `X` be a Noetherian scheme, let `i : Z ⟶ X` be an integral
> closed subscheme with generic point `ξ`, and let `ℱ` be a coherent `𝒪_X`-module whose stalk at
> `i ξ` is annihilated by the maximal ideal of the local ring there. Then there are an integer
> `r ≥ 0`, a coherent sheaf of ideals `ℐ ⊆ 𝒪_Z` and an injective map of coherent sheaves
> `i_*(ℐ^{⊕ r}) ⟶ ℱ` which is an isomorphism on a neighbourhood of `i ξ`.
>
> The subsheaf of sections of `ℱ` annihilated by the ideal sheaf of `Z` has the same stalk at
> `i ξ` as `ℱ` does, because that ideal generates the maximal ideal there, so it agrees with `ℱ`
> on a neighbourhood of `i ξ`; being killed by the ideal it is `i_* 𝒢` for a coherent `𝒢` on `Z`
> by [Stacks, Tag 087T]; and the case `Z = X`, applied to `𝒢`, supplies the sheaf of ideals and
> the monomorphism.

```lean
theorem exists_idealCoproduct_pushforward_mono_isIso_near_genericPoint
    [AlgebraicGeometry.IsNoetherian X] (i : Z ⟶ X)
    [AlgebraicGeometry.IsClosedImmersion i] [AlgebraicGeometry.IsIntegral Z]
    (ξ : Z) (hξ : IsGenericPoint ξ (Set.univ : Set Z))
    (F : X.Modules) [F.IsCoherent] (hF : StalkKilledByMaximalIdeal F (i ξ)) :
    ∃ (r : ℕ) (I : (SheafOfModules.unit Z.ringCatSheaf).Submodule),
      I.toSheafOfModules.IsCoherent ∧
      ((Scheme.Modules.pushforward i).obj
        (∐ fun _ : Fin r => I.toSheafOfModules)).IsCoherent ∧
      ∃ φ : (Scheme.Modules.pushforward i).obj
          (∐ fun _ : Fin r => I.toSheafOfModules) ⟶ F,
        Mono φ ∧ ∃ U : X.Opens, i ξ ∈ U ∧
          IsIso ((Scheme.Modules.restrictFunctor U.ι).map φ)
```

## Tag 01YF, a lemma

[Tag 01YF](https://stacks.math.columbia.edu/tag/01YF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentDevissage.exists_filtration_by_integral_ideal_pushforwards`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/IdealFiltration/NoetherianInduction.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/IdealFiltration/NoetherianInduction.lean#L638).

> **[Stacks, Tag 01YF].** A coherent module on a Noetherian scheme has a finite filtration by
> coherent submodules, starting at `⊥` and ending at `⊤`, whose successive quotients are direct
> images of nonzero coherent sheaves of ideals on integral closed subschemes.

```lean
public theorem exists_filtration_by_integral_ideal_pushforwards
    (X : Scheme.{u}) [IsNoetherian X] (F : X.Modules) [F.IsCoherent] :
    ∃ (n : ℕ) (G : Fin (n + 1) → Subobject F) (hG : Monotone G),
      G 0 = ⊥ ∧ G (Fin.last n) = ⊤ ∧
      (∀ j : Fin (n + 1), (G j : X.Modules).IsCoherent) ∧
      ∀ j : Fin n,
        ∃ (Z : Scheme.{u}) (i : Z ⟶ X) (_ : IsClosedImmersion i) (_ : IsIntegral Z)
          (I : (SheafOfModules.unit Z.ringCatSheaf).Submodule),
          I.toSheafOfModules.IsCoherent ∧ ¬ IsZero I.toSheafOfModules ∧
          Nonempty (cokernel (Subobject.ofLE (G j.castSucc) (G j.succ)
            (hG j.castSucc_le_succ)) ≅
            (Scheme.Modules.pushforward i).obj I.toSheafOfModules)
```

## Tag 01YG, a lemma

[Tag 01YG](https://stacks.math.columbia.edu/tag/01YG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentDevissage.property_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/IdealPushforwardCriterion.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/IdealPushforwardCriterion.lean#L73).

> Let `X` be a Noetherian scheme and let `P` be a property of
> coherent `𝒪_X`-modules which holds on the zero module, is stable under extensions of coherent
> modules, and holds on the direct image `i_* I` of every quasi-coherent ideal `I ⊆ 𝒪_Z` along
> the closed immersion of every integral closed subscheme `i : Z ⟶ X`. Then `P` holds on every
> coherent `𝒪_X`-module.
>
> Every coherent module is filtered by such direct images ([Stacks, Tag 01YF]), and extension
> stability propagates `P` along the filtration.

```lean
public theorem property_of_isCoherent (X : Scheme.{u}) [IsNoetherian X]
    (P : X.Modules → Prop) (hzero : P (⊤_ X.Modules))
    (hext : ∀ S : ShortComplex X.Modules, S.ShortExact →
      _root_.SheafOfModules.IsCoherent S.X₁ → _root_.SheafOfModules.IsCoherent S.X₂ →
      _root_.SheafOfModules.IsCoherent S.X₃ → P S.X₁ → P S.X₃ → P S.X₂)
    (hideal : ∀ {Z : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z]
      (I : (SheafOfModules.unit Z.ringCatSheaf).Submodule),
      I.toSheafOfModules.IsQuasicoherent →
      P ((Scheme.Modules.pushforward i).obj I.toSheafOfModules)) :
    ∀ F : X.Modules, _root_.SheafOfModules.IsCoherent F → P F
```

## Tag 01YH, a lemma

[Tag 01YH](https://stacks.math.columbia.edu/tag/01YH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.IrreducibleSupportDevissage.property_of_irreducible_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/IrreducibleSupportCriterion.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/IrreducibleSupportCriterion.lean#L706).

> A two-out-of-three property of coherent sheaves holds for every sheaf
> supported on the given irreducible closed subset if it holds on proper
> integral closed subschemes and on one generically simple sheaf of full support.

```lean
public theorem property_of_irreducible_support
    (X : Scheme.{u}) [IsNoetherian X]
    (Z₀ : Set X) (hZ₀ : IsClosed Z₀) (_hZ₀irr : IsIrreducible Z₀)
    (ξ : X) (hξ : IsGenericPoint ξ Z₀)
    (P : X.Modules → Prop)
    (hexact : ∀ (S : ShortComplex X.Modules), S.ShortExact →
      S.X₁.IsCoherent → S.X₂.IsCoherent → S.X₃.IsCoherent →
      ((P S.X₁ ∧ P S.X₂ → P S.X₃) ∧
        (P S.X₁ ∧ P S.X₃ → P S.X₂) ∧
        (P S.X₂ ∧ P S.X₃ → P S.X₁)))
    (hproper : ∀ (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i]
      [IsIntegral Z], Set.range i.base ⊂ Z₀ →
      ∀ (I : (SheafOfModules.unit Z.ringCatSheaf).Submodule)
        [I.toSheafOfModules.IsQuasicoherent],
        P ((Scheme.Modules.pushforward i).obj I.toSheafOfModules))
    (hgeneric : ∃ G : X.Modules,
      G.IsCoherent ∧ SheafOfModules.supp G = Z₀ ∧
      Stacks.ClosedImmersion.StalkKilledByMaximalIdeal G ξ ∧
      (letI : Module (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) G.val ξ
       Module.length (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) = 1) ∧
      P G) :
    ∀ F : X.Modules, F.IsCoherent → SheafOfModules.supp F ⊆ Z₀ → P F
```

## Tag 01YI, a lemma

[Tag 01YI](https://stacks.math.columbia.edu/tag/01YI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentDevissage.property_of_isCoherent_of_generic_stalk_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/GenericStalkCriterion.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/GenericStalkCriterion.lean#L166).

> **[Stacks, Tag 01YI].** Let `X` be a nonempty Noetherian scheme and let `P` be a property of
> coherent `𝒪_X`-modules such that
>
> 1. for a short exact sequence of coherent modules, if two out of three have `P` then so does the
>    third, and
> 2. every integral closed subscheme `i : Z ⟶ X` with generic point `ξ` carries some coherent
>    module `𝒢` with `Supp 𝒢` the range of `i`, with `𝒢_ξ` annihilated by `𝔪_ξ` and of length one
>    over `𝒪_{X,ξ}`, and with `P 𝒢`.
>
> Then `P` holds on every coherent `𝒪_X`-module.
>
> Nonemptiness cannot be dropped: on the empty Noetherian scheme hypotheses (1) and (2) hold for
> `P := fun _ => False`, while the zero module is coherent.

```lean
public theorem property_of_isCoherent_of_generic_stalk_of_nonempty
    (X : Scheme.{u}) [IsNoetherian X] (hX : Nonempty X) (P : X.Modules → Prop)
    (hexact : ∀ S : ShortComplex X.Modules, S.ShortExact →
      _root_.SheafOfModules.IsCoherent S.X₁ → _root_.SheafOfModules.IsCoherent S.X₂ →
      _root_.SheafOfModules.IsCoherent S.X₃ →
      ((P S.X₁ ∧ P S.X₂ → P S.X₃) ∧
        (P S.X₁ ∧ P S.X₃ → P S.X₂) ∧
        (P S.X₂ ∧ P S.X₃ → P S.X₁)))
    (hgeneric : ∀ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i → IsIntegral Z →
      ∀ ξ : X, IsGenericPoint ξ (Set.range i.base) →
      ∃ G : X.Modules, _root_.SheafOfModules.IsCoherent G ∧
        SheafOfModules.supp G = Set.range i.base ∧
        Stacks.ClosedImmersion.StalkKilledByMaximalIdeal G ξ ∧
        (letI : Module (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) G.val ξ
         Module.length (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) = 1) ∧
        P G) :
    ∀ F : X.Modules, _root_.SheafOfModules.IsCoherent F → P F
```

**`Stacks.AlgebraicGeometry.GenericRankOneDevissage.property_of_genericRankOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericRankOneDevissage/Basic.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericRankOneDevissage/Basic.lean#L217). The attribute's comment: “corrected: the source statement is false on the empty scheme, where condition (2) is vacuous and the identically false property satisfies both hypotheses, so `P` on the zero module is added”.

> **The dévissage criterion of [Stacks, Tag 01YI], with the zero module added to its
> hypotheses.** On a Noetherian scheme `X`, a property `P` of coherent modules which holds for the
> zero module, propagates along a short exact sequence of coherent modules from any two of its
> terms to the third, and holds for one coherent module supported exactly on each integral closed
> subscheme with generic stalk killed by the maximal ideal there and of length one over it, holds
> for every coherent module.
>
> The criterion of [Stacks, Tag 01YG] reduces this to the direct images of quasi-coherent ideals
> on integral closed subschemes, which is
> `pushforward_ideal_property_of_genericRankOne`. The hypothesis on the zero module cannot be
> dropped: on the empty scheme, which is Noetherian and has no integral closed subscheme, the
> identically false property satisfies the other two hypotheses.

```lean
theorem property_of_genericRankOne (X : Scheme.{u}) [IsNoetherian X]
    (P : X.Modules → Prop) (hzero : P (⊤_ X.Modules))
    (hexact : ∀ S : ShortComplex X.Modules, S.ShortExact →
      S.X₁.IsCoherent → S.X₂.IsCoherent → S.X₃.IsCoherent →
      ((P S.X₁ ∧ P S.X₂ → P S.X₃) ∧
        (P S.X₁ ∧ P S.X₃ → P S.X₂) ∧
        (P S.X₂ ∧ P S.X₃ → P S.X₁)))
    (hgeneric : ∀ (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z]
      (ξ : X), IsGenericPoint ξ (Set.range i.base) →
      ∃ G : X.Modules, G.IsCoherent ∧
        SheafOfModules.supp G = Set.range i.base ∧
        Stacks.ClosedImmersion.StalkKilledByMaximalIdeal G ξ ∧
        (letI : Module (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) G.val ξ
         Module.length (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) = 1) ∧
        P G) :
    ∀ F : X.Modules, F.IsCoherent → P F
```

**`Stacks.AlgebraicGeometry.GenericRankOneDevissage.property_of_genericRankOne_of_exists_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericRankOneDevissage/Basic.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericRankOneDevissage/Basic.lean#L253). The attribute's comment: “corrected: the source statement is false on the empty scheme, where condition (2) is vacuous and the identically false property satisfies both hypotheses, so the existence of one integral closed subscheme is added”.

> **The dévissage criterion of [Stacks, Tag 01YI], with one integral closed subscheme added to
> its hypotheses.** On a Noetherian scheme carrying at least one integral closed subscheme, a
> property `P` of coherent modules satisfying conditions (1) and (2) of [Stacks, Tag 01YI] holds
> for every coherent module.
>
> Condition (2) at that one subscheme produces a coherent module for which `P` holds, and
> condition (1) then carries `P` to the zero module, so the hypothesis of
> `property_of_genericRankOne` is met. The added hypothesis is implied by `Nonempty X` and
> implies it, and it cannot be dropped: on the empty scheme the identically false property
> satisfies conditions (1) and (2) and fails for the coherent zero module.

```lean
theorem property_of_genericRankOne_of_exists_isIntegral (X : Scheme.{u}) [IsNoetherian X]
    (hne : ∃ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i ∧ IsIntegral Z)
    (P : X.Modules → Prop)
    (hexact : ∀ S : ShortComplex X.Modules, S.ShortExact →
      S.X₁.IsCoherent → S.X₂.IsCoherent → S.X₃.IsCoherent →
      ((P S.X₁ ∧ P S.X₂ → P S.X₃) ∧
        (P S.X₁ ∧ P S.X₃ → P S.X₂) ∧
        (P S.X₂ ∧ P S.X₃ → P S.X₁)))
    (hgeneric : ∀ (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z]
      (ξ : X), IsGenericPoint ξ (Set.range i.base) →
      ∃ G : X.Modules, G.IsCoherent ∧
        SheafOfModules.supp G = Set.range i.base ∧
        Stacks.ClosedImmersion.StalkKilledByMaximalIdeal G ξ ∧
        (letI : Module (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) G.val ξ
         Module.length (X.presheaf.stalk ξ) (G.presheaf.stalk ξ) = 1) ∧
        P G) :
    ∀ F : X.Modules, F.IsCoherent → P F
```

## Tag 01YL, a lemma

[Tag 01YL](https://stacks.math.columbia.edu/tag/01YL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.HigherRankIrreducibleDevissage.property_irreducible_higher_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/HigherRankIrreducibleCriterion.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/HigherRankIrreducibleCriterion.lean#L1080).

> **[Stacks, Tag 01YL], in the corrected form.** Let `X` be a Noetherian scheme, `Z₀` an
> irreducible closed subset with generic point `ξ`, and `P` a property of coherent modules which
> holds for the zero module, is stable under extensions of coherent modules, descends from a
> nonempty finite direct sum, holds for the direct image of every quasi-coherent sheaf of ideals on
> every integral closed subscheme strictly inside `Z₀`, and admits one coherent `G` of support
> exactly `Z₀` whose stalk at `ξ` is annihilated by the maximal ideal there and which has, inside
> every ideal multiple `J·G` with `J_ξ` the whole local ring, a quasi-coherent subsheaf agreeing
> with `G` at `ξ` for which `P` holds. Then `P` holds for every coherent module whose support is
> contained in `Z₀`.
>
> The correction is the hypothesis `hzero`: the source's four conditions do not list `P` for the
> zero module and do not imply it, and without it the statement is false. See this file's
> implementation notes for the counterexample.

```lean
public theorem property_irreducible_higher_rank
    (X : Scheme.{u}) [IsNoetherian X]
    (Z₀ : Set X) (hZ₀ : IsClosed Z₀)
    (ξ : X) (hξ : IsGenericPoint ξ Z₀)
    (P : X.Modules → Prop)
    (hzero : P (⊤_ X.Modules))
    (hext : ∀ (S : ShortComplex X.Modules), S.ShortExact →
      S.X₁.IsCoherent → S.X₂.IsCoherent → S.X₃.IsCoherent →
      P S.X₁ → P S.X₃ → P S.X₂)
    (hsum : ∀ (F : X.Modules), F.IsCoherent →
      (∃ n : ℕ, P (∏ᶜ (fun _ : Fin (n + 1) => F))) → P F)
    (hproper : ∀ (I : X.IdealSheafData) [IsIntegral I.subscheme],
      (I.support : Set X) ⊆ Z₀ → (I.support : Set X) ≠ Z₀ →
      ∀ (H : (SheafOfModules.unit I.subscheme.ringCatSheaf).Submodule)
        [H.toSheafOfModules.IsQuasicoherent],
        P ((Scheme.Modules.pushforward I.subschemeι).obj H.toSheafOfModules))
    (hgeneric : ∃ (G : X.Modules), G.IsCoherent ∧
      (∀ x : X, x ∈ Z₀ ↔ Nontrivial (G.presheaf.stalk x)) ∧
      Tag01YEStalkBridge.IsMaximalIdealAnnihilated G ξ ∧
      (∀ (J : X.IdealSheafData), ξ ∉ J.support →
        ∃ (G' : G.Submodule),
          G'.toSheafOfModules.IsQuasicoherent ∧
          (∀ (U : X.affineOpens) (s : Γ(G'.toSheafOfModules, U.1)),
            (Scheme.Modules.Hom.app G'.ι U.1 s : Γ(G, U.1)) ∈
              J.ideal U • (⊤ : Submodule Γ(X, U.1) Γ(G, U.1))) ∧
          Function.Surjective
            (((TopCat.Presheaf.stalkFunctor Ab ξ).map
              (Scheme.Modules.Hom.mapPresheaf G'.ι)).hom) ∧
          P G'.toSheafOfModules)) :
    ∀ (F : X.Modules), F.IsCoherent →
      (∀ x : X, Nontrivial (F.presheaf.stalk x) → x ∈ Z₀) → P F
```

## Tag 01YM, a lemma

[Tag 01YM](https://stacks.math.columbia.edu/tag/01YM) in the Stacks Project.

**`Stacks.AlgebraicGeometry.NoetherianDevissage.property_higher_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentDevissage/NoetherianDevissage.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentDevissage/NoetherianDevissage.lean#L82). The attribute's comment: “plus P on the zero sheaf, which conditions (1) and (2) do not give”.

> **The dévissage of coherent sheaves on a Noetherian scheme.** A property closed under
> extensions, descending from a nonempty finite direct sum, and holding for a suitable coherent
> module at every integral closed subscheme, holds for every coherent module.

```lean
theorem property_higher_rank [IsNoetherian X] (P : X.Modules → Prop)
    (hzero : P (⊤_ X.Modules))
    (hext : ∀ S : ShortComplex X.Modules, S.ShortExact →
      S.X₁.IsCoherent → S.X₂.IsCoherent → S.X₃.IsCoherent → P S.X₁ → P S.X₃ → P S.X₂)
    (hsum : ∀ F : X.Modules, F.IsCoherent →
      (∃ n : ℕ, P (∏ᶜ fun _ : Fin (n + 1) => F)) → P F)
    (hgeneric : ∀ (I : X.IdealSheafData) [IsIntegral I.subscheme],
      ∃ G : X.Modules, G.IsCoherent ∧
        (∀ x : X, x ∈ I.support ↔ Nontrivial (G.presheaf.stalk x)) ∧
        Tag01YEStalkBridge.IsMaximalIdealAnnihilated G
          (I.subschemeι (genericPoint I.subscheme)) ∧
        (∀ J : X.IdealSheafData,
          I.subschemeι (genericPoint I.subscheme) ∉ J.support →
          ∃ G' : G.Submodule,
            G'.toSheafOfModules.IsCoherent ∧
            (∀ (U : X.affineOpens) (s : Γ(G'.toSheafOfModules, U.1)),
              (Scheme.Modules.Hom.app G'.ι U.1 s : Γ(G, U.1)) ∈
                J.ideal U • (⊤ : Submodule Γ(X, U.1) Γ(G, U.1))) ∧
            Function.Surjective
              (((TopCat.Presheaf.stalkFunctor Ab
                (I.subschemeι (genericPoint I.subscheme))).map
                  (Scheme.Modules.Hom.mapPresheaf G'.ι)).hom) ∧
            P G'.toSheafOfModules)) :
    ∀ F : X.Modules, F.IsCoherent → P F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.12, Tag 01YC](https://stacks.math.columbia.edu/tag/01YC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
