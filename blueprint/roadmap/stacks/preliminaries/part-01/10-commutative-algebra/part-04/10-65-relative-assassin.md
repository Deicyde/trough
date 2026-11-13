---
declaration: section
origin: cited
lean: Module.relativeAssassin_comparison_annihilator, Module.relativeAssassin, associatedPrimes.tensorProduct_of_flat, Stacks.AssociatedPrimes.Localization.assPrimes_chain, assStacks_tensorProduct_of_flat_fiberRing
statement: formalized
proof: formalized
---

# 10.65 Relative assassin

Section 10.65 of the Stacks Project, [Tag 05GA](https://stacks.math.columbia.edu/tag/05GA). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05GB, a lemma

[Tag 05GB](https://stacks.math.columbia.edu/tag/05GB) in the Stacks Project.

**`Module.relativeAssassin_comparison_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelativeAssassin.lean, line 1096](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/RelativeAssassin.lean#L1096).

> Let `R → S` be a ring map and let `N` be an `S`-module. A prime `𝔮` of `S` is associated to an
> `S`-module `P` when it is the annihilator of some element of `P`, that is
> `(⊥ : Submodule S P).colon {m} = 𝔮` for some `m : P`. With `𝔭 = R ∩ 𝔮`, let `A` be the set of
> primes `𝔮` associated to `N ⊗_R κ(𝔭)`, `A'` the set of contractions of the primes of the fibre
> ring `S ⊗_R κ(𝔭)` associated to `(S ⊗_R κ(𝔭)) ⊗_S N ≅ N ⊗_R κ(𝔭)` over the fibre ring, `A_fin`
> the set of primes associated to `N / 𝔭N`, `A'_fin` the set of primes associated to `N / 𝔭'N`
> for some prime `𝔭'` of `R`, `B` the set of primes associated to `N ⊗_R M` for some `R`-module
> `M`, and `B_fin` the same with `M` finite. Then (1) `A = A'`; (2) `A_fin ⊆ A`, `B_fin ⊆ B`,
> `A_fin ⊆ A'_fin ⊆ B_fin` and `A ⊆ B`; (3) if `S` is Noetherian then `A = A_fin` and
> `B = B_fin`; (4) if `N` is flat over `R` then `A = A_fin = A'_fin` and `B = B_fin`; (5) if `R`
> is Noetherian and `N` is flat over `R` then all six sets are equal.

```lean
public theorem _root_.Module.relativeAssassin_comparison_annihilator (R : Type u) (S : Type v)
    [CommRing R] [CommRing S] [Algebra R S] (N : Type w) [AddCommGroup N] [Module S N]
    [Module R N] [IsScalarTower R S N] {A A' Afin A'fin B Bfin : Set (PrimeSpectrum S)}
    (hA : A = {q | ∃ m : N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField,
      (⊥ : Submodule S
        (N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)).colon {m} =
        q.asIdeal})
    (hA' : A' = {q | ∃ Q : PrimeSpectrum
        (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField),
        (∃ m : (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) ⊗[S] N,
          (⊥ : Submodule (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)
            ((S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) ⊗[S]
              N)).colon {m} = Q.asIdeal) ∧
        PrimeSpectrum.comap (algebraMap S
          (S ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField)) Q = q})
    (hAfin : Afin = {q | ∃ w : N ⧸ ((PrimeSpectrum.comap (algebraMap R S) q).asIdeal.map
        (algebraMap R S) • (⊤ : Submodule S N)),
      (⊥ : Submodule S (N ⧸ ((PrimeSpectrum.comap (algebraMap R S) q).asIdeal.map
        (algebraMap R S) • (⊤ : Submodule S N)))).colon {w} = q.asIdeal})
    (hA'fin : A'fin = {q | ∃ p : PrimeSpectrum R,
      ∃ w : N ⧸ (p.asIdeal.map (algebraMap R S) • (⊤ : Submodule S N)),
        (⊥ : Submodule S (N ⧸ (p.asIdeal.map (algebraMap R S) • (⊤ : Submodule S N)))).colon
          {w} = q.asIdeal})
    (hB : B = {q | ∃ (M : Type (max u v)) (_ : AddCommGroup M) (_ : Module R M),
      ∃ z : N ⊗[R] M, (⊥ : Submodule S (N ⊗[R] M)).colon {z} = q.asIdeal})
    (hBfin : Bfin = {q | ∃ (M : Type (max u v)) (_ : AddCommGroup M) (_ : Module R M)
      (_ : Module.Finite R M),
      ∃ z : N ⊗[R] M, (⊥ : Submodule S (N ⊗[R] M)).colon {z} = q.asIdeal}) :
    A = A' ∧
    (Afin ⊆ A ∧ Bfin ⊆ B ∧ Afin ⊆ A'fin ∧ A'fin ⊆ Bfin ∧ A ⊆ B) ∧
    (IsNoetherianRing S → A = Afin ∧ B = Bfin) ∧
    (Module.Flat R N → A = Afin ∧ Afin = A'fin ∧ B = Bfin) ∧
    (IsNoetherianRing R → Module.Flat R N →
      A = A' ∧ A' = Afin ∧ Afin = A'fin ∧ A'fin = Bfin ∧ Bfin = B)
```

## Tag 05GC, a definition

[Tag 05GC](https://stacks.math.columbia.edu/tag/05GC) in the Stacks Project.

**`Module.relativeAssassin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelativeAssassin/Defs.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/RelativeAssassin/Defs.lean#L101).

> The **relative assassin** `Ass_{S/R}(N)` of an `S`-module `N` over a ring map `R → S`: the
> set of primes `𝔮` of `S` which, with `𝔭 = R ∩ 𝔮` the contraction of `𝔮` to `R`, are associated
> primes over `S` of the fibre module `N ⊗_R κ(𝔭)`, that is, are the annihilator of some element
> of it. This is the set `A` of `Module.relativeAssassin_comparison_annihilator`.

```lean
public def relativeAssassin : Set (PrimeSpectrum S)
```

## Tag 0312, a lemma

[Tag 0312](https://stacks.math.columbia.edu/tag/0312) in the Stacks Project.

**`associatedPrimes.tensorProduct_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean#L565).

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

**`Stacks.AssociatedPrimes.Localization.assPrimes_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean#L436). The attribute's comment: “Exact-annihilator Ass (00LA); S ⊗\_R K and N ⊗\_R K modelled by their localization universal properties; R generalized from a domain to any ring with K its total ring of fractions.”.

> **Stacks 05C1 / Lemma 10.65.4.**  Let `R → S` be a ring map, `N` an `S`-module that is flat
> over `R`, and `K` the fraction field of `R` (more generally, its total ring of fractions).
> Then `Ass_S(N) = Ass_S(N ⊗_R K) = Ass_{S ⊗_R K}(N ⊗_R K)` via the canonical inclusion
> `Spec(S ⊗_R K) ⊆ Spec(S)`: the first equality holds as sets of ideals of `S`, and contraction
> along `algebraMap S (S ⊗_R K)` is injective on ideals and maps `Ass_{S ⊗_R K}(N ⊗_R K)` onto
> `Ass_S(N ⊗_R K)`.  Here `Ass` is the exact-annihilator notion `assPrimes` of Stacks 00LA,
> `S ⊗_R K` is modelled as the localization `SK` of `S` at the image of `R⁰`, and `N ⊗_R K` as
> the localization `NK` of `N` at `R⁰` (over `R`) and at the image of `R⁰` (over `S`), the two
> localization maps agreeing.

```lean
theorem assPrimes_chain [Module.Flat R N] (μN : N →ₗ[R] NK) (μNₛ : N →ₗ[S] NK)
    (hSK : IsLocalization (Algebra.algebraMapSubmonoid S (nonZeroDivisors R)) SK)
    (hμN : IsLocalizedModule (nonZeroDivisors R) μN)
    (hμNₛ : IsLocalizedModule (Algebra.algebraMapSubmonoid S (nonZeroDivisors R)) μNₛ)
    (hμ : ∀ n, μNₛ n = μN n) :
    assPrimes S N = assPrimes S NK ∧
      Function.Injective (Ideal.comap (algebraMap S SK)) ∧
      Ideal.comap (algebraMap S SK) '' assPrimes SK NK = assPrimes S NK
```

## Tag 05C2, a lemma

[Tag 05C2](https://stacks.math.columbia.edu/tag/05C2) in the Stacks Project.

**`assStacks_tensorProduct_of_flat_fiberRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatTensorProductFibre.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatTensorProductFibre.lean#L313). The attribute's comment: “Every `Ass` is that of Definition 00LA (`IsAssociatedPrimeStacks`), over `R`, over `S` and over the fibre rings; the fibre module `N ⊗_R κ(𝔭)` is written `(S ⊗[R] κ(𝔭)) ⊗[S] N`.”.

> **Stacks Tag 05C2.** Let `R → S` be a ring map, let `M` be an `R`-module and let `N` be an
> `S`-module which is flat as an `R`-module. Viewing `Spec(S ⊗_R κ(𝔭))` as a subset of `Spec(S)`
> (Remark 00E6), we have
> `Ass_S(N ⊗_R M) ⊇ ⋃_{𝔭 ∈ Ass_R(M)} Ass_{S ⊗_R κ(𝔭)}(N ⊗_R κ(𝔭))`,
> and this inclusion is an equality if `R` is Noetherian. Every `Ass` is that of Definition 00LA,
> `IsAssociatedPrimeStacks`: the primes that are the annihilator of an element, over `R`, over `S`
> and over the fibre rings, with no Noetherian hypothesis on `S` or on the fibre rings.
>
> The source writes `M ⊗_R N`; it is `N ⊗[R] M` here, the `S`-module structure being carried by the
> left factor, and the two are the same `S`-module by `TensorProduct.comm`. The fibre module
> `N ⊗_R κ(𝔭)` is spelled as the base change `(S ⊗[R] κ(𝔭)) ⊗[S] N`, which carries the action of
> the fibre ring and is `S`-isomorphic to `N ⊗[R] κ(𝔭)` by
> `TensorProduct.AlgebraTensorModule.cancelBaseChange`. The inclusion
> `Spec(S ⊗_R κ(𝔭)) ⊆ Spec(S)` is the image under `PrimeSpectrum.comap` of the canonical map
> `S → S ⊗_R κ(𝔭)`.

```lean
public theorem assStacks_tensorProduct_of_flat_fiberRing {R S M N : Type*} [CommRing R]
    [CommRing S] [Algebra R S] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module S N]
    [Module R N] [IsScalarTower R S N] [Module.Flat R N] :
    (⋃ p ∈ {p : PrimeSpectrum R | IsAssociatedPrimeStacks R M p.asIdeal},
        PrimeSpectrum.comap (algebraMap S (S ⊗[R] p.asIdeal.ResidueField)) ''
          {Q | IsAssociatedPrimeStacks (S ⊗[R] p.asIdeal.ResidueField)
            ((S ⊗[R] p.asIdeal.ResidueField) ⊗[S] N) Q.asIdeal}) ⊆
      {q : PrimeSpectrum S | IsAssociatedPrimeStacks S (N ⊗[R] M) q.asIdeal} ∧
    (IsNoetherianRing R →
      {q : PrimeSpectrum S | IsAssociatedPrimeStacks S (N ⊗[R] M) q.asIdeal} =
        ⋃ p ∈ {p : PrimeSpectrum R | IsAssociatedPrimeStacks R M p.asIdeal},
          PrimeSpectrum.comap (algebraMap S (S ⊗[R] p.asIdeal.ResidueField)) ''
            {Q | IsAssociatedPrimeStacks (S ⊗[R] p.asIdeal.ResidueField)
              ((S ⊗[R] p.asIdeal.ResidueField) ⊗[S] N) Q.asIdeal})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.65, Tag 05GA](https://stacks.math.columbia.edu/tag/05GA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
