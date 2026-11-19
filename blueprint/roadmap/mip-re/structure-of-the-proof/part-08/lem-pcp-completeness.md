---
declaration: lemma
origin: cited
lean: MIPRE.TM.CookLevin.Pad.classicalPcp_completeness
statement: formalized
proof: formalized
---

# PCP completeness

If $\left\vert {a} \right\vert,\left\vert {b} \right\vert\leq T$ and the decider accepts $(n, x, y, a, b)$ within $T$ steps, then the honestly generated proof $\Pi$ — the low-degree encodings of the actual answers, with the auxiliary polynomials computed from them — makes ${{\mathsf{M}}^{\mathsf{ar}}}$ accept with certainty.

## Depends on

- [The PCP's proof format and query structure](lem-pcp-format.md)

## Proof

Combine the padded describer's accepting witness, the degree-seven zero certificate, and the equivalence of raw and typed tests.

## Lean

Formalized as [`MIPRE.TM.CookLevin.Pad.classicalPcp_completeness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.classicalPcp_completeness).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5184](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5184)
