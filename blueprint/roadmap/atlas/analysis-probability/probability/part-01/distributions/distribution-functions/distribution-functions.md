---
declaration: section
origin: cited
lean: MathlibExt.Probability.map_prodMk_apply_prod
statement: formalized
proof: formalized
---

# Distribution functions and quantiles: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/index.html).

Cumulative distribution functions and their continuity points, quantile functions and inverse transform sampling, medians, and joint laws.

## Joint law of two random variables on a rectangle

Let $P$ be a measure on a measurable
space $\Omega$, and let $X : \Omega \to \mathcal{X}$ and $Y : \Omega \to \mathcal{Y}$ be
$P$-almost everywhere measurable maps into measurable spaces. For measurable sets
$s \subseteq \mathcal{X}$ and $t \subseteq \mathcal{Y}$, the pushforward of $P$ under
$\omega \mapsto (X(\omega), Y(\omega))$ gives $s \times t$ the measure
$P(\{\omega : X(\omega) \in s \text{ and } Y(\omega) \in t\})$.

When $P$ is a probability measure this pushforward is the joint law of $X$ and $Y$, and the value
is the probability that both events occur.

Formalized by `MathlibExt.Probability.map_prodMk_apply_prod`, a theorem declared in [MathlibExt/Probability/JointLaw.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/JointLaw.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/index.html#map-prod-mk-apply-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distribution functions and quantiles](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/distribution-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/distribution-functions)
