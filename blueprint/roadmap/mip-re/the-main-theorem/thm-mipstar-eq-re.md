---
declaration: theorem
origin: cited
lean: MIPRE.Halting.mipstarComputable_eq_re, MIPRE.Halting.re_subset_mipstarComputable, MIPRE.Halting.mipstar_eq_re, MIPRE.Halting.re_subset_mipstar, MIPRE.Halting.re_subset_mipclass_of_reduction, MIPRE.Halting.mipclass_eq_re_of_reduction
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^* = \mathrm{RE}$

$\mathrm{MIP}^* = \mathrm{RE}$, for the class $\mathrm{MIP}^*_{1,1/2}(2,1)$ of Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../foundations/part-03/def-mipstar.md) and for the computable class of Definition [The computable class](../foundations/part-03/def-mipstar-computable.md).

## Depends on

- [The computable class](../foundations/part-03/def-mipstar-computable.md)
- [Recursively enumerable](../foundations/part-02/def-re.md)
- [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md)
- [Turing](../background-results/part-03/thm-halting-undecidable.md)
- [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md)
- [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](lem-mipstar-sub-re.md)
- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../foundations/part-03/def-mipstar.md)
- [The class is contained in the computable one](../foundations/part-03/lem-mipstar-poly-sub.md)

## Proof depends on

- [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](../structure-of-the-proof/part-09/cor-compression-from-answer-reduction.md)
- [Answer reduction](../structure-of-the-proof/part-09/thm-answer-reduction.md)

## Proof

For $\mathrm{RE} \subseteq \mathrm{MIP}^*$: the halting problem is $\mathrm{RE}$-complete (Theorem [Turing](../background-results/part-03/thm-halting-undecidable.md)) and Theorem [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md) provides a computable map to explicit games, whose completeness–soundness gap is already in the form the computable class of Definition [The computable class](../foundations/part-03/def-mipstar-computable.md) requires (Corollary [Halting reduces to the quantum value](cor-main-quantum.md)); no transport between the two values is needed. $\mathrm{MIP}^* \subseteq \mathrm{RE}$ is Lemma [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](lem-mipstar-sub-re.md). In Lean the many-one reduction of an r.e. language to halting on the empty input is `MIPRE.IsRE.exists_code_halts`, from Mathlib's `Nat.Partrec.Code.curry`, for the computable class of Definition [The computable class](../foundations/part-03/def-mipstar-computable.md) (`MIPRE.Halting.mipstarComputable_eq_re`); the equality holds at the compression of Theorem [Ambient compression inhabitation target](../structure-of-the-proof/part-09/thm-compression-target.md), as Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](thm-main.md) does.

For the class of Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../foundations/part-03/def-mipstar.md), `MIPRE.Halting.mipstar_eq_re`: $\mathrm{MIP}^* \subseteq \mathrm{RE}$ is Lemma [The class is contained in the computable one](../foundations/part-03/lem-mipstar-poly-sub.md), and $\mathrm{RE} \subseteq \mathrm{MIP}^*$ (`re_subset_mipstar`) is the polynomial-time form of Theorem [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md). An r.e. language many-one reduces to halting on the empty input by a polynomial-time map $z \mapsto \mathcal{M}_z$ (`Cost.exists_polyTime_reduction`: the semidecider with $z$ hardcoded), and the class verifier of Theorem [Halting reduction](../structure-of-the-proof/part-09/thm-halting.md) on input $z$ plays the game of $\mathsf{V}^{\mathsf{halt}}_{\mathcal{M}_z, \lambda(\mathcal{M}_z)}$ at the fixed level $C$, whose value is $1$ if $\mathcal{M}_z$ halts and at most $\frac12$ if not.

## Lean

Formalized as [`MIPRE.Halting.mipstarComputable_eq_re`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipstarComputable_eq_re), [`MIPRE.Halting.re_subset_mipstarComputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.re_subset_mipstarComputable), [`MIPRE.Halting.mipstar_eq_re`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipstar_eq_re), [`MIPRE.Halting.re_subset_mipstar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.re_subset_mipstar), [`MIPRE.Halting.re_subset_mipclass_of_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.re_subset_mipclass_of_reduction), [`MIPRE.Halting.mipclass_eq_re_of_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipclass_eq_re_of_reduction).

## Sources

- [MIP* = RE blueprint: content/07_main_theorem.tex, line 183](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/07_main_theorem.tex#L183)
