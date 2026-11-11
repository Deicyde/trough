---
declaration: section
origin: cited
lean: Polynomial.SplittingField.lift, Polynomial.IsSplittingField.algEquiv, NormalClosure, IsNormalClosure.normalClosure, IsNormalClosure.algEquiv, NormalClosure.algebra, IsNormalClosure.lift', IsNormalClosure.of
statement: formalized
proof: formalized
---

# 9.16 Splitting fields

Section 9.16 of the Stacks Project, [Tag 09HT](https://stacks.math.columbia.edu/tag/09HT). 5 tags here are carried by 13 declarations of the repository (all in StacksCore) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09HU, a lemma

[Tag 09HU](https://stacks.math.columbia.edu/tag/09HU) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.SplittingField.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.SplittingField.lift#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SplittingField/Construction.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SplittingField/Construction.lean#L10) (StacksCore): “smallest”.
- [`Polynomial.IsSplittingField.algEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.IsSplittingField.algEquiv#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SplittingField/Construction.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SplittingField/Construction.lean#L11) (StacksCore): “unique up to (not necessarily unique) isomorphism”.

## Tag 09DT, a lemma

[Tag 09DT](https://stacks.math.columbia.edu/tag/09DT) in the Stacks Project.

**`NormalClosure`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L36). The attribute's comment: “the absolute normal closure”.

```lean
noncomputable abbrev NormalClosure (F E : Type*) [Field F] [Field E] [Algebra F E] : Type _
```

**`IsNormalClosure.normalClosure`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L57).

```lean
instance IsNormalClosure.normalClosure (F E : Type*) [Field F] [Field E] [Algebra F E] :
    IsNormalClosure F E (NormalClosure F E)
```

**`IsNormalClosure.algEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L64). The attribute's comment: “unique”.

```lean
noncomputable def IsNormalClosure.algEquiv (F E N : Type*) [Field F] [Field E] [Field N]
    [Algebra F E] [Algebra F N] [IsNormalClosure F E N] :
    N ≃ₐ[F] NormalClosure F E
```

**`NormalClosure.algebra`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L69).

```lean
noncomputable instance NormalClosure.algebra
    (F E : Type*) [Field F] [Field E] [Algebra F E] [Algebra.IsAlgebraic F E] :
    Algebra E (NormalClosure F E)
```

**`IsNormalClosure.lift'`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L87). The attribute's comment: “smallest”.

> Let `L/E/F` with `L/F` normal. Then a normal closure of `E/F` embeds into `L`.
>
> This is **Stacks 09DT** (smallest).

```lean
noncomputable def IsNormalClosure.lift'
    (F E N L : Type*) [Field F] [Field E] [Field N] [Field L]
    [Algebra F E] [Algebra F N] [Algebra F L] [Algebra E L] [IsScalarTower F E L]
    [IsNormalClosure F E N] [Normal F L] : N →ₐ[F] L
```

**`IsNormalClosure.of`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L193). The attribute's comment: “extends”.

> A **non-canonical** embedding to any arbitrary normal closure.

```lean
noncomputable def IsNormalClosure.of
    (F E N : Type*) [Field F] [Field E] [Field N]
    [Algebra F E] [Algebra F N] [Algebra.IsAlgebraic F E] [IsNormalClosure F E N] : E →ₐ[F] N
```

**`IsNormalClosure.finiteDimensional`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L204).

```lean
theorem IsNormalClosure.finiteDimensional
    (F E N : Type*) [Field F] [Field E] [Field N] [Algebra F E] [Algebra F N]
    [IsNormalClosure F E N] [FiniteDimensional F E] : FiniteDimensional F N
```

Declarations registered for the tag:

- [`IntermediateField.normalClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.normalClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Normal/Closure.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L14) (StacksCore): “the relative normal closure”.
- [`normalClosure.normal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=normalClosure.normal#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Normal/Closure.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L16) (StacksCore): “normal”.
- [`normalClosure.is_finiteDimensional`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=normalClosure.is_finiteDimensional#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Normal/Closure.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L17) (StacksCore): “finite dimensional”.
- [`IsNormalClosure.equiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsNormalClosure.equiv#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Normal/Closure.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L18) (StacksCore): “unique”.

## Tag 0BMF, a definition

[Tag 0BMF](https://stacks.math.columbia.edu/tag/0BMF) in the Stacks Project.

**`NormalClosure`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L36). The attribute's comment: “absolute”.

```lean
noncomputable abbrev NormalClosure (F E : Type*) [Field F] [Field E] [Algebra F E] : Type _
```

## Tag 0BMG, a lemma

[Tag 0BMG](https://stacks.math.columbia.edu/tag/0BMG) in the Stacks Project.

**`normalClosure.algebraOfTower`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L75). The attribute's comment: “2, containment”.

```lean
noncomputable instance normalClosure.algebraOfTower (K M N L : Type*)
    [Field K] [Field M] [Field N] [Field L]
    [Algebra K N] [Algebra K L] [Algebra M N] [Algebra M L] [Algebra N L]
    [IsScalarTower K N L] [IsScalarTower M N L] :
    Algebra M (normalClosure K N L)
```

**`finiteDimensional_normalClosure_of_tower`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L94). The attribute's comment: “2, finite”.

> If we have `L/N/M/K` where `M/K` is normal and `N/M` is finite dimensional then
> the normal closure of `N/K` in `L/K` is finite dimensional over `M`.

```lean
theorem finiteDimensional_normalClosure_of_tower (K M N L : Type*)
    [Field K] [Field M] [Field N] [Field L]
    [Algebra K M] [Algebra K N] [Algebra K L] [Algebra M N] [Algebra M L] [Algebra N L]
    [IsScalarTower K M N] [IsScalarTower K M L] [IsScalarTower K N L] [IsScalarTower M N L]
    [FiniteDimensional M N] [Normal K M] : FiniteDimensional M (normalClosure K N L)
```

Declarations registered for the tag:

- [`IntermediateField.normalClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IntermediateField.normalClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/Normal/Closure.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L15) (StacksCore): “relative normal closure (covers 1 and 2)”.

## Tag 0EXL, a lemma

[Tag 0EXL](https://stacks.math.columbia.edu/tag/0EXL) in the Stacks Project.

**`piTensorProductEmbeddings`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L155).

> **Stacks 0EXL** (the underlying map).
> The canonical `F`-algebra map `(⨂[F] _ : K →ₐ[F] L, K) →ₐ[F] L` whose restriction to the tensor
> factor indexed by an embedding `f : K →ₐ[F] L` is `f` itself; equivalently, on a pure tensor
> `tprod F x` it returns `∏ f, f (x f)`. When `L` is a normal closure of an algebraic extension
> `K/F` this map is surjective; see `IsNormalClosure.piTensorProductEmbeddings_surjective`.

```lean
def piTensorProductEmbeddings (F K L : Type*)
    [CommSemiring F] [Semiring K] [CommSemiring L] [Algebra F K] [Algebra F L]
    [Fintype (K →ₐ[F] L)] : (⨂[F] _ : K →ₐ[F] L, K) →ₐ[F] L
```

**`range_piTensorProductEmbeddings`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L177).

> **Stacks 0EXL** (range).
> For an algebraic extension `K/F`, the range of `piTensorProductEmbeddings F K L` as a subalgebra
> of `L` is exactly the normal closure of `K/F` inside `L`.

```lean
theorem range_piTensorProductEmbeddings (F K L : Type*)
    [Field F] [Field K] [Field L] [Algebra F K] [Algebra F L]
    [Fintype (K →ₐ[F] L)] [Algebra.IsAlgebraic F K] :
    (piTensorProductEmbeddings F K L).range = (normalClosure F K L).toSubalgebra
```

**`IsNormalClosure.piTensorProductEmbeddings_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Closure.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Closure.lean#L218). The attribute's comment: “surjective”.

> **Stacks 0EXL** (surjectivity).
> If `L` is a normal closure of an algebraic extension `K/F`, then the canonical `F`-algebra map
> `piTensorProductEmbeddings F K L : (⨂[F] _ : K →ₐ[F] L, K) →ₐ[F] L` is surjective.

```lean
theorem IsNormalClosure.piTensorProductEmbeddings_surjective
    (F K L : Type*) [Field F] [Field K] [Field L] [Algebra F K] [Algebra F L]
    [Fintype (K →ₐ[F] L)] [Algebra.IsAlgebraic F K] [IsNormalClosure F K L] :
    Function.Surjective (piTensorProductEmbeddings F K L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.16, Tag 09HT](https://stacks.math.columbia.edu/tag/09HT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
