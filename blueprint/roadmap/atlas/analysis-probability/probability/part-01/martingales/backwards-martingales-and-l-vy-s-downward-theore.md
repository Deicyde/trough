---
declaration: section
origin: cited
lean: MeasureTheory.levy_downward_ae, MeasureTheory.levy_downward_tendsto_eLpNorm_one, MeasureTheory.IsBackwardsMartingale, MeasureTheory.backwards_martingale_ae_tendsto, MeasureTheory.backwards_martingale_tendsto_eLpNorm_one, MeasureTheory.Filtration.tailAlgebra, MeasureTheory.Filtration.tailAlgebra_le, MeasureTheory.Filtration.tailAlgebra_le_seq
statement: formalized
proof: formalized
---

# Backwards martingales and Lévy's downward theorem

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html).

## Lévy's downward theorem, almost sure convergence

Let $(\Omega, \mathcal F, \mu)$ be a
probability space, let $\mathcal F_0 \supseteq \mathcal F_1 \supseteq \cdots$ be a decreasing
sequence of sub-σ-algebras of $\mathcal F$, and let $\mathcal F_\infty = \bigcap_n \mathcal F_n$.
For every function $g : \Omega \to \mathbb R$, the conditional expectations
$\mathbb E[g \mid \mathcal F_n]$ converge to $\mathbb E[g \mid \mathcal F_\infty]$ as
$n \to \infty$, $\mu$-almost everywhere.

No integrability hypothesis is needed: for a non-integrable $g$ every conditional expectation is
$0$ by convention, and the statement is trivial.

Formalized by `MeasureTheory.levy_downward_ae`, a theorem declared in [MathlibExt/Probability/BackwardsMartingales.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingales.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#levy-downward-ae).

## Lévy's downward theorem in L¹

Let $(\Omega, \mathcal F, \mu)$ be a probability space,
let $\mathcal F_0 \supseteq \mathcal F_1 \supseteq \cdots$ be a decreasing sequence of
sub-σ-algebras of $\mathcal F$, and let $\mathcal F_\infty = \bigcap_n \mathcal F_n$. For every
integrable function $g : \Omega \to \mathbb R$, the $L^1(\mu)$ norm
$\lVert \mathbb E[g \mid \mathcal F_n] - \mathbb E[g \mid \mathcal F_\infty] \rVert_1$ tends to $0$
as $n \to \infty$.

Formalized by `MeasureTheory.levy_downward_tendsto_eLpNorm_one`, a theorem declared in [MathlibExt/Probability/BackwardsMartingales.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingales.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#levy-downward-tendsto-e-lp-norm-one).

## Backwards martingale

Let $\mu$ be a measure on a measurable space $(\Omega, \mathcal F)$
and let $(\mathcal F_n)_{n \ge 0}$ be a sequence of σ-algebras on $\Omega$. A sequence of
functions $M_n : \Omega \to \mathbb R$ is a backwards martingale with respect to $(\mathcal F_n)$
and $\mu$ if $M_0$ is $\mu$-integrable and, for every $n$, $M_n = \mathbb E[M_0 \mid \mathcal F_n]$
$\mu$-almost everywhere.

Here $\mathbb E[M_0 \mid \mathcal F_n]$ is the conditional expectation with respect to $\mu$ when
$\mathcal F_n \subseteq \mathcal F$ and the restriction of $\mu$ to $\mathcal F_n$ is σ-finite,
and is $0$ by convention otherwise. The definition is used when $(\mathcal F_n)$ is a decreasing
sequence of sub-σ-algebras, but it does not require this.

Formalized by `MeasureTheory.IsBackwardsMartingale`, a definition declared in [MathlibExt/Probability/BackwardsMartingales.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingales.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#is-backwards-martingale).

## Backwards martingale convergence theorem, almost sure convergence

Let
$(\Omega, \mathcal F, \mu)$ be a probability space, let
$\mathcal F_0 \supseteq \mathcal F_1 \supseteq \cdots$ be a decreasing sequence of sub-σ-algebras
of $\mathcal F$, and let $\mathcal F_\infty = \bigcap_n \mathcal F_n$. If the real-valued process
$(M_n)_{n \ge 0}$ is a backwards martingale with respect to $(\mathcal F_n)$ and $\mu$, then
$M_n \to \mathbb E[M_0 \mid \mathcal F_\infty]$ as $n \to \infty$, $\mu$-almost everywhere.

Formalized by `MeasureTheory.backwards_martingale_ae_tendsto`, a theorem declared in [MathlibExt/Probability/BackwardsMartingales.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingales.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#backwards-martingale-ae-tendsto).

## Backwards martingale convergence theorem in L¹

Let $(\Omega, \mathcal F, \mu)$ be a
probability space, let $\mathcal F_0 \supseteq \mathcal F_1 \supseteq \cdots$ be a decreasing
sequence of sub-σ-algebras of $\mathcal F$, and let $\mathcal F_\infty = \bigcap_n \mathcal F_n$.
If the real-valued process $(M_n)_{n \ge 0}$ is a backwards martingale with respect to
$(\mathcal F_n)$ and $\mu$, then the $L^1(\mu)$ norm
$\lVert M_n - \mathbb E[M_0 \mid \mathcal F_\infty] \rVert_1$ tends to $0$ as $n \to \infty$.

Formalized by `MeasureTheory.backwards_martingale_tendsto_eLpNorm_one`, a theorem declared in [MathlibExt/Probability/BackwardsMartingales.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingales.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#backwards-martingale-tendsto-e-lp-norm-o).

## Tail sigma-algebra of a decreasing filtration

The tail sigma-algebra of a decreasing filtration, the intersection of its levels.

Formalized by `MeasureTheory.Filtration.tailAlgebra`, a definition declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#tail-algebra).

## Tail sigma-algebra lies in the ambient sigma-algebra

The tail sigma-algebra lies in the ambient sigma-algebra.

Formalized by `MeasureTheory.Filtration.tailAlgebra_le`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#tail-algebra-le).

## Tail sigma-algebra lies in every level of the filtration

The tail sigma-algebra lies in every level of the decreasing filtration.

Formalized by `MeasureTheory.Filtration.tailAlgebra_le_seq`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#tail-algebra-le-seq).

## Tail sigma-algebra of a constant filtration

A constant decreasing filtration has its constant value as tail algebra.

Formalized by `MeasureTheory.Filtration.tailAlgebra_const`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#tail-algebra-const).

## Conditional expectations along a filtration are strongly adapted

Conditional-expectation representatives are strongly adapted separately
from their canonical backwards-martingale membership. No integrability of g is needed.

Formalized by `MeasureTheory.Filtration.stronglyAdapted_condExp`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#strongly-adapted-cond-exp).

## Terms of a backwards martingale are integrable

Every term is integrable by its canonical conditional-expectation representation.

Formalized by `MeasureTheory.IsBackwardsMartingale.integrable`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#integrable).

## Backwards martingales are uniformly integrable

Canonical backwards membership is uniformly integrable in L1 on a finite measure.
The ambient bounds suffice; representative adaptedness and antitonicity are unnecessary.

Formalized by `MeasureTheory.IsBackwardsMartingale.uniformIntegrable`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#uniform-integrable).

## Conditioning a backwards martingale on the next level

Conditioning a term on the next, smaller level gives the next term a.e.

Formalized by `MeasureTheory.IsBackwardsMartingale.condExp_succ_ae_eq`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#cond-exp-succ-ae-eq).

## Conditional expectations form a backwards martingale

Conditional expectations of arbitrary g form a canonical backwards martingale
along decreasing sub-sigma-algebras. The nonintegrable-g convention is retained.

Formalized by `MeasureTheory.isBackwardsMartingale_condExp`, a theorem declared in [MathlibExt/Probability/BackwardsMartingale.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BackwardsMartingale.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#is-backwards-martingale-cond-exp).

## Almost-everywhere convergent conditional expectations converge in L¹

Let $\mu$ be a finite
measure on a measurable space $(\Omega, \mathcal{F})$, let $(\mathcal{G}_n)_{n \in \mathbb{N}}$ be
a sequence of sub-σ-algebras of $\mathcal{F}$, let $g : \Omega \to \mathbb{R}$ be integrable,
and write $\mu[g \mid \mathcal{G}_n]$ for the conditional expectation of $g$ given
$\mathcal{G}_n$ with respect to $\mu$. If $h : \Omega \to \mathbb{R}$ is integrable and
$\mu[g \mid \mathcal{G}_n] \to h$ $\mu$-almost everywhere as $n \to \infty$, then
$\int_\Omega |\mu[g \mid \mathcal{G}_n] - h| \, d\mu \to 0$ as $n \to \infty$.

This is Vitali's theorem applied to the uniformly integrable family of conditional expectations of
a single integrable function.

Formalized by `MathlibExt.Probability.CondExpAntitoneLimit.tendsto_eLpNorm_condExp_sub_of_ae_tendsto`, a theorem declared in [MathlibExt/Probability/CondExpAntitoneLimit.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CondExpAntitoneLimit.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#tendsto-e-lp-norm-cond-exp-sub-of-ae-ten).

## Identifying the a.e. limit of conditional expectations

Let $\mu$ be a finite measure on a
measurable space $(\Omega, \mathcal{F})$, let $(\mathcal{G}_n)_{n \in \mathbb{N}}$ be any
sequence of sub-σ-algebras of $\mathcal{F}$ (not assumed monotone), and let
$g : \Omega \to \mathbb{R}$ be integrable. Write $\mu[g \mid \mathcal{G}]$ for the conditional
expectation of $g$ given a sub-σ-algebra $\mathcal{G}$ with respect to $\mu$, and
$\mathcal{G}_\infty = \bigcap_n \mathcal{G}_n$. Suppose $h : \Omega \to \mathbb{R}$ is
integrable, strongly measurable with respect to $\mathcal{G}_\infty$, and
$\mu[g \mid \mathcal{G}_n](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/\omega) \to h(\omega)$ as $n \to \infty$ for $\mu$-almost every
$\omega$. Then $h = \mu[g \mid \mathcal{G}_\infty]$ $\mu$-almost everywhere.

Formalized by `MathlibExt.Probability.CondExpAntitoneLimit.condExp_antitone_limit_eq`, a theorem declared in [MathlibExt/Probability/CondExpAntitoneLimit.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CondExpAntitoneLimit.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html#cond-exp-antitone-limit-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Backwards martingales and Lévy's downward theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/backwards-martingales-and-l-vy-s-downward-theore)
