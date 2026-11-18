---
declaration: module
origin: cited
lean: ProbabilisticTheory.HilbertSchmidt.IsHilbertSchmidt, ProbabilisticTheory.HilbertSchmidt.hasSum_norm_sq_apply_eq_adjoint, ProbabilisticTheory.HilbertSchmidt.summable_norm_sq_adjoint_of_summable_norm_sq, ProbabilisticTheory.HilbertSchmidt.hasSum_norm_sq_apply_of_basis, ProbabilisticTheory.HilbertSchmidt.summable_norm_sq_apply_of_hilbertBasis, ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_zero, ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_smul, ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_add
statement: formalized
proof: formalized
---

# Hilbert–Schmidt operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.HilbertSchmidt`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean): 28 declarations, 9 with a docstring.

> Hilbert–Schmidt operators: a ⋆-closed two-sided ideal whose products have summable diagonals.

## i. Overview

> A bounded operator `S` is Hilbert–Schmidt when `∑ᵢ ‖S eᵢ‖²` converges for a Hilbert basis `{eᵢ}`.
> Hilbert–Schmidt operators form a two-sided ideal closed under the adjoint, `S⋆S` is trace class for
> Hilbert–Schmidt `S`, and a product of two Hilbert–Schmidt operators has an absolutely summable
> diagonal in every basis, with the diagonal sum symmetric in the two factors.

## ii. Key results

> - `IsHilbertSchmidt` : a bounded operator is Hilbert–Schmidt.
> - `isHilbertSchmidt_add`, `isHilbertSchmidt_star` : closure under sums and adjoints.
> - `isHilbertSchmidt_mul_left`, `isHilbertSchmidt_mul_right` : the ideal property.
> - `isTraceClass_star_mul_self_of_isHilbertSchmidt` : `S⋆S` is trace class.
> - `summable_diagonal_of_hilbertSchmidt` : the diagonal of a product of two Hilbert–Schmidt operators
>   is absolutely summable.
> - `tsum_diagonal_mul_eq_tsum_diagonal_swap` : the diagonal sums of `R S` and `S R` agree.

## iv. References

> * None.

**`ProbabilisticTheory.HilbertSchmidt.IsHilbertSchmidt`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L60).

> A bounded operator is Hilbert–Schmidt when its squared norm sum is summable in one Hilbert
> basis. The basis-independence theorem below shows this existential definition is equivalent to
> using any basis.

```lean
def IsHilbertSchmidt (S : H →L[ℂ] H) : Prop
```

**`ProbabilisticTheory.HilbertSchmidt.hasSum_norm_sq_apply_eq_adjoint`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L66).

> The Hilbert–Schmidt square sum of `S` in one basis equals the square sum of `S⋆` in a second
> basis. This is the nonnegative double-sum identity; the usual basis-independence statement follows
> by applying it twice.

```lean
lemma hasSum_norm_sq_apply_eq_adjoint {S : H →L[ℂ] H}
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H)
    (hb : Summable (fun i : w => ‖S (b i)‖ ^ 2)) :
    HasSum (fun j : w' => ‖(ContinuousLinearMap.adjoint S) (c j)‖ ^ 2)
      (∑' i : w, ‖S (b i)‖ ^ 2)
```

**`ProbabilisticTheory.HilbertSchmidt.summable_norm_sq_adjoint_of_summable_norm_sq`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L122).

```lean
lemma summable_norm_sq_adjoint_of_summable_norm_sq {S : H →L[ℂ] H}
    {w : Set H} (b : HilbertBasis w ℂ H)
    (hb : Summable (fun i : w => ‖S (b i)‖ ^ 2)) :
    Summable (fun i : w => ‖(ContinuousLinearMap.adjoint S) (b i)‖ ^ 2)
```

**`ProbabilisticTheory.HilbertSchmidt.hasSum_norm_sq_apply_of_basis`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L128).

```lean
lemma hasSum_norm_sq_apply_of_basis {S : H →L[ℂ] H} {w w' : Set H}
    (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H)
    (hb : Summable (fun i : w => ‖S (b i)‖ ^ 2)) :
    HasSum (fun j : w' => ‖S (c j)‖ ^ 2) (∑' i : w, ‖S (b i)‖ ^ 2)
```

**`ProbabilisticTheory.HilbertSchmidt.summable_norm_sq_apply_of_hilbertBasis`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L142).

```lean
lemma summable_norm_sq_apply_of_hilbertBasis {S : H →L[ℂ] H}
    (w : Set H) (b : HilbertBasis w ℂ H) (hS : IsHilbertSchmidt S) :
    Summable (fun i : w => ‖S (b i)‖ ^ 2)
```

## A. Elementary algebraic closure

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_zero`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L150).

```lean
lemma isHilbertSchmidt_zero : IsHilbertSchmidt (0 : H →L[ℂ] H)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_smul`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L156).

```lean
lemma isHilbertSchmidt_smul {S : H →L[ℂ] H} (c : ℂ) (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (c • S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_add`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L166).

```lean
lemma isHilbertSchmidt_add {R S : H →L[ℂ] H}
    (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (R + S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_sub`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L184).

```lean
lemma isHilbertSchmidt_sub {R S : H →L[ℂ] H}
    (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (R - S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_star`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L189).

```lean
lemma isHilbertSchmidt_star {S : H →L[ℂ] H} (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (star S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_mul_left_of_opNorm_le_one`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L197).

```lean
lemma isHilbertSchmidt_mul_left_of_opNorm_le_one {U S : H →L[ℂ] H}
    (hU : ‖U‖ ≤ 1) (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (U * S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_mul_right_of_opNorm_le_one`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L210).

```lean
lemma isHilbertSchmidt_mul_right_of_opNorm_le_one {S U : H →L[ℂ] H}
    (hU : ‖U‖ ≤ 1) (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (S * U)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_mul_left`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L219).

```lean
lemma isHilbertSchmidt_mul_left {U S : H →L[ℂ] H} (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (U * S)
```

**`ProbabilisticTheory.HilbertSchmidt.isHilbertSchmidt_mul_right`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L232).

```lean
lemma isHilbertSchmidt_mul_right {S U : H →L[ℂ] H} (hS : IsHilbertSchmidt S) :
    IsHilbertSchmidt (S * U)
```

**`ProbabilisticTheory.HilbertSchmidt.isTraceClass_star_mul_self_of_isHilbertSchmidt`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L240).

> `S⋆S` is trace class whenever `S` is Hilbert–Schmidt.

```lean
lemma isTraceClass_star_mul_self_of_isHilbertSchmidt {S : H →L[ℂ] H}
    (hS : IsHilbertSchmidt S) : IsTraceClass (star S * S)
```

**`ProbabilisticTheory.HilbertSchmidt.isTraceClass_mul_star_of_isHilbertSchmidt`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L258).

> `S S⋆` is trace class whenever `S` is Hilbert–Schmidt.

```lean
lemma isTraceClass_mul_star_of_isHilbertSchmidt {S : H →L[ℂ] H}
    (hS : IsHilbertSchmidt S) : IsTraceClass (S * star S)
```

## B. Cauchy–Schwarz estimates on Hilbert–Schmidt diagonals

**`ProbabilisticTheory.HilbertSchmidt.holder_two_two`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L265).

```lean
lemma holder_two_two : (2 : ℝ).HolderConjugate 2
```

**`ProbabilisticTheory.HilbertSchmidt.tsum_mul_le_sqrt_mul_sqrt`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L270).

> The real `ℓ²` Cauchy–Schwarz estimate, in the tsum form needed for operator diagonal bounds.

```lean
lemma tsum_mul_le_sqrt_mul_sqrt {w : Set H} {f g : w → ℝ}
    (hf : Summable (fun i => f i ^ 2)) (hg : Summable (fun i => g i ^ 2))
    (hf_nonneg : ∀ i, 0 ≤ f i) (hg_nonneg : ∀ i, 0 ≤ g i) :
    ∑' i : w, f i * g i ≤ Real.sqrt (∑' i : w, f i ^ 2) * Real.sqrt (∑' i : w, g i ^ 2)
```

**`ProbabilisticTheory.HilbertSchmidt.summable_norm_mul_of_square_sums`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L286).

```lean
lemma summable_norm_mul_of_square_sums {w : Set H}
    (f g : w → ℝ) (hf : Summable (fun i => f i ^ 2)) (hg : Summable (fun i => g i ^ 2))
    (hf_nonneg : ∀ i, 0 ≤ f i) (hg_nonneg : ∀ i, 0 ≤ g i) :
    Summable (fun i => f i * g i)
```

**`ProbabilisticTheory.HilbertSchmidt.tsum_norm_inner_mul_inner_le`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L295).

```lean
lemma tsum_norm_inner_mul_inner_le {w : Set H} (b : HilbertBasis w ℂ H) (x y : H) :
    ∑' i : w, ‖⟪x, b i⟫_ℂ‖ * ‖⟪b i, y⟫_ℂ‖ ≤ ‖x‖ * ‖y‖
```

**`ProbabilisticTheory.HilbertSchmidt.summable_norm_inner_mul_inner`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L323).

```lean
lemma summable_norm_inner_mul_inner {w : Set H} (b : HilbertBasis w ℂ H) (x y : H) :
    Summable (fun i : w => ‖⟪x, b i⟫_ℂ‖ * ‖⟪b i, y⟫_ℂ‖)
```

**`ProbabilisticTheory.HilbertSchmidt.summable_diagonal_of_hilbertSchmidt`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L337).

> The diagonal coefficients of a product of two Hilbert–Schmidt operators are absolutely
> summable.

```lean
lemma summable_diagonal_of_hilbertSchmidt {R S : H →L[ℂ] H}
    {w : Set H} (b : HilbertBasis w ℂ H) (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) :
    Summable (fun i : w => ⟪b i, (R * S) (b i)⟫_ℂ)
```

**`ProbabilisticTheory.HilbertSchmidt.summable_matrix_of_hilbertSchmidt`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L357).

```lean
lemma summable_matrix_of_hilbertSchmidt {R S : H →L[ℂ] H}
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H)
    (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) :
    Summable (Function.uncurry (fun (i : w) (j : w') =>
      ⟪(ContinuousLinearMap.adjoint R) (b i), c j⟫_ℂ * ⟪c j, S (b i)⟫_ℂ))
```

**`ProbabilisticTheory.HilbertSchmidt.hasSum_matrix_row_of_hilbertSchmidt`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L391).

```lean
lemma hasSum_matrix_row_of_hilbertSchmidt {R S : H →L[ℂ] H}
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H) (i : w) :
    HasSum (fun j : w' => ⟪(ContinuousLinearMap.adjoint R) (b i), c j⟫_ℂ * ⟪c j, S (b i)⟫_ℂ)
      ⟪b i, (R * S) (b i)⟫_ℂ
```

**`ProbabilisticTheory.HilbertSchmidt.hasSum_matrix_col_of_hilbertSchmidt`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L400).

```lean
lemma hasSum_matrix_col_of_hilbertSchmidt {R S : H →L[ℂ] H}
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H) (j : w') :
    HasSum (fun i : w => ⟪(ContinuousLinearMap.adjoint R) (b i), c j⟫_ℂ * ⟪c j, S (b i)⟫_ℂ)
      ⟪c j, (S * R) (c j)⟫_ℂ
```

**`ProbabilisticTheory.HilbertSchmidt.tsum_diagonal_mul_eq_tsum_diagonal_swap`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L419).

> For Hilbert–Schmidt `R` and `S`, the diagonal sum of `R S` in one basis equals the diagonal sum
> of `S R` in any other.

```lean
lemma tsum_diagonal_mul_eq_tsum_diagonal_swap {R S : H →L[ℂ] H}
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H)
    (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) :
    (∑' i : w, ⟪b i, (R * S) (b i)⟫_ℂ) = ∑' j : w', ⟪c j, (S * R) (c j)⟫_ℂ
```

## C. Quantitative right-multiplication estimate

**`ProbabilisticTheory.HilbertSchmidt.tsum_norm_sq_mul_right_le_of_opNorm_le_one`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L440).

> **Quantitative right-multiplication-by-a-contraction bound**: for `X` and a contraction `W`,
> the Hilbert–Schmidt square sum of `X * W` never exceeds that of `X` itself, in the same basis.

```lean
lemma tsum_norm_sq_mul_right_le_of_opNorm_le_one {X W : H →L[ℂ] H} (hW : ‖W‖ ≤ 1)
    (hX : IsHilbertSchmidt X) {w : Set H} (b : HilbertBasis w ℂ H) :
    (∑' i : w, ‖(X * W) (b i)‖ ^ 2) ≤ ∑' i : w, ‖X (b i)‖ ^ 2
```

**`ProbabilisticTheory.HilbertSchmidt.tsum_norm_sq_mul_right_le_of_selfAdjoint`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean#L495).

> Right multiplication by a self-adjoint contraction does not increase the Hilbert–Schmidt sum.

```lean
lemma tsum_norm_sq_mul_right_le_of_selfAdjoint {S A : H →L[ℂ] H}
    (hSself : IsSelfAdjoint S) (hS : IsHilbertSchmidt S)
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H) :
    (∑' i : w', ‖(S * A) (c i)‖ ^ 2) ≤ ‖A‖ ^ 2 * (∑' j : w, ‖S (b j)‖ ^ 2)
```

## Depends on

- [Trace-class operators](traceclass-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/HilbertSchmidt.lean)
