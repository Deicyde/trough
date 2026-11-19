---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.cw_encCws, MIPRE.Tailored.AnsRed.Typed.decAns_honestBits, MIPRE.Tailored.AnsRed.Typed.accepts_honestBits, MIPRE.Tailored.AnsRed.Typed.indOK_honestBits, MIPRE.Tailored.AnsRed.Typed.isoAgrees_honestBits, MIPRE.Tailored.AnsRed.Typed.passesV_honestBits, MIPRE.Tailored.AnsRed.Typed.arPred_honest
statement: formalized
proof: formalized
---

# The checks hold of honest answers

At two typed questions read off one seed, honest answers to answers of the oracularized input game that its predicate accepts pass the four checks of the answer-reduced predicate, for a degree $d \geq 17$.

## Depends on

- [The honest answers](def-ar-honest-answers.md)
- [The honest PCP of an answer pair](lem-ar-pair-pcp.md)
- [Completeness of oracularization, at the level of games](../../structure-of-the-proof/part-06/lem-oracular-completeness.md)
- [Answer-reduction completeness](../../structure-of-the-proof/part-08/lem-ar-completeness.md)

## Proof depends on

- [Slot values and block-local polynomials](lem-ar-slots.md)

## Proof

The two low-degree questions come from one sample of the seeded test. Equal roles carry equal oracularized answers, so one tuple of polynomials of individual degree at most $d$ answers both, and the test accepts its honest answers. At one low-degree type the questions agree, and an isolated player's polynomials are the oracle's in its slots. A codeword whose block misses the direction of an axis-parallel line does not involve that variable, so its restriction to the line is constant. An oracle's pair is accepted by the input game, so its PCP satisfies the identities, and the values of the oracle's point answer are the PCP's values at the point.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.cw_encCws`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.cw_encCws), [`MIPRE.Tailored.AnsRed.Typed.decAns_honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.decAns_honestBits), [`MIPRE.Tailored.AnsRed.Typed.accepts_honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.accepts_honestBits), [`MIPRE.Tailored.AnsRed.Typed.indOK_honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indOK_honestBits), [`MIPRE.Tailored.AnsRed.Typed.isoAgrees_honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isoAgrees_honestBits), [`MIPRE.Tailored.AnsRed.Typed.passesV_honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.passesV_honestBits), [`MIPRE.Tailored.AnsRed.Typed.arPred_honest`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arPred_honest).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2993](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2993)
