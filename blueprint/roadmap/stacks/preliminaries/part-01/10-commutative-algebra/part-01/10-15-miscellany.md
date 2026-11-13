---
declaration: section
origin: cited
lean: Ideal.IsPrime.mul_le, Ideal.exists_add_mem_notMem, Ideal.exists_add_mem_notMem', Ideal.prod_eq_iInf_of_pairwise_isCoprime, Ideal.isCoprime_of_isMaximal, Ideal.IsMaximal.coprime_of_ne, Ideal.quotientInfRingEquivPiQuotient, Matrix.exists_mul_eq_smul_one_of_mem_minorIdeal
statement: formalized
proof: formalized
---

# 10.15 Miscellany

Section 10.15 of the Stacks Project, [Tag 00DR](https://stacks.math.columbia.edu/tag/00DR). 7 tags here are carried by 13 declarations of the repository (9 in StacksCore and 4 in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07K1, a lemma

[Tag 07K1](https://stacks.math.columbia.edu/tag/07K1) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.IsPrime.mul_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsPrime.mul_le#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Operations.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L12) (StacksCore).
- [`Ideal.IsPrime.mul_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsPrime.mul_le#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/Operations.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/Operations.lean#L25) (StacksFrontier).

## Tag 0EHL, a lemma

[Tag 0EHL](https://stacks.math.columbia.edu/tag/0EHL) in the Stacks Project.

**`Ideal.exists_add_mem_notMem`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Ideal/Operations.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L173).

> **Stacks 0EHL.** If the coset `x + I` is contained in none of the ideals `p i`, then some
> `x + y` with `y ∈ I` avoids all of them simultaneously.
>
> All but one of the `p i` must be prime; the exceptional index `a` matches the shape of
> `Ideal.subset_union_prime`. Allowing *two* exceptional indices is false.

```lean
theorem exists_add_mem_notMem (a : ι) {s : Finset ι} {p : ι → Ideal R}
    (hp : ∀ i ∈ s, i ≠ a → (p i).IsPrime) {I : Ideal R} {x : R}
    (h : ∀ i ∈ s, ¬(x ∈ p i ∧ I ≤ p i)) : ∃ y ∈ I, ∀ i ∈ s, x + y ∉ p i
```

**`Ideal.exists_add_mem_notMem'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Ideal/Operations.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L189).

> **Stacks 0EHL** in the tag's literal wording, via `Ideal.vadd_coe_subset_iff`.

```lean
theorem exists_add_mem_notMem' (a : ι) {s : Finset ι} {p : ι → Ideal R}
    (hp : ∀ i ∈ s, i ≠ a → (p i).IsPrime) {I : Ideal R} {x : R}
    (h : ∀ i ∈ s, ¬x +ᵥ (I : Set R) ⊆ (p i : Set R)) : ∃ y ∈ I, ∀ i ∈ s, x + y ∉ p i
```

## Tag 00DT, a lemma

[Tag 00DT](https://stacks.math.columbia.edu/tag/00DT) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.prod_eq_iInf_of_pairwise_isCoprime`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.prod_eq_iInf_of_pairwise_isCoprime#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Operations.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L8) (StacksCore): “(1)”.
- [`Ideal.isCoprime_of_isMaximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isCoprime_of_isMaximal#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Operations.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L9) (StacksCore): “(2)”.
- [`Ideal.IsMaximal.coprime_of_ne`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsMaximal.coprime_of_ne#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Operations.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L10) (StacksCore): “(2)”.
- [`Ideal.quotientInfRingEquivPiQuotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.quotientInfRingEquivPiQuotient#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Quotient/Operations.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Quotient/Operations.lean#L11) (StacksCore): “(1)”. References: EGA 0 (19.3.10.2), “special case”; SGA 3 XXII (5.9.10), “partial”; SGA 3 XXIV (3.9.1), “partial”.

## Tag 07DQ, a lemma

[Tag 07DQ](https://stacks.math.columbia.edu/tag/07DQ) in the Stacks Project.

**`Matrix.exists_mul_eq_smul_one_of_mem_minorIdeal`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Matrix/Minor.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/Matrix/Minor.lean#L76). The attribute's comment: “(1)”.

> **Stacks 07DQ (1)**: every element of the ideal of maximal minors of `A` is realised as a
> scalar left inverse of `A`.

```lean
theorem exists_mul_eq_smul_one_of_mem_minorIdeal {A : Matrix n m R} {f : R}
    (hf : f ∈ A.minorIdeal) : ∃ B : Matrix m n R, B * A = f • 1
```

**`Matrix.pow_card_mem_minorIdeal`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Matrix/Minor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/Matrix/Minor.lean#L99). The attribute's comment: “(2)”.

> **Stacks 07DQ (2)**: a scalar left inverse of `A` lies in the ideal of maximal minors of `A`
> after raising it to the number of columns of `A`.

```lean
theorem pow_card_mem_minorIdeal {A : Matrix n m R} {B : Matrix m n R} {f : R}
    (h : B * A = f • 1) : f ^ Fintype.card m ∈ A.minorIdeal
```

**`Matrix.mem_radical_minorIdeal_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Matrix/Minor.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/Matrix/Minor.lean#L107).

> **Stacks 07DQ**, both parts at once: the radical of the ideal of maximal minors of `A` is
> exactly the set of scalars some power of which admits a left inverse against `A`.

```lean
theorem mem_radical_minorIdeal_iff {A : Matrix n m R} {f : R} :
    f ∈ A.minorIdeal.radical ↔ ∃ k : ℕ, ∃ B : Matrix m n R, B * A = (f ^ k) • 1
```

**`exists_matrix_of_mem_minorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean#L62). The attribute's comment: “(1)”.

> **Statement 1.** For any `f` in the ideal `J` generated by the `m × m`
> minors of `A`, there is an `m × n` matrix `B` with `B * A = f • 1` (the `m × m`
> matrix `f · I_m`).

```lean
theorem exists_matrix_of_mem_minorIdeal (A : Matrix (Fin n) (Fin m) R)
    (f : R) (hf : f ∈ maximalMinorsIdeal A) :
    ∃ B : Matrix (Fin m) (Fin n) R, B * A = f • (1 : Matrix (Fin m) (Fin m) R)
```

**`pow_mem_minorIdeal_of_matrix`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean#L141). The attribute's comment: “(2)”.

> **Statement 2.** If `B * A = f • 1` for some `m × n` matrix `B`, then
> `f ^ m` lies in the ideal `J` generated by the `m × m` minors of `A`.

```lean
theorem pow_mem_minorIdeal_of_matrix (A : Matrix (Fin n) (Fin m) R)
    (f : R) (B : Matrix (Fin m) (Fin n) R)
    (hB : B * A = f • (1 : Matrix (Fin m) (Fin m) R)) :
    f ^ m ∈ maximalMinorsIdeal A
```

## Tag 080R, a lemma

[Tag 080R](https://stacks.math.columbia.edu/tag/080R) in the Stacks Project.

**`Matrix.fromRows_mul_adjugate`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Matrix/Adjugate.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/Matrix/Adjugate.lean#L34).

> **Stacks 080R.**

```lean
theorem fromRows_mul_adjugate (A₁ : Matrix m m R) (A₂ : Matrix p m R) :
    fromRows A₁ A₂ * adjugate A₁ =
      fromRows (A₁.det • (1 : Matrix m m R))
        (Matrix.of fun (i : p) (j : m) => (A₁.updateRow j (A₂ i)).det)
```

**`Matrix.fromRows_mul_adjugate_apply_inr`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/Matrix/Adjugate.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/Matrix/Adjugate.lean#L44).

> **Stacks 080R**, identifying the bottom block's entries as `m × m` minors of the stacked
> matrix — with no sign, taking the rows in the order `1, …, ĵ, …, m` with `i` at slot `j`.

```lean
theorem fromRows_mul_adjugate_apply_inr (A₁ : Matrix m m R)
    (A₂ : Matrix p m R) (i : p) (j : m) :
    (fromRows A₁ A₂ * adjugate A₁) (Sum.inr i) j =
      ((fromRows A₁ A₂).submatrix (Function.update Sum.inl j (Sum.inr i)) id).det
```

**`ab_top_block`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean#L309). The attribute's comment: “top block”.

> **Top block.** With `B = adj(A₁)` and `f = det(A₁)`, the top `m × m` block of
> `A * B` is `f • 1`: for all row/column indices `i, j` in the top block,
> `(A * B)_{i j} = f · δ_{i j}`.

```lean
theorem ab_top_block (hmn : m₀ + 1 ≤ n) (A : Matrix (Fin n) (Fin (m₀ + 1)) R)
    (i j : Fin (m₀ + 1)) :
    (A * (topBlock hmn A).adjugate) (Fin.castLE hmn i) j
      = (topBlock hmn A).det • (1 : Matrix (Fin (m₀ + 1)) (Fin (m₀ + 1)) R) i j
```

**`ab_bottom_block`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/MaximalMinors.lean#L323). The attribute's comment: “bottom block”.

> **Bottom block.** With `B = adj(A₁)`, for a row index `i` lying in the bottom
> block (i.e. `m ≤ i`, here `m₀ + 1 ≤ i`) and any column index `j`,
> `(A * B)_{i j} = (-1)^{m - j} · det(M_{i j})`.

```lean
theorem ab_bottom_block (hmn : m₀ + 1 ≤ n) (A : Matrix (Fin n) (Fin (m₀ + 1)) R)
    (i : Fin n) (j : Fin (m₀ + 1)) :
    (A * (topBlock hmn A).adjugate) i j
      = (-1) ^ (m₀ - (j : ℕ)) * (minorMat hmn A i j).det
```

## Tag 05WI, a lemma

[Tag 05WI](https://stacks.math.columbia.edu/tag/05WI) in the Stacks Project.

**`Module.not_injective_of_spanRank_lt`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/SpanRank.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/SpanRank.lean#L31).

> **Stacks 05WI**, in its general form: no nontriviality or `Ring` hypothesis, and stated as
> non-injectivity rather than as a nonzero kernel.

```lean
theorem not_injective_of_spanRank_lt [StrongRankCondition R] {n : ℕ}
    (h : (⊤ : Submodule R M).spanRank < n) (f : (Fin n → R) →ₗ[R] M) :
    ¬ Function.Injective f
```

**`LinearMap.ker_ne_bot_of_spanRank_lt`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/SpanRank.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/SpanRank.lean#L51).

> **Stacks 05WI** in the tag's literal wording: the kernel is nonzero. The tag's `n ≥ 1` is
> implied by `spanRank ⊤ < n`, and `Module.Finite M` is not needed.

```lean
theorem LinearMap.ker_ne_bot_of_spanRank_lt {n : ℕ}
    (h : (⊤ : Submodule R M).spanRank < n) (f : (Fin n → R) →ₗ[R] M) : LinearMap.ker f ≠ ⊥
```

## Tag 0FJ7, a lemma

[Tag 0FJ7](https://stacks.math.columbia.edu/tag/0FJ7) in the Stacks Project.

Declarations registered for the tag:

- [`invariantBasisNumber_of_nontrivial_of_commRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=invariantBasisNumber_of_nontrivial_of_commRing#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/InvariantBasisNumber.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/InvariantBasisNumber.lean#L13) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.15, Tag 00DR](https://stacks.math.columbia.edu/tag/00DR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
