---
declaration: section
origin: cited
lean: IsIntegrallyClosed, isIntegrallyClosed_iff, integralClosure_isNormalDomain, isAlmostIntegral_iff, IsCompletelyNormal, IsLocalization.isDomain_of_le_nonZeroDivisors, isIntegrallyClosed_of_isLocalization, PrincipalIdealRing.to_uniqueFactorizationMonoid
statement: formalized
proof: formalized
---

# 10.37 Normal rings

Section 10.37 of the Stacks Project, [Tag 037B](https://stacks.math.columbia.edu/tag/037B). 14 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0309, a definition

[Tag 0309](https://stacks.math.columbia.edu/tag/0309) in the Stacks Project.

Declarations registered for the tag:

- [`IsIntegrallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsIntegrallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L20) (StacksFrontier). References: EGA IV (14.5.5); EGA IV (7.5.3), “(vi), partial”.
- [`isIntegrallyClosed_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isIntegrallyClosed_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L23) (StacksFrontier): “identified with the Stacks wording”.

## Tag 034L, a lemma

[Tag 034L](https://stacks.math.columbia.edu/tag/034L) in the Stacks Project.

**`integralClosure_isNormalDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean#L151). References: EGA II (6.3.7), “special case”; EGA II (6.3.8), “special case”; EGA II (6.3.9), “special case”; EGA IV (14.5.5), “partial”.

> **Stacks Tag 034L.** If `S` is a normal domain, then the integral closure of
> `R` in `S` is a normal domain.

```lean
theorem integralClosure_isNormalDomain
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    (hS : IsNormalDomain S) :
    IsNormalDomain (integralClosure R S)
```

## Tag 00GW, a definition

[Tag 00GW](https://stacks.math.columbia.edu/tag/00GW) in the Stacks Project.

**`isAlmostIntegral_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/AlmostIntegral.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/AlmostIntegral.lean#L71). The attribute's comment: “(1)”.

> For a domain `R`, an element `g` of the fraction field is almost integral over `R` if and
> only if there is a nonzero `r ∈ R` with `r • g ^ n` in the image of `R` for all `n`.

```lean
theorem isAlmostIntegral_iff (g : FractionRing R) :
    IsAlmostIntegral R g ↔
      ∃ r : R, r ≠ 0 ∧ ∀ n, r • g ^ n ∈ (algebraMap R (FractionRing R)).range
```

**`IsCompletelyNormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/AlmostIntegral.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/AlmostIntegral.lean#L79). The attribute's comment: “(2)”.

> A domain `R` is *completely normal* if every almost integral element of its fraction field
> lies in the image of `R`.

```lean
def IsCompletelyNormal (R : Type*) [CommRing R] [IsDomain R] : Prop
```

## Tag 00GY, a lemma

[Tag 00GY](https://stacks.math.columbia.edu/tag/00GY) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.isDomain_of_le_nonZeroDivisors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.isDomain_of_le_nonZeroDivisors#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L121) (StacksFrontier): “the localization is a domain”.
- [`isIntegrallyClosed_of_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isIntegrallyClosed_of_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L123) (StacksFrontier): “the localization is integrally closed”. References: EGA II (8.11.8), “partial”.

## Tag 00GZ, a lemma

[Tag 00GZ](https://stacks.math.columbia.edu/tag/00GZ) in the Stacks Project.

Declarations registered for the tag:

- [`PrincipalIdealRing.to_uniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrincipalIdealRing.to_uniqueFactorizationMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean#L101) (StacksFrontier): “a principal ideal domain is a unique factorization domain”.
- [`UniqueFactorizationMonoid.instIsIntegrallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=UniqueFactorizationMonoid.instIsIntegrallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean#L103) (StacksFrontier): “a unique factorization domain is integrally closed in its field of fractions”.

## Tag 0BI0, a lemma

[Tag 0BI0](https://stacks.math.columbia.edu/tag/0BI0) in the Stacks Project.

**`PowerSeries.instIsIntegrallyClosed`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PowerSeries/IntegrallyClosed.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PowerSeries/IntegrallyClosed.lean#L312). References: EGA IV (21.13.9), “(iv)”.

> The formal power series ring `R⟦X⟧` over a Noetherian normal domain `R` is a normal domain:
> it is integrally closed in its fraction field. Together with `PowerSeries.instIsNoetherianRing`
> and `PowerSeries.instIsDomain` this says that `R⟦X⟧` is a Noetherian normal domain.

```lean
public instance instIsIntegrallyClosed {R : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    [IsIntegrallyClosed R] : IsIntegrallyClosed R⟦X⟧
```

## Tag 030B, a lemma

[Tag 030B](https://stacks.math.columbia.edu/tag/030B) in the Stacks Project.

Declarations registered for the tag:

- [`isIntegrallyClosed_of_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isIntegrallyClosed_of_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L119) (StacksFrontier): “(1) ⇒ (2) and (1) ⇒ (3)”. References: EGA II (8.11.8), “partial”.
- [`IsIntegrallyClosed.of_isLocalization_maximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsIntegrallyClosed.of_isLocalization_maximal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L122) (StacksFrontier): “(3) ⇒ (1)”.

## Tag 00GV, a definition

[Tag 00GV](https://stacks.math.columbia.edu/tag/00GV) in the Stacks Project.

**`IsNormalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L28). References: EGA IV (5.13.5); EGA IV (5.13.6).

> A commutative ring `R` is *normal* if for every prime ideal `p` the localization `R_p` is an
> integrally closed integral domain.

```lean
def IsNormalRing (R : Type*) [CommRing R] : Prop
```

## Tag 034M, a lemma

[Tag 034M](https://stacks.math.columbia.edu/tag/034M) in the Stacks Project.

**`IsNormalRing.isIntegrallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L201). References: EGA IV (6.14.1.1), “(i) necessity”.

> A normal ring `R` is integrally closed in its total ring of fractions
> `Q(R) = FractionRing R`.

```lean
theorem IsNormalRing.isIntegrallyClosed
    {R : Type*} [CommRing R] (hR : IsNormalRing R) :
    IsIntegrallyClosed R
```

## Tag 037C, a lemma

[Tag 037C](https://stacks.math.columbia.edu/tag/037C) in the Stacks Project.

**`IsNormalRing.isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L74).

> A localization of a normal ring is a normal ring.

```lean
theorem IsNormalRing.isLocalization {R : Type*} [CommRing R] (h : IsNormalRing R)
    (M : Submonoid R) (S : Type*) [CommRing S] [Algebra R S] [IsLocalization M S] :
    IsNormalRing S
```

## Tag 00H1, a lemma

[Tag 00H1](https://stacks.math.columbia.edu/tag/00H1) in the Stacks Project.

**`polynomial_ring_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Polynomial.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Polynomial.lean#L60).

> Stacks Lemma 10.37.14: if `R` is a normal ring, then the polynomial ring
> `R[x]` (`Polynomial R`) is a normal ring.

```lean
theorem polynomial_ring_normal (R : Type*) [CommRing R] (hR : IsNormalRing R) :
    IsNormalRing (Polynomial R)
```

## Tag 0CYA, a lemma

[Tag 0CYA](https://stacks.math.columbia.edu/tag/0CYA) in the Stacks Project.

**`isNormalRing_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean#L277).

> A finite product of normal rings is normal.
> (Stacks Lemma 10.37.16, tag `0CYA`.)

```lean
theorem isNormalRing_pi
    {ι : Type*} [Finite ι] {R : ι → Type*} [∀ i, CommRing (R i)]
    (h : ∀ i, IsNormalRing (R i)) :
    IsNormalRing (∀ i, R i)
```

## Tag 030C, a lemma

[Tag 030C](https://stacks.math.columbia.edu/tag/030C) in the Stacks Project.

**`isIntegrallyClosed_tfae_of_finite_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/ProductOfDomains.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/ProductOfDomains.lean#L256). References: EGA IV (5.13.5), “Noeth ⇒ product of doms”; EGA IV (6.14.1.1), “(i)”.

> **Stacks 030C.** Let `R` be a reduced ring with finitely many minimal primes. Then the
> following are equivalent: (1) `R` is a normal ring, i.e. all its localizations at primes are
> normal domains; (2) `R` is integrally closed in its total ring of fractions; (3) `R` is a finite
> product of normal domains; (4) the canonical map from `R` to the product of the quotients `R/𝔭`
> by its minimal primes is bijective and each such quotient is integrally closed.

```lean
theorem isIntegrallyClosed_tfae_of_finite_minimalPrimes {R : Type u} [CommRing R]
    [IsReduced R] (hR : (minimalPrimes R).Finite) :
    List.TFAE
      [ ∀ (p : Ideal R) [p.IsPrime],
          IsDomain (Localization.AtPrime p) ∧ IsIntegrallyClosed (Localization.AtPrime p),
        IsIntegrallyClosed R,
        ∃ (n : ℕ) (A : Fin n → Type u) (_ : ∀ i, CommRing (A i)),
          (∀ i, IsDomain (A i)) ∧ (∀ i, IsIntegrallyClosed (A i)) ∧
            Nonempty (R ≃+* ∀ i, A i),
        (∀ p ∈ minimalPrimes R, IsIntegrallyClosed (R ⧸ p)) ∧
          Function.Bijective
            (RingHom.pi fun p : minimalPrimes R => Ideal.Quotient.mk (p : Ideal R)) ]
```

## Tag 037D, a lemma

[Tag 037D](https://stacks.math.columbia.edu/tag/037D) in the Stacks Project.

**`directLimit_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegrallyClosed/Defs.lean#L488). References: EGA IV (5.13.6), “more general”.

> Let `(ι, ≤)` be a directed nonempty preorder, let `(G_i)` be a family of commutative rings,
> and let `φ_{ij} : G_i →+* G_j` (for `i ≤ j`) be ring homomorphisms forming a directed system of
> rings. If every `G_i` is a normal ring, then the directed colimit `Ring.DirectLimit G φ` is a
> normal ring.

```lean
theorem directLimit_isNormalRing
    (hdir : DirectedSystem G (fun i j h => φ i j h))
    (hnormal : ∀ i, IsNormalRing (G i)) :
    IsNormalRing (Ring.DirectLimit G (fun i j h => φ i j h))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.37, Tag 037B](https://stacks.math.columbia.edu/tag/037B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
