---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.closedRejections, MathlibExt.Probability.Statistics.MultipleTesting.mem_closedRejections, MathlibExt.Probability.Statistics.MultipleTesting.inter_nonempty_closedRejections, MathlibExt.Probability.Statistics.MultipleTesting.measure_closed_familywiseError_le, MathlibExt.Probability.Statistics.MultipleTesting.bonferroniLocalTest, MathlibExt.Probability.Statistics.MultipleTesting.measure_bonferroniLocalTest_le, MathlibExt.Probability.Statistics.MultipleTesting.holmRejections_eq_closedRejections
statement: formalized
proof: formalized
---

# Closed testing principle

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html).

## Closed testing procedure

The closed testing procedure: given the decisions `φ J` of local tests of the intersection
hypotheses `H_J`, reject `Hᵢ` exactly when `φ J` holds for every `J` containing `i`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.closedRejections`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#closed-rejections).

## Membership in the closed rejection set

Membership in the closed rejection set.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.mem_closedRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#mem-closed-rejections).

## Closed testing rejection implies the intersection test rejects

If the closed procedure rejects a hypothesis in `H0`, then the local test of the
intersection hypothesis `H_{H0}` rejects.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.inter_nonempty_closedRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#inter-nonempty-closed-rejections).

## The closed testing principle

If `H0` is the set of true nulls and the local test of
`H_{H0}` rejects with probability at most `α`, then the closed procedure rejects some true
null with probability at most `α`. Applied to every possible `H0`, local level-`α` tests give
strong control of the family-wise error rate. No assumption on the dependence between local
tests is made.

## Sources

- Marcus, Peritz and Gabriel (1976).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_closed_familywiseError_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#measure-closed-familywise-error-le).

## Bonferroni local test of an intersection hypothesis

The Bonferroni local test of the intersection hypothesis `H_J` at level `α`: reject when
some `j ∈ J` has `p j ≤ α / |J|`. (It never rejects `H_∅`.)

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bonferroniLocalTest`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#bonferroni-local-test).

## Level of the Bonferroni local test

The Bonferroni local test of `H_{H0}` has level `α ∈ [0, 1]` when the p-values in `H0`
are valid.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_bonferroniLocalTest_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#measure-bonferroni-local-test-le).

## Holm's procedure is a closed test

For `α ≥ 0`, the hypotheses rejected by Holm's
step-down procedure are exactly those rejected by the closed testing procedure built on the
Bonferroni local tests.

## Sources

- Holm (1979) introduces the procedure; the closure is that of Marcus, Peritz and Gabriel (1976).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.holmRejections_eq_closedRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/ClosedTesting.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html#holm-rejections-eq-closed-rejections).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closed testing principle](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/closed-testing-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/closed-testing-principle)
