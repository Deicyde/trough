---
declaration: section
origin: cited
lean: OAI.TalagrandThreshold.talagrand_expectation_threshold_equivalence, OAI.TalagrandDiscreteConvexity.talagrand_discrete_convexity
statement: formalized
proof: formalized
---

# 175. Talagrand’s expectation thresholds, discrete convexity, and graph decompositions

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that integral and fractional expectation thresholds differ by at most a universal factor, and resolves Talagrand's discrete-convexity conjecture. An application proves the Ascoli–He–Park–Talagrand graph-decomposition conjecture: every graph's edges split into a universally bounded number of fixed pieces, each with containment threshold at most a universal constant times the original graph's integral expectation threshold. The pieces' embeddings need not agree on shared vertices.

## Graph Decompositions at the Integral Expectation Threshold

We prove the graph-decomposition conjecture of Ascoli, He, Park, and Talagrand. Every graph admits a partition into a universally bounded number of fixed edge pieces, each having ordinary containment threshold at most a universal constant times the original graph's integral expectation threshold. The partition is chosen before sampling the random host, and the separate embeddings of the pieces need not agree on shared vertices.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf).

## Integral and fractional expectation thresholds are equivalent

We prove Talagrand's conjecture that integral and fractional expectation thresholds are within a universal constant factor, with the same covering budget.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Talagrand’s discrete-convexity conjecture

We prove Talagrand's discrete-convexity conjecture. There is a universal integer *k* such that, whenever an arbitrary family has Bernoulli product measure at least $1-1/k$, the sets not contained in a union of *k* members admit a cover of total cost at most 1/2 at the same density.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Talagrand's expectation-threshold conjecture asks whether the fractional and integral expectation thresholds are comparable by an absolute constant. The formalized result proves $q_f(\mathcal F)\le25\cdot512^4 q(\mathcal F)$ for every nonempty proper increasing family on a finite nonempty ground set. Both thresholds use cover budget $1/2$, and fractional covers may assign weights to every subset, including the empty set.

The formalized result proves Talagrand's discrete-convexity assertion with $k=2^{75}$. If a family of subsets of a finite nonempty ground set has Bernoulli-$p$ measure at least $1-1/k$, then the sets not contained in a union of $k$ members form a $p$-small family: they have a containment cover of total $p$-cost at most $1/2$. This holds for every $0<p<1$, with repeated members allowed in the union and no monotonicity assumption.

## Lean: Integral–fractional expectation-threshold comparison

Stated in [TalagrandExpectationThreshold.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TalagrandExpectationThreshold.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem talagrand_expectation_threshold_equivalence [Nonempty α]
    (F : Family α) (_hF : F.Nonempty) (hproper : F ≠ Finset.univ)
    (hIncreasing : Increasing F) :
    qf F ≤ ((25 : ℝ) * (512 : ℝ) ^ 4) * q F
```

Proved in [lean/OAI/Combinatorics/ExpectationThreshold/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ExpectationThreshold/Main.lean#L21).

## Lean: Talagrand discrete convexity

Stated in [TalagrandDiscreteConvexity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TalagrandDiscreteConvexity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem talagrand_discrete_convexity (N : ℕ) (_hN : 1 ≤ N)
    (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (D : Family (Fin N))
    (hD : 1 - 1 / (2 : ℝ) ^ 75 ≤ familyMeasure p D) :
    Small p (exceptional ((2 : ℕ) ^ 75) D)
```

Proved in [lean/OAI/Combinatorics/DiscreteConvexity/Main.lean, line 61](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/DiscreteConvexity/Main.lean#L61).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/175.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/175.md)
