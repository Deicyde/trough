---
declaration: section
origin: cited
lean: mapsTo_surjOn_minimalPrimes_and_numberOfBranches_le_completion, numberOfBranches_eq_completion_iff_radical_map_minimalPrime_isPrime, exists_surjective_bijective_away_prod, exists_finiteType_algEquiv_adicCompletion_of_cotangent_annihilated, exists_minimalPrime_henselization_radical_map_eq_of_quotient_dimension_one, not_isConnected_puncturedSpectrum_adicCompletion_iff_henselization, numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion_of_dimension_one, isNagataRing_and_numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion
statement: formalized
proof: formalized
---

# 15.110 Branches of the completion

Section 15.110 of the Stacks Project, [Tag 0C27](https://stacks.math.columbia.edu/tag/0C27). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C28, a lemma

[Tag 0C28](https://stacks.math.columbia.edu/tag/0C28) in the Stacks Project.

**`mapsTo_surjOn_minimalPrimes_and_numberOfBranches_le_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean#L572). The attribute's comment: “parts (1)-(3): contraction along Aʰ → Â maps Min(Â) into and onto Min(Aʰ); branch counts of Â use Â as its own henselization and Â ⊗[Aʰ] Aˢʰ as its strict henselization”.

> For a Noetherian local ring `A` with henselization `Aʰ` and strict henselization `Aˢʰ`, there
> is a map `f : Aʰ → Â` over `A` such that:
> 1. contraction along `f` carries minimal primes of `Â` to minimal primes of `Aʰ`, and every
>    minimal prime of `Aʰ` arises this way;
> 2. the number of branches of `A` is at most that of `Â` (which is henselian, so is its own
>    henselization);
> 3. `Â ⊗[Aʰ] Aˢʰ` is a strict henselization of `Â`, and the number of geometric branches of `A` is
>    at most that of `Â`.

```lean
theorem mapsTo_surjOn_minimalPrimes_and_numberOfBranches_le_completion
    (A Ah Ash : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    (κsep : Type v) [Field κsep] [Algebra (ResidueField A) κsep]
    [IsSepClosure (ResidueField A) κsep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash] [Algebra Ah Ash]
    [IsScalarTower A Ah Ash] [IsHenselization A κsep Ash]
    [IsLocalHom (algebraMap Ah Ash)] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    ∃ hAhatLocal : IsLocalRing Ahat,
      letI : IsLocalRing Ahat := hAhatLocal
      ∃ hAhatMapLocal : IsLocalHom (algebraMap A Ahat),
        letI : IsLocalHom (algebraMap A Ahat) := hAhatMapLocal
        ∃ f : Ah →+* Ahat,
          (∀ x : A, f (algebraMap A Ah x) = algebraMap A Ahat x) ∧
          Set.MapsTo (fun q => Ideal.comap f q) (minimalPrimes Ahat) (minimalPrimes Ah) ∧
          Set.SurjOn (fun q => Ideal.comap f q) (minimalPrimes Ahat) (minimalPrimes Ah) ∧
          letI : Algebra Ah Ahat := f.toAlgebra
          ∃ hAhatHenselization : IsHenselization Ahat (ResidueField Ahat) Ahat,
            letI : IsHenselization Ahat (ResidueField Ahat) Ahat := hAhatHenselization
            numberOfBranches A Ah ≤ numberOfBranches Ahat Ahat ∧
            ∃ algKhat : Algebra (ResidueField Ahat) κsep,
              letI : Algebra (ResidueField Ahat) κsep := algKhat
              (∀ x : ResidueField A,
                algebraMap (ResidueField Ahat) κsep
                    (ResidueField.map (algebraMap A Ahat) x) =
                  algebraMap (ResidueField A) κsep x) ∧
              ∃ hKsep : IsSepClosure (ResidueField Ahat) κsep,
                letI : IsSepClosure (ResidueField Ahat) κsep := hKsep
                ∃ hTensorLocal : IsLocalRing (Ahat ⊗[Ah] Ash),
                  letI : IsLocalRing (Ahat ⊗[Ah] Ash) := hTensorLocal
                  ∃ hTensorHenselization : IsHenselization Ahat κsep (Ahat ⊗[Ah] Ash),
                    letI : IsHenselization Ahat κsep (Ahat ⊗[Ah] Ash) := hTensorHenselization
                    numberOfGeometricBranches A κsep Ash ≤
                      numberOfGeometricBranches Ahat κsep (Ahat ⊗[Ah] Ash)
```

## Tag 0C29, a lemma

[Tag 0C29](https://stacks.math.columbia.edu/tag/0C29) in the Stacks Project.

**`numberOfBranches_eq_completion_iff_radical_map_minimalPrime_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean#L289).

> A Noetherian local ring and its completion have the same number of branches if and only if
> the radical of the extension of every minimal prime of a henselization to the completion is
> prime.

```lean
theorem numberOfBranches_eq_completion_iff_radical_map_minimalPrime_isPrime
    (A Ah : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    ∃ hAhatLocal : IsLocalRing Ahat,
      letI : IsLocalRing Ahat := hAhatLocal
      ∃ hAhatMapLocal : IsLocalHom (algebraMap A Ahat),
        letI : IsLocalHom (algebraMap A Ahat) := hAhatMapLocal
        ∃ f : Ah →+* Ahat,
          (∀ x : A, f (algebraMap A Ah x) = algebraMap A Ahat x) ∧
          ∃ hAhatHenselization : IsHenselization Ahat (ResidueField Ahat) Ahat,
            letI : IsHenselization Ahat (ResidueField Ahat) Ahat := hAhatHenselization
            (numberOfBranches A Ah =
                numberOfBranches Ahat Ahat ↔
              ∀ q ∈ minimalPrimes Ah, (Ideal.map f q).radical.IsPrime)
```

## Tag 0C2A, a lemma

[Tag 0C2A](https://stacks.math.columbia.edu/tag/0C2A) in the Stacks Project.

**`exists_surjective_bijective_away_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Idempotent.lean, line 844](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/Idempotent.lean#L844).

> **Stacks Tag 0C2A, Lemma 15.110.3.**
> Let `A` be a ring, `I ⊆ A` a finitely generated ideal, and `A → C` a ring map such that
> for every `f ∈ I` the induced map `A_f → C_f` is localization at an idempotent. Then there
> is a surjective ring map `A → C'` such that for every `f ∈ I` the canonical ring map
> `A_f → (C × C')_f` is an isomorphism (here expressed as a bijective ring homomorphism).
>
> Note: `C'` is constructed as a quotient of `A`, so it lives in the universe `u` of `A`.

```lean
theorem exists_surjective_bijective_away_prod {A : Type u} {C : Type v} [CommRing A] [CommRing C]
  [Algebra A C]
    (I : Ideal A) (hI : I.FG)
    (h : ∀ f ∈ I, IsLocalizationAtIdempotent
      (IsLocalization.Away.map (Localization.Away f)
        (Localization.Away (algebraMap A C f)) (algebraMap A C) f)) :
    ∃ (C' : Type u) (_ : CommRing C') (_ : Algebra A C'),
      Function.Surjective (algebraMap A C') ∧
      ∀ f ∈ I, Function.Bijective
        (IsLocalization.Away.map (Localization.Away f)
          (Localization.Away (algebraMap A (C × C') f)) (algebraMap A (C × C')) f)
```

## Tag 0ALR, a lemma

[Tag 0ALR](https://stacks.math.columbia.edu/tag/0ALR) in the Stacks Project.

**`exists_finiteType_algEquiv_adicCompletion_of_cotangent_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Algebraization.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Algebraization.lean#L521).

> **Stacks Tag 0ALR.** A quotient of the adic completion of a finite-type algebra is itself
> the adic completion of a finite-type algebra if its conormal module is annihilated by a power of
> the defining ideal.

```lean
theorem exists_finiteType_algEquiv_adicCompletion_of_cotangent_annihilated
    (A : Type u) (B : Type v) (C : Type w) [CommRing A] [IsNoetherianRing A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    [CommRing C] [Algebra A C] (I : Ideal A)
    (φ : AdicCompletion (I.map (algebraMap A B)) B →ₐ[A] C)
    (hφ : Function.Surjective φ) (c : ℕ)
    (hJ : I ^ c • (⊤ : Submodule A (RingHom.ker φ.toRingHom).Cotangent) = ⊥) :
    ∃ (D : Type (max u v w)) (_ : CommRing D) (_ : Algebra A D),
      Algebra.FiniteType A D ∧
        Nonempty (C ≃ₐ[A] AdicCompletion (I.map (algebraMap A D)) D)
```

## Tag 0C2B, a lemma

[Tag 0C2B](https://stacks.math.columbia.edu/tag/0C2B) in the Stacks Project.

**`exists_minimalPrime_henselization_radical_map_eq_of_quotient_dimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/HenselizationToCompletion.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/HenselizationToCompletion.lean#L716).

> A minimal prime defining a one-dimensional component of the completion of a Noetherian local
> ring is the radical of the extension of a minimal prime of its henselization.

```lean
theorem exists_minimalPrime_henselization_radical_map_eq_of_quotient_dimension_one
    (A : Type u) (Ah : Type v)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    ∃ f : Ah →+* Ahat,
      (∀ x : A, f (algebraMap A Ah x) = algebraMap A Ahat x) ∧
        ∀ q : Ideal Ahat, q ∈ minimalPrimes Ahat →
          ringKrullDim (Ahat ⧸ q) = 1 →
            ∃ qh : Ideal Ah, qh ∈ minimalPrimes Ah ∧ q = (Ideal.map f qh).radical
```

## Tag 0C2C, a lemma

[Tag 0C2C](https://stacks.math.columbia.edu/tag/0C2C) in the Stacks Project.

**`not_isConnected_puncturedSpectrum_adicCompletion_iff_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/PuncturedSpectrum.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/PuncturedSpectrum.lean#L122).

> The punctured spectrum of the completion of a Noetherian local ring is disconnected if and
> only if the punctured spectrum of its henselization is disconnected.

```lean
theorem not_isConnected_puncturedSpectrum_adicCompletion_iff_henselization
    (A : Type u) (Ah : Type v)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    (¬ _root_.IsConnected {p : PrimeSpectrum Ahat | p.asIdeal ≠ maximalIdeal Ahat}) ↔
      ¬ _root_.IsConnected {p : PrimeSpectrum Ah | p.asIdeal ≠ maximalIdeal Ah}
```

## Tag 0C2D, a lemma

[Tag 0C2D](https://stacks.math.columbia.edu/tag/0C2D) in the Stacks Project.

**`numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion_of_dimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean, line 735](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/BranchCounts.lean#L735).

> Completion preserves the ordinary and the geometric number of branches of a one-dimensional
> Noetherian local ring.

```lean
theorem numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion_of_dimension_one
    (A Ah AhatH Ash AhatSh : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    [CommRing AhatH] [IsLocalRing AhatH]
    [Algebra (AdicCompletion (maximalIdeal A) A) AhatH]
    [IsHenselization (AdicCompletion (maximalIdeal A) A)
      (ResidueField (AdicCompletion (maximalIdeal A) A)) AhatH]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField A) ksep]
    [IsSepClosure (ResidueField A) ksep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash] [IsHenselization A ksep Ash]
    (khatsep : Type w) [Field khatsep]
    [Algebra (ResidueField (AdicCompletion (maximalIdeal A) A)) khatsep]
    [IsSepClosure (ResidueField (AdicCompletion (maximalIdeal A) A)) khatsep]
    [CommRing AhatSh] [IsLocalRing AhatSh]
    [Algebra (AdicCompletion (maximalIdeal A) A) AhatSh]
    [IsHenselization (AdicCompletion (maximalIdeal A) A) khatsep AhatSh]
    (hdim : ringKrullDim A = 1) :
    numberOfBranches A Ah =
        numberOfBranches (AdicCompletion (maximalIdeal A) A) AhatH ∧
      numberOfGeometricBranches A ksep Ash =
        numberOfGeometricBranches
          (AdicCompletion (maximalIdeal A) A) khatsep AhatSh
```

## Tag 0C2E, a lemma

[Tag 0C2E](https://stacks.math.columbia.edu/tag/0C2E) in the Stacks Project.

**`isNagataRing_and_numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Completion/GeometricallyNormalFormalFibres.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Branches/Completion/GeometricallyNormalFormalFibres.lean#L444). References: EGA IV (7.6.1), “A' finite over A”; EGA IV (7.8.3), “(vi) local case”.

> A Noetherian local ring whose formal fibres are geometrically normal is Nagata, and its
> ordinary and geometric branch counts agree with those of its completion.

```lean
theorem isNagataRing_and_numberOfBranches_and_numberOfGeometricBranches_eq_adicCompletion
    (A Ah AhatH Ash AhatSh : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    [CommRing AhatH] [IsLocalRing AhatH]
    [Algebra (AdicCompletion (maximalIdeal A) A) AhatH]
    [IsHenselization (AdicCompletion (maximalIdeal A) A)
      (ResidueField (AdicCompletion (maximalIdeal A) A)) AhatH]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField A) ksep]
    [IsSepClosure (ResidueField A) ksep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash] [IsHenselization A ksep Ash]
    (khatsep : Type w) [Field khatsep]
    [Algebra (ResidueField (AdicCompletion (maximalIdeal A) A)) khatsep]
    [IsSepClosure (ResidueField (AdicCompletion (maximalIdeal A) A)) khatsep]
    [CommRing AhatSh] [IsLocalRing AhatSh]
    [Algebra (AdicCompletion (maximalIdeal A) A) AhatSh]
    [IsHenselization (AdicCompletion (maximalIdeal A) A) khatsep AhatSh]
    (hformal : ∀ q : PrimeSpectrum A,
      Algebra.IsGeometricallyNormal q.asIdeal.ResidueField
        (q.asIdeal.Fiber (AdicCompletion (maximalIdeal A) A))) :
    IsNagataRing A ∧
      numberOfBranches A Ah =
        numberOfBranches (AdicCompletion (maximalIdeal A) A) AhatH ∧
      numberOfGeometricBranches A ksep Ash =
        numberOfGeometricBranches
          (AdicCompletion (maximalIdeal A) A) khatsep AhatSh
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.110, Tag 0C27](https://stacks.math.columbia.edu/tag/0C27)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
