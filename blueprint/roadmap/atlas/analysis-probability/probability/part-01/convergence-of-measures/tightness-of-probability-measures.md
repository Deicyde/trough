---
declaration: section
origin: cited
lean: MathlibExt.Probability.TightnessFamily.IsTightFamily, MathlibExt.Probability.TightnessFamily.IsTightFamilyReal, MathlibExt.Probability.TightnessFamily.IsTightFamilyReal.isTightFamily, MathlibExt.Probability.TightnessFamily.IsTightFamily.isTightFamilyReal, MathlibExt.Probability.TightnessFamily.isTightFamily_iff_isTightMeasureSet, MathlibExt.Probability.TightnessFamily.isTightFamily_of_singleton
statement: formalized
proof: formalized
---

# Tightness of probability measures

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html).

## Tight family of probability measures

Let $\alpha$ be a space carrying a σ-algebra and a
topology. A family $(\mu_i)_{i \in \iota}$ of probability measures on $\alpha$ is tight if its
range $\{\mu_i : i \in \iota\}$ is a tight set of measures: for every $\varepsilon \in (0, \infty]$
there is a compact set $K \subseteq \alpha$ such that $\mu_i(\alpha \setminus K) \le \varepsilon$
for every index $i$.

Formalized by `MathlibExt.Probability.TightnessFamily.IsTightFamily`, a definition declared in [MathlibExt/Probability/TightnessFamily.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family).

## Tightness on the real line

A family $(\mu_i)_{i \in \iota}$ of probability measures on
$\mathbb{R}$ is tight in the real-line sense if for every $\varepsilon \in (0, \infty]$ there is
$M \in \mathbb{R}$ such that $\mu_i([-M, M]) \ge 1 - \varepsilon$ for every index $i$.

Formalized by `MathlibExt.Probability.TightnessFamily.IsTightFamilyReal`, a definition declared in [MathlibExt/Probability/TightnessFamily.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family-real).

## Real-line tightness implies tightness

Let $(\mu_i)_{i \in \iota}$ be a family of
probability measures on $\mathbb{R}$. If the family is tight in the real-line sense, that is,
for every $\varepsilon \in (0, \infty]$ there is $M \in \mathbb{R}$ with
$\mu_i([-M, M]) \ge 1 - \varepsilon$ for every $i$, then the family is tight, that is, for every
$\varepsilon \in (0, \infty]$ there is a compact set $K \subseteq \mathbb{R}$ with
$\mu_i(\mathbb{R} \setminus K) \le \varepsilon$ for every $i$.

The interval $[-M, M]$ is compact.

Formalized by `MathlibExt.Probability.TightnessFamily.IsTightFamilyReal.isTightFamily`, a theorem declared in [MathlibExt/Probability/TightnessFamily.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family-2).

## Tight families on the real line concentrate on bounded intervals

Let
$(\mu_i)_{i \in \iota}$ be a family of probability measures on $\mathbb{R}$. If the family is
tight, that is, for every $\varepsilon \in (0, \infty]$ there is a compact set
$K \subseteq \mathbb{R}$ with $\mu_i(\mathbb{R} \setminus K) \le \varepsilon$ for every $i$, then
it is tight in the real-line sense: for every $\varepsilon \in (0, \infty]$ there is
$M \in \mathbb{R}$ with $\mu_i([-M, M]) \ge 1 - \varepsilon$ for every $i$.

The proof encloses the compact set in a closed ball.

Formalized by `MathlibExt.Probability.TightnessFamily.IsTightFamily.isTightFamilyReal`, a theorem declared in [MathlibExt/Probability/TightnessFamily.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family-real-2).

## Tightness of a family is tightness of its range

Let $\alpha$ be a space carrying a
σ-algebra and a topology. A family $(\mu_i)_{i \in \iota}$ of probability measures on $\alpha$ is
tight exactly when its range $\{\mu_i : i \in \iota\}$ is a tight set of measures.

Formalized by `MathlibExt.Probability.TightnessFamily.isTightFamily_iff_isTightMeasureSet`, a theorem declared in [MathlibExt/Probability/TightnessFamily.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family-iff-is-tight-measure-set).

## Constant families on the real line are tight

For every index type $\iota$ and every
probability measure $\mu$ on $\mathbb{R}$, the constant family $(\mu)_{i \in \iota}$ is tight.

Formalized by `MathlibExt.Probability.TightnessFamily.isTightFamily_of_singleton`, a theorem declared in [MathlibExt/Probability/TightnessFamily.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/TightnessFamily.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html#is-tight-family-of-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tightness of probability measures](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/convergence-of-measures/tightness-of-probability-measures)
