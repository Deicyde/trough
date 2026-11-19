---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.pairPcp, MIPRE.Tailored.AnsRed.circOf, MIPRE.Tailored.AnsRed.HonestHyp, MIPRE.Tailored.AnsRed.Typed.encCws, MIPRE.Tailored.AnsRed.Typed.honestCoef, MIPRE.Tailored.AnsRed.Typed.honestBits, MIPRE.Tailored.AnsRed.Typed.ldPolys, MIPRE.Tailored.AnsRed.Typed.inSeeded, MIPRE.Tailored.AnsRed.Typed.rolePcp, MIPRE.Tailored.AnsRed.Typed.honestAns
statement: formalized
---

# The honest answers

The honest PCP of an answer pair $(a, b)$ at a question pair $(x, y)$ is $\mathrm{Induce}$ of the readable tables of the readable parts of $a, b$ and the linear tables of their linear parts. The honest answer of a tuple of polynomials on the test's $M$ variables to a question of the seeded low-degree test is its values at a point, or the coefficients of its restrictions to a line, each field element as its canonical bits, codeword after codeword. At a typed question of role $r$, to an answer of the oracularized input game, the honest answer is the honest answer of the role's codewords of the PCP of the oracle's pair at the questions of its seed, or of an isolated player's answer paired with itself. The hypotheses under which these PCPs satisfy the checks at every seed are that the parameters fit the lengths of the input game and the constraints its processor outputs on readable answers of at most the readable lengths, and that each seed's circuit describes the output indicator through the windows of its question pair within a time $L^*$ meets.

## Depends on

- [The honest PCP of accepted answers; cor:functional_viewpoint_final, item 1](lem-ar-pcp-honest.md)
- [The answer-reduced game as typed tailored data; defn:combi_ans_red](def-ar-tailored-game.md)
- [Restriction to a line](../../structure-of-the-proof/part-07/def-line-restriction.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.pairPcp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.pairPcp), [`MIPRE.Tailored.AnsRed.circOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.circOf), [`MIPRE.Tailored.AnsRed.HonestHyp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.HonestHyp), [`MIPRE.Tailored.AnsRed.Typed.encCws`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.encCws), [`MIPRE.Tailored.AnsRed.Typed.honestCoef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.honestCoef), [`MIPRE.Tailored.AnsRed.Typed.honestBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.honestBits), [`MIPRE.Tailored.AnsRed.Typed.ldPolys`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldPolys), [`MIPRE.Tailored.AnsRed.Typed.inSeeded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.inSeeded), [`MIPRE.Tailored.AnsRed.Typed.rolePcp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.rolePcp), [`MIPRE.Tailored.AnsRed.Typed.honestAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.honestAns).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2944](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2944)
