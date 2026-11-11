---
declaration: section
origin: cited
lean: Cslib.LTL.Tableau.State, Cslib.LTL.Tableau.value, Cslib.LTL.Tableau.obligationCount, Cslib.LTL.Tableau.step, Cslib.LTL.Tableau.obligation, Cslib.LTL.Tableau.Fair, Cslib.LTL.Tableau.automaton, Cslib.LTL.Tableau.fair_iff
statement: formalized
proof: formalized
---

# Model checking for linear temporal logic

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html).

## Truth-annotation states of the LTL tableau

One Boolean for each syntactic occurrence in an LTL formula.

Formalized by `Cslib.LTL.Tableau.State`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#state).

## Root truth bit of a tableau annotation

The truth bit at the root of an annotation.

Formalized by `Cslib.LTL.Tableau.value`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#value).

## Number of until fairness obligations

The number of until occurrences, hence of fairness requirements.

Formalized by `Cslib.LTL.Tableau.obligationCount`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#obligation-count).

## Local transition relation of the LTL tableau

Local equations at every occurrence. The symbol labels the source state.

Formalized by `Cslib.LTL.Tableau.step`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#step).

## Boolean test for an until fairness obligation

The Boolean test for each until fairness requirement.

Formalized by `Cslib.LTL.Tableau.obligation`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#obligation).

## Fairness of a tableau annotation sequence

Every until occurrence is absent or fulfilled at arbitrarily late times.

Formalized by `Cslib.LTL.Tableau.Fair`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#fair).

## Generalized Büchi tableau for an LTL formula

Generalized Büchi tableau: the root is initially true.

Formalized by `Cslib.LTL.Tableau.automaton`, a definition declared in [CSLibExt/Logics/LTL/Tableau.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#automaton).

## Tableau fairness is generalized Büchi acceptance

Structural fairness is exactly generalized Büchi acceptance.

Formalized by `Cslib.LTL.Tableau.fair_iff`, a theorem declared in [CSLibExt/Logics/LTL/Tableau.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#fair-iff).

## Tableau acceptance via initial, local and fairness conditions

Membership exposes exactly the initial, local, and fairness conditions.

Formalized by `Cslib.LTL.Tableau.mem_language_iff`, a theorem declared in [CSLibExt/Logics/LTL/Tableau.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/Tableau.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#mem-language-iff).

## LTL tableau accepts exactly the satisfying words

The full tableau recognizes exactly the existing LTL satisfaction relation.

Formalized by `Cslib.LTL.Tableau.mem_automaton_iff`, a theorem declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#mem-automaton-iff).

## Generalized LTL tableau language equals the formula language

Exact omega-language equality for the generalized tableau.

Formalized by `Cslib.LTL.Tableau.language_automaton`, a theorem declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#language-automaton).

## Büchi automaton for an LTL formula

Ordinary Büchi recognition, using the existing fairness counter.

Formalized by `Cslib.LTL.Tableau.buchi`, a definition declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#buchi).

## Büchi automaton language equals the LTL formula language

Every LTL formula has precisely its existing language as a Büchi language.

Formalized by `Cslib.LTL.Tableau.language_buchi`, a theorem declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#language-buchi).

## Büchi automaton accepts exactly the satisfying words

The ordinary Büchi recognizer accepts exactly satisfaction of the formula.

Formalized by `Cslib.LTL.Tableau.mem_buchi_iff`, a theorem declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#mem-buchi-iff).

## Every LTL formula has a finite-state Büchi automaton

Every existing LTL formula has a finite-state Büchi recognizer under the
same valuation. Neither atoms nor the alphabet need be finite or decidable.

Formalized by `Cslib.LTL.exists_buchi`, a theorem declared in [CSLibExt/Logics/LTL/FullBuchi.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/FullBuchi.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#exists-buchi).

## Initial infinite run of a transition system

An initial infinite state run, witnessed by a canonical action execution.

Formalized by `Cslib.LTL.ModelChecking.IsRun`, a definition declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#is-run).

## Runs are sequences with a transition between adjacent states

Equivalently, every adjacent state pair has a real model transition.

Formalized by `Cslib.LTL.ModelChecking.isRun_iff`, a theorem declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#is-run-iff).

## Product of a transition system with a Büchi recognizer

Synchronized state-reading product, with the recognizer's Büchi condition.

Formalized by `Cslib.LTL.ModelChecking.product`, a definition declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#product).

## Product accepts exactly the runs accepted by the recognizer

A product accepts precisely the model runs accepted by its recognizer.

Formalized by `Cslib.LTL.ModelChecking.mem_product_iff`, a theorem declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#mem-product-iff).

## Counterexample product for an LTL formula

The finite-state product for runs that violate the full LTL formula.

Formalized by `Cslib.LTL.ModelChecking.counterexample`, a definition declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#counterexample).

## Satisfaction of an LTL formula by all initial runs

All initial infinite canonical executions satisfy the formula.

Formalized by `Cslib.LTL.ModelChecking.Models`, a definition declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#models).

## Counterexample words are runs violating the formula

A counterexample word is exactly an infinite model run violating LTL.

Formalized by `Cslib.LTL.ModelChecking.mem_counterexample_iff`, a theorem declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#mem-counterexample-iff).

## Finite-model LTL satisfaction iff no counterexample lasso

Full-LTL model checking reduces to the proved finite Büchi lasso criterion.
A cycle must be nonempty; neither seriality nor finite action/atom types are needed.

Formalized by `Cslib.LTL.ModelChecking.models_iff_no_lasso`, a theorem declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#models-iff-no-lasso).

## LTL satisfaction iff the counterexample language is empty

Universal infinite-run satisfaction is emptiness of the counterexample language.

Formalized by `Cslib.LTL.ModelChecking.models_iff_language_empty`, a theorem declared in [CSLibExt/Logics/LTL/ModelChecking.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/ModelChecking.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#models-iff-language-empty).

## Computable fairness-counter update

Computable fairness-counter update, reading the destination annotation.

Formalized by `Cslib.LTL.Tableau.advance`, a definition declared in [CSLibExt/Logics/LTL/DecidableModelChecking.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/DecidableModelChecking.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#advance).

## Computable counter update equals generic degeneralization

The computable update is exactly the existing generic degeneralization.

Formalized by `Cslib.LTL.Tableau.nextCount_eq_advance`, a theorem declared in [CSLibExt/Logics/LTL/DecidableModelChecking.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/DecidableModelChecking.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#next-count-eq-advance).

## Büchi transition test via the computable counter update

The existing Büchi transition can be tested using the computable update.

Formalized by `Cslib.LTL.Tableau.buchi_tr_iff`, a theorem declared in [CSLibExt/Logics/LTL/DecidableModelChecking.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/DecidableModelChecking.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#buchi-tr-iff).

## Executable full-LTL model checker

Full-LTL checking by the existing finite Büchi reachability algorithm.
The finite/decidable data requirements are only for execution, not recognition.

Formalized by `Cslib.LTL.ModelChecking.checkB`, a definition declared in [CSLibExt/Logics/LTL/DecidableModelChecking.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/DecidableModelChecking.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#check-b).

## Correctness of the executable LTL model checker

The executable checker is correct for all initial infinite model runs.

Formalized by `Cslib.LTL.ModelChecking.checkB_iff`, a theorem declared in [CSLibExt/Logics/LTL/DecidableModelChecking.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/LTL/DecidableModelChecking.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html#check-b-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Model checking for linear temporal logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/temporal-logic/model-checking-for-linear-temporal-logic)
