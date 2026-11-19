---
declaration: definition
origin: cited
lean: IsCoverWithBoundedCoveringNumber
statement: formalized
---

# Cover with bounded covering numbers

A set $T$ is said to have a cover with bounded covering numbers if there exists a monotone sequence of totally bounded subsets $(T_n)_{n \in \mathbb{N}}$ of $T$ such that for all $n$, $T_n$ has bounded internal covering number with constant $c_n$ and exponent $d_n > 0$, and such that $T \subseteq \bigcup_{n \in \mathbb{N}} T_n$.

## Depends on

- [Bounded internal covering number](../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Lean

Formalized as [`IsCoverWithBoundedCoveringNumber`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCoverWithBoundedCoveringNumber).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1778](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1778)
