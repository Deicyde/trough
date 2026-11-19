---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.le_of_arg_le, MIPRE.Tailored.AnsRed.Typed.le_size_arParams, MIPRE.Tailored.AnsRed.Typed.lms_pdom, MIPRE.Tailored.AnsRed.Typed.ArRoutine.params_pdom, MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_time, MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldPar_time, MIPRE.Tailored.AnsRed.Typed.ArRoutine.arProgs_size_pdom, MIPRE.Tailored.AnsRed.Typed.ArRoutine.arTyped_time, MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_time, MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_dim_pdom
statement: formalized
proof: formalized
---

# The running time and the dimension of the answer-reduced sampler

For a parameter routine in polynomial time there are $C$, $M$ and $E$ such that, for every $W \geq (\lambda n + 1)^\mu + \sigma + \lambda + n$ and every input sampler $S$ with $|S| \leq W$ running within $(\lambda n + 1)^\mu (|d| + 1)^\mu$ at $n$, the answer-reduced sampler runs within $(C (W + 1)^M)^{\mu + 1} (|d| + 1)^{E (\mu + 1)}$ at $n$; and when the dimension of $S$ at $n$ is at most $W$, the answer-reduced sampler's dimension at $n$ is at most $(C (W + 1)^M)^{\mu + 1}$.

## Depends on

- [A parameter routine in polynomial time](def-ar-par-time.md)
- [The answer-reduced sampler](../part-07/def-ar-sampler.md)
- [The typed answer-reduced sampler](../../structure-of-the-proof/part-08/lem-ar-typed-sampler.md)
- [The typed oracularized sampler](../../structure-of-the-proof/part-06/lem-oracle-typed-sampler.md)
- [Answer-reduction construction](../../structure-of-the-proof/part-08/lem-ar-construction.md)

## Proof

The parameters are the output of a run within the bound, so their encoding and each parameter are dominated. The low-degree half's parameter program is the routine's followed by a polynomial-time projection. The typed sampler is the product of the oracularized input sampler, within a monomial at degree $e (\mu + 1)$ (Lemma [The typed oracularized sampler](../../structure-of-the-proof/part-06/lem-oracle-typed-sampler.md)), and the low-degree half, whose cost is that of the product's accounting (Lemma [The typed answer-reduced sampler](../../structure-of-the-proof/part-08/lem-ar-typed-sampler.md)); detyping preserves the shape of the bound (Lemma [Answer-reduction construction](../../structure-of-the-proof/part-08/lem-ar-construction.md)). The dimension is the graph view's bits, the input sampler's dimension and $(2 M + 1) t$, with $M$ and $t$ below the parameters' size.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.le_of_arg_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.le_of_arg_le), [`MIPRE.Tailored.AnsRed.Typed.le_size_arParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.le_size_arParams), [`MIPRE.Tailored.AnsRed.Typed.lms_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lms_pdom), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.params_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.params_pdom), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_time), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldPar_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldPar_time), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.arProgs_size_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.arProgs_size_pdom), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.arTyped_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.arTyped_time), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_time), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_dim_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.arSampler_dim_pdom).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3918](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3918)
