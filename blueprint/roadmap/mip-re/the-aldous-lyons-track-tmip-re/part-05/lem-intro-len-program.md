---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.LenIntro.introLenR, MIPRE.Tailored.Intro.LenIntro.introLenL, MIPRE.Tailored.Intro.LenIntro.introLen, MIPRE.Tailored.Intro.LenIntro.lin_coef, MIPRE.Tailored.Intro.LenIntro.lenIntroC, MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs, MIPRE.Tailored.Intro.LenIntro.lenAt_eq, MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs_detype, MIPRE.Tailored.Intro.LenIntro.lenIntroC_budget, MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenTotal, MIPRE.Tailored.Intro.LenIntro.lenIntro, MIPRE.Tailored.Intro.LenIntro.lenIntroProg, MIPRE.Tailored.Intro.LenIntro.lenIntroProg_eq, MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs, MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs_zero, MIPRE.Tailored.Intro.LenIntro.lenIntro_budget, MIPRE.Tailored.Intro.LenIntro.lenIntro_lenTotal
statement: formalized
proof: formalized
---

# The introspection answer-length calculator

A program, depending on $\lambda$ alone, outputs at every question the lengths of the presented game at the question's label — $0$ off the decodable views, and at index $0$ or $\lambda = 0$ — halts everywhere, and runs within $2^{(\lambda n + 1)^C}(|d| + 1)^C$, its outputs at most $2^{(\lambda n + 1)^C}$.

## Depends on

- [The typed tailored data of the introspection verifier](../part-04/lem-intro-typed-cons.md)
- [Detyping a tailored game](../part-03/def-tailored-detyping.md)
- [Supplying ambient introspection](../../structure-of-the-proof/part-06/lem-introspection-supply.md)

## Proof

The lengths are fixed combinations of $k$, $2^j k$, $Q$, $R$ and $1$, read from a table over the graph view; $Q$ and $R$ are computed in unary.

## Lean

Formalized as [`MIPRE.Tailored.Intro.LenIntro.introLenR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.introLenR), [`MIPRE.Tailored.Intro.LenIntro.introLenL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.introLenL), [`MIPRE.Tailored.Intro.LenIntro.introLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.introLen), [`MIPRE.Tailored.Intro.LenIntro.lin_coef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lin_coef), [`MIPRE.Tailored.Intro.LenIntro.lenIntroC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroC), [`MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs), [`MIPRE.Tailored.Intro.LenIntro.lenAt_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenAt_eq), [`MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs_detype`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenIs_detype), [`MIPRE.Tailored.Intro.LenIntro.lenIntroC_budget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroC_budget), [`MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenTotal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroC_lenTotal), [`MIPRE.Tailored.Intro.LenIntro.lenIntro`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntro), [`MIPRE.Tailored.Intro.LenIntro.lenIntroProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroProg), [`MIPRE.Tailored.Intro.LenIntro.lenIntroProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntroProg_eq), [`MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs), [`MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntro_lenIs_zero), [`MIPRE.Tailored.Intro.LenIntro.lenIntro_budget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntro_budget), [`MIPRE.Tailored.Intro.LenIntro.lenIntro_lenTotal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LenIntro.lenIntro_lenTotal).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2125](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2125)
