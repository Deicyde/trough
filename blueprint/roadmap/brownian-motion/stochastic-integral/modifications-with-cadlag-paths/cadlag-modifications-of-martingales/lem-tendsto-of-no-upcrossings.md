---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: tendsto_of_no_upcrossings
---

# tendsto_of_no_upcrossings

Let $u : \beta \to \alpha$, for $\alpha$ a densely ordered, conditionally complete linear order equipped with the order topology. Let $S$ be a dense subset of $\alpha$ and $f$ a filter of $\beta$. If for all $a < b$ in $S$, the number of upcrossings of the interval $[a, b]$ by $u$ along $f$ is finite, then $u$ tends to a limit along $f$.

## Depends on

- [Upcrossings](def-upcrossings.md)

## Lean

Formalized as [`tendsto_of_no_upcrossings`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/tendsto_of_no_upcrossings).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 117](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L117)
