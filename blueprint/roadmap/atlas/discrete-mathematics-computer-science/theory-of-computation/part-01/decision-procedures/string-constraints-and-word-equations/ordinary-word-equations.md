---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.evalWord, Cslib.AutomatedReasoning.StringConstraints.wordTerm, Cslib.AutomatedReasoning.StringConstraints.eval_wordTerm, Cslib.AutomatedReasoning.StringConstraints.WordEq, Cslib.AutomatedReasoning.StringConstraints.WordEq.Satisfies, Cslib.AutomatedReasoning.StringConstraints.WordEq.toFormula, Cslib.AutomatedReasoning.StringConstraints.WordEq.sat_toFormula, Cslib.AutomatedReasoning.StringConstraints.evalWord_eq_of_agree_on_vars
statement: formalized
proof: formalized
---

# Ordinary word equations

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html).

## Substitution of words for variables in a word

Substitute words for variables in a word over constants and variables.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.evalWord`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#eval-word).

## Embedding of ordinary words into string terms

Embed an ordinary word in the larger string-constraint term language.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordTerm`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#word-term).

## Word embedding preserves substitution semantics

The embedding preserves substitution semantics.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.eval_wordTerm`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#eval-word-term).

## Ordinary word equation

An ordinary word equation, with no morphisms or language-membership atoms.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq`, a structure declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#word-eq).

## Solution of a word equation

A substitution solves a word equation when the substituted sides agree.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.Satisfies`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#satisfies).

## Word equation as a string-constraint formula

View an ordinary word equation as a string-constraint formula.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.toFormula`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#to-formula).

## Formula embedding of word equations preserves satisfaction

The formula embedding preserves satisfaction.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.sat_toFormula`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#sat-to-formula).

## Word evaluation depends only on occurring variables

Evaluation depends only on variables that occur in the word.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.evalWord_eq_of_agree_on_vars`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#eval-word-eq-of-agree-on-vars).

## Occurring variable's image is no longer than the evaluated word

Each occurring variable contributes a contiguous block, so its length cannot
exceed the length of the evaluated word, even when substitutions may be empty.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.length_le_evalWord_of_mem`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#length-le-eval-word-of-mem).

## Word substitution normalized by emptying unused images

Retain the images of occurring variables and replace every unused image by
`[]`. Only equality of variables, not equality of alphabet symbols, is needed.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.normalizeWordSubst`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#normalize-word-subst).

## Normalization keeps images of occurring variables

Normalization preserves the image of every occurring variable.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.normalizeWordSubst_of_mem`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#normalize-word-subst-of-mem).

## Normalization empties images of absent variables

Every variable absent from the word has empty normalized image.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.normalizeWordSubst_of_not_mem`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#normalize-word-subst-of-not-mem).

## Normalization does not change the evaluated word

Removing unused images does not change the evaluated word.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.evalWord_normalizeWordSubst`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#eval-word-normalize-word-subst).

## Normalized images are bounded by the evaluation length

After normalization, every variable image, including unused ones, is
bounded by the length of the original evaluation.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.length_normalizeWordSubst_le`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#length-normalize-word-subst-le).

## Bounding variable images by the target loses no pattern matches

Matching a pattern against a fixed target loses no solutions by bounding
ALL variable images by the target length. Unused variables are normalized to
`[]`; an arbitrary unnormalized solution need not obey this bound.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.patternMatch_iff_bounded`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#pattern-match-iff-bounded).

## Executable satisfaction test for ground word equations

Executable satisfaction test for a ground equation. Since the variable
type is `Empty`, no substitution search is required.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.groundSatB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#ground-sat-b).

## Ground test agrees with satisfaction under any substitution

The ground test agrees with satisfaction under any substitution.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.groundSatB_eq_true_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#ground-sat-b-eq-true-iff).

## Ground test decides solvability of ground word equations

The executable ground test decides existence of a solution, not just
satisfaction of one guessed substitution.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.groundSatB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#ground-sat-b-iff).

## Solvability of word equation systems at a finite length bound

A system over finitely many variables has a solution iff one substitution
solves every equation at some finite global length bound. The witness bound is
obtained from the solution; this supplies no terminating general UNSAT test.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordSystem_satisfiable_iff_exists_bound`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#word-system-satisfiable-iff-exists-bound).

## Satisfiability of a single word equation at a finite length bound

An equation over `Fin n` is satisfiable iff it is satisfiable at some
finite global length bound. There is no equation-computable bound claimed.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.WordEq.satisfiable_iff_exists_bound`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/WordEquations.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html#satisfiable-iff-exists-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordinary word equations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/ordinary-word-equations)
