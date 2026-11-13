---
declaration: section
origin: cited
lean: exists_least_flat_quotient_ideal, flat_tensorProduct_iff_map_least_flat_quotient_ideal_eq_bot
statement: formalized
proof: formalized
---

# 15.17 Flattening over an Artinian ring

Section 15.17 of the Stacks Project, [Tag 05LJ](https://stacks.math.columbia.edu/tag/05LJ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0524, a lemma

[Tag 0524](https://stacks.math.columbia.edu/tag/0524) in the Stacks Project.

**`exists_least_flat_quotient_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Artinian.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Artinian.lean#L34). References: EGA IV (11.4.4), “flat clause, Artinian”.

> Over an Artinian ring `R`, there is a smallest ideal `I` such that `M ⧸ I • M` is flat over
> `R ⧸ I`.

```lean
theorem exists_least_flat_quotient_ideal {R M : Type*} [CommRing R]
    [IsArtinianRing R] [AddCommGroup M] [Module R M] :
    ∃ I : Ideal R,
      Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))) ∧
        ∀ J : Ideal R,
          Module.Flat (R ⧸ J) (M ⧸ (J • (⊤ : Submodule R M))) → I ≤ J
```

## Tag 0525, a lemma

[Tag 0525](https://stacks.math.columbia.edu/tag/0525) in the Stacks Project.

**`flat_tensorProduct_iff_map_least_flat_quotient_ideal_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Artinian.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Artinian.lean#L75).

> The least ideal making the corresponding quotient of a module flat maps
> to zero under precisely those ring maps along which the module becomes flat.

```lean
theorem flat_tensorProduct_iff_map_least_flat_quotient_ideal_eq_bot
    {R M : Type*} [CommRing R] [IsArtinianRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R)
    (hI : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (hmin : ∀ J : Ideal R,
      Module.Flat (R ⧸ J) (M ⧸ (J • (⊤ : Submodule R M))) → I ≤ J) :
    ∀ {S : Type*} [CommRing S] (φ : R →+* S),
      let _ := φ.toAlgebra;
      Module.Flat S (S ⊗[R] M) ↔ I.map φ = ⊥
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.17, Tag 05LJ](https://stacks.math.columbia.edu/tag/05LJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
