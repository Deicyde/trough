---
declaration: section
origin: cited
lean: Real.sum_mul_log_sum_div_sum_le_sum_mul_log_div, MathlibExt.InformationTheory.Pinsker.csiszar_kullback_pinsker
statement: formalized
proof: formalized
---

# Information inequalities: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/index.html).

Inequalities relating entropies, divergences and mutual information, such as the log-sum, Pinsker, Fano, data-processing and Shearer inequalities.

## Log-sum inequality

Let $s$ be a finite subset of a type $\iota$ and let
$p, q : \iota \to \mathbb{R}$ satisfy $p_i \ge 0$ and $q_i > 0$ for all $i \in s$. Then

$$
\Bigl(\sum_{i \in s} p_i\Bigr) \log \frac{\sum_{i \in s} p_i}{\sum_{i \in s} q_i}
\le \sum_{i \in s} p_i \log \frac{p_i}{q_i}.
$$

Here $\log$ is the natural logarithm; a summand with $p_i = 0$ is $0$, and both sides are $0$
when $s$ is empty.

Formalized by `Real.sum_mul_log_sum_div_sum_le_sum_mul_log_div`, a theorem declared in [MathlibExt/InformationTheory/LogSum.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/LogSum.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/index.html#sum-mul-log-sum-div-sum-le-sum-mul-log-d).

## Csiszár–Kullback–Pinsker inequality for strictly positive distributions

Let $\alpha$ be a
finite nonempty set and let $p, q : \alpha \to \mathbb{R}$ satisfy $p(a) > 0$ and $q(a) > 0$
for every $a \in \alpha$ and $\sum_a p(a) = \sum_a q(a) = 1$. Then, with the natural logarithm,

$$
\Bigl(\sum_{a \in \alpha} |p(a) - q(a)|\Bigr)^2
\le 2 \sum_{a \in \alpha} p(a) \log \frac{p(a)}{q(a)}.
$$

Equivalently, the total variation distance $\frac12 \sum_a |p(a) - q(a)|$ is at most
$\sqrt{D/2}$, where $D = \sum_a p(a) \log (p(a)/q(a))$ is the Kullback–Leibler divergence.

## Sources

- M. S. Pinsker, Information and Information Stability of Random Variables and Processes (1960; English translation 1964), with I. Csiszar, Information-type measures of difference of probability distributions and indirect observations, Studia Sci. Math. Hungar. 2 (1967), 299-318.

Formalized by `MathlibExt.InformationTheory.Pinsker.csiszar_kullback_pinsker`, a theorem declared in [MathlibExt/InformationTheory/Pinsker.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/Pinsker.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/index.html#csiszar-kullback-pinsker).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Information inequalities](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/information-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/information-inequalities)
