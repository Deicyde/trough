---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.NeymanPearson.neyman_pearson_dominated_two_simple
statement: formalized
proof: formalized
---

# Hypothesis testing: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/index.html).

Tests and their validity and power: Neyman–Pearson, likelihood-ratio, score and Wald tests, monotone likelihood ratio, exact conditional tests (Fisher, Hardy–Weinberg), rank tests and ROC area (Mann–Whitney), permutation p-values, multiple testing (Bonferroni, Holm, closed testing, Benjamini–Hochberg, false discovery rates), and meta-analysis and heterogeneity statistics.

## Neyman–Pearson lemma

Let $\mu$ be a measure on a measurable space $\Omega$, and let
$p, q : \Omega \to \mathbb{R}$ be measurable, nonnegative and $\mu$-integrable. Let $k \ge 0$ be a
real number and let $\varphi^\star : \Omega \to [0, 1]$ be measurable with $\varphi^\star(x) = 1$
whenever $q(x) > k\,p(x)$ and $\varphi^\star(x) = 0$ whenever $q(x) < k\,p(x)$. Then every
measurable test $\varphi : \Omega \to [0, 1]$ satisfying
$\int \varphi\, p \, d\mu \le \int \varphi^\star p \, d\mu$ also satisfies
$\int \varphi\, q \, d\mu \le \int \varphi^\star q \, d\mu$.

No normalization of $p$ or $q$ and no condition on $\varphi^\star$ on the set where $q = k\,p$ are
assumed.

## Sources

- J. Neyman and E. S. Pearson, "On the problem of the most efficient tests of statistical hypotheses", Phil. Trans. R. Soc. Lond. A 231 (1933), 289–337, DOI `10.1098/rsta.1933.0009`.

Formalized by `MathlibExt.Probability.Statistics.NeymanPearson.neyman_pearson_dominated_two_simple`, a theorem declared in [MathlibExt/Probability/Statistics/NeymanPearson.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/NeymanPearson.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/index.html#neyman-pearson-dominated-two-simple).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypothesis testing](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing)
