---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Intro.Inhabit.tailoredIntrospection, MIPRE.Tailored.Intro.Inhabit.exists_tailoredIntrospection
statement: formalized
proof: formalized
---

# Question reduction for tailored verifiers; II:5712

The contract `TailoredIntrospection` is inhabited, at input level $7$.

## Depends on

- [The three stage contracts](def-tailored-stages.md)
- [The introspection linear-constraints processor](../part-05/lem-intro-lp-program.md)
- [The honest strategy is a perfect ZPC strategy](../part-04/lem-intro-honest-zpc.md)
- [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md)
- [Reading the construction at $C\lambda$ as one at $\lambda$](../part-05/lem-intro-rescale.md)
- [A tailored verifier as a bounded normal form verifier](../part-04/lem-of-tnfvt.md)

## Proof

Route A (Remark [Route A: the two checks](../README.md)). A $\lambda$-bounded tailored input has a $C_0\lambda$-bounded normal form verifier (Lemma [A tailored verifier as a bounded normal form verifier](../part-04/lem-of-tnfvt.md)); with $M = 2^{C_0 + 1}$, the output at $\lambda$ is the output tailored verifier of Lemma [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md) at $M\lambda$, with the introspection verifier's sampler and the programs $\mathrm{L}^{\mathrm{intro}}$ and $\mathrm{LP}^{\mathrm{intro}}$ at $M\lambda$, which meet its specification (Lemma [The introspection linear-constraints processor](../part-05/lem-intro-lp-program.md)). Soundness is that of Lemma [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md), with $a M^a$ in place of $a$; completeness at $n \geq 1$ is Lemma [The honest strategy is a perfect ZPC strategy](../part-04/lem-intro-honest-zpc.md), and at $n = 0$ the output is empty. The budgets at $M\lambda$ are budgets at $\lambda$ (Lemma [Reading the construction at $C\lambda$ as one at $\lambda$](../part-05/lem-intro-rescale.md)).

## Lean

Formalized as [`MIPRE.Tailored.Intro.Inhabit.tailoredIntrospection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Inhabit.tailoredIntrospection), [`MIPRE.Tailored.Intro.Inhabit.exists_tailoredIntrospection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Inhabit.exists_tailoredIntrospection).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1078](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1078)
