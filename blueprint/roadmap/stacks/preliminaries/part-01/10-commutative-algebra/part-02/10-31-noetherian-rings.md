---
declaration: section
origin: cited
lean: Algebra.FiniteType.isNoetherianRing, IsLocalization.isNoetherianRing, mvPowerSeries_fin_isNoetherianRing, Module.finitePresentation_of_finite, Submodule.FG.of_le, Algebra.FinitePresentation.of_finiteType, PrimeSpectrum.instNoetherianSpace, minimalPrimes.finite_of_isNoetherianRing
statement: formalized
proof: formalized
---

# 10.31 Noetherian rings

Section 10.31 of the Stacks Project, [Tag 00FM](https://stacks.math.columbia.edu/tag/00FM). 10 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00FN, a lemma

[Tag 00FN](https://stacks.math.columbia.edu/tag/00FN) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FiniteType.isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FiniteType.isNoetherianRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Spec.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Spec.lean#L54) (StacksFrontier): “(1)”. References: EGA 0 (22.3.1), “Noetherianity of A”; EGA 0 (23.2.5), “Noetherian clause”; EGA II (2.1.5), “sufficiency”; EGA IV (1.4.1), “more general”; EGA IV (1.5.3), “affine case”; SGA 3 VIB (10.10), “more general”; SGA 5 V (5.1.4), “special case”.
- [`IsLocalization.isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.isNoetherianRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Spec.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Spec.lean#L64) (StacksFrontier): “(2)”. References: EGA 0 (10.3.1.1), “B is Noetherian”.

## Tag 0306, a lemma

[Tag 0306](https://stacks.math.columbia.edu/tag/0306) in the Stacks Project.

**`mvPowerSeries_fin_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPowerSeries/Noetherian.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MvPowerSeries/Noetherian.lean#L165).

> The formal power series ring in `n` variables over a Noetherian commutative ring is
> Noetherian.

```lean
theorem mvPowerSeries_fin_isNoetherianRing
    (R : Type*) [CommRing R] [IsNoetherianRing R] (n : ℕ) :
    IsNoetherianRing (MvPowerSeries (Fin n) R)
```

## Tag 00FO, a lemma

[Tag 00FO](https://stacks.math.columbia.edu/tag/00FO) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FiniteType.isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FiniteType.isNoetherianRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L138) (StacksFrontier): “over any Noetherian base; fields and ℤ are Noetherian”. References: EGA 0 (22.3.1), “Noetherianity of A”; EGA 0 (23.2.5), “Noetherian clause”; EGA II (2.1.5), “sufficiency”; EGA IV (1.4.1), “more general”; EGA IV (1.5.3), “affine case”; SGA 3 VIB (10.10), “more general”; SGA 5 V (5.1.4), “special case”.

## Tag 00FP, a lemma

[Tag 00FP](https://stacks.math.columbia.edu/tag/00FP) in the Stacks Project.

Declarations registered for the tag:

- [`Module.finitePresentation_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finitePresentation_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L141) (StacksFrontier): “(1) finite modules are finitely presented”. References: EGA 0 (1.0.5), “more general”; EGA 0 (1.3.5), “more general”.
- [`Submodule.FG.of_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.FG.of_le#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L142) (StacksFrontier): “(2) submodules of finite modules are finite”.
- [`Algebra.FinitePresentation.of_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.of_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L143) (StacksFrontier): “(3) finite type algebras are finitely presented”. References: EGA IV (1.4.1); SGA 1 IX (4.7), “special case”; SGA 1 IX (4.10), “affine Noetherian base”; SGA 3 V (6.1), “affine case”.

## Tag 00FQ, a lemma

[Tag 00FQ](https://stacks.math.columbia.edu/tag/00FQ) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.instNoetherianSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.instNoetherianSpace#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Spec.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Spec.lean#L68) (StacksFrontier). References: EGA I (1.1.6).

## Tag 00FR, a lemma

[Tag 00FR](https://stacks.math.columbia.edu/tag/00FR) in the Stacks Project.

Declarations registered for the tag:

- [`minimalPrimes.finite_of_isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=minimalPrimes.finite_of_isNoetherianRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Spec.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Spec.lean#L75) (StacksFrontier). References: EGA 0 (1.1.1), “Minimal primes over (0)”; EGA 0 (2.2.5), “affine case”; EGA 0 (2.2.5), “ring-theoretic form”.

## Tag 0CY6, a lemma

[Tag 0CY6](https://stacks.math.columbia.edu/tag/0CY6) in the Stacks Project.

**`noetherian_base_change_finite_type`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/Spec.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Spec.lean#L100). References: EGA I (6.3.8), “affine case”; EGA IV (1.5.5), “affine case”; EGA I (10.13.5), “(ii)”; EGA I (6.6.7), “affine case”; EGA II (2.1.5), “sufficiency”; EGA IV (1.3.5), “affine schemes”; EGA IV (6.7.1.1), “special case”; SGA 1 III (1.4), “partial”; SGA 5 V (5.1.4), “special case”; SGA 5 V (5.1.5), “special case”; SGA 6 X (7.15), “special case”; SGA 6 X (7.17), “special case”.

> If `R → R'` is of finite type and `S` is a Noetherian `R`-algebra, then
> the base change `R' ⊗[R] S` is a Noetherian ring.
>
> The proof transports the result along the commutativity isomorphism
> `S ⊗[R] R' ≃ R' ⊗[R] S`, after observing that base change preserves
> finite type and applying the Hilbert basis theorem.

```lean
theorem noetherian_base_change_finite_type
    (R R' S : Type*) [CommRing R] [CommRing R'] [CommRing S]
    [Algebra R R'] [Algebra R S]
    [Algebra.FiniteType R R'] [IsNoetherianRing S] :
    IsNoetherianRing (TensorProduct R R' S)
```

## Tag 045I, a lemma

[Tag 045I](https://stacks.math.columbia.edu/tag/045I) in the Stacks Project.

**`tensorProduct_isNoetherianRing_of_finitelyGenerated_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/TensorProduct.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/TensorProduct.lean#L73). References: EGA IV (4.7.3), “(i), special case”; EGA IV (6.7.1), “Affine X, special case”; EGA IV (6.7.1.1), “more general”; SGA 1 III (1.4), “special case”; SGA 5 V (5.1.5), “special case”.

> **Stacks Tag 045I.** Let `k` be a field and `R` a Noetherian commutative
> `k`-algebra. If `K/k` is a finitely generated field extension (finitely
> generated *as a field*, expressed by `(⊤ : IntermediateField k K).FG`), then the
> `k`-algebra `K ⊗[k] R` is Noetherian.

```lean
theorem tensorProduct_isNoetherianRing_of_finitelyGenerated_fieldExtension
    (k : Type*) [Field k]
    (R : Type*) [CommRing R] [Algebra k R] [IsNoetherianRing R]
    (K : Type*) [Field K] [Algebra k K]
    (hK : (⊤ : IntermediateField k K).FG) :
    IsNoetherianRing (K ⊗[k] R)
```

## Tag 0BX1, a lemma

[Tag 0BX1](https://stacks.math.columbia.edu/tag/0BX1) in the Stacks Project.

**`exists_injective_localizationAwayToAtPrime_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean#L93). The attribute's comment: “(1)”.

> Case (1): `R` an integral domain. There exists `f ∉ p` such that the
> canonical map `R_f → R_p` is injective. (One may take `f = 1`.)

```lean
theorem exists_injective_localizationAwayToAtPrime_of_isDomain
    {R : Type*} [CommRing R] [IsDomain R] (p : Ideal R) [p.IsPrime] :
    ∃ f : R, ∃ hf : f ∉ p, Function.Injective (localizationAwayToAtPrime f p hf)
```

**`exists_injective_localizationAwayToAtPrime_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean#L103). The attribute's comment: “(2)”.

> Case (2): `R` Noetherian. There exists `f ∉ p` such that the canonical
> map `R_f → R_p` is injective.

```lean
theorem exists_injective_localizationAwayToAtPrime_of_isNoetherianRing
    {R : Type*} [CommRing R] [IsNoetherianRing R] (p : Ideal R) [p.IsPrime] :
    ∃ f : R, ∃ hf : f ∉ p, Function.Injective (localizationAwayToAtPrime f p hf)
```

**`exists_injective_localizationAwayToAtPrime_of_isReduced_finite_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/AwayToAtPrime.lean#L135). The attribute's comment: “(3)”.

> Case (3): `R` reduced with finitely many minimal primes not contained in `p`.
> There exists `f ∉ p` such that the canonical map `R_f → R_p` is injective.
>
> The hypothesis is weaker than the `(minimalPrimes R).Finite` of 0BX1 (3), which
> implies it by `Set.Finite.subset _ (Set.sep_subset _ _)`.

```lean
theorem exists_injective_localizationAwayToAtPrime_of_isReduced_finite_minimalPrimes
    {R : Type*} [CommRing R] [IsReduced R] (p : Ideal R) [p.IsPrime]
    (hfin : {q ∈ minimalPrimes R | ¬ q ≤ p}.Finite) :
    ∃ f : R, ∃ hf : f ∉ p, Function.Injective (localizationAwayToAtPrime f p hf)
```

## Tag 06RN, a lemma

[Tag 06RN](https://stacks.math.columbia.edu/tag/06RN) in the Stacks Project.

**`surjective_endomorphism_noetherian_isomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/Endomorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Endomorphism.lean#L68).

> The bijective endomorphism above is genuinely a ring isomorphism: there is a
> `RingEquiv` `e : R ≃+* R` that agrees with `φ` on every element.

```lean
theorem surjective_endomorphism_noetherian_isomorphism
    (R : Type*) [CommRing R] [IsNoetherianRing R] (φ : R →+* R)
    (hφ : Function.Surjective φ) : ∃ e : R ≃+* R, ∀ x, e x = φ x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.31, Tag 00FM](https://stacks.math.columbia.edu/tag/00FM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
