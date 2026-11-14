---
declaration: lemma
origin: cited
lean: ProbabilityTheory.memHolder_brownian
statement: formalized
proof: formalized
---

# isHolderWith_brownian

The paths of the Brownian motion are locally Hölder continuous of all orders $\gamma \in (0, 1/2)$.

## Depends on

- [Brownian motion](def-brownian.md)

## Proof depends on

- [hasBoundedCoveringNumberCover_nnreal](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/lem-hasboundedcoveringnumbercover-nnreal.md)
- [isKolmogorovProcess_preBrownian](lem-iskolmogorovprocess-prebrownian.md)
- [localized_holder_modification_sup](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/thm-localized-holder-modification-sup.md)

## Proof

Consider the cover of $\mathbb{R}_+$ given by $T_n := [0, n + 1)$. By Lemma [hasBoundedCoveringNumberCover_nnreal](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/lem-hasboundedcoveringnumbercover-nnreal.md), this cover has bounded covering numbers with exponent $1$. Moreover, by Lemma [isKolmogorovProcess_preBrownian](lem-iskolmogorovprocess-prebrownian.md), the pre-Brownian process satisfies the Kolmogorov condition with exponents $(2n + 4, n + 2)$ for all $n \in \mathbb{N}$. In particular, for all $n \in \mathbb{N}$, $2n + 4 > 1$. Applying Theorem [localized_holder_modification_sup](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/thm-localized-holder-modification-sup.md) we deduce that the modification used in Definition [Brownian motion](def-brownian.md) has locally Hölder continuous paths for all orders $\gamma \in (0, \sup_n (n + 1) / (2n + 4))$. Clearly for all $n \in \mathbb{N}$ we have $(n + 1) / (2n + 4) \leqslant 2$, and this quantity tends to $2$ as $n$ goes to infinity. Therefore the Brownian motion has Hölder continuous paths of order $\gamma$ for all $\gamma \in (0, 1 / 2)$.

## Lean

Formalized as [`ProbabilityTheory.memHolder_brownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.memHolder_brownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 101](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L101)
