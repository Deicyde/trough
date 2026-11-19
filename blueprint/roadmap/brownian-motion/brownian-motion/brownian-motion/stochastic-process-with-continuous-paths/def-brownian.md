---
declaration: definition
origin: cited
lean: ProbabilityTheory.brownian
statement: formalized
---

# Brownian motion

By Theorem [localized_holder_modification_sup](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/thm-localized-holder-modification-sup.md), there exists a modification $B$ of the pre-Brownian process such that all the paths of $B$ are Hölder continuous of all orders $\gamma \in (0, 1/2)$. We call $B$ the *Brownian motion* on $\mathbb{R}_+$.

## Depends on

- [localized_holder_modification_sup](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/thm-localized-holder-modification-sup.md)
- [pre-Brownian process](def-prebrownian.md)
- [isKolmogorovProcess_preBrownian](lem-iskolmogorovprocess-prebrownian.md)
- [hasBoundedCoveringNumberCover_nnreal](../../kolmogorov-chentsov-theorem/kolmogorov-chentsov-theorem/lem-hasboundedcoveringnumbercover-nnreal.md)

## Lean

Formalized as [`ProbabilityTheory.brownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.brownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 77](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L77)
