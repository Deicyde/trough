---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.CLData.context, MIPRE.Tailored.Intro.CLData.eval, MIPRE.Tailored.Intro.CLData.eval_correct, MIPRE.Tailored.Intro.CLData.sourceEval, MIPRE.Tailored.Intro.CLData.sourceEval_correct, MIPRE.Tailored.Intro.CLData.scan, MIPRE.Tailored.Intro.CLData.outputPrefix, MIPRE.Tailored.Intro.CLData.Guard, MIPRE.Tailored.Intro.CLData.guard_mono, MIPRE.Tailored.Intro.CLData.guard_zero, MIPRE.Tailored.Intro.CLData.outputPrefix_correct, MIPRE.Tailored.Intro.CLData.factor, MIPRE.Tailored.Intro.CLData.factor_correct, MIPRE.Tailored.Intro.CLData.register, MIPRE.Tailored.Intro.CLData.register_correct, MIPRE.Tailored.Intro.CLData.matrix, MIPRE.Tailored.Intro.CLData.matrix_correct, MIPRE.Tailored.Intro.CLData.kernelGenerators, MIPRE.Tailored.Intro.CLData.kernelGenerators_correct, MIPRE.Tailored.Intro.CLData.guard, MIPRE.Tailored.Intro.CLData.guard_correct, MIPRE.Tailored.Intro.CLData.inSource, MIPRE.Tailored.Intro.CLData.inSource_correct
statement: formalized
proof: formalized
---

# The sampler's data, from the introspection kernel's queries

For a $\lambda$-bounded normal form verifier at index $2^n$ and a register $y$, polynomial-time functions of the kernel's context and $y$ compute the evaluation of the padded CL function, the prefix condition, and membership in the source's outputs; and, when the prefix condition holds at stage $k$, the reported prefix, the prefix register and the stage's factor as masks, and the matrix of the stage's linear map, hence generators of its kernel.

## Depends on

- [Conditionally linear function](../../structure-of-the-proof/part-01/def-cl-function.md)
- [Decider](../../foundations/part-03/def-decider.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Sampler](../../foundations/part-03/def-sampler.md)
- [Closure of CL functions](../../structure-of-the-proof/part-01/lem-cl-closure.md)
- [Structure of a CL function](../../structure-of-the-proof/part-01/lem-cl-structure.md)
- [Register embeddings and detyped query routing](../../structure-of-the-proof/part-01/lem-detype-queries.md)
- [Total clocking of arbitrary typed decision programs](../../structure-of-the-proof/part-01/lem-detype-total-clock.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)
- [Effective binary matrix arithmetic and elimination](../../background-results/part-05/lem-effective-binary-linear-algebra.md)
- [Actual adaptive prefix law and residual registers](../../structure-of-the-proof/part-04/lem-intro-adaptive-prefix.md)
- [Arbitrary binary source registers and exact padding](../../structure-of-the-proof/part-06/lem-intro-binary-source-padding.md)
- [Uniform executable cross-introspection compiler](../../structure-of-the-proof/part-03/lem-intro-dynamic-source-compiler.md)
- [Guarded maps on arbitrary hiding answers](../../structure-of-the-proof/part-03/lem-intro-guarded-hiding-maps.md)
- [The parsed introspection decision predicate](../../structure-of-the-proof/part-02/lem-intro-parsed-predicate.md)
- [Full Read rigidity](../../structure-of-the-proof/part-04/lem-intro-read-rigidity.md)
- [Sampling and hiding subtest estimates](../../structure-of-the-proof/part-03/lem-intro-subtest-estimates.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Proof

These are the kernel's own queries and scans, read out rather than compared; the sampler's program is specified at attained prefixes, which the prefix condition provides.

## Lean

Formalized as [`MIPRE.Tailored.Intro.CLData.context`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.context), [`MIPRE.Tailored.Intro.CLData.eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.eval), [`MIPRE.Tailored.Intro.CLData.eval_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.eval_correct), [`MIPRE.Tailored.Intro.CLData.sourceEval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.sourceEval), [`MIPRE.Tailored.Intro.CLData.sourceEval_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.sourceEval_correct), [`MIPRE.Tailored.Intro.CLData.scan`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.scan), [`MIPRE.Tailored.Intro.CLData.outputPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.outputPrefix), [`MIPRE.Tailored.Intro.CLData.Guard`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.Guard), [`MIPRE.Tailored.Intro.CLData.guard_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.guard_mono), [`MIPRE.Tailored.Intro.CLData.guard_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.guard_zero), [`MIPRE.Tailored.Intro.CLData.outputPrefix_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.outputPrefix_correct), [`MIPRE.Tailored.Intro.CLData.factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.factor), [`MIPRE.Tailored.Intro.CLData.factor_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.factor_correct), [`MIPRE.Tailored.Intro.CLData.register`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.register), [`MIPRE.Tailored.Intro.CLData.register_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.register_correct), [`MIPRE.Tailored.Intro.CLData.matrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.matrix), [`MIPRE.Tailored.Intro.CLData.matrix_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.matrix_correct), [`MIPRE.Tailored.Intro.CLData.kernelGenerators`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.kernelGenerators), [`MIPRE.Tailored.Intro.CLData.kernelGenerators_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.kernelGenerators_correct), [`MIPRE.Tailored.Intro.CLData.guard`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.guard), [`MIPRE.Tailored.Intro.CLData.guard_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.guard_correct), [`MIPRE.Tailored.Intro.CLData.inSource`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.inSource), [`MIPRE.Tailored.Intro.CLData.inSource_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.CLData.inSource_correct).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2053](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2053)
