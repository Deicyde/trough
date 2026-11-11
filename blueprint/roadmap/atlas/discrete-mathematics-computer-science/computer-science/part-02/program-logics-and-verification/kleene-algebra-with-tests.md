---
declaration: section
origin: cited
lean: KleeneAlgebra.star_simulation, KleeneAlgebra.test_star_absorption, Cslib.RelationAlgebra.testSet, Cslib.RelationAlgebra.mem_testSet, Cslib.RelationAlgebra.testSet_le_one, Cslib.RelationAlgebra.testSet_mul_testSet, Cslib.RelationAlgebra.test_mul_le_mul_test_iff, Cslib.RelationAlgebra.test_mul_eq_test_mul_test_iff
statement: formalized
proof: formalized
---

# Kleene algebra with tests

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html).

## A one-step simulation lifts to finite iteration

A one-step simulation lifts to arbitrary finite iteration.
The simulator `p` need not be invertible or a test.

Formalized by `KleeneAlgebra.star_simulation`, a theorem declared in [MathlibExt/Algebra/Order/Kleene.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Order/Kleene.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#star-simulation).

## Tests preserved by one step are preserved by iteration

An idempotent subidentity preserved by one step is preserved by
iteration. This is a corollary of `star_simulation`; the test assumptions
are explicit, with no additional algebraic structure.

Formalized by `KleeneAlgebra.test_star_absorption`, a theorem declared in [MathlibExt/Algebra/Order/Kleene.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Order/Kleene.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-star-absorption).

## Diagonal test relation of an assertion

The diagonal relation restricted to an assertion.

Formalized by `Cslib.RelationAlgebra.testSet`, a definition declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set).

## Membership in a diagonal test relation

Membership in a diagonal test.

Formalized by `Cslib.RelationAlgebra.mem_testSet`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#mem-test-set).

## Diagonal tests are subidentities

A test is a subidentity, not an arbitrary relation.

Formalized by `Cslib.RelationAlgebra.testSet_le_one`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-le-one).

## Composing diagonal tests conjoins their assertions

Sequential tests conjoin their assertions without changing state.

Formalized by `Cslib.RelationAlgebra.testSet_mul_testSet`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-mul-test-set).

## Verification inequality characterizes partial correctness

The verification inequality is precisely universal partial
correctness: every execution from `P` ends in `Q`.

Formalized by `Cslib.RelationAlgebra.test_mul_le_mul_test_iff`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-mul-le-mul-test-iff).

## Postcondition absorption characterizes partial correctness

A postcondition can be absorbed on the right exactly when it holds
on every execution starting in the precondition.

Formalized by `Cslib.RelationAlgebra.test_mul_eq_test_mul_test_iff`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-mul-eq-test-mul-test-iff).

## Partial correctness as unreachability of the negated postcondition

Classically, verification means that no execution from `P` can
reach the complement of `Q`.

Formalized by `Cslib.RelationAlgebra.test_mul_test_compl_eq_bot_iff`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-mul-test-compl-eq-bot-iff).

## Test of the false assertion is the zero relation

The false assertion is the zero relation.

Formalized by `Cslib.RelationAlgebra.testSet_empty`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-empty).

## Test of the true assertion is the identity relation

The true assertion is the identity relation.

Formalized by `Cslib.RelationAlgebra.testSet_univ`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-univ).

## Test of a negated assertion is the complement within identity

Boolean test negation is complement relative to identity, not the
full relation-algebra complement (which includes off-diagonal pairs).

Formalized by `Cslib.RelationAlgebra.testSet_compl`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-compl).

## Test of a union of assertions is the union of tests

Union of assertions is union of their diagonal tests.

Formalized by `Cslib.RelationAlgebra.testSet_union`, a theorem declared in [CSLibExt/Foundations/RelationAlgebra/Tests.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/RelationAlgebra/Tests.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html#test-set-union).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kleene algebra with tests](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/program-logics-and-verification/kleene-algebra-with-tests)
