---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.Scale.doubleF, MIPRE.Tailored.Intro.Scale.doubleF_apply, MIPRE.Tailored.Intro.Scale.mulPow2F, MIPRE.Tailored.Intro.Scale.mulPow2F_apply, MIPRE.Tailored.Intro.Scale.ansBound_scale, MIPRE.Tailored.Intro.Scale.LenBound.mono, MIPRE.Tailored.Intro.Scale.lenIntro_within, MIPRE.Tailored.Intro.Scale.hasPerfectZPC_of_zero, MIPRE.Tailored.TailoredVerifier.IsBounded.mono
statement: formalized
proof: formalized
---

# Reading the construction at $C\lambda$ as one at $\lambda$

$\lambda \mapsto 2^k \lambda$ is a polynomial-time function. A budget at $C\lambda$ is a budget at $\lambda$ with the exponent multiplied by $C$: $2^{(C\lambda n + 1)^{C'}} \le 2^{(\lambda n + 1)^{CC'}}$. $\lambda$-boundedness of a tailored verifier is monotone in $\lambda$. A tailored verifier whose calculator outputs $0$ and whose processor outputs no constraint at index $n$ has a perfect ZPC strategy there, the trivial one.

## Depends on

- [The introspection answer-length calculator](lem-intro-len-program.md)
- [The trivial strategy; II:1148](../part-01/lem-tailored-trivial-zpc.md)
- [The output tailored verifier, from a specification of its programs](../part-04/lem-intro-output.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)

## Proof

Bernoulli's inequality $C x + 1 \le (x + 1)^C$; for the last, every pair of empty answers is accepted.

## Lean

Formalized as [`MIPRE.Tailored.Intro.Scale.doubleF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.doubleF), [`MIPRE.Tailored.Intro.Scale.doubleF_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.doubleF_apply), [`MIPRE.Tailored.Intro.Scale.mulPow2F`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.mulPow2F), [`MIPRE.Tailored.Intro.Scale.mulPow2F_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.mulPow2F_apply), [`MIPRE.Tailored.Intro.Scale.ansBound_scale`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.ansBound_scale), [`MIPRE.Tailored.Intro.Scale.LenBound.mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.LenBound.mono), [`MIPRE.Tailored.Intro.Scale.lenIntro_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.lenIntro_within), [`MIPRE.Tailored.Intro.Scale.hasPerfectZPC_of_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Scale.hasPerfectZPC_of_zero), [`MIPRE.Tailored.TailoredVerifier.IsBounded.mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.IsBounded.mono).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2215](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2215)
