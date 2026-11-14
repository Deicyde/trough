---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isKolmogorovProcess_preBrownian
statement: formalized
proof: formalized
---

# isKolmogorovProcess_preBrownian

The pre-Brownian process $X$ of Definition [pre-Brownian process](def-prebrownian.md) satisfies the Kolmogorov condition for exponents $(2n,n)$ with constant $(2n - 1)!!$ for all $n \in \mathbb{N}$. That is, for all $s, t \in \mathbb{R}_+$, we have

$$
\begin{aligned}
\mathbb{E} \left[ |X_t - X_s|^{2n} \right] \le (2n - 1)!! |t - s|^n
\: .
\end{aligned}
$$

## Depends on

- [pre-Brownian process](def-prebrownian.md)

## Proof depends on

- [centralMoment_two_mul_gaussianReal](../../gaussian-distributions/gaussian-measures/part-01/lem-centralmoment-two-mul-gaussianreal.md)
- [hasLaw_preBrownian_sub](lem-haslaw-prebrownian-sub.md)

## Proof

$X_t - X_s$ is a Gaussian random variable with mean $0$ and variance $|t - s|$ (Lemma [hasLaw_preBrownian_sub](lem-haslaw-prebrownian-sub.md)). Thus, by Lemma [centralMoment_two_mul_gaussianReal](../../gaussian-distributions/gaussian-measures/part-01/lem-centralmoment-two-mul-gaussianreal.md), we have

$$
\begin{aligned}
\mathbb{E} \left[ |X_t - X_s|^{2n} \right]
= (2n - 1)!! |t - s|^n
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.isKolmogorovProcess_preBrownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isKolmogorovProcess_preBrownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 53](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L53)
