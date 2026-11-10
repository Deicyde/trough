---
declaration: section
origin: cited
lean: AdicCompletion.isMittagLeffler_finsupp, AdicCompletion.flat_directSum, AdicCompletion.flat_of_projective_quotient_smul_top, AdicCompletion.isMittagLeffler_of_projective_quotient_smul_top, AdicCompletion.universallyInjective_of_associatedPrimes, AdicCompletion.universallyInjective_of_flat_of_fibre_associatedPrimes
statement: formalized
proof: formalized
---

# 38.8 Completion and Mittag-Leffler modules

Section 38.8 of the Stacks Project, [Tag 05DI](https://stacks.math.columbia.edu/tag/05DI). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05DJ, a lemma

[Tag 05DJ](https://stacks.math.columbia.edu/tag/05DJ) in the Stacks Project.

**`AdicCompletion.isMittagLeffler_finsupp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveCompletedDirectSum.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveCompletedDirectSum.lean#L186). The attribute's comment: “the Mittag-Leffler property; the direct sum `⊕_{α ∈ A} R` is spelled `A →₀ R`. Mittag-Leffler is `IsMittagLeffler`, condition (1) of 059E, as in 059N and 059X.”.

> **Stacks Project, Tag 05DJ.** If `R` is Noetherian and `I`-adically complete, then the
> `I`-adic completion of the direct sum of an `A`-indexed family of copies of `R` is a
> Mittag-Leffler `R`-module.

```lean
theorem isMittagLeffler_finsupp {R : Type uR} [CommRing R] (I : Ideal R) [IsNoetherianRing R]
    [IsAdicComplete I R] (A : Type uA) :
    IsMittagLeffler.{uR, uP, max uR uA, max uR uP, uN} R (AdicCompletion I (A →₀ R))
```

Declarations registered for the tag:

- [`AdicCompletion.flat_directSum`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/Flat/FlatCompletion.lean#L202), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/ProjectiveCompletedDirectSum.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveCompletedDirectSum.lean#L59) (StacksFrontier): “flatness; neither `IsAdicComplete` nor the shape of the direct sum is needed, so the library statement is the more general Tag 06LE”.

## Tag 05DK, a lemma

[Tag 05DK](https://stacks.math.columbia.edu/tag/05DK) in the Stacks Project.

**`AdicCompletion.flat_of_projective_quotient_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveQuotientAdicCompletion.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveQuotientAdicCompletion.lean#L112). The attribute's comment: “flatness; `M/IM` is `M ⧸ I • ⊤`. The source's hypothesis that `R` be `I`-adically complete is dropped: it is unused, neither Tag 05D3 nor Tag 06LE needing it, so this is strictly more general than the source's statement.”. References: SGA 1 IV (3.1).

> **Stacks Project, Tag 05DK.** If `R` is Noetherian, `M` is flat and `M/IM` is projective over
> `R/I`, then the `I`-adic completion of `M` is flat over `R`. The source's hypothesis that `R` be
> `I`-adically complete is not needed for this half.

```lean
theorem flat_of_projective_quotient_smul_top [IsNoetherianRing R]
    [Module.Flat R M] (hM : Module.Projective (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) :
    Module.Flat R (AdicCompletion I M)
```

**`AdicCompletion.isMittagLeffler_of_projective_quotient_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveQuotientAdicCompletion.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveQuotientAdicCompletion.lean#L129). The attribute's comment: “the Mittag-Leffler property; `M/IM` is `M ⧸ I • ⊤`, and Mittag-Leffler is `IsMittagLeffler`, condition (1) of 059E, as in 059N and 05DJ.”.

> **Stacks Project, Tag 05DK.** If `R` is Noetherian and `I`-adically complete, `M` is flat and
> `M/IM` is projective over `R/I`, then the `I`-adic completion of `M` is a Mittag-Leffler
> `R`-module.

```lean
theorem isMittagLeffler_of_projective_quotient_smul_top [IsNoetherianRing R] [IsAdicComplete I R]
    [Module.Flat R M] (hM : Module.Projective (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) :
    IsMittagLeffler.{u, uP, v, max u uP, uN} R (AdicCompletion I M)
```

## Tag 05DL, a lemma

[Tag 05DL](https://stacks.math.columbia.edu/tag/05DL) in the Stacks Project.

**`AdicCompletion.universallyInjective_of_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveAdicCompletionInjectivity.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveAdicCompletionInjectivity.lean#L227). The attribute's comment: “`IS` is `I.map (algebraMap R S)` and `IS + 𝔮` is a supremum of ideals; associatedness is `IsAssociatedPrimeStacks`, the source's definition; the tensor product is written `N ⊗[R] Q`, with `N` on the left, so that it carries its standard `S`-module structure. The source's hypothesis that `R` be Noetherian is dropped: the argument runs entirely over `S`, using Tag 00IQ and Tag 0311 there, so this is strictly more general than the source's statement.”.

> **Stacks Project, Tag 05DL.** Let `R → S` be a map of Noetherian rings, let `I ⊆ R` be an
> ideal and let `N` be a finite `S`-module. If for every finite `R`-module `Q` and every associated
> prime `q` of `N ⊗[R] Q` the ideal `IS + q` is proper, then the canonical map from `N` to its
> `I`-adic completion is universally injective as a map of `R`-modules.

```lean
theorem universallyInjective_of_associatedPrimes {R : Type u} [CommRing R] (I : Ideal R)
    {S : Type v} [CommRing S] [Algebra R S] {N : Type w} [AddCommGroup N] [Module R N]
    [Module S N] [IsScalarTower R S N] [IsNoetherianRing S] [Module.Finite S N]
    (h : ∀ (Q : Type w) [AddCommGroup Q] [Module R Q] [Module.Finite R Q] (q : Ideal S),
      IsAssociatedPrimeStacks S (N ⊗[R] Q) q → I.map (algebraMap R S) ⊔ q ≠ ⊤) :
    UniversallyInjective (AdicCompletion.of I N)
```

## Tag 05DM, a lemma

[Tag 05DM](https://stacks.math.columbia.edu/tag/05DM) in the Stacks Project.

**`AdicCompletion.universallyInjective_of_flat_of_fibre_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ProjectiveAdicCompletionInjectivity.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ProjectiveAdicCompletionInjectivity.lean#L303). The attribute's comment: “`IS` is `I.map (algebraMap R S)` and `IS + 𝔮` is a supremum of ideals; the contraction `𝔭 = R ∩ 𝔮` is `PrimeSpectrum.comap (algebraMap R S) 𝔮`, and `κ(𝔭)` is its `ResidueField`; the tensor product is written `N ⊗[R] κ(𝔭)`, with `N` on the left, so that it carries its standard `S`-module structure.”.

> **Stacks Project, Tag 05DM.** Let `R → S` be a map of Noetherian rings, let `I ⊆ R` be an
> ideal and let `N` be a finite `S`-module which is flat over `R`. If for every prime `𝔮` of `S`
> which is an associated prime of the fibre `N ⊗[R] κ(𝔭)`, where `𝔭 = R ∩ 𝔮`, the ideal `IS + 𝔮` is
> proper, then the canonical map from `N` to its `I`-adic completion is universally injective as a
> map of `R`-modules.

```lean
theorem universallyInjective_of_flat_of_fibre_associatedPrimes {R : Type u} {S : Type v}
    [CommRing R] [CommRing S] [Algebra R S] (I : Ideal R) (N : Type w) [AddCommGroup N]
    [Module S N] [Module R N] [IsScalarTower R S N] [IsNoetherianRing R] [IsNoetherianRing S]
    [Module.Finite S N] [Module.Flat R N]
    (h : ∀ q : PrimeSpectrum S, q.asIdeal ∈ associatedPrimes S
        (N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) →
      I.map (algebraMap R S) ⊔ q.asIdeal ≠ ⊤) :
    UniversallyInjective (AdicCompletion.of I N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.8, Tag 05DI](https://stacks.math.columbia.edu/tag/05DI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
