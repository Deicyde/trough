---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.pv, MIPRE.Tailored.AnsRed.Typed.pvR, MIPRE.Tailored.AnsRed.Typed.oc, MIPRE.Tailored.AnsRed.Typed.pvO, MIPRE.Tailored.AnsRed.Typed.evalR, MIPRE.Tailored.AnsRed.Typed.restr, MIPRE.Tailored.AnsRed.Typed.selR, MIPRE.Tailored.AnsRed.Typed.arPred_of_arDt, MIPRE.Tailored.AnsRed.Typed.pvR_eq_pvO_of_arDt, MIPRE.Tailored.AnsRed.Typed.pvO_eq_pvR_of_arDt, MIPRE.Tailored.AnsRed.Typed.sum_dis_edge_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_MA_GB_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_MB_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_GB_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_le
statement: formalized
proof: formalized
---

# The point relations

Write $\mathrm{ev}_w$ for evaluation at the point the registers $w$ carry, and $\mathrm{res}_r$ for the restriction of the oracle's tuple to the slots of an isolated role $r$. Summed over the seeds:

1. at one pair of types, if the typed data's acceptance forces two readings of the two answers to agree, their disagreement is at most $81 |Z| |W| \theta$; the consistency check at the point questions of an isolated role and the oracle forces the role's point values to be the oracle's in the role's slots;
2. $\mathrm{ev}_w G^\textsc{B}_r$ disagrees with Alice's point values at most $|Z| |W| \delta_r(9\theta)$, $\mathrm{ev}_w G^\textsc{A}_r$ with Bob's likewise, and $G^\textsc{A}_r$ with $G^\textsc{B}_r$ at most $|Z| \delta_r(9\theta)$;
3. for an isolated role $r$, $\mathrm{ev}_w G^\textsc{A}_r$ disagrees with $\mathrm{ev}_w \mathrm{res}_r G^\textsc{B}_\textsc{O}$ at most $11 |Z| |W| (\delta_r(9\theta) + 81 \theta + \delta_\textsc{O}(9\theta))$, and the same with the players exchanged.

## Depends on

- [The polynomial measurements](lem-ar-sound-extract.md)
- [The per-role failures](../part-06/lem-ar-sound-roles.md)
- [Reading the answer-reduced constraints](../part-06/lem-ar-tailored-reading.md)

## Proof depends on

- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)

## Proof

The first part reads the typed data's acceptance (Lemma [Reading the answer-reduced constraints](../part-06/lem-ar-tailored-reading.md)): two readings that acceptance forces to agree disagree at most as often as the strategy fails there, and Lemma [The per-role failures](../part-06/lem-ar-sound-roles.md) sums the failures. The second is Lemma [The polynomial measurements](lem-ar-sound-extract.md), the test's uniform point being read off the registers of a uniform vector. The third chains the second part at the role, the consistency check and the second part at the oracle, through Bob's point answer of the role and Alice's point answer of the oracle at the same seed, by the triangle inequality for disagreements across the two players, which costs a factor $11$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.pv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pv), [`MIPRE.Tailored.AnsRed.Typed.pvR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pvR), [`MIPRE.Tailored.AnsRed.Typed.oc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.oc), [`MIPRE.Tailored.AnsRed.Typed.pvO`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pvO), [`MIPRE.Tailored.AnsRed.Typed.evalR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.evalR), [`MIPRE.Tailored.AnsRed.Typed.restr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.restr), [`MIPRE.Tailored.AnsRed.Typed.selR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.selR), [`MIPRE.Tailored.AnsRed.Typed.arPred_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arPred_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.pvR_eq_pvO_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pvR_eq_pvO_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.pvO_eq_pvR_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pvO_eq_pvR_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_edge_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_edge_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_MA_GB_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_MA_GB_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_MB_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_MB_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_GB_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GA_GB_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3208](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3208)
