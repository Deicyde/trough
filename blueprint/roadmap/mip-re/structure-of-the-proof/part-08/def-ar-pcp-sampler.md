---
declaration: definition
origin: cited
lean: MIPRE.LIDT.CL.Regs, MIPRE.LIDT.CL.Regs.pres, MIPRE.LIDT.CL.Regs.pres_exactlyOn, MIPRE.LIDT.CL.Sel, MIPRE.LIDT.CL.Sel.canonical, MIPRE.LIDT.CL.Sel.exists_perm, MIPRE.LIDT.CL.Sel.ofSelector, MIPRE.LIDT.CL.Regs.questionOf_eval, MIPRE.LIDT.CL.Regs.sum_sampleOf, MIPRE.CL.sum_comp_injective, MIPRE.AnswerReduction.Pcp.Coord, MIPRE.AnswerReduction.Pcp.Coord.card_coord, MIPRE.AnswerReduction.Pcp.regs, MIPRE.AnswerReduction.Pcp.regs6, MIPRE.AnswerReduction.Pcp.block_ptOf_regs6, MIPRE.AnswerReduction.Pcp.pres, MIPRE.AnswerReduction.Pcp.pres_exactlyOn, MIPRE.AnswerReduction.Pcp.question_eval
statement: formalized
---

# The PCP sampler of answer reduction

For PCP parameters $(q,m,d,m',s)$, the typed PCP sampler has the eighteen types $\mathrm{Point}_i,\mathrm{ALine}_i,\mathrm{DLine}_i$, $i=1,\ldots,6$, on the space

$$
V^{\mathrm{pcp}}=\bigoplus_{i\leq5}\bigl(V_{i,\mathrm{pt}}\oplus V_{i,\mathrm{coord}}\oplus
V_{i,\mathrm{dir}}\bigr)\oplus V_{\mathrm{aux},\mathrm{pt}}\oplus V_{6,\mathrm{coord}}\oplus
V_{\mathrm{aux},\mathrm{dir}}
$$

over $\mathbb{F}_q$, of dimension $10m+2s+16$. Copy $i\leq5$ is the seeded CL test of Definition [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md) in $m$ variables on its own point, coordinate and direction registers. Copy $6$ is the test in $m'=5m+5+s$ variables whose point and direction registers are the concatenations of the five copies' registers with the auxiliary ones. Each type is presented as a three-level CL function (seed, then direction, then the point register), exact on the whole space. Its full evaluation is the seeded question of its copy, and a uniform vector carries a uniform sample of each copy. The $i$-th block of copy $6$'s point, in the block order of the PCP, is copy $i$'s point: this overlap is what the consistency tests compare.

The block of the seed register a direction is drawn from is read off the seed by a selector $\chi:\mathbb{F}_q\to[m]$. The test's own selector numbers the field by an enumeration no program computes, so the presentation takes any selector with blocks of size $q/m$ (the effective one reads the seed's high bits), together with a permutation of the seeds carrying it to the test's; the permutation is used only in the analysis, where a uniform seed stays uniform under it.

## Depends on

- [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)
- [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md)
- [Structure of a CL function](../part-01/lem-cl-structure.md)

## Lean

Formalized as [`MIPRE.LIDT.CL.Regs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Regs), [`MIPRE.LIDT.CL.Regs.pres`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Regs.pres), [`MIPRE.LIDT.CL.Regs.pres_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Regs.pres_exactlyOn), [`MIPRE.LIDT.CL.Sel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sel), [`MIPRE.LIDT.CL.Sel.canonical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sel.canonical), [`MIPRE.LIDT.CL.Sel.exists_perm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sel.exists_perm), [`MIPRE.LIDT.CL.Sel.ofSelector`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sel.ofSelector), [`MIPRE.LIDT.CL.Regs.questionOf_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Regs.questionOf_eval), [`MIPRE.LIDT.CL.Regs.sum_sampleOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Regs.sum_sampleOf), [`MIPRE.CL.sum_comp_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.sum_comp_injective), [`MIPRE.AnswerReduction.Pcp.Coord`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.Coord), [`MIPRE.AnswerReduction.Pcp.Coord.card_coord`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.Coord.card_coord), [`MIPRE.AnswerReduction.Pcp.regs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.regs), [`MIPRE.AnswerReduction.Pcp.regs6`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.regs6), [`MIPRE.AnswerReduction.Pcp.block_ptOf_regs6`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.block_ptOf_regs6), [`MIPRE.AnswerReduction.Pcp.pres`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.pres), [`MIPRE.AnswerReduction.Pcp.pres_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.pres_exactlyOn), [`MIPRE.AnswerReduction.Pcp.question_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Pcp.question_eval).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5416](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5416)
