---
declaration: section
origin: cited
lean: DerivedHomAway.tfae_ext_localization_vanishing, exists_isRadical_ideal_isDerivedCompleteAt, isDerivedCompleteModule_of_isAdicComplete_and_adicCompletion_surjective, IsDerivedComplete, IsDerivedCompleteModule, isAdicComplete_iff_isDerivedCompleteModule_and_iInf_pow_smul_top_eq_bot, AdicWeakSerre.derivedCompleteModules_isWeakSerreClass_and_homology_iff, subsingleton_of_isDerivedCompleteModule_of_quotient_smul
statement: formalized
proof: formalized
---

# 15.93 Derived Completion

Section 15.93 of the Stacks Project, [Tag 091N](https://stacks.math.columbia.edu/tag/091N). 25 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 091P, a lemma

[Tag 091P](https://stacks.math.columbia.edu/tag/091P) in the Stacks Project.

**`DerivedHomAway.tfae_ext_localization_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionVanishing/VanishingCriteria.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionVanishing/VanishingCriteria.lean#L599).

> The cohomology of `RHom_A(A_f, K)` is `Ext_A(A_f, K)`. Moreover, the
> following are equivalent: all those Ext groups vanish; `K` is right orthogonal to every object
> of `D(A_f)`; `T(K, f)` vanishes; every `T(H^p(K), f)` vanishes; both
> `Hom_A(A_f, H^p(K))` and `Ext^1_A(A_f, H^p(K))` vanish for every `p`;
> `RHom_A(A_f, K)` vanishes; and `(x_n) ↦ (x_n - f x_{n+1})` is an isomorphism on the product
> of countably many copies of `K`.

```lean
public theorem tfae_ext_localization_vanishing (A : Type u) [CommRing A] (f : A)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let Af : Type u := Localization.Away f
    let AfA := ModuleCat.of A Af
    let sAf := (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj AfA
    let tower := Functor.ofOpSequence (X := fun _ : ℕ => K) (fun _ => f • 𝟙 K)
    IsDerivedLimit tower (derivedHomFromAway A f K) ∧
      Nonempty (∀ n : ℤ,
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj
      (derivedHomFromAway A f K)) ≃+
        DerivedCategory.Ext sAf K n) ∧
      List.TFAE
        [ ∀ n : ℤ, Subsingleton (DerivedCategory.Ext sAf K n)
        , ∀ E : DerivedCategory (ModuleCat.{u} Af),
            Subsingleton
              (((ModuleCat.restrictScalars.{u} (algebraMap A Af)).mapDerivedCategory.obj E) ⟶ K)
        , ∃ L : DerivedCategory (ModuleCat.{u} A), IsDerivedLimit tower L ∧ IsZero L
        , ∀ p : ℤ,
            let Hp := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj K
            let sHp := (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj Hp
            let towerHp := Functor.ofOpSequence (X := fun _ : ℕ => sHp) (fun _ => f • 𝟙 sHp)
            ∃ L : DerivedCategory (ModuleCat.{u} A), IsDerivedLimit towerHp L ∧ IsZero L
        , ∀ p : ℤ,
            let Hp := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj K
            Subsingleton (AfA ⟶ Hp) ∧ Subsingleton (Abelian.zExt AfA Hp 1)
        , IsZero (derivedHomFromAway A f K)
        , IsIso (Pi.lift fun n : ℕ =>
            Pi.π (fun _ : ℕ => K) n - f • Pi.π (fun _ : ℕ => K) (n + 1)) ]
```

## Tag 091Q, a lemma

[Tag 091Q](https://stacks.math.columbia.edu/tag/091Q) in the Stacks Project.

**`exists_isRadical_ideal_isDerivedCompleteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean#L174).

> For `K ∈ D(A)`, the elements `f : A` at which `K` is derived complete —
> equivalently, for which the derived limit of `⋯ → K → K`, with every transition map
> multiplication by `f`, is zero — are precisely the elements of a radical ideal of `A`.

```lean
public theorem exists_isRadical_ideal_isDerivedCompleteAt (A : Type u) [CommRing A]
    (K : DerivedCategory (ModuleCat.{v} A))
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))] :
    ∃ I : Ideal A, I.IsRadical ∧ ∀ f : A, f ∈ I ↔ IsDerivedCompleteAt K f
```

## Tag 091R, a lemma

[Tag 091R](https://stacks.math.columbia.edu/tag/091R) in the Stacks Project.

**`isDerivedCompleteModule_of_isAdicComplete_and_adicCompletion_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean#L418).

> An `I`-adically complete module is derived complete with respect to `I`. Conversely, for a
> finitely generated ideal `I`, derived completeness makes the canonical map to the `I`-adic
> completion surjective.

```lean
public theorem isDerivedCompleteModule_of_isAdicComplete_and_adicCompletion_surjective
    (A : Type u) [CommRing A] (I : Ideal A)
    (M : Type v) [AddCommGroup M] [Module A M]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))] :
    (IsAdicComplete I M → IsDerivedCompleteModule I (ModuleCat.of A M)) ∧
      (I.FG → IsDerivedCompleteModule I (ModuleCat.of A M) →
        Function.Surjective (AdicCompletion.of I M))
```

## Tag 091S, a definition

[Tag 091S](https://stacks.math.columbia.edu/tag/091S) in the Stacks Project.

**`IsDerivedComplete`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete.lean#L172). The attribute's comment: “(1)”.

> `K` is derived complete with respect to the ideal `I` if `T(K,f) = 0` for every `f ∈ I`.

```lean
def IsDerivedComplete {C : Type*} [Category C] [Preadditive C] [Linear A C]
    [HasProductsOfShape ℕ C] (I : Ideal A) (K : C) : Prop
```

**`IsDerivedCompleteModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete.lean#L378). The attribute's comment: “(2)”.

> An `A`-module is derived complete with respect to `I` when the corresponding object of
> `D(A)`, concentrated in degree zero, is derived complete.

```lean
def IsDerivedCompleteModule (I : Ideal A) (M : ModuleCat.{v} A) : Prop
```

## Tag 091T, a proposition

[Tag 091T](https://stacks.math.columbia.edu/tag/091T) in the Stacks Project.

**`isAdicComplete_iff_isDerivedCompleteModule_and_iInf_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteAdic.lean#L454).

> For a finitely generated ideal `I`, an `A`-module `M` is `I`-adically complete if and only
> if it is derived complete with respect to `I` and the intersection of the submodules `I ^ n M`
> is zero.

```lean
public theorem isAdicComplete_iff_isDerivedCompleteModule_and_iInf_pow_smul_top_eq_bot
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : Type v) [AddCommGroup M] [Module A M]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))] :
    IsAdicComplete I M ↔
      IsDerivedCompleteModule I (ModuleCat.of A M) ∧
        ⨅ n : ℕ, I ^ n • (⊤ : Submodule A M) = ⊥
```

## Tag 091U, a lemma

[Tag 091U](https://stacks.math.columbia.edu/tag/091U) in the Stacks Project.

**`AdicWeakSerre.derivedCompleteModules_isWeakSerreClass_and_homology_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/AdicWeakSerreClass.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/AdicWeakSerreClass.lean#L97).

> **Stacks 091U.** The derived complete modules with respect to `I` form a weak Serre
> subcategory of `ModuleCat A`. Moreover, an object of `D(A)` is derived complete exactly when all
> of its cohomology modules are derived complete.

```lean
public theorem derivedCompleteModules_isWeakSerreClass_and_homology_iff
    (A : Type u) [CommRing A] (I : Ideal A) :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{v} A) :=
      moduleCat_hasExactLimitsOfShape_discrete.{v} A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let C : ObjectProperty (ModuleCat.{v} A) :=
      fun M => IsDerivedCompleteModule I M
    C.IsWeakSerreClass ∧
      ∀ K : DerivedCategory (ModuleCat.{v} A),
        (∀ n : ℤ, C ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) n).obj K)) ↔
          IsDerivedComplete I K
```

## Tag 09B9, a lemma

[Tag 09B9](https://stacks.math.columbia.edu/tag/09B9) in the Stacks Project.

**`subsingleton_of_isDerivedCompleteModule_of_quotient_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NakayamaModule.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/NakayamaModule.lean#L256).

> **Stacks 09B9.** A derived complete module with zero reduction modulo a finitely generated
> ideal is zero.

```lean
theorem subsingleton_of_isDerivedCompleteModule_of_quotient_smul
    (A : Type u) [CommRing A]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))]
    (I : Ideal A) (M : ModuleCat.{v} A) (hI : I.FG)
    (hM : IsDerivedCompleteModule I M)
    (hMI : Subsingleton (M ⧸ (I • ⊤ : Submodule A M))) : Subsingleton M
```

## Tag 0A05, a lemma

[Tag 0A05](https://stacks.math.columbia.edu/tag/0A05) in the Stacks Project.

**`isDerivedComplete_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PseudoCoherentComplete.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PseudoCoherentComplete.lean#L232).

> **Stacks 0A05.** A pseudo-coherent object over a ring that is derived complete with respect
> to `I` is itself derived complete with respect to `I`. Pseudo-coherence is spelled out as in
> Stacks 064Q (2): `K` is represented by a bounded-above complex of finite free modules.

```lean
theorem isDerivedComplete_of_isPseudoCoherent
    (A : Type u) [CommRing A] (I : Ideal A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    IsDerivedCompleteModule I (ModuleCat.of A A) →
      ∀ K : DerivedCategory (ModuleCat.{u} A),
        (∃ E : CochainComplex (ModuleCat.{u} A) ℤ,
            ((∃ b : ℤ, E.IsStrictlyLE b) ∧
              ∀ i : ℤ, Module.Finite A (E.X i) ∧ Module.Free A (E.X i)) ∧
            Nonempty (DerivedCategory.Q.obj E ≅ K)) →
          IsDerivedComplete I K
```

## Tag 0A6C, a lemma

[Tag 0A6C](https://stacks.math.columbia.edu/tag/0A6C) in the Stacks Project.

**`DerivedHomLocalization.derivedHom_localization_comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionLocalizationComp.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionLocalizationComp.lean#L48).

> **Stacks 0A6C.** For `f, g ∈ A` and `K ∈ D(A)`, there is a canonical isomorphism
> `RHom_A(A_f, RHom_A(A_g, K)) ≅ RHom_A(A_{fg}, K)`.

```lean
public noncomputable def derivedHom_localization_comp {A : Type u} [CommRing A]
    [HasDerivedCategory (ModuleCat A)] (f g : A) (K : DerivedCategory (ModuleCat A)) :
    let D := StacksDraft.DerivedHom.derivedHomAdjunction (R := A)
    let away (a : A) := DerivedCategory.Q.obj
      ((CochainComplex.singleFunctor (ModuleCat A) 0).obj
        (ModuleCat.of A (Localization.Away a)))
    D.hom.obj (Opposite.op (away f), D.hom.obj (Opposite.op (away g), K)) ≅
      D.hom.obj (Opposite.op (away (f * g)), K)
```

## Tag 091V, a lemma

[Tag 091V](https://stacks.math.columbia.edu/tag/091V) in the Stacks Project.

**`CechCompletion.cechCompletion_isReflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CechCompletion.lean, line 1131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CechCompletion.lean#L1131).

> Derived completion with respect to the ideal generated by a finite family
> `f` is computed functorially as derived Hom from its extended alternating Čech complex. It is
> derived complete, and the natural map from an object to its completion induces a bijection on
> morphisms into every derived-complete object.

```lean
public theorem cechCompletion_isReflection (A : Type u) [CommRing A] {r : ℕ}
    (f : Fin r → A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    ∃ η : Functor.id (DerivedCategory (ModuleCat.{u} A)) ⟶ cechCompletionFunctor A f,
      (∀ K, IsDerivedComplete (Ideal.span (Set.range f))
        ((cechCompletionFunctor A f).obj K)) ∧
      ∀ (K E : DerivedCategory (ModuleCat.{u} A)),
        IsDerivedComplete (Ideal.span (Set.range f)) E →
          Function.Bijective
            (fun g : (cechCompletionFunctor A f).obj K ⟶ E ↦ η.app K ≫ g)
```

## Tag 0G3E, a remark

[Tag 0G3E](https://stacks.math.columbia.edu/tag/0G3E) in the Stacks Project.

**`DerivedCompletion.derivedCompletion_isReflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CechReflection.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CechReflection.lean#L69).

> Derived completion with respect to a finitely generated ideal is the reflection into the
> derived-complete objects: it takes derived-complete values, and its unit `K ⟶ K̂` induces a
> bijection from maps out of `K̂` to maps out of `K` whenever the target is derived complete.

```lean
public theorem derivedCompletion_isReflection (A : Type u) [CommRing A] {r : ℕ}
    (f : Fin r → A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    (∀ K, IsDerivedComplete (Ideal.span (Set.range f))
      ((derivedCompletionFunctor A f).obj K)) ∧
    ∀ (K E : DerivedCategory (ModuleCat.{u} A)),
      IsDerivedComplete (Ideal.span (Set.range f)) E →
        Function.Bijective
          (fun g : (derivedCompletionFunctor A f).obj K ⟶ E ↦
            (derivedCompletionUnit A f).app K ≫ g)
```

## Tag 0A6D, a lemma

[Tag 0A6D](https://stacks.math.columbia.edu/tag/0A6D) in the Stacks Project.

**`CechCompletion.isZero_cechCompletion_of_isIso_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CechCompletionVanishing.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CechCompletionVanishing.lean#L129).

> **Stacks 0A6D.** Let `I` be the ideal generated by a finite family `g`. If some `x ∈ I`
> acts invertibly on `K ∈ D(A)`, then the derived completion of `K` with respect to `I` is zero.

```lean
public theorem isZero_cechCompletion_of_isIso_smul (A : Type u) [CommRing A] {r : ℕ}
    (g : Fin r → A) (K : DerivedCategory (ModuleCat.{u} A))
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))]
    {x : A} (hx : x ∈ Ideal.span (Set.range g)) [IsIso (x • 𝟙 K)] :
    IsZero ((cechCompletionFunctor A g).obj K)
```

## Tag 0A6E, a lemma

[Tag 0A6E](https://stacks.math.columbia.edu/tag/0A6E) in the Stacks Project.

**`DerivedHomCechCompletion.derivedHom_cechCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionHom.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionHom.lean#L276).

> For a finite family `f` generating an ideal of `A`, derived completion commutes naturally
> with derived Hom in its target: `RHom_A(K, L)^∧ ≅ RHom_A(K, L^∧)`. If `η : K ⟶ K^∧` is the
> reflection unit, then precomposition with `η` is the natural isomorphism
> `RHom_A(K^∧, L^∧) ≅ RHom_A(K, L^∧)`.

```lean
public theorem derivedHom_cechCompletion (A : Type u) [CommRing A] {r : ℕ}
    (f : Fin r → A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    let C := DerivedCategory (ModuleCat.{u} A)
    let D := StacksDraft.DerivedHom.derivedHomAdjunction (R := A)
    let F := CechCompletion.cechCompletionFunctor A f
    ∃ η : Functor.id C ⟶ F,
      (∀ K, IsDerivedComplete (Ideal.span (Set.range f)) (F.obj K)) ∧
      (∀ (K E : C), IsDerivedComplete (Ideal.span (Set.range f)) E →
        Function.Bijective (fun g : F.obj K ⟶ E ↦ η.app K ≫ g)) ∧
      Nonempty
        ((D.hom ⋙ F) ≅
          (((CategoryTheory.Prod.fst Cᵒᵖ C).prod'
            (CategoryTheory.Prod.snd Cᵒᵖ C ⋙ F)) ⋙ D.hom)) ∧
      ∃ e :
          ((((CategoryTheory.Prod.fst Cᵒᵖ C ⋙ F.op).prod'
              (CategoryTheory.Prod.snd Cᵒᵖ C ⋙ F)) ⋙ D.hom) ≅
            (((CategoryTheory.Prod.fst Cᵒᵖ C).prod'
              (CategoryTheory.Prod.snd Cᵒᵖ C ⋙ F)) ⋙ D.hom)),
        ∀ (K L : C), e.hom.app (Opposite.op K, L) =
          D.hom.map
            (show (Opposite.op (F.obj K), F.obj L) ⟶ (Opposite.op K, F.obj L) from
              ((η.app K).op, 𝟙 (F.obj L)))
```

## Tag 091W, a lemma

[Tag 091W](https://stacks.math.columbia.edu/tag/091W) in the Stacks Project.

**`isDerivedComplete_of_isMilnorTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete.lean#L449).

> Let `A` be a ring and `I ⊂ A` an ideal. Let `(Kₙ)` be an inverse system of objects of `D(A)`
> (objects `Ksys n`, transition maps `Kt n : Ksys (n+1) ⟶ Ksys n`) such that for every `f ∈ I` and
> every `n` the scalar `f` acts nilpotently on `Ksys n`. Let `F` be an additive `A`-linear
> endofunctor of `D(A)`, standing for `K ⊗ᴸ (-)`. Then any derived limit `K'` of the tower
> `(F.obj (Ksys n))` is derived complete with respect to `I`.

```lean
theorem
    isDerivedComplete_of_isMilnorTriangle (I : Ideal A) (Ksys : ℕ → DerivedCategory (ModuleCat A))
    (Kt : ∀ n, Ksys (n + 1) ⟶ Ksys n) (hnil : ∀ f ∈ I, ∀ n, IsNilpotent (f • (1 : End (Ksys n))))
    (F : DerivedCategory (ModuleCat A) ⥤ DerivedCategory (ModuleCat A)) [F.Additive] [F.Linear A]
    (K' : DerivedCategory (ModuleCat A)) {ι : K' ⟶ ∏ᶜ fun n => F.obj (Ksys n)}
    {δ : (∏ᶜ fun n => F.obj (Ksys n)) ⟶ K'⟦(1 : ℤ)⟧}
    (hMilnor : IsMilnorTriangle (fun n => F.obj (Ksys n)) (fun n => F.map (Kt n)) K' ι δ) :
    IsDerivedComplete I K'
```

## Tag 0BKC, a situation

[Tag 0BKC](https://stacks.math.columbia.edu/tag/0BKC) in the Stacks Project.

**`koszulPowerComplexes_form_inverseSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteKoszulPowers.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteKoszulPowers.lean#L416). References: SGA 2 II (Lemma9), “partial”.

> **Stacks Project, Tag 0BKC.** The Koszul complexes on the positive powers of a finite
> sequence form an inverse system. The displayed formula says that its transition maps are the
> maps of Koszul complexes induced by multiplying the `i`-th basis vector by the appropriate
> power of `f i`. The system is compatible both with its canonical maps from `A` and, under the
> natural identifications in degree zero, with the inverse system of quotients by the ideals
> generated by the powered sequences.

```lean
public theorem koszulPowerComplexes_form_inverseSystem
    {A : Type u} [CommRing A] {r : ℕ} (f : Fin r → A) :
    let K : ℕ → ChainComplex (ModuleCat.{u} A) ℕ := fun n ↦
      Koszul.seqComplex (fun i ↦ f i ^ (n + 1))
    let Q : ℕ → ModuleCat.{u} A := fun n ↦
      ModuleCat.of A (A ⧸ Ideal.span (Set.range fun i ↦ f i ^ (n + 1)))
    ∃ (τ : ∀ (m n : ℕ), n ≤ m → (K m ⟶ K n))
      (σ : ∀ (m n : ℕ), n ≤ m → (Q m ⟶ Q n))
      (e : ∀ n, (K n).homology 0 ≅ Q n)
      (η : ∀ n, (ChainComplex.single₀ (ModuleCat.{u} A)).obj (ModuleCat.of A A) ⟶ K n),
      (∀ n, τ n n (le_refl n) = 𝟙 (K n)) ∧
      (∀ (k m n : ℕ) (hkm : m ≤ k) (hmn : n ≤ m),
        τ k m hkm ≫ τ m n hmn = τ k n (hmn.trans hkm)) ∧
      (∀ n, σ n n (le_refl n) = 𝟙 (Q n)) ∧
      (∀ (k m n : ℕ) (hkm : m ≤ k) (hmn : n ≤ m),
        σ k m hkm ≫ σ m n hmn = σ k n (hmn.trans hkm)) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m) (j : ℕ) (v : Fin j → Fin r → A),
        (τ m n hmn).f j
            ⟨ExteriorAlgebra.ιMulti A j v, Koszul.ιMulti_mem j v⟩ =
          ⟨ExteriorAlgebra.ιMulti A j
              (fun k i ↦ f i ^ (m - n) * v k i),
            Koszul.ιMulti_mem j (fun k i ↦ f i ^ (m - n) * v k i)⟩) ∧
      (∀ (n : ℕ) (a : A),
        (η n).f 0 a =
          a • ⟨ExteriorAlgebra.ιMulti A 0 (fun i ↦ Fin.elim0 i),
            Koszul.ιMulti_mem 0 (fun i ↦ Fin.elim0 i)⟩) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m), η m ≫ τ m n hmn = η n) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m),
        ModuleCat.ofHom
              (Ideal.span (Set.range fun i ↦ f i ^ (m + 1))).mkQ ≫
            σ m n hmn =
          ModuleCat.ofHom
            (Ideal.span (Set.range fun i ↦ f i ^ (n + 1))).mkQ) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m),
        (e m).inv ≫ HomologicalComplex.homologyMap (τ m n hmn) 0 ≫ (e n).hom =
          σ m n hmn) ∧
      ∀ n,
        (HomologicalComplex.singleObjHomologySelfIso
              (ComplexShape.down ℕ) 0 (ModuleCat.of A A)).inv ≫
            HomologicalComplex.homologyMap (η n) 0 ≫ (e n).hom =
          ModuleCat.ofHom
            (Ideal.span (Set.range fun i ↦ f i ^ (n + 1))).mkQ
```

## Tag 091Y, a lemma

[Tag 091Y](https://stacks.math.columbia.edu/tag/091Y) in the Stacks Project.

**`AdicKoszul.rlim_derivedTensor_koszulPowers_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/AdicKoszulTower.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/AdicKoszulTower.lean#L244).

> **Stacks 091Y.** Let `I` be generated by a finite sequence `f`. For any inverse system whose
> `n`-th term is the Koszul complex on `f i ^ (n + 1)`, the derived limit after derived tensoring
> with `K` is derived complete with respect to `I`.

```lean
theorem rlim_derivedTensor_koszulPowers_isDerivedComplete
    {r : ℕ} (f : Fin r → A)
    (τ : ∀ n : ℕ,
      Koszul.seqComplex (fun i ↦ f i ^ (n + 2)) ⟶
        Koszul.seqComplex (fun i ↦ f i ^ (n + 1)))
    (T : DerivedTensorProduct A)
    (K K' : DerivedCategory (ModuleCat.{u} A))
    (hRlim : IsDerivedLimit (koszulPowerSystem f τ ⋙ T.tensor.obj K) K') :
    IsDerivedComplete (Ideal.span (Set.range f)) K'
```

## Tag 091Z, a lemma

[Tag 091Z](https://stacks.math.columbia.edu/tag/091Z) in the Stacks Project.

**`AdicKoszul.isDerivedComplete_iff_isIso_to_rlim_derivedTensor_koszulPowers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/AdicDerivedCompletionKoszul.lean, line 778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/AdicDerivedCompletionKoszul.lean#L778).

> The Koszul derived limit and its canonical natural map exist for every complex. A complex is
> derived complete for the ideal generated by `f` if and only if the component of this map is an
> isomorphism. The ring and module universes are independent; only the tensor calculation is
> enlarged using `ULift`.

```lean
public theorem isDerivedComplete_iff_isIso_to_rlim_derivedTensor_koszulPowers
    {r : ℕ} (f : Fin r → A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct (ULift.{v} A)) :
    ∃ C : KoszulPowerCompletion f T, ∀ K : DerivedCategory (ModuleCat.{v} A),
      IsDerivedComplete (Ideal.span (Set.range f)) K ↔
        IsIso (C.unit.app K)
```

## Tag 0920, a lemma

[Tag 0920](https://stacks.math.columbia.edu/tag/0920) in the Stacks Project.

**`AdicKoszulAdjunction.koszulPowerDerivedLimit_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/AdicDerivedCompletion/Adjunction.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/AdicDerivedCompletion/Adjunction.lean#L226).

> For a finite family `f`, the functor whose value at `K` is the derived
> inverse limit of `K ⊗ᴸ Kₙ`, where `Kₙ` runs through the Koszul complexes on the positive
> powers of `f`, is left adjoint to the inclusion of the derived-complete objects into `D(A)`.

```lean
public theorem koszulPowerDerivedLimit_isLeftAdjoint
    (A : Type u) [CommRing A] {r : ℕ} (f : Fin r → A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct (ULift.{v} A))
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))] :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{max u v} (ULift.{v} A)) :=
      moduleCat_hasExactLimitsOfShape_discrete.{max u v} (ULift.{v} A) ℕ
    letI : HasProductsOfShape ℕ
        (DerivedCategory (ModuleCat.{max u v} (ULift.{v} A))) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun K ↦ IsDerivedComplete (Ideal.span (Set.range f)) K
    ∃ L : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory,
      Nonempty (L ⊣ P.ι) ∧
        ∀ K, IsDerivedLimit (AdicKoszul.tensorKoszulPowerSystem f T K)
          ((AdicKoszul.derivedUniverseLift A).obj ((L ⋙ P.ι).obj K))
```

## Tag 0H83, a lemma

[Tag 0H83](https://stacks.math.columbia.edu/tag/0H83) in the Stacks Project.

**`KoszulTensorVanishing.positive_homology_isZero_iff_derivedTensorProduct_mod_ideal_iff_koszul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/KoszulTensorVanishing.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/KoszulTensorVanishing.lean#L605).

> **Stacks Project, Tag 0H83.** For a complex derived complete with respect to the ideal
> generated by a finite sequence, the following are equivalent: it has no positive cohomology,
> its derived reduction modulo that ideal has no positive cohomology, and its derived tensor
> product with the Koszul complex of the sequence has no positive cohomology.

```lean
theorem positive_homology_isZero_iff_derivedTensorProduct_mod_ideal_iff_koszul
    {A : Type u} [CommRing A] {r : ℕ} (f : Fin r → A)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    IsDerivedComplete (Ideal.span (Set.range f)) K →
    let I := Ideal.span (Set.range f)
    let K₁ : DerivedCategory (ModuleCat.{u} A) :=
      DerivedCategory.Q.obj
        ((ComplexShape.embeddingDownNat.extendFunctor (ModuleCat.{u} A)).obj
          (Koszul.seqComplex f))
    let p₁ := ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K)
    let p₂ := ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
        (((canonicalDerivedTensorProductFunctor A).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A (A ⧸ I)))))
    let p₃ := ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
        (((canonicalDerivedTensorProductFunctor A).obj K).obj K₁))
    (p₁ ↔ p₂) ∧ (p₂ ↔ p₃)
```

## Tag 0G1U, a lemma

[Tag 0G1U](https://stacks.math.columbia.edu/tag/0G1U) in the Stacks Project.

**`KoszulTensorVanishing.isZero_of_isDerivedComplete_of_derivedTensorProduct_mod_ideal_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/KoszulTensorVanishing.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/KoszulTensorVanishing.lean#L659).

> **Derived Nakayama lemma, Stacks Project, Tag 0G1U.** A derived-complete complex with
> respect to a finitely generated ideal is zero if its derived reduction modulo that ideal is
> zero.

```lean
theorem isZero_of_isDerivedComplete_of_derivedTensorProduct_mod_ideal_isZero
    {A : Type u} [CommRing A] (I : Ideal A) (hI : I.FG)
    (K : DerivedCategory (ModuleCat.{u} A)) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    IsDerivedComplete I K →
      IsZero
        (((canonicalDerivedTensorProductFunctor A).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A (A ⧸ I)))) →
      IsZero K
```

## Tag 0AAJ, a lemma

[Tag 0AAJ](https://stacks.math.columbia.edu/tag/0AAJ) in the Stacks Project.

**`CompletionAdjunction.derivedCompletion_finiteCohomologicalDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompletionAdjunction.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompletionAdjunction.lean#L593).

> Derived completion along an ideal generated by `r` elements has cohomological amplitude
> contained in `[-r, 0]`: it preserves isomorphisms in positive cohomological degrees and
> epimorphisms in degree zero, and it sends isomorphisms in negative degrees together with a
> monomorphism in degree zero to isomorphisms below degree `-r` and a monomorphism in degree `-r`.

```lean
public theorem derivedCompletion_finiteCohomologicalDimension
    (A : Type u) [CommRing A]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))]
    {r : ℕ} (f : Fin r → A) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun K ↦ IsDerivedComplete (Ideal.span (Set.range f)) K
    ∀ (C : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory),
      (C ⊣ P.ι) →
      ∀ {K L : DerivedCategory (ModuleCat.{u} A)} (φ : K ⟶ L),
        (((∀ i : ℤ, 1 ≤ i →
              IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map φ)) ∧
            Epi ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map φ)) →
          ((∀ i : ℤ, 1 ≤ i →
              IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
                ((C ⋙ P.ι).map φ))) ∧
            Epi ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
              ((C ⋙ P.ι).map φ)))) ∧
        (((∀ i : ℤ, i ≤ -1 →
              IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map φ)) ∧
            Mono ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map φ)) →
          ((∀ i : ℤ, i ≤ -(r : ℤ) - 1 →
              IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
                ((C ⋙ P.ι).map φ))) ∧
            Mono ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(r : ℤ))).map
              ((C ⋙ P.ι).map φ))))
```

## Tag 0BKD, a lemma

[Tag 0BKD](https://stacks.math.columbia.edu/tag/0BKD) in the Stacks Project.

**`AdicFilteredCompletion.exists_derivedCompletion_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/FilteredCompletionSpectralSequence.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/FilteredCompletionSpectralSequence.lean#L184).

> **Stacks 0BKD.** Let `I` be a finitely generated ideal, and let `K^•` be a decreasingly
> filtered complex of `A`-modules. There is a filtered representative `M^•` of the derived
> completion of `K^•` whose canonical spectral sequence consists of derived-complete modules from
> its first page onward and has `E₁^{p,q} ≅ H^{p+q}((gr^pK^•)^∧)`. If the filtration of `K^•` is
> finite in each degree, the spectral sequence is bounded and converges canonically to the
> cohomology of `(K^•)^∧`.

```lean
theorem exists_derivedCompletion_spectralSequence
    (A : Type u) [CommRing A]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))]
    (I : Ideal A) (hI : I.FG)
    (K : FilteredObject (CochainComplex (ModuleCat.{v} A) ℤ) ℤᵒᵖ) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun L ↦ IsDerivedComplete I L
    ∀ (completion : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory),
      (completion ⊣ P.ι) →
    ∃ (M : CochainComplex.Filtered (ModuleCat.{v} A))
      (eTotal : DerivedCategory.Q.obj M.X ≅
        (completion ⋙ P.ι).obj (DerivedCategory.Q.obj K.X))
      (eCohomology : ∀ n : ℤ, M.X.homology n ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) n).obj
          ((completion ⋙ P.ι).obj (DerivedCategory.Q.obj K.X))),
      let E := CochainComplex.Filtered.spectralSequenceFunctor.obj M
      (∀ (r p q : ℤ) (hr : 1 ≤ r),
        IsDerivedCompleteModule I ((E.page r (by omega)).X (p, q))) ∧
      (∀ p q : ℤ, Nonempty
        ((E.page 1 (by omega)).X (p, q) ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{v} A) (p + q)).obj
            ((completion ⋙ P.ι).obj
              (DerivedCategory.Q.obj ((FilteredObject.gr p).obj K))))) ∧
      (K.filtration.IsDegreewiseFinite →
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧
          M.inducedFiltrationStep n a = ⊤ ∧ M.inducedFiltrationStep n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ ↦
              CochainComplex.filtrationSubobject M p n ⊓
                (Subobject.pullback (M.X.d n (n + 1))).obj
                  (CochainComplex.filtrationSubobject M (p + r) (n + 1)) ⊔
                CochainComplex.filtrationSubobject M (p + 1) n)
            (kernelSubobject (M.X.d n (n + 1)) ⊓ CochainComplex.filtrationSubobject M p n ⊔
              CochainComplex.filtrationSubobject M (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ ↦
              CochainComplex.filtrationSubobject M p n ⊓
                (Subobject.«exists» (M.X.d (n - 1) n)).obj
                  (CochainComplex.filtrationSubobject M (p - r) (n - 1)) ⊔
                CochainComplex.filtrationSubobject M (p + 1) n)
            (imageSubobject (M.X.d (n - 1) n) ⊓ CochainComplex.filtrationSubobject M p n ⊔
              CochainComplex.filtrationSubobject M (p + 1) n)) ∧
        (∀ p n : ℤ,
          let C := (Subobject.pullback (M.X.iCycles n)).obj
            (CochainComplex.filtrationSubobject M p n)
          let N := kernelSubobject (M.X.d n (n + 1)) ⊓
            CochainComplex.filtrationSubobject M p n ⊔
            CochainComplex.filtrationSubobject M (p + 1) n
          let B := imageSubobject (M.X.d (n - 1) n) ⊓
            CochainComplex.filtrationSubobject M p n ⊔
            CochainComplex.filtrationSubobject M (p + 1) n
          ∃ (a : (C : ModuleCat.{v} A) ⟶ (N : ModuleCat.{v} A))
            (b : (C : ModuleCat.{v} A) ⟶ (M.inducedFiltrationStep n p : ModuleCat.{v} A))
            (hFH : M.inducedFiltrationStep n (p + 1) ≤ M.inducedFiltrationStep n p)
            (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
              cokernel (Subobject.ofLE _ _ hFH)),
            C.arrow ≫ M.X.iCycles n = a ≫ N.arrow ∧
            C.arrow ≫ M.X.homologyπ n =
              b ≫ (M.inducedFiltrationStep n p).arrow ∧
            a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
              b ≫ cokernel.π (Subobject.ofLE _ _ hFH)))
```

## Tag 0BKE, an example

[Tag 0BKE](https://stacks.math.columbia.edu/tag/0BKE) in the Stacks Project.

**`AdicFilteredCompletion.exists_spectralSequence_derivedCompletion_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/FilteredCompletionTruncation.lean, line 765](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/FilteredCompletionTruncation.lean#L765).

> **Stacks 0BKE.** For a finitely generated ideal `I` and `K ∈ D(A)`, the truncation
> filtration gives a bounded cohomological spectral sequence `S₁^{p,q} ≅ H^{2p+q}(H^{-p}(K)^∧)`
> converging to `H^{p+q}(K^∧)`. After the reindexing `p = -j`, `q = i + 2j` and a shift of the page
> number by one it is a bounded spectral sequence of derived-complete modules with
> `E₂^{i,j} ≅ H^i(H^j(K)^∧)` converging to `H^{i+j}(K^∧)`.

```lean
theorem exists_spectralSequence_derivedCompletion_homology
    (A : Type u) [CommRing A]
    (I : Ideal A) (hI : I.FG) (K : DerivedCategory (ModuleCat.{v} A)) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun L ↦ IsDerivedComplete I L
    ∃ (completion : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory)
      (adj : completion ⊣ P.ι)
      (C : CochainComplex (ModuleCat.{v} A) ℤ)
      (eK : DerivedCategory.Q.obj C ≅ K)
      (T : FilteredObject (CochainComplex (ModuleCat.{v} A) ℤ) ℤᵒᵖ)
      (eUnderlying : T.X ≅ C)
      (eStep : ∀ p : ℤ, T.filtration.obj (op p) ≅ C.truncLE (-p))
      (eStep_ι : ∀ p : ℤ,
        (eStep p).hom ≫ C.ιTruncLE (-p) =
          T.filtration.ι.app (op p) ≫ eUnderlying.hom)
      (hT : T.filtration.IsDegreewiseFinite)
      (M : CochainComplex.Filtered (ModuleCat.{v} A))
      (eTotal : DerivedCategory.Q.obj M.X ≅ (completion ⋙ P.ι).obj K)
      (eCohomology : ∀ n : ℤ, M.X.homology n ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) n).obj
          ((completion ⋙ P.ι).obj K)),
      let S := CochainComplex.Filtered.spectralSequenceFunctor.obj M
      ∃ (E : E₂CohomologicalSpectralSequence (ModuleCat.{v} A))
      (eGr : ∀ p : ℤ,
        DerivedCategory.Q.obj ((FilteredObject.gr p).obj T) ≅
          ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
            ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) (-p)).obj K))⟦p⟧)
      (e₁Filtered : ∀ p q : ℤ, (S.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) (p + q)).obj
          ((completion ⋙ P.ι).obj
            (DerivedCategory.Q.obj ((FilteredObject.gr p).obj T))))
      (e₁ : ∀ p q : ℤ, (S.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) (2 * p + q)).obj
          ((completion ⋙ P.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
              ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) (-p)).obj K))))
      (e₂ : ∀ i j : ℤ, (E.page 2).X (i, j) ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).obj
          ((completion ⋙ P.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
              ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) j).obj K))))
      (reindex : ∀ (r i j : ℤ) (hr : 2 ≤ r),
        (E.page r hr).X (i, j) ≅ (S.page (r - 1) (by omega)).X (-j, i + 2 * j))
      (hF : ∀ n : ℤ, Antitone (M.inducedFiltrationStep n)),
      (∀ (r p q : ℤ) (hr : 1 ≤ r),
        IsDerivedCompleteModule I ((S.page r (by omega)).X (p, q))) ∧
      (∀ (r i j : ℤ) (hr : 2 ≤ r),
        IsDerivedCompleteModule I ((E.page r hr).X (i, j))) ∧
      (∀ (r i j : ℤ) (hr : 2 ≤ r),
        (reindex r i j hr).hom ≫ (S.page (r - 1) (by omega)).d
              (-j, i + 2 * j) (-(j - r + 1), (i + r) + 2 * (j - r + 1)) =
          (E.page r hr).d (i, j) (i + r, j - r + 1) ≫
            (reindex r (i + r) (j - r + 1) hr).hom) ∧
      (∀ n : ℤ, {p : ℤ | ¬ IsZero ((S.page 1 (by omega)).X (p, n - p))}.Finite) ∧
      (∀ n : ℤ, {i : ℤ | ¬ IsZero ((E.page 2).X (i, n - i))}.Finite) ∧
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ M.inducedFiltrationStep n a = ⊤ ∧
        M.inducedFiltrationStep n b = ⊥) ∧
      (∀ p q : ℤ, ∃ (r₀ : ℤ) (hr₀ : 1 ≤ r₀), ∀ (r : ℤ) (hr : r₀ ≤ r),
        (S.page r (by omega)).d (p, q) (p + r, q - r + 1) = 0 ∧
        (S.page r (by omega)).d (p - r, q + r - 1) (p, q) = 0 ∧
        Nonempty ((S.page r (by omega)).X (p, q) ≅
          cokernel (Subobject.ofLE (M.inducedFiltrationStep (p + q) (p + 1))
            (M.inducedFiltrationStep (p + q) p) (hF (p + q) (by omega))))) ∧
      ∀ i j : ℤ, ∃ (r₀ : ℤ) (hr₀ : 2 ≤ r₀), ∀ (r : ℤ) (hr : r₀ ≤ r),
        (E.page r (by omega)).d (i, j) (i + r, j - r + 1) = 0 ∧
        (E.page r (by omega)).d (i - r, j + r - 1) (i, j) = 0 ∧
        Nonempty ((E.page r (by omega)).X (i, j) ≅
          cokernel (Subobject.ofLE (M.inducedFiltrationStep (i + j) (-j + 1))
            (M.inducedFiltrationStep (i + j) (-j)) (hF (i + j) (by omega))))
```

## Tag 0924, a lemma

[Tag 0924](https://stacks.math.columbia.edu/tag/0924) in the Stacks Project.

**`isDerivedComplete_restrictScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteRestrictScalars.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteRestrictScalars.lean#L142).

> A complex of `B`-modules is derived complete for the extension of `I` to
> `B` if and only if its restriction to `A` is derived complete for `I`. Equivalently, the inverse
> image of `D_comp(A, I)` under restriction of scalars is `D_comp(B, I B)`.

```lean
public theorem isDerivedComplete_restrictScalars_iff
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] (φ : A →+* B) (I : Ideal A)
    (L : DerivedCategory (ModuleCat.{w} B)) :
    IsDerivedComplete I ((ModuleCat.restrictScalars φ).mapDerivedCategory.obj L) ↔
      IsDerivedComplete (I.map φ) L
```

## Tag 0925, a lemma

[Tag 0925](https://stacks.math.columbia.edu/tag/0925) in the Stacks Project.

**`CompleteRestrictScalarsEquivalence.restrictScalars_equivalence_derivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompleteRestrictScalarsEquivalence/SmallQuotients.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompleteRestrictScalarsEquivalence/SmallQuotients.lean#L694).

> If `A → B` is flat and induces an isomorphism modulo a finitely generated ideal `I`, then
> restriction of scalars induces an equivalence from the full subcategory of `I B`-derived complete
> objects of `D(B)` to the full subcategory of `I`-derived complete objects of `D(A)`.

```lean
theorem restrictScalars_equivalence_derivedComplete
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) (hI : I.FG) (hflat : Module.Flat A B)
    (hquot : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B) Ideal.le_comap_map)) :
    ∃ hprodA : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)),
    ∃ hprodB : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} B)),
    letI := hprodA
    letI := hprodB
    let completeA : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun K ↦ IsDerivedComplete I K
    let completeB : ObjectProperty (DerivedCategory (ModuleCat.{u} B)) :=
      fun K ↦ IsDerivedComplete (I.map (algebraMap A B)) K
    let res := (ModuleCat.restrictScalars.{u} (algebraMap A B)).mapDerivedCategory
    ∃ hres : ∀ K : completeB.FullSubcategory, completeA (res.obj K.obj),
      Functor.IsEquivalence
        (completeA.lift (completeB.ι ⋙ res) (fun K ↦ hres K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.93, Tag 091N](https://stacks.math.columbia.edu/tag/091N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
