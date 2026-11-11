---
declaration: section
origin: cited
lean: Cslib.MachineLearning.InformationTheory.infoGain, Cslib.MachineLearning.InformationTheory.infoGain_eq, Cslib.MachineLearning.InformationTheory.infoGain_nonneg, Cslib.MachineLearning.InformationTheory.ofReal_infoGain, Cslib.MachineLearning.InformationTheory.infoGain_eq_zero_iff
statement: formalized
proof: formalized
---

# Information gain in decision trees

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html).

## Information gain of a split

Let $p$ be a joint probability law on $\alpha \times \beta$
with $\alpha$ and $\beta$ finite, the law of an attribute $X$ (first coordinate) and a label $Y$
(second coordinate). The information gain of splitting on $X$ for predicting $Y$ is the real
number $H(Y) - H(Y \mid X)$, where $H(Y)$ is the Shannon entropy in bits of the marginal law of
$Y$ and $H(Y \mid X)$ is the conditional entropy in bits of $Y$ given $X$ under $p$.

Formalized by `Cslib.MachineLearning.InformationTheory.infoGain`, a definition declared in [CSLibExt/MachineLearning/InformationTheory/InformationGain.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/InformationGain.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html#info-gain).

## Information gain in terms of entropies

Let $p$ be a joint probability law on
$\alpha \times \beta$ with $\alpha$ and $\beta$ finite, and let $p_X$ and $p_Y$ be its marginal
laws on $\alpha$ and on $\beta$. Writing $H$ for Shannon entropy in bits, the information gain of
$p$ equals $H(p_X) + H(p_Y) - H(p)$.

Formalized by `Cslib.MachineLearning.InformationTheory.infoGain_eq`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/InformationGain.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/InformationGain.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html#info-gain-eq).

## No split has negative information gain

For every joint probability law $p$ on
$\alpha \times \beta$ with $\alpha$ and $\beta$ finite, the information gain of $p$ is at least
$0$.

Formalized by `Cslib.MachineLearning.InformationTheory.infoGain_nonneg`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/InformationGain.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/InformationGain.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html#info-gain-nonneg).

## Information gain is mutual information

Let $\alpha$ and $\beta$ be finite sets carrying
σ-algebras in which singletons are measurable, and let $p$ be a joint probability law on
$\alpha \times \beta$. The information gain of $p$, regarded as an element of $[0, \infty]$, equals
the mutual information in bits of $p$ viewed as a probability measure on $\alpha \times \beta$.

Formalized by `Cslib.MachineLearning.InformationTheory.ofReal_infoGain`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/InformationGain.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/InformationGain.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html#of-real-info-gain).

## Zero information gain means independence

Let $\alpha$ and $\beta$ be finite sets carrying
σ-algebras in which singletons are measurable, and let $p$ be a joint probability law on
$\alpha \times \beta$. The information gain of $p$ is zero if and only if $p$, as a measure, equals
the product of its marginal law on $\alpha$ and its marginal law on $\beta$; that is, exactly when
the attribute (first coordinate) and the label (second coordinate) are independent.

Formalized by `Cslib.MachineLearning.InformationTheory.infoGain_eq_zero_iff`, a theorem declared in [CSLibExt/MachineLearning/InformationTheory/InformationGain.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/InformationTheory/InformationGain.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html#info-gain-eq-zero-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Information gain in decision trees](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/information-gain-in-decision-trees)
