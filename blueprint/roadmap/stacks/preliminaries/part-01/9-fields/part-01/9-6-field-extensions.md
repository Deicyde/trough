---
declaration: section
origin: cited
lean: RingHom.injective, Algebra, IntermediateField.fg_top_iff, Algebra.EssFiniteType, Complex.cardinalMk_of_adjoin_Rat_eq_top, RatFunc.algEquivOfTranscendental, exists_common_extension
statement: formalized
proof: formalized
---

# 9.6 Field extensions

Section 9.6 of the Stacks Project, [Tag 09FT](https://stacks.math.columbia.edu/tag/09FT). 6 tags here are carried by 2 declarations of the repository (all in StacksCore) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09FU, a lemma

[Tag 09FU](https://stacks.math.columbia.edu/tag/09FU) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.injective#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/SimpleRing/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleRing/Basic.lean#L19) (StacksCore). References: EGA 0 (21.1.1), “more general”.

## Tag 09FV, a definition

[Tag 09FV](https://stacks.math.columbia.edu/tag/09FV) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Algebra/Defs.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Algebra/Defs.lean#L10) (StacksCore). References: EGA 0 (1.0.4); EGA 0 (18.4.1); EGA 0 (21.1.1); SGA 6 V (6.4).

## Tag 09FZ, a definition

[Tag 09FZ](https://stacks.math.columbia.edu/tag/09FZ) in the Stacks Project.

Declarations registered for the tag:

- [`IntermediateField.fg_top_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.fg_top_iff#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/IntermediateField/Adjoin/Algebra.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/IntermediateField/Adjoin/Algebra.lean#L10) (StacksCore): “finitely generated field extension: correctness”.
- [`Algebra.EssFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.EssFiniteType#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/EssentialFiniteness.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/EssentialFiniteness.lean#L14) (StacksCore): “finitely generated field extension”. References: EGA I (6.4.11); EGA IV (1.3.8); SGA 1 III (1.2); SGA 7 I (0.0.5).

## Tag 09G0, an exercise

[Tag 09G0](https://stacks.math.columbia.edu/tag/09G0) in the Stacks Project.

**`Complex.cardinalMk_of_adjoin_Rat_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Complex/FiniteDimensional.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/LinearAlgebra/Complex/FiniteDimensional.lean#L16).

```lean
theorem Complex.cardinalMk_of_adjoin_Rat_eq_top {s : Set ℂ} (hs : adjoin ℚ s = ⊤) : #s = 𝔠
```

## Tag 09G1, a lemma

[Tag 09G1](https://stacks.math.columbia.edu/tag/09G1) in the Stacks Project.

Declarations registered for the tag:

- [`RatFunc.algEquivOfTranscendental`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RatFunc.algEquivOfTranscendental#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/RatFunc/AsPolynomial.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/RatFunc/AsPolynomial.lean#L10) (StacksCore): “transcendental case”.

## Tag 0H7K, a lemma

[Tag 0H7K](https://stacks.math.columbia.edu/tag/0H7K) in the Stacks Project.

**`exists_common_extension`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Flat/FaithfullyFlat/Basic.lean#L25).

> **Stacks Lemma 0H7K**: Given two field extensions E/K and F/K, there exists a common field
> extension M/K with K-algebra maps E → M and F → M. (The Lean statement is more general but will
> apply where `[Field K] [Field E] [Field F]` by virtue of Mathlib instance
> `Module.FaithfullyFlat.lTensor_nontrivial`.)

```lean
theorem exists_common_extension (K : Type u) (E : Type v) (F : Type w) [CommSemiring K]
    [CommRing E] [CommSemiring F] [Algebra K E] [Algebra K F] [Nontrivial (E ⊗[K] F)] :
    ∃ (M : Type (max v w)) (_ : Field M) (_ : Algebra K M) (_ : Algebra E M) (_ : Algebra F M),
    IsScalarTower K E M ∧ IsScalarTower K F M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.6, Tag 09FT](https://stacks.math.columbia.edu/tag/09FT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
