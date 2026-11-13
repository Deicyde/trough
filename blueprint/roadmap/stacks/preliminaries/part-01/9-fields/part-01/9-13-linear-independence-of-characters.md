---
declaration: section
origin: cited
lean: Finset.Nonempty.exists_sum_pow_ne_zero, Algebra.liftEmbeddingsEquiv
statement: formalized
proof: formalized
---

# 9.13 Linear independence of characters

Section 9.13 of the Stacks Project, [Tag 0CKK](https://stacks.math.columbia.edu/tag/0CKK). 2 tags here are carried by 2 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EM9, a lemma

[Tag 0EM9](https://stacks.math.columbia.edu/tag/0EM9) in the Stacks Project.

**`Finset.Nonempty.exists_sum_pow_ne_zero`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/LinearIndependent/Basic.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/LinearIndependent/Basic.lean#L16).

```lean
theorem Finset.Nonempty.exists_sum_pow_ne_zero {R : Type*} [CommRing R] [IsDomain R]
    {s : Finset R} (hs : s.Nonempty) : ∃ n, ∑ x ∈ s, x ^ n ≠ 0
```

## Tag 0CKN, a lemma

[Tag 0CKN](https://stacks.math.columbia.edu/tag/0CKN) in the Stacks Project.

**`Algebra.liftEmbeddingsEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/LiftEmbeddingsEquiv.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/LiftEmbeddingsEquiv.lean#L96).

> **Stacks 0CKN**.
> For a finite separable extension `K/F` with `L` algebraically closed, the canonical
> `L`-algebra map `L ⊗[F] K → (K →ₐ[F] L) → L` sending `x ⊗ₜ y` to `σ ↦ x * σ y` is an
> isomorphism.

```lean
noncomputable def liftEmbeddingsEquiv (F K L : Type*)
    [Field F] [Field K] [Field L] [Algebra F K] [Algebra F L]
    [Module.Finite F K] [Algebra.IsSeparable F K] [IsAlgClosed L] :
    L ⊗[F] K ≃ₐ[L] ((K →ₐ[F] L) → L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.13, Tag 0CKK](https://stacks.math.columbia.edu/tag/0CKK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
