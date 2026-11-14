---
declaration: corollary
origin: cited
lean: MIPRE.Halting.halting_reduction_quantum_of, MIPRE.Halting.gameValue_uncomputable_of, MIPRE.Halting.quantumValue_uncomputable_of, MIPRE.Halting.re_subset_mipstarComputable_of, MIPRE.Halting.mipstarComputable_eq_re_of
statement: formalized
proof: formalized
---

# The consequences of Chapter The main theorem, from compression

Assume an ambient `MIPRE.GapCompression`. On the map of Theorem [Halting reduction](thm-halting.md), the quantum value of the game is also $1$ when the machine halts on the empty input and at most $\tfrac12$ when it does not. Consequently no computable function separates game descriptions of value $1$ from those of value at most $\tfrac12$, for the synchronous value or for the quantum value; every recursively enumerable language is in $\mathrm{MIP}^*$; and $\mathrm{MIP}^* = \mathrm{RE}$.

## Depends on

- [Halting reduction](thm-halting.md)
- [Turing](../../background-results/part-03/thm-halting-undecidable.md)
- [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [The computable class](../../foundations/part-03/def-mipstar-computable.md)
- [Recursively enumerable](../../foundations/part-02/def-re.md)

## Proof

The tabulation of Theorem [Halting reduction](thm-halting.md) gives both values at once (`halting_reduction_both_of`): at a halting machine the tabulated game has a value-$1$ PCC strategy, and at a non-halting one its quantum value is at most $\tfrac12$. A separating function composed with the map would decide halting, against Theorem [Turing](../../background-results/part-03/thm-halting-undecidable.md). An r.e. language reduces to the halting problem by a computable map, which composes with the quantum-value reduction; the converse inclusion is Lemma [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md). These are the conditional forms of the results of Chapter [The main theorem](../../the-main-theorem/README.md), which Corollary [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](cor-compression-from-answer-reduction.md) instantiates.

## Lean

Formalized as [`MIPRE.Halting.halting_reduction_quantum_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_quantum_of), [`MIPRE.Halting.gameValue_uncomputable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.gameValue_uncomputable_of), [`MIPRE.Halting.quantumValue_uncomputable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.quantumValue_uncomputable_of), [`MIPRE.Halting.re_subset_mipstarComputable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.re_subset_mipstarComputable_of), [`MIPRE.Halting.mipstarComputable_eq_re_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipstarComputable_eq_re_of).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7427](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7427)
