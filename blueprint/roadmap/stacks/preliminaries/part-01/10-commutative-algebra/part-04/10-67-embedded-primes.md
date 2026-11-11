---
declaration: section
origin: cited
lean: IsEmbeddedAssociatedPrime, Module.exists_isGreatest_isNowhereDense_support, Module.isGreatest_isNowhereDense_support_localized', hasNoEmbeddedAssociatedPrimes_quotient_annihilator
statement: formalized
proof: formalized
---

# 10.67 Embedded primes

Section 10.67 of the Stacks Project, [Tag 02M4](https://stacks.math.columbia.edu/tag/02M4). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02M5, a definition

[Tag 02M5](https://stacks.math.columbia.edu/tag/02M5) in the Stacks Project.

**`IsEmbeddedAssociatedPrime`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean#L899).

> Definition 1 (Embedded associated prime). A prime `𝔭` is an *embedded
> associated prime of `M`* if it is an associated prime of `M` that is not minimal
> among the associated primes of `M`, i.e. there is an associated prime `𝔮` of `M`
> with `𝔮 ⊊ 𝔭`.

```lean
def IsEmbeddedAssociatedPrime
    (R M : Type*) [CommRing R] [AddCommGroup M] [Module R M] (𝔭 : Ideal R) : Prop
```

## Tag 02M6, a lemma

[Tag 02M6](https://stacks.math.columbia.edu/tag/02M6) in the Stacks Project.

**`Module.exists_isGreatest_isNowhereDense_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean#L421).

> Let `R` be a Noetherian ring and `M` a finite `R`-module. The set of `R`-submodules
> `K ⊆ M` whose support is nowhere dense in `Supp(M)` has a largest element `K`, and the
> quotient `M' = M / K` satisfies: (1) `Supp(M) = Supp(M')`; (2) every associated prime of `M'`
> is minimal among the associated primes of `M'`, that is, `M'` has no embedded associated
> primes; (3) for every `f ∈ R` lying in all embedded associated primes of `M`, the localization
> of `M → M'` at the powers of `f` is bijective, so `M_f ≅ M'_f`.

```lean
public theorem exists_isGreatest_isNowhereDense_support :
    ∃ K : Submodule R M,
      IsGreatest {K : Submodule R M |
          IsNowhereDense (Subtype.val ⁻¹' support R ↥K : Set ↥(support R M))} K ∧
        support R (M ⧸ K) = support R M ∧
        (∀ p ∈ associatedPrimes R (M ⧸ K), Minimal (· ∈ associatedPrimes R (M ⧸ K)) p) ∧
        ∀ f : R, (∀ p ∈ associatedPrimes R M, ¬ Minimal (· ∈ associatedPrimes R M) p → f ∈ p) →
          Function.Bijective (LocalizedModule.map (Submonoid.powers f) K.mkQ)
```

## Tag 02M7, a lemma

[Tag 02M7](https://stacks.math.columbia.edu/tag/02M7) in the Stacks Project.

**`Module.isGreatest_isNowhereDense_support_localized'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean, line 859](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean#L859).

> Let `R` be a Noetherian ring, `M` a finite `R`-module, and let `K ⊆ M` be the largest
> `R`-submodule whose support is nowhere dense in `Supp(M)`, as produced by
> `Module.exists_isGreatest_isNowhereDense_support`. Let `Rₚ` be the localization of `R` at a
> submonoid `p` and `g : M →ₗ[R] Mₚ` the localization of `M` at `p`. Then the localized submodule
> `Kₚ ⊆ Mₚ` is the largest `Rₚ`-submodule of `Mₚ` whose support is nowhere dense in `Supp(Mₚ)`.
> Since `(M ⧸ K)ₚ = Mₚ ⧸ Kₚ`, this says that removing the embedded associated primes commutes
> with localization: `(M')ₚ = (Mₚ)'`.

```lean
public theorem isGreatest_isNowhereDense_support_localized' (p : Submonoid R)
    [IsLocalization p Rₚ] (g : M →ₗ[R] Mₚ) [IsLocalizedModule p g] {K : Submodule R M}
    (hK : IsGreatest {K : Submodule R M |
        IsNowhereDense (Subtype.val ⁻¹' support R ↥K : Set ↥(support R M))} K) :
    IsGreatest {L : Submodule Rₚ Mₚ |
        IsNowhereDense (Subtype.val ⁻¹' support Rₚ ↥L : Set ↥(support Rₚ Mₚ))}
      (K.localized' Rₚ p g)
```

## Tag 02M8, a lemma

[Tag 02M8](https://stacks.math.columbia.edu/tag/02M8) in the Stacks Project.

**`hasNoEmbeddedAssociatedPrimes_quotient_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean, line 980](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Embedded.lean#L980).

> **Theorem (Stacks Tag 02M8).** Let `R` be a Noetherian commutative ring and
> `M` a finite `R`-module having no embedded associated primes. Let `I` be the
> annihilator of `M`. Then `R ⧸ I`, viewed as a module over itself, has no embedded
> associated primes (i.e. the ring `R ⧸ I` has no embedded primes, in the sense of
> `HasNoEmbeddedAssociatedPrimes`).

```lean
theorem hasNoEmbeddedAssociatedPrimes_quotient_annihilator
    (R M : Type*) [CommRing R] [IsNoetherianRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (hM : HasNoEmbeddedAssociatedPrimes R M) :
    HasNoEmbeddedAssociatedPrimes (R ⧸ Module.annihilator R M) (R ⧸ Module.annihilator R M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.67, Tag 02M4](https://stacks.math.columbia.edu/tag/02M4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
