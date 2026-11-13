---
declaration: section
origin: cited
lean: MathlibExt.Probability.ScottishBook161Wanted.LacunaryCLT, MathlibExt.Probability.ScottishBook161Wanted.kacLacunaryCentralLimitTheorem
statement: formalized
---

# Lacunary central limit theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lacunary-central-limit-theorem/index.html).

## Central limit theorem for lacunary sine sums

A sequence of integers $(r_k)_{k \ge 0}$
satisfies the central limit theorem for lacunary sine sums if for all real numbers $a < b$, the
Lebesgue measure of the set of $x \in [0, 1]$ with
$a < \frac{1}{\sqrt{n}} \sum_{k=0}^{n-1} \sin(2 \pi r_k x) < b$ tends to
$\frac{1}{\sqrt{\pi}} \int_a^b e^{-y^2} \, dy$ as $n \to \infty$.

Formalized by `MathlibExt.Probability.ScottishBook161Wanted.LacunaryCLT`, a definition declared in [WantedExt/Probability/ScottishBook161Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ScottishBook161Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lacunary-central-limit-theorem/index.html#lacunary-clt).

## Kac's lacunary central limit theorem

Let $(r_n)_{n \ge 0}$ be a sequence of integers such
that $r_n - (r_0 + r_1 + \dots + r_{n-1})$ tends to $+\infty$ as $n \to \infty$. Then $(r_n)$
satisfies the central limit theorem for lacunary sine sums. The sequence $r_n = 2^n$ satisfies
it as well.

The sequence $r_n = 2^n$ does not satisfy the gap hypothesis, since
$2^n - (1 + 2 + \dots + 2^{n-1}) = 1$ for every $n$. The sequence $r_n = 2^{n^2}$ is the example
given in the problem that does satisfy it.

## Sources

- M. Kac, Problem 161 of the Scottish Book; the `2ⁿ` case is affirmative by R. Salem and A. Zygmund, "On lacunary trigonometric series", Proc. Natl. Acad. Sci. USA 33 (1947), 333-338, who proved the central limit theorem for lacunary trigonometric series with ratio bounded away from `1`.

Stated but not proved: `MathlibExt.Probability.ScottishBook161Wanted.kacLacunaryCentralLimitTheorem` is written with `theorem_wanted` in [WantedExt/Probability/ScottishBook161Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ScottishBook161Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lacunary-central-limit-theorem/index.html#kac-lacunary-central-limit-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lacunary central limit theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lacunary-central-limit-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/central-limit-theorems/lacunary-central-limit-theorem)
