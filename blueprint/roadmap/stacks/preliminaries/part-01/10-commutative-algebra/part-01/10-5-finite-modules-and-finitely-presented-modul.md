---
declaration: section
origin: cited
lean: Module.FinitePresentation, Module.Finite, Module.projective_iff_lift_map_range_le, Module.FinitePresentation.of_exact_fst, Module.FinitePresentation.of_exact_third, Module.Finite.of_exact_left, Module.Finite.exists_relSeries_isQuotientEquivQuotientCyclic, Module.Finite.of_restrictScalars_finite
statement: formalized
proof: formalized
---

# 10.5 Finite modules and finitely presented modules

Section 10.5 of the Stacks Project, [Tag 0517](https://stacks.math.columbia.edu/tag/0517). 5 tags here are carried by 5 declarations of the repository (all in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0518, a definition

[Tag 0518](https://stacks.math.columbia.edu/tag/0518) in the Stacks Project.

Declarations registered for the tag:

- [`Module.FinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FinitePresentation#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/FinitePresentation.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/FinitePresentation.lean#L10) (StacksCore): “part 2”. References: EGA 0 (1.0.5); EGA IV (2.5.3); SGA 4 VI (5.6), “special case”; SGA 5 IIIB (5.10); SGA 6 I (2.8), “special case”.
- [`Module.Finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Finiteness/Defs.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/Defs.lean#L14) (StacksCore): “part 1”. References: EGA 0 (10.3.1.2); EGA 0 (1.0.5); EGA II (6.3.1); EGA III (4.4.7); EGA III (7.4.6); EGA III (7.9.1); EGA IV (6.1.3); EGA IV (7.2.4); EGA IV (14.5.5); EGA IV (2.5.3); EGA IV (18.3.2.1); SGA 1 I (2.1); SGA 3 VIII (3.4); SGA 3 XXI (1.1.1), “partial”; SGA 4 VI (5.6), “special case”; SGA 4 XVII (5.5.6.3); SGA 4½ Rapport (4.11); SGA 5 X (3.1), “partial”; SGA 6 I (1.2), “special case”; SGA 6 I (1.3), “special case”; SGA 6 I (2.8), “special case”; SGA 6 II (2.2.10).

## Tag 07JX, a lemma

[Tag 07JX](https://stacks.math.columbia.edu/tag/07JX) in the Stacks Project.

**`Module.projective_iff_lift_map_range_le`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/Projective.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/Projective.lean#L17). References: SGA 5 XV (3.Lemma3), “more general”; SGA 6 I (1.3), “more general”.

> This is a generalisation of 07JX to an characterization of projective modules, the forward
> direction is exactly what 07JX states.

```lean
theorem Module.projective_iff_lift_map_range_le
    {R : Type u} [Semiring R] {P : Type v} [AddCommMonoid P] [Module R P] [Small.{v} R] :
    Module.Projective R P ↔ ∀ {M N : Type v} [AddCommMonoid M] [AddCommMonoid N] [Module R M]
      [Module R N] (α : P →ₗ[R] M) (β : N →ₗ[R] M), LinearMap.range α ≤ LinearMap.range β →
      ∃ γ : P →ₗ[R] N, α = β.comp γ
```

## Tag 0519, a lemma

[Tag 0519](https://stacks.math.columbia.edu/tag/0519) in the Stacks Project.

**`Module.FinitePresentation.of_exact_fst`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/FinitePresentation.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/FinitePresentation.lean#L26). The attribute's comment: “2”.

```lean
lemma Module.FinitePresentation.of_exact_fst [Module.FinitePresentation R M1]
    [Module.FinitePresentation R M3] :
    Module.FinitePresentation R M2
```

**`Module.FinitePresentation.of_exact_third`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/FinitePresentation.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/FinitePresentation.lean#L34). The attribute's comment: “4”. References: EGA 0 (1.0.5), “partial”.

```lean
lemma Module.FinitePresentation.of_exact_third [Module.Finite R M1]
    [Module.FinitePresentation R M2] :
    Module.FinitePresentation R M3
```

**`Module.Finite.of_exact_left`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/FinitePresentation.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/FinitePresentation.lean#L43). The attribute's comment: “5”.

```lean
lemma Module.Finite.of_exact_left [Module.Finite R M2]
    [Module.FinitePresentation R M3] :
    Module.Finite R M1
```

## Tag 00KZ, a lemma

[Tag 00KZ](https://stacks.math.columbia.edu/tag/00KZ) in the Stacks Project.

**`Module.Finite.exists_relSeries_isQuotientEquivQuotientCyclic`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Ideal/AssociatedPrime/Finiteness.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Ideal/AssociatedPrime/Finiteness.lean#L78).

> **Stacks 00KZ**.
> Let `R` be a ring and `M` a finite `R`-module. Then `M` admits a finite filtration
> `0 = M₀ ≤ M₁ ≤ ⋯ ≤ Mₙ = M`, packaged as a `RelSeries` of
> `Submodule.IsQuotientEquivQuotientCyclic`, whose terms are finitely generated and whose successive
> quotients `Mᵢ₊₁ ⧸ Mᵢ` are cyclic, i.e. each isomorphic to `R ⧸ Iᵢ` for some ideal `Iᵢ`.
>
> The quotients are cyclic but not necessarily simple, so this is a filtration rather than a
> composition series in the sense of `CompositionSeries` (which requires simple quotients, hence
> finite length).

```lean
theorem Module.Finite.exists_relSeries_isQuotientEquivQuotientCyclic (R M : Type*) [Ring R]
    [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ X : RelSeries {(N₁, N₂) | N₁.IsQuotientEquivQuotientCyclic N₂},
      X.head = (⊥ : Submodule R M) ∧ X.last = ⊤ ∧ ∀ i, Module.Finite R (X i)
```

## Tag 0560, a lemma

[Tag 0560](https://stacks.math.columbia.edu/tag/0560) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Finite.of_restrictScalars_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.of_restrictScalars_finite#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Finiteness/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/Basic.lean#L11) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.5, Tag 0517](https://stacks.math.columbia.edu/tag/0517)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
