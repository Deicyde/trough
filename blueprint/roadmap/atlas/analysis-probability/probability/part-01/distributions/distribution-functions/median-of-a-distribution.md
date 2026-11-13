---
declaration: section
origin: cited
lean: ProbabilityTheory.IsMedian, ProbabilityTheory.integrable_abs_sub_iff, ProbabilityTheory.integral_abs_sub_le_of_isMedian
statement: formalized
proof: formalized
---

# Median of a distribution

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution/index.html).

## Median of a measure on the real line

Let $\nu$ be a measure on $\mathbb{R}$, typically a
probability measure. A real number $m$ is a median of $\nu$ when $\nu((-\infty, m]) \ge 1/2$
and $\nu([m, \infty)) \ge 1/2$, where a set of infinite measure counts as having measure $0$.

Formalized by `ProbabilityTheory.IsMedian`, a definition declared in [MathlibExt/Probability/Median.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Median.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution/index.html#is-median).

## Absolute deviations are integrable exactly when the mean exists

Let $\nu$ be a finite
measure on $\mathbb{R}$ and let $c \in \mathbb{R}$. Then $\theta \mapsto |\theta - c|$ is
$\nu$-integrable if and only if $\theta \mapsto \theta$ is $\nu$-integrable.

Formalized by `ProbabilityTheory.integrable_abs_sub_iff`, a theorem declared in [MathlibExt/Probability/Median.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Median.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution/index.html#integrable-abs-sub-iff).

## A median minimizes the expected absolute loss

Let $\nu$ be a probability measure on
$\mathbb{R}$ and let $m$ be a median of $\nu$. Then for every $y \in \mathbb{R}$,

$$
\int |\theta - m| \, d\nu(\theta) \le \int |\theta - y| \, d\nu(\theta).
$$

When $\nu$ has no first moment, neither integrand is integrable and both integrals are $0$ by
the convention for non-integrable functions.

Formalized by `ProbabilityTheory.integral_abs_sub_le_of_isMedian`, a theorem declared in [MathlibExt/Probability/Median.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Median.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution/index.html#integral-abs-sub-le-of-is-median).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Median of a distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/distribution-functions/median-of-a-distribution)
