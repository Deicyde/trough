---
declaration: section
origin: cited
lean: InformationTheory.quantizedConditionalEntropy, InformationTheory.quantizedConditionalEntropy_singleton, InformationTheory.quantizedConditionalEntropy_const, InformationTheory.conditionalShannonEntropy, InformationTheory.conditionalShannonEntropy_const, InformationTheory.measureMutualInformation, InformationTheory.toReal_klDiv_prod, InformationTheory.shannonEntropy_le_add
statement: formalized
proof: formalized
---

# Conditional entropy and mutual information

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html).

## Conditional entropy of a finite observation given a sub-$\sigma$-algebra

Let $\mu$ be a
probability measure on a measurable space $\Omega$, let $m$ be a sub-$\sigma$-algebra of the
$\sigma$-algebra of $\Omega$, let $n \in \mathbb{N}$, and let $f : \Omega \to \{0, \dots, n-1\}$ be
measurable. For each $i < n$ let $P_i = \mathbb{E}_\mu[\mathbf{1}_{\{f = i\}} \mid m]$ be the
conditional probability of $\{f = i\}$ given $m$. The quantized conditional entropy of $f$ given
$m$, in bits, is

$$H_\mu(f \mid m) = \int_\Omega \sum_{i < n} -P_i(\omega) \log_2 P_i(\omega) \, d\mu(\omega),$$

with the convention $0 \log_2 0 = 0$.

Formalized by `InformationTheory.quantizedConditionalEntropy`, a definition declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#quantized-conditional-entropy).

## One-valued observations have zero conditional entropy

Let $\mu$ be a probability measure
on a measurable space $\Omega$ and let $m$ be a sub-$\sigma$-algebra of the $\sigma$-algebra of
$\Omega$. The quantized conditional entropy given $m$ of the observation that is constantly $0$,
with values in the one-element set $\{0\}$, is $0$.

Formalized by `InformationTheory.quantizedConditionalEntropy_singleton`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#quantized-conditional-entropy-singleton).

## Constant quantized observations have zero conditional entropy

Let $\mu$ be a probability
measure on a measurable space $\Omega$, let $m$ be a sub-$\sigma$-algebra of the $\sigma$-algebra of
$\Omega$, and let $c \in \{0, \dots, n-1\}$ for some $n \in \mathbb{N}$. The quantized conditional
entropy given $m$ of the constant observation $\omega \mapsto c$ is $0$.

Formalized by `InformationTheory.quantizedConditionalEntropy_const`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#quantized-conditional-entropy-const).

## Conditional Shannon entropy given a sub-$\sigma$-algebra

Let $\mu$ be a probability measure
on a measurable space $\Omega$, let $m$ be a sub-$\sigma$-algebra of the $\sigma$-algebra of
$\Omega$, and let $X : \Omega \to Y$ be a measurable map into a measurable space $Y$. The
conditional Shannon entropy of $X$ given $m$ is the supremum in $[0, \infty]$, over all
$n \in \mathbb{N}$ and all measurable maps $q : Y \to \{0, \dots, n-1\}$, of the quantized
conditional entropy of $q \circ X$ given $m$, a negative value of the latter being counted as $0$.

## Sources

- the supremum over all finite measurable output quantizations.

Formalized by `InformationTheory.conditionalShannonEntropy`, a definition declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#conditional-shannon-entropy).

## Conditional entropy of a constant output vanishes

Let $\mu$ be a probability measure on a
measurable space $\Omega$, let $m$ be a sub-$\sigma$-algebra of the $\sigma$-algebra of $\Omega$,
and let $y$ be a point of a measurable space $Y$. The conditional Shannon entropy given $m$ of the
constant output $\omega \mapsto y$ is $0$.

Formalized by `InformationTheory.conditionalShannonEntropy_const`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#conditional-shannon-entropy-const).

## Mutual information of a joint probability measure

Let $\mu$ be a probability measure on
the product $X \times Y$ of two measurable spaces, with marginals $\mu_X$ and $\mu_Y$. The mutual
information of $\mu$, in bits and possibly infinite, is

$$I(\mu) = \frac{D_{\mathrm{KL}}(\mu \parallel \mu_X \otimes \mu_Y)}{\ln 2} \in [0, \infty],$$

where $D_{\mathrm{KL}}$ is the Kullback–Leibler divergence in nats.

## Sources

- KL divergence from the actual product of the actual marginals.

Formalized by `InformationTheory.measureMutualInformation`, a definition declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#measure-mutual-information).

## Divergence of a finite joint law from the product of its marginals

Let $\alpha$ and
$\beta$ be finite sets with measurable structures in which singletons are measurable, let $p$ be
a probability law on $\alpha \times \beta$ with marginals $p_X$ and $p_Y$, and write $H$ for
Shannon entropy in bits. Then the Kullback–Leibler divergence of $p$ from the product measure
$p_X \otimes p_Y$, computed with the natural logarithm and taken as a real number, equals
$(H(p_X) + H(p_Y) - H(p)) \log 2$.

Formalized by `InformationTheory.toReal_klDiv_prod`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#to-real-kl-div-prod).

## Subadditivity of entropy

Let $p$ be a probability law on $\alpha \times \beta$, where
$\alpha$ and $\beta$ are finite, with marginals $p_X$ and $p_Y$. Writing $H$ for Shannon entropy
in bits, $H(p) \le H(p_X) + H(p_Y)$.

Formalized by `InformationTheory.shannonEntropy_le_add`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#shannon-entropy-le-add).

## Mutual information of a finite joint law

Let $p$ be a probability distribution on
$\alpha \times \beta$, where $\alpha$ and $\beta$ are finite measurable spaces in which every
singleton is measurable, viewed as the joint law of a pair $(X, Y)$. Write $H(X, Y)$, $H(X)$ and
$H(Y)$ for the Shannon entropies of $p$ and of its first and second marginals. Then the mutual
information of the probability measure defined by $p$, in bits, is the real number
$H(X) + H(Y) - H(X, Y)$ read as an element of $[0, \infty]$, a negative value being read as $0$.

Formalized by `InformationTheory.measureMutualInformation_toMeasure`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#measure-mutual-information-to-measure).

## Mutual information vanishes exactly under independence

Let $p$ be a discrete probability
distribution on $\alpha \times \beta$, where $\alpha$ and $\beta$ are measurable spaces. The mutual
information of the probability measure defined by $p$ is $0$ if and only if this measure equals
the product of the probability measures defined by the two marginals of $p$.

Formalized by `InformationTheory.measureMutualInformation_toMeasure_eq_zero_iff`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#measure-mutual-information-to-measure-eq).

## Conditional entropy of a finite joint law

Let $p$ be a probability distribution on
$\alpha \times \beta$, where $\alpha$ and $\beta$ are finite, viewed as the joint law of a pair
$(X, Y)$, and let $p_X(a) = \sum_{b \in \beta} p(a, b)$ be its first marginal. The conditional
entropy of $Y$ given $X$, in bits, is

$$H(Y \mid X) = -\sum_{a \in \alpha} \sum_{b \in \beta} p(a, b) \log_2 \frac{p(a, b)}{p_X(a)},$$

where every term with $p(a, b) = 0$ is $0$.

It is the finite counterpart of the conditional Shannon entropy given a sub-$\sigma$-algebra.

Formalized by `InformationTheory.finiteConditionalEntropy`, a definition declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#finite-conditional-entropy).

## Chain rule for entropy

Let $p$ be a probability law on $\alpha \times \beta$, where
$\alpha$ and $\beta$ are finite, and let $p_X$ be its first marginal. Write $H(X, Y)$ for the
Shannon entropy of $p$, $H(X)$ for the Shannon entropy of $p_X$, and
$H(Y \mid X) = -\sum_{a, b} p(a, b) \log_2 (p(a, b) / p_X(a))$ for the finite conditional entropy
of $p$, all in bits. Then $H(X, Y) = H(X) + H(Y \mid X)$.

Formalized by `InformationTheory.shannonEntropy_eq_add_finiteConditionalEntropy`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#shannon-entropy-eq-add-finite-conditiona).

## Conditioning does not increase entropy

Let $p$ be a probability distribution on
$\alpha \times \beta$, where $\alpha$ and $\beta$ are finite, viewed as the joint law of a pair
$(X, Y)$. Then the conditional entropy $H(Y \mid X)$ of $p$ is at most the Shannon entropy $H(Y)$
of the second marginal of $p$, both in bits.

Formalized by `InformationTheory.finiteConditionalEntropy_le`, a theorem declared in [MathlibExt/InformationTheory/ConditionalEntropy.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalEntropy.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html#finite-conditional-entropy-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conditional entropy and mutual information](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/entropy-and-mutual-information/conditional-entropy-and-mutual-information)
