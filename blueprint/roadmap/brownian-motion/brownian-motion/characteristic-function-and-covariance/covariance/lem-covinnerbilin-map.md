---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.covarianceBilin_map
---

# covInnerBilin_map

Let $E$ and $F$ be two Hilbert spaces with $F$ finite dimensional, $\mu$ a finite measure on $E$ with finite second moment, and $L : E \to F$ a continuous linear map. Then the covariance bilinear form of the measure $L_*\mu$ is given by

$$
\begin{aligned}
C'_{L_*\mu}(u, v)
&= C'_\mu(L^\dagger(u), L^\dagger(v))
\: ,
\end{aligned}
$$

in which $L^\dagger : F \to E$ is the adjoint of $L$.

## Depends on

- [Covariance in a Hilbert space](def-covinnerbilin.md)

## Proof

$$
\begin{aligned}
C'_{L_*\mu}(u, v)
&= (L_*\mu)\left[\langle u, x - m_{L_*\mu}\rangle \langle x - m_{L_*\mu}, v \rangle\right]
\\
&= \mu\left[\langle u, L(x) - L(m_\mu)\rangle \langle L(x) - L(m_\mu), v \rangle \right]
\\
&= \mu\left[\langle L^\dagger(u), x - m_\mu\rangle \langle x - m_\mu, L^\dagger(v) \rangle \right]
\\
&= C'_\mu(L^\dagger(u), L^\dagger(v))
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.covarianceBilin_map`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covarianceBilin_map).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 125](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L125)
