---
declaration: section
origin: cited
lean: invLimit_isAdicComplete, Stacks.AdicCompletion.InverseLimit.InverseSystem.quotientEquiv, Stacks.AdicCompletion.InverseLimit.InverseSystem.isAdicComplete, Ideal.IsHomogeneous.exists_finite_graded_forall_ker_eq_pow_smul_top, GradedCompletionData.main_theorem
statement: formalized
proof: formalized
---

# 10.98 Taking limits of modules

Section 10.98 of the Stacks Project, [Tag 09B7](https://stacks.math.columbia.edu/tag/09B7). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G1Q, a lemma

[Tag 0G1Q](https://stacks.math.columbia.edu/tag/0G1Q) in the Stacks Project.

**`invLimit_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean, line 647](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean#L647).

> **Stacks 0G1Q**.  For a finitely generated ideal `I` of a commutative ring `A` and an
> inverse system `(M_n)` of `A`-modules with `I^n M_n = 0` for all `n`, the inverse limit
> `M = lim_n M_n` is `I`-adically complete: it is a direct summand of its own completion, which
> is `I`-adically complete because `I` is finitely generated.

```lean
theorem invLimit_isAdicComplete (hI : I.FG)
    (hM : ∀ n, I ^ n • (⊤ : Submodule A (M n)) = ⊥) :
    IsAdicComplete I (invLimit M t)
```

## Tag 09B8, a lemma

[Tag 09B8](https://stacks.math.columbia.edu/tag/09B8) in the Stacks Project.

**`Stacks.AdicCompletion.InverseLimit.InverseSystem.quotientEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean#L505). The attribute's comment: “(1)”.

> Identification of the quotients: the map `M / Iⁿ M → M n` induced by the limit projection
> `p n` is an isomorphism of `A`-modules.

```lean
noncomputable def quotientEquiv (hI : I.FG) (n : ℕ) :
    (S.limit ⧸ (I ^ n • (⊤ : Submodule A S.limit))) ≃ₗ[A] S.M n
```

**`Stacks.AdicCompletion.InverseLimit.InverseSystem.isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean#L540). The attribute's comment: “(2)”.

> The limit `M = lim_n M n` is `I`-adically complete: the canonical map `M → lim_k M / Iᵏ M`
> is an isomorphism.

```lean
theorem isAdicComplete (hI : I.FG) : IsAdicComplete I S.limit
```

## Tag 0EKC, a lemma

[Tag 0EKC](https://stacks.math.columbia.edu/tag/0EKC) in the Stacks Project.

**`Ideal.IsHomogeneous.exists_finite_graded_forall_ker_eq_pow_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean, line 1402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/InverseLimit.lean#L1402).

> **Stacks 0EKC**. Let `A = ⨁_{i ≥ 0} 𝒜 i` be a graded ring, let `I ⊆ 𝒜₊ = ⨁_{i > 0} 𝒜 i` be a
> homogeneous ideal, and let `(Nₙ)` be an inverse system of finite graded `A`-modules whose
> transition maps `t n : N_{n+1} → Nₙ` are graded and exhibit `Nₙ = N_{n+1}/Iⁿ N_{n+1}`. Then there
> is a finite graded `A`-module `M` and a compatible system of graded surjections `f n : M → Nₙ`
> with `ker (f n) = Iⁿ M`, i.e. `Nₙ = M/Iⁿ M` as graded modules for all `n`.
>
> The source assumes `A` Noetherian; the argument uses only that each `Nₙ` is a finite `A`-module,
> so that hypothesis is omitted.

```lean
public theorem exists_finite_graded_forall_ker_eq_pow_smul_top
    {A : Type u} {σ : Type*} [CommRing A]
    [SetLike σ A] [AddSubmonoidClass σ A] {𝒜 : ℕ → σ} [GradedRing 𝒜]
    {I : Ideal A} (hIhom : I.IsHomogeneous 𝒜)
    (hI : I ≤ (HomogeneousIdeal.irrelevant 𝒜).toIdeal)
    {N : ℕ → Type v} [∀ n, AddCommGroup (N n)] [∀ n, Module A (N n)]
    [∀ n, Module.Finite A (N n)]
    (𝒩 : ∀ n, ℤ → AddSubgroup (N n)) [∀ n, DirectSum.Decomposition (𝒩 n)]
    (h𝒩 : ∀ (n i : ℕ) (d : ℤ) (a : A) (x : N n), a ∈ 𝒜 i → x ∈ 𝒩 n d → a • x ∈ 𝒩 n (i + d))
    (t : ∀ n, N (n + 1) →ₗ[A] N n)
    (ht : ∀ (n : ℕ) (d : ℤ) (x : N (n + 1)), x ∈ 𝒩 (n + 1) d → t n x ∈ 𝒩 n d)
    (htsurj : ∀ n, Function.Surjective (t n))
    (htker : ∀ n, LinearMap.ker (t n) = I ^ n • (⊤ : Submodule A (N (n + 1)))) :
    ∃ (M : Type v) (_ : AddCommGroup M) (_ : Module A M) (ℳ : ℤ → AddSubgroup M)
        (_ : DirectSum.Decomposition ℳ) (f : ∀ n, M →ₗ[A] N n),
      Module.Finite A M ∧
      (∀ (i : ℕ) (d : ℤ) (a : A) (x : M), a ∈ 𝒜 i → x ∈ ℳ d → a • x ∈ ℳ (i + d)) ∧
      (∀ (n : ℕ) (d : ℤ) (x : M), x ∈ ℳ d → f n x ∈ 𝒩 n d) ∧
      (∀ n, Function.Surjective (f n)) ∧
      (∀ n, LinearMap.ker (f n) = I ^ n • (⊤ : Submodule A M)) ∧
      (∀ n, (t n).comp (f (n + 1)) = f n)
```

## Tag 0EKD, a lemma

[Tag 0EKD](https://stacks.math.columbia.edu/tag/0EKD) in the Stacks Project.

**`GradedCompletionData.main_theorem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Completion.lean, line 984](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Completion.lean#L984).

> Stacks tag 0EKD (Lemma 10.98.4): if the induced map `φ : M ⊗_A A' → lim_n Gₙ` is an
> isomorphism, then for every `d ∈ ℤ` the induced map `φ^(d) : M_d → lim_n G_{n,d}` is an
> isomorphism.
>
> Bijectivity of `φ^(d)` splits into injectivity and surjectivity, each reduced through
> `limGdIncl` to `baseChange_degree_injective` and `baseChange_degree_surjective`.

```lean
theorem main_theorem (D : GradedCompletionData)
    (hφ : Function.Bijective D.φ) (d : ℤ) :
    Function.Bijective (D.phiD d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.98, Tag 09B7](https://stacks.math.columbia.edu/tag/09B7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
