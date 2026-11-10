---
declaration: section
origin: cited
lean: RingHom.Etale.ringKrullDim_localization_atPrime_eq, isNoetherianRing_localization_iff_of_etale, isRegularLocalRing_localization_iff_of_etale, exists_ringEquiv_pi_isDedekindDomain_and_isDiscreteValuationRing_atPrime_of_etale, isNoetherianRing_localization_iff_of_flat_of_finiteType
statement: formalized
proof: formalized
---

# 15.45 Permanence of properties under étale maps

Section 15.45 of the Stacks Project, [Tag 0AGY](https://stacks.math.columbia.edu/tag/0AGY). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AGY, the section

[Tag 0AGY](https://stacks.math.columbia.edu/tag/0AGY) in the Stacks Project.

**`RingHom.Etale.ringKrullDim_localization_atPrime_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Height.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Height.lean#L95). The tag is given by the `attribute` command at [StacksFrontier/RingTheory/Etale/Height.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Height.lean#L103). The attribute's comment: “Lemma 07QP of the section: for an étale ring map `A → B` and a prime `𝔮 ⊂ B` lying over `𝔭 ⊂ A`, `dim A_𝔭 = dim B_𝔮`.”. References: EGA IV (17.6.4), “affine/ring case”; EGA IV (6.1.3), “special case”.

> Stacks Tag 07QP. For an étale ring map `f : A →+* B`, if `q` is a prime of `B` lying over the
> prime `p` of `A`, then the Krull dimensions of the localizations `A_p` and `B_q` agree.

```lean
theorem RingHom.Etale.ringKrullDim_localization_atPrime_eq {A B : Type*} [CommRing A] [CommRing B]
    {f : A →+* B} (hf : f.Etale) (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime]
    (hlo : p = q.comap f) :
    ringKrullDim (Localization.AtPrime p) = ringKrullDim (Localization.AtPrime q)
```

**`isNoetherianRing_localization_iff_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L100). The attribute's comment: “Lemma 0AGZ of the section: for an étale ring map `A → B` and a prime `𝔮 ⊂ B` lying over `𝔭 ⊂ A`, `A_𝔭` is Noetherian if and only if `B_𝔮` is.”.

> For an étale map, the local rings at primes lying over one another are Noetherian
> simultaneously.

```lean
public lemma isNoetherianRing_localization_iff_of_etale
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p] :
    IsNoetherianRing (Localization.AtPrime p) ↔
      IsNoetherianRing (Localization.AtPrime q)
```

**`isRegularLocalRing_localization_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L132). The tag is given by the `attribute` command at [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L161). The attribute's comment: “Lemma 0AH0 of the section: for an étale ring map `A → B` and a prime `𝔮 ⊂ B` lying over `𝔭 ⊂ A`, `A_𝔭` is regular if and only if `B_𝔮` is.”.

> Local rings at corresponding primes under an étale ring map are regular simultaneously.

```lean
public theorem isRegularLocalRing_localization_iff_of_etale
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p] :
    IsRegularLocalRing (Localization.AtPrime p) ↔
      IsRegularLocalRing (Localization.AtPrime q)
```

**`exists_ringEquiv_pi_isDedekindDomain_and_isDiscreteValuationRing_atPrime_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L277). The tag is given by the `attribute` command at [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L288). The attribute's comment: “Lemma 0AP2 of the section, its localization clause in corrected form: an étale algebra `B` over a Dedekind domain `A` is a finite product of Dedekind domains, and `B_𝔮` is a discrete valuation ring for every maximal ideal `𝔮 ⊂ B` with `𝔮 ∩ A ≠ (0)`. As written the clause asserts this for every maximal ideal, which is false: at a prime over `(0)` the local ring has dimension `0` by Lemma 07QP, see `not_isDiscreteValuationRing_localization_of_etale_of_comap_eq_bot` and the instance `not_forall_isDiscreteValuationRing_localization_rat` for the étale map `ℚ → ℚ`. The source's proof, through Lemmas 07QP, 0AH0 and Algebra 00PD, establishes the corrected clause.”.

> An étale algebra over a Dedekind domain is a finite product of Dedekind domains, and its
> localizations at maximal ideals with nonzero contraction to the base are discrete valuation
> rings.

```lean
public theorem exists_ringEquiv_pi_isDedekindDomain_and_isDiscreteValuationRing_atPrime_of_etale
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
    [IsDedekindDomain A] :
    (∃ (n : ℕ) (D : Fin n → Type v) (_ : ∀ i, CommRing (D i)),
      (∀ i, IsDedekindDomain (D i)) ∧ Nonempty (B ≃+* ∀ i, D i)) ∧
      ∀ q : MaximalSpectrum B, q.asIdeal.comap (algebraMap A B) ≠ ⊥ →
        ∃ _ : IsDomain (Localization.AtPrime q.asIdeal),
          IsDiscreteValuationRing (Localization.AtPrime q.asIdeal)
```

## Tag 0AGZ, a lemma

[Tag 0AGZ](https://stacks.math.columbia.edu/tag/0AGZ) in the Stacks Project.

**`isNoetherianRing_localization_iff_of_flat_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L67).

> For a flat finite type map, the local rings at primes lying over one another are Noetherian
> simultaneously.

```lean
public theorem isNoetherianRing_localization_iff_of_flat_of_finiteType
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [Module.Flat A B] [Algebra.FiniteType A B]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p] :
    IsNoetherianRing (Localization.AtPrime p) ↔
      IsNoetherianRing (Localization.AtPrime q)
```

## Tag 07QP, a lemma

[Tag 07QP](https://stacks.math.columbia.edu/tag/07QP) in the Stacks Project.

**`RingHom.Etale.ringKrullDim_localization_atPrime_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Height.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/Height.lean#L95). References: EGA IV (17.6.4), “affine/ring case”; EGA IV (6.1.3), “special case”.

> Stacks Tag 07QP. For an étale ring map `f : A →+* B`, if `q` is a prime of `B` lying over the
> prime `p` of `A`, then the Krull dimensions of the localizations `A_p` and `B_q` agree.

```lean
theorem RingHom.Etale.ringKrullDim_localization_atPrime_eq {A B : Type*} [CommRing A] [CommRing B]
    {f : A →+* B} (hf : f.Etale) (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime]
    (hlo : p = q.comap f) :
    ringKrullDim (Localization.AtPrime p) = ringKrullDim (Localization.AtPrime q)
```

## Tag 0AH0, a lemma

[Tag 0AH0](https://stacks.math.columbia.edu/tag/0AH0) in the Stacks Project.

**`isRegularLocalRing_localization_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L132).

> Local rings at corresponding primes under an étale ring map are regular simultaneously.

```lean
public theorem isRegularLocalRing_localization_iff_of_etale
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p] :
    IsRegularLocalRing (Localization.AtPrime p) ↔
      IsRegularLocalRing (Localization.AtPrime q)
```

## Tag 0AP2, a lemma

[Tag 0AP2](https://stacks.math.columbia.edu/tag/0AP2) in the Stacks Project.

**`exists_ringEquiv_pi_isDedekindDomain_and_isDiscreteValuationRing_atPrime_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/PermanenceOfProperties.lean#L277).

> An étale algebra over a Dedekind domain is a finite product of Dedekind domains, and its
> localizations at maximal ideals with nonzero contraction to the base are discrete valuation
> rings.

```lean
public theorem exists_ringEquiv_pi_isDedekindDomain_and_isDiscreteValuationRing_atPrime_of_etale
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
    [IsDedekindDomain A] :
    (∃ (n : ℕ) (D : Fin n → Type v) (_ : ∀ i, CommRing (D i)),
      (∀ i, IsDedekindDomain (D i)) ∧ Nonempty (B ≃+* ∀ i, D i)) ∧
      ∀ q : MaximalSpectrum B, q.asIdeal.comap (algebraMap A B) ≠ ⊥ →
        ∃ _ : IsDomain (Localization.AtPrime q.asIdeal),
          IsDiscreteValuationRing (Localization.AtPrime q.asIdeal)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.45, Tag 0AGY](https://stacks.math.columbia.edu/tag/0AGY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
