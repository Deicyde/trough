---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ldBitsV, MIPRE.Tailored.AnsRed.Typed.toBits_ld, MIPRE.Tailored.AnsRed.Typed.blocks1, MIPRE.Tailored.AnsRed.Typed.blocks1_ldBitsV, MIPRE.Tailored.AnsRed.Typed.ldDesc, MIPRE.Tailored.AnsRed.Typed.ldAnswer, MIPRE.Tailored.AnsRed.Typed.ldAnswer_marginal, MIPRE.Tailored.AnsRed.Typed.ldAnswer_linear, MIPRE.Tailored.AnsRed.Typed.ldAnswer_factor, MIPRE.Tailored.AnsRed.Typed.ldAnswerProg, MIPRE.Tailored.AnsRed.Typed.ldDimProg, MIPRE.Tailored.AnsRed.Typed.LdFamily, MIPRE.Tailored.AnsRed.Typed.LdFamily.ldAnswerProg_apply, MIPRE.Tailored.AnsRed.Typed.LdFamily.ldDimProg_pd, MIPRE.Tailored.AnsRed.Typed.LdFamily.directSampler
statement: formalized
proof: formalized
---

# The low-degree half of the answer-reduced sampler, directly answered

Represent a vector of the registers $\mathbb{F}_q^{D}$ of the seeded low-degree test, $D = 2M + 1$, by its coordinates' Shoup bits, $t$ per coordinate: three runs of $t$-bit blocks, $M$ for the point, $M$ for the direction and one for the seed. On such bits, the run functions of the MIP\* answer reduction's stage program, on one copy of the test at offset $0$ and length $M$, return the bits of the answers of the test's presentation to its marginal, linear-map and factor queries. So for parameters $t \geq 1$ and $j \leq t$ at every index, computed by a closed program, the presentation, downsized along the Shoup basis, is a sampler answered directly by a polynomial-time function of the parameters.

## Depends on

- [The answer-reduced game as typed tailored data; defn:combi_ans_red](../part-06/def-ar-tailored-game.md)
- [The typed answer-reduced sampler](../../structure-of-the-proof/part-08/lem-ar-typed-sampler.md)

## Proof

A query returns, run by run, the point, the direction and the seed components of the presentation's answer, each a linear function of the components of the query; the run functions compute these on blocks of Shoup bits, which are coordinates of $\mathbb{F}_q$ written over $\mathbb{F}_2$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ldBitsV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldBitsV), [`MIPRE.Tailored.AnsRed.Typed.toBits_ld`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.toBits_ld), [`MIPRE.Tailored.AnsRed.Typed.blocks1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.blocks1), [`MIPRE.Tailored.AnsRed.Typed.blocks1_ldBitsV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.blocks1_ldBitsV), [`MIPRE.Tailored.AnsRed.Typed.ldDesc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldDesc), [`MIPRE.Tailored.AnsRed.Typed.ldAnswer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldAnswer), [`MIPRE.Tailored.AnsRed.Typed.ldAnswer_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldAnswer_marginal), [`MIPRE.Tailored.AnsRed.Typed.ldAnswer_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldAnswer_linear), [`MIPRE.Tailored.AnsRed.Typed.ldAnswer_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldAnswer_factor), [`MIPRE.Tailored.AnsRed.Typed.ldAnswerProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldAnswerProg), [`MIPRE.Tailored.AnsRed.Typed.ldDimProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldDimProg), [`MIPRE.Tailored.AnsRed.Typed.LdFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdFamily), [`MIPRE.Tailored.AnsRed.Typed.LdFamily.ldAnswerProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdFamily.ldAnswerProg_apply), [`MIPRE.Tailored.AnsRed.Typed.LdFamily.ldDimProg_pd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdFamily.ldDimProg_pd), [`MIPRE.Tailored.AnsRed.Typed.LdFamily.directSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdFamily.directSampler).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3550](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3550)
