---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: hensels_lemma
mathlib_file: Mathlib/NumberTheory/Padics/Hensel.lean
---

# Hensel's lemma (for $\mathbb{Z}_p$)

Mathlib states this as `hensels_lemma`.

```lean
hensels_lemma.{u_1} {p : ℕ} [Fact (Nat.Prime p)] {R : Type u_1} [CommSemiring R] [Algebra R ℤ_[p]]
  {F : Polynomial R} {a : ℤ_[p]}
  (hnorm : ‖(Polynomial.aeval a) F‖ < ‖(Polynomial.aeval a) (Polynomial.derivative F)‖ ^ 2) :
  ∃ z,
    (Polynomial.aeval z) F = 0 ∧
      ‖z - a‖ < ‖(Polynomial.aeval a) (Polynomial.derivative F)‖ ∧
        ‖(Polynomial.aeval z) (Polynomial.derivative F)‖ =
            ‖(Polynomial.aeval a) (Polynomial.derivative F)‖ ∧
          ∀ (z' : ℤ_[p]),
            (Polynomial.aeval z') F = 0 →
              ‖z' - a‖ < ‖(Polynomial.aeval a) (Polynomial.derivative F)‖ → z' = z
```

## Depends on

- [$p$-adic integer](../numbers/p-adic-integer.md)
- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)

## Proof depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `hensels_lemma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/Hensel.html#hensels_lemma)
- [Source of `hensels_lemma` in Mathlib/NumberTheory/Padics/Hensel.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Padics/Hensel.lean#L460)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L150)
