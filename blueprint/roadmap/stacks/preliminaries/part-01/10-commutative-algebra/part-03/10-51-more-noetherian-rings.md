---
declaration: section
origin: cited
lean: Module.finitePresentation_of_finite, isNoetherian_of_isNoetherianRing_of_finite, IsNoetherian.noetherian, isNoetherian_iff', artin_rees, exists_comap_smul_eq_and_range_inf_le, Ideal.iInf_pow_smul_eq_bot_of_isLocalRing, exists_notMem_localized_krullIntersection_eq_bot
statement: formalized
proof: formalized
---

# 10.51 More Noetherian rings

Section 10.51 of the Stacks Project, [Tag 00IJ](https://stacks.math.columbia.edu/tag/00IJ). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00IK, a lemma

[Tag 00IK](https://stacks.math.columbia.edu/tag/00IK) in the Stacks Project.

Declarations registered for the tag:

- [`Module.finitePresentation_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finitePresentation_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Basic.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Basic.lean#L23) (StacksFrontier): “(1)”. References: EGA 0 (1.0.5), “more general”; EGA 0 (1.3.5), “more general”.
- [`isNoetherian_of_isNoetherianRing_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isNoetherian_of_isNoetherianRing_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Basic.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Basic.lean#L24) (StacksFrontier): “(2) and (3): a finite module over a Noetherian ring is Noetherian”. References: SGA 6 I (1.3), “more general”.
- [`IsNoetherian.noetherian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsNoetherian.noetherian#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Basic.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Basic.lean#L27) (StacksFrontier): “(2): the submodules of a Noetherian module are finitely generated”.
- [`isNoetherian_iff'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isNoetherian_iff'#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/Basic.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/Basic.lean#L29) (StacksFrontier): “(3): a Noetherian module satisfies the ascending chain condition on submodules”.

## Tag 00IN, a lemma

[Tag 00IN](https://stacks.math.columbia.edu/tag/00IN) in the Stacks Project.

**`artin_rees`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/ArtinRees.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/ArtinRees.lean#L66). References: EGA 0 (7.3.2.1).

> **Artin–Rees lemma.** For a Noetherian ring `R`, an ideal `I ⊆ R` and a submodule `N` of a
> finite `R`-module `M`, there is a constant `c > 0` with `I^n M ⊓ N = I^(n-c) • (I^c M ⊓ N)` for
> every `n ≥ c`.

```lean
theorem artin_rees
    {R : Type*} {M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    [IsNoetherianRing R] [Module.Finite R M]
    (I : Ideal R) (N : Submodule R M) :
    ∃ c > 0, ∀ n ≥ c,
      (I ^ n • (⊤ : Submodule R M)) ⊓ N
        = I ^ (n - c) • ((I ^ c • (⊤ : Submodule R M)) ⊓ N)
```

## Tag 00IO, a lemma

[Tag 00IO](https://stacks.math.columbia.edu/tag/00IO) in the Stacks Project.

**`exists_comap_smul_eq_and_range_inf_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/ArtinRees.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/ArtinRees.lean#L158). References: EGA 0 (7.3.2.1), “more general”.

> **Map version of Artin–Rees.** For an exact sequence `0 → K → M → N` of
> finitely generated modules over a Noetherian ring `R` and an ideal `I`, there is
> a constant `c` such that for all `n ≥ c`,
> `f⁻¹(IⁿN) = K + Iⁿ⁻ᶜ · f⁻¹(IᶜN)` and `f(M) ∩ IⁿN ⊆ f(Iⁿ⁻ᶜ M)`.

```lean
theorem exists_comap_smul_eq_and_range_inf_le
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {M N : Type*} [AddCommGroup M] [AddCommGroup N]
    [Module R M] [Module R N] [Module.Finite R M] [Module.Finite R N]
    (f : M →ₗ[R] N) (I : Ideal R) :
    ∃ c, ∀ n ≥ c,
      Submodule.comap f (I ^ n • (⊤ : Submodule R N)) =
        LinearMap.ker f +
          I ^ (n - c) • Submodule.comap f (I ^ c • (⊤ : Submodule R N)) ∧
      LinearMap.range f ⊓ (I ^ n • (⊤ : Submodule R N)) ≤
        Submodule.map f (I ^ (n - c) • (⊤ : Submodule R M))
```

## Tag 00IP, a lemma

[Tag 00IP](https://stacks.math.columbia.edu/tag/00IP) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.iInf_pow_smul_eq_bot_of_isLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.iInf_pow_smul_eq_bot_of_isLocalRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Noetherian/ArtinRees.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/ArtinRees.lean#L175) (StacksFrontier): “Krull's intersection theorem for a finite module over a Noetherian local ring”.

## Tag 00IQ, a lemma

[Tag 00IQ](https://stacks.math.columbia.edu/tag/00IQ) in the Stacks Project.

**`exists_notMem_localized_krullIntersection_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/ArtinRees.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/ArtinRees.lean#L206). References: EGA 0 (7.4.2), “more general”; SGA 3 VIB (6.5.3), “special case”.

> For every prime ideal `p` containing `I`, there exists `f ∈ R` with
> `f ∉ p` such that the localization of `N = ⋂_n I^n M` at the submonoid
> generated by `f` is the zero submodule.

```lean
theorem exists_notMem_localized_krullIntersection_eq_bot
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (p : Ideal R) [p.IsPrime] (hIp : I ≤ p) :
    ∃ f : R, f ∉ p ∧
      (krullIntersection M I).localized (Submonoid.powers f) = ⊥
```

**`krullIntersection_eq_bot_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Noetherian/ArtinRees.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Noetherian/ArtinRees.lean#L228). References: EGA 0 (7.3.5), “(a) => (c)”.

> If `I` is contained in the Jacobson radical of `R`, then `N = ⋂_n I^n M = 0`.

```lean
theorem krullIntersection_eq_bot_of_le_jacobson
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (hI : I ≤ Ideal.jacobson ⊥) :
    krullIntersection M I = ⊥
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.51, Tag 00IJ](https://stacks.math.columbia.edu/tag/00IJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
