---
declaration: section
origin: cited
lean: OAI.MetricEntropyDuality.exists_entropy_duality_counterexample_with_covers
statement: formalized
proof: formalized
---

# 329. A counterexample to metric-entropy duality

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Pietsch's dimension-free duality conjecture for metric entropy. Origin-symmetric convex bodies violate every proposed choice of universal constants in the conjectured comparison between covering numbers and those of the polar bodies, even when the covering body is a cube.

## Counterexamples to the duality conjecture for metric entropy

We disprove Pietsch's dimension-free duality conjecture for metric entropy. For every proposed pair of universal constants, we construct origin-symmetric convex bodies that violate the corresponding covering-entropy inequality, already when the covering body is a cube.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

Metric-entropy duality predicts a universal comparison between covering numbers of convex bodies and their polars. The formalized result disproves such a comparison: for every $a,b\ge1$, there is an origin-symmetric convex body $K$ in a positive finite dimension with $\log N(K,B_\infty)>b\log N(B_\infty^\circ,a^{-1}K^\circ)$, where $N$ is the least number of translates in a finite cover. A further construction makes the dual-to-primal logarithmic entropy ratio tend to zero as the dimension grows.

## Lean: Counterexample to metric-entropy duality

```lean
theorem exists_entropy_duality_counterexample_with_covers
    (a b : ℝ) (ha : 1 ≤ a) (hb : 1 ≤ b) :
    ∃ n : ℕ, 0 < n ∧ ∃ K : Set (RealSpace (Fin n)),
      IsSymmetricConvexBody K ∧
      Coverable K (cube (Fin n)) ∧
      Coverable (polar (cube (Fin n))) (a⁻¹ • polar K) ∧
      b * Real.log (coveringNumber (polar (cube (Fin n))) (a⁻¹ • polar K) : ℝ) <
        Real.log (coveringNumber K (cube (Fin n)) : ℝ)
```

Stated in [MetricEntropyDuality.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MetricEntropyDuality.lean#L45). Proved in [lean/OAI/Analysis/MetricEntropy/Main.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/MetricEntropy/Main.lean#L48). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/329.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/329.md)
