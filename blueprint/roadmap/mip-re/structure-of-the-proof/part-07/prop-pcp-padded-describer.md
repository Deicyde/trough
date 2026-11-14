---
declaration: proposition
origin: cited
lean: MIPRE.TM.CookLevin.Pad.formula5_circuit, MIPRE.TM.CookLevin.Pad.describe, MIPRE.TM.CookLevin.Pad.describe_wellFormed, MIPRE.TM.CookLevin.Pad.describe_describes, MIPRE.TM.CookLevin.Pad.innerDim_isPow, MIPRE.TM.CookLevin.Pad.innerDim_le, MIPRE.TM.CookLevin.Pad.two_mul_le_innerDim, MIPRE.SAT.Circuit.padGatesProg, MIPRE.SAT.Circuit.wellFormed_padGates, MIPRE.SAT.Circuit.eval_padGates, MIPRE.TM.CookLevin.Pad.describeExact, MIPRE.TM.CookLevin.Pad.describeExact_wellFormed, MIPRE.TM.CookLevin.Pad.describeExact_describes, MIPRE.TM.CookLevin.Pad.describeExact_gateCount, MIPRE.TM.CookLevin.Pad.describeExact_variables, MIPRE.TM.CookLevin.Pad.outerDim_isPow, MIPRE.TM.CookLevin.Pad.outerDim_polynomial, MIPRE.TM.CookLevin.Pad.innerDim_add_bound_le_gateCount, MIPRE.TM.CookLevin.Pad.paddingParams, MIPRE.TM.CookLevin.Pad.paddingParams_apply
statement: formalized
proof: formalized
---

# Effective padded descriptions with an explicit output budget

There are effectively computed parameters $m(T,\sigma)$ and $s(n,T,Q,\sigma)$, with $m$ a power of two, $m=O(\log T+\log\sigma)$, $2^m\geq 2T$, $s\geq m$, and $5m+5+s$ a power of two polynomially bounded in $\log n+\log T+Q+\sigma$. On a valid specification and a unary budget of length $s$, an ambient polynomial-time program constructs a well-formed circuit with five $m$-bit blocks, five signs, and exactly $s$ gates, describing exactly the same accepting answer prefixes. The parameter program is polynomial-time in the binary parameter lengths.

## Depends on

- [Succinct decoupled 5SAT](lem-decoupled-5sat.md)
- [Padding preserves the complete answer tapes](lem-pcp-padding-semantics.md)
- [Effective indexing and padding arithmetic](lem-pcp-padding-programs.md)

## Proof

Implement the padded clause predicate by a renamed formula and comparisons with the original block bounds. Round the common width up to a power of two. From the circuit program's proved output bound $s_1$, set $m'=2^{\lceil\log_2(6m+5+s_1)\rceil}$ and $s=m'-5m-5$. Append copying OR gates to reach exactly $s$ gates; this preserves the last-gate output convention and fan-out two. The unary budget prevents an invalid short input from demanding exponentially many output gates. In the PCP verifier the formatted view will supply this budget; connecting that caller remains part of Theorem [The bespoke PCP for deciders](thm-pcp-decider.md).

## Lean

Formalized as [`MIPRE.TM.CookLevin.Pad.formula5_circuit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.formula5_circuit), [`MIPRE.TM.CookLevin.Pad.describe`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describe), [`MIPRE.TM.CookLevin.Pad.describe_wellFormed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describe_wellFormed), [`MIPRE.TM.CookLevin.Pad.describe_describes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describe_describes), [`MIPRE.TM.CookLevin.Pad.innerDim_isPow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.innerDim_isPow), [`MIPRE.TM.CookLevin.Pad.innerDim_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.innerDim_le), [`MIPRE.TM.CookLevin.Pad.two_mul_le_innerDim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.two_mul_le_innerDim), [`MIPRE.SAT.Circuit.padGatesProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.padGatesProg), [`MIPRE.SAT.Circuit.wellFormed_padGates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.wellFormed_padGates), [`MIPRE.SAT.Circuit.eval_padGates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_padGates), [`MIPRE.TM.CookLevin.Pad.describeExact`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describeExact), [`MIPRE.TM.CookLevin.Pad.describeExact_wellFormed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describeExact_wellFormed), [`MIPRE.TM.CookLevin.Pad.describeExact_describes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describeExact_describes), [`MIPRE.TM.CookLevin.Pad.describeExact_gateCount`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describeExact_gateCount), [`MIPRE.TM.CookLevin.Pad.describeExact_variables`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.describeExact_variables), [`MIPRE.TM.CookLevin.Pad.outerDim_isPow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.outerDim_isPow), [`MIPRE.TM.CookLevin.Pad.outerDim_polynomial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.outerDim_polynomial), [`MIPRE.TM.CookLevin.Pad.innerDim_add_bound_le_gateCount`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.innerDim_add_bound_le_gateCount), [`MIPRE.TM.CookLevin.Pad.paddingParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.paddingParams), [`MIPRE.TM.CookLevin.Pad.paddingParams_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.paddingParams_apply).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4782](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4782)
