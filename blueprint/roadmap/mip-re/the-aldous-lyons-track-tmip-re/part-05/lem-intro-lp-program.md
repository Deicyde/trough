---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.LpIntro.lpIntroC, MIPRE.Tailored.Intro.LpIntro.lpIntroProgC, MIPRE.Tailored.Intro.LpIntro.lpIntroProgC_eq, MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs, MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs_zero, MIPRE.Tailored.Intro.LpIntro.lpIntroC_cons_eq, MIPRE.Tailored.Intro.LpIntro.lpIntroC_size, MIPRE.Tailored.Intro.LpIntro.lpIntroC_size_le, MIPRE.Tailored.Intro.LpIntro.lpIntroC_budget, MIPRE.Tailored.Intro.LpIntro.lpIntro, MIPRE.Tailored.Intro.LpIntro.lpIntroProg, MIPRE.Tailored.Intro.LpIntro.lpIntroProg_eq, MIPRE.Tailored.Intro.LpIntro.lpIntro_lpIs_zero, MIPRE.Tailored.Intro.LpIntro.lpIntro_cons_eq, MIPRE.Tailored.Intro.LpIntro.introSpec_lenIntro_lpIntro, MIPRE.Tailored.Intro.LpIntro.lpIntro_budget, MIPRE.Tailored.Intro.LpIntro.lpIntro_size_le
statement: formalized
proof: formalized
---

# The introspection linear-constraints processor

A program $\mathrm{LP}^{\mathrm{intro}}$, computed from the input's three descriptions and $\lambda$ in polynomial time, outputs nothing at $\lambda = 0$ or $n = 0$, and otherwise, at a pair of detyped questions, decodes the edge they ask, checks the readable lengths of the two answers, and outputs the presented game's constraints at that edge: the Pauli constraints, the Pauli hiding constraints in either order, and the auxiliary constraints, with the kernel generators computed by elimination and the input's programs run on the clamped descriptions under a clock. With $\mathrm{L}^{\mathrm{intro}}$ it meets the specification of Lemma [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md) for a $\lambda$-bounded input whose normal form verifier is $\lambda$-bounded. It runs within $2^{(\lambda n + 1)^C}$ at degree $C$ on every input, and $|\mathrm{LP}^{\mathrm{intro}}| \le C(\lambda + 1)^C$.

## Depends on

- [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md)
- [The introspection answer-length calculator](lem-intro-len-program.md)
- [The input's programs, run on a clamped description](../part-04/lem-intro-input-runs.md)
- [The sampler's data, from the introspection kernel's queries](../part-04/lem-intro-cl-data.md)
- [The Pauli constraints of the first hiding edge, as programs](lem-intro-pauli-progs.md)
- [The Pauli constraints, as a program](lem-intro-pauli-cons-prog.md)
- [The constraint lists of the auxiliary checks, as programs](lem-intro-aux-progs.md)
- [Kernel generators of a register-local linear map](../part-04/lem-intro-kergens.md)
- [The typed tailored data of the introspection verifier](../part-04/lem-intro-typed-cons.md)

## Proof

A composition of the programs of the previous lemmas, by cases on the finitely many labels; each branch's output is the corresponding constraint family on the edge, and the costs add.

## Lean

Formalized as [`MIPRE.Tailored.Intro.LpIntro.lpIntroC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC), [`MIPRE.Tailored.Intro.LpIntro.lpIntroProgC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroProgC), [`MIPRE.Tailored.Intro.LpIntro.lpIntroProgC_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroProgC_eq), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_lpIs_zero), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_cons_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_cons_eq), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_size), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_size_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_size_le), [`MIPRE.Tailored.Intro.LpIntro.lpIntroC_budget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroC_budget), [`MIPRE.Tailored.Intro.LpIntro.lpIntro`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntro), [`MIPRE.Tailored.Intro.LpIntro.lpIntroProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroProg), [`MIPRE.Tailored.Intro.LpIntro.lpIntroProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntroProg_eq), [`MIPRE.Tailored.Intro.LpIntro.lpIntro_lpIs_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntro_lpIs_zero), [`MIPRE.Tailored.Intro.LpIntro.lpIntro_cons_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntro_cons_eq), [`MIPRE.Tailored.Intro.LpIntro.introSpec_lenIntro_lpIntro`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.introSpec_lenIntro_lpIntro), [`MIPRE.Tailored.Intro.LpIntro.lpIntro_budget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntro_budget), [`MIPRE.Tailored.Intro.LpIntro.lpIntro_size_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LpIntro.lpIntro_size_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2181](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2181)
