---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.isGaussian_iff_gaussian_charFun, ProbabilityTheory.gaussian_charFun_congr
---

# isGaussian_iff_gaussian_charFun

A finite measure $\mu$ on $E$ is Gaussian if and only if there exists $m \in E$ and $C$ positive semidefinite such that for all $t \in E$, the characteristic function of $\mu$ at $t$ is

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(i \langle t, m \rangle - \frac{1}{2} C(t, t)\right) \: ,
\end{aligned}
$$

If that's the case, then $m = m_\mu$ and $C = C'_\mu$.

## Depends on

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [Characteristic function](../../../../../mathlib/overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Covariance matrix](../../../characteristic-function-and-covariance/covariance/def-covmatrix.md)

## Proof depends on

- [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md)
- [charFun_map_eq_charFunDual_smul](../../../characteristic-function-and-covariance/characteristic-functions/lem-charfun-map-eq-charfundual-smul.md)
- [ext_of_charFun](../../../characteristic-function-and-covariance/characteristic-functions/thm-ext-of-charfun.md)

## Proof

Lemma [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md) states that the characteristic function of a Gaussian measure has the wanted form.

Suppose now that there exists $m \in E$ and $C$ positive semidefinite such that for all $t \in E$, $\hat{\mu}(t) = \exp\left(i \langle t, m \rangle - \frac{1}{2} C(t, t)\right)$.

We need to show that for all $L \in E^*$, $L_*\mu$ is a Gaussian measure on $\mathbb{R}$. Such an $L$ can be written as $\langle u, \cdot \rangle$ for some $u \in E$. Let then $u \in E$. We compute the characteristic function of $\langle u, \cdot\rangle_*\mu$ at $x \in \mathbb{R}$ with Lemma [charFun_map_eq_charFunDual_smul](../../../characteristic-function-and-covariance/characteristic-functions/lem-charfun-map-eq-charfundual-smul.md):

$$
\begin{aligned}
\widehat{\langle u, \cdot\rangle_*\mu}(x)
&= \hat{\mu}(x \cdot u)
\\
&= \exp\left(i x \langle u, m \rangle - \frac{1}{2} x^2 C(u, u)\right)
\: .
\end{aligned}
$$

This is the characteristic function of a Gaussian measure on $\mathbb{R}$ with mean $\langle u, m \rangle$ and variance $C(u, u)$. By Theorem [ext_of_charFun](../../../characteristic-function-and-covariance/characteristic-functions/thm-ext-of-charfun.md), $\langle u, \cdot\rangle_*\mu$ is Gaussian, hence $\mu$ is Gaussian.

By Lemma [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md), we deduce that for any $t \in E$ we have

$$
\exp\left(i\langle t, m \rangle - \frac{1}{2} C(t, t)\right) = \exp\left(i\langle t, m_\mu \rangle - \frac{1}{2} C'_\mu(t, t)\right).
$$

In particular, for any $t$ there exists $n_t \in \mathbb{Z}$ such that

$$
i\langle t, m \rangle - \frac{1}{2} C(t, t) = i\langle t, m_\mu \rangle - \frac{1}{2} C'_\mu(t, t) + 2i\pi n_t.
$$

We deduce that $n$ is a continuous map from $E$ to $\mathbb{Z}$, and thus must be constant because $E$ is connected. By looking at the value at $t = 0$, we deduce that for any $t$, $n_t = 0$. Looking at real and imaginary parts we obtain that for any $t$,

$$
\langle t, m \rangle = \langle t, m_\mu \rangle \quad \text{and} \quad C(t, t) = C'_\mu(t, t).
$$

We immediately deduce that $m = m_\mu$. Moreover, because $C$ and $C'_\mu$ are symmetric, they are characterized by their values on the diagonal. Indeed, for any $x, y$,

$$
C(x, y) = \frac{1}{2} (C(x + y, x + y) - C(x, x) - C(y, y)).
$$

We deduce that $C = C'_\mu$.

## Lean

Formalized as [`ProbabilityTheory.isGaussian_iff_gaussian_charFun`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussian_iff_gaussian_charFun), [`ProbabilityTheory.gaussian_charFun_congr`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.gaussian_charFun_congr).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 245](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L245)
