---
declaration: section
origin: cited
lean: MetaMathlibExt.khintchine_inequality, ProbabilityTheory.paley_zygmund
statement: formalized
proof: formalized
---

# Concentration inequalities: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/index.html).

Non-asymptotic tail and moment bounds: Hoeffding, McDiarmid, Efron–Stein, Khintchine and Paley–Zygmund inequalities, sampling without replacement, sub-Gaussian convex comparison, and hypercontractivity (Bonami–Beckner, p-biased two-point inequalities) on the discrete cube.

## Khintchine inequality

For every real $p > 0$ there are constants $A_p > 0$ and $B_p > 0$
such that the following holds for every $N \in \mathbb{N}$, all real numbers $a_1, \dots, a_N$
and every probability space. Let $\varepsilon_1, \dots, \varepsilon_N$ be independent measurable
random variables, each almost surely equal to $1$ or $-1$ and each with mean $0$, and let
$S = \sum_{i=1}^N a_i \varepsilon_i$ and $\|a\|_2 = \big(\sum_{i=1}^N a_i^2\big)^{1/2}$. Then

$$A_p \|a\|_2 \le \big(\mathbb{E}\,|S|^p\big)^{1/p} \le B_p \|a\|_2.$$

## Sources

- https://en.wikipedia.org/wiki/Khintchine_inequality

Formalized by `MetaMathlibExt.khintchine_inequality`, a theorem declared in [MathlibExt/Probability/KhintchineInequality.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KhintchineInequality.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/index.html#khintchine-inequality).

## The Paley–Zygmund inequality

Let $Z$ be a real random variable on a probability space with
probability measure $\mathbb{P}$, such that $Z \ge 0$ almost surely and $\mathbb{E}[Z^2] < \infty$,
and let $\theta$ be a real number with $0 \le \theta \le 1$. Then

$$(1-\theta)^2 (\mathbb{E}[Z])^2 \le \mathbb{E}[Z^2] \, \mathbb{P}(Z > \theta \, \mathbb{E}[Z]).$$

When $\mathbb{E}[Z^2] > 0$, this says
$\mathbb{P}(Z > \theta \, \mathbb{E}[Z]) \ge (1 - \theta)^2 (\mathbb{E}[Z])^2 / \mathbb{E}[Z^2]$.

Formalized by `ProbabilityTheory.paley_zygmund`, a theorem declared in [MathlibExt/Probability/PaleyZygmund.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PaleyZygmund.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/index.html#paley-zygmund).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Concentration inequalities](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/concentration-inequalities)
