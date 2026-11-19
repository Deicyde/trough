---
declaration: lemma
origin: cited
lean: MIPRE.Halting.exists_sem_of_tab, MIPRE.Halting.exists_sem_lower, MIPRE.Halting.exists_sem_upper, MIPRE.REPred.or, MIPRE.Verifier.LongAcceptance, MIPRE.Verifier.longAcceptanceB, MIPRE.Verifier.longAcceptanceB_iff, MIPRE.Verifier.not_rejectsLong_iff_exists, MIPRE.Verifier.rePred_not_rejectsLong
statement: formalized
proof: formalized
---

# The semidecider of the halting reduction

Let the family `Vof` of verifiers named by strings be computably presented (Lemma [A violated time bound is enumerable](lem-bounded-violation-re.md)) and let $x, n \mapsto \mathfrak{G}_{x,n}$ be a computable family of game descriptions with $\mathrm{val}^*(\mathfrak{G}_{x, n}) = \mathrm{val}^*(\mathsf{V}^x_n)$ whenever $\mathsf{V}^x$ is $n$-bounded. Then there is a closed program of the cost model halting on $\mathrm{encode}(x, n)$ exactly when $x \notin B_n$: obligation O3 of Remark [Relation to the abstract compression lemma](../README.md).

## Depends on

- [A violated time bound is enumerable](lem-bounded-violation-re.md)
- [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md)
- [Semideciders on encoded values](../../computability/lem-semidecide-encoded.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Gap-preserving compression from ambient stage contracts](thm-compression.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Proof

$x \notin B_n$ is “$\mathsf{V}^x$ is not $n$-bounded, or its decider accepts some answer longer than the answer bound at index $n$, or $\mathrm{val}^*(\mathsf{V}^x_n) > \frac12$” (`Verifier.not_inClassB_iff`). Under the hypothesis on the family the last disjunct may be read on $\mathfrak{G}_{x,n}$ instead, in both directions: if $\mathsf{V}^x$ is $n$-bounded the two values are equal, and if it is not then the first disjunct holds anyway. The first disjunct is recursively enumerable by Lemma [A violated time bound is enumerable](lem-bounded-violation-re.md); the second by the same pattern with a simpler witness — the tuple and a step budget, tested by one budgeted run of the decider (`Verifier.rePred_not_rejectsLong`); the third by the $\mathrm{val}^*$ half of Lemma [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md) along the computable family. A union of recursively enumerable sets is recursively enumerable, by dovetailing. Lemma [Semideciders on encoded values](../../computability/lem-semidecide-encoded.md) turns the result into a program on the encodings of pairs.

## Lean

Formalized as [`MIPRE.Halting.exists_sem_of_tab`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_sem_of_tab), [`MIPRE.Halting.exists_sem_lower`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_sem_lower), [`MIPRE.Halting.exists_sem_upper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_sem_upper), [`MIPRE.REPred.or`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.REPred.or), [`MIPRE.Verifier.LongAcceptance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.LongAcceptance), [`MIPRE.Verifier.longAcceptanceB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.longAcceptanceB), [`MIPRE.Verifier.longAcceptanceB_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.longAcceptanceB_iff), [`MIPRE.Verifier.not_rejectsLong_iff_exists`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.not_rejectsLong_iff_exists), [`MIPRE.Verifier.rePred_not_rejectsLong`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.rePred_not_rejectsLong).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6979](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6979)
