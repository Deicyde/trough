---
declaration: section
origin: cited
lean: GenericFinitePresentation.generic_finite_presentation, image_constructible_contains_open_dense_in_closure, main_equivalence, domain_image_dense_set_points_generic_point_tfae, Ideal.exists_minimalPrimes_comap_eq, contraction_ne_bot_of_algebraic, PrimeSpectrum.not_dense_image_comap_of_isAlgebraic
statement: formalized
proof: formalized
---

# 10.30 More on images

Section 10.30 of the Stacks Project, [Tag 00FF](https://stacks.math.columbia.edu/tag/00FF). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00FG, a lemma

[Tag 00FG](https://stacks.math.columbia.edu/tag/00FG) in the Stacks Project.

**`GenericFinitePresentation.generic_finite_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/AwayMapMul.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/AwayMapMul.lean#L662).

> **Generic finite presentation.** An inclusion of domains of finite type admits nonzero
> `f ∈ R` and `g ∈ S` such that `R[1/f] → S[1/(fg)]` is of finite presentation.
> The domain hypothesis on `R` follows from injectivity.

```lean
theorem GenericFinitePresentation.generic_finite_presentation
    {R S : Type*} [CommRing R] [CommRing S] [IsDomain S] [Algebra R S]
    [Algebra.FiniteType R S] (hinj : Function.Injective (algebraMap R S)) :
    ∃ (f : R) (g : S), f ≠ 0 ∧ g ≠ 0 ∧ (awayMapMul f g).FinitePresentation
```

## Tag 00FH, a lemma

[Tag 00FH](https://stacks.math.columbia.edu/tag/00FH) in the Stacks Project.

**`image_constructible_contains_open_dense_in_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/ConstructibleImage.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/ConstructibleImage.lean#L650).

> **Stacks 00FH (Lemma 10.30.2).**  Let `φ : R →+* S` be a ring map of finite type, let
> `E ⊆ Spec S` be constructible, and let `ξ ∈ Spec R` lie in the image `f(E)` of `E` under
> `f = PrimeSpectrum.comap φ`.  Then `closure {ξ} ∩ f(E)` contains a subset `D` that is open and
> dense in the subspace `closure {ξ}`.

```lean
theorem image_constructible_contains_open_dense_in_closure
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (hφ : φ.FiniteType)
    (E : Set (PrimeSpectrum S)) (hE : Topology.IsConstructible E)
    (ξ : PrimeSpectrum R)
    (hξ : ξ ∈ PrimeSpectrum.comap φ '' E) :
    ∃ D : Set (closure {ξ} : Set (PrimeSpectrum R)),
      IsOpen D ∧ Dense D ∧
      (Subtype.val '' D) ⊆ closure {ξ} ∩ (PrimeSpectrum.comap φ '' E)
```

## Tag 00FI, a lemma

[Tag 00FI](https://stacks.math.columbia.edu/tag/00FI) in the Stacks Project.

**`main_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean#L112).

> Main equivalence: conditions (1), (2), (3), (4) are equivalent.

```lean
theorem main_equivalence
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S) :
    (SpecSurjective φ ↔ RadicalContractionEq φ) ∧
    (RadicalContractionEq φ ↔ RadicalIdealContractionEq φ) ∧
    (RadicalIdealContractionEq φ ↔ PrimeContractionEq φ) ∧
    (PrimeContractionEq φ ↔ SpecSurjective φ)
```

## Tag 00FJ, a lemma

[Tag 00FJ](https://stacks.math.columbia.edu/tag/00FJ) in the Stacks Project.

**`domain_image_dense_set_points_generic_point_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean#L306). References: EGA 0 (2.1.5), “special case”; EGA I (1.2.7), “special case”.

> Let `R` be a domain and `φ : R →+* S` a ring map. Then the following are equivalent:
> 1. `φ` is injective.
> 2. The range of the induced map `PrimeSpectrum.comap φ` is dense in `PrimeSpectrum R`.
> 3. There exists a prime `q` of `S` whose preimage under `φ` is the zero ideal of `R`.

```lean
theorem domain_image_dense_set_points_generic_point_tfae :
    List.TFAE
      [ Function.Injective φ
      , Dense (Set.range (PrimeSpectrum.comap φ))
      , ∃ q : PrimeSpectrum S, (PrimeSpectrum.comap φ q).asIdeal = ⊥ ]
```

## Tag 0CAN, a lemma

[Tag 0CAN](https://stacks.math.columbia.edu/tag/0CAN) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.exists_minimalPrimes_comap_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.exists_minimalPrimes_comap_eq#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Surjective.lean#L331) (StacksFrontier): “at `I = ⊥`, where minimality over `f⁻¹(⊥)` is the tag's hypothesis that `p` be a minimal prime lying in the image”. References: EGA 0 (1.5.8).

## Tag 0H7L, a lemma

[Tag 0H7L](https://stacks.math.columbia.edu/tag/0H7L) in the Stacks Project.

**`contraction_ne_bot_of_algebraic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/ContractionNeBot.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/ContractionNeBot.lean#L46). The attribute's comment: “first sentence”.

> **Algebraic core (Stacks 0H7L).** Let `A ⊆ B` be an inclusion of integral
> domains, modeled by an injective `algebraMap A B`. Let `K = Frac(A)` and
> `L = Frac(B)` be their fields of fractions, with the induced field embedding
> `K ↪ L` (encoded by the algebra structure `Algebra K L` and the scalar towers
> `A → K → L`, `A → B → L`). Assume the extension `K ⊆ L` is algebraic. If `J` is
> a nonzero ideal of `B`, then its contraction `A ∩ J = comap (algebraMap A B) J`
> is a nonzero ideal of `A`.

```lean
theorem contraction_ne_bot_of_algebraic
    (A B K L : Type*)
    [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [Algebra A B] (hinj : Function.Injective (algebraMap A B))
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra B L] [IsFractionRing B L]
    [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [Algebra.IsAlgebraic K L]
    (J : Ideal B) (hJ : J ≠ ⊥) :
    Ideal.comap (algebraMap A B) J ≠ ⊥
```

**`PrimeSpectrum.not_dense_image_comap_of_isAlgebraic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/ContractionNeBot.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/ContractionNeBot.lean#L67). The attribute's comment: “second sentence”.

> Let `A → B` be an algebraic ring map from a reduced ring into a domain. Then the image in
> `Spec A` of a proper closed subset of `Spec B` is not dense.

```lean
theorem PrimeSpectrum.not_dense_image_comap_of_isAlgebraic {A B : Type*} [CommRing A]
    [CommRing B] [IsReduced A] [IsDomain B] [Algebra A B] [Algebra.IsAlgebraic A B]
    {Z : Set (PrimeSpectrum B)} (hZ : IsClosed Z) (hZ' : Z ≠ Set.univ) :
    ¬ Dense (PrimeSpectrum.comap (algebraMap A B) '' Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.30, Tag 00FF](https://stacks.math.columbia.edu/tag/00FF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
