---
declaration: lemma
origin: cited
lean: MIPRE.SAT.Circuit.trivial, MIPRE.SAT.Circuit.wellFormed_trivial, MIPRE.SAT.Circuit.padTo, MIPRE.SAT.Circuit.padTo_inputs, MIPRE.SAT.Circuit.padTo_size, MIPRE.SAT.Circuit.wellFormed_padTo, MIPRE.SAT.Circuit.padTo_of_le, MIPRE.SAT.Circuit.evalBits_padTo, MIPRE.SAT.Circuit.formula6_padTo, MIPRE.SAT.Circuit.describesWindows_padTo, MIPRE.SAT.Circuit.trivialProg, MIPRE.SAT.Circuit.trivialProg_apply, MIPRE.SAT.Circuit.padToProg, MIPRE.SAT.Circuit.padToProg_apply
statement: formalized
proof: formalized
---

# Padding a circuit to an exact gate count

A well-formed circuit with at most $s$ gates, $s \geq 1$, padded with copies of its output gate is a well-formed circuit with exactly $s$ gates, the same inputs and the same function, so it describes the same formula and the same decider through three windows; a larger one is replaced by a constant circuit padded to $s$ gates. The padding is computed in polynomial time.

## Depends on

- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)
- [Effective padded descriptions with an explicit output budget](../../structure-of-the-proof/part-07/prop-pcp-padded-describer.md)

## Proof

Each copying gate reads the previous output twice, so fan-out stays at most two and the new output is terminal.

## Lean

Formalized as [`MIPRE.SAT.Circuit.trivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.trivial), [`MIPRE.SAT.Circuit.wellFormed_trivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.wellFormed_trivial), [`MIPRE.SAT.Circuit.padTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padTo), [`MIPRE.SAT.Circuit.padTo_inputs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padTo_inputs), [`MIPRE.SAT.Circuit.padTo_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padTo_size), [`MIPRE.SAT.Circuit.wellFormed_padTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.wellFormed_padTo), [`MIPRE.SAT.Circuit.padTo_of_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padTo_of_le), [`MIPRE.SAT.Circuit.evalBits_padTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.evalBits_padTo), [`MIPRE.SAT.Circuit.formula6_padTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.formula6_padTo), [`MIPRE.SAT.Circuit.describesWindows_padTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.describesWindows_padTo), [`MIPRE.SAT.Circuit.trivialProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.trivialProg), [`MIPRE.SAT.Circuit.trivialProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.trivialProg_apply), [`MIPRE.SAT.Circuit.padToProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padToProg), [`MIPRE.SAT.Circuit.padToProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padToProg_apply).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 4050](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L4050)
