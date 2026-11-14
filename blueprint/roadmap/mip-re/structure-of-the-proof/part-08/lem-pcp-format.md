---
declaration: lemma
origin: cited
lean: MIPRE.SAT.PcpProof, MIPRE.SAT.PcpProof.ev, MIPRE.SAT.PcpProof.rawView, MIPRE.SAT.ViewFormat, MIPRE.SAT.viewFormat_rawView
statement: formalized
proof: formalized
---

# The PCP's proof format and query structure

The proof $\Pi$ that ${{\mathsf{M}}^{\mathsf{ar}}}$ reads is well defined: it consists of the low-degree encodings $g_1, g_2$ of the two padded answer prefixes, together with the auxiliary polynomials the zero-test needs, in the stated input formats; and ${{\mathsf{M}}^{\mathsf{ar}}}$'s queries and decision rule are determined by them.

## Depends on

- [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md)
- [Succinct decoupled 5SAT](../part-07/lem-decoupled-5sat.md)

## Proof

A proof is five $m$-variate and $m'+1$ $m'$-variate polynomials of individual degree at most $d$ (`PcpProof`); the verifier reads, at a point $z$, the five answer polynomials on their blocks and the constraint polynomials (`PcpProof.ev`), as $k$-bit blocks (`PcpProof.rawView`), and an honest view is well formatted (`viewFormat_rawView`).

## Lean

Formalized as [`MIPRE.SAT.PcpProof`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpProof), [`MIPRE.SAT.PcpProof.ev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpProof.ev), [`MIPRE.SAT.PcpProof.rawView`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpProof.rawView), [`MIPRE.SAT.ViewFormat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ViewFormat), [`MIPRE.SAT.viewFormat_rawView`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.viewFormat_rawView).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5160](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5160)
