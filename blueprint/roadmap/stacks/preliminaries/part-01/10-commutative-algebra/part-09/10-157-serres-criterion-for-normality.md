---
declaration: section
origin: cited
lean: HasPropertyRk, PropertySkRing, PropertySkModule, propertySkRing_of_ringEquiv, Module.forall_minimal_mem_associatedPrimes_iff_min_one_supportDim_le_depth, isReduced_iff_hasR0_and_hasS1, isDomain_and_isIntegrallyClosed_atPrime_iff_isRegularLocalRing_and_min_two_le_depth, main_theorem0567
statement: formalized
proof: formalized
---

# 10.157 Serre's criterion for normality

Section 10.157 of the Stacks Project, [Tag 031O](https://stacks.math.columbia.edu/tag/031O). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 031P, a definition

[Tag 031P](https://stacks.math.columbia.edu/tag/031P) in the Stacks Project.

**`HasPropertyRk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Defs.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Defs.lean#L104). The attribute's comment: “Rk”. References: EGA IV (5.8.2), “affine case”; EGA IV (7.5.3), “partial”.

> Property `(Rₖ)`: every prime `𝔭` of `A` of height at most `k` has regular localization `A_𝔭`.
> As `height 𝔭 = dim A_𝔭`, this is regularity of `A` in codimension at most `k`.

```lean
def HasPropertyRk (A : Type*) [CommRing A] (k : ℕ) : Prop
```

**`PropertySkRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Defs.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Defs.lean#L113). The attribute's comment: “Sk ring”. References: EGA IV (5.7.2), “special case”; EGA IV (5.7.3), “special case”; EGA IV (7.5.3).

> Property `(Sₖ)` for a Noetherian commutative ring `R`: at every prime `𝔭` the depth of the
> localization `R_𝔭` is at least `min(k, dim R_𝔭)`.

```lean
def PropertySkRing (R : Type*) [CommRing R] [IsNoetherianRing R] (k : ℕ) : Prop
```

**`PropertySkModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Defs.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Defs.lean#L124). The attribute's comment: “Sk module”. References: EGA IV (5.7.2), “special case”; EGA IV (5.7.3); EGA IV (7.5.3), “more general”.

> Property `(Sₖ)` for a finite module `M` over a Noetherian commutative ring `R`: at every prime
> `𝔭` the depth of the localization `M_𝔭` is at least `min(k, dim Supp(M_𝔭))`.

```lean
def PropertySkModule (R : Type*) [CommRing R] [IsNoetherianRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] (k : ℕ) : Prop
```

**`propertySkRing_of_ringEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/RingEquiv.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/RingEquiv.lean#L71). The attribute's comment: “Sk ring, isomorphism invariance”.

> **Serre's condition `(Sₖ)` is invariant under an isomorphism of rings.** A prime of the
> target pulls back along the isomorphism, `Localization.localRingEquiv` identifies the two
> localizations, and both the Krull dimension and the depth are invariant under that
> isomorphism.

```lean
public theorem propertySkRing_of_ringEquiv {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [IsNoetherianRing A] [IsNoetherianRing B]
    (e : A ≃+* B) (k : ℕ) (h : PropertySkRing A k) : PropertySkRing B k
```

## Tag 031Q, a lemma

[Tag 031Q](https://stacks.math.columbia.edu/tag/031Q) in the Stacks Project.

**`Module.forall_minimal_mem_associatedPrimes_iff_min_one_supportDim_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Defs.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Defs.lean#L356). The attribute's comment: “Property `(S₁)` is spelled out as the inequality `min{1, dim Supp(M_𝔭)} ≤ depth_{𝔭R_𝔭}(M_𝔭)` of Definition 031P at `k = 1` rather than as `PropertySkModule R M 1`, whose depth and dimension truncate the conventions this statement needs; having no embedded associated prime is spelled out with `Minimal`, as in tag 02M6; and the localizations are the canonical models `Localization.AtPrime` and `LocalizedModule`, indexed by `PrimeSpectrum R` as in Definition 0AAH. See the module docstring.”.

> Let `R` be a Noetherian ring and let `M` be a finite `R`-module. Then
> `M` has no embedded associated prime — that is, every associated prime of `M` is minimal among
> the associated primes of `M` — if and only if `M` has property `(S₁)`: for every prime `𝔭` of
> `R` the depth of the `R_𝔭`-module `M_𝔭` along `𝔭R_𝔭` is at least `min{1, dim Supp(M_𝔭)}`, the
> inequality being read in `WithBot ℕ∞`. Concretely the right-hand side says that
> `depth(M_𝔭) ≥ 1` at every prime `𝔭` with `dim Supp(M_𝔭) ≥ 1`.

```lean
public theorem forall_minimal_mem_associatedPrimes_iff_min_one_supportDim_le_depth
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    (∀ p ∈ associatedPrimes R M, Minimal (· ∈ associatedPrimes R M) p) ↔
      ∀ p : PrimeSpectrum R,
        min 1 (supportDim (Localization.AtPrime p.asIdeal)
            (LocalizedModule p.asIdeal.primeCompl M)) ≤
          (depth (Localization.AtPrime p.asIdeal)
            (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M) : WithBot ℕ∞)
```

## Tag 031R, a lemma

[Tag 031R](https://stacks.math.columbia.edu/tag/031R) in the Stacks Project.

**`isReduced_iff_hasR0_and_hasS1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Reduced.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Reduced.lean#L405). References: EGA IV (12.1.8), “more general”; EGA IV (3.2.1), “a), special case”; EGA IV (5.8.5), “special case”; EGA IV (7.3.9), “(i), special case”.

> Stacks Tag 031R (Lemma 10.157.3, Serre's criterion). A Noetherian ring `R`
> is reduced if and only if it has both property `(R_0)` and property `(S_1)`.

```lean
theorem isReduced_iff_hasR0_and_hasS1 (R : Type*) [CommRing R] [IsNoetherianRing R] :
    IsReduced R ↔ HasR0 R ∧ HasS1 R
```

## Tag 031S, a lemma

[Tag 031S](https://stacks.math.columbia.edu/tag/031S) in the Stacks Project.

**`isDomain_and_isIntegrallyClosed_atPrime_iff_isRegularLocalRing_and_min_two_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Criterion.lean, line 886](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Criterion.lean#L886). The attribute's comment: “Normality is inlined as `IsDomain` plus `IsIntegrallyClosed` on `Localization.AtPrime 𝔭` for every prime `𝔭`, as in item (1) of tag 030C, Mathlib having no predicate for a normal ring; properties `(R_1)` and `(S_2)` are spelled out from Definition 031P at `k = 1` and `k = 2` with `Ideal.height`, `IsRegularLocalRing`, `ringKrullDim` and `Module.depth` (tag 00LI), the depth inequality being read in `WithBot ℕ∞`. See the module docstring.”. References: EGA IV (5.8.6), “affine case”; SGA 2 XI (3.11), “more general”.

> **Stacks Tag 031S (Serre's criterion for normality).** Let `R` be a Noetherian ring. Then `R`
> is a normal ring — every localization `R_𝔭` at a prime is a domain integrally closed in its
> fraction field — if and only if `R` has properties `(R_1)` and `(S_2)`: the local ring `R_𝔭` is
> regular for every prime `𝔭` of height `≤ 1`, and `depth(R_𝔭) ≥ min{2, dim(R_𝔭)}` for every
> prime `𝔭`, the latter inequality being read in `WithBot ℕ∞`.

```lean
public theorem isDomain_and_isIntegrallyClosed_atPrime_iff_isRegularLocalRing_and_min_two_le_depth
    {R : Type*} [CommRing R] [IsNoetherianRing R] :
    (∀ (p : Ideal R) [p.IsPrime],
        IsDomain (Localization.AtPrime p) ∧ IsIntegrallyClosed (Localization.AtPrime p)) ↔
      (∀ (p : Ideal R) [p.IsPrime], p.height ≤ 1 →
          IsRegularLocalRing (Localization.AtPrime p)) ∧
        ∀ (p : Ideal R) [p.IsPrime],
          min 2 (ringKrullDim (Localization.AtPrime p)) ≤
            (Module.depth (Localization.AtPrime p)
              (IsLocalRing.maximalIdeal (Localization.AtPrime p))
              (Localization.AtPrime p) : WithBot ℕ∞)
```

## Tag 0567, a lemma

[Tag 0567](https://stacks.math.columbia.edu/tag/0567) in the Stacks Project.

**`main_theorem0567`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegrallyClosed/Stability.lean#L64). References: EGA II (7.1.6), “more general”; EGA IV (6.13.1), “special case”; EGA IV (7.3.9), “(i): (iv) implies (vii)”.

> **A regular ring is normal.**

```lean
theorem main_theorem0567 (R : Type*) [CommRing R] [IsRegularRing R] :
    IsNormalRing R
```

## Tag 031T, a lemma

[Tag 031T](https://stacks.math.columbia.edu/tag/031T) in the Stacks Project.

**`associatedPrimes_minimal_and_height_eq_one_and_iInf_localization_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/Defs.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/Defs.lean#L552). The attribute's comment: “A normal domain is `IsDomain` plus `IsIntegrallyClosed`, as in Definition 0309; having no embedded primes is spelled with `Minimal`, as in tags 02M6 and 031Q; item (2) is the equality `⨅ 𝔭, R_𝔭 = ⊥` of `R`-subalgebras of `K`, as in `IsDedekindDomain.HeightOneSpectrum.iInf_localization_eq_bot`; and `R ∩ xR` is the pullback of `xR ⊆ K` along `Algebra.linearMap R K`. See the module docstring.”. References: EGA 0 (23.2.9), “A normal (A = A')”; EGA IV (7.8.3), “(viii), special case”.

> Let `R` be a Noetherian normal domain with fraction field `K`. Then
> (1) for every nonzero `a : R` each associated prime of `R/aR` is minimal among the associated
> primes of `R/aR` — that is, `R/aR` has no embedded primes — and has height `1`;
> (2) `R` is the intersection, inside `K`, of the subalgebras `R_𝔭` over the primes `𝔭` of height
> `1`; and (3) the same as (1) for the ideal `R ∩ xR` attached to a nonzero `x : K`.

```lean
public theorem associatedPrimes_minimal_and_height_eq_one_and_iInf_localization_eq_bot
    {R : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R] [IsIntegrallyClosed R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K] :
    (∀ a : R, a ≠ 0 → ∀ p ∈ associatedPrimes R (R ⧸ Ideal.span {a}),
        Minimal (· ∈ associatedPrimes R (R ⧸ Ideal.span {a})) p ∧ p.height = 1) ∧
      ((⨅ p : PrimeSpectrum R, ⨅ _ : p.asIdeal.height = 1,
          Localization.subalgebra.ofField K _ p.asIdeal.primeCompl_le_nonZeroDivisors) = ⊥) ∧
      (∀ x : K, x ≠ 0 →
        ∀ p ∈ associatedPrimes R
            (R ⧸ ((Submodule.span R {x}).comap (Algebra.linearMap R K) : Ideal R)),
          Minimal (· ∈ associatedPrimes R
              (R ⧸ ((Submodule.span R {x}).comap (Algebra.linearMap R K) : Ideal R))) p ∧
            p.height = 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.157, Tag 031O](https://stacks.math.columbia.edu/tag/031O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
