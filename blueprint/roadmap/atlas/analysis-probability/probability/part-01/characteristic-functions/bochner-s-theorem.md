---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.BochnerWanted.bochner, ProbabilityTheory.IsPositiveDefinite, ProbabilityTheory.IsPositiveDefiniteReal, ProbabilityTheory.IsCharacteristicFun, ProbabilityTheory.IsCharacteristicFunReal, ProbabilityTheory.bochner_forward, ProbabilityTheory.charFun_isPositiveDefinite, ProbabilityTheory.bochner_forward_real
statement: formalized
proof: formalized
---

# Bochner's theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html).

## Bochner's theorem

Let $f : \mathbb{R} \to \mathbb{C}$. Then $f$ is continuous, satisfies
$f(0) = 1$, and is positive definite, meaning that for every $n \in \mathbb{N}$, all points
$x_1, \dots, x_n \in \mathbb{R}$ and all coefficients $c_1, \dots, c_n \in \mathbb{C}$ the sum
$S = \sum_{i=1}^{n} \sum_{j=1}^{n} \overline{c_i}\, c_j\, f(x_i - x_j)$ is a nonnegative real
number, if and only if there is a Borel probability measure $\mu$ on $\mathbb{R}$ such that
$f(t) = \int_{\mathbb{R}} e^{itx} \, d\mu(x)$ for every $t \in \mathbb{R}$, that is, $f$ is the
characteristic function of $\mu$.

## Sources

- Bochner's theorem on positive-definite functions, S. Bochner, Vorlesungen über Fouriersche Integrale 1932 and Math. Ann. 108 (1933); see Folland, Abstract Harmonic Analysis, Fourier Analysis on Groups; Lean is ℝ→ℂ iff version continuous f 0=1 positive- definite via double sum iff ∃ Borel probability μ with f = charFun μ, fixed +I sign via charFun.

Formalized by `MathlibExt.Analysis.Fourier.BochnerWanted.bochner`, a theorem declared in [MathlibExt/Analysis/Fourier/Bochner.lean, line 1664](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/Bochner.lean#L1664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#bochner).

## Positive definite functions

A function $\varphi : \mathbb{R} \to \mathbb{C}$ is
positive definite when for every $n \in \mathbb{N}$, all $t_1, \dots, t_n \in \mathbb{R}$ and all
$z_1, \dots, z_n \in \mathbb{C}$, the sum
$S = \sum_{i=1}^{n} \sum_{j=1}^{n} \varphi(t_i - t_j) \, z_i \, \overline{z_j}$ is real and
nonnegative, that is, $\operatorname{Im} S = 0$ and $\operatorname{Re} S \ge 0$.

Formalized by `ProbabilityTheory.IsPositiveDefinite`, a definition declared in [MathlibExt/Probability/BochnerForward.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#is-positive-definite).

## Positive definite real-valued functions

A function $\varphi : \mathbb{R} \to \mathbb{R}$
is positive definite when its composition with the inclusion $\mathbb{R} \to \mathbb{C}$ is
positive definite, that is, when for every $n \in \mathbb{N}$, all
$t_1, \dots, t_n \in \mathbb{R}$ and all $z_1, \dots, z_n \in \mathbb{C}$, the sum
$\sum_{i=1}^{n} \sum_{j=1}^{n} \varphi(t_i - t_j) \, z_i \, \overline{z_j}$ is a nonnegative
real number.

Formalized by `ProbabilityTheory.IsPositiveDefiniteReal`, a definition declared in [MathlibExt/Probability/BochnerForward.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#is-positive-definite-real).

## Characteristic functions

A function $\varphi : \mathbb{R} \to \mathbb{C}$ is a
characteristic function when there is a probability measure $\mu$ on $\mathbb{R}$ whose
characteristic function equals $\varphi$, that is,
$\int_{\mathbb{R}} e^{itx} \, d\mu(x) = \varphi(t)$ for every $t \in \mathbb{R}$.

Formalized by `ProbabilityTheory.IsCharacteristicFun`, a definition declared in [MathlibExt/Probability/BochnerForward.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#is-characteristic-fun).

## Real-valued characteristic functions

A function $\varphi : \mathbb{R} \to \mathbb{R}$
is a real-valued characteristic function when its composition with the inclusion
$\mathbb{R} \to \mathbb{C}$ is a characteristic function, that is, when there is a probability
measure $\mu$ on $\mathbb{R}$ with $\int_{\mathbb{R}} e^{itx} \, d\mu(x) = \varphi(t)$ for every
$t \in \mathbb{R}$.

Formalized by `ProbabilityTheory.IsCharacteristicFunReal`, a definition declared in [MathlibExt/Probability/BochnerForward.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#is-characteristic-fun-real).

## Forward direction of Bochner's theorem

Let $\varphi : \mathbb{R} \to \mathbb{C}$ be the
characteristic function of a probability measure on $\mathbb{R}$. Then $\varphi$ is continuous,
positive definite, and satisfies $\varphi(0) = 1$.

Formalized by `ProbabilityTheory.bochner_forward`, a theorem declared in [MathlibExt/Probability/BochnerForward.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#bochner-forward).

## Characteristic functions are positive definite

Let $\mu$ be a probability measure on
$\mathbb{R}$ with characteristic function $\varphi_\mu(t) = \int_{\mathbb{R}} e^{itx} \, d\mu(x)$.
Then $\varphi_\mu$ is positive definite: for every $n \in \mathbb{N}$, all
$t_1, \dots, t_n \in \mathbb{R}$ and all $z_1, \dots, z_n \in \mathbb{C}$, the sum
$\sum_{i=1}^{n} \sum_{j=1}^{n} \varphi_\mu(t_i - t_j) \, z_i \, \overline{z_j}$ is a nonnegative
real number.

Formalized by `ProbabilityTheory.charFun_isPositiveDefinite`, a theorem declared in [MathlibExt/Probability/BochnerForward.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#char-fun-is-positive-definite).

## Real-valued characteristic functions are continuous and positive definite

Let
$\varphi : \mathbb{R} \to \mathbb{R}$ be a real-valued characteristic function, that is, a
function whose composition with the inclusion $\mathbb{R} \to \mathbb{C}$ is the
characteristic function of a probability measure on $\mathbb{R}$. Then $\varphi$ is
continuous, $\varphi$ is positive definite in the sense that its composition with the
inclusion $\mathbb{R} \to \mathbb{C}$ is positive definite, and $\varphi(0) = 1$.

Formalized by `ProbabilityTheory.bochner_forward_real`, a theorem declared in [MathlibExt/Probability/BochnerForward.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BochnerForward.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html#bochner-forward-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bochner's theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/bochner-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/characteristic-functions/bochner-s-theorem)
