---
declaration: section
origin: cited
lean: OAI.MetricKMedianRecovery.global_application, OAI.MetricKMedianRecovery.RefinedRecovery.refined_recovery, OAI.MetricKMedian.threshold, OAI.MetricKMedian.main_finite_work
statement: formalized
proof: formalized
---

# 125. The metric \*k\*-median approximation threshold and recovery

2 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a deterministic polynomial-time $(1+2/e+\varepsilon)$-approximation for finite rational metric *k*-median with specified candidate facilities, for every fixed *ε* > 0. Assuming $P\ne NP$, the optimal infimum approximation factor is $1+2/e$.

## Single-exponential recovery and bounded-price strictness for metric k-median

We give an exact-budget recovery algorithm for metric *k*-median with single-exponential dependence on the number of comparison clusters without accurate, distinct proxies in a supplied anchor solution. On positive integral metrics of polynomially bounded diameter, a sufficiently small total proxy error and logarithmically many such clusters yield a $(1+2/e+\varepsilon)$ approximation in polynomial time with arbitrarily high success probability. We also prove bounded-price strictness for one compatible execution of the logarithmic-surplus construction. Together the recovery and payment arguments give a randomized $(2-\sigma)$ approximation, for an absolute *σ* > 0, on arbitrary finite rational metrics, both with high probability and in expectation, while opening at most *k* facilities on every output.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The approximation threshold for metric k-median

For every fixed *ε* > 0, we give a deterministic polynomial-time $(1+2/e+\varepsilon)$-approximation for finite rational metric *k*-median with specified candidate facilities, opening at most *k* facilities. Under $P\ne NP$, the infimum approximation factor in this model is therefore $1+2/e$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives an exact-budget recovery algorithm for metric $k$-median on the stated polynomially bounded integral metrics. Suppose a supplied anchor represents all but logarithmically many comparison clusters by distinct proxies, with total proxy cost at most the comparison cost plus a sufficiently small relative error. The algorithm always opens at most $k$ facilities and, with any requested confidence, attains a $(1+2/e+\varepsilon)$ factor relative to those comparison centers in polynomial time.

The linked final approximation result applies to arbitrary finite rational metrics. For one absolute $\sigma>0$, a polynomial-time fair-bit algorithm always returns a feasible solution, has expected cost at most $(2-\sigma)\mathrm{OPT}$, and attains the same factor with arbitrarily high polynomial confidence.

The formalization gives, for every fixed $\varepsilon>0$, a deterministic polynomial-time $(1+2/e+\varepsilon)$-approximation for metric $k$-median on finite rational metrics with specified candidate facilities. Every output is a nonempty subset of the candidate facilities and opens at most $k$ of them.

Assuming $P\ne NP$, it also proves that the infimum of all polynomial-time approximation factors in this model is exactly $1+2/e$.

## Lean: Randomized metric $k$-median approximation below two

Stated in [KMedianRecovery.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KMedianRecovery.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem global_application : globalApplicationClaim
```

Proved in [lean/OAI/Combinatorics/KMedianRecovery/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/KMedianRecovery/Main.lean#L21).

## Lean: Exact-budget recovery from accurate distinct cluster proxies

Stated in [KMedianRefinedRecovery.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KMedianRefinedRecovery.lean).

```lean
theorem refined_recovery :
    ∀ (bound : Polynomial ℕ) (ε L₀ : ℝ) (μ : ℚ),
      0 < ε → 0 < L₀ → 0 < μ → μ ≤ 1/4 → (μ : ℝ) ≤ ε/12 →
      ∃ A : BinaryRandomizedAlgorithm,
        PolynomialWork A bound ∧
        ∀ I : Input, I.Bounded bound → ∀ ζ : ℝ, 0 < ζ → ζ < 1 →
          (∀ s : Seed A I ζ, I.metric.Feasible (output A I ζ s)) ∧
          (∀ C : Certificate I μ L₀,
            1 - ζ ≤ successProbability A I ζ
              ((1 + 2 / Real.exp 1 + ε) * (I.metric.cost C.centers : ℝ)))
```

Proved in [lean/OAI/Combinatorics/KMedianRecovery/Refined/Recovery.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/KMedianRecovery/Refined/Recovery.lean#L11).

## Lean: Exact approximation threshold under $P\ne NP$

Stated in [KMedianThreshold.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KMedianThreshold.lean).

```lean
theorem threshold (h : Complexity.PNeNP) :
    sInf approximationFactors=1+2/Real.exp 1
```

Proved in [lean/OAI/Combinatorics/KMedian/Threshold.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/KMedian/Threshold.lean#L25).

## Lean: Deterministic metric $k$-median approximation at the threshold

Stated in [MetricKMedian.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MetricKMedian.lean).

```lean
theorem main_finite_work : ∀ ε : ℝ, 0 < ε →
    ∃ (algorithm : Instance → List Bool) (P : Turing.TM2ComputableInPolyTime encodeInstance id algorithm),
      (∀ k : P.tm.K, Finite (P.tm.Γ k)) ∧ ∀ I, Correct ε I (algorithm I)
```

Proved in [lean/OAI/Combinatorics/KMedian/Main.lean, line 54](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/KMedian/Main.lean#L54).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/125.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/125.md)
