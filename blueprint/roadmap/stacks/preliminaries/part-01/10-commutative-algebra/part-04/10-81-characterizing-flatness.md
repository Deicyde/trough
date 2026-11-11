---
declaration: section
origin: cited
lean: Module.Flat.iff_exists_factorization_of_finitePresentation, Module.Flat.iff_surjective_compRight_of_finitePresentation, flat_iff_directLimit_free_finite
statement: formalized
proof: formalized
---

# 10.81 Characterizing flatness

Section 10.81 of the Stacks Project, [Tag 058C](https://stacks.math.columbia.edu/tag/058C). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 058E, a lemma

[Tag 058E](https://stacks.math.columbia.edu/tag/058E) in the Stacks Project.

**`Module.Flat.iff_exists_factorization_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/EquationalCriterion.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/EquationalCriterion.lean#L172).

> **Stacks 058E.** An `R`-module `M` is flat if and only if every `R`-linear map to `M` from a
> finitely presented `R`-module `P` factors through a free finite `R`-module: there are `k : ℕ` and
> maps `h : P → (Fin k →₀ R)` and `g : (Fin k →₀ R) → M` with `f = g ∘ h`.

```lean
public theorem Module.Flat.iff_exists_factorization_of_finitePresentation {R : Type u} {M : Type v}
    [CommRing R] [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔ ∀ ⦃P : Type u⦄ [AddCommGroup P] [Module R P]
      [Module.FinitePresentation R P] (f : P →ₗ[R] M),
      ∃ (k : ℕ) (h : P →ₗ[R] (Fin k →₀ R)) (g : (Fin k →₀ R) →ₗ[R] M), f = g ∘ₗ h
```

## Tag 058F, a lemma

[Tag 058F](https://stacks.math.columbia.edu/tag/058F) in the Stacks Project.

**`Module.Flat.iff_surjective_compRight_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/EquationalCriterion.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/EquationalCriterion.lean#L250).

> **Stacks 058F.** An `R`-module `M` is flat if and only if for every finitely presented
> `R`-module `P` and every surjection `φ : N → M` of `R`-modules the induced map
> `Hom_R(P, N) → Hom_R(P, M)`, postcomposition with `φ`, is surjective.

```lean
public theorem Module.Flat.iff_surjective_compRight_of_finitePresentation {R : Type u} [CommRing R]
    [Small.{v} R] {M : Type v} [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        ⦃N : Type v⦄ [AddCommGroup N] [Module R N] (φ : N →ₗ[R] M), Function.Surjective φ →
        Function.Surjective (LinearMap.compRight (M := P) R φ)
```

## Tag 058G, a theorem

[Tag 058G](https://stacks.math.columbia.edu/tag/058G) in the Stacks Project.

**`flat_iff_directLimit_free_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Lazard.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Lazard.lean#L714). References: EGA 0 (6.1.2), “special case”; EGA 0 (6.2.3), “special case”; EGA 0 (6.3.4), “partial”; SGA 3 VIIA (4.2.1), “more general”; SGA 4 V (1.2), “Reverse implication only”; SGA 4 V (8.2.12), “special case”; SGA 4 VI (8.6.4), “special case”; SGA 4 XVII (5.5.1.1), “special case”; SGA 4 XVII (5.5.1.2), “partial”; SGA 4 XVII (5.5.6.3), “partial”.

> **Lazard's theorem.**
> An `R`-module `M` over a commutative ring `R` is flat if and only if `M` is the
> colimit of a directed system of free finite `R`-modules: there exists a directed
> (nonempty, filtered) preorder `ι`, a family of `R`-modules `G : ι → Type` with
> `R`-linear transition maps `f` forming a `DirectedSystem`, such that every `G i`
> is free and finite, together with an `R`-linear isomorphism between the direct
> limit `Module.DirectLimit G f` and `M`.

```lean
theorem flat_iff_directLimit_free_finite {R : Type u} [CommRing R] (M : Type u)
    [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      ∃ (ι : Type u) (_ : Preorder ι) (_ : IsDirected ι (· ≤ ·)) (_ : Nonempty ι)
        (_ : DecidableEq ι) (G : ι → Type u) (_ : (i : ι) → AddCommGroup (G i))
        (_ : (i : ι) → Module R (G i)) (f : (i j : ι) → i ≤ j → G i →ₗ[R] G j)
        (_ : DirectedSystem G fun i j h => f i j h),
        (∀ i, Module.Free R (G i)) ∧ (∀ i, Module.Finite R (G i)) ∧
          Nonempty (Module.DirectLimit G f ≃ₗ[R] M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.81, Tag 058C](https://stacks.math.columbia.edu/tag/058C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
