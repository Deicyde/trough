---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.integralClosures_after_finite_fraction_field_extension, Stacks.KummerExtension.intermediateField_eq_adjoin, Stacks.KummerExtension.isDiscreteValuationRing_A1, Stacks.KummerExtension.exists_ramificationIdx_eq, Stacks.KummerExtension.isTotallyRamified_K1, Stacks.KummerExtension.isTamelyRamified_K1, Stacks.KummerExtension.finrank_K1, Stacks.KummerExtension.integralClosure_eq_adjoin
statement: formalized
proof: formalized
---

# 15.116 Abhyankar's lemma and tame ramification

Section 15.116 of the Stacks Project, [Tag 0EXT](https://stacks.math.columbia.edu/tag/0EXT). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09EM, a remark

[Tag 09EM](https://stacks.math.columbia.edu/tag/09EM) in the Stacks Project.

**`IsDiscreteValuationRing.integralClosures_after_finite_fraction_field_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/BaseChangeClosure.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/BaseChangeClosure.lean#L743).

> The integral closures attached to a finite extension `K₁/K` and an extension of discrete
> valuation rings `A → B` have the product, spectral, local, henselian, inseparable, separable,
> and Nagata properties listed in Stacks Project, Tag 09EM.

```lean
theorem integralClosures_after_finite_fraction_field_extension
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    (K₁ : Type uK₁) (L₁ : Type uL₁) (A₁ : Type uA₁) (B₁ : Type uB₁)
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [CommRing L₁] [CommRing A₁] [CommRing B₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [IsExtension A B]
    [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L] [Algebra K K₁]
    [Algebra A K₁] [Algebra K L₁] [Algebra B L₁] [Algebra L L₁] [Algebra K₁ L₁]
    [Algebra A A₁] [Algebra B B₁] [Algebra A B₁] [Algebra A₁ B₁] [Algebra B₁ L₁]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [IsScalarTower K L L₁] [IsScalarTower K K₁ L₁] [IsScalarTower B L L₁]
    [IsScalarTower A B B₁] [IsScalarTower A A₁ B₁] [IsScalarTower B B₁ L₁]
    [IsFractionRing A K] [IsFractionRing B L] [Module.Finite K K₁]
    (eL₁ : L₁ ≃ₐ[K] ((L ⊗[K] K₁) ⧸ nilradical (L ⊗[K] K₁)))
    (eA₁ : A₁ ≃ₐ[A] integralClosure A K₁)
    (eB₁ : B₁ ≃ₐ[B] integralClosure B L₁)
    (eL₁_left : ∀ x : L,
      eL₁ (algebraMap L L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeLeft : L →ₐ[K] L ⊗[K] K₁) x))
    (eL₁_right : ∀ x : K₁,
      eL₁ (algebraMap K₁ L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁) x))
    (eB₁_coe : ∀ x : B₁, ((eB₁ x : integralClosure B L₁) : L₁) = algebraMap B₁ L₁ x)
    (hfieldSquare : ∀ x : K, algebraMap L L₁ (algebraMap K L x) =
      algebraMap K₁ L₁ (algebraMap K K₁ x))
    (hringSquare : ∀ x : A₁, algebraMap B₁ L₁ (algebraMap A₁ B₁ x) =
      algebraMap K₁ L₁ ((eA₁ x : integralClosure A K₁) : K₁)) :
    IsNonemptyFiniteProductOfFiniteFieldExtensions L L₁ ∧
      IsDedekindDomain A₁ ∧
      IsFiniteProductOfDedekindDomains B₁ ∧
      (∃ π : A,
        IsLocalRing.maximalIdeal A = Ideal.span {π} ∧
        IsRegular (algebraMap A (B ⊗[A] A₁) π) ∧
        (∃ e : Localization.Away (algebraMap A (B ⊗[A] A₁) π) ≃+* (L ⊗[K] K₁),
          (∀ b : B, e (algebraMap (B ⊗[A] A₁) _
              ((Algebra.TensorProduct.includeLeft : B →ₐ[A] B ⊗[A] A₁) b)) =
            (Algebra.TensorProduct.includeLeft : L →ₐ[K] L ⊗[K] K₁) (algebraMap B L b)) ∧
          (∀ a : A₁, e (algebraMap (B ⊗[A] A₁) _
              ((Algebra.TensorProduct.includeRight : A₁ →ₐ[A] B ⊗[A] A₁) a)) =
            (Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁)
              ((eA₁ a : integralClosure A K₁) : K₁))) ∧
        ∃ g : (B ⊗[A] A₁) →+* B₁,
          g.IsIntegral ∧ RingHom.ker g ≤ nilradical (B ⊗[A] A₁) ∧
          Function.Surjective (PrimeSpectrum.comap g) ∧
          (∀ b : B, g ((Algebra.TensorProduct.includeLeft : B →ₐ[A] B ⊗[A] A₁) b) =
            algebraMap B B₁ b) ∧
          (∀ a : A₁, g ((Algebra.TensorProduct.includeRight : A₁ →ₐ[A] B ⊗[A] A₁) a) =
            algebraMap A₁ B₁ a)) ∧
      Function.Surjective (PrimeSpectrum.comap (algebraMap A₁ B₁)) ∧
      Finite (MaximalSpectrum A₁) ∧
      Nonempty (MaximalSpectrum A₁) ∧
      (∀ p : MaximalSpectrum A₁,
        Finite {q : MaximalSpectrum B₁ //
          q.asIdeal.comap (algebraMap A₁ B₁) = p.asIdeal} ∧
        Nonempty {q : MaximalSpectrum B₁ //
          q.asIdeal.comap (algebraMap A₁ B₁) = p.asIdeal}) ∧
      (∀ p : Ideal A₁, p.IsMaximal →
        ∃ q : Ideal B₁, q.IsMaximal ∧ q.comap (algebraMap A₁ B₁) = p) ∧
      (∀ q : Ideal B₁, q.IsMaximal →
        (q.comap (algebraMap A₁ B₁)).IsMaximal ∧
        ∃ (_ : q.IsPrime) (_ : (q.comap (algebraMap A₁ B₁)).IsPrime),
          (∃ _ : IsDomain (Localization (q.comap (algebraMap A₁ B₁)).primeCompl),
            IsDiscreteValuationRing (Localization (q.comap (algebraMap A₁ B₁)).primeCompl)) ∧
          (∃ _ : IsDomain (Localization q.primeCompl),
            IsDiscreteValuationRing (Localization q.primeCompl)) ∧
          ∃ φ : Localization (q.comap (algebraMap A₁ B₁)).primeCompl →+*
              Localization q.primeCompl,
            Function.Injective φ ∧ IsLocalHom φ ∧
              ∀ x : A₁, φ (algebraMap A₁ _ x) = algebraMap B₁ _ (algebraMap A₁ B₁ x)) ∧
      (HenselianLocalRing A → ∃ _ : IsDomain A₁, IsDiscreteValuationRing A₁) ∧
      (IsAdicComplete (IsLocalRing.maximalIdeal A) A →
        ∃ _ : IsDomain A₁, IsDiscreteValuationRing A₁) ∧
      (HenselianLocalRing B →
        IsFiniteProductOfDiscreteValuationRings B₁) ∧
      (IsAdicComplete (IsLocalRing.maximalIdeal B) B →
        IsFiniteProductOfDiscreteValuationRings B₁) ∧
      (IsPurelyInseparable K K₁ →
        (∃ _ : IsDomain A₁, IsDiscreteValuationRing A₁) ∧
        (∃ _ : IsDomain B₁, IsDiscreteValuationRing B₁)) ∧
      (Algebra.IsSeparable K K₁ →
        IsReduced (L ⊗[K] K₁) ∧
        IsNonemptyFiniteProductOfFiniteSeparableFieldExtensions L L₁ ∧
        Module.Finite A A₁ ∧ Module.Finite B B₁) ∧
      (IsNagataRing A → Module.Finite A A₁) ∧
      (IsNagataRing B → Module.Finite B B₁)
```

## Tag 09EV, a lemma

[Tag 09EV](https://stacks.math.columbia.edu/tag/09EV) in the Stacks Project.

**`Stacks.KummerExtension.intermediateField_eq_adjoin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/IntermediateFields.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/IntermediateFields.lean#L406). The attribute's comment: “(6)”.

> If `n` is prime to the residue characteristic of `A`, then every intermediate field
> `K ⊆ L ⊆ K_1` is of the form `L = K[pi^{1/d}]` for some positive divisor `d | n`: `L` is generated
> over `K` by the `d`-th root `(pi')^{n/d}` of `pi`, and `[L : K] = d` and `[K_1 : L] = n / d`.

```lean
theorem intermediateField_eq_adjoin [Fact (Irreducible (kummerPoly K π n))]
    (hn : 2 ≤ n) (hπ : Irreducible π)
    (hcop : ringChar (A ⧸ IsLocalRing.maximalIdeal A) = 0 ∨
      Nat.Coprime (ringChar (A ⧸ IsLocalRing.maximalIdeal A)) n)
    (L : IntermediateField K (K1 K π n)) :
    ∃ d : ℕ, 0 < d ∧ d ∣ n ∧
      L = IntermediateField.adjoin K {(piRoot K π n) ^ (n / d)} ∧
      Module.finrank K L = d ∧
      Module.finrank L (K1 K π n) = n / d
```

**`Stacks.KummerExtension.isDiscreteValuationRing_A1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean#L184). The attribute's comment: “(3)”.

> `A_1` is a discrete valuation ring.

```lean
theorem isDiscreteValuationRing_A1 [Fact (Irreducible (kummerPoly K π n))]
    (hn : 2 ≤ n) (hπ : Irreducible π) :
    IsDiscreteValuationRing (A1 K π n)
```

**`Stacks.KummerExtension.exists_ramificationIdx_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean#L221). The attribute's comment: “(4)”.

> `A_1` has a unique maximal ideal `m` lying over `m_A`, and the ramification index of `m`
> over `m_A` is `n`.

```lean
theorem exists_ramificationIdx_eq (hn : 2 ≤ n) (hπ : Irreducible π) :
    ∃ m : Ideal (A1 K π n), m.IsMaximal ∧
      m.LiesOver (IsLocalRing.maximalIdeal A) ∧
      (∀ m' : Ideal (A1 K π n), m'.IsMaximal →
        m'.LiesOver (IsLocalRing.maximalIdeal A) → m' = m) ∧
      Ideal.ramificationIdx' (IsLocalRing.maximalIdeal A) m = n
```

**`Stacks.KummerExtension.isTotallyRamified_K1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean#L284). The attribute's comment: “(5)”.

> `K_1 / K` is totally ramified with respect to `A`, whatever the residue characteristic of
> `A`.

```lean
theorem isTotallyRamified_K1 [Fact (Irreducible (kummerPoly K π n))]
    (hn : 2 ≤ n) (hπ : Irreducible π) :
    IsTotallyRamified A K (K1 K π n)
```

**`Stacks.KummerExtension.isTamelyRamified_K1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Ramification.lean#L371). The attribute's comment: “(6)”.

> If `n` is prime to the residue characteristic of `A`, then `K_1 / K` is tamely ramified
> with respect to `A`.

```lean
theorem isTamelyRamified_K1 [Fact (Irreducible (kummerPoly K π n))]
    [Algebra.IsSeparable K (K1 K π n)]
    (hn : 2 ≤ n) (hπ : Irreducible π)
    (hcop : ringChar (A ⧸ IsLocalRing.maximalIdeal A) = 0 ∨
      Nat.Coprime (ringChar (A ⧸ IsLocalRing.maximalIdeal A)) n) :
    IsTamelyRamified A K (K1 K π n)
```

**`Stacks.KummerExtension.finrank_K1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/RingOfIntegers.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/RingOfIntegers.lean#L396). The attribute's comment: “(1)”.

> `[K_1 : K] = n`.

```lean
theorem finrank_K1 (hn : 2 ≤ n) (hπ : Irreducible π) :
    Module.finrank K (K1 K π n) = n
```

**`Stacks.KummerExtension.integralClosure_eq_adjoin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/RingOfIntegers.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/RingOfIntegers.lean#L555). The attribute's comment: “(2)”.

> The integral closure `A_1` of `A` in `K_1` is the `A`-subalgebra `A[pi'] = A[pi^{1/n}]`
> generated by `pi'`.

```lean
theorem integralClosure_eq_adjoin (hn : 2 ≤ n) (hπ : Irreducible π) :
    (A1 K π n) = Algebra.adjoin A {piRoot K π n}
```

## Tag 09EQ, a lemma

[Tag 09EQ](https://stacks.math.columbia.edu/tag/09EQ) in the Stacks Project.

**`IsDiscreteValuationRing.formallySmooth_localizations_after_finite_fraction_field_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/FiniteFractionFieldExtension.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/FiniteFractionFieldExtension.lean#L359). The attribute's comment: “Corrected statement. The formal smoothness of every local extension `(A₁)_{𝔪_i} → (B₁)_{𝔪_ij}` holds for every finite `K₁ / K`, as printed, and so does `B₁ = (B ⊗_A A₁)_red`. The printed equalities `L₁ = L ⊗_K K₁` and `B₁ = B ⊗_A A₁` are false in general (`exists_formallySmoothNAdic_not_isReduced_tensorProduct`); both say that `L ⊗_K K₁` is reduced, and both are proved here in exactly that case. Recorded in `errata.md`.”.

> Formal smoothness of an extension of discrete valuation rings persists at every local factor
> after a finite extension of the fraction field.  The integral closure upstairs is the reduced
> tensor product, and it is the unreduced tensor product whenever `L ⊗_K K₁` is reduced, which is
> exactly when `L₁ = L ⊗_K K₁`.

```lean
theorem formallySmooth_localizations_after_finite_fraction_field_extension
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    (K₁ : Type uK₁) (L₁ : Type uL₁) (A₁ : Type uA₁) (B₁ : Type uB₁)
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [CommRing L₁] [CommRing A₁] [CommRing B₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [IsExtension A B]
    [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L] [Algebra K K₁]
    [Algebra A K₁] [Algebra K L₁] [Algebra B L₁] [Algebra L L₁] [Algebra K₁ L₁]
    [Algebra A A₁] [Algebra B B₁] [Algebra A B₁] [Algebra A₁ B₁] [Algebra B₁ L₁]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [IsScalarTower K L L₁] [IsScalarTower K K₁ L₁] [IsScalarTower B L L₁]
    [IsScalarTower A B B₁] [IsScalarTower A A₁ B₁] [IsScalarTower B B₁ L₁]
    [IsFractionRing A K] [IsFractionRing B L] [Module.Finite K K₁]
    (eL₁ : L₁ ≃ₐ[K] ((L ⊗[K] K₁) ⧸ nilradical (L ⊗[K] K₁)))
    (eA₁ : A₁ ≃ₐ[A] integralClosure A K₁)
    (eB₁ : B₁ ≃ₐ[B] integralClosure B L₁)
    (eL₁_left : ∀ x : L,
      eL₁ (algebraMap L L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeLeft : L →ₐ[K] L ⊗[K] K₁) x))
    (eL₁_right : ∀ x : K₁,
      eL₁ (algebraMap K₁ L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁) x))
    (eB₁_coe : ∀ x : B₁, ((eB₁ x : integralClosure B L₁) : L₁) = algebraMap B₁ L₁ x)
    (hfieldSquare : ∀ x : K, algebraMap L L₁ (algebraMap K L x) =
      algebraMap K₁ L₁ (algebraMap K K₁ x))
    (hringSquare : ∀ x : A₁, algebraMap B₁ L₁ (algebraMap A₁ B₁ x) =
      algebraMap K₁ L₁ ((eA₁ x : integralClosure A K₁) : K₁))
    (hformal : RingHom.FormallySmoothNAdic.{max uA uB} (algebraMap A B)
      (IsLocalRing.maximalIdeal B)) :
    (∃ eB : B₁ ≃ₐ[B] ((B ⊗[A] A₁) ⧸ nilradical (B ⊗[A] A₁)),
        (∀ x : A₁, eB (algebraMap A₁ B₁ x) = Ideal.Quotient.mk _
          ((Algebra.TensorProduct.includeRight : A₁ →ₐ[A] B ⊗[A] A₁) x))) ∧
      (IsReduced (L ⊗[K] K₁) →
        (∃ eL : L₁ ≃ₐ[L] (L ⊗[K] K₁),
        (∀ x : L₁, Ideal.Quotient.mk _ (eL x) = eL₁ x) ∧
        (∀ x : K₁, eL (algebraMap K₁ L₁ x) =
          (Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁) x)) ∧
      (∃ eB : B₁ ≃ₐ[B] (B ⊗[A] A₁),
        (∀ x : A₁, eB (algebraMap A₁ B₁ x) =
          (Algebra.TensorProduct.includeRight : A₁ →ₐ[A] B ⊗[A] A₁) x))) ∧
      (∀ q : Ideal B₁, q.IsMaximal →
        (q.comap (algebraMap A₁ B₁)).IsMaximal ∧
        ∃ (_ : q.IsPrime) (_ : (q.comap (algebraMap A₁ B₁)).IsPrime),
          (∃ _ : IsDomain (Localization (q.comap (algebraMap A₁ B₁)).primeCompl),
            IsDiscreteValuationRing
              (Localization (q.comap (algebraMap A₁ B₁)).primeCompl)) ∧
          (∃ _ : IsDomain (Localization q.primeCompl),
            IsDiscreteValuationRing (Localization q.primeCompl)) ∧
          ∃ φ : Localization (q.comap (algebraMap A₁ B₁)).primeCompl →+*
              Localization q.primeCompl,
            Function.Injective φ ∧ IsLocalHom φ ∧
              (∀ x : A₁, φ (algebraMap A₁ _ x) =
                algebraMap B₁ _ (algebraMap A₁ B₁ x)) ∧
              RingHom.FormallySmoothNAdic.{max uA₁ uB₁} φ
                (IsLocalRing.maximalIdeal (Localization q.primeCompl)))
```

**`IsDiscreteValuationRing.exists_formallySmoothNAdic_not_isReduced_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/FiniteFractionFieldExtensionCounterexample.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/FiniteFractionFieldExtensionCounterexample.lean#L69). The attribute's comment: “The printed equalities `L₁ = L ⊗_K K₁` and `B₁ = B ⊗_A A₁` are false in general: this is the counterexample, `A → A^` for a non-excellent discrete valuation ring of characteristic two and a purely inseparable `K₁ / K` of degree two. The corrected statement, with the equalities under the hypothesis that `L ⊗_K K₁` is reduced, is `formallySmooth_localizations_after_finite_fraction_field_extension`.”.

> **The equalities of Tag 09EQ fail as printed.** There are an extension `A → B` of discrete
> valuation rings, formally smooth for the `𝔪_B`-adic topology, and a finite extension `K₁ / K` of
> the fraction field of `A`, such that neither `L ⊗_K K₁` nor `B ⊗_A A₁` is reduced, where `L` is
> the fraction field of `B` and `A₁` the integral closure of `A` in `K₁`. Since `L₁ = (L ⊗_K K₁)_red`
> and its subring `B₁` are reduced, neither `L₁ = L ⊗_K K₁` nor `B₁ = B ⊗_A A₁` holds.
>
> The witness is `A → A^` for the characteristic-two discrete valuation ring of Tag 00PB, with
> `K₁ = K(√a)` for an `a ∈ A` that is a square in `A^` but not in `K`.

```lean
theorem exists_formallySmoothNAdic_not_isReduced_tensorProduct :
    ∃ (A B K L K₁ : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : IsDiscreteValuationRing A)
      (_ : CommRing B) (_ : IsDomain B) (_ : IsDiscreteValuationRing B) (_ : Algebra A B)
      (_ : IsExtension A B) (_ : Field K) (_ : Field L) (_ : Field K₁)
      (_ : Algebra A K) (_ : Algebra A L) (_ : Algebra B L) (_ : Algebra K L)
      (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A B L) (_ : IsScalarTower A K L) (_ : IsScalarTower A K K₁)
      (_ : IsFractionRing A K) (_ : IsFractionRing B L) (_ : Module.Finite K K₁),
      RingHom.FormallySmoothNAdic.{u} (algebraMap A B) (maximalIdeal B) ∧
        ¬ IsReduced (L ⊗[K] K₁) ∧ ¬ IsReduced (B ⊗[A] integralClosure A K₁)
```

## Tag 0BRM, a lemma

[Tag 0BRM](https://stacks.math.columbia.edu/tag/0BRM) in the Stacks Project.

**`IsDiscreteValuationRing.formallySmooth_localizations_of_ramificationIndex_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/AbhyankarLemma.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/AbhyankarLemma.lean#L97).

> **Abhyankar's lemma.** A tamely ramified extension of discrete valuation rings becomes
> formally smooth at every local factor after a finite fraction-field extension whose local
> ramification index is divisible by the original one.

```lean
theorem formallySmooth_localizations_of_ramificationIndex_dvd
    (A : Type u) (B : Type v) (K : Type w) (L : Type x) (K₁ : Type y)
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [IsExtension A B]
    [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L] [Algebra K K₁]
    [Algebra A K₁]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [IsFractionRing A K] [IsFractionRing B L] [Module.Finite K K₁]
    (htame : ringChar (IsLocalRing.ResidueField A) = 0 ∨
      Nat.Coprime (ringChar (IsLocalRing.ResidueField A))
          (ramificationIndex A B) ∧
        Algebra.IsSeparableExtension (IsLocalRing.ResidueField A)
          (IsLocalRing.ResidueField B)) :
    ∃ (n : ℕ) (E : Fin n → Type (max u v w x y))
      (_ : ∀ i, Field (E i))
      (_ : ∀ i, Algebra K (E i))
      (_ : ∀ i, Algebra L (E i))
      (_ : ∀ i, Algebra K₁ (E i))
      (_ : ∀ i, Algebra B (E i))
      (_ : ∀ i, IsScalarTower K L (E i))
      (_ : ∀ i, IsScalarTower K K₁ (E i))
      (_ : ∀ i, Module.Finite L (E i))
      (decomp : ((L ⊗[K] K₁) ⧸ nilradical (L ⊗[K] K₁)) ≃ₐ[K] ∀ i, E i),
      0 < n ∧
      (∀ i (z : L),
        decomp (Ideal.Quotient.mk _
          ((Algebra.TensorProduct.includeLeft : L →ₐ[K] L ⊗[K] K₁) z)) i =
          algebraMap L (E i) z) ∧
      (∀ i (z : K₁),
        decomp (Ideal.Quotient.mk _
          ((Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁) z)) i =
          algebraMap K₁ (E i) z) ∧
      (∀ i (z : B), algebraMap B (E i) z =
        algebraMap L (E i) (algebraMap B L z)) ∧
      ∀ i, let A₁ := integralClosure A K₁
        let B₁ := integralClosure B (E i)
        ∃ f : A₁ →+* B₁,
          (∀ z : A₁, ((f z : B₁) : E i) =
            algebraMap K₁ (E i) ((z : A₁) : K₁)) ∧
          (∀ z : A, f (algebraMap A A₁ z) =
            algebraMap B B₁ (algebraMap A B z)) ∧
          ∀ p : Ideal A₁, p.IsMaximal →
            ramificationIndex A B ∣ p.ramificationIdx A →
            ∀ q : Ideal B₁, q.IsMaximal → q.comap f = p →
              ∃ (_ : q.IsPrime) (_ : p.IsPrime),
                (∃ _ : IsDomain (Localization p.primeCompl),
                  IsDiscreteValuationRing (Localization p.primeCompl)) ∧
                (∃ _ : IsDomain (Localization q.primeCompl),
                  IsDiscreteValuationRing (Localization q.primeCompl)) ∧
                ∃ φ : Localization p.primeCompl →+* Localization q.primeCompl,
                  Function.Injective φ ∧ IsLocalHom φ ∧
                    (∀ z : A₁, φ (algebraMap A₁ _ z) =
                      algebraMap B₁ _ (f z)) ∧
                    RingHom.FormallySmoothNAdic φ
                      (IsLocalRing.maximalIdeal (Localization q.primeCompl))
```

## Tag 0EXU, a lemma

[Tag 0EXU](https://stacks.math.columbia.edu/tag/0EXU) in the Stacks Project.

**`IsDiscreteValuationRing.isTamelyRamified_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/TameRamification.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/TameRamification.lean#L307).

> Tame ramification composes in a tower of finite separable extensions when
> the upper extension is tamely ramified at every maximal localization of the
> intermediate integral closure.

```lean
theorem isTamelyRamified_tower
    (A : Type u) (K : Type v) (L : Type w) (M : Type x)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Field L] [Field M]
    [Algebra A K] [IsFractionRing A K]
    [Algebra K L] [Algebra L M] [Algebra K M] [IsScalarTower K L M]
    [Algebra A L] [IsScalarTower A K L]
    [Algebra A M] [IsScalarTower A K M] [IsScalarTower A L M]
    [Module.Finite K L] [Algebra.IsSeparable K L]
    [Module.Finite L M] [Algebra.IsSeparable L M]
    (hLK : Stacks.KummerExtension.IsTamelyRamified A K L)
    (hML : ∀ (m : Ideal (integralClosure A L)) (hm : m.IsMaximal),
      letI : m.IsPrime := hm.isPrime
      letI : IsFractionRing (integralClosure A L) L :=
        integralClosure.isFractionRing_of_finite_extension K L
      letI : Algebra (Localization.AtPrime m) L :=
        IsLocalization.localizationAlgebraOfSubmonoidLe _ _ m.primeCompl
          (nonZeroDivisors (integralClosure A L)) m.primeCompl_le_nonZeroDivisors
      letI : Algebra (Localization.AtPrime m) M :=
        ((algebraMap L M).comp (algebraMap (Localization.AtPrime m) L)).toAlgebra
      letI : IsScalarTower (Localization.AtPrime m) L M :=
        IsScalarTower.of_algebraMap_eq fun _ => rfl
      Stacks.KummerExtension.IsTamelyRamified (Localization.AtPrime m) L M) :
    letI : Module.Finite K M := Module.Finite.trans L M
    letI : Algebra.IsSeparable K M := Algebra.IsSeparable.trans K L M
    Stacks.KummerExtension.IsTamelyRamified A K M
```

## Tag 0EXV, a lemma

[Tag 0EXV](https://stacks.math.columbia.edu/tag/0EXV) in the Stacks Project.

**`IsDiscreteValuationRing.isTamelyRamified_of_isTamelyRamified_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/TameRamification.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/TameRamification.lean#L398). References: SGA 1 XIII (2.0.3), “subalgebra of tame”.

> Every intermediate extension of a finite separable extension tamely ramified
> with respect to a discrete valuation ring is itself tamely ramified.

```lean
theorem isTamelyRamified_of_isTamelyRamified_tower
    (A : Type u) (K : Type v) (L : Type w) (M : Type x)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Field L] [Field M]
    [Algebra A K] [IsFractionRing A K]
    [Algebra K L] [Algebra L M] [Algebra K M] [IsScalarTower K L M]
    [Algebra A L] [IsScalarTower A K L]
    [Algebra A M] [IsScalarTower A K M] [IsScalarTower A L M]
    [Module.Finite K L] [Algebra.IsSeparable K L]
    [Module.Finite L M] [Algebra.IsSeparable L M]
    (hM : letI : Module.Finite K M := Module.Finite.trans L M
      letI : Algebra.IsSeparable K M := Algebra.IsSeparable.trans K L M
      Stacks.KummerExtension.IsTamelyRamified A K M) :
    Stacks.KummerExtension.IsTamelyRamified A K L
```

## Tag 0EXW, a lemma

[Tag 0EXW](https://stacks.math.columbia.edu/tag/0EXW) in the Stacks Project.

**`IsDiscreteValuationRing.isTamelyRamifiedWithRespectTo_tfae_hasUnramifiedKummerOverfield`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/TameRamificationKummer.lean, line 764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/TameRamificationKummer.lean#L764).

> A finite separable extension of the fraction field of a discrete valuation ring is tamely
> ramified if and only if it embeds into an unramified extension after some Kummer base change;
> equivalently, such an unramified overfield exists after every prime-to-residue-characteristic
> multiple of one fixed exponent.

```lean
theorem isTamelyRamifiedWithRespectTo_tfae_hasUnramifiedKummerOverfield
    (A : Type u) (K : Type v) (L : Type w)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Field L]
    [Algebra A K] [IsFractionRing A K]
    [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    [FiniteDimensional K L] [Algebra.IsSeparable K L]
    (π : A) (hπ : Irreducible π) :
    List.TFAE
      [ IsTamelyRamifiedWithRespectTo A K L,
        ∃ e : ℕ, HasUnramifiedKummerOverfield A K L π hπ e,
        ∃ e₀ : ℕ, 1 ≤ e₀ ∧ IsUnit (e₀ : IsLocalRing.ResidueField A) ∧
          ∀ d : ℕ, 1 ≤ d → IsUnit (d : IsLocalRing.ResidueField A) →
            HasUnramifiedKummerOverfield A K L π hπ (d * e₀) ]
```

## Tag 0EXX, a lemma

[Tag 0EXX](https://stacks.math.columbia.edu/tag/0EXX) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isGalois_and_common_extension_isTamelyRamifiedWithRespectTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/TameGaloisClosure.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/TameGaloisClosure.lean#L249).

> **Stacks 0EXX.** Every finite separable extension of the fraction field of a discrete
> valuation ring which is tamely ramified with respect to the ring is contained in a finite
> Galois extension with the same property. Any two such extensions are contained in a common
> finite separable extension which is again tamely ramified.

```lean
theorem exists_isGalois_and_common_extension_isTamelyRamifiedWithRespectTo
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K] :
    (∀ (L : Type w) [Field L] [Algebra K L] [FiniteDimensional K L]
        [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L],
      IsTamelyRamifiedWithRespectTo A K L →
        ∃ (M : Type (max u v w)) (_ : Field M) (_ : Algebra K M)
          (_ : FiniteDimensional K M) (_ : Algebra.IsSeparable K M)
          (_ : Algebra A M) (_ : IsScalarTower A K M)
          (_ : Algebra L M) (_ : IsScalarTower K L M),
          IsGalois K M ∧ IsTamelyRamifiedWithRespectTo A K M) ∧
    (∀ (L₁ : Type w) [Field L₁] [Algebra K L₁] [FiniteDimensional K L₁]
        [Algebra.IsSeparable K L₁] [Algebra A L₁] [IsScalarTower A K L₁]
        (L₂ : Type x) [Field L₂] [Algebra K L₂] [FiniteDimensional K L₂]
        [Algebra.IsSeparable K L₂] [Algebra A L₂] [IsScalarTower A K L₂],
      IsTamelyRamifiedWithRespectTo A K L₁ →
        IsTamelyRamifiedWithRespectTo A K L₂ →
        ∃ (L : Type (max u v w x)) (_ : Field L) (_ : Algebra K L)
          (_ : FiniteDimensional K L) (_ : Algebra.IsSeparable K L)
          (_ : Algebra A L) (_ : IsScalarTower A K L)
          (_ : Algebra L₁ L) (_ : IsScalarTower K L₁ L)
          (_ : Algebra L₂ L) (_ : IsScalarTower K L₂ L),
          IsTamelyRamifiedWithRespectTo A K L)
```

## Tag 0EXY, a lemma

[Tag 0EXY](https://stacks.math.columbia.edu/tag/0EXY) in the Stacks Project.

**`IsDiscreteValuationRing.exists_algEquiv_pi_field_and_ramification_goes_up`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/RamificationGoesUp.lean, line 780](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Abhyankar/RamificationGoesUp.lean#L780). References: SGA 1 XIII (2.0.3), “tame after DVR extension”; SGA 1 XIII (2.0.2), “⇒: tameness ascends”.

> **Stacks 0EXY.** A finite separable field extension remains a finite product of fields after
> scalar extension along an extension of discrete valuation rings. If the original extension is
> unramified, respectively tamely ramified, then every resulting field factor has the same
> property over the larger discrete valuation ring.

```lean
theorem exists_algEquiv_pi_field_and_ramification_goes_up
    (A : Type u) (B : Type v) (K : Type w) (L : Type x) (K' : Type y)
    [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Field K] [Field L] [Field K']
    [Algebra A B] [IsExtension A B]
    [Algebra A K] [IsFractionRing A K]
    [Algebra B L] [IsFractionRing B L]
    [Algebra K L] [Algebra A L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [Algebra K K'] [Algebra A K'] [IsScalarTower A K K']
    [Module.Finite K K'] [Algebra.IsSeparable K K'] :
    ∃ (n : ℕ) (E : Fin n → Type (max u v w x y))
        (_ : ∀ i, Field (E i))
        (_ : ∀ i, Algebra L (E i))
        (_ : ∀ i, Algebra B (E i))
        (_ : ∀ i, IsScalarTower B L (E i))
        (_ : ∀ i, Module.Finite L (E i))
        (_ : ∀ i, Algebra.IsSeparable L (E i)),
      0 < n ∧
        Nonempty ((L ⊗[K] K') ≃ₐ[L] ∀ i, E i) ∧
        (IsUnramifiedWithRespectTo A K K' →
          ∀ i, IsUnramifiedWithRespectTo B L (E i)) ∧
        (IsTamelyRamifiedWithRespectTo A K K' →
          ∀ i, IsTamelyRamifiedWithRespectTo B L (E i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.116, Tag 0EXT](https://stacks.math.columbia.edu/tag/0EXT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
