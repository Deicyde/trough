---
declaration: section
origin: cited
lean: MeasureTheory.scheffe_lemma, MeasureTheory.tendsto_eLpNorm_one_of_tendstoInMeasure_of_tendsto_eLpNorm, MeasureTheory.uniformIntegrable_of_tendstoInMeasure_of_tendsto_eLpNorm, MeasureTheory.uniformIntegrable_tfae_of_tendstoInMeasure, MathlibExt.MeasureTheory.ScheffeL1ConvergenceWanted.tendsto_integral_abs_sub_of_ae_tendsto_of_tendsto_integral_abs
statement: formalized
---

# Scheffé's lemma

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html).

## Scheffé's lemma

Let $\mu$ be a measure on a measurable space $\alpha$, let
$f_n : \alpha \to \mathbb{R}$ ($n \in \mathbb{N}$) be $\mu$-almost everywhere strongly measurable,
and let $g : \alpha \to \mathbb{R}$ be in $L^1(\mu)$. Write
$\|h\|_1 = \int |h| \, d\mu \in [0, \infty]$ for the $L^1$ seminorm. If $f_n(x) \to g(x)$ for
$\mu$-almost every $x$ and $\|f_n\|_1 \to \|g\|_1$ in $[0, \infty]$, then $\|f_n - g\|_1 \to 0$,
that is, $f_n \to g$ in $L^1(\mu)$.

Formalized by `MeasureTheory.scheffe_lemma`, a theorem declared in [MathlibExt/MeasureTheory/Function/ScheffeLemma.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/ScheffeLemma.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html#scheffe-lemma).

## Scheffé's lemma for convergence in measure

Let $\mu$ be a measure on a measurable space
$\alpha$, let $f_n : \alpha \to \mathbb{R}$ ($n \in \mathbb{N}$) and $g : \alpha \to \mathbb{R}$ be
in $L^1(\mu)$, and write $\|h\|_1 = \int |h| \, d\mu$. If $f_n \to g$ in $\mu$-measure (for every
$\varepsilon > 0$, $\mu\{x : |f_n(x) - g(x)| \ge \varepsilon\} \to 0$) and $\|f_n\|_1 \to \|g\|_1$,
then $\|f_n - g\|_1 \to 0$, that is, $f_n \to g$ in $L^1(\mu)$.

The proof applies Scheffé's lemma along a further subsequence, extracted from every subsequence by
convergence in measure.

Formalized by `MeasureTheory.tendsto_eLpNorm_one_of_tendstoInMeasure_of_tendsto_eLpNorm`, a theorem declared in [MathlibExt/MeasureTheory/Function/ScheffeLemma.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/ScheffeLemma.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html#tendsto-e-lp-norm-one-of-tendsto-in-meas).

## Convergence in measure with converging L¹ norms implies uniform integrability

Let $\mu$
be a measure on a measurable space $\alpha$, let $f_n : \alpha \to \mathbb{R}$ ($n \in \mathbb{N}$)
and $g : \alpha \to \mathbb{R}$ be in $L^1(\mu)$, and write $\|h\|_1 = \int |h| \, d\mu$. If
$f_n \to g$ in $\mu$-measure (for every $\varepsilon > 0$,
$\mu\{x : |f_n(x) - g(x)| \ge \varepsilon\} \to 0$) and $\|f_n\|_1 \to \|g\|_1$, then the family
$(f_n)$ is uniformly integrable: $\sup_n \|f_n\|_1 < \infty$, and the supremum of
$\int_s |f_n| \, d\mu$ over all $n$ and all sets $s \subseteq \alpha$ with $\mu(s) \le \delta$
tends to $0$ as $\delta \to 0$.

The proof combines the $L^1$ convergence $\|f_n - g\|_1 \to 0$ given by Scheffé's lemma for
convergence in measure with the Vitali convergence theorem.

Formalized by `MeasureTheory.uniformIntegrable_of_tendstoInMeasure_of_tendsto_eLpNorm`, a theorem declared in [MathlibExt/MeasureTheory/Function/ScheffeLemma.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/ScheffeLemma.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html#uniform-integrable-of-tendsto-in-measure).

## Uniform integrability equivalences

Let $\mu$ be a finite measure on a measurable space
$\alpha$, let $f_n : \alpha \to \mathbb{R}$ ($n \in \mathbb{N}$) and $g : \alpha \to \mathbb{R}$ be
in $L^1(\mu)$, write $\|h\|_1 = \int |h| \, d\mu$, and suppose that $f_n \to g$ in $\mu$-measure
(for every $\varepsilon > 0$, $\mu\{x : |f_n(x) - g(x)| \ge \varepsilon\} \to 0$). Then the
following are equivalent: (1) the family $(f_n)$ is uniformly integrable, that is,
$\sup_n \|f_n\|_1 < \infty$ and the supremum of $\int_s |f_n| \, d\mu$ over all $n$ and all sets
$s \subseteq \alpha$ with $\mu(s) \le \delta$ tends to $0$ as $\delta \to 0$; (2) $f_n \to g$ in
$L^1(\mu)$, that is, $\|f_n - g\|_1 \to 0$; (3) $\|f_n\|_1 \to \|g\|_1$.

The equivalence of (1) and (2) is the Vitali convergence theorem; (3) implies (2) by Scheffé's
lemma for convergence in measure, and (2) implies (3) by the reverse triangle inequality.

Formalized by `MeasureTheory.uniformIntegrable_tfae_of_tendstoInMeasure`, a theorem declared in [MathlibExt/MeasureTheory/Function/ScheffeLemma.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Function/ScheffeLemma.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html#uniform-integrable-tfae-of-tendsto-in-me).

## Scheffé's lemma on the real line

Let $f : \mathbb{R} \to \mathbb{R}$ be integrable and
let $(f_n)_{n \in \mathbb{N}}$ be a sequence of integrable real functions $f_n$ on $\mathbb{R}$
such that $f_n(x) \to f(x)$ for almost every $x \in \mathbb{R}$. If
$\int_{\mathbb{R}} |f_n| \to \int_{\mathbb{R}} |f|$ as $n \to \infty$, then
$\int_{\mathbb{R}} |f_n - f| \to 0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_76`.

Stated but not proved: `MathlibExt.MeasureTheory.ScheffeL1ConvergenceWanted.tendsto_integral_abs_sub_of_ae_tendsto_of_tendsto_integral_abs` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ScheffeL1ConvergenceWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScheffeL1ConvergenceWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html#tendsto-integral-abs-sub-of-ae-tendsto-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scheffé's lemma](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/scheff-s-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/integration/scheff-s-lemma)
