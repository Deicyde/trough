---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.tailored_halting_reduction_of, MIPRE.Tailored.tailored_halting_reduction_quantum_of, MIPRE.Tailored.Halting.halting_tailored_search, MIPRE.Tailored.Halting.lamThreshold, MIPRE.Tailored.Halting.VT, MIPRE.Tailored.Halting.toData_F_code, MIPRE.Tailored.Halting.lpBuild, MIPRE.Tailored.Halting.lamOf, MIPRE.Tailored.Halting.descM, MIPRE.Tailored.Halting.gameOf, MIPRE.Tailored.Halting.presents_gameOf, MIPRE.Tailored.Halting.hasPerfectZPC_gameOf, MIPRE.Tailored.Halting.quantumValue_gameOf, MIPRE.Tailored.Halting.quantumValue_gameOf_le, MIPRE.Tailored.Halting.computable_gameOf
statement: formalized
proof: formalized
---

# Halting from tailored compression; II:1887–2066

A tailored gap compression gives the proposition of Definition [The tailored halting reduction, as a proposition](../part-01/def-tailored-halting-reduction.md), the statement of Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](../part-01/thm-tmip-re.md), with the soundness clause even in the quantum value $\mathrm{val}^*$, which bounds the synchronous value.

## Depends on

- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)
- [The tailored halting reduction, as a proposition](../part-01/def-tailored-halting-reduction.md)
- [The tailored halting theorem at a fixed level; II:2021–2066](thm-tailored-halting-level.md)
- [The search program](lem-tailored-search.md)
- [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)
- [A presentation of a game without weight on its loops](lem-tailored-presents.md)
- [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)

## Proof

The reduction sends $\mathcal{M}$ to the tabulation, at the level $C$, of the tailored halting verifier $\mathsf{V}^{\mathcal{M},\lambda}$ with the search program of Lemma [The search program](lem-tailored-search.md) and $\lambda = \Lambda_0 + 4\left\vert {\mathcal{M}} \right\vert$. That verifier is $\lambda$-bounded (Lemma [$\lambda$ for the tailored halting verifier; II:2002](lem-tailored-lambda.md)), so its tabulation presents the doubled game at $C$ (Lemma [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)). If $\mathcal{M}$ halts, the verifier has a perfect ZPC strategy at $C$ (Theorem [The tailored halting theorem at a fixed level; II:2021–2066](thm-tailored-halting-level.md)), which, padded, is one of the tabulation; if not, its value at $C$ is at most $\frac12$, and that is the tabulation's quantum value (Lemma [A presentation of a game without weight on its loops](lem-tailored-presents.md)), which bounds the synchronous value (Lemma [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)). The map is computable: the processor's description is a fixed tree around the encodings of $\mathcal{M}$ and $\lambda$, built as the decider's is for Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md), and the tabulation is computable.

## Lean

Formalized as [`MIPRE.Tailored.tailored_halting_reduction_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailored_halting_reduction_of), [`MIPRE.Tailored.tailored_halting_reduction_quantum_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tailored_halting_reduction_quantum_of), [`MIPRE.Tailored.Halting.halting_tailored_search`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.halting_tailored_search), [`MIPRE.Tailored.Halting.lamThreshold`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lamThreshold), [`MIPRE.Tailored.Halting.VT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.VT), [`MIPRE.Tailored.Halting.toData_F_code`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.toData_F_code), [`MIPRE.Tailored.Halting.lpBuild`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lpBuild), [`MIPRE.Tailored.Halting.lamOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lamOf), [`MIPRE.Tailored.Halting.descM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.descM), [`MIPRE.Tailored.Halting.gameOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.gameOf), [`MIPRE.Tailored.Halting.presents_gameOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.presents_gameOf), [`MIPRE.Tailored.Halting.hasPerfectZPC_gameOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.hasPerfectZPC_gameOf), [`MIPRE.Tailored.Halting.quantumValue_gameOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.quantumValue_gameOf), [`MIPRE.Tailored.Halting.quantumValue_gameOf_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.quantumValue_gameOf_le), [`MIPRE.Tailored.Halting.computable_gameOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.computable_gameOf).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 863](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L863)
