---
declaration: section
origin: cited
lean: monotone_stabilizes_iff_artinian, finite_dimensional_algebra_is_artinian, MaximalSpectrum.algebraMap_pi_bijective, nonempty_ringEquiv_pi_localization_and_isMaximal, isArtinianRing_iff_isFiniteLength_and_isNoetherianRing_and_toPiLocalization_bijective
statement: formalized
proof: formalized
---

# 10.53 Artinian rings

Section 10.53 of the Stacks Project, [Tag 00J4](https://stacks.math.columbia.edu/tag/00J4). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00J5, a definition

[Tag 00J5](https://stacks.math.columbia.edu/tag/00J5) in the Stacks Project.

Declarations registered for the tag:

- [`monotone_stabilizes_iff_artinian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=monotone_stabilizes_iff_artinian#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L300) (StacksFrontier): “the descending chain condition, as stabilization of monotone chains”.

## Tag 00J6, a lemma

[Tag 00J6](https://stacks.math.columbia.edu/tag/00J6) in the Stacks Project.

**`finite_dimensional_algebra_is_artinian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L158). References: EGA IV (2.5.8.8), “special case”.

> A finite-dimensional algebra over a field is an Artinian ring.

```lean
theorem finite_dimensional_algebra_is_artinian
    (K : Type*) [Field K] (R : Type*) [Ring R] [Algebra K R]
    [FiniteDimensional K R] : IsArtinianRing R
```

## Tag 00JA, a lemma

[Tag 00JA](https://stacks.math.columbia.edu/tag/00JA) in the Stacks Project.

**`MaximalSpectrum.algebraMap_pi_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L102). The attribute's comment: “The product decomposition, for an arbitrary family of localizations. Discreteness of `Spec R` is the tag's own hypothesis, by `PrimeSpectrum.discreteTopology_iff_finite_isMaximal_and_sInf_le_nilradical`.”. References: SGA 3 VIIB (0.1.1), “partial”.

> **Stacks 00JA and 00JB** (the product decomposition).
> A commutative semiring with discrete prime spectrum — in particular an Artinian ring — is the
> product of its localizations at its (finitely many) maximal ideals: for any family `Rₘ` of
> localizations of `R` at the maximal ideals of `R`, the canonical map `R → ∀ 𝔪, Rₘ 𝔪` is
> bijective.

```lean
public theorem algebraMap_pi_bijective (R : Type*) [CommSemiring R]
    [DiscreteTopology (PrimeSpectrum R)]
    (Rₘ : MaximalSpectrum R → Type*) [∀ m, CommSemiring (Rₘ m)] [∀ m, Algebra R (Rₘ m)]
    [∀ m, IsLocalization.AtPrime (Rₘ m) m.asIdeal] :
    Function.Bijective (algebraMap R (∀ m, Rₘ m))
```

**`nonempty_ringEquiv_pi_localization_and_isMaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L122). References: EGA I (6.2.2), “affine, special case”.

> A ring with finitely many maximal ideals whose Jacobson radical is contained in the
> nilradical is isomorphic to the product of its localizations at its maximal ideals, and
> every prime ideal of it is maximal.

```lean
theorem nonempty_ringEquiv_pi_localization_and_isMaximal (R : Type*) [CommRing R] [Finite
  (MaximalSpectrum R)]
    (h : Ring.jacobson R ≤ nilradical R) :
    Nonempty (R ≃+* (Π m : MaximalSpectrum R, Localization.AtPrime m.asIdeal)) ∧
    (∀ p : Ideal R, p.IsPrime → p.IsMaximal)
```

## Tag 00JB, a lemma

[Tag 00JB](https://stacks.math.columbia.edu/tag/00JB) in the Stacks Project.

**`MaximalSpectrum.algebraMap_pi_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L102). The attribute's comment: “The final assertion, under discreteness of `Spec R` in place of Artinian-ness”. References: SGA 3 VIIB (0.1.1), “partial”.

> **Stacks 00JA and 00JB** (the product decomposition).
> A commutative semiring with discrete prime spectrum — in particular an Artinian ring — is the
> product of its localizations at its (finitely many) maximal ideals: for any family `Rₘ` of
> localizations of `R` at the maximal ideals of `R`, the canonical map `R → ∀ 𝔪, Rₘ 𝔪` is
> bijective.

```lean
public theorem algebraMap_pi_bijective (R : Type*) [CommSemiring R]
    [DiscreteTopology (PrimeSpectrum R)]
    (Rₘ : MaximalSpectrum R → Type*) [∀ m, CommSemiring (Rₘ m)] [∀ m, Algebra R (Rₘ m)]
    [∀ m, IsLocalization.AtPrime (Rₘ m) m.asIdeal] :
    Function.Bijective (algebraMap R (∀ m, Rₘ m))
```

**`isArtinianRing_iff_isFiniteLength_and_isNoetherianRing_and_toPiLocalization_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/Basic.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/Basic.lean#L291). The attribute's comment: “All four assertions: the finite-length criterion, Noetherianness, maximality of the primes, and the product decomposition, the last as bijectivity of the canonical map.”. References: EGA I (6.2.2), “affine, special case”; SGA 3 VIIB (0.1.1), “partial, special case”.

> **Artinian rings have finite length, and decompose.** A commutative ring `R` is Artinian if
> and only if it has finite length as a module over itself; and any Artinian ring `R` is also
> Noetherian, has all of its prime ideals maximal, has only finitely many maximal ideals, and is
> the product of its localizations at them, in the sense that the canonical `R`-algebra map
> `R → ∀ 𝔪 : MaximalSpectrum R, Localization.AtPrime 𝔪` is bijective.

```lean
public theorem
    isArtinianRing_iff_isFiniteLength_and_isNoetherianRing_and_toPiLocalization_bijective
    (R : Type*) [CommRing R] :
    (IsArtinianRing R ↔ IsFiniteLength R R) ∧
      (IsArtinianRing R → IsNoetherianRing R ∧ (∀ p : Ideal R, p.IsPrime → p.IsMaximal) ∧
        Finite (MaximalSpectrum R) ∧
        Function.Bijective (MaximalSpectrum.toPiLocalization R))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.53, Tag 00J4](https://stacks.math.columbia.edu/tag/00J4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
