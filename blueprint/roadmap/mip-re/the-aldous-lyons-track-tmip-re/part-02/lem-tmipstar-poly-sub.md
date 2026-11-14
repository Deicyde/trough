---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TMIPStar.toComputable, MIPRE.Tailored.TMIPStar.isRE, MIPRE.Tailored.TPolyVerifier.tabP, MIPRE.Tailored.TPolyVerifier.computable_tabP, MIPRE.Tailored.TPolyVerifier.presents_tabP
statement: formalized
proof: formalized
---

# The class is contained in the computable one

Every language in $\mathrm{TMIP}^*$ is in the computable class of Definition [The computable class $\mathrm{TMIP}^*$; II:787](def-tmipstar.md); in particular it is recursively enumerable.

## Depends on

- [The class $\mathrm{TMIP}^*$; II:787, II:1505](def-tmipstar-poly.md)
- [The computable class $\mathrm{TMIP}^*$; II:787](def-tmipstar.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997](thm-tmipstar-eq-re.md)
- [A presentation of a game without weight on its loops](lem-tailored-presents.md)
- [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)
- [The class is contained in the computable one](../../foundations/part-03/lem-mipstar-poly-sub.md)

## Proof

On the input $z$, tabulate the doubled game of $\mathfrak{G}_z$: its vertices are the doubled strings of length at most $B$, its weights those of the tabulation of Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md)'s game (Lemma [The class is contained in the computable one](../../foundations/part-03/lem-mipstar-poly-sub.md)), and its lengths and constraints what the calculator and the processor output within the time bound $P$, as in Lemma [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md). The table is a computable function of $z$, and on an efficient input it presents the doubled game of $\mathfrak{G}_z$, which has no weight on its loops; so it has a perfect ZPC strategy when the doubled game does, and the doubled game's quantum value, which is $\mathfrak{G}_z$'s (Lemma [A presentation of a game without weight on its loops](lem-tailored-presents.md)). So $L$ is in the computable class, and in $\mathrm{RE}$ by Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997](thm-tmipstar-eq-re.md).

## Lean

Formalized as [`MIPRE.Tailored.TMIPStar.toComputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStar.toComputable), [`MIPRE.Tailored.TMIPStar.isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStar.isRE), [`MIPRE.Tailored.TPolyVerifier.tabP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.tabP), [`MIPRE.Tailored.TPolyVerifier.computable_tabP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.computable_tabP), [`MIPRE.Tailored.TPolyVerifier.presents_tabP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TPolyVerifier.presents_tabP).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 974](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L974)
