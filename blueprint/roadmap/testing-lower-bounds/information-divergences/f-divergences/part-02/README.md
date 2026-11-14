---
navigation: transparent
---

# condFDiv_ne_top_iff to fDiv_statInfoFun_eq

- [condFDiv_ne_top_iff](lem-condfdiv-ne-top-iff.md)
- [fDiv_compProd_ne_top_iff](lem-fdiv-compprod-ne-top-iff.md)
- [fDiv_compProd_right](lem-fdiv-compprod-right.md)

## Integral representation of $f$-divergences

We prove that any $f$-divergence is an integral over priors of statistical informations, in which the measure depends on $f$. The main references for this part are (Liese and Vajda 2006) and (Liese 2012).

- [Curvature measure](def-curvaturemeasure.md)
- [curvatureMeasure_mul](lem-curvaturemeasure-mul.md)
- [curvatureMeasure_add](lem-curvaturemeasure-add.md)
- [convex_taylor](lem-convex-taylor.md)
- [statInfoFun](def-statinfofun.md)

The following theorem is inspired from (Liese and Vajda 2006, Liese 2012) but gives a different integral representation.

- [fDiv_eq_integral_eGamma](thm-fdiv-eq-integral-egamma.md)

For probability measures, $D_{\phi_{1,y}}(\mu, \nu) = E_y(\mu, \nu)$ , but these functions can differ if $\mu$ and $\nu$ are finite measures with different masses.

*The proof of [Theorem fDiv_eq_integral_eGamma](thm-fdiv-eq-integral-egamma.md) is shown with its statement.*

TODO: define $\Gamma_f$.

TODO: in the lemma below, $I_\pi(\mu, \nu)$ is the correct value for probability measures, but in general it should be replaced by $D_{\phi_{\pi, 1 - \pi}}(\mu, \nu)$ . These functions can differ if $\mu$ and $\nu$ are finite measures with different masses.

## Data-processing inequality

This section contains three proofs of the data-processing inequality for $f$-divergences. That inequality states that for $\mu, \nu$ two measures on $\mathcal X$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel, $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$.

1. A first proof uses the convexity of $f$ through Jensen's inequality for conditional expectations. We first prove the DPI for measurable functions (or deterministic kernels) then use it to extend to the general case.
2. A second proof deals with the general case and uses Radon-Nikodym derivatives of kernels. This restrict its applicability to measurable spaces that satisfy some particular countability assumptions.
3. The last proof uses the representation of $f$-divergence as an integral over statistical (risk-based) divergences, then uses the data-processing inequality for those divergences.

**Lean Remark.** Currently we don't have Lean proofs of Jensen's inequality for conditional expectations (used in proof 1) or of an integration by part lemma that is used in proof 3. Proof 2 gives the weakest results since it is restricted to spaces that satisfy countability assumptions, but it's the only one for which our Lean proof is `sorry`-free.

We first remark that it is sufficient to prove the DPI under an absolute continuity assumption on the measures.

- [DPI_of_DPI_ac](lem-dpi-of-dpi-ac.md)

The next Lemma implies that in order to prove the DPI, it is sufficient to prove $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \kappa)$.

- [Composition-product with a kernel](thm-fdiv-compprod-left-1.md)
- [fDiv_prod_left_1](cor-fdiv-prod-left-1.md)

### DPI: proof using Jensen's inequality for the conditional expectation

This proof lifts the DPI on deterministic kernels to a DPI on all kernels. We first prove the DPI for the special cases of a composition with a deterministic kernel, which is the same as taking the map of the measures by a function.

- [fDiv_map_le](thm-fdiv-map-le.md)
- [Data-processing](thm-fdiv-data-proc-3.md)

### DPI: proof using derivatives of kernels

This proof does not use Jensen's inequality for the conditional expectation, but only for the ordinary expectation. It starts by establishing $D_f(\mu, \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$ for Markov kernels $\kappa$ and $\eta$, then deduces the DPI. Indeed, if the measurable spaces are standard Borel, we can write $\mu \otimes \kappa = ((\kappa \circ \mu) \otimes \kappa^\dagger_\mu)_\leftrightarrow$ for a Markov kernel $\kappa^\dagger_\mu$ (see Definition [bayesInv](../../../probability-transition-kernels/bayesian-inverse-of-a-kernel/def-bayesinv.md); $(...)_\leftrightarrow$ is notation for composition with the map that swaps the coordinates) and then use the inequality to get

$$
\begin{aligned}
D(\kappa \circ \mu, \kappa \circ \nu)
&\le D((\kappa \circ \mu) \otimes \kappa^\dagger_\mu, (\kappa \circ \nu) \otimes \kappa^\dagger_\nu)
\\
&= D(((\kappa \circ \mu) \otimes \kappa^\dagger_\mu)_{\leftrightarrow}, ((\kappa \circ \nu) \otimes \kappa^\dagger_\nu)_{\leftrightarrow})
\\
&= D(\mu \otimes \kappa, \nu \otimes \kappa)
\\
&= D(\mu, \nu)
\: .
\end{aligned}
$$

The main drawback of this approach is that it requires that the Bayesian inverse exists, which is not always the case, unless for example the measurable spaces are standard Borel.

The inequality $D_f(\mu, \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$ is obtained by describing the Radon-Nikodym derivative $\frac{d(\mu \otimes \kappa)}{d(\nu \otimes \eta)}$ and using convexity properties of the function $f$.

- [fDiv_le_compProd_1](thm-fdiv-le-compprod-1.md)
- [Marginals](thm-fdiv-fst-le-1.md)
- [fDiv_comp_le_compProd_1](lem-fdiv-comp-le-compprod-1.md)
- [Conditioning increases f-divergence](thm-fdiv-comp-le-condfdiv-1.md)
- [Data-processing](thm-fdiv-data-proc-1.md)

### DPI: proof using the integral representation

This proof uses that every $f$-divergence is an integral over $\gamma \ge 0$ of $f$-divergences for the function $\phi_{1,\gamma}$ of Definition [statInfoFun](def-statinfofun.md). It suffices then to prove the DPI for those particular $f$-divergences. Those are equal to the $E_\gamma$ divergence, up to a term that is invariant by composition with a Markov kernel. Finally, we already know that the $E_\gamma$ divergence satisfies the DPI, and that completes the proof.

- [fDiv_statInfoFun_eq](lem-fdiv-statinfofun-eq.md)
