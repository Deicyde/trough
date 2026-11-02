---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AddCircle.exists_norm_nsmul_le, Real.exists_int_int_abs_mul_sub_le, Real.exists_nat_abs_mul_sub_round_le, Real.exists_rat_abs_sub_le_and_den_le
mathlib_file: Mathlib/NumberTheory/WellApproximable.lean
---

# Dirichlet's approximation theorem

Mathlib records this with 4 declarations.

`AddCircle.exists_norm_nsmul_le`: **Dirichlet's approximation theorem**

See also `Real.exists_rat_abs_sub_le_and_den_le`.

```lean
AddCircle.exists_norm_nsmul_le {T : ℝ} [hT : Fact (0 < T)] (ξ : AddCircle T) {n : ℕ} (hn : 0 < n) :
  ∃ j ∈ Set.Icc 1 n, ‖j • ξ‖ ≤ T / ↑(n + 1)
```

`Real.exists_int_int_abs_mul_sub_le`: *Dirichlet's approximation theorem:*
For any real number `ξ` and positive natural `n`, there are integers `j` and `k`,
with `0 < k ≤ n` and `|k*ξ - j| ≤ 1/(n+1)`.

See also `Real.exists_nat_abs_mul_sub_round_le`.

```lean
Real.exists_int_int_abs_mul_sub_le (ξ : ℝ) {n : ℕ} (n_pos : 0 < n) :
  ∃ j k, 0 < k ∧ k ≤ ↑n ∧ |↑k * ξ - ↑j| ≤ 1 / (↑n + 1)
```

`Real.exists_nat_abs_mul_sub_round_le`: *Dirichlet's approximation theorem:*
For any real number `ξ` and positive natural `n`, there is a natural number `k`,
with `0 < k ≤ n` such that `|k*ξ - round(k*ξ)| ≤ 1/(n+1)`.

```lean
Real.exists_nat_abs_mul_sub_round_le (ξ : ℝ) {n : ℕ} (n_pos : 0 < n) :
  ∃ k, 0 < k ∧ k ≤ n ∧ |↑k * ξ - ↑(round (↑k * ξ))| ≤ 1 / (↑n + 1)
```

`Real.exists_rat_abs_sub_le_and_den_le`: *Dirichlet's approximation theorem:*
For any real number `ξ` and positive natural `n`, there is a fraction `q`
such that `q.den ≤ n` and `|ξ - q| ≤ 1/((n+1)*q.den)`.

See also `AddCircle.exists_norm_nsmul_le`.

```lean
Real.exists_rat_abs_sub_le_and_den_le (ξ : ℝ) {n : ℕ} (n_pos : 0 < n) :
  ∃ q, |ξ - ↑q| ≤ 1 / ((↑n + 1) * ↑q.den) ∧ q.den ≤ n
```

## Depends on

- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Proof depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Connected components](../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../../overview/topology/general-topology/part-01/connectedness.md)
- [Continuity of inverse functions](../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-inverse-functions.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Path connectedness](../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Product of sigma-algebras](../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)

## Sources

- [Mathlib documentation: `AddCircle.exists_norm_nsmul_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/WellApproximable.html#AddCircle.exists_norm_nsmul_le)
- [Source of `AddCircle.exists_norm_nsmul_le` in Mathlib/NumberTheory/WellApproximable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/WellApproximable.lean#L354)
- [Mathlib documentation: `Real.exists_int_int_abs_mul_sub_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/Basic.html#Real.exists_int_int_abs_mul_sub_le)
- [Source of `Real.exists_int_int_abs_mul_sub_le` in Mathlib/NumberTheory/DiophantineApproximation/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean#L89)
- [Mathlib documentation: `Real.exists_nat_abs_mul_sub_round_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/Basic.html#Real.exists_nat_abs_mul_sub_round_le)
- [Source of `Real.exists_nat_abs_mul_sub_round_le` in Mathlib/NumberTheory/DiophantineApproximation/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean#L130)
- [Mathlib documentation: `Real.exists_rat_abs_sub_le_and_den_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/Basic.html#Real.exists_rat_abs_sub_le_and_den_le)
- [Source of `Real.exists_rat_abs_sub_le_and_den_le` in Mathlib/NumberTheory/DiophantineApproximation/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean#L141)
- [1000+ theorems list: Q1227703](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1554)
- [1000+ theorems project: Q1227703](https://1000-plus.github.io/?length=-1#Q1227703)
- [Wikipedia: Dirichlet's approximation theorem](https://en.wikipedia.org/wiki/Dirichlet's_approximation_theorem)
- [Wikidata: Q1227703](https://www.wikidata.org/wiki/Q1227703)
