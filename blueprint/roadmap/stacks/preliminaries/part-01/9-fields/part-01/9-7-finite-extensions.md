---
declaration: section
origin: cited
lean: Module.finrank, Module.Finite, RatFunc.rank_eq_max, MvRatFunc.essFiniteType, MvRatFunc.not_moduleFinite, RingHom.Finite.finiteType, Polynomial.Monic.finrank_adjoinRoot, finrank_quotient_span_eq_natDegree
statement: formalized
proof: formalized
---

# 9.7 Finite extensions

Section 9.7 of the Stacks Project, [Tag 09G2](https://stacks.math.columbia.edu/tag/09G2). 5 tags here are carried by 4 declarations of the repository (all in StacksCore) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09G3, a definition

[Tag 09G3](https://stacks.math.columbia.edu/tag/09G3) in the Stacks Project.

Declarations registered for the tag:

- [`Module.finrank`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finrank#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/Dimension/Finrank.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/LinearAlgebra/Dimension/Finrank.lean#L12) (StacksCore). References: EGA 0 (21.9.5); EGA 0 (22.4.1); EGA I (6.4.5); EGA II (6.4.2); SGA 1 I (7.5), “more general”; SGA 1 IV (4.4); SGA 3 XXI (1.1.6); SGA 3 XXII (5.3.1); SGA 6 0 (2.3.Corollary2), “affine clause”; SGA 6 I (6.11), “special case”.
- [`Module.Finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Finiteness/Defs.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/Defs.lean#L12) (StacksCore). References: EGA 0 (10.3.1.2); EGA 0 (1.0.5); EGA II (6.3.1); EGA III (4.4.7); EGA III (7.4.6); EGA III (7.9.1); EGA IV (6.1.3); EGA IV (7.2.4); EGA IV (14.5.5); EGA IV (2.5.3); EGA IV (18.3.2.1); SGA 1 I (2.1); SGA 3 VIII (3.4); SGA 3 XXI (1.1.1), “partial”; SGA 4 VI (5.6), “special case”; SGA 4 XVII (5.5.6.3); SGA 4½ Rapport (4.11); SGA 5 X (3.1), “partial”; SGA 6 I (1.2), “special case”; SGA 6 I (1.3), “special case”; SGA 6 I (2.8), “special case”; SGA 6 II (2.2.10).

## Tag 09G6, an example

[Tag 09G6](https://stacks.math.columbia.edu/tag/09G6) in the Stacks Project.

**`RatFunc.rank_eq_max`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/RatFunc/Rank.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/RatFunc/Rank.lean#L14).

```lean
theorem RatFunc.rank_eq_max (F : Type*) [Field F] : Module.rank F (RatFunc F) = #F ⊔ ℵ₀
```

## Tag 0BU1, a lemma

[Tag 0BU1](https://stacks.math.columbia.edu/tag/0BU1) in the Stacks Project.

**`MvRatFunc.essFiniteType`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/MvRatFunc/EssFiniteType.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/MvRatFunc/EssFiniteType.lean#L15).

```lean
instance essFiniteType (R σ : Type*) [CommRing R] [Finite σ] : EssFiniteType R (MvRatFunc σ R)
```

**`MvRatFunc.not_moduleFinite`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/MvRatFunc/Rank.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/MvRatFunc/Rank.lean#L15).

```lean
theorem not_moduleFinite (F σ : Type*) [Field F] [Nonempty σ] :
    ¬Module.Finite F (MvRatFunc σ F)
```

Declarations registered for the tag:

- [`RingHom.Finite.finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Finite.finiteType#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteType.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/FiniteType.lean#L17) (StacksCore).

## Tag 09G7, an example

[Tag 09G7](https://stacks.math.columbia.edu/tag/09G7) in the Stacks Project.

**`Polynomial.Monic.finrank_adjoinRoot`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/AdjoinRoot.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/AdjoinRoot.lean#L22). References: EGA 0 (22.4.1), “(i), special case”; SGA 3 VIIB (1.6), “(F)”.

> For a monic polynomial `f` over a nontrivial commutative ring `R`, the rank of
> `AdjoinRoot f` as an `R`-module equals the degree of `f`.

```lean
theorem Polynomial.Monic.finrank_adjoinRoot {R : Type*} [CommRing R] [Nontrivial R]
    {f : R[X]} (hf : f.Monic) : Module.finrank R (AdjoinRoot f) = f.natDegree
```

Declarations registered for the tag:

- [`finrank_quotient_span_eq_natDegree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finrank_quotient_span_eq_natDegree#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/AdjoinRoot.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/AdjoinRoot.lean#L12) (StacksCore).

## Tag 09G9, a lemma

[Tag 09G9](https://stacks.math.columbia.edu/tag/09G9) in the Stacks Project.

Declarations registered for the tag:

- [`Module.finrank_mul_finrank`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finrank_mul_finrank#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/Dimension/Free.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/LinearAlgebra/Dimension/Free.lean#L10) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.7, Tag 09G2](https://stacks.math.columbia.edu/tag/09G2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
