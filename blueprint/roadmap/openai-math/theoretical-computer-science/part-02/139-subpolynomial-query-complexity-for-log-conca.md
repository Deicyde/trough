---
declaration: section
origin: cited
lean: OAI.LogConcaveSampling.exact_source_main
statement: formalized
proof: formalized
---

# 139. Subpolynomial query complexity for log-concave sampling

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For $C^{2}$ potentials with a supplied minimizer and $I\preceq\nabla^2V\preceq2I$, proves that sampling within total variation 1/10 requires only $C_\varepsilon d^\varepsilon$ exact value-and-gradient queries for every fixed *ε* > 0. The bound holds on every run, with unrestricted computation between queries. A logarithmic lower bound also holds, so the optimal power-law exponent in this oracle model is zero.

## Subpolynomial query complexity for well-conditioned log-concave sampling

For every fixed *ε* > 0, we give a sampling algorithm using at most $C_\varepsilon d^\varepsilon$ exact first-order queries on every execution for $C^{2}$ potentials on ℝ$^{d}$ with a known minimizer and Hessian between $I_{d}$ and $2I_d$. The output has total-variation distance at most 1/10 from the target Gibbs law. Computation between queries is unrestricted. We also prove an $\Omega(\log d)$ query lower bound for arbitrary randomized adaptive algorithms, determining the optimal dimension exponent to be zero.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result determines the dimension exponent of exact value-and-gradient query complexity for well-conditioned log-concave sampling. For potentials with $V(0)=0$, $\nabla V(0)=0$, and $I\le\nabla^2V\le2I$, the least worst-case query budget achieving total-variation error at most $1/10$ is at most $C_\varepsilon d^\varepsilon$ for every $\varepsilon>0$, and at least $c\log d$ eventually. Hence the infimal polynomial exponent is zero. Algorithms may be measurable, randomized, and adaptive; arithmetic and bit costs are not bounded.

## Lean: Subpolynomial query complexity for log-concave sampling

```lean
theorem exact_source_main :
    (∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ d : ℕ, 2 ≤ d →
      (queryComplexity d).toENNReal ≤ ENNReal.ofReal (C * (d : ℝ) ^ ε)) ∧
    (∃ c : ℝ, 0 < c ∧ ∃ d₀ : ℕ, 2 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
      ENNReal.ofReal (c * Real.log (d : ℝ)) ≤ (queryComplexity d).toENNReal) ∧
    gammaStar = 0
```

Stated in [LogConcaveQuery.lean, line 81](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LogConcaveQuery.lean#L81). Proved in [lean/OAI/Probability/LogConcave/Main.lean, line 68](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/LogConcave/Main.lean#L68). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/139.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/139.md)
