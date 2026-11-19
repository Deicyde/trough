---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TMIPStarComputable
statement: formalized
---

# The computable class $\mathrm{TMIP}^*$; II:787

A language $L \subseteq \{0,1\}^*$ is in the computable class $\mathrm{TMIP}^*$ if there is a computable map $g$ from bit strings to tailored game descriptions such that for every string $z$: if $z \in L$, then $g(z)$ has a perfect ZPC strategy; if $z \notin L$, then $\mathrm{val}^*(g(z)) \leq \frac12$. As for Definition [The computable class](../../foundations/part-03/def-mipstar-computable.md), there is no polynomial-time bound on $g$.

## Depends on

- [Tailored game descriptions, standalone; II:1243, II:1279](../part-01/def-tailored-game-data.md)
- [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Lean

Formalized as [`MIPRE.Tailored.TMIPStarComputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStarComputable).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 898](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L898)
