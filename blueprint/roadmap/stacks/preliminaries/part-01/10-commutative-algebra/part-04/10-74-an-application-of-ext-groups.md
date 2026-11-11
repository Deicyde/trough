---
declaration: section
origin: cited
lean: split_injection_of_arbitrarily_large_split_mod_pow
statement: formalized
proof: formalized
---

# 10.74 An application of Ext groups

Section 10.74 of the Stacks Project, [Tag 02HN](https://stacks.math.columbia.edu/tag/02HN). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02HO, a lemma

[Tag 02HO](https://stacks.math.columbia.edu/tag/02HO) in the Stacks Project.

**`split_injection_of_arbitrarily_large_split_mod_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/SplitInjection.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/SplitInjection.lean#L439). References: EGA 0 (19.1.8), “partial”.

> **Theorem (Stacks Tag 02HO, Lemma 10.74.1).**
> Let `R` be a Noetherian commutative ring, `I ⊆ R` an ideal contained in the Jacobson
> radical of `R`, and `N`, `M` finite `R`-modules. Let `φ : N → M` be `R`-linear. If for
> arbitrarily large `n` the induced map `φ̄ₙ : N / Iⁿ N → M / Iⁿ M` is a split injection,
> then `φ` itself is a split injection.

```lean
theorem split_injection_of_arbitrarily_large_split_mod_pow
    {R N M : Type*} [CommRing R] [IsNoetherianRing R]
    [AddCommGroup N] [Module R N] [Module.Finite R N]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (hI : I ≤ Ideal.jacobson ⊥) (φ : N →ₗ[R] M)
    (h : ForArbitrarilyLarge (fun n => IsSplitInjection (inducedMapModPow φ I n))) :
    IsSplitInjection φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.74, Tag 02HN](https://stacks.math.columbia.edu/tag/02HN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
