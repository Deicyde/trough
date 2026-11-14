---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.charFun_stdGaussian
---

# charFun_stdGaussian

The characteristic function of the standard Gaussian measure on $E$ is given by

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(-\frac{1}{2} \Vert t \Vert^2 \right) \: .
\end{aligned}
$$

## Depends on

- [Standard Gaussian measure](def-stdgaussian.md)
- [Characteristic function](../../../../../mathlib/overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)

## Proof depends on

- [charFun_gaussianReal](lem-charfun-gaussianreal.md)

## Proof

Denote by $\nu$ the standard Gaussian measure on $\mathbb{R}$. This is a straightforward computation:

$$
\begin{aligned}
\hat{\mu}(t) = \int \exp\left(i\langle t, \sum_{j=1}^d x_j \cdot e_j \rangle\right) d(\nu \times \ldots \times \nu)(dx) &= \int \exp\left(\sum_{j=1}^d ix_j\langle t, e_j \rangle\right) d(\nu \times \ldots \times \nu)(dx) \\
&= \int \prod_{j=1}^d \exp\left(ix_j\langle t, e_j \rangle\right) d(\nu \times \ldots \times \nu)(dx) \\
&= \prod_{j=1}^d \int \exp\left(ix\langle t, e_j \rangle\right) d\nu(x) \\
&= \prod_{j=1}^d \exp\left(-\frac{\langle t, e_j \rangle^2}{2}\right) \\
&= \exp\left(-\frac{1}{2} \Vert t \Vert^2 \right).
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.charFun_stdGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.charFun_stdGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 358](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L358)
