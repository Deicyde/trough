---
declaration: lemma
origin: cited
lean: MIPRE.SAT.cubeIndexEquiv, MIPRE.SAT.clauseInput5_injective, MIPRE.SAT.PcpParams.clauseInput5_pointClause, MIPRE.SAT.PcpParams.pointClause_pointFromClause, MIPRE.SAT.PcpParams.degreeOf_circuitArith, MIPRE.SAT.PcpParams.eval_circuitArith_bool, MIPRE.SAT.PcpParams.eval_iff_exists_circuitArith, MIPRE.SAT.PcpParams.exists_proof_of_formula5_sat, MIPRE.SAT.PcpParams.formula5_sat_of_majority, MIPRE.SAT.PcpParams.completeness_of_describes, MIPRE.SAT.PcpParams.soundness_of_describes
statement: formalized
proof: formalized
---

# PCP semantics for a circuit describer

For a well-formed circuit with $5m+5$ inputs and exactly $m'$ input and gate variables, the typed algebraic PCP is complete and majority-sound for the actual five-block formula. If the circuit describes a decider, completeness uses its accepted answer prefixes, and soundness recovers accepted prefixes and both entire decoded answer tapes.

## Depends on

- [Circuit arithmetization with bounded input use](lem-pcp-circuit-arithmetization.md)
- [PCP answer blocks, honest proof and decoded clauses](lem-pcp-proof-algebra.md)
- [Effective padded descriptions with an explicit output budget](prop-pcp-padded-describer.md)

## Proof

Identify little-endian indices with Boolean cube points by an explicit bijection. The circuit's input order is exactly the five PCP blocks followed by their signs, with inverse encodings preserving every literal. Transport the finite circuit polynomial to the advertised PCP dimension. Its Boolean witnesses correspond to precisely the circuit's clauses. Apply the honest-proof construction and majority decoding, then the describer's exact accepting-tape relation. These are typed algebraic tests; the raw verifier program is a separate obligation.

## Lean

Formalized as [`MIPRE.SAT.cubeIndexEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.cubeIndexEquiv), [`MIPRE.SAT.clauseInput5_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.clauseInput5_injective), [`MIPRE.SAT.PcpParams.clauseInput5_pointClause`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.clauseInput5_pointClause), [`MIPRE.SAT.PcpParams.pointClause_pointFromClause`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.pointClause_pointFromClause), [`MIPRE.SAT.PcpParams.degreeOf_circuitArith`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.degreeOf_circuitArith), [`MIPRE.SAT.PcpParams.eval_circuitArith_bool`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.eval_circuitArith_bool), [`MIPRE.SAT.PcpParams.eval_iff_exists_circuitArith`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.eval_iff_exists_circuitArith), [`MIPRE.SAT.PcpParams.exists_proof_of_formula5_sat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.exists_proof_of_formula5_sat), [`MIPRE.SAT.PcpParams.formula5_sat_of_majority`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.formula5_sat_of_majority), [`MIPRE.SAT.PcpParams.completeness_of_describes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.completeness_of_describes), [`MIPRE.SAT.PcpParams.soundness_of_describes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams.soundness_of_describes).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4910](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4910)
