---
declaration: section
origin: cited
lean: BeauvilleLaszlo.quotient_pow_equiv_adicCompletion, BeauvilleLaszlo.tensorProduct_prod_away_nontrivial_of_quotientMap_bijective, BeauvilleLaszlo.primeSpectrum_cover_of_quotientMap_bijective, BeauvilleLaszlo.finite_iff_tensorProduct_prod_away_of_quotientMap_bijective, BeauvilleLaszlo.exists_nonflat_adicCompletion_prod_localizationAway, BeauvilleLaszlo.beauvilleLaszloSequence, BeauvilleLaszlo.adicCompletionBeauvilleLaszloSequence, BeauvilleLaszlo.beauvilleLaszloSequence_exactness_iff_powerTorsionMap
statement: formalized
proof: formalized
---

# 15.92 The Beauville-Laszlo theorem

Section 15.92 of the Stacks Project, [Tag 0BNI](https://stacks.math.columbia.edu/tag/0BNI). 27 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BNJ, a lemma

[Tag 0BNJ](https://stacks.math.columbia.edu/tag/0BNJ) in the Stacks Project.

**`BeauvilleLaszlo.quotient_pow_equiv_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean#L84).

> The canonical map `R / f^n R → R^∧ / f^n R^∧` is an isomorphism,
> where `R^∧` is the `(f)`-adic completion.

```lean
public theorem quotient_pow_equiv_adicCompletion {R : Type*} [CommRing R]
    (f : R) (n : ℕ) :
    ∃ e : (R ⧸ (Ideal.span {f}) ^ n) ≃+*
        (AdicCompletion (Ideal.span {f}) R ⧸
          (Ideal.span {(algebraMap R (AdicCompletion (Ideal.span {f}) R)) f}) ^ n),
      ∀ r : R,
        e (Ideal.Quotient.mk _ r) =
          Ideal.Quotient.mk _ ((algebraMap R (AdicCompletion (Ideal.span {f}) R)) r)
```

## Tag 0BNL, a lemma

[Tag 0BNL](https://stacks.math.columbia.edu/tag/0BNL) in the Stacks Project.

**`BeauvilleLaszlo.tensorProduct_prod_away_nontrivial_of_quotientMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean#L177).

> If `R → S` induces isomorphisms modulo every positive power of `(f)`, then tensoring
> with `S ⊕ R_f` detects nonzero modules. In particular, tensoring with `R^∧ ⊕ R_f`, where
> `R^∧` is the `(f)`-adic completion, detects nonzero modules.

```lean
public theorem tensorProduct_prod_away_nontrivial_of_quotientMap_bijective
    (R : Type u) [CommRing R] (f : R) :
    (∀ (S : Type v) [CommRing S] [Algebra R S],
      (∀ n : ℕ, 0 < n →
        Function.Bijective
          (Ideal.quotientMap
            (Ideal.map (algebraMap R S) ((Ideal.span {f}) ^ n))
            (algebraMap R S) Ideal.le_comap_map)) →
      ∀ (M : Type w) [AddCommGroup M] [Module R M] [Nontrivial M],
        Nontrivial (TensorProduct R M (S × Localization.Away f))) ∧
    (∀ (M : Type w) [AddCommGroup M] [Module R M] [Nontrivial M],
      Nontrivial
        (TensorProduct R M
          (AdicCompletion (Ideal.span {f}) R × Localization.Away f)))
```

## Tag 0BNM, a lemma

[Tag 0BNM](https://stacks.math.columbia.edu/tag/0BNM) in the Stacks Project.

**`BeauvilleLaszlo.primeSpectrum_cover_of_quotientMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean#L273).

> If `R → S` is an isomorphism modulo `f`, then `Spec(S)` and `Spec(R_f)`
> jointly cover `Spec(R)`. The same cover holds with the `(f)`-adic completion in
> place of `S`.

```lean
public theorem primeSpectrum_cover_of_quotientMap_bijective {R : Type*} [CommRing R] (f : R) :
    (∀ {S : Type*} [CommRing S] (φ : R →+* S),
      Function.Bijective
          (Ideal.quotientMap (Ideal.map φ (Ideal.span {f})) φ Ideal.le_comap_map) →
        Function.Surjective
          (Sum.elim (PrimeSpectrum.comap φ)
            (PrimeSpectrum.comap (algebraMap R (Localization.Away f))))) ∧
      Function.Surjective
        (Sum.elim
          (PrimeSpectrum.comap
            (algebraMap R (AdicCompletion (Ideal.span {f}) R)))
          (PrimeSpectrum.comap (algebraMap R (Localization.Away f))))
```

## Tag 0BNN, a lemma

[Tag 0BNN](https://stacks.math.columbia.edu/tag/0BNN) in the Stacks Project.

**`BeauvilleLaszlo.finite_iff_tensorProduct_prod_away_of_quotientMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Covering.lean#L337).

> Finite generation of a module is detected after extension of scalars to the product of
> an algebra inducing isomorphisms modulo every positive power of `(f)` and the localization
> away from `f`. In particular, it is detected by the product of the `(f)`-adic completion and
> that localization.

```lean
public theorem finite_iff_tensorProduct_prod_away_of_quotientMap_bijective
    (R : Type u) [CommRing R] (f : R) :
    (∀ (S : Type v) [CommRing S] [Algebra R S],
      (∀ n : ℕ, 0 < n →
        Function.Bijective
          (Ideal.quotientMap
            (Ideal.map (algebraMap R S) ((Ideal.span {f}) ^ n))
            (algebraMap R S) Ideal.le_comap_map)) →
      ∀ (M : Type w) [AddCommGroup M] [Module R M],
        Module.Finite R M ↔
          Module.Finite (S × Localization.Away f)
            (TensorProduct R (S × Localization.Away f) M)) ∧
    (∀ (M : Type w) [AddCommGroup M] [Module R M],
      Module.Finite
          (AdicCompletion (Ideal.span {f}) R × Localization.Away f)
          (TensorProduct R
            (AdicCompletion (Ideal.span {f}) R × Localization.Away f) M) →
        Module.Finite R M)
```

## Tag 0BNP, a remark

[Tag 0BNP](https://stacks.math.columbia.edu/tag/0BNP) in the Stacks Project.

**`BeauvilleLaszlo.exists_nonflat_adicCompletion_prod_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 1363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L1363).

> **Stacks 0BNP.** Adic completion and localization do not in general form a flat cover: there
> is a commutative ring `R` and an element `f` such that the product of the completion of `R` at
> `(f)` and `R_f` is not flat over `R`.

```lean
public theorem exists_nonflat_adicCompletion_prod_localizationAway :
    ∃ (R : Type) (_ : CommRing R) (f : R),
      ¬ Module.Flat R
        (AdicCompletion (Ideal.span ({f} : Set R)) R × Localization.Away f)
```

## Tag 0F1Q, an equation

[Tag 0F1Q](https://stacks.math.columbia.edu/tag/0F1Q) in the Stacks Project.

**`BeauvilleLaszlo.beauvilleLaszloSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L142).

> The canonical sequence
> `0 → R → S ⊕ Rₑ → Sₓ → 0`, whose right-hand map is the difference of the
> two canonical localization maps.

```lean
public noncomputable def beauvilleLaszloSequence (f : R) (φ : R →+* S) :
    ShortComplex AddCommGrpCat.{max u v}
```

## Tag 0BNQ, an equation

[Tag 0BNQ](https://stacks.math.columbia.edu/tag/0BNQ) in the Stacks Project.

**`BeauvilleLaszlo.adicCompletionBeauvilleLaszloSequence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L173).

> The canonical sequence `0 → R → R̂ ⊕ Rₑ → R̂ₑ → 0`, where `R̂` is the
> completion of `R` along the principal ideal generated by `f`.

```lean
public noncomputable abbrev adicCompletionBeauvilleLaszloSequence
    (R : Type u) [CommRing R] (f : R) : ShortComplex AddCommGrpCat.{u}
```

## Tag 0BNR, a lemma

[Tag 0BNR](https://stacks.math.columbia.edu/tag/0BNR) in the Stacks Project.

**`BeauvilleLaszlo.beauvilleLaszloSequence_exactness_iff_powerTorsionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L433).

> If `R → S` is an isomorphism modulo every positive power of `f`, the
> Beauville--Laszlo sequence is always exact on the right; its left and middle
> exactness are equivalent to injectivity and surjectivity on `f`-power torsion.
> Consequently it is short exact precisely when that map is bijective. The same
> criterion specializes to the `(f)`-adic completion of `R`.

```lean
public theorem beauvilleLaszloSequence_exactness_iff_powerTorsionMap
    (f : R) (φ : R →+* S)
    (hφ : ∀ n : ℕ, 0 < n → Function.Bijective (quotientPowMap f n φ)) :
    Epi (beauvilleLaszloSequence f φ).g ∧
      (Mono (beauvilleLaszloSequence f φ).f ↔
        Function.Injective (powerTorsionMap f φ)) ∧
      ((beauvilleLaszloSequence f φ).Exact ↔
        Function.Surjective (powerTorsionMap f φ)) ∧
      ((beauvilleLaszloSequence f φ).ShortExact ↔
        Function.Bijective (powerTorsionMap f φ)) ∧
      ((beauvilleLaszloSequence f
          (algebraMap R (AdicCompletion (Ideal.span {f}) R))).ShortExact ↔
        Function.Bijective (powerTorsionMap f
          (algebraMap R (AdicCompletion (Ideal.span {f}) R))))
```

## Tag 0BNS, a remark

[Tag 0BNS](https://stacks.math.columbia.edu/tag/0BNS) in the Stacks Project.

**`BeauvilleLaszlo.adicCompletion_isRegular_and_isGlueingPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L520).

> A nonzerodivisor `f` remains a nonzerodivisor in the `(f)`-adic completion, and the
> canonical Beauville--Laszlo sequence is short exact; equivalently, `(R, f)` is a glueing pair.

```lean
public theorem adicCompletion_isRegular_and_isGlueingPair {R : Type*} [CommRing R] (f : R) (hf :
  IsRegular f) :
    IsRegular (algebraMap R (AdicCompletion (Ideal.span {f}) R) f) ∧
      (beauvilleLaszloSequence f
        (algebraMap R (AdicCompletion (Ideal.span {f}) R))).ShortExact
```

## Tag 0BNT, a remark

[Tag 0BNT](https://stacks.math.columbia.edu/tag/0BNT) in the Stacks Project.

**`BeauvilleLaszlo.adicCompletion_isGlueingPair_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L558).

> If the `(f)`-adic completion of `R` is flat over `R`, then tensoring the exact sequence
> given by multiplication by `f ^ n` remains exact for every positive `n`, the canonical map on
> `f ^ n`-torsion is an isomorphism, and `(R, f)` is a glueing pair. These conclusions hold in
> particular when `R` is Noetherian.

```lean
public theorem adicCompletion_isGlueingPair_of_flat {R : Type u} [CommRing R] (f : R) :
    let P : Prop :=
      (∀ n : ℕ, 0 < n →
        let T := Submodule.torsionBy R R (f ^ n)
        let a : T ⊗[R] AdicCompletion (Ideal.span {f}) R →ₗ[R]
            AdicCompletion (Ideal.span {f}) R :=
          (TensorProduct.lid R (AdicCompletion (Ideal.span {f}) R)).toLinearMap.comp
            (TensorProduct.map T.subtype
              (LinearMap.id (R := R) (M := AdicCompletion (Ideal.span {f}) R)))
        let b : AdicCompletion (Ideal.span {f}) R →ₗ[R]
            AdicCompletion (Ideal.span {f}) R :=
          (LinearMap.lsmul R (AdicCompletion (Ideal.span {f}) R)) (f ^ n)
        Function.Injective a ∧ Function.Exact a b ∧
          Function.Injective
            (fun x : T => algebraMap R (AdicCompletion (Ideal.span {f}) R) x.1) ∧
          Set.range (fun x : T => algebraMap R (AdicCompletion (Ideal.span {f}) R) x.1) =
            (Submodule.torsionBy (AdicCompletion (Ideal.span {f}) R)
              (AdicCompletion (Ideal.span {f}) R)
              ((algebraMap R (AdicCompletion (Ideal.span {f}) R) f) ^ n) :
                Set (AdicCompletion (Ideal.span {f}) R))) ∧
      Function.Injective (fun r : R =>
        (algebraMap R (AdicCompletion (Ideal.span {f}) R) r,
          algebraMap R (Localization.Away f) r)) ∧
      Function.Exact
        (fun r : R => (algebraMap R (AdicCompletion (Ideal.span {f}) R) r,
          algebraMap R (Localization.Away f) r))
        (fun x : AdicCompletion (Ideal.span {f}) R × Localization.Away f =>
          algebraMap (AdicCompletion (Ideal.span {f}) R)
              (Localization.Away
                (algebraMap R (AdicCompletion (Ideal.span {f}) R) f)) x.1 -
            Localization.awayMap
              (algebraMap R (AdicCompletion (Ideal.span {f}) R)) f x.2) ∧
      Function.Surjective
        (fun x : AdicCompletion (Ideal.span {f}) R × Localization.Away f =>
          algebraMap (AdicCompletion (Ideal.span {f}) R)
              (Localization.Away
                (algebraMap R (AdicCompletion (Ideal.span {f}) R) f)) x.1 -
            Localization.awayMap
              (algebraMap R (AdicCompletion (Ideal.span {f}) R)) f x.2)
    (Module.Flat R (AdicCompletion (Ideal.span {f}) R) → P) ∧
      (∀ [IsNoetherianRing R], P)
```

## Tag 0BNU, an example

[Tag 0BNU](https://stacks.math.columbia.edu/tag/0BNU) in the Stacks Project.

**`BeauvilleLaszlo.adicCompletion_torsionMap_not_bijective_examples`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean, line 1287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingPair.lean#L1287).

> Two quotients of `k[f, T₁, T₂, …]` for which the canonical map on `f`-power torsion
> to the adic completion is respectively noninjective and nonsurjective. In the first example
> `T₁` is a nonzero kernel element whose image is divisible by every power of `f`. In the second,
> the compatible residues of `T₁ + f T₂ + f² T₃ + ⋯` define an `f`-torsion element outside
> the image. The two completion maps are not flat.

```lean
public theorem adicCompletion_torsionMap_not_bijective_examples (k : Type*) [Field k] :
    let P := MvPolynomial (Option ℕ) k
    let F : P := MvPolynomial.X none
    let T : ℕ → P := fun n ↦ MvPolynomial.X (some n)
    let I₁ : Ideal P := Ideal.span ({F * T 0} ∪ Set.range (fun n ↦ F * T (n + 1) - T n))
    let R₁ := P ⧸ I₁
    let f₁ : R₁ := Ideal.Quotient.mk I₁ F
    let t₁ : ℕ → R₁ := fun n ↦ Ideal.Quotient.mk I₁ (T n)
    let J₁ : Ideal R₁ := Ideal.span {f₁}
    let c₁ := AdicCompletion.of J₁ R₁
    let I₂ : Ideal P := Ideal.span (Set.range (fun n ↦ F ^ (n + 1) * T n))
    let R₂ := P ⧸ I₂
    let f₂ : R₂ := Ideal.Quotient.mk I₂ F
    let t₂ : ℕ → R₂ := fun n ↦ Ideal.Quotient.mk I₂ (T n)
    let J₂ : Ideal R₂ := Ideal.span {f₂}
    let c₂ := AdicCompletion.of J₂ R₂
    t₁ 0 ≠ 0 ∧ t₁ 0 ∈ Ideal.primaryComponent R₁ J₁ ∧ c₁ (t₁ 0) = 0 ∧
    (∀ n : ℕ, f₁ ^ n • c₁ (t₁ n) = c₁ (t₁ 0)) ∧
    (¬ Function.Injective (Ideal.primaryComponent.map J₁ c₁)) ∧
    (¬ Module.Flat R₁ (AdicCompletion J₁ R₁)) ∧
    (¬ Function.Surjective (Ideal.primaryComponent.map J₂ c₂)) ∧
    (∃ x : Ideal.primaryComponent (AdicCompletion J₂ R₂) J₂,
      (∀ n : ℕ, AdicCompletion.evalₐ J₂ n x.1 =
        Ideal.Quotient.mk (J₂ ^ n) (∑ i ∈ Finset.range n, f₂ ^ i * t₂ i)) ∧
      f₂ • x.1 = 0 ∧
      x ∉ Set.range (Ideal.primaryComponent.map J₂ c₂)) ∧
    (¬ Module.Flat R₂ (AdicCompletion J₂ R₂))
```

## Tag 0F1R, an equation

[Tag 0F1R](https://stacks.math.columbia.edu/tag/0F1R) in the Stacks Project.

**`BeauvilleLaszlo.beauvilleLaszloModuleSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean#L148).

> The canonical sequence
> `0 → M → (M ⊗[R] S) ⊕ (M ⊗[R] R_f) → M ⊗[R] S_f → 0`.
> The right-hand map is the difference of the two maps induced by localization.

```lean
public noncomputable def beauvilleLaszloModuleSequence (f : R) :
    ShortComplex AddCommGrpCat.{max u v w}
```

## Tag 0BNV, an equation

[Tag 0BNV](https://stacks.math.columbia.edu/tag/0BNV) in the Stacks Project.

**`BeauvilleLaszlo.isGlueable_iff_adicCompletion_beauvilleLaszloModuleSequence_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean#L217).

> An `R`-module is glueable at `f` exactly when
> `0 → M → (M ⊗[R] R̂) ⊕ (M ⊗[R] R_f) → M ⊗[R] R̂_f → 0`
> is short exact, where `R̂` is the `(f)`-adic completion.

```lean
public theorem isGlueable_iff_adicCompletion_beauvilleLaszloModuleSequence_shortExact {R : Type u}
  [CommRing R] (M : Type w) [AddCommGroup M] [Module R M]
    (f : R) :
    IsGlueable M f ↔
      (beauvilleLaszloModuleSequence
        (S := AdicCompletion (Ideal.span {f}) R) M f).ShortExact
```

## Tag 0BNW, a lemma

[Tag 0BNW](https://stacks.math.columbia.edu/tag/0BNW) in the Stacks Project.

**`BeauvilleLaszlo.beauvilleLaszloModuleSequence_exactness_iff_powerTorsionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean, line 714](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/ModuleSequence.lean#L714).

> If `R → S` is an isomorphism modulo every positive power of `f`, the module
> Beauville--Laszlo sequence is surjective on the right; its left and middle exactness
> are equivalent to injectivity and surjectivity of the canonical map on `f`-power torsion.
> Thus the module is glueable exactly when this map is bijective. If the ring sequence is
> short exact, surjectivity on power torsion is automatic, so injectivity alone characterizes
> glueability. The latter criterion also applies to the `(f)`-adic completion.

```lean
public theorem beauvilleLaszloModuleSequence_exactness_iff_powerTorsionMap :
    (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
      (M : Type w) [AddCommGroup M] [Module R M] (f : R),
      (∀ n : ℕ, 0 < n → Function.Bijective
        (quotientPowMap f n (algebraMap R S))) →
      Epi (beauvilleLaszloModuleSequence (S := S) M f).g ∧
        (Mono (beauvilleLaszloModuleSequence (S := S) M f).f ↔
          Function.Injective (tensorProductPowerTorsionMap (S := S) M f)) ∧
        ((beauvilleLaszloModuleSequence (S := S) M f).Exact ↔
          Function.Surjective (tensorProductPowerTorsionMap (S := S) M f)) ∧
        ((beauvilleLaszloModuleSequence (S := S) M f).ShortExact ↔
          Function.Bijective (tensorProductPowerTorsionMap (S := S) M f)) ∧
        ((beauvilleLaszloSequence f (algebraMap R S)).ShortExact →
          ((beauvilleLaszloModuleSequence (S := S) M f).ShortExact ↔
            Function.Injective (tensorProductPowerTorsionMap (S := S) M f)))) ∧
    (∀ (R : Type u) [CommRing R] (M : Type w) [AddCommGroup M] [Module R M] (f : R),
      (beauvilleLaszloSequence f
          (algebraMap R (AdicCompletion (Ideal.span {f}) R))).ShortExact →
        ((beauvilleLaszloModuleSequence
            (S := AdicCompletion (Ideal.span {f}) R) M f).ShortExact ↔
          Function.Injective
            (tensorProductPowerTorsionMap
              (S := AdicCompletion (Ideal.span {f}) R) M f)))
```

## Tag 0BNX, a remark

[Tag 0BNX](https://stacks.math.columbia.edu/tag/0BNX) in the Stacks Project.

**`BeauvilleLaszlo.glueable_criteria`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/Criteria.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/Criteria.lean#L640).

> Criteria ensuring that a module is glueable for a Beauville--Laszlo glueing pair.
>
> For completion at `f`, glueability is equivalent to injectivity on `f`-power torsion.
> Injectivity of `M[f] → M̂` is equivalent to
> `M[f] ∩ ⋂ n ≥ 1, f ^ n M = 0` and implies glueability. For a general glueing pair
> `R → S`, vanishing of `Tor₁(M, S_f)` is sufficient and is equivalent to
> `Tor₁(M, S)` being `f`-power torsion. Consequently flat modules are glueable; if
> `S` is flat over `R`, every module is glueable. The latter applies to completion over
> a Noetherian ring.

```lean
public theorem glueable_criteria :
    (∀ (R : Type u) [CommRing R] (M : Type w) [AddCommGroup M] [Module R M]
      (f : R),
      (beauvilleLaszloSequence f
        (algebraMap R (AdicCompletion (Ideal.span {f}) R))).ShortExact →
        ((IsGlueable M f ↔
            Function.Injective
              (tensorProductPowerTorsionMap
                (S := AdicCompletion (Ideal.span {f}) R) M f)) ∧
          (Function.Injective
              (fun x : Submodule.torsionBy R M f ↦
                AdicCompletion.of (Ideal.span {f}) M x.1) ↔
            Submodule.torsionBy R M f ⊓
                (⨅ n : ℕ, (Ideal.span {f}) ^ (n + 1) • ⊤) = ⊥) ∧
          (Function.Injective
              (fun x : Submodule.torsionBy R M f ↦
                AdicCompletion.of (Ideal.span {f}) M x.1) →
            IsGlueable M f))) ∧
    (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
      (M : Type w) [AddCommGroup M] [Module R M] (f : R),
      (beauvilleLaszloSequence f (algebraMap R S)).ShortExact →
        ((IsZero
            (((Tor' (ModuleCat.{max u v w} (ULift.{max v w} R)) 1).obj
              (ModuleCat.of (ULift.{max v w} R) (ULift.{max u v} M))).obj
                (ModuleCat.of (ULift.{max v w} R)
                  (ULift.{max u w} (Localization.Away (algebraMap R S f))))) →
            IsGlueableFor (S := S) M f) ∧
          (IsZero
              (((Tor' (ModuleCat.{max u v w} (ULift.{max v w} R)) 1).obj
                (ModuleCat.of (ULift.{max v w} R) (ULift.{max u v} M))).obj
                  (ModuleCat.of (ULift.{max v w} R)
                    (ULift.{max u w} (Localization.Away (algebraMap R S f))))) ↔
            modulePowerTorsion
                (((Tor' (ModuleCat.{max u v w} (ULift.{max v w} R)) 1).obj
                  (ModuleCat.of (ULift.{max v w} R) (ULift.{max u v} M))).obj
                    (ModuleCat.of (ULift.{max v w} R) (ULift.{max u w} S)))
                (ULift.up f) = ⊤) ∧
          (Module.Flat R M → IsGlueableFor (S := S) M f) ∧
          (Module.Flat R S → IsGlueableFor (S := S) M f))) ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R]
      (M : Type w) [AddCommGroup M] [Module R M] (f : R),
      IsGlueable M f)
```

## Tag 0BNY, an example

[Tag 0BNY](https://stacks.math.columbia.edu/tag/0BNY) in the Stacks Project.

**`BeauvilleLaszlo.exists_non_glueable_module_over_smooth_germ_ring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/NonGlueableExample.lean, line 718](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueableModule/NonGlueableExample.lean#L718).

> The ring `R` of germs at zero of smooth functions on `ℝ`, with coordinate germ `f`, has
> completion `ℝ[[X]]`. The flat germs `φ(x) = exp (-1 / x²)` and `ψ(x) = φ(x) / x` vanish
> in the completion, while the class of `ψ` in `M = R / φR` is nonzero `f`-torsion. It therefore
> lies in the kernel of the completion base-change map, so `M` is not glueable.

```lean
public theorem exists_non_glueable_module_over_smooth_germ_ring :
    let S := smoothSheafCommRing (modelWithCornersSelf ℝ ℝ)
      (modelWithCornersSelf ℝ ℝ) ℝ ℝ
    let R := S.presheaf.stalk (0 : ℝ)
    ∃ (f₀ φ₀ ψ₀ : S.presheaf.obj (op ⊤)),
      (∀ x : ℝ, f₀ ⟨x, Set.mem_univ x⟩ = x) ∧
      (∀ x : ℝ, φ₀ ⟨x, Set.mem_univ x⟩ =
        if x = 0 then 0 else Real.exp (-1 / x ^ 2)) ∧
      (∀ x : ℝ, ψ₀ ⟨x, Set.mem_univ x⟩ =
        if x = 0 then 0 else Real.exp (-1 / x ^ 2) / x) ∧
      let f : R := S.presheaf.germ ⊤ 0 (Set.mem_univ 0) f₀
      let φ : R := S.presheaf.germ ⊤ 0 (Set.mem_univ 0) φ₀
      let ψ : R := S.presheaf.germ ⊤ 0 (Set.mem_univ 0) ψ₀
      IsRegular f ∧ IsRegular φ ∧ f * ψ = φ ∧
      ∃ e : AdicCompletion (Ideal.span {f}) R ≃+* PowerSeries ℝ,
        e (algebraMap R (AdicCompletion (Ideal.span {f}) R) f) = PowerSeries.X ∧
        algebraMap R (AdicCompletion (Ideal.span {f}) R) φ = 0 ∧
        algebraMap R (AdicCompletion (Ideal.span {f}) R) ψ = 0 ∧
        (let M := R ⧸ Ideal.span {φ}
         let m : M := Ideal.Quotient.mk (Ideal.span {φ}) ψ
         let C := AdicCompletion (Ideal.span {f}) R
         m ≠ 0 ∧ f • m = 0 ∧
          TensorProduct.mk R M C m 1 = 0 ∧
          (∃ q : TensorProduct R M C ≃ₗ[R] C,
            ∀ (r : R) (c : C),
              q (TensorProduct.mk R M C (Ideal.Quotient.mk (Ideal.span {φ}) r) c) =
                algebraMap R C r * c) ∧
          ¬ Function.Injective
            (fun x : {x : M // ∃ n : ℕ, f ^ n • x = 0} ↦
              TensorProduct.mk R M C x.1 1))
```

## Tag 0BNZ, a lemma

[Tag 0BNZ](https://stacks.math.columbia.edu/tag/0BNZ) in the Stacks Project.

**`BeauvilleLaszlo.isZero_Tor_one_ideal_pow_of_beauvilleLaszlo_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean#L179).

> If `(R → R', f)` is a gluing pair, then
> `Tor₁ʿ(R', f ^ n R) = 0` for every positive `n`.

```lean
public theorem isZero_Tor_one_ideal_pow_of_beauvilleLaszlo_shortExact
    {R S : Type u} [CommRing R] [CommRing S] (f : R) (φ : R →+* S)
    (hφ : ∀ n : ℕ, 0 < n →
      Function.Bijective (quotientPowMap f n φ))
    (hglue : (beauvilleLaszloSequence f φ).ShortExact) :
    ∀ n : ℕ, 0 < n →
      Limits.IsZero (((Tor (ModuleCat.{u} R) 1).obj
        ((ModuleCat.restrictScalars φ).obj (ModuleCat.of S S))).obj
        (ModuleCat.of R ↑((Ideal.span {f}) ^ n)))
```

## Tag 0BP0, a lemma

[Tag 0BP0](https://stacks.math.columbia.edu/tag/0BP0) in the Stacks Project.

**`BeauvilleLaszlo.isZero_Tor_one_quotient_powerTorsion_of_beauvilleLaszlo_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean#L448).

> If `(R → R', f)` is a glueing pair, then
> `Tor₁ᴿ(R', R / R[f^∞]) = 0`.

```lean
public theorem isZero_Tor_one_quotient_powerTorsion_of_beauvilleLaszlo_shortExact
    {R S : Type u} [CommRing R] [CommRing S] (f : R) (φ : R →+* S)
    (hφ : ∀ n : ℕ, 0 < n → Function.Bijective (quotientPowMap f n φ))
    (hglue : (beauvilleLaszloSequence f φ).ShortExact) :
    Limits.IsZero (((Tor (ModuleCat.{u} R) 1).obj
      ((ModuleCat.restrictScalars φ).obj (ModuleCat.of S S))).obj
      (ModuleCat.of R (R ⧸ powerTorsion f)))
```

## Tag 0BP1, a lemma

[Tag 0BP1](https://stacks.math.columbia.edu/tag/0BP1) in the Stacks Project.

**`BeauvilleLaszlo.isZero_Tor_one_coker_localizationMap_of_beauvilleLaszlo_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean, line 636](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/TorVanishing.lean#L636).

> If `(R → R', f)` is a Beauville--Laszlo glueing pair, then for every `R`-module `M`,
> `Tor₁ᴿ(R', coker(M → M_f)) = 0`.

```lean
public theorem isZero_Tor_one_coker_localizationMap_of_beauvilleLaszlo_shortExact
    {R : Type u} {S : Type v} {M : Type w}
    [CommRing R] [CommRing S] [AddCommGroup M] [Module R M]
    (f : R) (φ : R →+* S)
    (hφ : ∀ n : ℕ, 0 < n → Function.Bijective (quotientPowMap f n φ))
    (hglue : (beauvilleLaszloSequence f φ).ShortExact) :
    Limits.IsZero (((Tor (ModuleCat.{max u v w}
      (ULift.{max u v w} R)) 1).obj
      ((ModuleCat.restrictScalars (φ.ulift.{max u v w, max u v w})).obj
        (ModuleCat.of (ULift.{max u v w} S) (ULift.{max u v w} S)))).obj
      (ModuleCat.of (ULift.{max u v w} R)
        (ULift.{max u v w}
          (LocalizedModule (Submonoid.powers f) M ⧸
            LinearMap.range (LocalizedModule.mkLinearMap (Submonoid.powers f) M)))))
```

## Tag 0BP2, a theorem

[Tag 0BP2](https://stacks.math.columbia.edu/tag/0BP2) in the Stacks Project.

**`BeauvilleLaszlo.canonicalOnGlueableModules_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/ModuleEquivalence.lean, line 852](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/ModuleEquivalence.lean#L852).

> **Beauville--Laszlo glueing.** For a glueing pair `(R → S, f)`, the canonical functor
> from glueable `R`-modules to module glueing data is an equivalence of categories. Compatible
> sections of every glueing datum are glueable, and the canonical map from any module to the
> sections of its canonical datum induces isomorphisms after extension of scalars to `S` and
> localization away from `f`.

```lean
public theorem canonicalOnGlueableModules_isEquivalence
    (hquot : ∀ n : ℕ, 0 < n →
      Function.Bijective (quotientPowMap f n (algebraMap R S)))
    (hglue : (beauvilleLaszloSequence f (algebraMap R S)).ShortExact) :
    let C := moduleGlueingConstruction.{u, v, w} S (fun _ : Fin 1 ↦ f)
    letI := C.category
    (canonicalOnGlueableModules f C).IsEquivalence ∧
      (∀ X : ModuleGlueingDatum.{u, v, w} S (fun _ : Fin 1 ↦ f) C.comparison,
        glueableModules (S := S) f (C.sections.obj X)) ∧
      (∀ M : ModuleCat.{max u v w} R,
        Function.Bijective
            (TensorProduct.map (LinearMap.id (R := R) (M := S))
              (C.canonicalSectionsUnit.app M).hom) ∧
          Function.Bijective
            (LocalizedModule.map (Submonoid.powers f)
              (C.canonicalSectionsUnit.app M).hom))
```

## Tag 0BP3, an equation

[Tag 0BP3](https://stacks.math.columbia.edu/tag/0BP3) in the Stacks Project.

**`BeauvilleLaszlo.gluingDatum_difference_shortExact_of_quotientMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean#L105).

> The kernel of the difference map attached to a gluing datum fits into the short exact
> sequence `0 → ker(d) → M' × M₁ → M'ₑ → 0`.
>
> Here the difference map sends `(x, y)` to `x / 1 - α⁻¹(1 ⊗ y)`. It is surjective as
> soon as `R → S` is surjective modulo every positive power of `f`; in particular the result
> applies to a Beauville--Laszlo gluing pair.

```lean
public theorem gluingDatum_difference_shortExact_of_quotientMap_surjective
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    (f : R)
    (hmod : ∀ n : ℕ, 0 < n →
      Function.Surjective
        (Ideal.quotientMap
          (Ideal.map (algebraMap R S) ((Ideal.span {f}) ^ n))
          (algebraMap R S) Ideal.le_comap_map))
    (M' : Type w) [AddCommGroup M'] [Module R M'] [Module S M']
    [IsScalarTower R S M']
    (M₁ : Type x) [AddCommGroup M₁] [Module R M₁]
    [Module (Localization.Away f) M₁] [IsScalarTower R (Localization.Away f) M₁]
    (α : LocalizedModule.Away (algebraMap R S f) M' ≃ₗ[S]
      TensorProduct R S M₁) :
    let localizationMap : M' →ₗ[R] LocalizedModule.Away (algebraMap R S f) M' :=
      (LocalizedModule.mkLinearMap (Submonoid.powers (algebraMap R S f)) M').restrictScalars R
    let tensorMap : M₁ →ₗ[R] TensorProduct R S M₁ := TensorProduct.mk R S M₁ 1
    let d : (M' × M₁) →ₗ[R] LocalizedModule.Away (algebraMap R S f) M' :=
      localizationMap.comp (LinearMap.fst R M' M₁) -
        ((α.symm.toLinearMap.restrictScalars R).comp tensorMap).comp
          (LinearMap.snd R M' M₁)
    Function.Injective (LinearMap.ker d).subtype ∧
      Function.Exact (LinearMap.ker d).subtype d ∧
        Function.Surjective d
```

## Tag 0BP4, an equation

[Tag 0BP4](https://stacks.math.columbia.edu/tag/0BP4) in the Stacks Project.

**`BeauvilleLaszlo.exists_exact_quotient_powerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean#L219).

> Suppose `A → L` is localization away from `f`, the difference map
> `A × B → L`, `(a, b) ↦ g a - h b`, is surjective, and multiplication by `f` is
> injective on `B`. If `M` is the kernel of the difference map, projection to `B` induces
> the canonical short exact sequence
> `0 → M / M[f^∞] → B → L / range(g) → 0`.
>
> The displayed compatibility uniquely specifies the induced left-hand map.

```lean
public theorem exists_exact_quotient_powerTorsion
    (f : R) (g : A →ₗ[R] L) [IsLocalizedModule.Away f g] (h : B →ₗ[R] L)
    (hd : Function.Surjective
      (g.comp (LinearMap.fst R A B) - h.comp (LinearMap.snd R A B)))
    (hf : Function.Injective (fun b : B ↦ f • b)) :
    let d := g.comp (LinearMap.fst R A B) - h.comp (LinearMap.snd R A B)
    let M := LinearMap.ker d
    let T := Submodule.torsion' R M (Submonoid.powers f)
    let q := (Submodule.mkQ (LinearMap.range g)).comp h
    ∃ i : (M ⧸ T) →ₗ[R] B,
      (∀ m : M, i (Submodule.mkQ T m) = m.1.2) ∧
        Function.Injective i ∧ LinearMap.range i = LinearMap.ker q ∧
          Function.Surjective q
```

## Tag 0BP5, an equation

[Tag 0BP5](https://stacks.math.columbia.edu/tag/0BP5) in the Stacks Project.

**`BeauvilleLaszlo.gluingDatum_baseChange_localizationQuotient_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/GlueingData.lean#L477).

> Let `(R → S, f)` be a Beauville--Laszlo glueing pair and let `(M', M₁, α)` be a
> glueing datum. If `M` is the kernel of
> `M' × M₁ → (M')_f`, `(x, y) ↦ x / 1 - α⁻¹(y ⊗ 1)`, projection to `M₁`
> induces a map `i : M / M[f^∞] → M₁`. After extending `i` to `S` and using
> `α`, it is the left map of the canonical short exact sequence
> `0 → (M / M[f^∞]) ⊗_R S → (M')_f → (M')_f / M' → 0`.
>
> The first displayed condition characterizes the induced map `i`; thus the assertion
> also records the canonical construction, rather than only the existence of some exact
> sequence with isomorphic terms.

```lean
public theorem gluingDatum_baseChange_localizationQuotient_shortExact
    (R : Type uR) [CommRing R] (S : Type uS) [CommRing S] [Algebra R S]
    (f : R)
    (hmod : ∀ n : ℕ, 0 < n →
      Function.Bijective
        (Ideal.quotientMap
          (Ideal.map (algebraMap R S) ((Ideal.span {f}) ^ n))
          (algebraMap R S) Ideal.le_comap_map))
    (hglue : (beauvilleLaszloSequence f (algebraMap R S)).ShortExact)
    (M' : Type uM) [AddCommGroup M'] [Module R M'] [Module S M']
    [IsScalarTower R S M']
    (M₁ : Type uM₁) [AddCommGroup M₁] [Module R M₁]
    [Module (Localization.Away f) M₁] [IsScalarTower R (Localization.Away f) M₁]
    (α : LocalizedModule.Away (algebraMap R S f) M' ≃ₗ[S]
      TensorProduct R S M₁) :
    let localizationMap : M' →ₗ[R] LocalizedModule.Away (algebraMap R S f) M' :=
      (LocalizedModule.mkLinearMap
        (Submonoid.powers (algebraMap R S f)) M').restrictScalars R
    let tensorMap : M₁ →ₗ[R] TensorProduct R S M₁ :=
      TensorProduct.mk R S M₁ 1
    let d : (M' × M₁) →ₗ[R] LocalizedModule.Away (algebraMap R S f) M' :=
      localizationMap.comp (LinearMap.fst R M' M₁) -
        ((α.symm.toLinearMap.restrictScalars R).comp tensorMap).comp
          (LinearMap.snd R M' M₁)
    let M := LinearMap.ker d
    let T := Submodule.torsion' R M (Submonoid.powers f)
    let q : LocalizedModule.Away (algebraMap R S f) M' →ₗ[R]
        AwayCokernel R S f M' :=
      ((LinearMap.range
        (LocalizedModule.mkLinearMap
          (Submonoid.powers (algebraMap R S f)) M')).mkQ).restrictScalars R
    ∃ i : (M ⧸ T) →ₗ[R] M₁,
      (∀ m : M, i (Submodule.mkQ T m) = m.1.2) ∧
        let iS :=
          (TensorProduct.map (LinearMap.id (R := R) (M := S)) i).comp
            (TensorProduct.comm R (M ⧸ T) S).toLinearMap
        let a := (α.symm.toLinearMap.restrictScalars R).comp iS
        Function.Injective a ∧ Function.Exact a q ∧ Function.Surjective q
```

## Tag 0BP9, a remark

[Tag 0BP9](https://stacks.math.columbia.edu/tag/0BP9) in the Stacks Project.

**`BeauvilleLaszlo.canonicalToSections_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/ModuleEquivalence.lean, line 1061](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/ModuleEquivalence.lean#L1061).

> Let `(R → S, f)` be a Beauville--Laszlo glueing pair and let `M` be any
> `R`-module. The canonical map from `M` to the compatible sections of its canonical
> glueing datum is surjective. Its target is glueable, and the map becomes an isomorphism
> after extension of scalars to `S` and after localization away from `f`.
>
> The equations on the generic and local coordinates characterize the canonical map.

```lean
public theorem canonicalToSections_surjective
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    (f : R)
    (hquot : ∀ n : ℕ, 0 < n →
      Function.Bijective (quotientPowMap f n (algebraMap R S)))
    (hglue : (beauvilleLaszloSequence f (algebraMap R S)).ShortExact)
    (M : Type w) [AddCommGroup M] [Module R M] :
    let C := FormalGlueing.moduleGlueingConstruction.{u, v, w} S (fun _ : Fin 1 ↦ f)
    letI := C.category
    let X := C.canonical.obj (ModuleCat.of R (ULift.{max u v w} M))
    let Mbar := C.sections.obj X
    ∃ g : M →ₗ[R] Mbar,
      (∀ m : M,
        let x := C.sectionsObj X (g m)
        C.canonicalGeneric (ModuleCat.of R (ULift.{max u v w} M)) x.1.1 =
          1 ⊗ₜ[R] ULift.up m ∧
          C.canonicalLocal (ModuleCat.of R (ULift.{max u v w} M)) 0 (x.1.2 0) =
            LocalizedModule.mkLinearMap (Submonoid.powers f) (ULift M) (ULift.up m)) ∧
      glueableModules (S := S) f Mbar ∧
      Function.Bijective
        (TensorProduct.map (LinearMap.id (R := R) (M := S)) g) ∧
      Function.Bijective (LocalizedModule.map (Submonoid.powers f) g) ∧
      Function.Surjective g
```

## Tag 0BP7, a lemma

[Tag 0BP7](https://stacks.math.columbia.edu/tag/0BP7) in the Stacks Project.

**`BeauvilleLaszlo.flat_iff_flat_baseChange_and_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Descent.lean, line 669](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Descent.lean#L669).

> Let `(R → S, f)` be a Beauville--Laszlo glueing pair. An `R`-module `M` is flat
> if and only if its scalar extension to `S` is flat over `S` and its localization away
> from `f` is flat over `R_f`.

```lean
public theorem flat_iff_flat_baseChange_and_localization
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    (f : R)
    (hquot : ∀ n : ℕ, 0 < n →
      Function.Bijective (quotientPowMap f n (algebraMap R S)))
    (hglue : (beauvilleLaszloSequence f (algebraMap R S)).ShortExact)
    (M : Type w) [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      Module.Flat S (S ⊗[R] M) ∧
        Module.Flat (Localization.Away f) (LocalizedModule.Away f M)
```

## Tag 0BP6, a lemma

[Tag 0BP6](https://stacks.math.columbia.edu/tag/0BP6) in the Stacks Project.

**`BeauvilleLaszlo.finite_projective_iff_baseChange_and_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/Descent.lean, line 796](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/Descent.lean#L796).

> Let `(R → S, f)` be a Beauville--Laszlo glueing pair. An `R`-module `M` is finite
> projective if and only if its scalar extension to `S` is finite projective over `S` and its
> localization away from `f` is finite projective over `R_f`.

```lean
public theorem finite_projective_iff_baseChange_and_localization
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    (f : R)
    (hquot : ∀ n : ℕ, 0 < n →
      Function.Bijective (quotientPowMap f n (algebraMap R S)))
    (hglue : (beauvilleLaszloSequence f (algebraMap R S)).ShortExact)
    (M : Type w) [AddCommGroup M] [Module R M] :
    (Module.Finite R M ∧ Module.Projective R M) ↔
      ((Module.Finite S (S ⊗[R] M) ∧ Module.Projective S (S ⊗[R] M)) ∧
        (Module.Finite (Localization.Away f) (LocalizedModule.Away f M) ∧
          Module.Projective (Localization.Away f) (LocalizedModule.Away f M)))
```

## Tag 0BP8, a remark

[Tag 0BP8](https://stacks.math.columbia.edu/tag/0BP8) in the Stacks Project.

**`BeauvilleLaszlo.beauvilleLaszlo_completion_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/BeauvilleLaszlo/CompletionComparison.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BeauvilleLaszlo/CompletionComparison.lean#L52).

> For a nonzerodivisor `f : R`, passage to the `(f)`-adic completion gives a
> Beauville--Laszlo glueing pair. Every module on which `f` is a nonzerodivisor is
> glueable, the canonical functor identifies all glueable modules with glueing data, and
> finite projectivity can be checked after completion and localization for an arbitrary
> module, with no torsion-freeness or glueability assumption on that module.

```lean
public theorem beauvilleLaszlo_completion_comparison
    (R : Type u) [CommRing R] (f : R) (hf : IsSMulRegular R f) :
    let Rhat := AdicCompletion (Ideal.span {f}) R
    (beauvilleLaszloSequence f (algebraMap R Rhat)).ShortExact ∧
      (∀ (M : Type w) [AddCommGroup M] [Module R M], IsSMulRegular M f →
        (beauvilleLaszloModuleSequence (S := Rhat) M f).ShortExact) ∧
      (let C := FormalGlueing.moduleGlueingConstruction.{u, u, w} Rhat (fun _ : Fin 1 ↦ f);
        let _ := C.category;
        (canonicalOnGlueableModules f C).IsEquivalence) ∧
      (∀ (M : Type w) [AddCommGroup M] [Module R M],
        (Module.Finite R M ∧ Module.Projective R M) ↔
          ((Module.Finite Rhat (Rhat ⊗[R] M) ∧ Module.Projective Rhat (Rhat ⊗[R] M)) ∧
            (Module.Finite (Localization.Away f) (LocalizedModule.Away f M) ∧
              Module.Projective (Localization.Away f) (LocalizedModule.Away f M))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.92, Tag 0BNI](https://stacks.math.columbia.edu/tag/0BNI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
