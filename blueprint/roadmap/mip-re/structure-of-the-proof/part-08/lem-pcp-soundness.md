---
declaration: lemma
origin: cited
lean: MIPRE.TM.CookLevin.Pad.classicalPcp_soundness
statement: formalized
proof: formalized
---

# PCP soundness

If ${{\mathsf{M}}^{\mathsf{ar}}}$ accepts with probability greater than $\tfrac12$ on views of a fixed proof whose answer and certificate polynomials all have individual degree at most seven, then the decider accepts the answers the first two polynomials decode to. The entire decoded answer vectors equal the padded tape encodings of the accepted prefixes.

## Depends on

- [The PCP's proof format and query structure](lem-pcp-format.md)
- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)

## Proof

Zero-testing of the constraint polynomial against a zero basis, with Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md) bounding the probability that a nonzero polynomial vanishes on a random point. The stated error bounds are what the composition consumes, so a formalization should carry them rather than an asymptotic form.

## Lean

Formalized as [`MIPRE.TM.CookLevin.Pad.classicalPcp_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.classicalPcp_soundness).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5203](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5203)
