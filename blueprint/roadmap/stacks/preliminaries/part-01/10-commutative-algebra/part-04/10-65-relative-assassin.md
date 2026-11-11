---
declaration: section
origin: cited
lean: Module.relativeAssassin_comparison, Module.relativeAssassin, associatedPrimes.tensorProduct_of_flat, Stacks.AssociatedPrimes.Localization.associatedPrimes_chain, associatedPrimes.tensorProduct_of_flat_fiberRing
statement: formalized
proof: formalized
---

# 10.65 Relative assassin

Section 10.65 of the Stacks Project, [Tag 05GA](https://stacks.math.columbia.edu/tag/05GA). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05GB, a lemma

[Tag 05GB](https://stacks.math.columbia.edu/tag/05GB) in the Stacks Project.

**`Module.relativeAssassin_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelativeAssassin.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RelativeAssassin.lean#L842).

> Let `R → S` be a ring map, let `N` be an `S`-module, and let `A`, `A'`, `A_fin`, `A'_fin`, `B`,
> `B_fin` be the six sets of primes of `S` attached to this data: with `𝔭 = R ∩ 𝔮`, the primes `𝔮`
> associated to `N ⊗_R κ(𝔭)` over `S`, those in the image of the primes associated to `N ⊗_R κ(𝔭)`
> over the fibre ring `S ⊗_R κ(𝔭)`, those associated to `N / 𝔭N`, those associated to `N / 𝔭'N` for
> some prime `𝔭'` of `R`, those associated to `N ⊗_R M` for some `R`-module `M`, and those associated
> to `N ⊗_R M` for some finite `R`-module `M`. Then (1) `A = A'`; (2) `A_fin ⊆ A`, `B_fin ⊆ B`,
> `A_fin ⊆ A'_fin ⊆ B_fin` and `A ⊆ B`; (3) if `S` is Noetherian then `A = A_fin` and `B = B_fin`;
> (4) if `N` is flat over `R` then `A = A_fin = A'_fin` and `B = B_fin`; (5) if `R` is Noetherian and
> `N` is flat over `R` then all six sets are equal.

```lean
public theorem relativeAssassin_comparison (R : Type u) (S : Type v) [CommRing R] [CommRing S]
    [Algebra R S] (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    {A A' Afin A'fin B Bfin : Set (PrimeSpectrum S)}
    (hA : A = {q | q.asIdeal ∈
      associatedPrimes S (N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)})
    (hA' : A' = {q | ∃ Q : PrimeSpectrum
        (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField),
        Q.asIdeal ∈ associatedPrimes
          (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)
          ((S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) ⊗[S] N) ∧
        PrimeSpectrum.comap (algebraMap S
          (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)) Q = q})
    (hAfin : Afin = {q | q.asIdeal ∈ associatedPrimes S
      (N ⧸ ((PrimeSpectrum.comap (algebraMap R S) q).asIdeal.map (algebraMap R S) •
        (⊤ : Submodule S N)))})
    (hA'fin : A'fin = {q | ∃ p : PrimeSpectrum R, q.asIdeal ∈ associatedPrimes S
      (N ⧸ (p.asIdeal.map (algebraMap R S) • (⊤ : Submodule S N)))})
    (hB : B = {q | ∃ (M : Type (max u v)) (_ : AddCommGroup M) (_ : Module R M),
      q.asIdeal ∈ associatedPrimes S (N ⊗[R] M)})
    (hBfin : Bfin = {q | ∃ (M : Type (max u v)) (_ : AddCommGroup M) (_ : Module R M)
      (_ : Module.Finite R M), q.asIdeal ∈ associatedPrimes S (N ⊗[R] M)}) :
    A = A' ∧
    (Afin ⊆ A ∧ Bfin ⊆ B ∧ Afin ⊆ A'fin ∧ A'fin ⊆ Bfin ∧ A ⊆ B) ∧
    (IsNoetherianRing S → A = Afin ∧ B = Bfin) ∧
    (Module.Flat R N → A = Afin ∧ Afin = A'fin ∧ B = Bfin) ∧
    (IsNoetherianRing R → Module.Flat R N →
      A = A' ∧ A' = Afin ∧ Afin = A'fin ∧ A'fin = Bfin ∧ Bfin = B)
```

## Tag 05GC, a definition

[Tag 05GC](https://stacks.math.columbia.edu/tag/05GC) in the Stacks Project.

**`Module.relativeAssassin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelativeAssassin/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RelativeAssassin/Defs.lean#L100).

> The **relative assassin** `Ass_{S/R}(N)` of an `S`-module `N` over a ring map `R → S`: the
> set of primes `𝔮` of `S` which, with `𝔭 = R ∩ 𝔮` the contraction of `𝔮` to `R`, are associated
> primes over `S` of the fibre module `N ⊗_R κ(𝔭)`, that is, are the annihilator of some element
> of it. This is the set `A` of `Module.relativeAssassin_comparison`.

```lean
public def relativeAssassin : Set (PrimeSpectrum S)
```

## Tag 0312, a lemma

[Tag 0312](https://stacks.math.columbia.edu/tag/0312) in the Stacks Project.

**`associatedPrimes.tensorProduct_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean#L495).

> Let `R → S` be a ring map, let `M` be an `R`-module and let `N` be an `S`-module which is flat
> as an `R`-module. Then `Ass_S(N ⊗_R M) ⊇ ⋃_{𝔭 ∈ Ass_R(M)} Ass_S(N / 𝔭N)`, and if `R` is
> Noetherian this inclusion is an equality. Here `Ass` is the set of primes that *are* the
> annihilator of an element, written out as such, and the index set of the equality is
> `associatedPrimes R M`.

```lean
public theorem associatedPrimes.tensorProduct_of_flat {R S M N : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module S N] [Module R N]
    [IsScalarTower R S N] [Module.Flat R N] :
    (⋃ p ∈ {p : Ideal R | p.IsPrime ∧ ∃ m : M, (⊥ : Submodule R M).colon {m} = p},
        {q : Ideal S | q.IsPrime ∧
          ∃ w : N ⧸ (p.map (algebraMap R S) • (⊤ : Submodule S N)),
            (⊥ : Submodule S (N ⧸ (p.map (algebraMap R S) • (⊤ : Submodule S N)))).colon {w} =
              q}) ⊆
      {q : Ideal S | q.IsPrime ∧ ∃ w : N ⊗[R] M, (⊥ : Submodule S (N ⊗[R] M)).colon {w} = q} ∧
    (IsNoetherianRing R →
      {q : Ideal S | q.IsPrime ∧ ∃ w : N ⊗[R] M, (⊥ : Submodule S (N ⊗[R] M)).colon {w} = q} =
        ⋃ p ∈ associatedPrimes R M,
          {q : Ideal S | q.IsPrime ∧
            ∃ w : N ⧸ (p.map (algebraMap R S) • (⊤ : Submodule S N)),
              (⊥ : Submodule S (N ⧸ (p.map (algebraMap R S) • (⊤ : Submodule S N)))).colon {w} =
                q})
```

## Tag 05C1, a lemma

[Tag 05C1](https://stacks.math.columbia.edu/tag/05C1) in the Stacks Project.

**`Stacks.AssociatedPrimes.Localization.associatedPrimes_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean#L311).

> **Stacks 05C1, combined (abstract).**  Under flatness, via the canonical map
> `Spec(S ⊗_R K) → Spec(S)`, we have
> `Ass_S(N) = Ass_S(N ⊗_R K) = Ass_{S ⊗_R K}(N ⊗_R K)`, where the last equality is read as the
> preimage identity along `Ideal.comap (algebraMap S (S ⊗_R K))`.  All localization data are
> explicit hypotheses.

```lean
theorem associatedPrimes_chain [Module.Flat R N] (μN : N →ₗ[R] NK) (μNₛ : N →ₗ[S] NK)
    (hSK : IsLocalization (Algebra.algebraMapSubmonoid S (nonZeroDivisors R)) SK)
    (hμN : IsLocalizedModule (nonZeroDivisors R) μN)
    (hμNₛ : IsLocalizedModule (Algebra.algebraMapSubmonoid S (nonZeroDivisors R)) μNₛ)
    (hμ : ∀ n, μNₛ n = μN n) :
    associatedPrimes S N = associatedPrimes S NK ∧
      (Ideal.comap (algebraMap S SK)) ⁻¹' (associatedPrimes S NK)
        = associatedPrimes SK NK
```

## Tag 05C2, a lemma

[Tag 05C2](https://stacks.math.columbia.edu/tag/05C2) in the Stacks Project.

**`associatedPrimes.tensorProduct_of_flat_fiberRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatTensorProduct.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatTensorProduct.lean#L420). References: EGA IV (3.3.1), “affine case”; EGA IV (3.3.6), “affine case, X = S”.

> **Stacks Tag 05C2.** Let `R → S` be a ring map, let `M` be an `R`-module and let `N` be an
> `S`-module which is flat as an `R`-module. Viewing `Spec(S ⊗_R κ(𝔭))` as a subset of `Spec(S)`
> (Tag 00E6), we have
> `Ass_S(N ⊗_R M) ⊇ ⋃_{𝔭 ∈ Ass_R(M)} Ass_{S ⊗_R κ(𝔭)}(N ⊗_R κ(𝔭))`,
> and this inclusion is an equality if `R` is Noetherian. Here `Ass_R(M)` is the source's set of
> associated primes of Tag 00LA, the primes that *are* the annihilator of an element of `M`; over a
> Noetherian ring it agrees with Mathlib's `associatedPrimes`, which is how the second assertion
> spells it.

```lean
public theorem associatedPrimes.tensorProduct_of_flat_fiberRing {R S M N : Type*} [CommRing R]
    [CommRing S] [Algebra R S] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module S N]
    [Module R N] [IsScalarTower R S N] [Module.Flat R N] :
    (⋃ p ∈ {p : PrimeSpectrum R | ∃ m : M, (⊥ : Submodule R M).colon {m} = p.asIdeal},
        PrimeSpectrum.comap (algebraMap S (S ⊗[R] p.asIdeal.ResidueField)) ''
          {Q | Q.asIdeal ∈ associatedPrimes (S ⊗[R] p.asIdeal.ResidueField)
            ((S ⊗[R] p.asIdeal.ResidueField) ⊗[S] N)}) ⊆
      {q : PrimeSpectrum S | q.asIdeal ∈ associatedPrimes S (N ⊗[R] M)} ∧
    (IsNoetherianRing R →
      {q : PrimeSpectrum S | q.asIdeal ∈ associatedPrimes S (N ⊗[R] M)} =
        ⋃ p ∈ {p : PrimeSpectrum R | p.asIdeal ∈ associatedPrimes R M},
          PrimeSpectrum.comap (algebraMap S (S ⊗[R] p.asIdeal.ResidueField)) ''
            {Q | Q.asIdeal ∈ associatedPrimes (S ⊗[R] p.asIdeal.ResidueField)
              ((S ⊗[R] p.asIdeal.ResidueField) ⊗[S] N)})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.65, Tag 05GA](https://stacks.math.columbia.edu/tag/05GA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
