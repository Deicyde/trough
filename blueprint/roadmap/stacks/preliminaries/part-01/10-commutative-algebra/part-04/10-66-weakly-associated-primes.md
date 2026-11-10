---
declaration: section
origin: cited
lean: IsWeaklyAssociatedPrime, weaklyAssociatedPrimes, weaklyAssociated_iff_localization_and_exists_radical_eq, weakAss_eq_minimalPrimes0EMA, Module.weaklyAssociatedPrimes_subset_of_injective, Module.weaklyAssociatedPrimes_subset_union_of_exact, weakAss_empty_iff_zero, StacksProblem.ass_subset_weakAss_subset_supp
statement: formalized
proof: formalized
---

# 10.66 Weakly associated primes

Section 10.66 of the Stacks Project, [Tag 0546](https://stacks.math.columbia.edu/tag/0546). 17 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0547, a definition

[Tag 0547](https://stacks.math.columbia.edu/tag/0547) in the Stacks Project.

**`IsWeaklyAssociatedPrime`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L81). The attribute's comment: “predicate”.

> A prime ideal `I` of `R` is *weakly associated* to the `R`-module `M` if `I` is minimal among
> the prime ideals containing the annihilator `(R ∙ m).annihilator` of some element `m ∈ M`.

```lean
def IsWeaklyAssociatedPrime (I : Ideal R) : Prop
```

**`weaklyAssociatedPrimes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L86). The attribute's comment: “set”.

> The set of weakly associated primes of `M` (over `R`).

```lean
def weaklyAssociatedPrimes : Set (Ideal R)
```

## Tag 0566, a lemma

[Tag 0566](https://stacks.math.columbia.edu/tag/0566) in the Stacks Project.

**`weaklyAssociated_iff_localization_and_exists_radical_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L247).

> For a prime `p` of `R`, the following are equivalent:
>
> 1. `p` is weakly associated to `M`;
> 2. `p R_p` is weakly associated to `M_p`;
> 3. there exists `t ∈ M_p` with `√(Ann_{R_p}(t)) = p R_p`.

```lean
theorem weaklyAssociated_iff_localization_and_exists_radical_eq
    (p : Ideal R) [p.IsPrime] :
    (WeaklyAssociated p M ↔
      WeaklyAssociated (IsLocalRing.maximalIdeal (Localization.AtPrime p))
        (LocalizedModule.AtPrime p M))
    ∧ (WeaklyAssociated (IsLocalRing.maximalIdeal (Localization.AtPrime p))
        (LocalizedModule.AtPrime p M) ↔
      ∃ t : LocalizedModule.AtPrime p M,
        (annihilatorOfElem_semiring (R := Localization.AtPrime p) t).radical
          = IsLocalRing.maximalIdeal (Localization.AtPrime p))
```

## Tag 0EMA, a lemma

[Tag 0EMA](https://stacks.math.columbia.edu/tag/0EMA) in the Stacks Project.

**`weakAss_eq_minimalPrimes0EMA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L505).

> For a reduced commutative ring `R`, the weakly associated primes of `R` are exactly the minimal
> primes of `R`.

```lean
theorem weakAss_eq_minimalPrimes0EMA [IsReduced R] :
    weaklyAssociatedPrimes R R = minimalPrimes R
```

## Tag 0548, a lemma

[Tag 0548](https://stacks.math.columbia.edu/tag/0548) in the Stacks Project.

**`Module.weaklyAssociatedPrimes_subset_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean#L680).

> **Stacks 0548**, first inclusion. Let `R` be a ring and let `f : M →ₗ[R] M'` be an injective
> map of `R`-modules. Then `WeakAss(M) ⊆ WeakAss(M')`, where `WeakAss(N)` is the set of primes of `R`
> minimal over the annihilator of an element of `N`.

```lean
public theorem Module.weaklyAssociatedPrimes_subset_of_injective
    {R : Type*} [CommSemiring R] {M M' : Type*}
    [AddCommMonoid M] [Module R M] [AddCommMonoid M'] [Module R M']
    {f : M →ₗ[R] M'} (hf : Function.Injective f) :
    {p : Ideal R | ∃ m : M, p ∈ (R ∙ m).annihilator.minimalPrimes} ⊆
      {p : Ideal R | ∃ m : M', p ∈ (R ∙ m).annihilator.minimalPrimes}
```

**`Module.weaklyAssociatedPrimes_subset_union_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean#L695).

> **Stacks 0548**, second inclusion. Let `R` be a ring and let `0 → M → M' → M''` be an exact
> sequence of `R`-modules, i.e. `f : M →ₗ[R] M'` is injective with image the kernel of
> `g : M' →ₗ[R] M''`. Then `WeakAss(M') ⊆ WeakAss(M) ∪ WeakAss(M'')`, where `WeakAss(N)` is the set
> of primes of `R` minimal over the annihilator of an element of `N`.

```lean
public theorem Module.weaklyAssociatedPrimes_subset_union_of_exact
    {R : Type*} [CommSemiring R] {M M' M'' : Type*}
    [AddCommMonoid M] [Module R M] [AddCommMonoid M'] [Module R M']
    [AddCommMonoid M''] [Module R M''] {f : M →ₗ[R] M'} {g : M' →ₗ[R] M''}
    (hf : Function.Injective f) (hfg : Function.Exact f g) :
    {p : Ideal R | ∃ m : M', p ∈ (R ∙ m).annihilator.minimalPrimes} ⊆
      {p : Ideal R | ∃ m : M, p ∈ (R ∙ m).annihilator.minimalPrimes} ∪
        {p : Ideal R | ∃ m : M'', p ∈ (R ∙ m).annihilator.minimalPrimes}
```

## Tag 0588, a lemma

[Tag 0588](https://stacks.math.columbia.edu/tag/0588) in the Stacks Project.

**`weakAss_empty_iff_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Basic.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Basic.lean#L30).

> Stacks Tag 0588 (Lemma 10.66.5): an `R`-module `M` is the zero module if and
> only if it has no weakly associated primes.

```lean
theorem weakAss_empty_iff_zero {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M]
    [Module R M] :
    (∀ m : M, m = 0) ↔ weaklyAssociatedPrimes R M = ∅
```

## Tag 0589, a lemma

[Tag 0589](https://stacks.math.columbia.edu/tag/0589) in the Stacks Project.

**`StacksProblem.ass_subset_weakAss_subset_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean#L313). References: SGA 2 III (1.2), “(ii) ⇒ (i)”.

> Stacks tag 0589 (Lemma 10.66.6): `Ass(M) ⊆ WeakAss(M) ⊆ Supp(M)`.

```lean
theorem ass_subset_weakAss_subset_supp (R : Type*) [CommRing R] (M : Type*)
    [AddCommGroup M] [Module R M] :
    Ass R M ⊆ WeakAss R M ∧ WeakAss R M ⊆ Supp R M
```

## Tag 05C3, a lemma

[Tag 05C3](https://stacks.math.columbia.edu/tag/05C3) in the Stacks Project.

**`iUnion_weaklyAssociatedPrimes_eq_zeroDivisorsOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L293).

> Let `R` be a commutative ring and `M` an `R`-module. The union of the weakly associated primes
> of `M` is the set of zerodivisors on `M`.

```lean
theorem iUnion_weaklyAssociatedPrimes_eq_zeroDivisorsOn
    (R : Type*) [CommRing R] (M : Type*) [AddCommGroup M] [Module R M] :
    (⋃ q ∈ weaklyAssociatedPrimes05C3 R M, (q : Set R)) = zeroDivisorsOn05C3 R M
```

## Tag 05C4, a lemma

[Tag 05C4](https://stacks.math.columbia.edu/tag/05C4) in the Stacks Project.

**`Module.exists_mem_minimalPrimes_annihilator_span_singleton_of_minimal_mem_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean#L466).

> **Stacks 05C4.** Let `R` be a ring and `M` an `R`-module. Any prime `𝔭` which is minimal among
> the elements of the support of `M` is weakly associated to `M`, i.e. `𝔭` is minimal over the
> annihilator of some element of `M`.

```lean
public theorem Module.exists_mem_minimalPrimes_annihilator_span_singleton_of_minimal_mem_support
    {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M] {p : PrimeSpectrum R}
    (hp : Minimal (· ∈ Module.support R M) p) :
    ∃ m : M, p.asIdeal ∈ (R ∙ m).annihilator.minimalPrimes
```

## Tag 058A, a lemma

[Tag 058A](https://stacks.math.columbia.edu/tag/058A) in the Stacks Project.

**`isAssociatedPrime_tfae_of_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean#L312).

> **Stacks 058A.** Let `R` be a ring, `M` an `R`-module and `p` a finitely generated ideal of
> `R`. Then `p ∈ Ass(M)`, i.e. `p` is prime and is the annihilator of an element of `M`, iff `p` is
> an associated prime of `M` in Mathlib's sense (the radical of the annihilator of an element), iff
> `p ∈ WeakAss(M)`, i.e. `p` is minimal among the primes containing the annihilator of an element of
> `M`.

```lean
public theorem isAssociatedPrime_tfae_of_fg {R : Type*} [CommSemiring R] {M : Type*}
    [AddCommMonoid M] [Module R M] {p : Ideal R} (hp : p.FG) :
    List.TFAE [(p.IsPrime ∧ ∃ m : M, p = (R ∙ m).annihilator),
      IsAssociatedPrime p M,
      ∃ m : M, p ∈ (R ∙ m).annihilator.minimalPrimes]
```

**`associatedPrimes_eq_setOf_exists_mem_minimalPrimes_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociated.lean#L323).

> **Stacks 058A**, the Noetherian case. Let `R` be a Noetherian ring and `M` an `R`-module. Then
> `Ass(M) = WeakAss(M)`: a prime of `R` is the radical of the annihilator of an element of `M` if and
> only if it is minimal among the primes containing the annihilator of an element of `M`.

```lean
public theorem associatedPrimes_eq_setOf_exists_mem_minimalPrimes_annihilator {R : Type*}
    [CommSemiring R] [IsNoetherianRing R] {M : Type*} [AddCommMonoid M] [Module R M] :
    associatedPrimes R M =
      {p : Ideal R | ∃ m : M, p ∈ (R ∙ m).annihilator.minimalPrimes}
```

## Tag 05C6, a lemma

[Tag 05C6](https://stacks.math.columbia.edu/tag/05C6) in the Stacks Project.

**`weakAss_subset_image_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Basic.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Basic.lean#L79). References: EGA IV (3.1.10.1), “Lifting inclusion”.

> Stacks tag 05C6 (Lemma 10.66.11): for a ring map `φ : R → S` and an `S`-module `M`
> regarded as an `R`-module by restriction of scalars along `φ`, every prime of `R` weakly
> associated to `M` is the contraction along `φ` of a prime of `S` weakly associated
> to `M`.

```lean
theorem weakAss_subset_image_comap
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    {M : Type*} [AddCommGroup M] [Module S M] :
    letI : Module R M := Module.compHom M φ
    weaklyAssociatedPrimes R M ⊆ (Ideal.comap φ) '' (weaklyAssociatedPrimes S M)
```

## Tag 05E1, a lemma

[Tag 05E1](https://stacks.math.columbia.edu/tag/05E1) in the Stacks Project.

**`weakAss_eq_comap_image_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Functoriality.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Functoriality.lean#L262).

> For a finite ring map `φ : R → S` and an `S`-module `M`, the weakly associated primes of `M`
> over `R` are exactly the contractions along `f = Spec(φ)` of the weakly associated primes of `M`
> over `S`, i.e. `WeakAss_R(M) = f(WeakAss_S(M))` as subsets of `Spec(R)`.

```lean
theorem weakAss_eq_comap_image_of_finite (hfin : Module.Finite R S) :
    {p : Ideal R | IsWeaklyAssociatedPrime R M p}
      = (Ideal.comap (algebraMap R S)) '' {q : Ideal S | IsWeaklyAssociatedPrime S M q}
```

## Tag 05C8, a lemma

[Tag 05C8](https://stacks.math.columbia.edu/tag/05C8) in the Stacks Project.

**`weaklyAssociatedPrimes_comap_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L342). References: EGA IV (3.1.10.1), “Quotient maps A → A/I”.

> For a commutative ring `R`, an ideal `I`, and an `R/I`-module `M` (viewed as an `R`-module by
> restriction of scalars), the canonical injection `π* = Ideal.comap (R → R/I)` carries the weakly
> associated primes computed over `R/I` onto those computed over `R`.

```lean
theorem weaklyAssociatedPrimes_comap_quotient :
    Ideal.comap (Ideal.Quotient.mk I) '' weaklyAssociatedPrimes (R ⧸ I) M
      = weaklyAssociatedPrimes R M
```

## Tag 05C9, a lemma

[Tag 05C9](https://stacks.math.columbia.edu/tag/05C9) in the Stacks Project.

**`weakAss_localizedModule_eq_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L436). The attribute's comment: “(1)”.

> `WeakAss_R(S⁻¹M) = ι(WeakAss_{S⁻¹R}(S⁻¹M))`: the `R`-module weakly associated primes of `S⁻¹M`
> are the image under `ι` of the `S⁻¹R`-module weakly associated primes of `S⁻¹M`.

```lean
theorem weakAss_localizedModule_eq_image :
    weakAss R (LocalizedModule S M) =
      localizationComap S '' (weakAss (Localization S) (LocalizedModule S M))
```

**`weakAss_inter_image_eq_weakAss_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Defs.lean#L466). The attribute's comment: “(2)”.

> `{ p ∈ WeakAss_R(M) | p ∈ ι(Spec(S⁻¹R)) } = WeakAss_R(S⁻¹M)`: the primes weakly associated to
> `M` and lying in the image of `ι` (i.e. disjoint from `S`) are exactly the primes weakly associated
> to `S⁻¹M`.

```lean
theorem weakAss_inter_image_eq_weakAss_localizedModule :
    {p ∈ weakAss R M | p ∈ Set.range (localizationComap S)} =
      weakAss R (LocalizedModule S M)
```

## Tag 05CA, a lemma

[Tag 05CA](https://stacks.math.columbia.edu/tag/05CA) in the Stacks Project.

**`Module.weaklyAssociatedPrimes_eq_of_isSMulRegular_of_isLocalizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Localization.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Localization.lean#L172).

> **Stacks 05CA.** Let `R` be a ring, `M` an `R`-module and `S ⊆ R` a multiplicative subset such
> that every `s ∈ S` is a nonzerodivisor on `M`. Then `M` and its localization `S⁻¹M` have the same
> weakly associated primes: `WeakAss(M) = WeakAss(S⁻¹M)`, where `WeakAss(N)` is the set of primes of
> `R` minimal over the annihilator of an element of `N`.

```lean
public theorem Module.weaklyAssociatedPrimes_eq_of_isSMulRegular_of_isLocalizedModule
    {R : Type*} [CommSemiring R] {M M' : Type*}
    [AddCommMonoid M] [Module R M] [AddCommMonoid M'] [Module R M']
    (S : Submonoid R) (f : M →ₗ[R] M') [IsLocalizedModule S f]
    (hS : ∀ s ∈ S, IsSMulRegular M s) :
    {p : Ideal R | ∃ m : M, p ∈ (R ∙ m).annihilator.minimalPrimes} =
      {p : Ideal R | ∃ m : M', p ∈ (R ∙ m).annihilator.minimalPrimes}
```

## Tag 05CB, a lemma

[Tag 05CB](https://stacks.math.columbia.edu/tag/05CB) in the Stacks Project.

**`Module.injective_pi_localization_weaklyAssociatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Separation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Separation.lean#L197).

> **Stacks 05CB.** Let `R` be a ring and `M` an `R`-module. The canonical map
> `M → ∏_{𝔭 ∈ WeakAss(M)} M_𝔭` from `M` to the product of its localizations at the weakly
> associated primes of `M` — the primes minimal over the annihilator of an element of `M` — is
> injective.

```lean
public theorem Module.injective_pi_localization_weaklyAssociatedPrimes
    {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]
    {Mₚ : {p : PrimeSpectrum R // ∃ m : M, p.asIdeal ∈ (R ∙ m).annihilator.minimalPrimes} → Type*}
    [∀ p, AddCommMonoid (Mₚ p)] [∀ p, Module R (Mₚ p)] (f : ∀ p, M →ₗ[R] Mₚ p)
    [∀ p, IsLocalizedModule.AtPrime p.1.asIdeal (f p)] :
    Function.Injective (LinearMap.pi f)
```

## Tag 05CC, a lemma

[Tag 05CC](https://stacks.math.columbia.edu/tag/05CC) in the Stacks Project.

**`Stacks.WeaklyAssociatedPrimes.BaseChange.weakAss_eq_of_flat_domain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Localization.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/Localization.lean#L341).

> Stacks tag 05CC (Lemma 10.66.18): let `R → S` be a ring map and `N` an `S`-module that
> is flat over the domain `R` (with `Module R N` compatible with the `S`-action via
> `IsScalarTower R S N`). Identifying `S ⊗_R K` with `A = Localization T_S`, `N ⊗_R K` with
> `M = LocalizedModule T_S N`, and `Spec(S ⊗_R K)` with its image in `Spec(S)` under
> `PrimeSpectrum.comap (algebraMap S A)`, the weakly associated primes of `N` over `S` are
> exactly the images of the weakly associated primes of `N ⊗_R K` over `S ⊗_R K`: a prime `q`
> of `S` is weakly associated to `N` if and only if there is a prime `q'` of `A` that is
> weakly associated to `M` and whose contraction along `S → A` equals `q`.

```lean
theorem weakAss_eq_of_flat_domain
    [Module.Flat R N] (q : PrimeSpectrum S) :
    IsWeaklyAssociatedPrime S N q.asIdeal ↔
      ∃ q' : PrimeSpectrum (Localization (baseChangeSubmonoid R S)),
        IsWeaklyAssociatedPrime (Localization (baseChangeSubmonoid R S))
          (LocalizedModule (baseChangeSubmonoid R S) N) q'.asIdeal ∧
        PrimeSpectrum.comap (algebraMap S (Localization (baseChangeSubmonoid R S))) q' = q
```

## Tag 0CUB, a lemma

[Tag 0CUB](https://stacks.math.columbia.edu/tag/0CUB) in the Stacks Project.

**`IsWeaklyAssociatedPrime.comap_tensorProduct_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociatedFieldExtension.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/WeaklyAssociatedFieldExtension.lean#L499).

> **Stacks 0CUB.** Let `K / k` be a field extension, `R` a `k`-algebra and `M` an
> `R`-module. If a prime `𝔮 ⊂ R ⊗[k] K` is weakly associated to `M ⊗[k] K`, here written as the
> base change `(R ⊗[k] K) ⊗[R] M`, then the prime `𝔭 = 𝔮 ∩ R` it lies over is weakly associated to
> `M`.

```lean
theorem IsWeaklyAssociatedPrime.comap_tensorProduct_field {k K R M : Type*} [Field k]
    [Field K] [Algebra k K] [CommRing R] [Algebra k R] [AddCommGroup M] [Module R M]
    {q : Ideal (R ⊗[k] K)} (hq : IsWeaklyAssociatedPrime (R ⊗[k] K) ((R ⊗[k] K) ⊗[R] M) q) :
    IsWeaklyAssociatedPrime R M (q.comap (algebraMap R (R ⊗[k] K)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.66, Tag 0546](https://stacks.math.columbia.edu/tag/0546)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
