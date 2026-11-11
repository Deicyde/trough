---
declaration: section
origin: cited
lean: InformationTheory.FiniteJointLaw, InformationTheory.FiniteJointLaw.inputLaw, InformationTheory.FiniteJointLaw.outputLaw, InformationTheory.FiniteJointLaw.mutualInformation, InformationTheory.FiniteExtension, InformationTheory.FiniteExtension.trivial, InformationTheory.FiniteExtension.auxiliaryLaw, InformationTheory.FiniteExtension.inputAuxiliaryLaw
statement: formalized
proof: formalized
---

# One-shot channel simulation

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html).

## Finite joint law

A finite joint law consists of positive integers $n_X$ and $n_Y$
and a probability distribution on $\{0, \dots, n_X - 1\} \times \{0, \dots, n_Y - 1\}$.

Formalized by `InformationTheory.FiniteJointLaw`, a structure declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#finite-joint-law).

## Input law

The input law of a finite joint law $p$ on
$\{0, \dots, n_X - 1\} \times \{0, \dots, n_Y - 1\}$ is its first marginal: the law on
$\{0, \dots, n_X - 1\}$ that is the image of $p$ under $(x, y) \mapsto x$.

Formalized by `InformationTheory.FiniteJointLaw.inputLaw`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#input-law).

## Output law

The output law of a finite joint law $p$ of an input $X$ and an output $Y$
is the law of $Y$: the marginal of $p$ on the output alphabet, obtained by pushing $p$ forward
along the projection onto the second coordinate.

Formalized by `InformationTheory.FiniteJointLaw.outputLaw`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-law).

## Mutual information

The mutual information of a finite joint law $p$ of $(X, Y)$ is
$I(X; Y) = H(X) + H(Y) - H(X, Y)$, where $H(X)$ and $H(Y)$ are the Shannon entropies in bits
of the input and output laws of $p$, and $H(X, Y)$ is the Shannon entropy in bits of $p$.

Formalized by `InformationTheory.FiniteJointLaw.mutualInformation`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#mutual-information).

## Finite extension of a joint law

A finite extension of a finite joint law $p$ on
$\{0, \dots, n_X - 1\} \times \{0, \dots, n_Y - 1\}$ consists of a positive integer $n_S$ and a
probability law on triples $(x, y, s)$ with $s \in \{0, \dots, n_S - 1\}$ whose marginal on the
pairs $(x, y)$ is exactly $p$.

Formalized by `InformationTheory.FiniteExtension`, a structure declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#finite-extension).

## Trivial extension

The trivial extension of a finite joint law $p$ of an input $X$ and an
output $Y$ has the one-letter auxiliary alphabet $\{0\}$ and, as its law, the law of
$((X, Y), 0)$ for $(X, Y)$ distributed according to $p$; its $(X, Y)$ marginal is $p$.

Formalized by `InformationTheory.FiniteExtension.trivial`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#trivial).

## Auxiliary marginal of an extension

For a finite extension $q$ of a finite joint law $p$,
viewed as the law of a triple $(X, Y, S)$ with $S$ taking values in $\{0, \dots, n_S - 1\}$, the
auxiliary law is the marginal law of $S$ under $q$.

Formalized by `InformationTheory.FiniteExtension.auxiliaryLaw`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#auxiliary-law).

## Input-auxiliary law

Let $q$ be a finite extension of a finite joint law of $(X, Y)$,
that is, a law of $((X, Y), S)$ with an auxiliary variable $S$. Its input-auxiliary law is the
joint law of $(X, S)$: the image of the law of $q$ under $((x, y), s) \mapsto (x, s)$.

Formalized by `InformationTheory.FiniteExtension.inputAuxiliaryLaw`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#input-auxiliary-law).

## Output-auxiliary law

Let $q$ be a finite extension of a finite joint law of $(X, Y)$,
that is, a law of $((X, Y), S)$ with an auxiliary variable $S$. Its output-auxiliary law is the
joint law of $(Y, S)$: the image of the law of $q$ under $((x, y), s) \mapsto (y, s)$.

Formalized by `InformationTheory.FiniteExtension.outputAuxiliaryLaw`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-auxiliary-law).

## Mutual information between the input and the auxiliary

For a finite extension $q$ of a
finite joint law $p$, viewed as the law of a triple $(X, Y, S)$ whose $(X, Y)$ marginal is $p$,
this is $I(X; S) = H(X) + H(S) - H(X, S)$, where $H(X)$ is the Shannon entropy in bits of the
$X$ marginal of $p$, and $H(S)$ and $H(X, S)$ are the Shannon entropies in bits of the $S$ and
$(X, S)$ marginals of $q$.

Formalized by `InformationTheory.FiniteExtension.auxiliaryInformation`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#auxiliary-information).

## Conditional entropy of the output given the auxiliary

For a finite extension $q$ of a
finite joint law $p$, viewed as the law of a triple $(X, Y, S)$ whose $(X, Y)$ marginal is $p$,
this is $H(Y \mid S) = H(Y, S) - H(S)$, where $H(Y, S)$ and $H(S)$ are the Shannon entropies in
bits of the $(Y, S)$ and $S$ marginals of $q$.

Formalized by `InformationTheory.FiniteExtension.conditionalEntropy`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-entropy).

## Conditional entropy of the output given the input and the auxiliary

For a finite
extension of a finite joint law, with input $X$, output $Y$ and auxiliary $S$, the conditional
entropy of $Y$ given $(X, S)$ is $H(Y \mid X, S) = H(X, Y, S) - H(X, S)$, where $H$ denotes
Shannon entropy in bits, $H(X, Y, S)$ is the entropy of the law of the extension and $H(X, S)$
is the entropy of its $(X, S)$ marginal.

It vanishes exactly when $Y$ is almost surely a deterministic function of $(X, S)$.

Formalized by `InformationTheory.FiniteExtension.outputGivenInputAuxiliaryEntropy`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-given-input-auxiliary-entropy).

## Zero output entropy given input and auxiliary for a one-letter output

Let $p$ be a
finite joint law of an input $X$ and an output $Y$ whose output alphabet has exactly one letter.
Then for every finite extension of $p$ by an auxiliary $S$, the conditional entropy
$H(Y \mid X, S)$ of the output given the input and the auxiliary is $0$.

Formalized by `InformationTheory.FiniteExtension.outputGivenInputAuxiliaryEntropy_eq_zero_of_output_subsingleton`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-given-input-auxiliary-entropy-eq).

## Auxiliary law of the trivial extension

For every finite joint law $p$, the auxiliary law
of the trivial extension of $p$ is the point mass at $0$, the only letter of its one-letter
auxiliary alphabet $\{0\}$.

Formalized by `InformationTheory.FiniteExtension.trivial_auxiliaryLaw`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#trivial-auxiliary-law).

## The trivial extension has zero auxiliary information

For every finite joint law $p$, the
mutual information $I(X; S)$ between the input $X$ and the auxiliary $S$ in the trivial extension
of $p$, whose auxiliary alphabet has a single letter, is $0$.

Formalized by `InformationTheory.FiniteExtension.trivial_auxiliaryInformation`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#trivial-auxiliary-information).

## Conditional entropy in the trivial extension

For every finite joint law $p$ of an input
$X$ and an output $Y$, the conditional entropy $H(Y \mid S)$ of the output given the auxiliary
$S$ in the trivial extension of $p$ equals the Shannon entropy $H(Y)$ of the output law of $p$.

Formalized by `InformationTheory.FiniteExtension.trivial_conditionalEntropy`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#trivial-conditional-entropy).

## Input marginal of the input-auxiliary law

Let $q$ be a finite extension of a finite
joint law $p$ of $(X, Y)$ by an auxiliary variable $S$. Then the marginal of $X$ under the
joint law of $(X, S)$ in $q$ equals the law of $X$ under $p$.

Formalized by `InformationTheory.FiniteExtension.inputAuxiliaryLaw_map_fst`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#input-auxiliary-law-map-fst).

## Output marginal of the output-auxiliary law

Let $q$ be a finite extension of a finite
joint law $p$ of $(X, Y)$ by an auxiliary variable $S$. Then the marginal of $Y$ under the
joint law of $(Y, S)$ in $q$ equals the law of $Y$ under $p$.

Formalized by `InformationTheory.FiniteExtension.outputAuxiliaryLaw_map_fst`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-auxiliary-law-map-fst).

## Auxiliary marginal of the input-auxiliary law

Let $q$ be a finite extension of a
finite joint law of $(X, Y)$ by an auxiliary variable $S$. Then the marginal of $S$ under the
joint law of $(X, S)$ in $q$ equals the law of $S$ in $q$.

Formalized by `InformationTheory.FiniteExtension.inputAuxiliaryLaw_map_snd`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#input-auxiliary-law-map-snd).

## Auxiliary marginal of the output-auxiliary law

Let $q$ be a finite extension of a
finite joint law of $(X, Y)$ by an auxiliary variable $S$. Then the marginal of $S$ under the
joint law of $(Y, S)$ in $q$ equals the law of $S$ in $q$.

Formalized by `InformationTheory.FiniteExtension.outputAuxiliaryLaw_map_snd`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#output-auxiliary-law-map-snd).

## Conditional entropy vanishes for a one-letter output

If the output alphabet of a finite
joint law $p$ of $(X, Y)$ has exactly one element, then for every finite extension of $p$ by an
auxiliary variable $S$, the conditional entropy $H(Y \mid S)$ is $0$.

Formalized by `InformationTheory.FiniteExtension.conditionalEntropy_eq_zero_of_output_subsingleton`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-entropy-eq-zero-of-output-su).

## Conditional-prefix optimum of a joint law

For a finite joint law $p$ of $(X, Y)$, this
is the infimum in the extended reals of the conditional entropy $H(Y \mid S)$ in bits over all
finite extensions of $p$ by an auxiliary variable $S$ such that $I(X; S) = 0$ and
$H(Y \mid X, S) = 0$. The infimum of the empty set is $+\infty$.

## Sources

- Li, arXiv:2501.13736v4, equation cs_h_c.

Formalized by `InformationTheory.conditionalPrefixOptimum`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-prefix-optimum).

## Worst-case conditional-prefix optimum

For a real number $t$, the worst-case optimum at
$t$ is the supremum, taken in the extended reals, of the conditional-prefix optimum of $p$ over
all finite joint laws $p$ of an input $X$ and an output $Y$ whose mutual information $I(X; Y)$,
in bits, equals $t$; it is $-\infty$ when no such law exists.

Formalized by `InformationTheory.worstCaseOptimum`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#worst-case-optimum).

## Channel simulation constant

The constant $c_c^*$ is the limit superior in the extended
reals, as the real number $t$ tends to $+\infty$, of $W(t) - t - \log_2 t$, where $W(t)$ is the
worst-case optimum at $t$: the supremum of the conditional-prefix optimum over all finite joint
laws whose mutual information in bits is exactly $t$.

## Sources

- Li, arXiv:2501.13736v4, definition of c_c*.

Formalized by `InformationTheory.channelSimulationConstant`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#channel-simulation-constant).

## Uniform outer constant for channel simulation

A real number $\alpha$ is a uniform
outer constant when there is a real $\beta > 0$ such that for every finite joint law $p$ of
$(X, Y)$ there is a finite extension of $p$ by an auxiliary variable $S$ with $I(X; S) = 0$
and $H(Y \mid X, S) = 0$ and

$$H(Y \mid S) \le I(X; Y) + \log_2\bigl(I(X; Y) + \beta\bigr) + \alpha,$$

where all entropies and mutual informations are in bits and are computed from the law of
$(X, Y, S)$ in the extension.

Formalized by `InformationTheory.HasUniformOuterConstant`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#has-uniform-outer-constant).

## Infimum of the uniform outer constants

Call a real number $\alpha$ a uniform outer
constant when there is a real $\beta > 0$ such that every finite joint law $p$ of an input $X$
and an output $Y$ has a finite extension by an auxiliary $S$ with $I(X; S) = 0$,
$H(Y \mid X, S) = 0$ and $H(Y \mid S) \le I(X; Y) + \log_2(I(X; Y) + \beta) + \alpha$, where
entropies and mutual informations are in bits. This is the infimum of the set of uniform outer
constants, taken in the extended reals, so it is $+\infty$ when there is none.

Formalized by `InformationTheory.uniformOuterConstantInfimum`, a definition declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#uniform-outer-constant-infimum).

## Each admissible extension bounds the conditional-prefix optimum

Let $p$ be a finite
joint law of $(X, Y)$ and let $q$ be a finite extension of $p$ by an auxiliary variable $S$ with
$I(X; S) = 0$ and $H(Y \mid X, S) = 0$. Then the conditional-prefix optimum of $p$ is at most
the conditional entropy $H(Y \mid S)$ of $q$.

Formalized by `InformationTheory.conditionalPrefixOptimum_le`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-prefix-optimum-le).

## The conditional-prefix optimum vanishes for a one-letter output

If the output alphabet
of a finite joint law $p$ has exactly one element, then the conditional-prefix optimum of $p$
equals $0$.

Formalized by `InformationTheory.conditionalPrefixOptimum_eq_zero_of_output_subsingleton`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-prefix-optimum-eq-zero-of-ou).

## The worst-case optimum dominates each conditional-prefix optimum

For every finite joint
law $p$ of $(X, Y)$, the conditional-prefix optimum of $p$ is at most the worst-case optimum at
$t = I(X; Y)$, the mutual information of $p$ in bits.

Formalized by `InformationTheory.conditionalPrefixOptimum_le_worstCaseOptimum`, a theorem declared in [MathlibExt/InformationTheory/FiniteChannelSimulation.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/FiniteChannelSimulation.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html#conditional-prefix-optimum-le-worst-case).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-shot channel simulation](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/channel-simulation/one-shot-channel-simulation)
