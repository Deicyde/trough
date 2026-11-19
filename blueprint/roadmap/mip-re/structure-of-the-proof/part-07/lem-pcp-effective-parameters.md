---
declaration: lemma
origin: cited
lean: MIPRE.TM.CookLevin.Pad.pcpParamsProg, MIPRE.TM.CookLevin.Pad.pcpParamsProg_apply, MIPRE.TM.CookLevin.Pad.pcpParams_odd, MIPRE.TM.CookLevin.Pad.pcpParams_field_large, MIPRE.TM.CookLevin.Pad.pcpParams_inner_dvd, MIPRE.TM.CookLevin.Pad.pcpParams_outer_dvd, MIPRE.TM.CookLevin.Pad.pcpParams_field_eventually_large, MIPRE.TM.CookLevin.Pad.fieldDegree_le
statement: formalized
proof: formalized
---

# Effective classical PCP parameters

The padded dimensions extend to ambient polynomial-time classical PCP parameters $(k,m,s)$ with $k$ odd, $q=2^k\geq 82m'$, and both $m\mid q$ and $m'\mid q$. The field is moreover eventually larger than every fixed power of $8(Q+1)m'$: for every $e$, once $Q\geq2^e$, $q\geq(8(Q+1)m')^e$, while $k$ stays polylogarithmic in $Qm'$.

## Depends on

- [Effective padded descriptions with an explicit output budget](prop-pcp-padded-describer.md)

## Proof

Choose $k=2(s_0^2+\mathrm{size}(m'))+7$ with $s_0=\mathrm{size}(Q)+\mathrm{size}(m')+3$. Then $q\geq128(2^{\mathrm{size}(m')})^2\geq82m'$. Both dimensions are powers of two at most $q$, hence divide it. Since $8(Q+1)m'<2^{s_0}$, for $s_0\geq e$ we get $(8(Q+1)m')^e<2^{s_0e}\leq2^{s_0^2}\leq q$, and $Q\geq2^e$ gives $s_0>e$; this is the field size answer reduction's low-degree test needs (`FieldLarge`), whose exponent this construction need not know. Compute the degree in unary from the binary lengths of $Q$ and $m'$ and combine it with the already verified $(m,s)$ program.

## Lean

Formalized as [`MIPRE.TM.CookLevin.Pad.pcpParamsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParamsProg), [`MIPRE.TM.CookLevin.Pad.pcpParamsProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParamsProg_apply), [`MIPRE.TM.CookLevin.Pad.pcpParams_odd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParams_odd), [`MIPRE.TM.CookLevin.Pad.pcpParams_field_large`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParams_field_large), [`MIPRE.TM.CookLevin.Pad.pcpParams_inner_dvd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParams_inner_dvd), [`MIPRE.TM.CookLevin.Pad.pcpParams_outer_dvd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParams_outer_dvd), [`MIPRE.TM.CookLevin.Pad.pcpParams_field_eventually_large`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.pcpParams_field_eventually_large), [`MIPRE.TM.CookLevin.Pad.fieldDegree_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.fieldDegree_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4822](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4822)
