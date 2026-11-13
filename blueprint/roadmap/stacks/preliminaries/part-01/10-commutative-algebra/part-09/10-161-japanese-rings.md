---
declaration: section
origin: cited
lean: IsN1, IsJapaneseRing, isN1_and_isJapaneseRing_of_isLocalization, isN1_and_isJapaneseRing_of_localizationSpan, isJapaneseRing_of_quasiFinite, main_theorem_032j, isN1_of_finite_of_isN1, isN2_of_finite_of_isN2
statement: formalized
proof: formalized
---

# 10.161 Japanese rings

Section 10.161 of the Stacks Project, [Tag 0BI1](https://stacks.math.columbia.edu/tag/0BI1). 15 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 032F, a definition

[Tag 032F](https://stacks.math.columbia.edu/tag/032F) in the Stacks Project.

**`IsN1`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Defs.lean#L100). The attribute's comment: “(1)”.

> A domain `R` is **N-1** if the integral closure of `R` in its field of fractions is a finite
> `R`-module.
>
> The field of fractions is `FractionRing R`; see the module docstring for the formulation with an
> arbitrary field of fractions. As with `IsIntegrallyClosed`, `R` is not required to be a domain:
> for a general commutative ring `FractionRing R` is the total ring of fractions, and the condition
> reads the same.

```lean
abbrev IsN1 (R : Type*) [CommRing R] : Prop
```

**`IsJapaneseRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Defs.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Defs.lean#L109). The attribute's comment: “(2)”. References: EGA 0 (23.1.1), “def. of Japanese”.

> A domain `R` is **N-2**, or **Japanese**, if for every finite field extension `L` of its
> field of fractions `K = Frac(R)`, the integral closure of `R` in `L` is a finite `R`-module.
>
> The extension is presented as a field `L` that is a `K`-algebra, finite dimensional over `K`,
> whose `R`-algebra structure is the composite of `R → K` with `K → L`.

```lean
class IsJapaneseRing (R : Type u) [CommRing R] [IsDomain R] : Prop
```

## Tag 032G, a lemma

[Tag 032G](https://stacks.math.columbia.edu/tag/032G) in the Stacks Project.

**`isN1_and_isJapaneseRing_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean#L151).

> **N-1 and N-2 pass to a localization.** Stacks Tag 032G: if a domain `R` is N-1 then so is
> every localization of `R` which is again a domain, and the same for N-2.

```lean
theorem isN1_and_isJapaneseRing_of_isLocalization {R : Type u} [CommRing R] [IsDomain R]
    (M : Submonoid R) (Rₛ : Type u) [CommRing Rₛ] [IsDomain Rₛ] [Algebra R Rₛ]
    [IsLocalization M Rₛ] :
    (IsN1 R → IsN1 Rₛ) ∧ (IsJapaneseRing R → IsJapaneseRing Rₛ)
```

## Tag 032H, a lemma

[Tag 032H](https://stacks.math.columbia.edu/tag/032H) in the Stacks Project.

**`isN1_and_isJapaneseRing_of_localizationSpan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean#L265).

> **N-1 and N-2 descend along a principal open cover.** Stacks Tag 032H: let `R` be a domain and
> let `t ⊆ R` generate the unit ideal. If the localization `R_g` is N-1 for every `g ∈ t` then so is
> `R`, and the same for N-2.

```lean
theorem isN1_and_isJapaneseRing_of_localizationSpan {R : Type u} [CommRing R] [IsDomain R]
    (t : Set R) (ht : Ideal.span t = ⊤)
    {Rₚ : ∀ _ : t, Type u} [∀ g, CommRing (Rₚ g)] [∀ g, IsDomain (Rₚ g)]
    [∀ g, Algebra R (Rₚ g)] [∀ g, IsLocalization.Away g.val (Rₚ g)] :
    ((∀ g, IsN1 (Rₚ g)) → IsN1 R) ∧
      ((∀ g, IsJapaneseRing (Rₚ g)) → IsJapaneseRing R)
```

## Tag 032I, a lemma

[Tag 032I](https://stacks.math.columbia.edu/tag/032I) in the Stacks Project.

**`isJapaneseRing_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean#L484).

> **N-2 ascends along a quasi-finite extension of domains.** Stacks Tag 032I: let `R ⊆ S` be a
> quasi-finite extension of domains with `R` Noetherian and N-2. Then `S` is N-2.
>
> Zariski's main theorem covers `Spec S` by principal opens on which `S` agrees with a subalgebra
> module-finite over `R`; N-2 ascends to such a subalgebra, passes to its localizations (Tag 032G),
> and descends from the cover (Tag 032H).

```lean
theorem isJapaneseRing_of_quasiFinite {R S : Type u} [CommRing R] [IsDomain R] [CommRing S]
    [IsDomain S] [Algebra R S] [FaithfulSMul R S] [IsNoetherianRing R] [Algebra.FiniteType R S]
    [Algebra.QuasiFinite R S] (hR : IsJapaneseRing R) : IsJapaneseRing S
```

## Tag 032J, a lemma

[Tag 032J](https://stacks.math.columbia.edu/tag/032J) in the Stacks Project.

**`main_theorem_032j`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Basic.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Basic.lean#L610).

> Theorem (Stacks Tag 032J). Let `R` be a Noetherian domain. If the Laurent
> polynomial ring `R[z, z^{-1}]` is N-1, then `R` is N-1.

```lean
theorem main_theorem_032j (R : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    (h : IsN1 (LaurentPolynomial R)) : IsN1 R
```

## Tag 032K, a lemma

[Tag 032K](https://stacks.math.columbia.edu/tag/032K) in the Stacks Project.

**`isN1_of_finite_of_isN1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Basic.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Basic.lean#L702). The attribute's comment: “(1)”.

> **Statement 1 (N-1 descends, part of Stacks Tag 032K).**
> Let `R` be a Noetherian domain and `R ⊂ S` a finite extension of domains
> (modelled by an injective algebra map `R → S` with `S` finite over `R`).
> If `S` is N-1, then `R` is N-1.

```lean
theorem isN1_of_finite_of_isN1
    (R S : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    [CommRing S] [IsDomain S] [Algebra R S]
    (hinj : Function.Injective (algebraMap R S))
    (hfin : Module.Finite R S)
    (hS : IsN1 S) : IsN1 R
```

**`isN2_of_finite_of_isN2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Basic.lean, line 818](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Basic.lean#L818). The attribute's comment: “(2)”.

> **Statement 2 (N-2 descends, part of Stacks Tag 032K).**
> Let `R` be a Noetherian domain and `R ⊂ S` a finite extension of domains
> (modelled by an injective algebra map `R → S` with `S` finite over `R`).
> If `S` is N-2, then `R` is N-2.

```lean
theorem isN2_of_finite_of_isN2
    (R S : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    [CommRing S] [IsDomain S] [Algebra R S]
    (hinj : Function.Injective (algebraMap R S))
    (hfin : Module.Finite R S)
    (hS : IsN2_032k S) : IsN2_032k R
```

## Tag 032L, a lemma

[Tag 032L](https://stacks.math.columbia.edu/tag/032L) in the Stacks Project.

**`Noetherian_normal_domain_finite_separable_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Basic.lean, line 908](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Basic.lean#L908). References: EGA II (6.3.10), “special case”; EGA II (7.3.12), “special case”; EGA IV (14.5.5), “finiteness of A₁ over A”; EGA IV (18.10.15), “partial”.

> The integral closure of a Noetherian normal domain in a finite separable
> extension is finite over the base ring.

```lean
theorem Noetherian_normal_domain_finite_separable_extension
    (R : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R] [IsIntegrallyClosed R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L] [Algebra.IsSeparable K L]
    [Algebra R L] [IsScalarTower R K L] :
    Module.Finite R (integralClosure R L)
```

## Tag 0AE0, a lemma

[Tag 0AE0](https://stacks.math.columbia.edu/tag/0AE0) in the Stacks Project.

**`Stacks.Nagata.PurelyInseparable.integralClosure_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/PurelyInseparable.lean, line 713](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/PurelyInseparable.lean#L713).

> **Stacks 0AE0.** The integral closure of `R` in `L = K[x]/(x^p - a)` is
> finite over `R`. Given the finitely generated `R`-module `N ⊇ integral closure`
> from `exists_fg_le`, the integral closure is a submodule of the f.g. module `N`
> over the Noetherian ring `R`, hence itself f.g. (`Submodule.FG.of_le`), hence
> finite (`Module.Finite.of_fg`).

```lean
theorem integralClosure_finite
    (h : ∃ D : Derivation ℤ K K,
      (∀ r : R, ∃ s : R, D (algebraMap R K r) = algebraMap R K s) ∧ D a ≠ 0) :
    Module.Finite R (integralClosure R (Lext p a))
```

## Tag 032M, a lemma

[Tag 032M](https://stacks.math.columbia.edu/tag/032M) in the Stacks Project.

**`N1_iff_N2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Basic.lean, line 868](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Basic.lean#L868). References: EGA 0 (23.1.2), “special case”.

> Stacks Tag 032M, Lemma 10.161.11. For a Noetherian domain `R` whose fraction
> field `K` has characteristic zero, `R` is N-1 if and only if `R` is N-2 (Japanese).

```lean
theorem N1_iff_N2 (R K : Type u) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    [Field K] [Algebra R K] [IsFractionRing R K] [CharZero K] :
    IsN1_032m R K ↔ IsN2_032m R K
```

## Tag 032N, a lemma

[Tag 032N](https://stacks.math.columbia.edu/tag/032N) in the Stacks Project.

**`isJapaneseRing_iff_finite_integralClosure_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/JapaneseCriteria.lean#L380). References: EGA 0 (23.1.2).

> **N-2 is tested on purely inseparable extensions.** Stacks Tag 032N: a Noetherian domain `R`
> is N-2 if and only if the integral closure of `R` in every finite purely inseparable extension of
> its field of fractions is a finite `R`-module.
>
> The source states this for a field of fractions of characteristic `p > 0`; the characteristic
> plays no role in the argument, which factors a finite normal extension of `K` as a purely
> inseparable extension followed by a separable one (Tag 030M) and is vacuously about `L = K` in
> characteristic zero, so no characteristic hypothesis is imposed.

```lean
theorem isJapaneseRing_iff_finite_integralClosure_isPurelyInseparable (R : Type u) [CommRing R]
    [IsDomain R] [IsNoetherianRing R] :
    IsJapaneseRing R ↔
      ∀ (L : Type u) [Field L] [Algebra R L] [Algebra (FractionRing R) L]
        [IsScalarTower R (FractionRing R) L] [FiniteDimensional (FractionRing R) L]
        [IsPurelyInseparable (FractionRing R) L],
        Module.Finite R (integralClosure R L)
```

## Tag 032O, a lemma

[Tag 032O](https://stacks.math.columbia.edu/tag/032O) in the Stacks Project.

**`Polynomial.isN1_and_isJapaneseRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Polynomial.lean, line 687](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Polynomial.lean#L687).

> **N-1 and N-2 ascend to a polynomial ring.** Let `R` be a domain. If the integral closure of
> `R` in `Frac(R)` is a finite `R`-module, then the integral closure of `R[x]` in `Frac(R[x])` is a
> finite `R[x]`-module; and if `R` is Noetherian and N-2 (Japanese), then `R[x]` is N-2.
>
> The Noetherian hypothesis of Tag 032O is attached to the N-2 conjunct only, the N-1 conjunct not
> using it; see the module docstring.

```lean
public theorem Polynomial.isN1_and_isJapaneseRing (R : Type u) [CommRing R] [IsDomain R] :
    (IsN1 R → IsN1 (Polynomial R)) ∧
      (IsNoetherianRing R → IsJapaneseRing R → IsJapaneseRing (Polynomial R))
```

## Tag 0332, a lemma

[Tag 0332](https://stacks.math.columbia.edu/tag/0332) in the Stacks Project.

**`PrimeSpectrum.isOpen_setOf_isIntegrallyClosed_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NormalLocus/Open.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NormalLocus/Open.lean#L558). The attribute's comment: “Normality of a localization is spelled `IsIntegrallyClosed`, Mathlib having no predicate for a normal ring; the `IsDomain` conjunct of the spelling used for tags 030C (1) and 031S is automatic here because `R` is a domain. `R_f` is the canonical model `Localization.Away f`. See the module docstring.”.

> **Stacks Tag 0332.** Let `R` be a Noetherian domain. If there is a nonzero `f ∈ R` such that
> `R_f` is normal, then the set of primes `𝔭` of `R` with `R_𝔭` a normal domain is open in
> `Spec(R)`.

```lean
public theorem PrimeSpectrum.isOpen_setOf_isIntegrallyClosed_atPrime
    {R : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R] {f : R} (hf : f ≠ 0)
    (hf' : IsIntegrallyClosed (Localization.Away f)) :
    IsOpen {p : PrimeSpectrum R | IsIntegrallyClosed (Localization.AtPrime p.asIdeal)}
```

## Tag 0333, a lemma

[Tag 0333](https://stacks.math.columbia.edu/tag/0333) in the Stacks Project.

**`isN1_iff_exists_isIntegrallyClosed_away_and_forall_isN1_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/N1.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/N1.lean#L476). The attribute's comment: “`R_f` normal is `IsIntegrallyClosed (Localization.Away f)`, normality of a domain being integral closedness in its field of fractions; the localizations are the concrete models `Localization.Away f` and `Localization.AtPrime 𝔪`. See the module docstring.”.

> A Noetherian domain `R` is **N-1** — its integral closure in `Frac R` is a finite `R`-module —
> if and only if `R_f` is normal for some nonzero `f ∈ R` and `R_𝔪` is N-1 for every maximal ideal
> `𝔪 ⊆ R`.
>
> Normality of the domain `R_f` is `IsIntegrallyClosed (Localization.Away f)`; see the module
> docstring.

```lean
public theorem isN1_iff_exists_isIntegrallyClosed_away_and_forall_isN1_atPrime
    (R : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R] :
    IsN1 R ↔
      (∃ f : R, f ≠ 0 ∧ IsIntegrallyClosed (Localization.Away f)) ∧
        ∀ (𝔪 : Ideal R) [𝔪.IsMaximal], IsN1 (Localization.AtPrime 𝔪)
```

## Tag 032P, a lemma

[Tag 032P](https://stacks.math.columbia.edu/tag/032P) in the Stacks Project.

**`IsJapaneseRing.of_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Tate.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Tate.lean#L623). References: EGA 0 (23.1.3).

> **Tate's theorem.** Let `R` be a Noetherian integrally closed (i.e. normal) domain and let
> `x ∈ R` generate a prime ideal, so that `R ⧸ xR` is a domain. If `R ⧸ xR` is N-2 (Japanese) and
> `R` is `x`-adically complete, then `R` is N-2.
>
> Completeness is asked for as `IsPrecomplete (Ideal.span {x}) R`; the Hausdorff half of
> `IsAdicComplete` is automatic here, see the module docstring.

```lean
public theorem IsJapaneseRing.of_quotient_span_singleton {R : Type u} [CommRing R] [IsDomain R]
    [IsNoetherianRing R] [IsIntegrallyClosed R] (x : R) [(Ideal.span {x}).IsPrime]
    [IsPrecomplete (Ideal.span {x}) R] (h : IsJapaneseRing (R ⧸ Ideal.span {x})) :
    IsJapaneseRing R
```

## Tag 032Q, a lemma

[Tag 032Q](https://stacks.math.columbia.edu/tag/032Q) in the Stacks Project.

**`PowerSeries.isJapaneseRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/PowerSeries.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/PowerSeries.lean#L261). References: EGA 0 (23.1.4), “case r = 1”.

> **Tag 032Q.** If `R` is a Noetherian N-2 (Japanese) domain, then so is the formal power
> series ring `R⟦X⟧`: the integral closure of `R⟦X⟧` in every finite extension of `Frac R⟦X⟧` is
> a finite `R⟦X⟧`-module.
>
> Together with `PowerSeries.instIsNoetherianRing` and `PowerSeries.instIsDomain` this says that
> `R⟦X⟧` is a Noetherian N-2 domain.

```lean
public theorem isJapaneseRing {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    (hR : IsJapaneseRing R) : IsJapaneseRing R⟦X⟧
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.161, Tag 0BI1](https://stacks.math.columbia.edu/tag/0BI1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
