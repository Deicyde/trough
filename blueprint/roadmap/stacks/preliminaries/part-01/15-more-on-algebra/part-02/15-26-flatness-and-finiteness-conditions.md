---
declaration: section
origin: cited
lean: Module.finitePresentation_of_flat_of_localized, Algebra.FinitePresentation.of_flat_of_localized, finitePresentation_of_finite_flat_of_isLocalRing, finitePresentation_of_flat_of_finiteType_of_finite_degreeZero, hasFiniteDetectingPrimes_of_standard_conditions, finitePresentation_of_flat_of_finiteType_of_valuationRing, essentiallyOfFinitePresentation_and_finitePresentation_of_flat_of_valuationRing
statement: formalized
proof: formalized
---

# 15.26 Flatness and finiteness conditions

Section 15.26 of the Stacks Project, [Tag 054A](https://stacks.math.columbia.edu/tag/054A). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 053A, a lemma

[Tag 053A](https://stacks.math.columbia.edu/tag/053A) in the Stacks Project.

**`Module.finitePresentation_of_flat_of_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L299).

> **Stacks Tag 053A.** Let `S = R[x₁, …, x_n]` and let `M` be a finite `S`-module which is flat
> over `R`.  If finitely many prime localizations jointly detect elements of `R` and `M` is
> finitely presented over `S` after localizing at every prime of `R`, then `M` is finitely
> presented over `S`.

```lean
theorem Module.finitePresentation_of_flat_of_localized
    {R : Type u} [CommRing R] {n : ℕ} {M : Type v} [AddCommGroup M]
    [Module (MvPolynomial (Fin n) R) M] [Module R M]
    [IsScalarTower R (MvPolynomial (Fin n) R) M]
    (hprimes : HasFiniteDetectingPrimes R)
    [Module.Finite (MvPolynomial (Fin n) R) M] [Module.Flat R M]
    (hlocal : ∀ p : PrimeSpectrum R,
      Module.FinitePresentation
        (Localization (Algebra.algebraMapSubmonoid (MvPolynomial (Fin n) R)
          p.asIdeal.primeCompl))
        (LocalizedModule (Algebra.algebraMapSubmonoid (MvPolynomial (Fin n) R)
          p.asIdeal.primeCompl) M)) :
    Module.FinitePresentation (MvPolynomial (Fin n) R) M
```

## Tag 053B, a lemma

[Tag 053B](https://stacks.math.columbia.edu/tag/053B) in the Stacks Project.

**`Algebra.FinitePresentation.of_flat_of_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L358).

> **Stacks Tag 053B.** Let `R → S` be a flat ring map of finite type.  Suppose finitely many
> prime localizations jointly detect elements of `R`, and that for every prime `p` of `R` the
> localization of `S` at `p` is finitely presented over `R` localized at `p`.  Then `S` is
> finitely presented over `R`.

```lean
theorem Algebra.FinitePresentation.of_flat_of_localized
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S]
    (hprimes : HasFiniteDetectingPrimes R)
    [Algebra.FiniteType R S] [Module.Flat R S]
    (hlocal : ∀ p : PrimeSpectrum R,
      Algebra.FinitePresentation (Localization.AtPrime p.asIdeal)
        (Localization (Algebra.algebraMapSubmonoid S p.asIdeal.primeCompl))) :
    Algebra.FinitePresentation R S
```

## Tag 053C, a lemma

[Tag 053C](https://stacks.math.columbia.edu/tag/053C) in the Stacks Project.

**`finitePresentation_of_finite_flat_of_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/GradedFinitePresentation.lean, line 1056](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/GradedFinitePresentation.lean#L1056). References: EGA IV (11.2.9.4), “special case”; SGA 6 VI (1.6), “partial”.

> **Stacks Tag 053C.** Let `R` be a local ring and let
> `S = MvPolynomial (Fin n) R = R[x_1, ..., x_n]` be the graded polynomial algebra
> with positive weights `w_i = deg(x_i) > 0`, graded by
> `weightedHomogeneousSubmodule R w`.  Let `M` be a graded `S`-module, encoded by a
> family of `R`-submodules `𝓜 : ℤ → Submodule R M` together with a compatible
> graded scalar multiplication and a direct-sum decomposition.  If `M` is finite as
> an `S`-module and flat as an `R`-module, then `M` is finitely presented as an
> `S`-module.

```lean
theorem finitePresentation_of_finite_flat_of_isLocalRing
    (R : Type*) [CommRing R] [IsLocalRing R]
    (n : ℕ) (w : Fin n → ℤ) (hw : ∀ i, 0 < w i)
    (M : Type*) [AddCommGroup M] [Module (MvPolynomial (Fin n) R) M]
    -- `R` acts on `M` through the structure map `R → S` compatibly
    [Module R M] [IsScalarTower R (MvPolynomial (Fin n) R) M]
    -- the grading on `M` over `ℤ`, as a family of `R`-submodules
    (𝓜 : ℤ → Submodule R M)
    [SetLike.GradedSMul (weightedHomogeneousSubmodule R w) 𝓜]
    [DirectSum.Decomposition 𝓜]
    -- `M` is finite as an `S`-module
    [Module.Finite (MvPolynomial (Fin n) R) M]
    -- `M` is flat as an `R`-module
    [Module.Flat R M] :
    Module.FinitePresentation (MvPolynomial (Fin n) R) M
```

## Tag 053D, a lemma

[Tag 053D](https://stacks.math.columbia.edu/tag/053D) in the Stacks Project.

**`finitePresentation_of_flat_of_finiteType_of_finite_degreeZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 797](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L797). References: EGA IV (11.2.9.4), “Module clause”.

> **Stacks Tag 053D.** Let `S = ⨁_d 𝒜 d` be a nonnegatively graded `R`-algebra of finite type
> whose degree-zero part is finite over `R`, and suppose a finite family of prime localizations
> jointly detects elements of `R`.  Then an `R`-flat `S` is finitely presented as an `R`-algebra,
> and every finite graded `S`-module which is flat over `R` is finitely presented as an
> `S`-module.

```lean
theorem finitePresentation_of_flat_of_finiteType_of_finite_degreeZero
    {R : Type u} {S : Type v} {M : Type w} [CommRing R] [CommRing S]
    [AddCommGroup M] [Algebra R S] [Module S M] [Module R M] [IsScalarTower R S M]
    (𝒜 : ℕ → Submodule R S) [GradedAlgebra 𝒜]
    (ℳ : ℤ → Submodule R M) [SetLike.GradedSMul 𝒜 ℳ] [DirectSum.Decomposition ℳ]
    [Algebra.FiniteType R S] [Module.Finite R (𝒜 0)]
    (hprimes : HasFiniteDetectingPrimes R) :
    (Module.Flat R S → Algebra.FinitePresentation R S) ∧
      (Module.Flat R M → Module.Finite S M → Module.FinitePresentation S M)
```

## Tag 05GS, a remark

[Tag 05GS](https://stacks.math.columbia.edu/tag/05GS) in the Stacks Project.

**`hasFiniteDetectingPrimes_of_standard_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 1297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L1297).

> **Stacks Tag 05GS.** Let `R` be a commutative ring.  If `R` is local, Noetherian, a domain,
> reduced with finitely many minimal primes, or has finitely many weakly associated primes, then
> finitely many prime localizations jointly detect elements of `R`, so that Tags 053A, 053B and
> 053D apply to `R`.

```lean
theorem hasFiniteDetectingPrimes_of_standard_conditions
    {R : Type u} [CommRing R]
    (h : IsLocalRing R ∨ IsNoetherianRing R ∨ IsDomain R ∨
      (IsReduced R ∧ (minimalPrimes R).Finite) ∨
      {p : Ideal R | ∃ x : R, p ∈ (R ∙ x).annihilator.minimalPrimes}.Finite) :
    HasFiniteDetectingPrimes R
```

## Tag 053E, a lemma

[Tag 053E](https://stacks.math.columbia.edu/tag/053E) in the Stacks Project.

**`finitePresentation_of_flat_of_finiteType_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 1174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L1174).

> **Stacks Tag 053E (Nagata).** Let `A` be a valuation ring, `B` an `A`-algebra of finite type,
> and `M` a `B`-module.  If `B` is flat over `A`, then `B` is finitely presented as an
> `A`-algebra.  If `M` is finite over `B` and flat over `A`, then `M` is finitely presented as a
> `B`-module.

```lean
theorem finitePresentation_of_flat_of_finiteType_of_valuationRing
    {A : Type u} {B : Type v} {M : Type w} [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B] [AddCommGroup M] [Module B M]
    [Module A M] [IsScalarTower A B M] :
    (Module.Flat A B → Algebra.FinitePresentation A B) ∧
      (Module.Flat A M → Module.Finite B M → Module.FinitePresentation B M)
```

## Tag 0GSE, a lemma

[Tag 0GSE](https://stacks.math.columbia.edu/tag/0GSE) in the Stacks Project.

**`essentiallyOfFinitePresentation_and_finitePresentation_of_flat_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Finiteness.lean, line 1229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Finiteness.lean#L1229).

> **Stacks Tag 0GSE.** Let `A` be a valuation ring, `B` an essentially-of-finite-type
> `A`-algebra, and `M` a `B`-module.  If `B` is flat over `A`, then `A → B` is essentially of
> finite presentation.  If `M` is finite over `B` and flat over `A`, then `M` is finitely presented
> over `B`.

```lean
theorem essentiallyOfFinitePresentation_and_finitePresentation_of_flat_of_valuationRing
    {A : Type u} {B : Type v} {M : Type w} [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [Algebra A B] [Algebra.EssFiniteType A B] [AddCommGroup M] [Module B M]
    [Module A M] [IsScalarTower A B M] :
    (Module.Flat A B → (algebraMap A B).EssentiallyOfFinitePresentation) ∧
      (Module.Flat A M → Module.Finite B M → Module.FinitePresentation B M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.26, Tag 054A](https://stacks.math.columbia.edu/tag/054A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
