---
declaration: section
origin: cited
lean: associated_iff_exists_unit_eq_mul, irreducible_iff_ne_zero_and_isUnit_or_eq_unit_mul, Ideal.isPrime_span_singleton_iff_eq_zero_or_prime, Associated, Ideal.span_singleton_eq_span_singleton, WfDvdMonoid.of_setOfPred_isPrincipal_wellFoundedOn_gt, WfDvdMonoid.not_isUnit_iff_exists_factors_eq, UniqueFactorizationMonoid
statement: formalized
proof: formalized
---

# 10.120 Factorization

Section 10.120 of the Stacks Project, [Tag 034O](https://stacks.math.columbia.edu/tag/034O). 17 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 034P, a definition

[Tag 034P](https://stacks.math.columbia.edu/tag/034P) in the Stacks Project.

**`associated_iff_exists_unit_eq_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L77). The attribute's comment: “(1) associates: `x = u y` for a unit `u`”.

> **Stacks 034P (1).** In a domain `R`, elements `x, y` are associates in the Stacks sense, that
> is `x = u y` for a unit `u ∈ R^*`, exactly when they are associated in Mathlib's sense
> (`Associated x y`, a unit `u` with `x * u = y`).

```lean
theorem associated_iff_exists_unit_eq_mul [IsDomain R] {x y : R} :
    Associated x y ↔ ∃ u : Rˣ, x = u * y
```

**`irreducible_iff_ne_zero_and_isUnit_or_eq_unit_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L89). The attribute's comment: “(2) irreducible elements”.

> **Stacks 034P (2).** In a domain `R`, an element `x` is irreducible in the Stacks sense, that
> is nonzero, not a unit, and whenever `x = y z` the factor `y` is a unit or an associate `y = u x`
> (`u ∈ R^*`) of `x`, exactly when it is irreducible in Mathlib's sense (`Irreducible x`).

```lean
theorem irreducible_iff_ne_zero_and_isUnit_or_eq_unit_mul [IsDomain R] {x : R} :
    Irreducible x ↔ x ≠ 0 ∧ ¬IsUnit x ∧
      ∀ y z : R, x = y * z → IsUnit y ∨ ∃ u : Rˣ, y = u * x
```

**`Ideal.isPrime_span_singleton_iff_eq_zero_or_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L114). The attribute's comment: “(3) prime elements”.

> **Stacks 034P (3).** In a domain `R`, an element `x` is prime in the Stacks sense, that is the
> ideal `(x)` is a prime ideal, exactly when `x = 0` or `x` is prime in Mathlib's sense
> (`Prime x`, which excludes `0`). The case `x ≠ 0` is Mathlib's `Ideal.span_singleton_prime`; the
> case `x = 0` is that `(0)` is a prime ideal of a domain (`Ideal.isPrime_bot`).

```lean
theorem Ideal.isPrime_span_singleton_iff_eq_zero_or_prime [IsDomain R] {x : R} :
    (Ideal.span {x}).IsPrime ↔ x = 0 ∨ Prime x
```

Declarations registered for the tag:

- [`Associated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Associated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L126) (StacksFrontier): “(1) associates”.

## Tag 034Q, a lemma

[Tag 034Q](https://stacks.math.columbia.edu/tag/034Q) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.span_singleton_eq_span_singleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.span_singleton_eq_span_singleton#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L126) (StacksFrontier): “associates generate the same principal ideal”.

## Tag 034R, a lemma

[Tag 034R](https://stacks.math.columbia.edu/tag/034R) in the Stacks Project.

Declarations registered for the tag:

- [`WfDvdMonoid.of_setOfPred_isPrincipal_wellFoundedOn_gt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WfDvdMonoid.of_setOfPred_isPrincipal_wellFoundedOn_gt#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L131) (StacksFrontier): “ACC on principal ideals implies `WfDvdMonoid`”.
- [`WfDvdMonoid.not_isUnit_iff_exists_factors_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WfDvdMonoid.not_isUnit_iff_exists_factors_eq#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L133) (StacksFrontier): “a nonzero nonunit factors into irreducibles”.

## Tag 034S, a definition

[Tag 034S](https://stacks.math.columbia.edu/tag/034S) in the Stacks Project.

Declarations registered for the tag:

- [`UniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=UniqueFactorizationMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L138) (StacksFrontier): “unique factorization domains”. References: EGA IV (21.7.7); SGA 2 XI (3.10).
- [`UniqueFactorizationMonoid.of_existsUnique_irreducible_factors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=UniqueFactorizationMonoid.of_existsUnique_irreducible_factors#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L141) (StacksFrontier): “existence and uniqueness of irreducible factorizations characterize a UFD”.
- [`UniqueFactorizationMonoid.factors_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=UniqueFactorizationMonoid.factors_unique#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L143) (StacksFrontier): “uniqueness of irreducible factorizations, up to associates and permutation”.

## Tag 034T, a lemma

[Tag 034T](https://stacks.math.columbia.edu/tag/034T) in the Stacks Project.

**`irreducible_factors_unique_iff_forall_irreducible_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L264). The attribute's comment: “a domain with irreducible factorizations is a UFD iff irreducibles are prime”.

> **Stacks 034T.** Let `R` be a domain in which every nonzero nonunit factors into
> irreducibles. Then `R` is a UFD in the sense of Stacks 034S (every nonzero nonunit has a
> factorization into irreducibles, and two factorizations of the same nonzero nonunit into
> irreducibles agree up to permutation and associates) if and only if every irreducible element
> of `R` is prime.

```lean
theorem irreducible_factors_unique_iff_forall_irreducible_prime {R : Type*} [CommRing R]
    [IsDomain R]
    (hfac : ∀ x : R, x ≠ 0 → ¬IsUnit x → ∃ f : Multiset R, (∀ a ∈ f, Irreducible a) ∧ f.prod = x) :
    ((∀ x : R, x ≠ 0 → ¬IsUnit x → ∃ f : Multiset R, (∀ a ∈ f, Irreducible a) ∧ f.prod = x) ∧
      ∀ x : R, x ≠ 0 → ¬IsUnit x → ∀ f g : Multiset R, (∀ a ∈ f, Irreducible a) →
        (∀ b ∈ g, Irreducible b) → f.prod = x → g.prod = x → Multiset.Rel Associated f g) ↔
      ∀ p : R, Irreducible p → Prime p
```

Declarations registered for the tag:

- [`irreducible_iff_prime_of_existsUnique_irreducible_factors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=irreducible_iff_prime_of_existsUnique_irreducible_factors#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L148) (StacksFrontier): “existence and uniqueness of irreducible factorizations make irreducibles prime”.

## Tag 0AFU, a lemma

[Tag 0AFU](https://stacks.math.columbia.edu/tag/0AFU) in the Stacks Project.

**`localized_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean#L184). The attribute's comment: “(1)”.

> **(Localized irreducibility.)** If `x` is irreducible in `A`, then its image
> in the localization `S⁻¹A` is irreducible or a unit.

```lean
theorem localized_irreducible (S : Submonoid A) (hS : GenByPrimes S)
    (x : A) (hx : Irreducible x) :
    Irreducible (algebraMap A (Localization S) x) ∨
      IsUnit (algebraMap A (Localization S) x)
```

**`prime_iff_localized_prime_or_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean#L421). The attribute's comment: “(2)”.

> **(Primality criterion.)** If `x` is irreducible in `A`, then `x` is prime
> in `A` if and only if its image in `S⁻¹A` is prime or a unit.
>
> PROOF (assembled; sub-lemmas above carry the content):
> `(→)` Given `Prime x`. Decide `IsUnit (φ x)`: if so, right disjunct; else by
> sub-lemma (2b) `Prime (φ x)`, left disjunct.
> `(←)` Given `Prime (φ x) ∨ IsUnit (φ x)`: the prime case is sub-lemma (2c), the
> unit case is sub-lemma (2a).

```lean
theorem prime_iff_localized_prime_or_unit (S : Submonoid A) (hS : GenByPrimes S)
    (x : A) (hx : Irreducible x) :
    Prime x ↔
      (Prime (algebraMap A (Localization S) x) ∨
        IsUnit (algebraMap A (Localization S) x))
```

**`nagata_criterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Nagata.lean#L582). The attribute's comment: “Moreover”.

> **(Nagata's criterion for factoriality.)** `A` is a UFD if and only if every
> nonzero nonunit of `A` factors into irreducibles and `S⁻¹A` is a UFD.
>
> PROOF (assembled; the content is in the sub-lemmas above and theorems (1),(2)):
> `(→)` `UFD A` ⇒ irreducible factorizations exist (3b) and `S⁻¹A` is a UFD (3c).
> `(←)` Given irreducible factorizations and `UFD (S⁻¹A)`: build `UFD A` via
> `UniqueFactorizationMonoid.of_exists_prime_factors` (Stacks 034T).  For `a ≠ 0`:
> units factor as the empty product; for a nonunit, take its irreducible
> factorization and observe each irreducible factor is prime by (3a) (which itself
> uses theorems (1),(2) and `UFD (S⁻¹A)`); the product equals `a` exactly, hence is
> `Associated` to `a`.

```lean
theorem nagata_criterion (S : Submonoid A) (hS : GenByPrimes S) :
    UniqueFactorizationMonoid A ↔
      (HasIrreducibleFactorizations A ∧
        UniqueFactorizationMonoid (Localization S))
```

## Tag 0BUD, a lemma

[Tag 0BUD](https://stacks.math.columbia.edu/tag/0BUD) in the Stacks Project.

**`accp_of_existsUnique_irreducible_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L313).

> A UFD satisfies the ascending chain condition for principal ideals: if `R` is a domain in
> which every nonzero element is, up to a unit, a product of irreducibles, uniquely up to
> associates and order (the definition of a UFD, Stacks 034S), then every ascending chain of
> principal ideals of `R` stabilizes. As in Stacks, the proof factors elements into primes.

```lean
theorem accp_of_existsUnique_irreducible_factors {R : Type*} [CommRing R] [IsDomain R]
    (eif : ∀ a : R, a ≠ 0 → ∃ f : Multiset R, (∀ b ∈ f, Irreducible b) ∧ Associated f.prod a)
    (uif : ∀ f g : Multiset R, (∀ x ∈ f, Irreducible x) → (∀ x ∈ g, Irreducible x) →
      Associated f.prod g.prod → Multiset.Rel Associated f g)
    (f : ℕ → Ideal R) (hp : ∀ i, (f i).IsPrincipal) (hm : ∀ i, f i ≤ f (i + 1)) :
    ∃ n, ∀ m, n ≤ m → f m = f n
```

Declarations registered for the tag:

- [`WfDvdMonoid.of_exists_prime_factors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WfDvdMonoid.of_exists_prime_factors#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L173) (StacksFrontier): “factorization into primes gives a well-founded divisibility relation”.

## Tag 0BUE, a lemma

[Tag 0BUE](https://stacks.math.columbia.edu/tag/0BUE) in the Stacks Project.

**`polynomial_wfDvdMonoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L201).

> Headline: if `R` is a commutative domain satisfying ACCP (`WfDvdMonoid R`),
> then `R[X]` also satisfies ACCP.

```lean
theorem polynomial_wfDvdMonoid {R : Type*} [CommRing R] [IsDomain R] [WfDvdMonoid R] :
    WfDvdMonoid (Polynomial R)
```

## Tag 0BC1, a lemma

[Tag 0BC1](https://stacks.math.columbia.edu/tag/0BC1) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.uniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.uniqueFactorizationMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L164) (StacksFrontier): “a polynomial ring over a UFD is a UFD”.
- [`MvPolynomial.uniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MvPolynomial.uniqueFactorizationMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L165) (StacksFrontier): “a multivariate polynomial ring over a UFD is a UFD”.

## Tag 0AFV, a lemma

[Tag 0AFV](https://stacks.math.columbia.edu/tag/0AFV) in the Stacks Project.

Declarations registered for the tag:

- [`UniqueFactorizationMonoid.instIsIntegrallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=UniqueFactorizationMonoid.instIsIntegrallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L156) (StacksFrontier): “a UFD is integrally closed”.

## Tag 034U, a definition

[Tag 034U](https://stacks.math.columbia.edu/tag/034U) in the Stacks Project.

Declarations registered for the tag:

- [`IsPrincipalIdealRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPrincipalIdealRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L288) (StacksFrontier): “a principal ideal domain is a domain (`IsDomain`) that is a principal ideal ring”.

## Tag 034V, a lemma

[Tag 034V](https://stacks.math.columbia.edu/tag/034V) in the Stacks Project.

Declarations registered for the tag:

- [`PrincipalIdealRing.to_uniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrincipalIdealRing.to_uniqueFactorizationMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L152) (StacksFrontier): “a principal ideal domain is a UFD”.

## Tag 034W, a definition

[Tag 034W](https://stacks.math.columbia.edu/tag/034W) in the Stacks Project.

**`IsStacksDedekindDomain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DedekindDomain/PrimeFactorization.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DedekindDomain/PrimeFactorization.lean#L56). The attribute's comment: “a domain (`IsDomain R`) in which every nonzero ideal is a product of nonzero prime ideals, uniquely up to permutation (`HasUniquePrimeIdealFactorization R`)”.

> A *Dedekind domain* in the sense of the Stacks project: a domain `R` in which every nonzero
> ideal can be written as a product of nonzero prime ideals, uniquely up to permutation. It agrees
> with Mathlib's `IsDedekindDomain` by `isStacksDedekindDomain_iff_isDedekindDomain`.

```lean
def IsStacksDedekindDomain (R : Type*) [CommRing R] : Prop
```

## Tag 0AUQ, a lemma

[Tag 0AUQ](https://stacks.math.columbia.edu/tag/0AUQ) in the Stacks Project.

Declarations registered for the tag:

- [`IsPrincipalIdealRing.isDedekindDomain`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPrincipalIdealRing.isDedekindDomain#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/UniqueFactorizationDomain/Basic.lean#L159) (StacksFrontier): “a principal ideal domain is a Dedekind domain”. References: EGA III (7.4.3), “special case”.

## Tag 09ME, a lemma

[Tag 09ME](https://stacks.math.columbia.edu/tag/09ME) in the Stacks Project.

**`Ideal.invertible_of_mul_eq_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Invertible.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/Invertible.lean#L215). The attribute's comment: “Stated as `Module.Invertible A ↥I` for one factor: the hypotheses are symmetric in `I` and `J`, and finite generation and local freeness of rank `1` follow from invertibility. The source's `I ≠ 0` and `J ≠ 0` are consequences of the hypothesis on `f` and are omitted. See the module docstring.”.

> **A factor of a principal ideal generated by a nonzerodivisor is invertible.** Let `A` be a
> commutative ring and let `I` and `J` be ideals of `A` with `I * J = (f)` for a nonzerodivisor
> `f ∈ A`. Then `I` is an invertible `A`-module, that is, finite locally free of rank `1`; in
> particular `I` is a finitely generated ideal. Applying this to `J * I = (f)` gives the same
> conclusions for `J`.

```lean
public theorem invertible_of_mul_eq_span_singleton {A : Type*} [CommRing A] {I J : Ideal A}
    {f : A} (hf : f ∈ nonZeroDivisors A) (hIJ : I * J = Ideal.span {f}) :
    Module.Invertible A I
```

## Tag 034X, a lemma

[Tag 034X](https://stacks.math.columbia.edu/tag/034X) in the Stacks Project.

**`Stacks.hasUniquePrimeIdealFactorization_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DedekindDomain/TFAE.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DedekindDomain/TFAE.lean#L249).

> **Stacks 034X**. For a ring `R` the following are equivalent:
> 1. `R` is a Dedekind domain in the sense of tag 034W: a domain in which every nonzero ideal is a
>    product of nonzero prime ideals, uniquely up to permutation;
> 2. `R` is a Noetherian domain and `R_𝔪` is a discrete valuation ring for every nonzero maximal
>    ideal `𝔪`;
> 3. `R` is a Noetherian normal domain of Krull dimension at most one.
>
> In (2) the domain hypothesis is an existential binder, so that it is available as an instance
> when stating that the localizations are discrete valuation rings.

```lean
theorem hasUniquePrimeIdealFactorization_tfae (R : Type*) [CommRing R] :
    [IsDomain R ∧ HasUniquePrimeIdealFactorization R,
      ∃ _ : IsDomain R, IsNoetherianRing R ∧
        ∀ (m : Ideal R) [m.IsMaximal], m ≠ ⊥ → IsDiscreteValuationRing (Localization.AtPrime m),
      IsDomain R ∧ IsNoetherianRing R ∧ IsIntegrallyClosed R ∧ ringKrullDim R ≤ 1].TFAE
```

## Tag 09IG, a lemma

[Tag 09IG](https://stacks.math.columbia.edu/tag/09IG) in the Stacks Project.

**`IsIntegralClosure.isDedekindDomain_and_comap_surjective_and_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/DedekindDomain.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/DedekindDomain.lean#L339). The attribute's comment: “Finite fibres and finiteness of the induced residue field extensions are packaged as `Algebra.QuasiFinite A C`, from which they follow by name; `dim A = 1` is weakened to `Ring.DimensionLEOne A`. See the module docstring.”. References: EGA 0 (23.2.6), “residue extensions”; EGA 0 (23.2.8), “(ii), dim ≤ 1”; EGA 0 (23.2.7), “partial”; EGA IV (18.9.7.8), “more general”; EGA IV (9.5.7), “B is a Dedekind ring”.

> **Variant of Krull–Akizuki.** Let `A` be a Noetherian domain of Krull dimension at most one
> with fraction field `K`, let `L/K` be a finite field extension and let `C` be the integral closure
> of `A` in `L`. Then `C` is a Dedekind domain, the map `Spec(C) → Spec(A)` is surjective, and `C`
> is quasi-finite over `A`; the latter says that every fibre `κ(𝔭) ⊗[A] C` is a finite-dimensional
> `κ(𝔭)`-vector space, whence `Spec(C) → Spec(A)` has finite fibres and induces finite residue field
> extensions. Neither `A` integrally closed nor `L/K` separable is assumed, so `C` need not be a
> finite `A`-algebra.

```lean
public theorem isDedekindDomain_and_comap_surjective_and_quasiFinite
    (A K L C : Type*) [CommRing A] [IsDomain A] [IsNoetherianRing A] [Ring.DimensionLEOne A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra K L] [FiniteDimensional K L] [Algebra A L] [IsScalarTower A K L]
    [CommRing C] [Algebra A C] [Algebra C L] [IsScalarTower A C L] [IsIntegralClosure C A L] :
    IsDedekindDomain C ∧ Function.Surjective (PrimeSpectrum.comap (algebraMap A C)) ∧
      Algebra.QuasiFinite A C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.120, Tag 034O](https://stacks.math.columbia.edu/tag/034O)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
