---
declaration: lemma
origin: cited
lean: ProbabilityTheory.covMatrix_map
statement: formalized
proof: formalized
---

# covMatrix_map

Let $E$ and $F$ be two finite dimensional inner product spaces, $\mu$ a measure on $E$ with finite second moment, and $L : E \to F$ a continuous linear map. Then the covariance matrix of the measure $L_*\mu$ has entries

$$
\begin{aligned}
\langle e_i, \Sigma_{L_*\mu} e_j\rangle
&= \langle L^\dagger(e_i), \Sigma_\mu L^\dagger(e_j)\rangle
\: ,
\end{aligned}
$$

in which $L^\dagger : F \to E$ is the adjoint of $L$.

## Depends on

- [Covariance matrix](def-covmatrix.md)

## Proof depends on

- [covInnerBilin_map](lem-covinnerbilin-map.md)

## Proof

On the left-hand side we have

$$
\langle e_i, \Sigma_{L_*\mu} e_j\rangle = C'_{L_*\mu}(e_i, e_j) = C'_\mu(L^\dagger(e_i), L^\dagger(e_j)),
$$

where the last equality comes from Lemma [covInnerBilin_map](lem-covinnerbilin-map.md). On the right-hand side we have

$$
\langle L^\dagger(e_i), \Sigma_{L_*\mu} L^\dagger(e_j)\rangle = C'_\mu(L^\dagger(e_i), L^\dagger(e_j)),
$$

which concludes the proof.

## Lean

Formalized as [`ProbabilityTheory.covMatrix_map`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covMatrix_map).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 166](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L166)
