---
declaration: section
origin: cited
lean: descent_noetherian, RingHom.FaithfullyFlat.isReduced, isDomain_and_isIntegrallyClosed_atPrime_of_faithfullyFlat, IsRegularRing.of_faithfullyFlat, isNoetherianRing_and_min_le_depth_atPrime_of_faithfullyFlat, isNoetherianRing_and_isRegularLocalRing_atPrime_of_faithfullyFlat, IsNagataRing.of_smooth_of_comap_surjective
statement: formalized
proof: formalized
---

# 10.164 Descending properties

Section 10.164 of the Stacks Project, [Tag 033D](https://stacks.math.columbia.edu/tag/033D). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 033E, a lemma

[Tag 033E](https://stacks.math.columbia.edu/tag/033E) in the Stacks Project.

**`descent_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L300). References: EGA 0 (6.5.2), “special case”; EGA IV (2.2.14), “affine source and target”.

> **Stacks 033E**. If `φ : R → S` is faithfully flat and `S` is Noetherian, then `R` is
> Noetherian.

```lean
theorem descent_noetherian {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (hφ : φ.FaithfullyFlat) (hS : IsNoetherianRing S) : IsNoetherianRing R
```

## Tag 033F, a lemma

[Tag 033F](https://stacks.math.columbia.edu/tag/033F) in the Stacks Project.

**`RingHom.FaithfullyFlat.isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L309). References: EGA IV (11.3.13), “(i), reduced case”.

> **Stacks 033F**. If `φ : R → S` is a faithfully flat ring map and `S` is reduced,
> then `R` is reduced.

```lean
theorem RingHom.FaithfullyFlat.isReduced {R S : Type*} [CommRing R] [CommRing S] {φ : R →+* S}
    (hφ : φ.FaithfullyFlat) [IsReduced S] : IsReduced R
```

## Tag 033G, a lemma

[Tag 033G](https://stacks.math.columbia.edu/tag/033G) in the Stacks Project.

**`isDomain_and_isIntegrallyClosed_atPrime_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegrallyClosed/FaithfullyFlatDescent.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegrallyClosed/FaithfullyFlatDescent.lean#L232). The attribute's comment: “Normality is inlined as `IsDomain` plus `IsIntegrallyClosed` on `Localization.AtPrime 𝔭` for every prime `𝔭`, as in item (1) of tag 030C and in tag 031S, Mathlib having no predicate for a normal ring; the ring map `R → S` is an `Algebra R S` instance and its faithful flatness is `Module.FaithfullyFlat R S`. See the module docstring.”. References: EGA IV (6.5.4), “(i), affine case”; EGA IV (2.1.13), “special case”; EGA IV (7.5.3), “(vi)”.

> **Stacks 033G.** Let `R → S` be a faithfully flat ring map. If `S` is a normal ring, i.e. all
> its localizations at primes are normal domains, then so is `R`.

```lean
public theorem isDomain_and_isIntegrallyClosed_atPrime_of_faithfullyFlat {R : Type*} [CommRing R]
    {S : Type*} [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S]
    (hS : ∀ (q : Ideal S) [q.IsPrime],
      IsDomain (Localization.AtPrime q) ∧ IsIntegrallyClosed (Localization.AtPrime q)) :
    ∀ (p : Ideal R) [p.IsPrime],
      IsDomain (Localization.AtPrime p) ∧ IsIntegrallyClosed (Localization.AtPrime p)
```

## Tag 07NG, a lemma

[Tag 07NG](https://stacks.math.columbia.edu/tag/07NG) in the Stacks Project.

**`IsRegularRing.of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularRing/FaithfullyFlatDescent.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularRing/FaithfullyFlatDescent.lean#L173). The attribute's comment: “The source's "regular ring" is Mathlib's class `IsRegularRing` (Definition 00OD), which already includes Noetherianness, so the Noetherianness of `R` that the source derives from Lemma 033E is part of the conclusion; the ring map `R → S` is an `Algebra R S` instance and its faithful flatness is `Module.FaithfullyFlat R S`, equal to `(algebraMap R S).FaithfullyFlat` by `RingHom.faithfullyFlat_algebraMap_iff`. See the module docstring.”.

> **Regularity descends along a faithfully flat ring map** (Stacks 07NG). Let `R → S` be a ring
> map. If it is faithfully flat and `S` is a regular ring, then `R` is a regular ring.

```lean
public theorem IsRegularRing.of_faithfullyFlat {R : Type u} (S : Type v) [CommRing R] [CommRing S]
    [Algebra R S] [Module.FaithfullyFlat R S] [IsRegularRing S] : IsRegularRing R
```

## Tag 0352, a lemma

[Tag 0352](https://stacks.math.columbia.edu/tag/0352) in the Stacks Project.

**`isNoetherianRing_and_min_le_depth_atPrime_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/FaithfullyFlatDescent.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/FaithfullyFlatDescent.lean#L332). The attribute's comment: “Property `(S_k)` is spelled out from Definition 031P as the inequality `min{k, dim(R_𝔭)} ≤ depth(R_𝔭)` at every prime, with `Module.depth` (tag 00LI) along the maximal ideal of `Localization.AtPrime 𝔭` and `ringKrullDim` for the dimension, as in tags 031Q and 031S, the inequality being read in `WithBot ℕ∞`; the ring map `R → S` is an `Algebra R S` instance and its faithful flatness is `Module.FaithfullyFlat R S`. See the module docstring.”. References: EGA IV (6.4.1), “(i), affine E=O,F=O”.

> **Stacks Tag 0352.** Let `R → S` be a ring map. If it is faithfully flat and `S` is Noetherian
> with property `(S_k)` — the depth of `S_𝔮` is at least `min{k, dim(S_𝔮)}` for every prime `𝔮` —
> then `R` is Noetherian and has property `(S_k)`. The depth inequalities are read in
> `WithBot ℕ∞`.

```lean
public theorem isNoetherianRing_and_min_le_depth_atPrime_of_faithfullyFlat
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Module.FaithfullyFlat R S] [IsNoetherianRing S] {k : ℕ}
    (hS : ∀ (q : Ideal S) [q.IsPrime],
      min (k : WithBot ℕ∞) (ringKrullDim (Localization.AtPrime q)) ≤
        (Module.depth (Localization.AtPrime q)
          (IsLocalRing.maximalIdeal (Localization.AtPrime q)) (Localization.AtPrime q) :
            WithBot ℕ∞)) :
    IsNoetherianRing R ∧
      ∀ (p : Ideal R) [p.IsPrime],
        min (k : WithBot ℕ∞) (ringKrullDim (Localization.AtPrime p)) ≤
          (Module.depth (Localization.AtPrime p)
            (IsLocalRing.maximalIdeal (Localization.AtPrime p)) (Localization.AtPrime p) :
              WithBot ℕ∞)
```

## Tag 0353, a lemma

[Tag 0353](https://stacks.math.columbia.edu/tag/0353) in the Stacks Project.

**`isNoetherianRing_and_isRegularLocalRing_atPrime_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/FaithfullyFlatDescent.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/FaithfullyFlatDescent.lean#L544). The attribute's comment: “Property `(R_k)` is spelled out from Definition 031P as the implication `height 𝔭 ≤ k → IsRegularLocalRing (Localization.AtPrime 𝔭)`, with `Ideal.height` and `IsRegularLocalRing`, as in tag 031S; the source's `dim(R_𝔭) ≤ k` is `Ideal.height 𝔭 ≤ k` by `IsLocalization.AtPrime.ringKrullDim_eq_height`. The bound `k` is generalized from a non-negative integer to an element of `ℕ∞`, whose top value recovers tag 07NG. The ring map `R → S` is an `Algebra R S` instance and its faithful flatness is `Module.FaithfullyFlat R S`. See the module docstring.”. References: EGA IV (6.5.3), “(i), affine case”.

> **Stacks Tag 0353.** Let `R → S` be a ring map. If it is faithfully flat and `S` is Noetherian
> with property `(R_k)` — the local ring `S_𝔮` is regular for every prime `𝔮` of height at most `k`
> — then `R` is Noetherian and has property `(R_k)`. The bound `k` ranges over `ℕ∞`, the value `⊤`
> giving the descent of regularity itself (tag 07NG).

```lean
public theorem isNoetherianRing_and_isRegularLocalRing_atPrime_of_faithfullyFlat
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Module.FaithfullyFlat R S] [IsNoetherianRing S] {k : ℕ∞}
    (hS : ∀ (q : Ideal S) [q.IsPrime], q.height ≤ k →
      IsRegularLocalRing (Localization.AtPrime q)) :
    IsNoetherianRing R ∧
      ∀ (p : Ideal R) [p.IsPrime], p.height ≤ k →
        IsRegularLocalRing (Localization.AtPrime p)
```

## Tag 0354, a lemma

[Tag 0354](https://stacks.math.columbia.edu/tag/0354) in the Stacks Project.

**`IsNagataRing.of_smooth_of_comap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/SmoothDescent.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/SmoothDescent.lean#L266). The attribute's comment: “Smoothness of the ring map `R → S` is `Algebra.Smooth R S` (Definition 00T2) for an `Algebra R S` instance, and surjectivity on spectra is surjectivity of `PrimeSpectrum.comap (algebraMap R S)`; the pair is equivalent to smooth plus `Module.FaithfullyFlat R S`. Nagata is `IsNagataRing` of Definition 032R(2), whose Noetherian clause is part of the conclusion rather than a hypothesis on `R`. See the module docstring.”.

> **Stacks Tag 0354.** Let `R → S` be a ring map. If it is smooth and the induced map
> `Spec S → Spec R` is surjective, and `S` is a Nagata ring — Noetherian, with every quotient
> `S ⧸ q` by a prime N-2 — then `R` is a Nagata ring.
>
> Smoothness is `Algebra.Smooth` (Definition 00T2), and together with surjectivity on spectra it is
> equivalent to `R → S` being smooth and faithfully flat, by `Algebra.Smooth.flat` and
> `Module.FaithfullyFlat.of_comap_surjective`.

```lean
public theorem IsNagataRing.of_smooth_of_comap_surjective {R S : Type u} [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.Smooth R S]
    (hsurj : Function.Surjective (PrimeSpectrum.comap (algebraMap R S)))
    (hS : IsNagataRing S) : IsNagataRing R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.164, Tag 033D](https://stacks.math.columbia.edu/tag/033D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
