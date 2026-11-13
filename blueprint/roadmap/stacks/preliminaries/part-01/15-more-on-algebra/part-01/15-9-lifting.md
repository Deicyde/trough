---
declaration: section
origin: cited
lean: Algebra.exists_etale_bijective_quotientMap_isUnit, Algebra.exists_etale_bijective_quotientMap_isIdempotentElem, exists_etale_lift_of_finite_disjoint_open_cover, exists_isUnit_quotient_mk_and_etale_away, exists_etale_lift_of_isCoprime_factorization, exists_etale_lift_of_isUnit_leadingCoeff_isCoprime_factorization, counterexample_to_etale_lift_without_isUnit_leadingCoeff, exists_quotient_eq_one_and_map_mem
statement: formalized
proof: formalized
---

# 15.9 Lifting

Section 15.9 of the Stacks Project, [Tag 07LW](https://stacks.math.columbia.edu/tag/07LW). 14 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07LX, a lemma

[Tag 07LX](https://stacks.math.columbia.edu/tag/07LX) in the Stacks Project.

**`Algebra.exists_etale_bijective_quotientMap_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean#L111).

> **Stacks 07LX**.
> For an ideal `I` of `A` and a unit `u` of `A ⧸ I`, there is an étale `A`-algebra `A'` such that
> the induced map `A ⧸ I → A' ⧸ IA'` is bijective, together with a unit `u'` of `A'` whose class in
> `A' ⧸ IA'` is the image of `u`.

```lean
theorem Algebra.exists_etale_bijective_quotientMap_isUnit {A : Type u} [CommRing A] (I : Ideal A)
    (u : A ⧸ I) (hu : IsUnit u) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A') (u' : A'),
      Algebra.Etale A A' ∧ IsUnit u' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A') Ideal.le_comap_map) ∧
      Ideal.Quotient.mk (I.map (algebraMap A A')) u' =
        Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A') Ideal.le_comap_map u
```

## Tag 07LY, a lemma

[Tag 07LY](https://stacks.math.columbia.edu/tag/07LY) in the Stacks Project.

**`Algebra.exists_etale_bijective_quotientMap_isIdempotentElem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean#L69).

> **Stacks 07LY**.
> For an ideal `I` of `A` and an idempotent `e` of `A ⧸ I`, there is an étale `A`-algebra `A'` such
> that the induced map `A ⧸ I → A' ⧸ IA'` is bijective, together with an idempotent `e'` of `A'`
> whose class in `A' ⧸ IA'` is the image of `e`.

```lean
theorem Algebra.exists_etale_bijective_quotientMap_isIdempotentElem {A : Type u} [CommRing A]
    (I : Ideal A) (e : A ⧸ I) (he : IsIdempotentElem e) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A') (e' : A'),
      Algebra.Etale A A' ∧ IsIdempotentElem e' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A') Ideal.le_comap_map) ∧
      Ideal.Quotient.mk (I.map (algebraMap A A')) e' =
        Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A') Ideal.le_comap_map e
```

## Tag 07LZ, a lemma

[Tag 07LZ](https://stacks.math.columbia.edu/tag/07LZ) in the Stacks Project.

**`exists_etale_lift_of_finite_disjoint_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftUnitsIdempotents.lean#L343).

> **Stacks 07LZ.** A finite disjoint open covering of `Spec(A ⧸ I)` lifts to a finite disjoint
> open covering after an étale extension `A → A'` inducing an isomorphism modulo `I`.

```lean
theorem exists_etale_lift_of_finite_disjoint_open_cover
    {A : Type u} [CommRing A] (I : Ideal A) {J : Type v} [Finite J]
    (U : J → Set (PrimeSpectrum (A ⧸ I)))
    (hU_open : ∀ j, IsOpen (U j))
    (hU_disjoint : Pairwise fun i j ↦ Disjoint (U i) (U j))
    (hU_cover : ⋃ j, U j = Set.univ) :
    ∃ (A' : Type u) (_ : CommRing A') (f : A →+* A')
      (U' : J → Set (PrimeSpectrum A')),
      f.Etale ∧
      Function.Bijective
        (Ideal.quotientMap (Ideal.map f I) f Ideal.le_comap_map) ∧
      (∀ j, IsOpen (U' j)) ∧
      (Pairwise fun i j ↦ Disjoint (U' i) (U' j)) ∧
      (⋃ j, U' j = Set.univ) ∧
      ∀ j,
        PrimeSpectrum.comap (Ideal.Quotient.mk (Ideal.map f I)) ⁻¹' U' j =
          PrimeSpectrum.comap
            (Ideal.quotientMap (Ideal.map f I) f Ideal.le_comap_map) ⁻¹' U j
```

## Tag 07M0, a lemma

[Tag 07M0](https://stacks.math.columbia.edu/tag/07M0) in the Stacks Project.

**`exists_isUnit_quotient_mk_and_etale_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Locus.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Locus.lean#L92).

> **Stacks 07M0.** If `A → B` is étale at every prime containing `J`, there is an element
> `g : B` whose image in `B ⧸ J` is a unit and such that `B` localized away from `g` is étale
> over `A`.

```lean
theorem exists_isUnit_quotient_mk_and_etale_away
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B] (J : Ideal B)
    (h : ∀ (q : Ideal B) [q.IsPrime], J ≤ q →
      ∃ f ∉ q, Algebra.Etale A (Localization.Away f)) :
    ∃ g : B, IsUnit (Ideal.Quotient.mk J g) ∧
      Algebra.Etale A (Localization.Away g)
```

## Tag 0ALH, a lemma

[Tag 0ALH](https://stacks.math.columbia.edu/tag/0ALH) in the Stacks Project.

**`exists_etale_lift_of_isCoprime_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftFactorization.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftFactorization.lean#L68).

> **Stacks 0ALH.** A factorization of a monic polynomial into coprime monic factors modulo an
> ideal lifts to a factorization into monic polynomials over an étale algebra which induces an
> isomorphism modulo the extended ideal.

```lean
theorem exists_etale_lift_of_isCoprime_factorization
    {A : Type u} [CommRing A] (I : Ideal A) (f : Polynomial A)
    (gbar hbar : Polynomial (A ⧸ I)) (hf : f.Monic) (hgbar : gbar.Monic)
    (hhbar : hbar.Monic) (hfac : f.map (Ideal.Quotient.mk I) = gbar * hbar)
    (hcoprime : IsCoprime gbar hbar) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A') (g' h' : Polynomial A'),
      Algebra.Etale A A' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
          Ideal.le_comap_map) ∧
      g'.Monic ∧ h'.Monic ∧ IsCoprime g' h' ∧
      f.map (algebraMap A A') = g' * h' ∧
      gbar.map
          (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
            Ideal.le_comap_map) =
        g'.map (Ideal.Quotient.mk (I.map (algebraMap A A'))) ∧
      hbar.map
          (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
            Ideal.le_comap_map) =
        h'.map (Ideal.Quotient.mk (I.map (algebraMap A A')))
```

## Tag 07M1, a lemma

[Tag 07M1](https://stacks.math.columbia.edu/tag/07M1) in the Stacks Project.

**`exists_etale_lift_of_isUnit_leadingCoeff_isCoprime_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftFactorization.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftFactorization.lean#L290).

> **Stacks 07M1.** A coprime factorization modulo an ideal, with invertible leading coefficient
> of the first factor, lifts to a factorization over an étale algebra which induces an isomorphism
> modulo the extended ideal.

```lean
theorem exists_etale_lift_of_isUnit_leadingCoeff_isCoprime_factorization
    {A : Type u} [CommRing A] (I : Ideal A) (f : Polynomial A)
    (gbar hbar : Polynomial (A ⧸ I)) (hf : f.Monic)
    (hgbar : IsUnit gbar.leadingCoeff)
    (hfac : f.map (Ideal.Quotient.mk I) = gbar * hbar)
    (hcoprime : IsCoprime gbar hbar) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A') (g' h' : Polynomial A'),
      Algebra.Etale A A' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
          Ideal.le_comap_map) ∧
      f.map (algebraMap A A') = g' * h' ∧
      gbar.map
          (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
            Ideal.le_comap_map) =
        g'.map (Ideal.Quotient.mk (I.map (algebraMap A A'))) ∧
      hbar.map
          (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
            Ideal.le_comap_map) =
        h'.map (Ideal.Quotient.mk (I.map (algebraMap A A')))
```

## Tag 07M2, an example

[Tag 07M2](https://stacks.math.columbia.edu/tag/07M2) in the Stacks Project.

**`counterexample_to_etale_lift_without_isUnit_leadingCoeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftFactorization.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftFactorization.lean#L626).

> **Stacks 07M2.** The monic polynomial `1` factors modulo `4` as `(2X² + 2X + 1)²`, with
> coprime factors but non-invertible leading coefficient. Nevertheless there is no étale extension
> of `ℤ`, unchanged modulo `4`, carrying a factorization together with the two canonical reduction
> equalities asserted in Stacks 07M1. The two completion-theoretic facts giving the obstruction are
> recorded as well.

```lean
theorem counterexample_to_etale_lift_without_isUnit_leadingCoeff :
    let I : Ideal ℤ := Ideal.span {(4 : ℤ)}
    let p : Polynomial (ℤ ⧸ I) := 2 * Polynomial.X ^ 2 + 2 * Polynomial.X + 1
    (1 : Polynomial ℤ).Monic ∧
    (1 : Polynomial ℤ).map (Ideal.Quotient.mk I) = p * p ∧
    IsCoprime p p ∧
    ¬ IsUnit p.leadingCoeff ∧
    (∀ (A' : Type v) (_ : CommRing A') (_ : Algebra ℤ A'),
      Algebra.Etale ℤ A' →
      Function.Bijective
        (Ideal.quotientMap
          (I.map (algebraMap ℤ A'))
          (algebraMap ℤ A') Ideal.le_comap_map) →
      Nonempty
        (AdicCompletion (Ideal.span {(algebraMap ℤ A' 2)}) A' ≃+* ℤ_[2])) ∧
    (∀ g' : Polynomial ℤ_[2],
      (∀ n : ℕ,
        g'.coeff n -
            (2 * Polynomial.X ^ 2 + 2 * Polynomial.X + 1 : Polynomial ℤ_[2]).coeff n ∈
          Ideal.span {(4 : ℤ_[2])}) →
      ¬ IsUnit g') ∧
    ¬ ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra ℤ A')
        (g' h' : Polynomial A'),
      Algebra.Etale ℤ A' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap ℤ A')) (algebraMap ℤ A')
          Ideal.le_comap_map) ∧
      (1 : Polynomial ℤ).map (algebraMap ℤ A') = g' * h' ∧
      p.map
          (Ideal.quotientMap (I.map (algebraMap ℤ A')) (algebraMap ℤ A')
            Ideal.le_comap_map) =
        g'.map (Ideal.Quotient.mk (I.map (algebraMap ℤ A'))) ∧
      p.map
          (Ideal.quotientMap (I.map (algebraMap ℤ A')) (algebraMap ℤ A')
            Ideal.le_comap_map) =
        h'.map (Ideal.Quotient.mk (I.map (algebraMap ℤ A')))
```

## Tag 07M3, a lemma

[Tag 07M3](https://stacks.math.columbia.edu/tag/07M3) in the Stacks Project.

**`exists_quotient_eq_one_and_map_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Image.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Image.lean#L285).

> **Stacks Tag 07M3.** If the closure of the image of `V(J)` under `Spec(φ)` is
> disjoint from `V(I)`, then there is `f ∈ R` mapping to `1` in `R/I` with `φ(f) ∈ J`.

```lean
theorem exists_quotient_eq_one_and_map_mem {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (I : Ideal R) (J : Ideal S)
    (h : closure ((PrimeSpectrum.comap φ) '' (PrimeSpectrum.zeroLocus (J : Set S)))
        ∩ PrimeSpectrum.zeroLocus (I : Set R) = ∅) :
    ∃ f : R, (Ideal.Quotient.mk I) f = 1 ∧ φ f ∈ J
```

## Tag 09XG, a lemma

[Tag 09XG](https://stacks.math.columbia.edu/tag/09XG) in the Stacks Project.

**`exists_monic_aeval_eq_zero_map_eq_of_sq_sub_mem_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Idempotents/Lifting.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Idempotents/Lifting.lean#L59).

> Stacks Tag 09XG, Lemma 15.9.9.
>
> If `A → B` is an integral ring map, `I ⊆ A` is an ideal, and `b ∈ B` maps to an
> idempotent in `B / IB` (equivalently, `b ^ 2 - b ∈ IB`), then there exist `d ≥ 1`
> and a monic polynomial `f ∈ A[X]` with `f(b) = 0` and `f mod I = X ^ d * (X - 1) ^ d`
> in `(A / I)[X]`.

```lean
theorem exists_monic_aeval_eq_zero_map_eq_of_sq_sub_mem_map
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] [Algebra.IsIntegral A B]
    (I : Ideal A) (b : B)
    (hb : b ^ 2 - b ∈ Ideal.map (algebraMap A B) I) :
    ∃ d : ℕ, 1 ≤ d ∧ ∃ f : A[X], f.Monic ∧ aeval b f = 0 ∧
      f.map (algebraMap A (A ⧸ I)) =
        (Polynomial.X ^ d * (Polynomial.X - 1) ^ d : (A ⧸ I)[X])
```

## Tag 07M4, a lemma

[Tag 07M4](https://stacks.math.columbia.edu/tag/07M4) in the Stacks Project.

**`exists_etale_baseChange_idempotent_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftIdempotentsAndModules.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftIdempotentsAndModules.lean#L81).

> **Stacks 07M4.** An idempotent of `B ⧸ IB`, for an integral `A`-algebra `B`, lifts to
> `B ⊗[A] A'` after an étale base change `A → A'` which induces an isomorphism modulo `I`.

```lean
theorem exists_etale_baseChange_idempotent_lift
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.IsIntegral A B]
    (I : Ideal A) (e : B ⧸ I.map (algebraMap A B)) (he : IsIdempotentElem e) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A'),
      let T := TensorProduct A B A'
      let ι : B →+* T :=
        Algebra.TensorProduct.includeLeftRingHom (R := A) (A := B) (B := A')
      let J : Ideal T := (I.map (algebraMap A B)).map ι
      let q : (B ⧸ I.map (algebraMap A B)) →+* T ⧸ J :=
        Ideal.quotientMap J ι Ideal.le_comap_map
      ∃ e' : T,
      Algebra.Etale A A' ∧
      Function.Bijective
        (Ideal.quotientMap (I.map (algebraMap A A')) (algebraMap A A')
          Ideal.le_comap_map) ∧
      IsIdempotentElem e' ∧
      q e = Ideal.Quotient.mk J e'
```

## Tag 07M5, a lemma

[Tag 07M5](https://stacks.math.columbia.edu/tag/07M5) in the Stacks Project.

**`exists_etale_baseChange_finite_projective_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftIdempotentsAndModules.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftIdempotentsAndModules.lean#L549).

> **Stacks 07M5.** A finite projective module over `A ⧸ I` lifts after an étale base change
> `A → A'` which induces an isomorphism `A ⧸ I ≃+* A' ⧸ I A'`.

```lean
theorem exists_etale_baseChange_finite_projective_lift
    {A : Type u} [CommRing A] (I : Ideal A)
    (Pbar : Type v) [AddCommGroup Pbar] [Module (A ⧸ I) Pbar]
    [Module.Finite (A ⧸ I) Pbar] [Module.Projective (A ⧸ I) Pbar] :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A'),
      let J := I.map (algebraMap A A')
      let q : (A ⧸ I) →+* (A' ⧸ J) :=
        Ideal.quotientMap J (algebraMap A A') Ideal.le_comap_map
      Algebra.Etale A A' ∧
      ∃ hq : Function.Bijective q,
      ∃ (P' : Type (max u v)) (_ : AddCommGroup P') (_ : Module A' P')
        (_ : Module.Finite A' P') (_ : Module.Projective A' P'),
        Nonempty
          (Pbar ≃ₛₗ[RingHomClass.toRingHom (RingEquiv.ofBijective q hq)]
            TensorProduct A' (A' ⧸ J) P')
```

## Tag 07EV, a lemma

[Tag 07EV](https://stacks.math.columbia.edu/tag/07EV) in the Stacks Project.

**`cotangentComplex_of_isSymmetricAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean#L225). The attribute's comment: “corrected: K ⊗\_A C → J/J² is a canonical surjection, compatible with the maps to ⊕ C dy\_j, and Ω\_\{C/A} = M ⊗\_A C; the isomorphism K ⊗\_A C ≅ J/J² claimed by Stacks fails”.

> **Stacks 07EV, corrected.** Let `0 → K → Aᵐ → M → 0` be exact and let `C` be the symmetric
> algebra on `M`. For the induced polynomial presentation of `C`, there is a canonical surjection
> `C ⊗[A] K → P.Cotangent` compatible with the map into `Cᵐ`, and `Ω[C⁄A]` is canonically
> `C ⊗[A] M`. The last three conditions pin down the canonical maps: polynomial differentials go to
> the standard basis, `1 ⊗ₜ k` goes to the conormal class of its linear relation, and the
> differential of a symmetric-algebra generator goes to `1 ⊗ₜ x`.
>
> Stacks states that `NL(α) = (K ⊗_A C → ⊕ C dy_j)`, i.e. that this surjection is an isomorphism.
> That is false: `not_forall_cotangentEquiv_of_isSymmetricAlgebra` gives `A = ℤ`, `K = ℤ²`,
> `i = 2`, `M = (ℤ/2)²`, where `y₂ ⊗ e₁ - y₁ ⊗ e₂` is a nonzero element of the kernel. What is true in
> general is the statement here: the conormal module is a quotient of `K ⊗_A C` compatibly with the
> maps to `⊕ C dy_j`, so `Ω_{C/A} = M ⊗_A C`. (When `M` is projective, `K → Aᵐ` splits and the map
> is an isomorphism.)

```lean
theorem cotangentComplex_of_isSymmetricAlgebra
    {A : Type uA} {K : Type uK} {M : Type uM} [CommRing A]
    [AddCommGroup K] [Module A K] [AddCommGroup M] [Module A M]
    (m : ℕ) (i : K →ₗ[A] (Fin m → A)) (p : (Fin m → A) →ₗ[A] M)
    (_hi : Function.Injective i) (hip : Function.Exact i p) (hp : Function.Surjective p)
    (C : Type uC) [CommRing C] [Algebra A C]
    (ι : M →ₗ[A] C) (hC : IsSymmetricAlgebra ι)
    (α : MvPolynomial (Fin m) A →ₐ[A] C) (hα : Function.Surjective α)
    (hαX : ∀ j, α (MvPolynomial.X j) = ι (p ((Pi.basisFun A (Fin m)) j))) :
    let P := Algebra.Extension.ofSurjective α hα
    ∃ (eK : C ⊗[A] K →ₗ[C] P.Cotangent)
      (eF : P.CotangentSpace ≃ₗ[C] (Fin m → C))
      (eΩ : KaehlerDifferential A C ≃ₗ[C] C ⊗[A] M),
      Function.Surjective eK ∧
        eF.toLinearMap ∘ₗ P.cotangentComplex ∘ₗ eK =
          (TensorProduct.piScalarRight A C C (Fin m)).toLinearMap ∘ₗ i.baseChange C ∧
        (∀ j, eF (1 ⊗ₜ[P.Ring]
          KaehlerDifferential.D A P.Ring (MvPolynomial.X j)) = Pi.single j 1) ∧
        (∀ k, ∃ hk : (∑ j, MvPolynomial.C (i k j) * MvPolynomial.X j) ∈ P.ker,
          eK (1 ⊗ₜ k) = Algebra.Extension.Cotangent.mk
            ⟨∑ j, MvPolynomial.C (i k j) * MvPolynomial.X j, hk⟩) ∧
        ∀ x, eΩ (KaehlerDifferential.D A C (ι x)) = 1 ⊗ₜ x
```

**`not_forall_cotangentEquiv_of_isSymmetricAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean#L472). The attribute's comment: “counterexample: for A = ℤ, K = ℤ², i = 2, M = (ℤ/2)², the canonical map K ⊗\_A C → J/J² has nonzero kernel, so J/J² is not K ⊗\_A C as claimed”.

> **Stacks 07EV is false as printed.** The lemma asserts that for an exact sequence
> `0 → K → Aᵐ → M → 0` and `C = Sym_A(M)` presented by `α : A[y_1, …, y_m] → C`, the conormal
> module `J/J²` of `α` is `K ⊗_A C`, with `1 ⊗ k` corresponding to the class of the linear relation
> `∑ i(k)_j y_j`. This fails for `A = ℤ`, `K = ℤ²`, `i = 2`, `M = (ℤ/2)²`: the element
> `y₂ ⊗ e₁ - y₁ ⊗ e₂` of `C ⊗ K` is nonzero but goes to the class of `y₂ · 2y₁ - y₁ · 2y₂ = 0`.
> So no `C`-linear isomorphism `C ⊗[A] K ≃ P.Cotangent` sends `1 ⊗ₜ k` to that class. The correct
> statement is `cotangentComplex_of_isSymmetricAlgebra`, where the canonical map is surjective.

```lean
theorem not_forall_cotangentEquiv_of_isSymmetricAlgebra :
    ¬ ∀ (A K M : Type) [CommRing A] [AddCommGroup K] [Module A K] [AddCommGroup M] [Module A M]
      (m : ℕ) (i : K →ₗ[A] (Fin m → A)) (p : (Fin m → A) →ₗ[A] M),
      Function.Injective i → Function.Exact i p → Function.Surjective p →
      ∀ (C : Type) [CommRing C] [Algebra A C] (ι : M →ₗ[A] C), IsSymmetricAlgebra ι →
      ∀ (α : MvPolynomial (Fin m) A →ₐ[A] C) (hα : Function.Surjective α),
      (∀ j, α (MvPolynomial.X j) = ι (p ((Pi.basisFun A (Fin m)) j))) →
      let P := Algebra.Extension.ofSurjective α hα
      ∃ eK : C ⊗[A] K ≃ₗ[C] P.Cotangent,
        ∀ k : K, ∃ hk : (∑ j : Fin m, MvPolynomial.C (σ := Fin m) (i k j) *
            MvPolynomial.X (R := A) j) ∈ P.ker,
          eK (1 ⊗ₜ k) = Algebra.Extension.Cotangent.mk
            ⟨∑ j, MvPolynomial.C (i k j) * MvPolynomial.X j, hk⟩
```

## Tag 07M6, a lemma

[Tag 07M6](https://stacks.math.columbia.edu/tag/07M6) in the Stacks Project.

**`symmetricAlgebra_smooth_iff_finite_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/SymmetricAlgebra.lean#L657). References: EGA 0 (19.3.2), “special case”.

> **Stacks 07M6.** The symmetric algebra of an `A`-module `M` is smooth over `A` if and only if
> `M` is finite projective.

```lean
theorem symmetricAlgebra_smooth_iff_finite_projective
    (A : Type u) [CommRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    Algebra.Smooth A (SymmetricAlgebra A M) ↔
      Module.Finite A M ∧ Module.Projective A M
```

## Tag 07M7, a lemma

[Tag 07M7](https://stacks.math.columbia.edu/tag/07M7) in the Stacks Project.

**`exists_etale_lift_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LiftSmoothMap.lean, line 648](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LiftSmoothMap.lean#L648).

> **Stacks 07M7.** A map from a smooth `A`-algebra `B` to `A ⧸ I` lifts to an étale
> `A`-algebra which induces an isomorphism modulo the extension of `I`.

```lean
theorem exists_etale_lift_of_smooth
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) (f : B →ₐ[A] (A ⧸ I)) [Algebra.Smooth A B] :
    ∃ (A' : Type (max u v)) (_ : CommRing A') (_ : Algebra A A'),
      let J := I.map (algebraMap A A')
      let q : (A ⧸ I) →+* (A' ⧸ J) :=
        Ideal.quotientMap J (algebraMap A A') Ideal.le_comap_map
      Algebra.Etale A A' ∧
      Function.Bijective q ∧
      ∃ f' : B →ₐ[A] A',
        q.comp f.toRingHom = (Ideal.Quotient.mk J).comp f'.toRingHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.9, Tag 07LW](https://stacks.math.columbia.edu/tag/07LW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
