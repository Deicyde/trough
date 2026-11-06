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

- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Connectedness](../../../overview/topology/general-topology/part-01/connectedness.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

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
- [1000+ theorems project: Q1227703](https://1000-plus.github.io/all.html?length=-1#Q1227703)
- [Wikipedia: Dirichlet's approximation theorem](https://en.wikipedia.org/wiki/Dirichlet's_approximation_theorem)
- [Wikidata: Q1227703](https://www.wikidata.org/wiki/Q1227703)
