---
declaration: section
origin: cited
lean: ProTorsion.proIso_of_torsionBounded, PrincipalNaiveCompletion.derivedCompletionToNaive_isIso_iff_torsionBounded, PrincipalAdicPresentation.isDerivedCompleteModule_iff_exists_shortExact_isAdicComplete, PrincipalScaledVariable.scaledVariableCompletionCokernel_isDerivedComplete_not_isAdicComplete, CompletionSequences.derivedCompletion_principal_homology, PrincipalCompletionDiagram.derivedCompletion_principal_homology_comparison, PrincipalTorsionTower.isMittagLeffler_principalDerivedTensor_iff_powerTorsion, DerivedCompleteTorsion.exists_pow_smul_top_eq_bot_of_isDerivedCompleteModule_of_isIPowerTorsion
statement: formalized
proof: formalized
---

# 15.95 Derived completion for a principal ideal

Section 15.95 of the Stacks Project, [Tag 0BKF](https://stacks.math.columbia.edu/tag/0BKF). 12 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 091X, a lemma

[Tag 091X](https://stacks.math.columbia.edu/tag/091X) in the Stacks Project.

**`ProTorsion.proIso_of_torsionBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/ProIsoBoundedTorsion.lean, line 1069](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/ProIsoBoundedTorsion.lean#L1069).

> **Main statement.**  Let `A` be a commutative ring, `f ∈ A`, and assume the
> `f`-power torsion of `A` is bounded, witnessed by `c ≥ 1` (so `A[f^c] = A[f^m]` for
> all `m ≥ c`).  Then the explicit families of morphisms in `D(A)`
>
>   `alpha n : K_n → A/(f^n)`   (the canonical map onto `H^0`),
>   `beta  c hc hstab n : A/(f^{n+c}) → K_n`   (built from `L_n = (A/A[f^c] →[f^{n+c}] A)`
>                                    and the quasi-isomorphism `L_n ≃ A/(f^{n+c})`, whose
>                                    existence is *derived* from `hstab`),
>
> defined above, induce an isomorphism of pro-objects between `{A/(f^n)}_{n ≥ 1}` and
> `{K_n}_{n ≥ 1}` in `D(A)`.  Since Mathlib lacks a category of pro-objects, this is
> encoded by the two round-trip identities together with the
> compatibility of *both* `α` and `β` with the single-step transition maps:
>
>   * round trip through `{A/(f^•)}`:  `β_n ≫ α_n = (A/(f^{n+c}) → A/(f^n))`;
>   * round trip through `{K_•}`:      `α_{n+c} ≫ β_n = (K_{n+c} → K_n)`;
>   * `α` compatible with transitions: `t_n ≫ α_n = α_{n+1} ≫ π_n`;
>   * `β` compatible with transitions: `π_{(n+1)+c → n+c} ≫ β_n = β_{n+1} ≫ t_n`.
>
> The hypotheses are exactly the boundedness data `c`, `1 ≤ c`, and `hstab`; the
> existence of `β` (i.e. the relevant quasi-isomorphisms) is supplied internally by
> `LqiCx_quasiIso`.

```lean
theorem proIso_of_torsionBounded (c : ℕ)
    (hstab : ∀ m : ℕ, c ≤ m → Submodule.torsionBy A A (f ^ c) = Submodule.torsionBy A A (f ^ m)) :
    -- round trip through the system `{A/(f^•)}`
    (∀ n : ℕ, beta A f c hstab n ≫ alpha A f n = Qtrans A f n c) ∧
    -- round trip through the system `{K_•}`
    (∀ n : ℕ, alpha A f (n + c) ≫ beta A f c hstab n = Ktrans A f n c) ∧
    -- `α` is compatible with the single-step transition maps
    (∀ n : ℕ, KtransOne A f n ≫ alpha A f n = alpha A f (n + 1) ≫ QtransOne A f n) ∧
    -- `β` is compatible with the single-step transition maps
    (∀ n : ℕ,
      QtransOne A f (n + c) ≫ beta A f c hstab n
        = eqToHom (by rw [Nat.add_right_comm]) ≫ beta A f c hstab (n +
            1) ≫ KtransOne A f n)
```

## Tag 0923, a lemma

[Tag 0923](https://stacks.math.columbia.edu/tag/0923) in the Stacks Project.

**`PrincipalNaiveCompletion.derivedCompletionToNaive_isIso_iff_torsionBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/NoetherianCompletePrincipalIdeal.lean, line 4117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/NoetherianCompletePrincipalIdeal.lean#L4117).

> **Stacks 0923.** For `f ∈ A`, the canonical natural transformation from derived completion
> at `(f)` to the naive derived completion formed from the quotients `A/(f^(n+1))` is an
> isomorphism if and only if the `f`-power torsion of `A` is bounded.

```lean
public theorem derivedCompletionToNaive_isIso_iff_torsionBounded
    (A : Type u) [CommRing A] (f : A)
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))] :
    let D := DerivedCategory (ModuleCat.{u} A)
    let generators : Fin 1 → A := fun _ ↦ f
    let P : ObjectProperty D :=
      fun K ↦ IsDerivedComplete (Ideal.span (Set.range generators)) K
    ∃ (completion : D ⥤ P.FullSubcategory) (naiveCompletion : D ⥤ D)
      (comparison : completion ⋙ P.ι ⟶ naiveCompletion),
      Nonempty (completion ⊣ P.ι) ∧
        (∀ K : D,
          let koszulTower := NoetherianKoszulProIso.koszulPowerSystem generators ⋙ T.tensor.obj K
          let quotientTower := NoetherianKoszulProIso.quotientPowerSystem generators ⋙ T.tensor.obj
            K
          ∃ (p : (completion ⋙ P.ι).obj K ⟶
                ∏ᶜ fun n : ℕ ↦ koszulTower.obj (op n))
            (δ : (∏ᶜ fun n : ℕ ↦ koszulTower.obj (op n)) ⟶
                ((completion ⋙ P.ι).obj K)⟦(1 : ℤ)⟧)
            (q : naiveCompletion.obj K ⟶
                ∏ᶜ fun n : ℕ ↦ quotientTower.obj (op n))
            (ε : (∏ᶜ fun n : ℕ ↦ quotientTower.obj (op n)) ⟶
                (naiveCompletion.obj K)⟦(1 : ℤ)⟧),
            Triangle.mk p
                (Pi.lift fun n : ℕ ↦
                  Pi.π (fun n : ℕ ↦ koszulTower.obj (op n)) n -
                    Pi.π (fun n : ℕ ↦ koszulTower.obj (op n)) (n + 1) ≫
                      koszulTower.map (homOfLE (Nat.le_succ n)).op)
                δ ∈ distTriang D ∧
              Triangle.mk q
                (Pi.lift fun n : ℕ ↦
                  Pi.π (fun n : ℕ ↦ quotientTower.obj (op n)) n -
                    Pi.π (fun n : ℕ ↦ quotientTower.obj (op n)) (n + 1) ≫
                      quotientTower.map (homOfLE (Nat.le_succ n)).op)
                ε ∈ distTriang D ∧
              ∀ n : ℕ,
                comparison.app K ≫ q ≫
                    Pi.π (fun n : ℕ ↦ quotientTower.obj (op n)) n =
                  p ≫ Pi.π (fun n : ℕ ↦ koszulTower.obj (op n)) n ≫
                    (T.tensor.obj K).map
                      ((NoetherianKoszulProIso.koszulQuotientComparison generators).app (op n))) ∧
        (IsIso comparison ↔ ProTorsion.TorsionBounded A f)
```

## Tag 09AT, an example

[Tag 09AT](https://stacks.math.columbia.edu/tag/09AT) in the Stacks Project.

**`PrincipalAdicPresentation.isDerivedCompleteModule_iff_exists_shortExact_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalAdicPresentation.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalAdicPresentation.lean#L325).

> **Stacks 09AT.** Let `f` be a nonzerodivisor in a commutative ring `A`. An `A`-module `M` is
> derived complete with respect to `(f)` if and only if it occurs as the cokernel in a short exact
> sequence `0 ⟶ K ⟶ L ⟶ M ⟶ 0`, where `K` and `L` are `f`-adically complete and multiplication by
> `f` is injective on both.

```lean
theorem isDerivedCompleteModule_iff_exists_shortExact_isAdicComplete
    (A : Type u) [CommRing A] (f : A)
    (hf : Function.Injective (LinearMap.lsmul A A f)) (M : ModuleCat.{u} A) :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{u} A) :=
      moduleCat_hasExactLimitsOfShape_discrete.{u} A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    IsDerivedCompleteModule (Ideal.span {f}) M ↔
      ∃ (K L : ModuleCat.{u} A) (i : K ⟶ L) (p : L ⟶ M) (w : i ≫ p = 0),
        (ShortComplex.mk i p w).ShortExact ∧
          IsAdicComplete (Ideal.span {f}) K ∧
          IsAdicComplete (Ideal.span {f}) L ∧
          Function.Injective (LinearMap.lsmul A K f) ∧
          Function.Injective (LinearMap.lsmul A L f)
```

## Tag 0G3F, an example

[Tag 0G3F](https://stacks.math.columbia.edu/tag/0G3F) in the Stacks Project.

**`PrincipalScaledVariable.scaledVariableCompletionCokernel_isDerivedComplete_not_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalScaledVariable.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalScaledVariable.lean#L178).

> **Stacks 0G3F.** Let `p` be prime. The cokernel of the map between the `p`-adic
> completions of `ℤ_[p][X]` induced by `X ↦ pX` is derived complete but not adically complete.
> The image of `1 + pX + p²X² + ⋯` is a nonzero element belonging to every `p^n M`.

```lean
theorem scaledVariableCompletionCokernel_isDerivedComplete_not_isAdicComplete
    (p : ℕ) [Fact p.Prime] :
    let A := ℤ_[p]
    let I : Ideal A := Ideal.span {(p : A)}
    let φ : Polynomial A →ₗ[A] Polynomial A :=
      (Polynomial.aeval ((p : A) • Polynomial.X)).toLinearMap
    let φhat := AdicCompletion.map I φ
    let M := HasQuotient.Quotient (AdicCompletion I (Polynomial A))
      (LinearMap.range (φhat.restrictScalars A))
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat A) :=
      moduleCat_hasExactLimitsOfShape_discrete A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    IsDerivedCompleteModule I (ModuleCat.of A M) ∧
      ¬ IsAdicComplete I M ∧
      ∃ z : AdicCompletion I (Polynomial A),
        (∀ n : ℕ, z.val n =
          Submodule.Quotient.mk
            (∑ i ∈ Finset.range n, (p : A) ^ i • (Polynomial.X : Polynomial A) ^ i)) ∧
        Submodule.Quotient.mk z ≠ (0 : M) ∧
        ∀ n : ℕ, Submodule.Quotient.mk z ∈ I ^ n • (⊤ : Submodule A M)
```

## Tag 0BKG, an example

[Tag 0BKG](https://stacks.math.columbia.edu/tag/0BKG) in the Stacks Project.

**`CompletionSequences.derivedCompletion_principal_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompletionSequences/TruncationSequences.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompletionSequences/TruncationSequences.lean#L456).

> **Stacks 0BKG.** The two principal-completion short exact sequences, with their
> canonical maps. `S` records the fixed mapping-cocone model, its comparison with the
> completion unit, and the normalized truncation maps. The remaining clauses retain all
> cohomology calculations, including both derived-limit realizations and the degree-one
> vanishing for the quotient system.

```lean
public theorem derivedCompletion_principal_homology
    (A : Type u) [CommRing A]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))]
    (f : A) :
    let I : Ideal A := Ideal.span {f}
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun L ↦ IsDerivedComplete I L
    ∀ (completion : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory)
      (adj : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      ∃ S : PrincipalCompletionSequences A f completed adj.unit,
        (∀ M : ModuleCat.{v} A,
          let Mhat := completed.obj ((single A 0).obj M)
          let torsionRlim := moduleDerivedLimit A (powerTorsionSystem A M f)
          let quotientRlim := moduleDerivedLimit A (powerQuotientSystem A M f)
          ∃ (eT : FirstDerivedLimitComparison A (powerTorsionSystem A M f))
            (eQ : FirstDerivedLimitComparison A (powerQuotientSystem A M f)),
            IsDerivedLimit (powerTorsionSystem A M f ⋙ single A 0) torsionRlim ∧
            IsDerivedLimit (powerQuotientSystem A M f ⋙ single A 0) quotientRlim ∧
            Nonempty ((homology A (-1)).obj Mhat ≅ adicTateModule A M f) ∧
            (ShortComplex.mk (eT.iso.hom ≫ (S.moduleSequence M).inclusion)
              (S.moduleSequence M).projection
              (by rw [Category.assoc, (S.moduleSequence M).zero, comp_zero])).ShortExact ∧
            Nonempty ((homology A 1).obj Mhat ≅ (homology A 1).obj quotientRlim) ∧
            IsZero ((homology A 1).obj quotientRlim) ∧
            ∀ n : ℤ, n ≠ -1 → n ≠ 0 → IsZero ((homology A n).obj Mhat)) ∧
        ∀ (K : DerivedCategory (ModuleCat.{v} A)) (p : ℤ),
          (ShortComplex.mk ((S.truncation K p).inclusion S.shift)
            ((S.truncation K p).projection f S.shift
              (S.moduleSequence ((homology A (p + 1)).obj K)).tateIso)
            (S.truncation_zero K p)).ShortExact
```

## Tag 0H32, a lemma

[Tag 0H32](https://stacks.math.columbia.edu/tag/0H32) in the Stacks Project.

**`PrincipalCompletionDiagram.derivedCompletion_principal_homology_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompletionSequencesComparison/ComparisonDiagram.lean, line 760](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/CompletionSequencesComparison/ComparisonDiagram.lean#L760).

> **Stacks 0H32.** For `K ∈ D(A)`, the ordinary completion of `Hᵖ(K)`, the cohomology
> of the derived completion of `Hᵖ(K)`, the cohomology of the derived completion of `K`, and the
> inverse limits of the cohomology of `K ⊗ᴸ_A (A →[f^n] A)` form the canonical commutative
> diagram of four short exact sequences from the source.  Its bottom comparison is an isomorphism
> between the indicated first derived inverse limits.

```lean
public theorem derivedCompletion_principal_homology_comparison
    (A : Type u) [CommRing A]
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A))]
    (f : A) (K : DerivedCategory (ModuleCat.{v} A)) (p : ℤ) :
    let I : Ideal A := Ideal.span {f}
    let P : ObjectProperty (DerivedCategory (ModuleCat.{v} A)) :=
      fun L ↦ IsDerivedComplete I L
    ∀ (completion : DerivedCategory (ModuleCat.{v} A) ⥤ P.FullSubcategory)
      (adj : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      ∃ S : CompletionSequences.PrincipalCompletionSequences A f completed adj.unit,
      let H (q : ℤ) := (homologyFunctor (ModuleCat.{v} A) q).obj K
      let C := DerivedCategory.Q.objPreimage K
      let eK := DerivedCategory.Q.objObjPreimageIso K
      let E := PrincipalTorsionTower.principalComplexSystem A f C
      let tensorSystem := principalDerivedTensorSystem A f K
      let homologySystem (q : ℤ) := tensorSystem ⋙ homologyFunctor (ModuleCat.{v} A) q
      let T := CompletionSequences.milnorTriangle A E
      let completionIso := completed.mapIso eK.symm ≪≫ S.comparison.iso C
      let coneTriangle (n : ℕ) := DerivedCategory.Q.mapTriangle.obj
        (CochainComplex.mappingCone.triangle (f ^ (n + 1) • 𝟙 C))
      let ordinaryCompletion := limit (CompletionSequences.powerQuotientSystem A (H p) f)
      let limitHpTensor := limit (homologySystem p)
      let tate := CompletionSequences.adicTateModule A (H (p + 1)) f
      let H0CompletedHp := (homologyFunctor (ModuleCat.{v} A) 0).obj
        (completed.obj ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj (H p)))
      let HpCompletedK := (homologyFunctor (ModuleCat.{v} A) p).obj (completed.obj K)
      let R1Torsion := CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (H p) f)
      let R1PreviousTensor := CompletionSequences.firstDerivedLimit A (homologySystem (p - 1))
      let middleIn : H0CompletedHp ⟶ HpCompletedK := (S.truncation K p).inclusion S.shift
      let middleOut : HpCompletedK ⟶ tate :=
        (S.truncation K p).projection f S.shift (S.moduleSequence (H (p + 1))).tateIso
      let leftIn : R1Torsion ⟶ H0CompletedHp := (S.moduleSequence (H p)).inclusion
      let leftOut : H0CompletedHp ⟶ ordinaryCompletion := (S.moduleSequence (H p)).projection
      ∃ (termIn : CompletionSequences.powerQuotientSystem A (H p) f ⟶ homologySystem p)
        (termOut : homologySystem p ⟶ PrincipalTorsionTower.powerTorsionSystem A (H (p + 1)) f)
        (previousOut : homologySystem (p - 1) ⟶ PrincipalTorsionTower.powerTorsionSystem A (H p) f)
        (productIso : (homologyFunctor (ModuleCat.{v} A) (p - 1)).obj T.obj₃ ≅
            CompletionSequences.moduleProduct A (homologySystem (p - 1)))
        (topIn : ordinaryCompletion ⟶ limitHpTensor)
        (topOut : limitHpTensor ⟶ tate)
        (htop : topIn ≫ topOut = 0)
        (columnIn : R1PreviousTensor ⟶ HpCompletedK)
        (columnOut : HpCompletedK ⟶ limitHpTensor)
        (hcolumn : columnIn ≫ columnOut = 0)
        (bottom : R1Torsion ≅ R1PreviousTensor),
        (∀ n : ℕ,
          cokernel.π (PrincipalTorsionTower.powerMultiplication A (H p) (f ^ (n + 1))) ≫
              termIn.app ⟨n⟩ =
            (homologyFunctor (ModuleCat.{v} A) p).map (eK.inv ≫ (coneTriangle n).mor₂)) ∧
        (∀ n : ℕ,
          termOut.app ⟨n⟩ ≫
              kernel.ι (PrincipalTorsionTower.powerMultiplication A (H (p + 1)) (f ^ (n + 1))) =
            (homologyFunctor (ModuleCat.{v} A) 0).homologySequenceδ
              (coneTriangle n) p (p + 1) (by omega) ≫
                (homologyFunctor (ModuleCat.{v} A) (p + 1)).map eK.hom) ∧
        (∀ n : ℕ,
          previousOut.app ⟨n⟩ ≫
              kernel.ι (PrincipalTorsionTower.powerMultiplication A (H p) (f ^ (n + 1))) =
            (homologyFunctor (ModuleCat.{v} A) 0).homologySequenceδ
              (coneTriangle n) (p - 1) p (by omega) ≫
                (homologyFunctor (ModuleCat.{v} A) p).map eK.hom) ∧
        (∀ n : ℕ, topIn ≫ limit.π (homologySystem p) ⟨n⟩ =
          limit.π (CompletionSequences.powerQuotientSystem A (H p) f) ⟨n⟩ ≫ termIn.app ⟨n⟩) ∧
        (∀ n : ℕ, topOut ≫ limit.π (PrincipalTorsionTower.powerTorsionSystem A (H (p + 1)) f) ⟨n⟩ =
          limit.π (homologySystem p) ⟨n⟩ ≫ termOut.app ⟨n⟩) ∧
        (∀ n : ℕ, productIso.hom ≫
            Pi.π (fun n : ℕ ↦ (homologySystem (p - 1)).obj ⟨n⟩) n =
          (homologyFunctor (ModuleCat.{v} A) (p - 1)).map
            (DerivedCategory.Q.map (Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n))) ∧
        (productIso.hom ≫ cokernel.π (CompletionSequences.moduleDifference A (homologySystem (p -
          1))) ≫
            columnIn = (homologyFunctor (ModuleCat.{v} A) 0).homologySequenceδ T (p - 1) p
              (by omega) ≫ (homologyFunctor (ModuleCat.{v} A) p).map completionIso.inv) ∧
        (cokernel.π (CompletionSequences.moduleDifference A (homologySystem (p - 1))) ≫ bottom.inv =
          (Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ (homologySystem (p - 1)).obj ⟨n⟩) n ≫
              previousOut.app ⟨n⟩) ≫
            cokernel.π (CompletionSequences.moduleDifference A
              (PrincipalTorsionTower.powerTorsionSystem A (H p) f))) ∧
        (∀ n : ℕ, columnOut ≫ limit.π (homologySystem p) ⟨n⟩ =
          (homologyFunctor (ModuleCat.{v} A) p).map (completionIso.hom ≫ T.mor₁ ≫
            DerivedCategory.Q.map (Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n))) ∧
        (ShortComplex.mk topIn topOut htop).ShortExact ∧
        (ShortComplex.mk middleIn middleOut (S.truncation_zero K p)).ShortExact ∧
        (ShortComplex.mk leftIn leftOut (S.moduleSequence (H p)).zero).ShortExact ∧
        (ShortComplex.mk columnIn columnOut hcolumn).ShortExact ∧
        middleIn ≫ columnOut = leftOut ≫ topIn ∧
        middleOut = columnOut ≫ topOut ∧
        bottom.hom ≫ columnIn = leftIn ≫ middleIn
```

## Tag 0H33, a remark

[Tag 0H33](https://stacks.math.columbia.edu/tag/0H33) in the Stacks Project.

**`PrincipalTorsionTower.isMittagLeffler_principalDerivedTensor_iff_powerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalTorsionTower.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalTorsionTower.lean#L213).

> The cohomology tower of the derived reductions of `K` modulo the positive
> powers of `f` is Mittag--Leffler if and only if the tower of elements of `H^(p + 1)(K)` killed
> by those powers is Mittag--Leffler.

```lean
theorem isMittagLeffler_principalDerivedTensor_iff_powerTorsion
    (A : Type u) [CommRing A] (f : A)
    (K : DerivedCategory (ModuleCat.{v} A)) (p : ℤ) :
    ((principalDerivedTensorSystem A f K ⋙
        homologyFunctor (ModuleCat.{v} A) p) ⋙ forget (ModuleCat.{v} A)).IsMittagLeffler ↔
      ((powerTorsionSystem A ((homologyFunctor (ModuleCat.{v} A) (p + 1)).obj K) f) ⋙
          forget (ModuleCat.{v} A)).IsMittagLeffler
```

## Tag 0CQY, a lemma

[Tag 0CQY](https://stacks.math.columbia.edu/tag/0CQY) in the Stacks Project.

**`DerivedCompleteTorsion.exists_pow_smul_top_eq_bot_of_isDerivedCompleteModule_of_isIPowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/TorsionAnnihilation.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/TorsionAnnihilation.lean#L420).

> If `I` is finitely generated and `M` is both derived complete and `I`-power torsion, then a
> single power of `I` annihilates all of `M`.

```lean
theorem exists_pow_smul_top_eq_bot_of_isDerivedCompleteModule_of_isIPowerTorsion
    (I : Ideal A) (M : ModuleCat.{v} A) (hI : I.FG)
    (hM : IsDerivedCompleteModule I M)
    (htors : IsIPowerTorsion A M I) :
    ∃ n : ℕ, I ^ n • (⊤ : Submodule A M) = ⊥
```

## Tag 0G3G, a lemma

[Tag 0G3G](https://stacks.math.columbia.edu/tag/0G3G) in the Stacks Project.

**`PrincipalCompletionKernel.iInf_principal_powers_annihilates_ker_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalCompletionKernel.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalCompletionKernel.lean#L180).

> **Stacks 0G3G.** Let `J` be the intersection of all powers of the principal ideal `(f)`.
> If `M` is derived complete with respect to `f`, then `J` annihilates the kernel of the canonical
> map from `M` to its `f`-adic completion. In particular, if `A` is derived complete with respect
> to `f`, then `J` is square-zero.

```lean
public theorem iInf_principal_powers_annihilates_ker_adicCompletion
    (A : Type u) [CommRing A] (f : A) (M : Type v) [AddCommGroup M] [Module A M] :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{v} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let I := Ideal.span ({f} : Set A)
    let J := ⨅ n : ℕ, I ^ n
    (IsDerivedCompleteModule I (ModuleCat.of A M) →
      J • (AdicCompletion.of I M).ker = ⊥) ∧
    (IsDerivedCompleteModule I (ModuleCat.of A A) →
        J ^ 2 = ⊥)
```

## Tag 0G3H, a lemma

[Tag 0G3H](https://stacks.math.columbia.edu/tag/0G3H) in the Stacks Project.

**`PrincipalHenselianPair.henselianPair_of_isDerivedCompleteModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalHenselianPair.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalHenselianPair.lean#L149).

> **Stacks 0G3H.** A commutative ring derived complete with respect to an ideal forms a
> henselian pair with that ideal.

```lean
theorem henselianPair_of_isDerivedCompleteModule
    (A : Type u) [CommRing A] (I : Ideal A) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_nat
    IsDerivedCompleteModule I (ModuleCat.of A A) → HenselianPair A I
```

## Tag 0G3I, a lemma

[Tag 0G3I](https://stacks.math.columbia.edu/tag/0G3I) in the Stacks Project.

**`PrincipalCompletionNilpotent.iInf_powers_pow_two_pow_eq_bot_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalCompletionNilpotent.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalCompletionNilpotent.lean#L114).

> **Stacks 0G3I.** If a commutative ring is derived complete with respect to an ideal `I`
> generated by `r` elements, then the `2 ^ r`-th power of the intersection of all powers of `I`
> is zero.

```lean
theorem iInf_powers_pow_two_pow_eq_bot_of_isDerivedComplete
    (A : Type u) [CommRing A] (I : Ideal A) (r : ℕ) (f : Fin r → A)
    (hI : I = Ideal.span (Set.range f)) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_nat
    IsDerivedCompleteModule I (ModuleCat.of A A) →
      (⨅ n : ℕ, I ^ n) ^ (2 ^ r) = ⊥
```

## Tag 0G5V, a lemma

[Tag 0G5V](https://stacks.math.columbia.edu/tag/0G5V) in the Stacks Project.

**`PrincipalCompletionNilpotent.isAdicComplete_of_isReduced_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/PrincipalCompletionNilpotent.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedComplete/PrincipalCompletionNilpotent.lean#L183).

> **Stacks 0G5V.** A reduced commutative ring which is derived complete with respect to a
> finitely generated ideal is adically complete with respect to that ideal.

```lean
theorem isAdicComplete_of_isReduced_of_isDerivedComplete
    (A : Type u) [CommRing A] [IsReduced A] (I : Ideal A) (hI : I.FG) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_nat
    IsDerivedCompleteModule I (ModuleCat.of A A) → IsAdicComplete I A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.95, Tag 0BKF](https://stacks.math.columbia.edu/tag/0BKF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
