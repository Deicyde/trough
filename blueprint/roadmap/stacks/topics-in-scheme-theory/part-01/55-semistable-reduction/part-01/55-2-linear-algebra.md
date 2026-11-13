---
declaration: section
origin: cited
lean: Matrix.det_ne_zero_of_sum_row_lt_diag_weighted, det_ne_zero_of_sum_row_lt_diag, Matrix.ker_mulVecLin_eq_span_indicator, Matrix.not_forall_ker_mulVecLin_eq_span_indicator, Matrix.dotProduct_mulVec_nonpos_of_positive_kernel, Matrix.dotProduct_mulVec_eq_zero_iff_of_positive_kernel, LinearMap.BilinForm.exists_injective_to_discriminantGroup_left, LinearMap.BilinForm.exists_injective_to_discriminantGroup_orthogonal
statement: formalized
proof: formalized
---

# 55.2 Linear algebra

Section 55.2 of the Stacks Project, [Tag 0C5T](https://stacks.math.columbia.edu/tag/0C5T). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C5U, a lemma

[Tag 0C5U](https://stacks.math.columbia.edu/tag/0C5U) in the Stacks Project.

**`Matrix.det_ne_zero_of_sum_row_lt_diag_weighted`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L375). The attribute's comment: “part (2)”.

> **Stacks 0C5U, part (2).** A square matrix over a normed field whose diagonal strictly
> dominates its off-diagonal entries after weighting the columns by a vector `m` has nonzero
> determinant.
>
> Weighting the columns is right multiplication by `Matrix.diagonal m`, whose determinant is the
> product of the `m i`, so the weighted matrix has nonzero determinant by part (1) and the
> determinants differ by that product. Positivity of the weights is not needed: the hypothesis
> already forces each `m i` to be nonzero.

```lean
public theorem det_ne_zero_of_sum_row_lt_diag_weighted {K n : Type*} [NormedField K] [Fintype n]
    [DecidableEq n] (A : Matrix n n K) (m : n → K)
    (h : ∀ i, ∑ j ∈ Finset.univ.erase i, ‖A i j * m j‖ < ‖A i i * m i‖) :
    A.det ≠ 0
```

Declarations registered for the tag:

- [`det_ne_zero_of_sum_row_lt_diag`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=det_ne_zero_of_sum_row_lt_diag#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L393) (StacksFrontier): “part (1)”.

## Tag 0C5V, a lemma

[Tag 0C5V](https://stacks.math.columbia.edu/tag/0C5V) in the Stacks Project.

**`Matrix.ker_mulVecLin_eq_span_indicator`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L68). The attribute's comment: “adds `A.IsSymm`: the printed statement is false without it; a correction”.

> The kernel of a symmetric matrix with nonnegative off-diagonal entries,
> diagonally dominant relative to a positive vector `m`, is spanned by the
> weighted indicator vectors of its isolated equality subsets.
>
> Stacks states 0C5V without the hypothesis `A.IsSymm`, and as printed it is false: see
> `Matrix.not_forall_ker_mulVecLin_eq_span_indicator`. Adding `A.IsSymm` is a correction of the
> printed statement, not a weakening. The proof uses symmetry just to know that `a_ji = 0` whenever
> `i ∈ I`, `j ∉ I` and `a_ij = 0`, so a symmetric zero pattern of `A` would already suffice. The one
> use of 0C5V in Stacks, the second proof of 0C5X, concerns a symmetric matrix.

```lean
public lemma ker_mulVecLin_eq_span_indicator {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (m : Fin n → ℝ)
    (hA : A.IsSymm)
    (hoff : ∀ i j, i ≠ j → 0 ≤ A i j)
    (hm : ∀ i, 0 < m i)
    (hdom : ∀ i, ∑ j ∈ Finset.univ.erase i, A i j * m j ≤ -A i i * m i) :
    LinearMap.ker A.mulVecLin =
      Submodule.span ℝ {x | ∃ I : Set (Fin n),
        x = I.indicator m ∧
        (∀ i ∈ I, ∀ j ∉ I, A i j = 0) ∧
        (∀ i ∈ I, -A i i * m i = ∑ j ∈ Finset.univ.erase i, A i j * m j)}
```

**`Matrix.not_forall_ker_mulVecLin_eq_span_indicator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L211). The attribute's comment: “counterexample: the statement as printed is false without symmetry of `A`”.

> **Stacks 0C5V is false as printed.** Without symmetry of `A` the printed statement fails:
> for `A = [[-1, 1], [0, 0]]` and `m = (1, 1)` every hypothesis holds, and `I = {2}` satisfies the
> conditions (1) and (2) of 0C5V, but `A x_I = (1, 0) ≠ 0`. Here `Fin 2` indexes from `0`, so the
> source's `I = {2}` is `{1}`. The corrected statement is
> `Matrix.ker_mulVecLin_eq_span_indicator`, which adds `A.IsSymm`.

```lean
public theorem not_forall_ker_mulVecLin_eq_span_indicator :
    ¬ ∀ (n : ℕ) (A : Matrix (Fin n) (Fin n) ℝ) (m : Fin n → ℝ),
      (∀ i j, i ≠ j → 0 ≤ A i j) → (∀ i, 0 < m i) →
      (∀ i, ∑ j ∈ Finset.univ.erase i, A i j * m j ≤ -A i i * m i) →
      LinearMap.ker A.mulVecLin =
        Submodule.span ℝ {x | ∃ I : Set (Fin n),
          x = I.indicator m ∧
          (∀ i ∈ I, ∀ j ∉ I, A i j = 0) ∧
          (∀ i ∈ I, -A i i * m i = ∑ j ∈ Finset.univ.erase i, A i j * m j)}
```

## Tag 0C5X, a lemma

[Tag 0C5X](https://stacks.math.columbia.edu/tag/0C5X) in the Stacks Project.

**`Matrix.dotProduct_mulVec_nonpos_of_positive_kernel`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L302). The attribute's comment: “negative semidefiniteness”.

> A symmetric matrix with nonnegative off-diagonal entries which kills a
> strictly positive vector has nonpositive associated quadratic form.

```lean
lemma dotProduct_mulVec_nonpos_of_positive_kernel
    {A : Matrix ι ι R} {m : ι → R} (hA : A.IsSymm)
    (hoffDiag : ∀ i j, i ≠ j → 0 ≤ A i j) (hm : ∀ i, 0 < m i)
    (hAm : A *ᵥ m = 0) (x : ι → R) :
    x ⬝ᵥ (A *ᵥ x) ≤ 0
```

**`Matrix.dotProduct_mulVec_eq_zero_iff_of_positive_kernel`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiagonallyDominant.lean#L321). The attribute's comment: “equality case”.

> If, in addition, no proper nonempty set of indices is disconnected from
> its complement, the zero locus of the quadratic form is the line spanned by
> the positive kernel vector.

```lean
lemma dotProduct_mulVec_eq_zero_iff_of_positive_kernel
    {A : Matrix ι ι R} {m x : ι → R} (hA : A.IsSymm)
    (hoffDiag : ∀ i j, i ≠ j → 0 ≤ A i j) (hm : ∀ i, 0 < m i)
    (hAm : A *ᵥ m = 0)
    (hconnected : ∀ I : Set ι, I.Nonempty → I ≠ Set.univ →
      ¬ ∀ i ∈ I, ∀ j ∉ I, A i j = 0) :
    x ⬝ᵥ (A *ᵥ x) = 0 ↔ ∃ q : R, x = q • m
```

## Tag 0C6V, a lemma

[Tag 0C6V](https://stacks.math.columbia.edu/tag/0C6V) in the Stacks Project.

**`LinearMap.BilinForm.exists_injective_to_discriminantGroup_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean#L232). The attribute's comment: “the map to the discriminant group of A”.

> **Stacks Project, Tag 0C6V (left-hand map).**  The quotient by a saturated
> submodule and its orthogonal complement injects into the discriminant group of
> the submodule.  The cokernel of this injection is a quotient of the
> discriminant group of the ambient lattice.

```lean
public theorem exists_injective_to_discriminantGroup_left
    {L : Type*} [AddCommGroup L] [Module.Free ℤ L] [Module.Finite ℤ L]
    (form : LinearMap.BilinForm ℤ L) (hform_symm : form.IsSymm)
    (A : Submodule ℤ L) (hA : Module.IsTorsionFree ℤ (L ⧸ A)) :
    ∃ i : OrthogonalSumQuotient form A →ₗ[ℤ]
        SubmoduleDiscriminantGroup form A,
      Function.Injective i ∧
        ∃ q : DiscriminantGroup form →ₗ[ℤ]
            (SubmoduleDiscriminantGroup form A ⧸ LinearMap.range i),
          Function.Surjective q
```

**`LinearMap.BilinForm.exists_injective_to_discriminantGroup_orthogonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean#L249). The attribute's comment: “the map to the discriminant group of B”.

> **Stacks Project, Tag 0C6V (right-hand map).**  The quotient by a saturated
> submodule and its orthogonal complement injects into the discriminant group of
> the orthogonal complement.  The cokernel of this injection is a quotient of
> the discriminant group of the ambient lattice.

```lean
public theorem exists_injective_to_discriminantGroup_orthogonal
    {L : Type*} [AddCommGroup L] [Module.Free ℤ L] [Module.Finite ℤ L]
    (form : LinearMap.BilinForm ℤ L) (hform_symm : form.IsSymm)
    (hform_pos : ∀ x : L, x ≠ 0 → 0 < form x x)
    (A : Submodule ℤ L) (hA : Module.IsTorsionFree ℤ (L ⧸ A)) :
    ∃ i : OrthogonalSumQuotient form A →ₗ[ℤ]
        SubmoduleDiscriminantGroup form (A.orthogonalBilin form),
      Function.Injective i ∧
        ∃ q : DiscriminantGroup form →ₗ[ℤ]
            (SubmoduleDiscriminantGroup form (A.orthogonalBilin form) ⧸
              LinearMap.range i),
          Function.Surjective q
```

## Tag 0C6W, a lemma

[Tag 0C6W](https://stacks.math.columbia.edu/tag/0C6W) in the Stacks Project.

**`LinearMap.BilinForm.torsionCokernelEquiv_discriminantGroup_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/DiscriminantGroup.lean#L282).

> **Stacks Project, Tag 0C6W.** For a pair of adjoint maps of positive
> definite integral lattices, when the form on the source is unimodular, the
> torsion in the cokernel of `dStar.comp d` is isomorphic to the discriminant
> group of the image lattice.

```lean
public theorem torsionCokernelEquiv_discriminantGroup_range
    {L₀ L₁ : Type*}
    [AddCommGroup L₀] [Module.Free ℤ L₀] [Module.Finite ℤ L₀]
    [AddCommGroup L₁] [Module.Free ℤ L₁] [Module.Finite ℤ L₁]
    (form₀ : LinearMap.BilinForm ℤ L₀) (form₁ : LinearMap.BilinForm ℤ L₁)
    (hform₀_symm : form₀.IsSymm) (hform₁_symm : form₁.IsSymm)
    (hform₁_pos : ∀ x : L₁, x ≠ 0 → 0 < form₁ x x)
    (d : L₀ →ₗ[ℤ] L₁) (dStar : L₁ →ₗ[ℤ] L₀)
    (hadjoint : LinearMap.IsAdjointPair form₀ form₁ d dStar)
    (hunimodular : Function.Bijective form₀) :
    Nonempty
      (AddCommGroup.torsion (L₀ ⧸ LinearMap.range (dStar.comp d)) ≃ₗ[ℤ]
        SubmoduleDiscriminantGroup form₁ (LinearMap.range d))
```

## Tag 0C6X, a lemma

[Tag 0C6X](https://stacks.math.columbia.edu/tag/0C6X) in the Stacks Project.

**`Matrix.finrank_torsionBy_matrixCokernel_le_cycleRank`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/CycleRank.lean, line 1267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/LinearAlgebra/CycleRank.lean#L1267).

> The prime torsion in the cokernel of a connected recurring symmetric
> integer matrix has dimension at most the cycle rank of its support graph.

```lean
lemma finrank_torsionBy_matrixCokernel_le_cycleRank
    {ι : Type*} [Fintype ι] [LinearOrder ι] {A : Matrix ι ι ℤ}
    {m : ι → ℤ} {ℓ : ℕ} [Fact ℓ.Prime]
    (hA : A.IsSymm)
    (hoffDiag : ∀ i j, i ≠ j → 0 ≤ A i j)
    (hm : ∀ i, 0 < m i)
    (hAm : A *ᵥ m = 0)
    (hconnected : ∀ I : Set ι, I.Nonempty → I ≠ Set.univ →
      ¬ ∀ i ∈ I, ∀ j ∉ I, A i j = 0)
    (hℓA : ∀ i j, 0 < A i j → IsCoprime (ℓ : ℤ) (A i j))
    (hℓm : ∀ i, IsCoprime (ℓ : ℤ) (m i)) :
    let C := (ι → ℤ) ⧸ LinearMap.range A.mulVecLin
    let T := AddSubgroup.torsionBy C (ℓ : ℤ)
    letI : Module (ZMod ℓ) T := AddSubgroup.torsionBy.zmodModule
    Module.finrank (ZMod ℓ) T + Fintype.card ι ≤
      1 + (Finset.univ.filter fun p : ι × ι => p.1 < p.2 ∧ 0 < A p.1 p.2).card
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.2, Tag 0C5T](https://stacks.math.columbia.edu/tag/0C5T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
