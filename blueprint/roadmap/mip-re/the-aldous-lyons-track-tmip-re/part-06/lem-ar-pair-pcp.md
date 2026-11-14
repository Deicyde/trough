---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.slot_pairPcp_readable, MIPRE.Tailored.AnsRed.slot_pairPcp_affine, MIPRE.Tailored.AnsRed.slot_pairPcp_alice, MIPRE.Tailored.AnsRed.slot_pairPcp_bob, MIPRE.Tailored.AnsRed.indDeg_pairPcp, MIPRE.Tailored.AnsRed.accepts_halts, MIPRE.Tailored.AnsRed.identities_pairPcp, MIPRE.Tailored.AnsRed.HonestHyp.identities
statement: formalized
proof: formalized
---

# The honest PCP of an answer pair

A readable polynomial of the honest PCP depends only on the readable answers; a linear one is, the readable answers fixed, $\mathbb{F}_2$-affine in the linear answers. Alice's polynomials depend only on her question and answer, when that answer carries its readable part and the part fits the table, and Bob's only on his; so they are the oracle's in the same slots. The PCP has individual degree at most $17$, and under the hypotheses of Definition [The honest answers](def-ar-honest-answers.md) the PCP of an answer pair the input game accepts satisfies the thirteen checks identically.

## Depends on

- [The honest answers](def-ar-honest-answers.md)
- [The readable and the linear parts of the honest PCP](lem-ar-pcp-parts.md)
- [The honest PCP of accepted answers; cor:functional_viewpoint_final, item 1](lem-ar-pcp-honest.md)

## Proof

The readable tables are read off the readable answers, and the readable polynomials off the readable tables. The linear tables are additive in the linear answers and the linear polynomials affine in the linear tables (Lemma [The readable and the linear parts of the honest PCP](lem-ar-pcp-parts.md)). Alice's encodings read only the cells of the padded readable answer and of her linear answer below $2^\ell$, Bob's only his. An accepted pair makes the verifier's programs halt, since otherwise its constraint rejects everything; then Lemma [The honest PCP of accepted answers; cor:functional_viewpoint_final, item 1](lem-ar-pcp-honest.md) applies.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.slot_pairPcp_readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slot_pairPcp_readable), [`MIPRE.Tailored.AnsRed.slot_pairPcp_affine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slot_pairPcp_affine), [`MIPRE.Tailored.AnsRed.slot_pairPcp_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slot_pairPcp_alice), [`MIPRE.Tailored.AnsRed.slot_pairPcp_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slot_pairPcp_bob), [`MIPRE.Tailored.AnsRed.indDeg_pairPcp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.indDeg_pairPcp), [`MIPRE.Tailored.AnsRed.accepts_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_halts), [`MIPRE.Tailored.AnsRed.identities_pairPcp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.identities_pairPcp), [`MIPRE.Tailored.AnsRed.HonestHyp.identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.HonestHyp.identities).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2967](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2967)
