---
declaration: lemma
origin: cited
lean: MIPRE.MIPStar.toComputable, MIPRE.MIPStar.isRE, MIPRE.PolyVerifier.tab, MIPRE.PolyVerifier.tab_computable, MIPRE.PolyVerifier.quantumValue_tab
statement: formalized
proof: formalized
---

# The class is contained in the computable one

Every language in $\mathrm{MIP}^*$ (Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](def-mipstar.md)) is in the computable class of Definition [The computable class](def-mipstar-computable.md), hence recursively enumerable.

## Depends on

- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](def-mipstar.md)
- [The computable class](def-mipstar-computable.md)

## Proof depends on

- [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md)

## Proof

Given $z$, run the sampler on every seed of length $B$ and the decider on every tuple of strings of length at most $B$, each under the budget the efficiency clause supplies; a run within a known budget is decidable, so the table of $\mathfrak{G}_z$ is computable from $z$. It is written as a game description with Alice's questions and Bob's tagged apart (the description format forces unequal answers to equal questions to lose, and $\mathfrak{G}_z$ is a general bipartite game), and the tagged game has the value of $\mathfrak{G}_z$ (`quantumValue_doubled`). In Lean: `PolyVerifier.tab`, `tab_computable` and `quantumValue_tab`. The inclusion in $\mathrm{RE}$ is then Lemma [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md).

## Lean

Formalized as [`MIPRE.MIPStar.toComputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStar.toComputable), [`MIPRE.MIPStar.isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStar.isRE), [`MIPRE.PolyVerifier.tab`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier.tab), [`MIPRE.PolyVerifier.tab_computable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier.tab_computable), [`MIPRE.PolyVerifier.quantumValue_tab`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier.quantumValue_tab).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1656](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1656)
