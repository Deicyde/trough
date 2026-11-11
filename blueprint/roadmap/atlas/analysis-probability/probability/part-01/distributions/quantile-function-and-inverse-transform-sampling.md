---
declaration: section
origin: cited
lean: ProbabilityTheory.cdfQuantile, ProbabilityTheory.cdfQuantile_mem, ProbabilityTheory.cdfQuantile_le_iff, ProbabilityTheory.cdfQuantile_monoOn, ProbabilityTheory.measurable_cdfQuantile, ProbabilityTheory.map_cdfQuantile_restrict_Icc
statement: formalized
proof: formalized
---

# Quantile function and inverse transform sampling

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html).

## Quantile function of a real measure

Let $\mu$ be a measure on $\mathbb{R}$ with cumulative
distribution function $F_\mu$ (for a probability measure, $F_\mu(x) = \mu((-\infty, x])$). The
quantile function of $\mu$, the generalized inverse of $F_\mu$, is the function
$Q_\mu : \mathbb{R} \to \mathbb{R}$ given by
$Q_\mu(u) = \inf \lbrace x \in \mathbb{R} : u \le F_\mu(x) \rbrace$ for $u \in (0, 1)$ and
$Q_\mu(u) = 0$ for $u \notin (0, 1)$.

Formalized by `ProbabilityTheory.cdfQuantile`, a definition declared in [MathlibExt/Probability/Quantile.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#cdf-quantile).

## The cdf at the quantile is at least the level

Let $\mu$ be a measure on $\mathbb{R}$ with
cumulative distribution function $F_\mu$ and quantile function $Q_\mu$. For every $u \in (0, 1)$,
$u \le F_\mu(Q_\mu(u))$.

Formalized by `ProbabilityTheory.cdfQuantile_mem`, a theorem declared in [MathlibExt/Probability/Quantile.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#cdf-quantile-mem).

## The quantile function as a generalized inverse of the cdf

Let $\mu$ be a measure on
$\mathbb{R}$ with cumulative distribution function $F_\mu$ and quantile function $Q_\mu$. For
every $u \in (0, 1)$ and every real $x$, $Q_\mu(u) \le x$ if and only if $u \le F_\mu(x)$.

Formalized by `ProbabilityTheory.cdfQuantile_le_iff`, a theorem declared in [MathlibExt/Probability/Quantile.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#cdf-quantile-le-iff).

## Monotonicity of the quantile function

For every measure $\mu$ on $\mathbb{R}$, the quantile
function $Q_\mu$ is monotone on $(0, 1)$: if $0 < u \le v < 1$, then $Q_\mu(u) \le Q_\mu(v)$.

Formalized by `ProbabilityTheory.cdfQuantile_monoOn`, a theorem declared in [MathlibExt/Probability/Quantile.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#cdf-quantile-mono-on).

## Measurability of the quantile function

For every measure $\mu$ on $\mathbb{R}$, the
quantile function $Q_\mu : \mathbb{R} \to \mathbb{R}$ is measurable.

Formalized by `ProbabilityTheory.measurable_cdfQuantile`, a theorem declared in [MathlibExt/Probability/Quantile.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#measurable-cdf-quantile).

## Inverse transform sampling

Let $\mu$ be a probability measure on $\mathbb{R}$ with quantile
function $Q_\mu$. The pushforward under $Q_\mu$ of Lebesgue measure restricted to $[0, 1]$ is
$\mu$.

Formalized by `ProbabilityTheory.map_cdfQuantile_restrict_Icc`, a theorem declared in [MathlibExt/Probability/Quantile.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Quantile.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html#map-cdf-quantile-restrict-icc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quantile function and inverse transform sampling](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/quantile-function-and-inverse-transform-sampling)
