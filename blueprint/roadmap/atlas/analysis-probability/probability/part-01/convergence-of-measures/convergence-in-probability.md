---
declaration: section
origin: cited
lean: MathlibExt.Probability.ConvergenceInProbability.tendstoInMeasure_iff_tendsto_measure_abs_sub, MathlibExt.Probability.ConvergenceInProbability.convergence_in_probability_iff_subsequential_ae_convergence
statement: formalized
proof: formalized
---

# Convergence in probability

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/convergence-in-probability/index.html).

## Convergence in measure in the textbook ε-formulation

Let $\mu$ be a measure on a
measurable space $\Omega$, and let $X_n : \Omega \to \mathbb{R}$ ($n \in \mathbb{N}$) and
$Y : \Omega \to \mathbb{R}$ be functions. Then $X_n$ converges to $Y$ in $\mu$-measure, that is,
$\mu(\{\omega : |X_n(\omega) - Y(\omega)| \ge \varepsilon\}) \to 0$ as $n \to \infty$ for every
$\varepsilon \in (0, \infty]$, if and only if
$\mu(\{\omega : |X_n(\omega) - Y(\omega)| > \varepsilon\}) \to 0$ as $n \to \infty$ for every
real $\varepsilon > 0$.

The second condition is the definition of convergence in probability used in the book.

Formalized by `MathlibExt.Probability.ConvergenceInProbability.tendstoInMeasure_iff_tendsto_measure_abs_sub`, a theorem declared in [MathlibExt/Probability/ConvergenceInProbability.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ConvergenceInProbability.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/convergence-in-probability/index.html#tendsto-in-measure-iff-tendsto-measure-a).

## Convergence in probability via subsequential a.s. convergence

Let $\mu$ be a finite
measure on a measurable space $\Omega$, let $X_n : \Omega \to \mathbb{R}$ ($n \in \mathbb{N}$) be
$\mu$-almost everywhere strongly measurable functions, and let $Y : \Omega \to \mathbb{R}$ be any
function. Then $\mu(\{\omega : |X_n(\omega) - Y(\omega)| > \varepsilon\}) \to 0$ as
$n \to \infty$ for every real $\varepsilon > 0$ if and only if for every strictly increasing
sequence $(n_k)$ of natural numbers there is a strictly increasing sequence $(k_j)$ of natural
numbers such that $X_{n_{k_j}}(\omega) \to Y(\omega)$ as $j \to \infty$ for $\mu$-almost every
$\omega \in \Omega$.

## Sources

- Lecture 9, convergence in probability via subsequential a.s. convergence.

Formalized by `MathlibExt.Probability.ConvergenceInProbability.convergence_in_probability_iff_subsequential_ae_convergence`, a theorem declared in [MathlibExt/Probability/ConvergenceInProbability.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ConvergenceInProbability.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/convergence-in-probability/index.html#convergence-in-probability-iff-subsequen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence in probability](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/convergence-in-probability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/convergence-of-measures/convergence-in-probability)
