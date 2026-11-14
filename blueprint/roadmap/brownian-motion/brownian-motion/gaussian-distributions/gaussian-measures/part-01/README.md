---
navigation: transparent
---

# Gaussian law to charFun_stdGaussian

- [Gaussian law](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-law.md)
- [charFun_gaussianReal](lem-charfun-gaussianreal.md)
- [centralMoment_two_mul_gaussianReal](lem-centralmoment-two-mul-gaussianreal.md)

## Gaussian measures on a Banach space

That kind of generality is not needed for this project, but we happen to have results about Gaussian measures on a Banach space in Mathlib, so we will use them. The main reference for this section is (hairer2009introduction).

Let $F$ be a separable Banach space.

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [isGaussian_iff_charFunDual_eq](thm-isgaussian-iff-charfundual-eq.md)

Transformations of Gaussian measures

- [isGaussian_map](lem-isgaussian-map.md)
- [isGaussian_conv](lem-isgaussian-conv.md)

Fernique's theorem

- [exists_integrable_exp_sq_of_map_rotation_eq_self](thm-exists-integrable-exp-sq-of-map-rotation-eq.md)
- [IsGaussian.map_rotation_eq_self](lem-isgaussian-map-rotation-eq-self.md)
- [Fernique's theorem](../../../../../mathlib/thousand-plus/analysis/28-measure-and-integration/ferniques-theorem.md)
- [IsGaussian.memLp_id](lem-isgaussian-memlp-id.md)

A Gaussian measure has finite second moment by Lemma [IsGaussian.memLp_id](lem-isgaussian-memlp-id.md), hence its covariance bilinear form is well defined.

## Gaussian measures on a finite dimensional Hilbert space

We specialize directly from Banach space to finite dimensional Hilbert space since that's what we need in this project, although there are results for Gaussian measures on infinite dimensional Hilbert spaces that would worth stating.

- [isGaussian_iff_charFun_eq](lem-isgaussian-iff-charfun-eq.md)

Let $E$ be a separable Hilbert space. We denote by $\langle \cdot, \cdot \rangle$ the inner product on $E$ and by $\Vert \cdot \Vert$ the associated norm.

- [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md)
- [isGaussian_iff_gaussian_charFun](lem-isgaussian-iff-gaussian-charfun.md)

Note that this lemma does not say that there exists a Gaussian measure for any such $m$ and $C$. We will prove that later.

*The proof of [Lemma isGaussian_iff_gaussian_charFun](lem-isgaussian-iff-gaussian-charfun.md) is shown with its statement.*

- [IsGaussian.ext_iff](lem-isgaussian-ext-iff.md)
- [Standard Gaussian measure](def-stdgaussian.md)

The fact that this definition does not depend on the choice of basis will be a consequence of the fact that its characteristic function does not depend on the basis.

- [integral_eval_pi](lem-integral-eval-pi.md)
- [isCentered_stdGaussian](lem-iscentered-stdgaussian.md)
- [isProbabilityMeasure_stdGaussian](lem-isprobabilitymeasure-stdgaussian.md)
- [charFun_stdGaussian](lem-charfun-stdgaussian.md)
