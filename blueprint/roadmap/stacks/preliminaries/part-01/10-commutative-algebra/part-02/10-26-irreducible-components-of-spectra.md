---
declaration: section
origin: cited
lean: PrimeSpectrum.instSpectralSpace, PrimeSpectrum.irreducibleClosedThroughEquiv, PrimeSpectrum.irreducibleComponentsThroughEquiv, PrimeSpectrum.exists_disjoint_basicOpen_of_mem_minimalPrimes, spec_profinite_tfae
statement: formalized
proof: formalized
---

# 10.26 Irreducible components of spectra

Section 10.26 of the Stacks Project, [Tag 00ER](https://stacks.math.columbia.edu/tag/00ER). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 090M, a lemma

[Tag 090M](https://stacks.math.columbia.edu/tag/090M) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.instSpectralSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.instSpectralSpace#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Profinite.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Profinite.lean#L216) (StacksFrontier): “the spectrum of a ring is a spectral space”. References: EGA I (1.1.8), “more general”; EGA I (1.1.10), “more general”.

## Tag 00ET, a lemma

[Tag 00ET](https://stacks.math.columbia.edu/tag/00ET) in the Stacks Project.

**`PrimeSpectrum.irreducibleClosedThroughEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleComponents.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleComponents.lean#L53). The attribute's comment: “(1)”.

> Part (1): The irreducible closed subsets of `Spec(R)` passing through `𝔭`
> correspond to the prime ideals of any localization `S` of `R` at `𝔭`.

```lean
def irreducibleClosedThroughEquiv :
    irreducibleClosedThrough R 𝔭 ≃ { q : Ideal S // q.IsPrime }
```

**`PrimeSpectrum.irreducibleComponentsThroughEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleComponents.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/IrreducibleComponents.lean#L149). The attribute's comment: “(2)”. References: EGA IV (5.1.12), “special case”.

> Part (2): The irreducible components of `Spec(R)` passing through `𝔭`
> correspond to the minimal prime ideals of any localization `S` of `R` at `𝔭`.

```lean
def irreducibleComponentsThroughEquiv :
    irreducibleComponentsThrough R 𝔭 ≃ minimalPrimes S
```

## Tag 00EV, a lemma

[Tag 00EV](https://stacks.math.columbia.edu/tag/00EV) in the Stacks Project.

**`PrimeSpectrum.exists_disjoint_basicOpen_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean#L290).

> Let `𝔭` be a minimal prime of `R` and let `W ⊆ Spec R` be a quasi-compact open not containing
> `𝔭`. Then some `f ∉ 𝔭` has `D(f)` disjoint from `W`.

```lean
theorem PrimeSpectrum.exists_disjoint_basicOpen_of_mem_minimalPrimes
    {R : Type*} [CommSemiring R]
    {𝔭 : Ideal R} (h𝔭min : 𝔭 ∈ minimalPrimes R)
    {W : TopologicalSpace.Opens (PrimeSpectrum R)}
    (hW : IsCompact (W : Set (PrimeSpectrum R)))
    (h𝔭W : (⟨𝔭, h𝔭min.isPrime⟩ : PrimeSpectrum R) ∉ W) :
    ∃ f ∉ 𝔭,
      Disjoint (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R))
        (W : Set (PrimeSpectrum R))
```

## Tag 04MG, a lemma

[Tag 04MG](https://stacks.math.columbia.edu/tag/04MG) in the Stacks Project.

**`spec_profinite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Profinite.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Profinite.lean#L184).

> For a ring `R` the following are equivalent: `Spec R` is profinite;
> `Spec R` is Hausdorff; `Spec R` is totally disconnected; every quasi-compact open of
> `Spec R` is closed; there are no nontrivial inclusions between primes of `R`; every prime
> of `R` is maximal; every prime of `R` is a minimal prime; every basic open `D(f)` is
> closed.

```lean
theorem spec_profinite_tfae (R : Type*) [CommRing R] :
    [ -- (1) X is profinite: compact, Hausdorff, and totally disconnected
      CompactSpace (PrimeSpectrum R) ∧ T2Space (PrimeSpectrum R) ∧
        TotallyDisconnectedSpace (PrimeSpectrum R),
      -- (2) X is Hausdorff
      T2Space (PrimeSpectrum R),
      -- (3) X is totally disconnected
      TotallyDisconnectedSpace (PrimeSpectrum R),
      -- (4) every quasi-compact open subset of X is closed
      ∀ U : Set (PrimeSpectrum R), IsOpen U → IsCompact U → IsClosed U,
      -- (5) no nontrivial inclusions between prime ideals
      ∀ p q : Ideal R, p.IsPrime → q.IsPrime → p ≤ q → p = q,
      -- (6) every prime ideal is maximal
      ∀ p : Ideal R, p.IsPrime → p.IsMaximal,
      -- (7) every prime ideal is a minimal prime
      ∀ p : Ideal R, p.IsPrime → p ∈ minimalPrimes R,
      -- (8) every standard open D(f) is closed
      ∀ f : R, IsClosed (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R)) ].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.26, Tag 00ER](https://stacks.math.columbia.edu/tag/00ER)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
