---
declaration: lemma
origin: cited
lean: exists_locallyFinite_subcover_of_locally
statement: formalized
proof: formalized
---

# exists_locally_finite_subcover_of_locally

Let $X$ be a metrizable locally compact second countable topological space. Let $C$ be a closed subset in $X$. Let $P$ be a non-decreasing predicate on subsets of $X$ (meaning that if $U ⊂ V$ and $V$ satisfies $P$ then so does $U$). Assume the empty set satisfies $P$ and every point in $C$ has a neighborhood in $X$ satisfying $P$. Then there exist sequences of subsets $K$ and $W$ indexed by natural numbers such that $K$ covers $C$, $W$ is locally finite and, for every $n$ :

- $K_n$ is compact
- $W_n$ is open
- $K_n ⊂ W_n$
- $W_n$ satisfies $P$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is a classical result.

## Lean

Formalized as [`exists_locallyFinite_subcover_of_locally`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/exists_locallyFinite_subcover_of_locally).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 267](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L267)
