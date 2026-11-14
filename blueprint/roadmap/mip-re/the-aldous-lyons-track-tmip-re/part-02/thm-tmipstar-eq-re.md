---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.TMIPStarComputable.mipStar, MIPRE.Tailored.TMIPStarComputable.isRE, MIPRE.Tailored.re_subset_tmipStarComputable_of, MIPRE.Tailored.tmipStarComputable_eq_re_of
statement: formalized
proof: formalized
---

# $\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997

$\mathrm{TMIP}^* \subseteq \mathrm{MIP}^* \subseteq \mathrm{RE}$. Given a tailored gap compression, $\mathrm{TMIP}^* = \mathrm{RE}$.

## Depends on

- [The computable class $\mathrm{TMIP}^*$; II:787](def-tmipstar.md)
- [Recursively enumerable](../../foundations/part-02/def-re.md)
- [A tailored game description as a game description](lem-tailored-conversion.md)
- [The computable class](../../foundations/part-03/def-mipstar-computable.md)
- [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md)
- [Halting from tailored compression; II:1887–2066](thm-tailored-halting.md)

## Proof depends on

- [Turing](../../background-results/part-03/thm-halting-undecidable.md)

## Proof

A perfect ZPC strategy gives quantum value $1$ (Lemma [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)), and the conversion to a game description keeps the quantum value (Lemma [A tailored game description as a game description](lem-tailored-conversion.md)); so a language in $\mathrm{TMIP}^*$ is in the computable class of Definition [The computable class](../../foundations/part-03/def-mipstar-computable.md), which is contained in $\mathrm{RE}$ (Lemma [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md)). The plan had this inclusion by enumerating signed-permutation strategies; the route through the quantum value needs no new semidecider. Conversely, an r.e. language many-one reduces to the halting problem, which reduces to tailored games by Theorem [Halting from tailored compression; II:1887–2066](thm-tailored-halting.md).

## Lean

Formalized as [`MIPRE.Tailored.TMIPStarComputable.mipStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStarComputable.mipStar), [`MIPRE.Tailored.TMIPStarComputable.isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TMIPStarComputable.isRE), [`MIPRE.Tailored.re_subset_tmipStarComputable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.re_subset_tmipStarComputable_of), [`MIPRE.Tailored.tmipStarComputable_eq_re_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tmipStarComputable_eq_re_of).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 910](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L910)
