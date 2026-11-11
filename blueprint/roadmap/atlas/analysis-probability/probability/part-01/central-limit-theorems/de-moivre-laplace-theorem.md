---
declaration: section
origin: cited
lean: MathlibExt.Probability.CharFunStandardizedBinomial.standardizedBinomial, MathlibExt.Probability.CharFunStandardizedBinomial.charFun_map_affine, MathlibExt.Probability.CharFunStandardizedBinomial.charFun_binomial_real, MathlibExt.Probability.CharFunStandardizedBinomial.exp_taylor2_err, MathlibExt.Probability.CharFunStandardizedBinomial.charFun_standardizedBinomial, MathlibExt.Probability.CharFunStandardizedBinomial.tendsto_charFun_standardizedBinomial, ProbabilityTheory.deMoivreLaplaceStandardized, ProbabilityTheory.standardizedBernoulli
statement: formalized
proof: formalized
---

# De Moivre–Laplace theorem

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html).

## Standardized binomial distribution

For a natural number $n$ and $p \in [0, 1]$, the
standardized binomial distribution is the measure on $\mathbb{R}$ given by the law of
$(S_n - np)/\sqrt{np(1-p)}$, where $S_n$ has the binomial distribution with parameters $n$ and
$p$. When $np(1-p) = 0$ the division by $0$ is read as $0$, so the law is the point mass at $0$.

This is the standardized sum appearing in the De Moivre–Laplace limit theorem.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.standardizedBinomial`, a definition declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#standardized-binomial).

## Affine transformation of a characteristic function

Let $\mu$ be a measure on
$\mathbb{R}$, let $a, s, t \in \mathbb{R}$, and let $\nu$ be the image of $\mu$ under the map
$x \mapsto (x - a)/s$. Then the characteristic functions satisfy
$\varphi_\nu(t) = \varphi_\mu(t s^{-1}) \, e^{-i a t s^{-1}}$. Here $s^{-1}$ and division by $s$
are read as $0$ when $s = 0$, so no hypothesis $s \neq 0$ is needed.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.charFun_map_affine`, a theorem declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#char-fun-map-affine).

## Characteristic function of the real-valued binomial distribution

For every natural
number $n$, every $p \in [0, 1]$ and every real $t$, the characteristic function
$\varphi_{\mathrm{Bin}(n, p)}$ of the binomial distribution $\mathrm{Bin}(n, p)$, viewed as a
measure on $\mathbb{R}$, satisfies
$\varphi_{\mathrm{Bin}(n, p)}(t) = \left((1 - p) + p e^{it}\right)^n$.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.charFun_binomial_real`, a theorem declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#char-fun-binomial-real).

## Second-order Taylor remainder bound for the exponential

For every complex number $z$
with $|z| \le 1$, the remainder after the degree-2 Taylor polynomial of the exponential
satisfies $|e^z - 1 - z - z^2/2| \le 2|z|^3$.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.exp_taylor2_err`, a theorem declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#exp-taylor2-err).

## Characteristic function of the standardized binomial

For every natural number $n$,
every $p \in [0, 1]$ and every real $t$, put $s = \sqrt{np(1-p)}$, with $s^{-1}$ read as $0$ when
$s = 0$. Let $\psi$ be the characteristic function of the binomial distribution
$\mathrm{Bin}(n, p)$ viewed as a measure on $\mathbb{R}$, and $\varphi$ that of the standardized
binomial distribution with parameters $n$ and $p$. Then
$\varphi(t) = \psi(t s^{-1}) \, e^{-i n p t s^{-1}}$.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.charFun_standardizedBinomial`, a theorem declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#char-fun-standardized-binomial).

## Convergence of characteristic functions in De Moivre–Laplace

Let $0 < p < 1$ and
$t \in \mathbb{R}$. As $n \to \infty$, the characteristic function of the standardized binomial
distribution with parameters $n$ and $p$, evaluated at $t$, converges to $e^{-t^2/2}$, the
value at $t$ of the characteristic function of the standard normal distribution.

This is the key analytic step in proving the De Moivre–Laplace theorem via Lévy's continuity
theorem.

Formalized by `MathlibExt.Probability.CharFunStandardizedBinomial.tendsto_charFun_standardizedBinomial`, a theorem declared in [MathlibExt/Probability/CharFunStandardizedBinomial.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CharFunStandardizedBinomial.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#tendsto-char-fun-standardized-binomial).

## Standardized partial sums

For a sequence $X_0, X_1, \dots$ of real-valued functions on a
set $\Omega$, a real number $p$ and $n \in \mathbb{N}$, the standardized partial sum is the
function $\omega \mapsto (S_n(\omega) - np)/\sqrt{np(1-p)}$ on $\Omega$, where
$S_n = X_0 + \dots + X_{n-1}$.

The square root of a negative number is taken to be $0$ and division by $0$ gives $0$; in
particular the standardized partial sum is $0$ for $n = 0$.

Formalized by `ProbabilityTheory.deMoivreLaplaceStandardized`, a definition declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#de-moivre-laplace-standardized).

## Bernoulli standardization map

For a real number $p$, the standardization map sends
$x \in \mathbb{R}$ to $(x - p)/\sqrt{p(1-p)}$.

The square root of a negative number is taken to be $0$ and division by $0$ gives $0$, so for
$p \le 0$ or $p \ge 1$ the map is identically $0$.

Formalized by `ProbabilityTheory.standardizedBernoulli`, a definition declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#standardized-bernoulli).

## Almost surely $\{0, 1\}$-valued random variables are integrable

Let $P$ be a probability
measure on $\Omega$ and let $f : \Omega \to \mathbb{R}$ be almost everywhere measurable with
$f(\omega) \in \{0, 1\}$ for $P$-almost every $\omega$. Then $f$ is integrable with respect to
$P$.

Formalized by `ProbabilityTheory.integrable_of_ae_eq_zero_or_one`, a theorem declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#integrable-of-ae-eq-zero-or-one).

## Second moment of a $\{0, 1\}$-valued random variable

Let $P$ be a probability measure on
$\Omega$ and let $f : \Omega \to \mathbb{R}$ satisfy $f(\omega) \in \{0, 1\}$ for $P$-almost every
$\omega$. Then $\int f^2 \, dP = \int f \, dP$.

Formalized by `ProbabilityTheory.integral_sq_eq_integral_of_ae_eq_zero_or_one`, a theorem declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#integral-sq-eq-integral-of-ae-eq-zero-or).

## De Moivre–Laplace limit theorem, convergence in distribution

Let $X_0, X_1, \dots$ be
independent, identically distributed real random variables on a probability space $(\Omega, P)$,
each almost surely equal to $0$ or $1$, with mean $p$ for some $0 < p < 1$. Write
$S_n = X_0 + \dots + X_{n-1}$. Then the standardized sums $(S_n - np)/\sqrt{np(1-p)}$ converge in
distribution to the standard normal distribution $\mathcal{N}(0, 1)$ as $n \to \infty$.

Formalized by `ProbabilityTheory.deMoivreLaplace_tendstoInDistribution`, a theorem declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#de-moivre-laplace-tendsto-in-distributio).

## De Moivre–Laplace limit theorem, interval form

Let $X_0, X_1, \dots$ be independent,
identically distributed real random variables on a probability space $(\Omega, P)$, each almost
surely equal to $0$ or $1$, with mean $p$ for some $0 < p < 1$. Write
$S_n = X_0 + \dots + X_{n-1}$. Then for all real numbers $a \le b$, the probability
$P\left(a \le (S_n - np)/\sqrt{np(1-p)} \le b\right)$ tends, as $n \to \infty$, to the mass that
the standard normal distribution $\mathcal{N}(0, 1)$ gives to the interval $[a, b]$.

Formalized by `ProbabilityTheory.deMoivreLaplace_interval_probability`, a theorem declared in [MathlibExt/Probability/DeMoivreLaplace.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DeMoivreLaplace.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html#de-moivre-laplace-interval-probability).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: De Moivre–Laplace theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems/de-moivre-laplace-theorem)
