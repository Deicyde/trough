---
declaration: corollary
origin: cited
lean: MIPRE.GapCompression.ofAnswerReduction, MIPRE.Halting.halting_reduces_to_gameValue_of_answerReduction, MIPRE.Halting.halting_reduction_quantum_of_answerReduction, MIPRE.Halting.gameValue_uncomputable_of_answerReduction, MIPRE.Halting.quantumValue_uncomputable_of_answerReduction, MIPRE.Halting.re_subset_mipstarComputable_of_answerReduction, MIPRE.Halting.mipstarComputable_eq_re_of_answerReduction
statement: formalized
proof: formalized
---

# Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone

From an inhabitant of `MIPRE.AnswerReduction 5` alone there is a `MIPRE.GapCompression`, and consequently Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](../../the-main-theorem/thm-main.md), Corollary [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md), Corollary [Uncomputability of the game value](../../the-main-theorem/cor-value-uncomputable.md) and Theorem [$\mathrm{MIP}^* = \mathrm{RE}$](../../the-main-theorem/thm-mipstar-eq-re.md) hold with no other hypothesis.

## Depends on

- [Gap-preserving compression from ambient stage contracts](thm-compression.md)
- [Supplying ambient introspection](../part-06/lem-introspection-supply.md)
- [Parallel repetition of normal form verifiers](thm-parallel-repetition.md)
- [Efficient universal Turing machine](../../computability/lem-universal-tm.md)

## Proof depends on

- [The consequences of Chapter The main theorem, from compression](cor-halting-consequences.md)

## Proof

Theorem [Gap-preserving compression from ambient stage contracts](thm-compression.md) applied to the introspection instance of Lemma [Supplying ambient introspection](../part-06/lem-introspection-supply.md), the given answer reduction, and the repetition construction of Theorem [Parallel repetition of normal form verifiers](thm-parallel-repetition.md); the universal machine is the one of Lemma [Efficient universal Turing machine](../../computability/lem-universal-tm.md). The chapter 7 results are then their conditional forms at this compression.

## Lean

Formalized as [`MIPRE.GapCompression.ofAnswerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.ofAnswerReduction), [`MIPRE.Halting.halting_reduces_to_gameValue_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduces_to_gameValue_of_answerReduction), [`MIPRE.Halting.halting_reduction_quantum_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_quantum_of_answerReduction), [`MIPRE.Halting.gameValue_uncomputable_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.gameValue_uncomputable_of_answerReduction), [`MIPRE.Halting.quantumValue_uncomputable_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.quantumValue_uncomputable_of_answerReduction), [`MIPRE.Halting.re_subset_mipstarComputable_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.re_subset_mipstarComputable_of_answerReduction), [`MIPRE.Halting.mipstarComputable_eq_re_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipstarComputable_eq_re_of_answerReduction).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6404](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6404)
