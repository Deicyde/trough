---
declaration: lemma
origin: cited
lean: MIPRE.TM.CookLevin.Pad.esize_bitBlocks_le, MIPRE.TM.CookLevin.Pad.esize_view_le, MIPRE.TM.CookLevin.Pad.pcpInput_size_polynomial, MIPRE.TM.CookLevin.Pad.pcpProgram_time_le
statement: formalized
proof: formalized
---

# Encoded PCP view size and source runtime

Valid formatted PCP inputs for the constructed parameters have encoded size polynomial in $L=\log n+\log T+Q+\sigma$. Consequently every ambient polynomial-time program on these inputs has runtime polynomial in $L$.

## Depends on

- [Effective classical PCP parameters](lem-pcp-effective-parameters.md)
- [Effective padded descriptions with an explicit output budget](prop-pcp-padded-describer.md)

## Proof

A list of $r$ field blocks of width $k$ has encoded size at most $(4k+2)r+1$. The two view lists therefore have total size at most $(4k+2)(2m'+6)+3$. The padded outer dimension is polynomial in $L$, and $k=2\mathrm{size}(m')+7\leq 2m'+7$. Add the valid specification's size bound and compose the resulting polynomial with the program's ambient time bound.

## Lean

Formalized as [`MIPRE.TM.CookLevin.Pad.esize_bitBlocks_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.esize_bitBlocks_le), [`MIPRE.TM.CookLevin.Pad.esize_view_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.esize_view_le), [`MIPRE.TM.CookLevin.Pad.pcpInput_size_polynomial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpInput_size_polynomial), [`MIPRE.TM.CookLevin.Pad.pcpProgram_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpProgram_time_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4941](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4941)
