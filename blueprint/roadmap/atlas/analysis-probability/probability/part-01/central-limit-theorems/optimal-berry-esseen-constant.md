---
declaration: section
origin: cited
lean: BerryEsseenConstant.IsAdmissible, BerryEsseenConstant.value, BerryEsseenConstant.esseenConstant, BerryEsseenConstant.esseenConstant_positive, BerryEsseenConstant.isAdmissible_nonnegative, BerryEsseenConstant.isAdmissible_fortyTwo, BerryEsseenConstant.admissible_nonempty, BerryEsseenConstant.admissible_bddBelow
statement: formalized
---

# Optimal Berry–Esseen constant

61 results, 46 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html).

## Admissible Berry–Esseen coefficient

A real number $C$ is an admissible Berry–Esseen
coefficient when, for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$
and finite third absolute moment $\rho = \int |x|^3 \, d\mu(x)$, and every positive integer $n$,
the Kolmogorov error $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$ is at most $C \rho / \sqrt{n}$.
Here $F_n$ is the distribution function of $(X_1 + \dots + X_n)/\sqrt{n}$ for independent random
variables $X_1, X_2, \dots$ with law $\mu$, and $\Phi$ is the standard normal distribution
function.

Formalized by `BerryEsseenConstant.IsAdmissible`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-admissible).

## The optimal Berry–Esseen constant

Call a real number $C$ admissible if for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment $\rho = \int |x|^3 \, d\mu$, and every positive integer $n$,

$$\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le \frac{C \rho}{\sqrt{n}},$$

where $F_n$ is the distribution function of $(X_1 + \dots + X_n)/\sqrt{n}$ for independent
random variables $X_1, X_2, \dots$ with law $\mu$, and $\Phi$ is the standard normal
distribution function. The optimal Berry–Esseen constant is the infimum of the admissible $C$.

The set of admissible constants is nonempty (it contains $42$) and bounded below by $0$, so
this is a genuine real infimum.

Formalized by `BerryEsseenConstant.value`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value).

## Esseen's lower-bound constant

Esseen's constant is the real number
$(\sqrt{10} + 3)/(6\sqrt{2\pi})$.

Esseen showed that the Berry–Esseen constant for i.i.d. sums is at least this number; the
definition records the value only, not that lower bound.

Formalized by `BerryEsseenConstant.esseenConstant`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen-constant).

## Esseen's lower-bound constant is positive

The number $(\sqrt{10} + 3)/(6\sqrt{2\pi})$ is
positive.

Formalized by `BerryEsseenConstant.esseenConstant_positive`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen-constant-positive).

## Admissible coefficients are nonnegative

Every admissible Berry–Esseen coefficient
$C \in \mathbb{R}$ satisfies $C \ge 0$.

Formalized by `BerryEsseenConstant.isAdmissible_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-admissible-nonnegative).

## The Berry–Esseen bound with coefficient 42

The number $42$ is an admissible
Berry–Esseen coefficient: for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$,
variance $1$ and finite third absolute moment $\rho = \int |x|^3 \, d\mu(x)$, and every positive
integer $n$, the Kolmogorov error $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$ is at most
$42 \rho / \sqrt{n}$, where $F_n$ is the distribution function of $(X_1 + \dots + X_n)/\sqrt{n}$
for independent random variables $X_1, X_2, \dots$ with law $\mu$, and $\Phi$ is the standard
normal distribution function.

Formalized by `BerryEsseenConstant.isAdmissible_fortyTwo`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-admissible-forty-two).

## Admissible Berry–Esseen coefficients exist

The set of real numbers $C$ that are
admissible Berry–Esseen coefficients (common Berry–Esseen coefficients for all standardized laws
and all positive sample sizes) is nonempty.

Formalized by `BerryEsseenConstant.admissible_nonempty`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#admissible-nonempty).

## The admissible Berry–Esseen coefficients are bounded below

The set of real numbers $C$
that are admissible Berry–Esseen coefficients (common Berry–Esseen coefficients for all
standardized laws and all positive sample sizes) is bounded below.

Formalized by `BerryEsseenConstant.admissible_bddBelow`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#admissible-bdd-below).

## The optimal Berry–Esseen coefficient is nonnegative

The infimum $C^*$ of all admissible
Berry–Esseen coefficients satisfies $0 \le C^*$.

Formalized by `BerryEsseenConstant.value_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-nonnegative).

## The optimal Berry–Esseen coefficient is at most every admissible one

If $C$ is an
admissible Berry–Esseen coefficient, then the infimum $C^*$ of all admissible coefficients
satisfies $C^* \le C$.

Formalized by `BerryEsseenConstant.value_le_of_isAdmissible`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-le-of-is-admissible).

## The optimal Berry–Esseen coefficient is at most 42

The infimum $C^*$ of all admissible
Berry–Esseen coefficients satisfies $C^* \le 42$.

Formalized by `BerryEsseenConstant.value_le_fortyTwo`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-le-forty-two).

## Admissibility is upward closed

If $C \le D$ are real numbers and $C$ is an admissible
Berry–Esseen coefficient, then $D$ is an admissible Berry–Esseen coefficient.

Formalized by `BerryEsseenConstant.isAdmissible_mono`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-admissible-mono).

## The optimal Berry–Esseen coefficient satisfies the Berry–Esseen bound

Let $C^*$ be the
infimum of all admissible Berry–Esseen coefficients. For every standardized law $\mu$ on
$\mathbb{R}$ and every positive integer $n$, the Kolmogorov error of $\mu$ at sample size $n$ is
at most $C^* \rho(\mu) / \sqrt{n}$, where $\rho(\mu) = \int |x|^3 \, d\mu(x)$ is the third
absolute moment of $\mu$.

Formalized by `BerryEsseenConstant.value_bound`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-bound).

## The optimal Berry–Esseen coefficient is admissible

The infimum $C^*$ of all admissible
Berry–Esseen coefficients is itself an admissible coefficient.

Formalized by `BerryEsseenConstant.value_isAdmissible`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-is-admissible).

## The Berry–Esseen constant is the least admissible coefficient

The infimum $C^*$ of all
admissible Berry–Esseen coefficients is the least element of the set of admissible
coefficients: $C^*$ is admissible, and $C^* \le C$ for every admissible coefficient $C$.

Formalized by `BerryEsseenConstant.value_isLeast`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#value-is-least).

## Admissible coefficients are exactly those above the optimal one

A real number $C$ is an
admissible Berry–Esseen coefficient if and only if $C_0 \le C$, where $C_0$ is the optimal
Berry–Esseen coefficient, the infimum of the set of admissible coefficients.

Formalized by `BerryEsseenConstant.isAdmissible_iff_value_le`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-admissible-iff-value-le).

## Admissible coefficients bound every standardized i.i.d. sequence

Let $C$ be an admissible
Berry–Esseen coefficient. Let $X_0, X_1, X_2, \dots$ be measurable real random variables on a
probability space $(\Omega, P)$ that are independent and identically distributed, with
$\mathbb{E}[X_0] = 0$, $\operatorname{Var}(X_0) = 1$ and $\mathbb{E}|X_0|^3 < \infty$. Then for
every positive integer $n$ and every real $x$,

$$
\left| P\left( \frac{X_0 + \dots + X_{n-1}}{\sqrt{n}} \le x \right) - \Phi(x) \right|
\le \frac{C \, \mathbb{E}|X_0|^3}{\sqrt{n}},
$$

where $\Phi$ is the distribution function of the standard normal law.

Formalized by `BerryEsseenConstant.iid_bound`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#iid-bound).

## Standardized two-point law

A measure $\mu$ on $\mathbb{R}$ is a standardized two-point
law when it is a probability measure with mean $0$, variance $1$ and finite third absolute
moment, and there are real numbers $a \ne b$ with $\mu(\mathbb{R} \setminus \{a, b\}) = 0$.

Formalized by `BerryEsseenConstant.IsBernoulliLaw`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-bernoulli-law).

## Symmetric Bernoulli law

The symmetric Bernoulli law is the measure
$\frac12 \delta_{-1} + \frac12 \delta_1$ on $\mathbb{R}$, where $\delta_a$ denotes the Dirac mass
at $a$; it puts mass $1/2$ at each of the points $-1$ and $1$.

Formalized by `BerryEsseenConstant.symmetricBernoulliLaw`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-law).

## The symmetric Bernoulli law has moments of all orders

For every exponent
$p \in [0, \infty]$, the identity function of $\mathbb{R}$ belongs to $L^p$ of the symmetric
Bernoulli law.

Formalized by `BerryEsseenConstant.symmetricBernoulli_memLp`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-mem-lp).

## Integrals against the symmetric Bernoulli law

For every function
$f : \mathbb{R} \to \mathbb{R}$, the integral of $f$ against the symmetric Bernoulli law
$\frac12 \delta_{-1} + \frac12 \delta_1$ equals $\frac12 f(-1) + \frac12 f(1)$.

Formalized by `BerryEsseenConstant.symmetricBernoulli_integral`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-integral).

## The symmetric Bernoulli law is standardized

The symmetric Bernoulli law, which puts mass
$1/2$ at each of the points $-1$ and $1$, is a standardized law: it is a probability measure on
$\mathbb{R}$ with mean $0$ and variance $1$, and it has a finite third absolute moment.

Formalized by `BerryEsseenConstant.symmetricBernoulli_isStandardized`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-is-standardized).

## The symmetric Bernoulli law is a standardized two-point law

The law
$\frac12 \delta_{-1} + \frac12 \delta_1$ on $\mathbb{R}$ is a probability measure with mean $0$,
variance $1$ and finite third absolute moment, and it is concentrated on the two distinct points
$-1$ and $1$.

Formalized by `BerryEsseenConstant.symmetricBernoulli_isBernoulli`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-is-bernoulli).

## Third absolute moment of the symmetric Bernoulli law

The third absolute moment
$\int |x|^3 \, d\mu(x)$ of the symmetric Bernoulli law $\mu$ equals $1$.

Formalized by `BerryEsseenConstant.symmetricBernoulli_thirdMoment`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#symmetric-bernoulli-third-moment).

## Admissible Berry–Esseen coefficient for two-point laws

A real number $C$ is an admissible
Berry–Esseen coefficient for standardized two-point laws when, for every probability measure $\mu$
on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment
$\rho = \int |x|^3 \, d\mu(x)$ that is concentrated on two distinct points, and every positive
integer $n$, the Kolmogorov error $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$ is at most
$C \rho / \sqrt{n}$. Here $F_n$ is the distribution function of $(X_1 + \dots + X_n)/\sqrt{n}$ for
independent random variables $X_1, X_2, \dots$ with law $\mu$, and $\Phi$ is the standard normal
distribution function.

Formalized by `BerryEsseenConstant.IsBernoulliAdmissible`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-bernoulli-admissible).

## Bernoulli Berry–Esseen constant

The Bernoulli Berry–Esseen constant is the infimum, in
$\mathbb{R}$, of the set of real numbers $C$ that are admissible Berry–Esseen coefficients for the
Bernoulli subclass: for every standardized law $\mu$ (a probability measure on $\mathbb{R}$ with
mean $0$, variance $1$ and finite third absolute moment) concentrated on two distinct points, and
every positive integer $n$, the supremum over $x \in \mathbb{R}$ of the distance between the
distribution function of $(X_0 + \dots + X_{n-1})/\sqrt{n}$ at $x$, for independent
$\mu$-distributed $X_0, \dots, X_{n-1}$, and the standard normal distribution function at $x$ is
at most $C \rho(\mu) / \sqrt{n}$, where $\rho(\mu) = \int |x|^3 \, d\mu(x)$.

Formalized by `BerryEsseenConstant.bernoulliValue`, a definition declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#bernoulli-value).

## Bernoulli-admissible coefficients are nonnegative

Every real number $C$ that is an
admissible Berry–Esseen coefficient for standardized two-point laws satisfies $C \ge 0$.

The class of standardized two-point laws is nonempty: it contains the law with mass $1/2$ at each
of $-1$ and $1$.

Formalized by `BerryEsseenConstant.isBernoulliAdmissible_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#is-bernoulli-admissible-nonnegative).

## Bernoulli-admissible coefficients exist

The set of real numbers $C$ that are admissible
Berry–Esseen coefficients for the Bernoulli subclass (common Berry–Esseen coefficients for all
standardized laws concentrated on two points and all positive sample sizes) is nonempty.

The coefficient $42$, admissible for all standardized laws, is one such coefficient.

Formalized by `BerryEsseenConstant.bernoulliAdmissible_nonempty`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#bernoulli-admissible-nonempty).

## The Bernoulli-admissible coefficients are bounded below

The set of real numbers $C$ that
are admissible Berry–Esseen coefficients for the Bernoulli subclass (common Berry–Esseen
coefficients for all standardized laws concentrated on two points and all positive sample sizes)
is bounded below.

Formalized by `BerryEsseenConstant.bernoulliAdmissible_bddBelow`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#bernoulli-admissible-bdd-below).

## The Bernoulli Berry–Esseen constant is nonnegative

The infimum of the real numbers that
are admissible Berry–Esseen coefficients for the Bernoulli subclass is nonnegative.

Formalized by `BerryEsseenConstant.bernoulliValue_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#bernoulli-value-nonnegative).

## The Bernoulli Berry–Esseen constant is at most the general one

The infimum of the real
numbers that are admissible Berry–Esseen coefficients for the Bernoulli subclass is at most the
infimum of the real numbers that are admissible Berry–Esseen coefficients for all standardized
laws.

Formalized by `BerryEsseenConstant.bernoulliValue_le_value`, a theorem declared in [MathlibExt/Probability/BerryEsseenConstant.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BerryEsseenConstant.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#bernoulli-value-le-value).

## Statement of Zolotarev's Berry–Esseen bound

The proposition that the Berry–Esseen
constant $C_0$ is at most $0.82$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, upper row Z1967; the non-i.i.d. 0.9051 is context only.

Formalized by `BerryEsseenWanted.zolotarev1967UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#zolotarev1967-upper-bound).

## Statement of van Beek's Berry–Esseen bound

The proposition that the Berry–Esseen
constant $C_0$ is at most $0.7975$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, upper row vB1972; original primary text is not retained here.

Formalized by `BerryEsseenWanted.vanBeek1972UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#van-beek1972-upper-bound).

## Statement of Shiganov's Berry–Esseen bound

The proposition that the Berry–Esseen
constant $C_0$ is at most $0.7655$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, upper row Shi1986; retained Shevtsova2011 introduction reports it.

Formalized by `BerryEsseenWanted.shiganov1986UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shiganov1986-upper-bound).

## Statement of Shevtsova's 2006 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. This is the proposition $C_0 \le 0.7056$.

## Sources

- catalogue C19a, upper row She2006; retained Shevtsova2011 introduction reports it.

Formalized by `BerryEsseenWanted.shevtsova2006UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2006-upper-bound).

## Statement of the Korolev–Shevtsova upper bound

For a probability measure $\mu$ on
$\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. Let $C_0$ be
the optimal i.i.d. Berry–Esseen constant, the infimum of all real $C$ such that
$\Delta_n(\mu) \le C \beta_3(\mu) / \sqrt{n}$ for every integer $n \ge 1$ and every probability
measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment. This
is the proposition that $C_0 \le 0.5129$.

## Sources

- catalogue C19a, upper row KS2009; retained Shevtsova2011 lines 141-148.

Formalized by `BerryEsseenWanted.korolevShevtsova2009UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#korolev-shevtsova2009-upper-bound).

## Statement of Tyurin's Berry–Esseen bound

The proposition that the Berry–Esseen
constant $C_0$ is at most $0.4785$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, upper row Tyu2009; retained Shevtsova2011 lines 150-154.

Formalized by `BerryEsseenWanted.tyurin2009UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#tyurin2009-upper-bound).

## Statement of Shevtsova's 2011 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. This is the proposition $C_0 \le 0.4748$.

## Sources

- catalogue C19a, upper row She2011; retained arXiv1111.6554 Corollary 1.

Formalized by `BerryEsseenWanted.shevtsova2011UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2011-upper-bound).

## Statement of Shevtsova's 2013 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. This is the proposition $C_0 \le 0.4690$.

## Sources

- catalogue C19a, upper row She2013. The original primary text and the correct structural formula remain unresolved; this is only the literal bound request.

Formalized by `BerryEsseenWanted.shevtsova2013UpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2013-upper-bound).

## Statement of the unverified Berry–Esseen bound 0.4395

The proposition that the Berry–Esseen
constant $C_0$ is at most $0.4395$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, upper row XL2026, explicitly unverified. No external repository certificate or compiler-trusting proof is accepted by this request.

Formalized by `BerryEsseenWanted.xiaoLi2026UnverifiedUpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#xiao-li2026-unverified-upper-bound).

## Statement of Lin's 2026 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. This is the proposition $C_0 \le 0.423$.

## Sources

- catalogue C19a, upper row Lin2026, explicitly unverified. No external repository certificate or comparator result is asserted here.

Formalized by `BerryEsseenWanted.lin2026UnverifiedUpperBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#lin2026-unverified-upper-bound).

## Statement of the Korolev–Shevtsova structural Berry–Esseen bound

For a probability
measure $\mu$ on $\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. This is the
proposition that for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$
and finite third absolute moment and every integer $n \ge 1$,

$$\Delta_n(\mu) \le \frac{0.34445\,(\beta_3(\mu) + 0.489)}{\sqrt{n}}.$$

## Sources

- catalogue C19a, KS2009 upper-row comment, and the exact retained Shevtsova2011 quotation at lines 141-148. The additive offset is 0.489, not 0.429.

Formalized by `BerryEsseenWanted.korolevShevtsova2009Structural`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#korolev-shevtsova2009-structural).

## Statement of Esseen's lower bound for the Berry–Esseen constant

For a probability measure
$\mu$ on $\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. Let $C_0$ be
the optimal i.i.d. Berry–Esseen constant, the infimum of all real $C$ such that
$\Delta_n(\mu) \le C \beta_3(\mu) / \sqrt{n}$ for every integer $n \ge 1$ and every probability
measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment. This
is the proposition that $(\sqrt{10} + 3)/(6\sqrt{2\pi}) \le C_0$.

## Sources

- catalogue C19a, lower row E1956, and retained Shevtsova2011 lines 185-194. The symbolic endpoint is not replaced by its decimal approximation.

Formalized by `BerryEsseenWanted.esseen1956LowerBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen1956-lower-bound).

## Statement of Esseen's asymptotic lower bound for a two-point law

For a probability
measure $\mu$ on $\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, let $\beta_3(\mu) = \int |x|^3 \, d\mu$, and let
$C_E = (\sqrt{10} + 3)/(6\sqrt{2\pi})$. This is the proposition that there is a probability
measure $\mu$ on $\mathbb{R}$ with mean $0$ and variance $1$ that is concentrated on two distinct
points, such that for every real $\varepsilon > 0$ and every $N \in \mathbb{N}$ there is a positive
integer $n \ge N$ with

$$\Delta_n(\mu) \ge \frac{(C_E - \varepsilon)\,\beta_3(\mu)}{\sqrt{n}}.$$

## Sources

- catalogue C19a, lower-row Bernoulli asymptotic comment. A single actual standardized two-point law is chosen before epsilon and the sample-size threshold. Its normalized sums approach the lower coefficient along arbitrarily large sample sizes; an original Esseen primary comparison remains a source gap.

Formalized by `BerryEsseenWanted.esseenBernoulliAsymptoticLowerBound`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen-bernoulli-asymptotic-lower-bound).

## Statement of Schulz's Bernoulli Berry–Esseen optimum

Let $C_B$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$ that is concentrated on two points, that is,
$\mu(\mathbb{R} \setminus \{a, b\}) = 0$ for some reals $a \ne b$, and every integer $n \ge 1$,
the distribution function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent
$X_1, \dots, X_n$ with law $\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$,
where $\Phi$ is the standard normal distribution function. This is the proposition
$C_B = (\sqrt{10} + 3)/(6\sqrt{2\pi})$.

## Sources

- catalogue C19a, Bernoulli/binomial comment and Sch2016 reference. The actual subclass consists of centered variance-one two-point laws. The full Schulz primary proof has not been acquired or verified in this lane.

Formalized by `BerryEsseenWanted.schulz2016BernoulliOptimum`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#schulz2016-bernoulli-optimum).

## Statement of the Kolmogorov distance via left-continuous distribution functions

This is
the proposition that for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance
$1$ and finite third absolute moment and every integer $n \ge 1$, if $S_n = X_1 + \dots + X_n$ for
independent random variables $X_1, X_2, \dots$ each with law $\mu$, then

$$
\sup_{x \in \mathbb{R}} \bigl|P(S_n/\sqrt{n} < x) - \Phi(x)\bigr|
= \sup_{x \in \mathbb{R}} \bigl|P(S_n/\sqrt{n} \le x) - \Phi(x)\bigr|,
$$

where $\Phi$ is the standard normal distribution function.

## Sources

- the right-CDF catalogue definition and retained Shevtsova2011 lines 104-108, which explicitly use a left-continuous CDF. This probability bridge is requested, not inferred by replacing strict with non-strict events.

Formalized by `BerryEsseenWanted.leftRightCDFErrorEquivalence`, a definition declared in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#left-right-cdferror-equivalence).

## Zolotarev's upper bound for the Berry–Esseen constant

The Berry–Esseen constant $C_0$ is
at most $0.82$. Here $C_0$ is the infimum of the real numbers $C$ such that for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution function
$F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with law $\mu$,
satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here $\Phi$ is
the standard normal distribution function.

## Sources

- catalogue C19a, Z1967 upper row.

Stated but not proved: `BerryEsseenWanted.zolotarev1967UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#zolotarev1967-upper-bound-holds).

## Van Beek's upper bound for the Berry–Esseen constant

The Berry–Esseen constant $C_0$ is
at most $0.7975$. Here $C_0$ is the infimum of the real numbers $C$ such that for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution function
$F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with law $\mu$,
satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here $\Phi$ is
the standard normal distribution function.

## Sources

- catalogue C19a, vB1972 upper row.

Stated but not proved: `BerryEsseenWanted.vanBeek1972UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#van-beek1972-upper-bound-holds).

## Shiganov's upper bound for the Berry–Esseen constant

The Berry–Esseen constant $C_0$ is
at most $0.7655$. Here $C_0$ is the infimum of the real numbers $C$ such that for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution function
$F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with law $\mu$,
satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here $\Phi$ is
the standard normal distribution function.

## Sources

- catalogue C19a, Shi1986 upper row.

Stated but not proved: `BerryEsseenWanted.shiganov1986UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shiganov1986-upper-bound-holds).

## Shevtsova's 2006 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. Then $C_0 \le 0.7056$.

## Sources

- catalogue C19a, She2006 upper row.

Stated but not proved: `BerryEsseenWanted.shevtsova2006UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2006-upper-bound-holds).

## Korolev–Shevtsova upper bound for the Berry–Esseen constant

For a probability measure
$\mu$ on $\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. Let $C_0$ be
the optimal i.i.d. Berry–Esseen constant, the infimum of all real $C$ such that
$\Delta_n(\mu) \le C \beta_3(\mu) / \sqrt{n}$ for every integer $n \ge 1$ and every probability
measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment. Then
$C_0 \le 0.5129$.

## Sources

- catalogue C19a, KS2009 upper row; retained Shevtsova2011 quotation.

Stated but not proved: `BerryEsseenWanted.korolevShevtsova2009UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#korolev-shevtsova2009-upper-bound-holds).

## Tyurin's upper bound for the Berry–Esseen constant

The Berry–Esseen constant $C_0$ is
at most $0.4785$. Here $C_0$ is the infimum of the real numbers $C$ such that for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution function
$F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with law $\mu$,
satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here $\Phi$ is
the standard normal distribution function.

## Sources

- catalogue C19a, Tyu2009 upper row.

Stated but not proved: `BerryEsseenWanted.tyurin2009UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#tyurin2009-upper-bound-holds).

## Shevtsova's 2011 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. Then $C_0 \le 0.4748$.

## Sources

- catalogue C19a, She2011 upper row; retained primary Corollary 1.

Stated but not proved: `BerryEsseenWanted.shevtsova2011UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2011-upper-bound-holds).

## Shevtsova's 2013 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. Then $C_0 \le 0.4690$.

## Sources

- catalogue C19a, She2013 upper row; the primary correction is unresolved.

Stated but not proved: `BerryEsseenWanted.shevtsova2013UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#shevtsova2013-upper-bound-holds).

## The unverified upper bound 0.4395 for the Berry–Esseen constant

The Berry–Esseen
constant $C_0$ is at most $0.4395$. Here $C_0$ is the infimum of the real numbers $C$ such that
for every probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third
absolute moment $\beta_3 = \int |x|^3 \, d\mu(x)$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, where $X_1, \dots, X_n$ are independent with
law $\mu$, satisfies $\sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)| \le C \beta_3 / \sqrt{n}$; here
$\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a, explicitly unverified XL2026 row.

Stated but not proved: `BerryEsseenWanted.xiaoLi2026UnverifiedUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#xiao-li2026-unverified-upper-bound-holds).

## Lin's 2026 Berry–Esseen bound

Let $C_0$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$, and every integer $n \ge 1$, the distribution
function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent $X_1, \dots, X_n$ with law
$\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$, where $\Phi$ is the
standard normal distribution function. Then $C_0 \le 0.423$.

## Sources

- catalogue C19a, explicitly unverified Lin2026 row.

Stated but not proved: `BerryEsseenWanted.lin2026UnverifiedUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#lin2026-unverified-upper-bound-holds).

## Korolev–Shevtsova structural Berry–Esseen bound

For a probability measure $\mu$ on
$\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. Then for every
probability measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute
moment and every integer $n \ge 1$,

$$\Delta_n(\mu) \le \frac{0.34445\,(\beta_3(\mu) + 0.489)}{\sqrt{n}}.$$

## Sources

- catalogue C19a, KS2009 structural comment; retained 2011 equation.

Stated but not proved: `BerryEsseenWanted.korolevShevtsova2009Structural_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#korolev-shevtsova2009-structural-holds).

## Esseen's lower bound for the Berry–Esseen constant

For a probability measure
$\mu$ on $\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, and let $\beta_3(\mu) = \int |x|^3 \, d\mu$. Let $C_0$ be
the optimal i.i.d. Berry–Esseen constant, the infimum of all real $C$ such that
$\Delta_n(\mu) \le C \beta_3(\mu) / \sqrt{n}$ for every integer $n \ge 1$ and every probability
measure $\mu$ on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment. Then
$(\sqrt{10} + 3)/(6\sqrt{2\pi}) \le C_0$.

## Sources

- catalogue C19a, E1956 lower row; retained 2011 exact benchmark.

Stated but not proved: `BerryEsseenWanted.esseen1956LowerBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen1956-lower-bound-holds).

## Esseen's asymptotic lower bound for a two-point law

For a probability measure $\mu$ on
$\mathbb{R}$ and an integer $n \ge 1$, let $F_n$ be the distribution function of
$(X_1 + \dots + X_n)/\sqrt{n}$ for independent random variables $X_1, X_2, \dots$ each with law
$\mu$, let $\Delta_n(\mu) = \sup_{x \in \mathbb{R}} |F_n(x) - \Phi(x)|$, where $\Phi$ is the
standard normal distribution function, let $\beta_3(\mu) = \int |x|^3 \, d\mu$, and let
$C_E = (\sqrt{10} + 3)/(6\sqrt{2\pi})$. There is a probability measure $\mu$ on $\mathbb{R}$ with
mean $0$ and variance $1$ that is concentrated on two distinct points, such that for every real
$\varepsilon > 0$ and every $N \in \mathbb{N}$ there is a positive integer $n \ge N$ with

$$\Delta_n(\mu) \ge \frac{(C_E - \varepsilon)\,\beta_3(\mu)}{\sqrt{n}}.$$

In other words, $\limsup_{n \to \infty} \sqrt{n}\,\Delta_n(\mu) / \beta_3(\mu) \ge C_E$.

## Sources

- catalogue C19a, the asymptotic normalized Bernoulli lower-row clause.

Stated but not proved: `BerryEsseenWanted.esseenBernoulliAsymptoticLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#esseen-bernoulli-asymptotic-lower-bound-2).

## Schulz's Bernoulli Berry–Esseen optimum

Let $C_B$ be the infimum of all
real $C$ such that for every real probability law $\mu$ with mean $0$, variance $1$ and finite
third absolute moment $\rho = \int |x|^3\,d\mu$ that is concentrated on two points, that is,
$\mu(\mathbb{R} \setminus \{a, b\}) = 0$ for some reals $a \ne b$, and every integer $n \ge 1$,
the distribution function $F_n$ of $(X_1 + \dots + X_n)/\sqrt{n}$, for independent
$X_1, \dots, X_n$ with law $\mu$, satisfies $\sup_x |F_n(x) - \Phi(x)| \le C \rho / \sqrt{n}$,
where $\Phi$ is the standard normal distribution function. Then
$C_B = (\sqrt{10} + 3)/(6\sqrt{2\pi})$.

## Sources

- catalogue C19a, Bernoulli/binomial comment, Schulz2016.

Stated but not proved: `BerryEsseenWanted.schulz2016BernoulliOptimum_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#schulz2016-bernoulli-optimum-holds).

## Kolmogorov distance via left-continuous distribution functions

Let $\mu$ be a probability
measure on $\mathbb{R}$ with mean $0$, variance $1$ and finite third absolute moment, let $n \ge 1$
be an integer, and let $S_n = X_1 + \dots + X_n$ for independent random variables $X_1, X_2, \dots$
each with law $\mu$. Then

$$
\sup_{x \in \mathbb{R}} \bigl|P(S_n/\sqrt{n} < x) - \Phi(x)\bigr|
= \sup_{x \in \mathbb{R}} \bigl|P(S_n/\sqrt{n} \le x) - \Phi(x)\bigr|,
$$

where $\Phi$ is the standard normal distribution function.

## Sources

- catalogue C19a right CDF and Shevtsova2011's explicit left convention.

Stated but not proved: `BerryEsseenWanted.leftRightCDFErrorEquivalence_holds` is written with `theorem_wanted` in [WantedExt/Probability/BerryEsseenConstantWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BerryEsseenConstantWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html#left-right-cdferror-equivalence-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Optimal Berry–Esseen constant](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems/optimal-berry-esseen-constant)
