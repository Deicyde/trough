---
declaration: section
origin: cited
lean: InformationTheory.shannonEntropy, InformationTheory.shannonEntropy_pure, InformationTheory.shannonEntropy_map_const, InformationTheory.shannonEntropy_map_equiv, InformationTheory.shannonEntropy_map_prod_singleton, InformationTheory.toReal_klDiv_eq_sum, InformationTheory.toReal_klDiv_toMeasure, InformationTheory.surprisal
statement: formalized
proof: formalized
---

# Shannon entropy and Kullback–Leibler divergence

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html).

## Shannon entropy

The Shannon entropy in bits of a probability mass function $p$ on a finite
type $\alpha$ is $H(p) = -\sum_{a \in \alpha} p(a) \log_2 p(a)$, where a term with $p(a) = 0$
contributes $0$.

## Sources

- the finite Shannon sum; Li, arXiv:2501.13736v4, entropy conventions.

Formalized by `InformationTheory.shannonEntropy`, a definition declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy).

## A point mass has zero entropy

For every outcome $a$ of a finite alphabet, the point mass
at $a$ has Shannon entropy $0$.

Formalized by `InformationTheory.shannonEntropy_pure`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy-pure).

## A constant observation has zero entropy

For any probability mass function $p$ on a type
$\alpha$ and any point $b$ of a finite alphabet $\beta$, the image of $p$ under the constant map
$\alpha \to \beta$ with value $b$ has Shannon entropy $0$.

Formalized by `InformationTheory.shannonEntropy_map_const`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy-map-const).

## Entropy is invariant under relabeling

For a probability mass function $p$ on a finite
alphabet $\alpha$ and a bijection $e : \alpha \to \beta$ onto a finite alphabet $\beta$, the image
of $p$ under $e$ has the same Shannon entropy as $p$.

Formalized by `InformationTheory.shannonEntropy_map_equiv`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy-map-equiv).

## Appending a singleton coordinate preserves entropy

For a probability mass function $p$ on
a finite alphabet $\alpha$, the image of $p$ under $a \mapsto (a, 0)$ in $\alpha \times \{0\}$
has the same Shannon entropy as $p$.

Formalized by `InformationTheory.shannonEntropy_map_prod_singleton`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy-map-prod-singleton).

## Kullback–Leibler divergence on a finite space

Let $\mu$ and $\nu$ be finite measures on
a finite type $\alpha$ in which every singleton is measurable, with $\mu \ll \nu$ and
$\mu(\alpha) = \nu(\alpha)$. Then the Kullback–Leibler divergence $\mathrm{KL}(\mu \parallel \nu)$,
taken as a real number, equals $\sum_{a \in \alpha} \mu(\{a\}) \log (\mu(\{a\}) / \nu(\{a\}))$,
where $\log$ is the natural logarithm and a term with $\mu(\{a\}) = 0$ is $0$.

Formalized by `InformationTheory.toReal_klDiv_eq_sum`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#to-real-kl-div-eq-sum).

## Kullback–Leibler divergence of finite probability laws

Let $p$ and $q$ be probability
mass functions on a finite type $\alpha$ in which every singleton is measurable, such that
$p(a) = 0$ whenever $q(a) = 0$, and let $P$ and $Q$ be the measures they define. Then the
Kullback–Leibler divergence $\mathrm{KL}(P \parallel Q)$, taken as a real number, equals
$\sum_{a \in \alpha} p(a) \log (p(a) / q(a))$, where $\log$ is the natural logarithm and a term
with $p(a) = 0$ is $0$.

Formalized by `InformationTheory.toReal_klDiv_toMeasure`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#to-real-kl-div-to-measure).

## Surprisal

The surprisal (information content) in bits of an outcome of probability
$q$ is $-\log_2 q$, with value $\infty$ when $q = 0$. Formally $q$ ranges over the extended
nonnegative reals $[0, \infty]$: the surprisal of $0$ is $\infty$, the surprisal of
$q \in (0, \infty)$ is $\max(0, -\log_2 q)$, and the surprisal of $\infty$ is $0$.

Formalized by `InformationTheory.surprisal`, a definition declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#surprisal).

## Cross-entropy

For probability mass functions $p$ and $q$ on a finite alphabet, the
cross-entropy of $q$ relative to $p$ is $H(p, q) = \sum_a p(a) \cdot (-\log_2 q(a))$ in bits, a
value in $[0, \infty]$. Here $-\log_2 q(a)$ is the surprisal of $a$ under $q$, which is $\infty$
when $q(a) = 0$, and a term with $p(a) = 0$ contributes $0$. So $H(p, q)$ is $\infty$ exactly
when $p$ charges an outcome that $q$ rules out.

Formalized by `InformationTheory.crossEntropy`, a definition declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#cross-entropy).

## Cross-entropy of a point mass

For an outcome $y$ of a finite alphabet and a probability
mass function $q$ on it, the cross-entropy $H(\delta_y, q)$ of $q$ relative to the point mass
$\delta_y$ at $y$ equals the surprisal $-\log_2 q(y)$ of $y$ under $q$, which is $\infty$ when
$q(y) = 0$.

Formalized by `InformationTheory.crossEntropy_pure`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#cross-entropy-pure).

## Cross-entropy is expected surprisal

For probability mass functions $p$ and $q$ on a
finite alphabet, the expected surprisal $\mathbb{E}_{a \sim p}[-\log_2 q(a)]$ (with
$-\log_2 0 = \infty$), taken as the integral of a $[0, \infty]$-valued function with respect to
the law $p$, equals the cross-entropy $H(p, q)$.

Formalized by `InformationTheory.lintegral_surprisal`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#lintegral-surprisal).

## Cross-entropy is entropy plus divergence

For probability mass functions $p$ and $q$ on a
finite alphabet, the cross-entropy $H(p, q)$ in bits equals $H(p) + D(p \parallel q) / \ln 2$,
where $H(p)$ is the Shannon entropy of $p$ in bits and $D(p \parallel q)$ is the
Kullback–Leibler divergence of $p$ from $q$ with the natural logarithm. The identity holds in
$[0, \infty]$ with no support hypothesis: when $p$ charges an outcome that $q$ rules out, both
sides are $\infty$.

Formalized by `InformationTheory.crossEntropy_eq_shannonEntropy_add_klDiv`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#cross-entropy-eq-shannon-entropy-add-kl).

## Gibbs' inequality

The cross-entropy of any prediction `q` is at least the entropy of the
truth `p`.

Formalized by `InformationTheory.shannonEntropy_le_crossEntropy`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#shannon-entropy-le-cross-entropy).

## Equality in Gibbs' inequality

For probability mass functions $p$ and $q$ on a finite
alphabet, the cross-entropy $H(p, q)$ in bits equals the Shannon entropy $H(p)$ in bits if and
only if $q = p$. Thus log loss is a strictly proper scoring rule.

Formalized by `InformationTheory.crossEntropy_eq_shannonEntropy_iff`, a theorem declared in [MathlibExt/InformationTheory/FiniteEntropy.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/FiniteEntropy.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html#cross-entropy-eq-shannon-entropy-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shannon entropy and Kullback–Leibler divergence](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/entropy-and-mutual-information/shannon-entropy-and-kullback-leibler-divergence)
