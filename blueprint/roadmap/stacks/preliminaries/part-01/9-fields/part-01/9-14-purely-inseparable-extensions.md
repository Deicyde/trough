---
declaration: section
origin: cited
lean: perfectClosure, IsPurelyInseparable.trans, IsPurelyInseparable.exists_tower, IsPurelyInseparable.exists_tower_finrank_eq, eq_separableClosure, Field.finSepDegree, Field.finInsepDegree
statement: formalized
proof: formalized
---

# 9.14 Purely inseparable extensions

Section 9.14 of the Stacks Project, [Tag 09HD](https://stacks.math.columbia.edu/tag/09HD). 5 tags here are carried by 2 declarations of the repository (all in StacksCore) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09HE, a definition

[Tag 09HE](https://stacks.math.columbia.edu/tag/09HE) in the Stacks Project.

Declarations registered for the tag:

- [`perfectClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L14) (StacksCore): “1”.

## Tag 09HG, a lemma

[Tag 09HG](https://stacks.math.columbia.edu/tag/09HG) in the Stacks Project.

Declarations registered for the tag:

- [`IsPurelyInseparable.trans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPurelyInseparable.trans#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L14) (StacksCore).

## Tag 09HI, a lemma

[Tag 09HI](https://stacks.math.columbia.edu/tag/09HI) in the Stacks Project.

**`IsPurelyInseparable.exists_tower`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L29). References: EGA 0 (10.3.1.4), “special case”.

> **Stacks 09HI**.
> A finite purely inseparable extension `E/F` of characteristic exponent `p` admits a tower of
> generators: there exist `x₀, …, x_{n-1} ∈ E` whose `F`-adjunction is all of `E`, and at each
> step `xᵢ` lies outside `F(x₀, …, x_{i-1})` while `xᵢ ^ p` lies inside it.

```lean
theorem IsPurelyInseparable.exists_tower
    (F E : Type*) [Field F] [Field E] [Algebra F E] (p : ℕ) [ExpChar F p]
    [FiniteDimensional F E] [IsPurelyInseparable F E] :
    ∃ (n : ℕ) (x : Fin n → E), adjoin F (Set.range x) = ⊤ ∧
      ∀ i, x i ∉ adjoin F (x '' Set.Iio i) ∧ x i ^ p ∈ adjoin F (x '' Set.Iio i)
```

**`IsPurelyInseparable.exists_tower_finrank_eq`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L97). The attribute's comment: “each step has degree p”.

> **Stacks 09HI** (each step has degree `p`).
> The tower of `IsPurelyInseparable.exists_tower` can be chosen so that, in addition, each step
> `F(x₀, …, x_{i-1}) ⊆ F(x₀, …, x_i)` has degree `p`.

```lean
theorem IsPurelyInseparable.exists_tower_finrank_eq
    (F E : Type*) [Field F] [Field E] [Algebra F E] (p : ℕ) [ExpChar F p]
    [FiniteDimensional F E] [IsPurelyInseparable F E] :
    ∃ (n : ℕ) (x : Fin n → E), adjoin F (Set.range x) = ⊤ ∧
      ∀ i, x i ∉ adjoin F (x '' Set.Iio i) ∧ x i ^ p ∈ adjoin F (x '' Set.Iio i) ∧
        Module.finrank (adjoin F (x '' Set.Iio i)) (adjoin F (x '' Set.Iio i))⟮x i⟯ = p
```

## Tag 030K, a lemma

[Tag 030K](https://stacks.math.columbia.edu/tag/030K) in the Stacks Project.

Declarations registered for the tag:

- [`eq_separableClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=eq_separableClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L15) (StacksCore): “uniqueness”.

## Tag 030L, a definition

[Tag 030L](https://stacks.math.columbia.edu/tag/030L) in the Stacks Project.

Declarations registered for the tag:

- [`Field.finSepDegree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Field.finSepDegree#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SeparableClosure.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SeparableClosure.lean#L15) (StacksCore): “1, Nat-valued version”. References: EGA I (6.4.7).
- [`Field.finInsepDegree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Field.finInsepDegree#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SeparableClosure.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SeparableClosure.lean#L16) (StacksCore): “2, Nat-valued version”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.14, Tag 09HD](https://stacks.math.columbia.edu/tag/09HD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
