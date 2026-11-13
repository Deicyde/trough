---
declaration: section
origin: cited
lean: MeasureTheory.Martingale.doob_sq_maximal_ineq, MeasureTheory.predictableQuadraticVariation, MeasureTheory.Martingale.integral_predictableQuadraticVariation, MeasureTheory.Martingale.doob_sq_maximal_ineq_predictableQuadraticVariation, MeasureTheory.Martingale.doob_sq_maximal_ineq_iSup
statement: formalized
proof: formalized
---

# Doob's maximal inequalities

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html).

## Doob's L² maximal inequality, finite horizon

Let $\mu$ be a probability measure and let
$(f_k)_{k \in \mathbb{N}}$ be a real-valued martingale with respect to a filtration
$(\mathcal{F}_k)$ and $\mu$ such that every $f_k$ is in $L^2(\mu)$. Then for every
$n \in \mathbb{N}$, $\int (\max_{k \le n} |f_k|)^2 \, d\mu \le 4 \int f_n^2 \, d\mu$.

Formalized by `MeasureTheory.Martingale.doob_sq_maximal_ineq`, a theorem declared in [MathlibExt/Probability/DoobLpInequality.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DoobLpInequality.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html#doob-sq-maximal-ineq).

## Predictable quadratic variation

Let $\mu$ be a measure on $\Omega$, let
$(\mathcal{F}_k)_{k \in \mathbb{N}}$ be a filtration and let $(f_k)_{k \in \mathbb{N}}$ be a
real-valued process. The predictable quadratic variation of $f$ with respect to
$(\mathcal{F}_k)$ and $\mu$ is the process defined pointwise by
$A_n(\omega) = \sum_{k=0}^{n-1} \mathbb{E}_\mu[(f_{k+1} - f_k)^2 \mid \mathcal{F}_k](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/doob-s-maximal-inequalities/\omega)$,
so $A_0 = 0$. For a square-integrable martingale this is the predictable part of $f^2$ in Doob's
decomposition.

Formalized by `MeasureTheory.predictableQuadraticVariation`, a definition declared in [MathlibExt/Probability/DoobLpInequality.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DoobLpInequality.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html#predictable-quadratic-variation).

## Expectation of the predictable quadratic variation

Let $\mu$ be a probability measure
and let $(f_k)_{k \in \mathbb{N}}$ be a real-valued martingale with respect to a filtration
$(\mathcal{F}_k)$ and $\mu$ such that every $f_k$ is in $L^2(\mu)$, and let $A_n$ be its
predictable quadratic variation. Then for every $n \in \mathbb{N}$,
$\int A_n \, d\mu = \int f_n^2 \, d\mu - \int f_0^2 \, d\mu$.

The proof telescopes, using the orthogonality of martingale increments.

Formalized by `MeasureTheory.Martingale.integral_predictableQuadraticVariation`, a theorem declared in [MathlibExt/Probability/DoobLpInequality.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DoobLpInequality.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html#integral-predictable-quadratic-variation).

## Doob's L² maximal inequality in terms of the predictable quadratic variation, finite horizon

**Doob's L² maximal inequality in terms of the predictable quadratic
variation, finite horizon.** Let $\mu$ be a probability measure and let $(f_k)_{k \in \mathbb{N}}$
be a real-valued martingale with respect to a filtration $(\mathcal{F}_k)$ and $\mu$ such that
every $f_k$ is in $L^2(\mu)$ and $f_0 = 0$ almost everywhere, and let $A_n$ be its predictable
quadratic variation. Then for every $n \in \mathbb{N}$,
$\int (\max_{k \le n} |f_k|)^2 \, d\mu \le 4 \int A_n \, d\mu$.

Formalized by `MeasureTheory.Martingale.doob_sq_maximal_ineq_predictableQuadraticVariation`, a theorem declared in [MathlibExt/Probability/DoobLpInequality.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DoobLpInequality.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html#doob-sq-maximal-ineq-predictable-quadrat).

## Doob's L² maximal inequality, infinite horizon

Let $\mu$ be a probability measure, let
$(f_n)_{n \in \mathbb{N}}$ be a real-valued martingale with respect to a filtration
$(\mathcal{F}_n)$ and $\mu$ such that every $f_n$ is in $L^2(\mu)$ and $f_0 = 0$ almost
everywhere, and let $A_n$ be its predictable quadratic variation. Then
$\int \sup_n |f_n|^2 \, d\mu \le 4 \int \sup_n \max(A_n, 0) \, d\mu$, where both integrals are
of $[0, \infty]$-valued functions and may be infinite.

Since each $A_n$ is nonnegative almost everywhere, the right side is $4\,\mathbb{E}[A_\infty]$
with $A_\infty = \sup_n A_n$.

Formalized by `MeasureTheory.Martingale.doob_sq_maximal_ineq_iSup`, a theorem declared in [MathlibExt/Probability/DoobLpInequality.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DoobLpInequality.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html#doob-sq-maximal-ineq-i-sup).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Doob's maximal inequalities](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/doob-s-maximal-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/doob-s-maximal-inequalities)
