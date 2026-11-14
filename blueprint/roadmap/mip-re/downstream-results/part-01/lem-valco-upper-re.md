---
declaration: lemma
origin: cited
lean: MIPRE.commutingUpperRE, MIPRE.Tsirelson.Coded.CheckUpper, MIPRE.Tsirelson.Coded.primrecRel_checkUpper, MIPRE.Tsirelson.checkUpper_iff
statement: formalized
proof: formalized
---

# Upper semidecision of the commuting-operator value

Write $\mathfrak{G}_g$ for the game described by a game description $g$ (Definition [Game description](../../foundations/part-02/def-game-description.md)). The set

$$
\{ (g, p, q) : g \text{ a game description},\ p, q \in \mathbb{N},\ {\omega^{\mathrm{co}}}(\mathfrak{G}_g) < p/q \}
$$

is recursively enumerable, with $p/0 = 0$.

## Depends on

- [Game description](../../foundations/part-02/def-game-description.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Exact sum-of-squares certificates](lem-sos-certificates.md)
- [Upper semidecision of the commuting-operator value](def-commuting-upper-re.md)

## Proof depends on

- [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md)

## Proof

The certificates of Lemma [Exact sum-of-squares certificates](lem-sos-certificates.md) at $\kappa = q\, W_g$, where $W_g$ is the total weight of $g$, have integer data: $\kappa(p/q \cdot 1 - W_{\mathfrak{G}_g}) = p W_g \cdot 1 - q \sum \mathrm{wt}(x,y)[D]\, e_{xa} f_{yb}$. The checker computes $T + T^*$ on lists of monomials with coded Gaussian-integer coefficients, merges equal words, tests dominance, and rejects $q = 0$ and malformed letters or relation indices; it is primitive recursive, and a certificate passes exactly when ${\omega^{\mathrm{co}}}(\mathfrak{G}_g) < p/q$. Enumerating certificates gives the semidecider.

## Lean

Formalized as [`MIPRE.commutingUpperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingUpperRE), [`MIPRE.Tsirelson.Coded.CheckUpper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.Coded.CheckUpper), [`MIPRE.Tsirelson.Coded.primrecRel_checkUpper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.Coded.primrecRel_checkUpper), [`MIPRE.Tsirelson.checkUpper_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.checkUpper_iff).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 299](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L299)
