---
declaration: section
origin: cited
lean: NoetherianKoszulProIso.koszulPowerSystem_proIso_quotientPowerSystem, NoetherianAdicCompletion.idealPowerDerivedLimit_isLeftAdjoint, AdicCompletionTor.derivedCompletion_homology_shortExact, AdicCompletionCohomology.derivedCompletion_homology_iso_adicCompletion, FiniteDerivedComplete.exists_finite_adicCompletionModule_of_isDerivedCompleteModule, AdicCompletionFlatTensor.derivedCompletion_iso_adicCompletion_of_finite_tensor_flat_and_localization, AdicCompletionPseudoCoherentTensor.derivedCompletion_tensor_iso_of_boundedAbove
statement: formalized
proof: formalized
---

# 15.96 Derived completion for Noetherian rings

Section 15.96 of the Stacks Project, [Tag 0BKH](https://stacks.math.columbia.edu/tag/0BKH). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0921, a lemma

[Tag 0921](https://stacks.math.columbia.edu/tag/0921) in the Stacks Project.

**`NoetherianKoszulProIso.koszulPowerSystem_proIso_quotientPowerSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianKoszulProIso.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianKoszulProIso.lean#L750).

> **Stacks Project, Tag 0921.** Over a Noetherian ring, the inverse systems in the derived
> category formed by the Koszul complexes on the positive powers of a finite sequence and by the
> corresponding quotients are isomorphic as pro-objects. Concretely, the comparison is a natural
> transformation, and at every level it admits an inverse after passing to a later level. The first
> of the two displayed identities is precisely the factorization through the quotient asserted in
> the source.

```lean
public theorem koszulPowerSystem_proIso_quotientPowerSystem
    {A : Type u} [CommRing A] [IsNoetherianRing A] {r : ℕ} (f : Fin r → A) :
    ∀ n : ℕ, ∃ (m : ℕ) (h : n ≤ m)
      (s : (quotientPowerSystem f).obj (op m) ⟶
        (koszulPowerSystem f).obj (op n)),
      (koszulQuotientComparison f).app (op m) ≫ s =
          (koszulPowerSystem f).map (homOfLE h).op ∧
        s ≫ (koszulQuotientComparison f).app (op n) =
          (quotientPowerSystem f).map (homOfLE h).op
```

## Tag 0922, a proposition

[Tag 0922](https://stacks.math.columbia.edu/tag/0922) in the Stacks Project.

**`NoetherianAdicCompletion.idealPowerDerivedLimit_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianCompleteIdealPowers.lean, line 1146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianCompleteIdealPowers.lean#L1146).

> **Stacks 0922.** Over a Noetherian ring, derived completion is left adjoint to the
> inclusion of derived-complete objects and is computed by `R lim (K ⊗ᴸ[A] A/Iⁿ)`.
> The adjunction unit induces the canonical reduction map at every level of the tower.
> The projections are natural in `K` and are the actual projections of the derived limit.
>
> The reflector acts on `ModuleCat.{v} A` for an independent module universe `v`. In the
> tensor formula only, the exact functor `U` lifts to modules over `ULift.{v} A`; `J` is the
> same ideal transported along `ULift.ringEquiv`.

```lean
public theorem idealPowerDerivedLimit_isLeftAdjoint
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct (ULift.{v} A)) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun K ↦ IsDerivedComplete I K
    let U := AdicKoszul.derivedUniverseLift.{u, v} A
    let J := I.comap ULift.ringEquiv.toRingHom
    ∃ L : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory,
      ∃ adj : L ⊣ P.ι,
        ∃ π : ∀ n : ℕ, (L ⋙ P.ι) ⋙ U ⟶
            U ⋙ T.tensor.flip.obj ((idealPowerQuotientSystem J).obj ⟨n⟩),
          (∀ K, IsDerivedLimitWithProjections
            (idealPowerQuotientSystem J ⋙ T.tensor.obj (U.obj K))
            (U.obj ((L ⋙ P.ι).obj K)) (fun n ↦ (π n).app K)) ∧
          ∀ K n, U.map (adj.unit.app K) ≫ (π n).app K =
            (derivedReductionMap J T n).app (U.obj K)
```

## Tag 0EET, a lemma

[Tag 0EET](https://stacks.math.columbia.edu/tag/0EET) in the Stacks Project.

**`AdicCompletionTor.derivedCompletion_homology_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionTorSequence.lean, line 1111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/DerivedHomCompletionTorSequence.lean#L1111).

> **Stacks 0EET.** Over a Noetherian ring, derived completion has Milnor short exact
> sequences. For a module these read
> `0 ⟶ R¹ lim Tor_(i+1)(M, A/Iⁿ) ⟶ H^(-i)(M^∧) ⟶ lim Tor_i(M, A/Iⁿ) ⟶ 0`.
> For a derived object, the Tor systems are replaced by the cohomology systems of its derived
> tensors with `A/Iⁿ`. The latter assertion is valid for every derived object, and in particular
> for every object of `D⁻(A)`.

```lean
public theorem derivedCompletion_homology_shortExact
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun K ↦ IsDerivedComplete I K
    ∃ L : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory,
      Nonempty (L ⊣ P.ι) ∧
        (∀ K, IsDerivedLimit
          (NoetherianAdicCompletion.idealPowerQuotientSystem I ⋙ T.tensor.obj K)
          ((L ⋙ P.ι).obj K)) ∧
        (∀ (M : ModuleCat.{u} A) (i : ℕ),
          let M₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M
          let Mhat := (L ⋙ P.ι).obj M₀
          let R1limTor := firstDerivedInverseLimit (torIdealPowerSystem I M (i + 1))
          let HminusI := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(i : ℤ))).obj Mhat
          let limTor := limit (torIdealPowerSystem I M i)
          ∃ (a : R1limTor ⟶ HminusI) (b : HminusI ⟶ limTor) (w : a ≫ b = 0),
            (ShortComplex.mk a b w).ShortExact) ∧
        (∀ (K : DerivedCategory (ModuleCat.{u} A)) (p : ℤ),
          let Khat := (L ⋙ P.ι).obj K
          let H := derivedTensorHomologySystem T I K
          let R1limH := firstDerivedInverseLimit (H (p - 1))
          let Hp := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj Khat
          let limH := limit (H p)
          ∃ (a : R1limH ⟶ Hp) (b : Hp ⟶ limH) (w : a ≫ b = 0),
            (ShortComplex.mk a b w).ShortExact)
```

## Tag 0A06, a lemma

[Tag 0A06](https://stacks.math.columbia.edu/tag/0A06) in the Stacks Project.

**`AdicCompletionCohomology.derivedCompletion_homology_iso_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianCohomologyAdicCompletion.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianCohomologyAdicCompletion.lean#L290).

> If every cohomology module of a complex over a Noetherian ring is finite,
> then the cohomology modules of its derived completion are the adic completions of the original
> cohomology modules.

```lean
public theorem derivedCompletion_homology_iso_adicCompletion
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : ∀ n : ℤ,
      Module.Finite A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj K)) :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{u} A) :=
      moduleCat_hasExactLimitsOfShape_discrete.{u} A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete I L
    ∀ (C : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory),
      (C ⊣ P.ι) → ∀ n : ℤ,
        Nonempty
          (((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj
              ((C ⋙ P.ι).obj K)) ≅
            ModuleCat.of A
              (AdicCompletion I
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj K)))
```

## Tag 09BA, a lemma

[Tag 09BA](https://stacks.math.columbia.edu/tag/09BA) in the Stacks Project.

**`FiniteDerivedComplete.exists_finite_adicCompletionModule_of_isDerivedCompleteModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianExtFiniteComplete.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianExtFiniteComplete.lean#L357).

> **Stacks 09BA.** A derived-complete module over a Noetherian ring whose reduction modulo
> `I` is finite is canonically its `I`-adic completion and is finite over the completed ring.

```lean
public theorem exists_finite_adicCompletionModule_of_isDerivedCompleteModule
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : ModuleCat.{v} A)
    (hM : IsDerivedCompleteModule I M)
    (hfin : Module.Finite (A ⧸ I) (M ⧸ (I • ⊤ : Submodule A M))) :
    ∃ moduleM : Module (AdicCompletion I A) M,
      letI := moduleM
      IsScalarTower A (AdicCompletion I A) M ∧
        Module.Finite (AdicCompletion I A) M ∧
        ∃ e : M ≃ₗ[AdicCompletion I A] AdicCompletion I M,
          ∀ m, e m = AdicCompletion.of I M m
```

## Tag 0EEU, a lemma

[Tag 0EEU](https://stacks.math.columbia.edu/tag/0EEU) in the Stacks Project.

**`AdicCompletionFlatTensor.derivedCompletion_iso_adicCompletion_of_finite_tensor_flat_and_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianCompleteFlatTensor.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianCompleteFlatTensor.lean#L406).

> Let `I` be an ideal of a Noetherian ring `A`. Derived `I`-adic
> completion agrees with ordinary `I`-adic completion for the tensor product of a finite
> module with a flat module, and for the localization of a finite module at one element.

```lean
public theorem derivedCompletion_iso_adicCompletion_of_finite_tensor_flat_and_localization
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun K ↦ IsDerivedComplete I K
    ∀ (L : Functor (DerivedCategory (ModuleCat.{u} A)) P.FullSubcategory),
    Nonempty (L ⊣ P.ι) →
    (∀ K, IsDerivedLimit
      (NoetherianAdicCompletion.idealPowerQuotientSystem I ⋙ T.tensor.obj K)
      ((L ⋙ P.ι).obj K)) →
    let isUsual (Q : Type u) [AddCommGroup Q] [Module A Q] : Prop :=
      Nonempty
        ((L ⋙ P.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A Q)) ≅
          (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A (AdicCompletion I Q)))
    (∀ (M N : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
        [AddCommGroup N] [Module A N] [Module.Flat A N],
      isUsual (TensorProduct A M N)) ∧
    (∀ (M Mf : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
        [AddCommGroup Mf] [Module A Mf] (f : A) (φ : M →ₗ[A] Mf)
        [IsLocalizedModule (Submonoid.powers f) φ],
      isUsual Mf)
```

## Tag 0EEV, a lemma

[Tag 0EEV](https://stacks.math.columbia.edu/tag/0EEV) in the Stacks Project.

**`AdicCompletionPseudoCoherentTensor.derivedCompletion_tensor_iso_of_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianTorPseudoCoherent.lean, line 918](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/NoetherianTorPseudoCoherent.lean#L918).

> **Stacks 0EEV.** Derived completion of a bounded-above complex commutes with derived
> tensor product by a finite module, and more generally by a pseudo-coherent complex.

```lean
public theorem derivedCompletion_tensor_iso_of_boundedAbove
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun K ↦ IsDerivedComplete I K
    ∀ (C : Functor (DerivedCategory (ModuleCat.{u} A)) P.FullSubcategory),
    Nonempty (C ⊣ P.ι) →
    (∀ K, IsDerivedLimit
      (NoetherianAdicCompletion.idealPowerQuotientSystem I ⋙ T.tensor.obj K)
      ((C ⋙ P.ι).obj K)) →
    ∀ (K : DerivedCategory (ModuleCat.{u} A)),
    DerivedCategory.TStructure.t.minus K →
      (∀ (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M],
        Nonempty
          ((C ⋙ P.ι).obj
              ((T.tensor.obj K).obj
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A M))) ≅
            (T.tensor.obj ((C ⋙ P.ι).obj K)).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                (ModuleCat.of A M)))) ∧
      (∀ L : DerivedCategory (ModuleCat.{u} A), StacksDraft.PseudoCoherence.IsPseudoCoherent L →
        Nonempty
          ((C ⋙ P.ι).obj ((T.tensor.obj K).obj L) ≅
            (T.tensor.obj ((C ⋙ P.ι).obj K)).obj L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.96, Tag 0BKH](https://stacks.math.columbia.edu/tag/0BKH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
