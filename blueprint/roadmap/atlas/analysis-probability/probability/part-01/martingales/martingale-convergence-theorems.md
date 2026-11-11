---
declaration: section
origin: cited
lean: MeasureTheory.Martingale.tendsto_eLpNorm_limitProcess_of_eLpNorm_bdd, MeasureTheory.Submartingale.uniformIntegrable_tfae, MeasureTheory.Martingale.uniformIntegrable_tfae, MeasureTheory.Martingale.ae_tendsto_of_tendsto_predictableQuadVar, MeasureTheory.Submartingale.integral_mono, MeasureTheory.Submartingale.integral_norm_le, MeasureTheory.Submartingale.exists_ae_tendsto_of_posPart_bdd, MeasureTheory.Supermartingale.exists_ae_tendsto_of_negPart_bdd
statement: formalized
proof: formalized
---

# Martingale convergence theorems

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html).

## The $L^p$ martingale convergence theorem

Let $(\Omega, \mu)$ be a probability space
with a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, write
$\mathcal{F}_\infty = \bigvee_n \mathcal{F}_n$, let $1 < p < \infty$, and let
$(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$
whose $L^p$ norms are uniformly bounded: there is a constant $R \ge 0$ with
$\|f_n\|_{L^p(\mu)} \le R$ for every $n$. Let $f_\infty$ be the limit process of $(f_n)$, that
is, a chosen $\mathcal{F}_\infty$-measurable function to which $f_n$ converges almost everywhere
if such a function exists, and $0$ otherwise. Then $f_n \to f_\infty$ almost surely, and
$\|f_n - f_\infty\|_{L^p(\mu)} \to 0$ as $n \to \infty$.

Formalized by `MeasureTheory.Martingale.tendsto_eLpNorm_limitProcess_of_eLpNorm_bdd`, a theorem declared in [MathlibExt/Probability/MartingaleLpConvergence.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MartingaleLpConvergence.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#tendsto-e-lp-norm-limit-process-of-e-lp).

## Equivalent conditions for uniform integrability of a submartingale

Let $(\Omega, \mu)$ be
a probability space with a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and let
$(X_n)_{n \in \mathbb{N}}$ be a real-valued submartingale with respect to $(\mathcal{F}_n)$ and
$\mu$. The following are equivalent:
1. $(X_n)$ is uniformly integrable.
2. There is an integrable $X_\infty$ such that $X_n \to X_\infty$ almost surely and
   $\int |X_n - X_\infty| \, d\mu \to 0$.
3. There is an integrable $X_\infty$ such that $\int |X_n - X_\infty| \, d\mu \to 0$.

Formalized by `MeasureTheory.Submartingale.uniformIntegrable_tfae`, a theorem declared in [MathlibExt/Probability/MartingaleUniformIntegrability.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MartingaleUniformIntegrability.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#uniform-integrable-tfae).

## Equivalent conditions for uniform integrability of a martingale

Let $(\Omega, \mu)$ be a
probability space with a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and let
$(X_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$.
The following are equivalent:
1. $(X_n)$ is uniformly integrable.
2. There is an integrable $X_\infty$ such that $X_n \to X_\infty$ almost surely and
   $\int |X_n - X_\infty| \, d\mu \to 0$.
3. There is an integrable $X_\infty$ such that $\int |X_n - X_\infty| \, d\mu \to 0$.
4. There is an integrable $X_\infty$ such that $X_n = \mathbb{E}[X_\infty \mid \mathcal{F}_n]$
   almost surely for every $n$.

Formalized by `MeasureTheory.Martingale.uniformIntegrable_tfae`, a theorem declared in [MathlibExt/Probability/MartingaleUniformIntegrability.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MartingaleUniformIntegrability.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#uniform-integrable-tfae-2).

## Square-integrable martingale convergence

Let $(X_n)_{n \in \mathbb{N}}$ be a
real-valued martingale with respect to a filtration $(\mathcal{F}_n)$ on a probability space,
with $E[X_n^2] < \infty$ for every $n$, and let $(A_n)$ be its predictable quadratic variation.
Then for almost every $\omega$: if $A_n(\omega)$ converges to a real limit as $n \to \infty$,
then $X_n(\omega)$ converges to a real limit as well.

In particular, $X_n$ converges almost surely on the event $\{\sup_n A_n < \infty\}$, since
$A_n$ is almost surely non-decreasing in $n$.

Formalized by `MeasureTheory.Martingale.ae_tendsto_of_tendsto_predictableQuadVar`, a theorem declared in [MathlibExt/Probability/SqMartingaleConvergence.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SqMartingaleConvergence.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#ae-tendsto-of-tendsto-predictable-quad-v).

## Expectations increase along a submartingale

Let $(X_n)_{n \ge 0}$ be a real-valued
submartingale with respect to a filtration $(\mathcal F_n)_{n \ge 0}$ on a probability space
$(\Omega, \mu)$. Then $\int X_i \, d\mu \le \int X_j \, d\mu$ for all natural numbers $i \le j$.

Formalized by `MeasureTheory.Submartingale.integral_mono`, a theorem declared in [MathlibExt/Probability/SubmartingaleConvergence.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SubmartingaleConvergence.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#integral-mono).

## L¹ bound for a submartingale with bounded positive parts

Let $(X_n)_{n \ge 0}$ be a
real-valued submartingale with respect to a filtration $(\mathcal F_n)_{n \ge 0}$ on a probability
space $(\Omega, \mu)$, and let $C$ be a real number with $\int X_n^+ \, d\mu \le C$ for every $n$,
where $X_n^+$ is the positive part of $X_n$. Then for every $n$,
$\int |X_n| \, d\mu \le 2C - \int X_0 \, d\mu$.

The proof uses the identity $|x| = 2x^+ - x$ together with the monotonicity of
$n \mapsto \int X_n \, d\mu$.

Formalized by `MeasureTheory.Submartingale.integral_norm_le`, a theorem declared in [MathlibExt/Probability/SubmartingaleConvergence.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SubmartingaleConvergence.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#integral-norm-le).

## Submartingale almost-sure convergence theorem

Let $(X_n)_{n \ge 0}$ be a real-valued
submartingale with respect to a filtration $(\mathcal F_n)_{n \ge 0}$ on a probability space
$(\Omega, \mu)$, and let $C$ be a real number with $\int X_n^+ \, d\mu \le C$ for every $n$, where
$X_n^+$ is the positive part of $X_n$. Then there is an integrable function
$X_\infty : \Omega \to \mathbb R$ such that $X_n(\omega) \to X_\infty(\omega)$ as $n \to \infty$
for $\mu$-almost every $\omega$.

Formalized by `MeasureTheory.Submartingale.exists_ae_tendsto_of_posPart_bdd`, a theorem declared in [MathlibExt/Probability/SubmartingaleConvergence.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SubmartingaleConvergence.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#exists-ae-tendsto-of-pos-part-bdd).

## Supermartingale almost-sure convergence theorem

Let $(X_n)_{n \ge 0}$ be a real-valued
supermartingale with respect to a filtration $(\mathcal F_n)_{n \ge 0}$ on a probability space
$(\Omega, \mu)$, and let $C$ be a real number with $\int X_n^- \, d\mu \le C$ for every $n$, where
$X_n^-$ is the negative part of $X_n$. Then there is an integrable function
$X_\infty : \Omega \to \mathbb R$ such that $X_n(\omega) \to X_\infty(\omega)$ as $n \to \infty$
for $\mu$-almost every $\omega$.

This follows from the submartingale theorem applied to $-X$, since $(-X_n)^+ = X_n^-$.

Formalized by `MeasureTheory.Supermartingale.exists_ae_tendsto_of_negPart_bdd`, a theorem declared in [MathlibExt/Probability/SubmartingaleConvergence.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SubmartingaleConvergence.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#exists-ae-tendsto-of-neg-part-bdd).

## Martingale almost-sure convergence theorem

Let $(X_n)_{n \ge 0}$ be a real-valued
martingale with respect to a filtration $(\mathcal F_n)_{n \ge 0}$ on a probability space
$(\Omega, \mu)$, and let $C$ be a real number with $\int X_n^+ \, d\mu \le C$ for every $n$, where
$X_n^+$ is the positive part of $X_n$. Then there is an integrable function
$X_\infty : \Omega \to \mathbb R$ such that $X_n(\omega) \to X_\infty(\omega)$ as $n \to \infty$
for $\mu$-almost every $\omega$.

This is the submartingale theorem, since every martingale is a submartingale.

Formalized by `MeasureTheory.Martingale.exists_ae_tendsto_of_posPart_bdd`, a theorem declared in [MathlibExt/Probability/SubmartingaleConvergence.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SubmartingaleConvergence.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html#exists-ae-tendsto-of-pos-part-bdd-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Martingale convergence theorems](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/martingale-convergence-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/martingales/martingale-convergence-theorems)
