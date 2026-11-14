---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TMIPStar, MIPRE.Tailored.TPolyVerifier, MIPRE.Tailored.TPolyVerifier.toPoly, MIPRE.Tailored.TPolyVerifier.tgame, MIPRE.Tailored.TPolyVerifier.Efficient
statement: formalized
---

# The class $\mathrm{TMIP}^*$; II:787, II:1505

A language $L \subseteq \{0,1\}^*$ is in $\mathrm{TMIP}^*$ if there are three machines, a sampler, an answer-length calculator and a linear-constraints processor, and a polynomial $P$, such that for every string $z$, writing $B = P(\left\vert {z} \right\vert)$:

1. *Efficiency.* The sampler is as in Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md): on $z$ and a uniform seed $r \in \{0,1\}^B$ it halts within time $P(\left\vert {z} \right\vert + \left\vert {r} \right\vert)$ with a pair of strings of length at most $B$; write $\mu_z$ for their distribution. On $(z, x, \kappa)$ the calculator, and on $(z, x, y, a^R, b^R)$ the processor, halt within time $P$ of the total input length. The tailored game $\mathfrak{G}_z$ has the strings of length at most $B$ as its questions, the distribution $\mu_z$, the lengths the calculator outputs and the constraints the processor outputs, read as for a tailored normal form verifier (Definition [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)).
2. *Completeness.* If $z \in L$, the doubled game of $\mathfrak{G}_z$ has a perfect ZPC strategy.
3. *Soundness.* If $z \notin L$, then $\mathrm{val}^*(\mathfrak{G}_z) \leq \frac12$.

## Depends on

- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md)
- [Tailored game; II:1243](../part-01/def-tailored-game.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](../part-01/def-zpc-strategy.md)
- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.TMIPStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStar), [`MIPRE.Tailored.TPolyVerifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier), [`MIPRE.Tailored.TPolyVerifier.toPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.toPoly), [`MIPRE.Tailored.TPolyVerifier.tgame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.tgame), [`MIPRE.Tailored.TPolyVerifier.Efficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.Efficient).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 936](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L936)
