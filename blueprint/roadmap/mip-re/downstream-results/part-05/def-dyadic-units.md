---
declaration: definition
origin: cited
lean: MIPRE.IsMatUnits, MIPRE.HasDyadicUnits
statement: formalized
---

# Unital dyadic matrix units

Let $A$ be a ring with an involution and $\iota$ a finite set. A family $(e_{ij})_{i, j \in \iota}$ of elements of $A$ is a system of *unital matrix units* if $e_{ij} e_{lm} = \delta_{jl}\, e_{im}$, $e_{ij}^* = e_{ji}$ and $\sum_i e_{ii} = 1$. The ring $A$ has *unital dyadic matrix units* if for every $n$ it has a system of unital matrix units indexed by $\{0, 1\}^n$, of size $2^n \times 2^n$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.IsMatUnits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits), [`MIPRE.HasDyadicUnits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HasDyadicUnits).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2853](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2853)
