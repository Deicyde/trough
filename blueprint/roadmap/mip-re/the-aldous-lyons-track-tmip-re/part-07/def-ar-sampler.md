---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.LdRoutine, MIPRE.Tailored.AnsRed.Typed.LdRoutine.ldDirect, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_cl, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_dim, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler, MIPRE.Tailored.AnsRed.Typed.LdRoutine.qe, MIPRE.Tailored.AnsRed.Typed.LdRoutine.typedPF, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg, MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg_eq
statement: formalized
---

# The answer-reduced sampler

A *parameter routine of the low-degree half* is a family of parameters $t, j$ at each $(\lambda, \mu, \sigma)$ and index, with a polynomial-time map from $(\lambda, \mu, \sigma)$ to a closed program computing them at each index. The *answer-reduced typed sampler* at $(\lambda, \mu, \sigma)$ puts the oracularized input sampler and the directly answered low-degree half of Lemma [The low-degree half of the answer-reduced sampler, directly answered](lem-ar-ld-direct.md) side by side; its CL functions are the answer-reduced family of Definition [The honest strategy of the answer-reduced game](../part-06/def-ar-honest-strategy.md). The *answer-reduced sampler* is the typed sampler detyped along the complete graph with loops, of level $\max(\ell + 1, 3) + 2$. Its program is computed from the input sampler's and $(\lambda, \mu, \sigma)$ in polynomial time.

## Depends on

- [The low-degree half of the answer-reduced sampler, directly answered](lem-ar-ld-direct.md)
- [The honest strategy of the answer-reduced game](../part-06/def-ar-honest-strategy.md)
- [The typed oracularized sampler](../../structure-of-the-proof/part-06/lem-oracle-typed-sampler.md)
- [Executable detyping sampler](../../structure-of-the-proof/part-01/lem-detype-functional-sampler.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.LdRoutine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.ldDirect`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.ldDirect), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_cl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_cl), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arTyped_dim), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.qe`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.qe), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.typedPF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.typedPF), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg), [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSamplerProg_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3580](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3580)
