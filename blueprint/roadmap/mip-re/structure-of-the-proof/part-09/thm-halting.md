---
declaration: theorem
origin: cited
lean: MIPRE.Halting.halting_reduction, MIPRE.Halting.halting_reduction_of, MIPRE.Halting.halting_reduction_lower, MIPRE.Halting.halting_reduction_lower_strings, MIPRE.Halting.halting_reduction_lower_of, MIPRE.Halting.exists_obligations, MIPRE.Halting.halting_reduces_to_gameValue_of, MIPRE.Halting.halting_reduction_both_of, MIPRE.Halting.halting_paper, MIPRE.Halting.halting_paper_valStar, MIPRE.Halting.Vpaper, MIPRE.Halting.semL, MIPRE.Halting.hasPerfectPCC_of_halts, MIPRE.Halting.valStar_le_of_not_halts, MIPRE.Halting.classV, MIPRE.Halting.classV_efficient, MIPRE.Halting.classV_value, MIPRE.Halting.classV_values, MIPRE.Halting.sampProg, MIPRE.Halting.decProg, MIPRE.Halting.sampProg_runs, MIPRE.Halting.decProg_accepts, MIPRE.Halting.decProg_runs, MIPRE.GapCompression.samplerFamily
statement: formalized
proof: formalized
---

# Halting reduction

Assume an ambient `MIPRE.GapCompression`. There is a computable map $\mathcal{M} \mapsto \mathfrak{G}_{\mathcal{M}}$ from Turing machines to explicit synchronous game descriptions (Definition [Game description](../../foundations/part-02/def-game-description.md)), such that:

1. if $\mathcal{M}$ halts on the empty input then $\mathfrak{G}_\mathcal{M}$ has a value-$1$ PCC strategy, so ${\mathrm{val}^{s}}(\mathfrak{G}_\mathcal{M}) = \mathrm{val}^*(\mathfrak{G}_\mathcal{M}) = 1$;
2. if $\mathcal{M}$ does not halt on the empty input then $\mathrm{val}^*(\mathfrak{G}_\mathcal{M}) \leq \tfrac12$, and hence also ${\mathrm{val}^{s}}(\mathfrak{G}_\mathcal{M}) \leq \tfrac12$ (Lemma [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)).

Moreover the reduction is polynomial-time: for every polynomial-time map $z \mapsto \mathcal{M}_z$ from strings to machines there is a polynomial-time verifier in the sense of Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md), efficient on every input, whose game on $z$ has a value-$1$ PCC strategy if $\mathcal{M}_z$ halts on the empty input and quantum value at most $\tfrac12$ if it does not.

## Depends on

- [Gap-preserving compression from ambient stage contracts](thm-compression.md)
- [Compressibility criterion](../../computability/lem-compressible-criterion.md)
- [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md)
- [Efficient Kleene recursion theorem](../../computability/lem-kleene.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)
- [Values of the halting verifier](lem-dhalt-values.md)
- [The parameter of the halting verifier](lem-lambda.md)
- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)
- [The class verifiers' sampler](lem-class-sampler.md)

## Proof depends on

- [The semidecider of the halting reduction](lem-halting-semidecider.md)
- [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md)

## Proof

`MIPRE.Halting.halting_reduction_of` in $\mathrm{val}^*$ and `halting_reduces_to_gameValue_of` in ${\mathrm{val}^{s}}$, from Theorem [Gap-preserving compression from ambient stage contracts](thm-compression.md) as a `GapCompression`: Lemma [Compressibility criterion](../../computability/lem-compressible-criterion.md) at the classes of Remark [Relation to the abstract compression lemma](../README.md), whose four obligations are the theorems named below, the last through `exists_obligations`. This proves computability of the explicit tabulation. It does not assert polynomial-time enumeration of that table.

## Lean

Formalized as [`MIPRE.Halting.halting_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction), [`MIPRE.Halting.halting_reduction_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_of), [`MIPRE.Halting.halting_reduction_lower`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_lower), [`MIPRE.Halting.halting_reduction_lower_strings`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_lower_strings), [`MIPRE.Halting.halting_reduction_lower_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_lower_of), [`MIPRE.Halting.exists_obligations`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_obligations), [`MIPRE.Halting.halting_reduces_to_gameValue_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduces_to_gameValue_of), [`MIPRE.Halting.halting_reduction_both_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_both_of), [`MIPRE.Halting.halting_paper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_paper), [`MIPRE.Halting.halting_paper_valStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_paper_valStar), [`MIPRE.Halting.Vpaper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.Vpaper), [`MIPRE.Halting.semL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.semL), [`MIPRE.Halting.hasPerfectPCC_of_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.hasPerfectPCC_of_halts), [`MIPRE.Halting.valStar_le_of_not_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.valStar_le_of_not_halts), [`MIPRE.Halting.classV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classV), [`MIPRE.Halting.classV_efficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classV_efficient), [`MIPRE.Halting.classV_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classV_value), [`MIPRE.Halting.classV_values`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classV_values), [`MIPRE.Halting.sampProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.sampProg), [`MIPRE.Halting.decProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.decProg), [`MIPRE.Halting.sampProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.sampProg_runs), [`MIPRE.Halting.decProg_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.decProg_accepts), [`MIPRE.Halting.decProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.decProg_runs), [`MIPRE.GapCompression.samplerFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.samplerFamily).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7378](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7378)
