---
declaration: section
origin: cited
lean: IsUnibranch, IsGeometricallyUnibranch, bijective_maximalIdeals_and_minimalPrimes_of_henselization, isUnibranch_iff_henselization_has_unique_minimalPrime, geometric_branches_of_strictHenselization, isGeometricallyUnibranch_iff_strictHenselization_has_unique_minimalPrime, numberOfBranches, numberOfGeometricBranches
statement: formalized
proof: formalized
---

# 15.108 Local irreducibility

Section 15.108 of the Stacks Project, [Tag 06DT](https://stacks.math.columbia.edu/tag/06DT). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BPZ, a definition

[Tag 0BPZ](https://stacks.math.columbia.edu/tag/0BPZ) in the Stacks Project.

**`IsUnibranch`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Defs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Defs.lean#L62). The attribute's comment: “(1)”. References: EGA 0 (23.2.1), “def. of unibranch”; EGA III (4.3.6), “unibranch local ring”.

> A local ring is unibranch if its reduction is a domain and the integral closure of its
> reduction in its field of fractions is local.

```lean
def IsUnibranch (A : Type u) [CommRing A] [IsLocalRing A] : Prop
```

**`IsGeometricallyUnibranch`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Defs.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Defs.lean#L70). The attribute's comment: “(2)”. References: EGA 0 (23.2.1), “def. of geom. unibranch”.

> A local ring is geometrically unibranch if it is unibranch and the residue field of the
> normalization of its reduction is purely inseparable over its residue field.

```lean
noncomputable def IsGeometricallyUnibranch
    (A : Type u) [CommRing A] [IsLocalRing A] : Prop
```

## Tag 0C24, a lemma

[Tag 0C24](https://stacks.math.columbia.edu/tag/0C24) in the Stacks Project.

**`bijective_maximalIdeals_and_minimalPrimes_of_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Henselization/BranchCorrespondence.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Henselization/BranchCorrespondence.lean#L598).

> Let `A'` be the integral closure of a local ring `A` in the total ring of fractions of its
> reduction, and let `Aʰ` be a henselization of `A`. Contraction from `A' ⊗[A] Aʰ` is bijective
> on maximal ideals toward `A'` and on minimal primes toward `Aʰ`. Each minimal prime of the tensor
> product lies in a unique maximal ideal, and each maximal ideal contains a unique minimal prime.

```lean
theorem bijective_maximalIdeals_and_minimalPrimes_of_henselization
    (A : Type u) (Ah : Type v) [CommRing A] [IsLocalRing A] [CommRing Ah] [IsLocalRing Ah]
    [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    (hmin : (minimalPrimes A).Finite) :
    let A' := integralClosure A (FractionRing (A ⧸ nilradical A))
    let T := TensorProduct A A' Ah
    Set.BijOn
        (Ideal.comap (Algebra.TensorProduct.includeLeftRingHom : A' →+* T))
        {I : Ideal T | I.IsMaximal} {I : Ideal A' | I.IsMaximal} ∧
      Set.BijOn
        (Ideal.comap
          (Algebra.TensorProduct.includeRight : Ah →ₐ[A] T).toRingHom)
        (minimalPrimes T) (minimalPrimes Ah) ∧
      (∀ q ∈ minimalPrimes T, ∃! m : Ideal T, m.IsMaximal ∧ q ≤ m) ∧
      (∀ m : Ideal T, m.IsMaximal → ∃! q : Ideal T, q ∈ minimalPrimes T ∧ q ≤ m)
```

## Tag 0BQ0, a lemma

[Tag 0BQ0](https://stacks.math.columbia.edu/tag/0BQ0) in the Stacks Project.

**`isUnibranch_iff_henselization_has_unique_minimalPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Henselization/Unibranch.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Henselization/Unibranch.lean#L132). References: EGA IV (18.6.12), “a) ⇔ c), irreducible”.

> A local ring is unibranch if and only if a henselization of it has a unique minimal prime.

```lean
theorem isUnibranch_iff_henselization_has_unique_minimalPrime
    (A Ah : Type u) [CommRing A] [IsLocalRing A] [CommRing Ah] [IsLocalRing Ah]
    [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah] :
    IsUnibranch A ↔ ∃! p : Ideal Ah, p ∈ minimalPrimes Ah
```

## Tag 0C25, a lemma

[Tag 0C25](https://stacks.math.columbia.edu/tag/0C25) in the Stacks Project.

**`geometric_branches_of_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Henselization/BranchCorrespondence.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Henselization/BranchCorrespondence.lean#L538).

> Let `A'` be the integral closure of a local ring `A` in the total ring of fractions of its
> reduction, and let `Aˢʰ` be a strict henselization with separably closed residue field `ksep`
> inside an algebraic closure `kbar`. The residue extension at every maximal ideal of `A'` is
> algebraic, and its embeddings into `kbar` canonically parametrize the fibre in
> `Spec (A' ⊗[A] Aˢʰ)`. Contraction to `Aˢʰ` is bijective on minimal primes, and containment gives
> mutually unique correspondences between minimal and maximal primes of the tensor product.

```lean
theorem geometric_branches_of_strictHenselization
    (A : Type u) (Ash : Type u') (ksep : Type v) (kbar : Type w)
    [CommRing A] [IsLocalRing A] [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [IsLocalRing.IsHenselization A ksep Ash]
    [Field kbar] [Algebra (IsLocalRing.ResidueField A) kbar]
    [IsAlgClosure (IsLocalRing.ResidueField A) kbar]
    [Algebra ksep kbar] [IsScalarTower (IsLocalRing.ResidueField A) ksep kbar]
    (e : ksep ≃+* IsLocalRing.ResidueField Ash)
    (he : ∀ x : A,
      e (algebraMap (IsLocalRing.ResidueField A) ksep (IsLocalRing.residue A x)) =
        IsLocalRing.residue Ash (algebraMap A Ash x))
    (hmin : (minimalPrimes A).Finite) :
    let A' := integralClosure A (FractionRing (A ⧸ nilradical A))
    let T := TensorProduct A A' Ash
    (∀ m' : MaximalSpectrum A',
      ∃ h : IsLocalRing.maximalIdeal A = m'.asIdeal.comap (algebraMap A A'),
        let f := Ideal.quotientMap m'.asIdeal (algebraMap A A') (le_of_eq h)
        f.IsIntegral ∧
          ∃ E : ({σ : (A' ⧸ m'.asIdeal) →+* kbar //
                    σ.comp f = algebraMap (IsLocalRing.ResidueField A) kbar} ≃
                  {q : PrimeSpectrum T //
                    PrimeSpectrum.comap
                      (Algebra.TensorProduct.includeLeftRingHom : A' →+* T) q =
                        m'.toPrimeSpectrum}),
            ∀ σ, ∃ φ : T →+* kbar,
              (∀ (a : A') (b : Ash),
                  φ (a ⊗ₜ[A] b) =
                    σ.1 (Ideal.Quotient.mk m'.asIdeal a) *
                      algebraMap ksep kbar (e.symm (IsLocalRing.residue Ash b))) ∧
                (E σ).1.asIdeal = RingHom.ker φ ∧
                ∀ ψ : T →+* kbar,
                  (∀ (a : A') (b : Ash),
                    ψ (a ⊗ₜ[A] b) =
                      σ.1 (Ideal.Quotient.mk m'.asIdeal a) *
                        algebraMap ksep kbar (e.symm (IsLocalRing.residue Ash b))) →
                  ψ = φ) ∧
      Set.BijOn
        (Ideal.comap
          (Algebra.TensorProduct.includeRight : Ash →ₐ[A] T).toRingHom)
        (minimalPrimes T) (minimalPrimes Ash) ∧
      (∀ q ∈ minimalPrimes T, ∃! m : Ideal T, m.IsMaximal ∧ q ≤ m) ∧
      (∀ m : Ideal T, m.IsMaximal → ∃! q : Ideal T, q ∈ minimalPrimes T ∧ q ≤ m)
```

## Tag 06DM, a lemma

[Tag 06DM](https://stacks.math.columbia.edu/tag/06DM) in the Stacks Project.

**`isGeometricallyUnibranch_iff_strictHenselization_has_unique_minimalPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Henselization/Unibranch.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Henselization/Unibranch.lean#L425). References: EGA IV (18.8.15), “a) ⇔ c), irreducible”.

> A local ring is geometrically unibranch if and only if a strict henselization of it has a
> unique minimal prime.

```lean
theorem isGeometricallyUnibranch_iff_strictHenselization_has_unique_minimalPrime
    (A Ash : Type u) [CommRing A] [IsLocalRing A] [CommRing Ash] [IsLocalRing Ash]
    [Algebra A Ash]
    (ksep : Type v) [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [IsLocalRing.IsHenselization A ksep Ash] :
    IsGeometricallyUnibranch A ↔
      ∃! p : Ideal Ash, p ∈ minimalPrimes Ash
```

## Tag 0C26, a definition

[Tag 0C26](https://stacks.math.columbia.edu/tag/0C26) in the Stacks Project.

**`numberOfBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Defs.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Defs.lean#L96). The attribute's comment: “number of branches”.

> The number of branches of a local ring is the extended-natural cardinality of the set of
> minimal primes of a henselization.

```lean
noncomputable def numberOfBranches (A Ah : Type u) [CommRing A] [IsLocalRing A]
    [CommRing Ah]
    [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah] : ℕ∞
```

**`numberOfGeometricBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Defs.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Defs.lean#L105). The attribute's comment: “number of geometric branches”.

> The number of geometric branches of a local ring is the extended-natural cardinality of the
> set of minimal primes of a strict henselization.

```lean
noncomputable def numberOfGeometricBranches (A : Type u) (ksep : Type v) (Ash : Type u)
    [CommRing A] [IsLocalRing A] [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep] [CommRing Ash] [IsLocalRing Ash]
    [Algebra A Ash] [IsLocalRing.IsHenselization A ksep Ash] : ℕ∞
```

## Tag 0C37, a lemma

[Tag 0C37](https://stacks.math.columbia.edu/tag/0C37) in the Stacks Project.

**`numberOfBranches_characterizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Henselization/BranchNumbers.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Henselization/BranchNumbers.lean#L204).

> The numbers of branches and geometric branches of a local ring are infinite if the ring has
> infinitely many minimal primes, and they equal one exactly for unibranch and geometrically
> unibranch rings, respectively. If the ring has finitely many minimal primes, its branches are
> the maximal ideals of the normalization of its reduction, with geometric branches weighted by
> the separable degrees of the corresponding residue-field extensions.

```lean
theorem numberOfBranches_characterizations
    (A Ah Ash : Type u) (ksep : Type v)
    [CommRing A] [IsLocalRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [IsLocalRing.IsHenselization A ksep Ash] :
    ((minimalPrimes A).Infinite →
        numberOfBranches A Ah = ⊤ ∧
          numberOfGeometricBranches A ksep Ash = ⊤) ∧
      (numberOfBranches A Ah = 1 ↔ IsUnibranch A) ∧
      (numberOfGeometricBranches A ksep Ash = 1 ↔
        IsGeometricallyUnibranch A) ∧
      ((minimalPrimes A).Finite →
        let A' := integralClosure A (FractionRing (A ⧸ nilradical A))
        numberOfBranches A Ah =
            Set.encard {m' : Ideal A' | m'.IsMaximal} ∧
          ∃ hcontract : ∀ m' : MaximalSpectrum A',
              IsLocalRing.maximalIdeal A = m'.asIdeal.comap (algebraMap A A'),
            numberOfGeometricBranches A ksep Ash =
              ENat.card (Σ m' : MaximalSpectrum A',
                letI : Field (A' ⧸ m'.asIdeal) := Ideal.Quotient.field m'.asIdeal
                let f := Ideal.quotientMap m'.asIdeal (algebraMap A A')
                  (le_of_eq (hcontract m'))
                letI : Algebra (IsLocalRing.ResidueField A) (A' ⧸ m'.asIdeal) := f.toAlgebra
                (Field.sepDegree (IsLocalRing.ResidueField A)
                  (A' ⧸ m'.asIdeal)).ord.ToType))
```

## Tag 0DQ1, a lemma

[Tag 0DQ1](https://stacks.math.columbia.edu/tag/0DQ1) in the Stacks Project.

**`numberOfBranches_eq_of_isLocalization_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Miscellaneous/SmoothInvariance.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Miscellaneous/SmoothInvariance.lean#L402).

> A local homomorphism of local rings which is a localization of a smooth ring map preserves
> the number of geometric branches. If its residue-field extension is purely inseparable, it also
> preserves the number of branches.
>
> The source's two rings carry independent universes, together with their henselizations and
> strict henselizations: `A`, `Aʰ`, `Aˢʰ` in one and `B`, `Bʰ`, `Bˢʰ` in the other, and the two
> separable closures in two more. The universe work is done by
> `StacksDraft.henselization_tensorProduct_at_unique_prime` and
> `StacksDraft.strictHenselization_tensorProduct_at_induced_prime`, the source-strength forms of
> tags 08HU and 08HV, and by the ind-étale layer they are built on, which lets the branch-counting
> lemmas above be stated with the base and its henselization in independent universes.

```lean
theorem numberOfBranches_eq_of_isLocalization_smooth
    (A Ah Ash : Type uA) (B Bh Bsh : Type uB) (kAsep : Type vA) (kBsep : Type vB)
    [CommRing A] [IsLocalRing A] [CommRing B] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)]
    (hsm : ∃ (C : Type uC) (_ : CommRing C) (_ : Algebra A C) (_ : Algebra C B)
      (_ : IsScalarTower A C B) (S : Submonoid C),
        Algebra.Smooth A C ∧ IsLocalization S B)
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh]
    [IsLocalRing.IsHenselization B (IsLocalRing.ResidueField B) Bh]
    [Field kAsep] [Algebra (IsLocalRing.ResidueField A) kAsep]
    [IsSepClosure (IsLocalRing.ResidueField A) kAsep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [IsLocalRing.IsHenselization A kAsep Ash]
    [Field kBsep] [Algebra (IsLocalRing.ResidueField B) kBsep]
    [IsSepClosure (IsLocalRing.ResidueField B) kBsep]
    [CommRing Bsh] [IsLocalRing Bsh] [Algebra B Bsh]
    [IsLocalRing.IsHenselization B kBsep Bsh] :
    numberOfGeometricBranches A kAsep Ash = numberOfGeometricBranches B kBsep Bsh ∧
      ((IsLocalRing.ResidueField.map (algebraMap A B)).IsPurelyInseparable →
        numberOfBranches A Ah = numberOfBranches B Bh)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.108, Tag 06DT](https://stacks.math.columbia.edu/tag/06DT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
