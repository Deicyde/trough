---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.bonferroniRejections, MathlibExt.Probability.Statistics.MultipleTesting.measure_exists_mem_le_le, MathlibExt.Probability.Statistics.MultipleTesting.measure_exists_le_div_le, MathlibExt.Probability.Statistics.MultipleTesting.measure_bonferroni_familywiseError_le
statement: formalized
proof: formalized
---

# Bonferroni correction

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html).

## Bonferroni rejection set

The hypotheses rejected by the Bonferroni procedure at level `α`: those whose p-value is
at most `α / m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bonferroniRejections`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html#bonferroni-rejections).

## Union bound for valid p-values

If every true-null p-value is valid and
`c ∈ [0, 1]`, the probability that some true null has p-value at most `c` is at most
`|H0| c`. No independence is assumed.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_exists_mem_le_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html#measure-exists-mem-le-le).

## Bonferroni inequality

If every true-null p-value is valid, the probability that some
true null has p-value at most `α / m` is at most `α |H0| / m`, for `α ∈ [0, 1]`. No
independence is assumed. (For `m = 0` there is no hypothesis and both sides are `0`.)

## Sources

- Bonferroni (1936); Dunn (1961).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_exists_le_div_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html#measure-exists-le-div-le).

## The Bonferroni procedure controls the FWER

If every true-null p-value is valid, the
probability that the Bonferroni procedure at level `α ∈ [0, 1]` rejects at least one true null
is at most `α`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_bonferroni_familywiseError_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Bonferroni.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html#measure-bonferroni-familywise-error-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bonferroni correction](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/bonferroni-correction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing/bonferroni-correction)
