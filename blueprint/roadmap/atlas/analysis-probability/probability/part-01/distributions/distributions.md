---
declaration: section
origin: cited
lean: MathlibExt.Probability.map_prodMk_apply_prod
statement: formalized
proof: formalized
---

# Probability distributions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/index.html).

Named discrete and continuous laws and their moments, densities, mass functions and tails (binomial, Poisson-binomial, hypergeometric, negative binomial, beta, gamma, exponential, chi-square, Dirichlet, multivariate Gaussian and Gaussian conditioning, Gaussian orthant probabilities), expectation under a probability mass function, joint laws, distribution functions, quantiles and medians; sampling laws used in tests (t, F) go to Linear models and multivariate analysis.

## Joint law of two random variables on a rectangle

Let $P$ be a measure on a measurable
space $\Omega$, and let $X : \Omega \to \mathcal{X}$ and $Y : \Omega \to \mathcal{Y}$ be
$P$-almost everywhere measurable maps into measurable spaces. For measurable sets
$s \subseteq \mathcal{X}$ and $t \subseteq \mathcal{Y}$, the pushforward of $P$ under
$\omega \mapsto (X(\omega), Y(\omega))$ gives $s \times t$ the measure
$P(\{\omega : X(\omega) \in s \text{ and } Y(\omega) \in t\})$.

When $P$ is a probability measure this pushforward is the joint law of $X$ and $Y$, and the value
is the probability that both events occur.

Formalized by `MathlibExt.Probability.map_prodMk_apply_prod`, a theorem declared in [MathlibExt/Probability/JointLaw.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/JointLaw.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/index.html#map-prod-mk-apply-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probability distributions](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions)
