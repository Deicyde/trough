---
declaration: section
origin: cited
lean: CategoryTheory.Abelian, CategoryTheory.Preadditive.fromOpposite, CategoryTheory.Abelian.fromOpposite, CategoryTheory.instPreadditiveOpposite, CategoryTheory.instAbelianOpposite, CategoryTheory.isIso_iff_mono_and_epi, CategoryTheory.Preadditive.mono_iff_isZero_kernel, CategoryTheory.Preadditive.epi_iff_isZero_cokernel
statement: formalized
proof: formalized
---

# 12.5 Abelian categories

Section 12.5 of the Stacks Project, [Tag 00ZX](https://stacks.math.columbia.edu/tag/00ZX). 19 tags here are carried by 10 declarations of the repository (all in StacksCore) and 27 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0109, a definition

[Tag 0109](https://stacks.math.columbia.edu/tag/0109) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L9) (StacksCore). References: SGA 3 VIA (5.4.2); SGA 5 V (4.2); SGA 6 II (3.1).

## Tag 010A, a lemma

[Tag 010A](https://stacks.math.columbia.edu/tag/010A) in the Stacks Project.

**`CategoryTheory.Preadditive.fromOpposite`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/Opposite.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Opposite.lean#L15).

```lean
local instance CategoryTheory.Preadditive.fromOpposite {C : Type*} [Category* C]
    [Preadditive Cᵒᵖ] : Preadditive C
```

**`CategoryTheory.Abelian.fromOpposite`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/Opposite.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Opposite.lean#L24).

```lean
noncomputable local instance CategoryTheory.Abelian.fromOpposite {C : Type*} [Category* C]
    [Abelian Cᵒᵖ] : Abelian C
```

Declarations registered for the tag:

- [`CategoryTheory.instPreadditiveOpposite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instPreadditiveOpposite#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Opposite.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Opposite.lean#L21) (StacksCore).
- [`CategoryTheory.instAbelianOpposite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instAbelianOpposite#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Opposite.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Opposite.lean#L34) (StacksCore).

## Tag 010C, a lemma

[Tag 010C](https://stacks.math.columbia.edu/tag/010C) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.isIso_iff_mono_and_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.isIso_iff_mono_and_epi#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Balanced.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Balanced.lean#L8) (StacksCore).
- [`CategoryTheory.Preadditive.mono_iff_isZero_kernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Preadditive.mono_iff_isZero_kernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/Basic.lean#L10) (StacksCore).
- [`CategoryTheory.Preadditive.epi_iff_isZero_cokernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Preadditive.epi_iff_isZero_cokernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/Basic.lean#L11) (StacksCore).

## Tag 010D, a lemma

[Tag 010D](https://stacks.math.columbia.edu/tag/010D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.hasFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.hasFiniteLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L10) (StacksCore).
- [`CategoryTheory.Abelian.hasFiniteColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.hasFiniteColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L11) (StacksCore).

## Tag 05PJ, an example

[Tag 05PJ](https://stacks.math.columbia.edu/tag/05PJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.PullbackToBiproductIsKernel.isLimitPullbackToBiproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.PullbackToBiproductIsKernel.isLimitPullbackToBiproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L12) (StacksCore).
- [`CategoryTheory.Abelian.BiproductToPushoutIsCokernel.isColimitBiproductToPushout`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.BiproductToPushoutIsCokernel.isColimitBiproductToPushout#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L13) (StacksCore). References: EGA 0 (18.2.7), “more general”.

## Tag 010E, a definition

[Tag 010E](https://stacks.math.columbia.edu/tag/010E) in the Stacks Project.

Declarations registered for the tag:

- [`HomologicalComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalComplex.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalComplex.lean#L8) (StacksCore). References: EGA 0 (11.1.1), “(a)”; EGA 0 (11.2.1), “more general”; EGA 0 (11.6.1), “more general”; SGA 4 XVII (0.4), “special case”; SGA 4 XVII (2.2.7), “special case”; SGA 6 I (1.1.5), “partial”; SGA 7 VII (3.1), “more general”.
- [`CategoryTheory.ShortComplex.Exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.Exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Exact.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/Exact.lean#L25) (StacksCore).
- [`HomologicalComplex.ExactAt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.ExactAt#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L20) (StacksCore).
- [`CategoryTheory.ShortComplex.ShortExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.ShortExact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ShortExact.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ShortExact.lean#L25) (StacksCore). References: EGA 0 (12.3.2).

## Tag 05AA, a lemma

[Tag 05AA](https://stacks.math.columbia.edu/tag/05AA) in the Stacks Project.

**`exact_iff_homLeft`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L43). The attribute's comment: “part 2”.

```lean
lemma exact_iff_homLeft : S.Exact ∧ Mono S.f ↔ ∀ N : C,
    (S.map (preadditiveCoyoneda.obj (op N))).Exact ∧
    Mono (S.map (preadditiveCoyoneda.obj (op N))).f
```

**`exact_iff_homRight`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L62). The attribute's comment: “part 1”.

```lean
lemma exact_iff_homRight : S.Exact ∧ Epi S.g ↔ ∀ N : C,
    (S.op.map (preadditiveYoneda.obj N)).Exact ∧
    Mono (S.op.map (preadditiveYoneda.obj N)).f
```

## Tag 010F, a definition

[Tag 010F](https://stacks.math.columbia.edu/tag/010F) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.Splitting`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.Splitting#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Exact.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/Exact.lean#L26) (StacksCore).

## Tag 010G, a lemma

[Tag 010G](https://stacks.math.columbia.edu/tag/010G) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.Splitting.ofExactOfSection`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.Splitting.ofExactOfSection#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Exact.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/Exact.lean#L27) (StacksCore).
- [`CategoryTheory.ShortComplex.Splitting.ofExactOfRetraction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.Splitting.ofExactOfRetraction#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Exact.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/Exact.lean#L28) (StacksCore).

## Tag 08N2, a lemma

[Tag 08N2](https://stacks.math.columbia.edu/tag/08N2) in the Stacks Project.

**`CategoryTheory.CommSq.isPullback_iff_exact_and_mono_f`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/CommSq.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/CommSq.lean#L51). The attribute's comment: “(1)”.

> A commutative square in an abelian category is cartesian if and only if the associated
> sequence `0 ⟶ X₁ ⟶ X₂ ⊞ X₃ ⟶ X₄` is exact, where the first map is `biprod.lift fst snd` and
> the second is `biprod.desc f (-g)`.

```lean
lemma isPullback_iff_exact_and_mono_f {fst : X₁ ⟶ X₂} {snd : X₁ ⟶ X₃} {f : X₂ ⟶ X₄}
    {g : X₃ ⟶ X₄} (sq : CommSq fst snd f g) :
    IsPullback fst snd f g ↔ sq.shortComplex'.Exact ∧ Mono sq.shortComplex'.f
```

**`CategoryTheory.CommSq.isPushout_iff_exact_and_epi_g`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/CommSq.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/CommSq.lean#L61). The attribute's comment: “(2)”.

> A commutative square in an abelian category is cocartesian if and only if the associated
> sequence `X₁ ⟶ X₂ ⊞ X₃ ⟶ X₄ ⟶ 0` is exact, where the first map is `biprod.lift f (-g)` and
> the second is `biprod.desc inl inr`.

```lean
lemma isPushout_iff_exact_and_epi_g {f : X₁ ⟶ X₂} {g : X₁ ⟶ X₃} {inl : X₂ ⟶ X₄}
    {inr : X₃ ⟶ X₄} (sq : CommSq f g inl inr) :
    IsPushout f g inl inr ↔ sq.shortComplex.Exact ∧ Epi sq.shortComplex.g
```

## Tag 08N3, a lemma

[Tag 08N3](https://stacks.math.columbia.edu/tag/08N3) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.isIso_kernel_map_of_isPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.isIso_kernel_map_of_isPullback#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Pullback/IsPullback/Kernels.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Pullback/IsPullback/Kernels.lean#L8) (StacksCore).
- [`CategoryTheory.Limits.isIso_cokernel_map_of_isPushout`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.isIso_cokernel_map_of_isPushout#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Pullback/IsPullback/Kernels.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Pullback/IsPullback/Kernels.lean#L9) (StacksCore).

## Tag 08N4, a lemma

[Tag 08N4](https://stacks.math.columbia.edu/tag/08N4) in the Stacks Project.

**`CategoryTheory.CommSq.IsPullback.epi_to_isPushout`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/CommSq.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/CommSq.lean#L78). The attribute's comment: “(1)”.

```lean
lemma IsPullback.epi_to_isPushout (hP : IsPullback g f k h) [Epi k] :
    IsPushout g f k h ∧ Epi f
```

**`CategoryTheory.CommSq.IsPushout.mono_to_isPullback`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/CommSq.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/CommSq.lean#L86). The attribute's comment: “(2)”.

```lean
lemma IsPushout.mono_to_isPullback (hP : IsPushout g f k h) [Mono g] :
    IsPullback g f k h ∧ Mono h
```

## Tag 05PK, a lemma

[Tag 05PK](https://stacks.math.columbia.edu/tag/05PK) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.epi_pullback_of_epi_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.epi_pullback_of_epi_f#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L14) (StacksCore).
- [`CategoryTheory.Abelian.mono_pushout_of_mono_g`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.mono_pushout_of_mono_g#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Basic.lean#L15) (StacksCore).

## Tag 08N5, a lemma

[Tag 08N5](https://stacks.math.columbia.edu/tag/08N5) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.exact_iff_exact_up_to_refinements`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.exact_iff_exact_up_to_refinements#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Refinements.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Refinements.lean#L8) (StacksCore).

## Tag 08N6, a lemma

[Tag 08N6](https://stacks.math.columbia.edu/tag/08N6) in the Stacks Project.

**`CategoryTheory.ShortComplex.Exact.exact_kernelShortComplex`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean#L49). The attribute's comment: “(1)”.

> If the first row of a commutative ladder in an abelian category is exact and the first map
> of the second row is a monomorphism, then the induced short complex
> `kernel α ⟶ kernel β ⟶ kernel γ` is exact.

```lean
lemma Exact.exact_kernelShortComplex (hS : S.Exact) [Mono k] :
    (S.kernelShortComplex comm₁ comm₂).Exact
```

**`CategoryTheory.ShortComplex.Exact.exact_cokernelShortComplex`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean#L109). The attribute's comment: “(2)”.

> If the second row of a commutative ladder in an abelian category is exact and the second
> map of the first row is an epimorphism, then the induced short complex
> `cokernel α ⟶ cokernel β ⟶ cokernel γ` is exact.

```lean
lemma Exact.exact_cokernelShortComplex (hT : T.Exact) [Epi g] :
    (T.cokernelShortComplex comm₁ comm₂).Exact
```

## Tag 010H, a lemma

[Tag 010H](https://stacks.math.columbia.edu/tag/010H) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.SnakeInput.snake_lemma`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.SnakeInput.snake_lemma#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean#L10) (StacksCore).

## Tag 08N7, a lemma

[Tag 08N7](https://stacks.math.columbia.edu/tag/08N7) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.SnakeInput.naturality_δ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.SnakeInput.naturality_δ#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/SnakeLemma.lean#L11) (StacksCore).

## Tag 05QA, a lemma

[Tag 05QA](https://stacks.math.columbia.edu/tag/05QA) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.epi_of_epi_of_epi_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.epi_of_epi_of_epi_of_mono#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean#L9) (StacksCore): “part 1”.
- [`CategoryTheory.Abelian.mono_of_epi_of_mono_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.mono_of_epi_of_mono_of_mono#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean#L10) (StacksCore): “part 2”.

## Tag 05QB, a lemma

[Tag 05QB](https://stacks.math.columbia.edu/tag/05QB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.isIso_of_epi_of_isIso_of_isIso_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.isIso_of_epi_of_isIso_of_isIso_of_mono#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/DiagramLemmas/Four.lean#L11) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.5, Tag 00ZX](https://stacks.math.columbia.edu/tag/00ZX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
