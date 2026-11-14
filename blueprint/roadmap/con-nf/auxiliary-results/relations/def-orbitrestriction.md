---
declaration: definition
origin: cited
lean: Rel.OrbitRestriction
statement: formalized
---

# OrbitRestriction

Let $s : \operatorname{\mathsf{Set}} \tau$. An *orbit restriction* for $s$ (over some type $\sigma$) consists of a set $t : \operatorname{\mathsf{Set}} \tau$ disjoint from $s$, a function $f : \tau \to \sigma$, and a permutation $\pi : \sigma \simeq \sigma$, such that for each $u : \sigma$, the set $t \cap f^{-1}(u)$ has cardinality at least $\max(\aleph_0, \#s, \#d)$.

An orbit restriction encapsulates information about how orbits should be completed.

- $t$ is the *sandbox*, the set inside which all added items must reside.
- $f$ is a *categorisation function*, placing each value $x : \tau$ into a category $u : \sigma$.
- $\pi$ is a permutation of categories. If $x$ has category $u$, then anything that $x$ is mapped to should have category $\pi(u)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Rel.OrbitRestriction`](https://leanprover-community.github.io/con-nf/doc/find/#doc/Rel.OrbitRestriction).

## Sources

- [Consistency of New Foundations blueprint: chapters/auxiliary.tex, line 44](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L44)
