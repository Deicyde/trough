---
declaration: lemma
origin: cited
lean: ProbabilityTheory.centralMoment_two_mul_gaussianReal
statement: formalized
proof: formalized
---

# centralMoment_two_mul_gaussianReal

The central moment of order $2n$ of a real Gaussian measure $\mathcal{N}(\mu, \sigma^2)$ is given by

$$
\begin{aligned}
\mathbb{E}[(X - \mu)^{2n}] = \sigma^{2n} (2n - 1)!! \: ,
\end{aligned}
$$

in which $(2n - 1)!! = (2n - 1)(2n - 3) \cdots 3 \cdot 1$ is the double factorial of $2n - 1$.

## Depends on

- [Gaussian law](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-law.md)

## Proof

$$
\begin{aligned}
\mathbb{E}[(X - \mu)^{2n}] &= \int_{-\infty}^\infty (x - \mu)^{2n} \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}} \mathrm dx \\
&= \int_{-\infty}^\infty x^{2n} \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{x^2}{2 \sigma^2}} \mathrm dx \\
&= 2 \int_{0}^\infty x^{2n} \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{x^2}{2 \sigma^2}} \mathrm dx \\
&= 2 \int_{0}^\infty {\sqrt{2 \sigma^2 x}}^{2n} \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-x)} \frac{\sigma^2}{\sqrt{2 \sigma^2 x'}} \mathrm dx \\
&= \frac{\sigma^{2n} 2^n}{\sqrt{\pi}} \int_{0}^\infty x^{n - 1/2} e{-x} \mathrm dx \\
&= \frac{\sigma^{2n} 2^n}{\sqrt{\pi}} \Gamma(n + 1/2) \\
&= \frac{\sigma^{2n} 2^n}{\Gamma(1/2)} \left( \prod_{k=0}^{n-1} (k + 1/2) \right) \Gamma(1/2) \\
&= \sigma^{2n} \prod_{k=0}^{n-1} (2k + 1) \\
&= \sigma^{2n} (2n - 1)!!
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.centralMoment_two_mul_gaussianReal`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.centralMoment_two_mul_gaussianReal).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 31](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L31)
