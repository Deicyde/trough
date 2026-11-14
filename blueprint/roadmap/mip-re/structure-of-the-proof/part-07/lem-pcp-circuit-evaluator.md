---
declaration: lemma
origin: cited
lean: MIPRE.SAT.PolyTimeFun.casesGate, MIPRE.SAT.Circuit.lastInputValueProg, MIPRE.SAT.Circuit.lastInputValue_range, MIPRE.SAT.Circuit.gateBitsProg, MIPRE.SAT.Circuit.evalBits_gateBits, MIPRE.SAT.Circuit.circuitBitsProg, MIPRE.SAT.Circuit.circuitBitsProg_apply, MIPRE.SAT.Circuit.length_circuitBits, MIPRE.SAT.Circuit.evalBits_circuitBits, MIPRE.SAT.Circuit.evalBits_circuitBits_finite, MIPRE.SAT.shoupBinField_charP, MIPRE.SAT.shoupBinField_toBits_ofBits
statement: formalized
proof: formalized
---

# Effective circuit polynomial evaluation

There is an ambient polynomial-time evaluator for the routed circuit polynomial on binary coefficient vectors, uniform in the supplied monic binary modulus. Over a characteristic-two field containing a root of that modulus, correctly sized inputs evaluate to the circuit polynomial at the corresponding field point, including its restriction to the exact finite set of input and gate coordinates.

## Depends on

- [Circuit arithmetization with bounded input use](lem-pcp-circuit-arithmetization.md)
- [Effective indexing and padding arithmetic](lem-pcp-padding-programs.md)

## Proof

Dispatch the five gate constructors, scan preceding input copies, and use the verified coefficient-vector addition and modular multiplication programs. Multiply the consistency factors and output coordinate directly. The scan stores only the supplied coordinates and preceding gate/value pairs; the accumulator width never grows, even on malformed inputs. Its ambient cost therefore has a global polynomial bound. Induction over the gate prefix identifies its accumulator with the product of the polynomial factors. The Shoup field uses the same quotient carrier and canonical coefficient representation after recording its exact degree. This proves circuit evaluation; assembling the PCP verifier and its prescribed runtime bound remains part of Theorem [The bespoke PCP for deciders](thm-pcp-decider.md).

## Lean

Formalized as [`MIPRE.SAT.PolyTimeFun.casesGate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PolyTimeFun.casesGate), [`MIPRE.SAT.Circuit.lastInputValueProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.lastInputValueProg), [`MIPRE.SAT.Circuit.lastInputValue_range`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.lastInputValue_range), [`MIPRE.SAT.Circuit.gateBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.gateBitsProg), [`MIPRE.SAT.Circuit.evalBits_gateBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.evalBits_gateBits), [`MIPRE.SAT.Circuit.circuitBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.circuitBitsProg), [`MIPRE.SAT.Circuit.circuitBitsProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.circuitBitsProg_apply), [`MIPRE.SAT.Circuit.length_circuitBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.length_circuitBits), [`MIPRE.SAT.Circuit.evalBits_circuitBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.evalBits_circuitBits), [`MIPRE.SAT.Circuit.evalBits_circuitBits_finite`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.evalBits_circuitBits_finite), [`MIPRE.SAT.shoupBinField_charP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupBinField_charP), [`MIPRE.SAT.shoupBinField_toBits_ofBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupBinField_toBits_ofBits).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4879](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4879)
