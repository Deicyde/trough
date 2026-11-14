---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Halting.quantumValue_tabT, MIPRE.Tailored.Halting.exists_searchProg, MIPRE.Tailored.Halting.search, MIPRE.Tailored.Halting.search_wellScoped, MIPRE.Tailored.Halting.search_spec
statement: formalized
proof: formalized
---

# The search program

There is a program meeting the search specification (Definition [The search program's specification](def-tailored-search-spec.md)).

## Depends on

- [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)
- [A presentation of a game without weight on its loops](lem-tailored-presents.md)
- [A tailored game description as a game description](lem-tailored-conversion.md)
- [The search program's specification](def-tailored-search-spec.md)
- [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md)

## Proof

On a string, semidecide $\mathrm{val}^* > \frac12$ for the game description of its tabulation at the level $C$. On the description of a $\lambda$-bounded verifier that tabulation presents the doubled game at $C \geq 2$ (Lemma [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)), so it has the doubled game's quantum value, which is the verifier's value (Lemma [A presentation of a game without weight on its loops](lem-tailored-presents.md)), and the conversion keeps it (Lemma [A tailored game description as a game description](lem-tailored-conversion.md)).

## Lean

Formalized as [`MIPRE.Tailored.Halting.quantumValue_tabT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.quantumValue_tabT), [`MIPRE.Tailored.Halting.exists_searchProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.exists_searchProg), [`MIPRE.Tailored.Halting.search`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.search), [`MIPRE.Tailored.Halting.search_wellScoped`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.search_wellScoped), [`MIPRE.Tailored.Halting.search_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.search_spec).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 842](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L842)
