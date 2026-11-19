---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredVerifier, MIPRE.Tailored.LenIs, MIPRE.Tailored.LenBound, MIPRE.Tailored.LenTotal, MIPRE.Tailored.LpIs, MIPRE.Cost.Data.spineList, MIPRE.Cost.Data.bitsListD, MIPRE.Tailored.TailoredVerifier.progs, MIPRE.Tailored.TailoredVerifier.size, MIPRE.Tailored.TailoredVerifier.Questions, MIPRE.Tailored.TailoredVerifier.lenOf, MIPRE.Tailored.TailoredVerifier.LenDefined, MIPRE.Tailored.TailoredVerifier.consOf, MIPRE.Tailored.TailoredVerifier.tgame, MIPRE.Tailored.TailoredVerifier.valStar, MIPRE.Tailored.TailoredVerifier.HasPerfectZPC
statement: formalized
---

# Tailored normal form verifier; II:1758

A *tailored normal form verifier* $\mathsf{V} = (\mathcal{S}, \mathcal{L}, \mathcal{P})$ is a conditionally linear sampler $\mathcal{S}$ (Definition [Sampler](../../foundations/part-03/def-sampler.md)), an *answer-length calculator* $\mathcal{L}$, which on $(n, x, \kappa)$ outputs, in unary, the number of readable ($\kappa = R$) or linear ($\kappa = L$) variables at the question $x$, and a *linear-constraints processor* $\mathcal{P}$, which on $(n, x, y, a^R, b^R)$ outputs the list $L_{xy}(a^R, b^R)$; the paper's fourth machine, the canonical decider, is the same for every verifier (Definition [The canonical decider, as a program; II:1757–1787](def-canonical-decider.md)). The outputs are read totally, so that none is malformed: a length as the length of the output's spine, a list of constraints elementwise. The *$n$-th game* $\mathsf{V}_n$ is the tailored game on the sampler's questions that the programs compute, a question or pair at which a program does not halt rejecting every answer. $\mathsf{V}$ *has a perfect ZPC strategy at $n$* when the doubled game of $\mathsf{V}_n$ has one (Remark [Two conventions](../README.md)).

## Depends on

- [Tailored game; II:1243](def-tailored-game.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](def-zpc-strategy.md)
- [Sampler](../../foundations/part-03/def-sampler.md)
- [Decider](../../foundations/part-03/def-decider.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier), [`MIPRE.Tailored.LenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.LenIs), [`MIPRE.Tailored.LenBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.LenBound), [`MIPRE.Tailored.LenTotal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.LenTotal), [`MIPRE.Tailored.LpIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.LpIs), [`MIPRE.Cost.Data.spineList`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Data.spineList), [`MIPRE.Cost.Data.bitsListD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Data.bitsListD), [`MIPRE.Tailored.TailoredVerifier.progs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.progs), [`MIPRE.Tailored.TailoredVerifier.size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.size), [`MIPRE.Tailored.TailoredVerifier.Questions`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.Questions), [`MIPRE.Tailored.TailoredVerifier.lenOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.lenOf), [`MIPRE.Tailored.TailoredVerifier.LenDefined`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.LenDefined), [`MIPRE.Tailored.TailoredVerifier.consOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.consOf), [`MIPRE.Tailored.TailoredVerifier.tgame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.tgame), [`MIPRE.Tailored.TailoredVerifier.valStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.valStar), [`MIPRE.Tailored.TailoredVerifier.HasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.HasPerfectZPC).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 330](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L330)
