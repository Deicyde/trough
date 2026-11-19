---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.pow_le_pow_of_le', MIPRE.Tailored.AnsRed.Typed.ArRoutine.output_within
statement: formalized
proof: formalized
---

# The complexity clause of the answer reduction

For a parameter routine in polynomial time there are a polynomial $P$ and a degree $k$ such that every input tailored verifier within the input budget of answer reduction at $n$, with $|\mathsf{V}| \leq \sigma$, gives an output verifier whose sampler, calculator and processor run within $P((\lambda n + 1)^\mu + \sigma + \lambda + n)^{\mu + 1}$ at degree $k (\mu + 1)$, whose dimension is at most that bound, and whose lengths are at most that bound.

## Depends on

- [The output verifier of the answer reduction](def-ar-output.md)
- [The running time and the dimension of the answer-reduced sampler](lem-ar-sampler-time.md)
- [The running time of the answer-length calculator](lem-ar-len-time.md)
- [The running time of the linear-constraints processor](lem-ar-lp-time.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)

## Proof

Take $W = (\lambda n + 1)^\mu + \sigma + \lambda + n$, $X = |d| + 1$, and the sum of the constants of Lemmas [The running time and the dimension of the answer-reduced sampler](lem-ar-sampler-time.md), [The running time of the answer-length calculator](lem-ar-len-time.md) and [The running time of the linear-constraints processor](lem-ar-lp-time.md). The input budget gives the input sampler's running time and dimension.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.pow_le_pow_of_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pow_le_pow_of_le'), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.output_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.output_within).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3998](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3998)
