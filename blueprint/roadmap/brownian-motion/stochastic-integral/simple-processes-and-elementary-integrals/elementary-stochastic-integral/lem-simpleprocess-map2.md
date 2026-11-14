---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.map₂
statement: formalized
proof: formalized
---

# simpleProcess_map2

For $V, W$ two simple processes with values in $E$ and $F$ respectively, the process defined by $B(V, W)_t(\omega) = B(V_t(\omega), W_t(\omega))$ is a simple process.

Note: in Lean, the above is not a lemma but a definition of a simple process with a lemma that its coercion to a function is given by above.

## Depends on

- [Elementary stochastic integral](def-elemstochintegralbilin.md)
- [Simple process](../simple-processes-and-elementary-predictable-sets/def-simpleprocess.md)

## Proof

It has values $B(\eta_i, \xi_j)$ on the intervals $(s_i, t_i] \cap (u_j, v_j]$ if $V$ and $W$ are defined by the sequences $(s_i, t_i, \eta_i)$ and $(u_j, v_j, \xi_j)$ respectively.

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.map₂`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.map₂).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 383](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L383)
