---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PadicInt.hasSum_mahler
mathlib_file: Mathlib/NumberTheory/Padics/MahlerBasis.lean
---

# Mahler's theorem

**Mahler's theorem**: for any continuous function `f` from `ℤ_[p]` to a `p`-adic Banach space, the
Mahler series with coefficients `n ↦ Δ_[1]^[n] f 0` converges to the original function `f`.

```lean
PadicInt.hasSum_mahler.{u_1} {p : ℕ} [hp : Fact (Nat.Prime p)] {E : Type u_1} [NormedAddCommGroup E]
  [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E] [IsUltrametricDist E] [CompleteSpace E]
  (f : C(ℤ_[p], E)) : HasSum (fun n => PadicInt.mahlerTerm ((fwdDiff 1)^[n] (⇑f) 0) n) f
```

## Depends on

- [$p$-adic integer](../../../overview/general-algebra/numbers/p-adic-integer.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Complete metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/complete-metric-spaces.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Heine-Cantor theorem](../../../overview/topology/uniform-notions/heine-cantor-theorem.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Prime ideal](../../../overview/general-algebra/ideals-and-quotients/prime-ideal.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Squeeze theorem](../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniform convergence](../../../overview/topology/uniform-notions/uniform-convergence.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `PadicInt.hasSum_mahler`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/MahlerBasis.html#PadicInt.hasSum_mahler)
- [Source of `PadicInt.hasSum_mahler` in Mathlib/NumberTheory/Padics/MahlerBasis.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Padics/MahlerBasis.lean#L331)
- [1000+ theorems list: Q3527118](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2495)
- [1000+ theorems project: Q3527118](https://1000-plus.github.io/?length=-1#Q3527118)
- [Wikipedia: Mahler's theorem](https://en.wikipedia.org/wiki/Mahler's_theorem)
- [Wikidata: Q3527118](https://www.wikidata.org/wiki/Q3527118)
