---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.Term, Cslib.AutomatedReasoning.StringConstraints.eval, Cslib.AutomatedReasoning.StringConstraints.varsOf, Cslib.AutomatedReasoning.StringConstraints.eval_eq_of_agree_on_vars, Cslib.AutomatedReasoning.StringConstraints.Atom, Cslib.AutomatedReasoning.StringConstraints.varsOfAtom, Cslib.AutomatedReasoning.StringConstraints.Formula, Cslib.AutomatedReasoning.StringConstraints.andChain
statement: formalized
proof: formalized
---

# String constraints: syntax and semantics

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html).

## String term over variables

A **string term** over variables `V`: a constant word, a variable,
the concatenation of two terms, or a letter-to-word morphism applied
to a term.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.Term`, an inductive type declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#term).

## Evaluation of a string term under an assignment

Evaluation of a term under an assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.eval`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#eval).

## Variables occurring in a string term

The variables occurring in a term, as a list (duplicates allowed).

Formalized by `Cslib.AutomatedReasoning.StringConstraints.varsOf`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#vars-of).

## String term evaluation depends only on its variables

Evaluation depends only on the values of the variables in the term.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.eval_eq_of_agree_on_vars`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#eval-eq-of-agree-on-vars).

## String constraint atom

A **string atom**: a word equation, a regular-membership test, or a
length bound. Regular languages are represented by the existing
`Cslib.Language.EncodedRegex`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.Atom`, an inductive type declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#atom).

## Variables occurring in a string atom

The variables occurring in an atom.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.varsOfAtom`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#vars-of-atom).

## String formulas

Positive Boolean combinations of atoms
(conjunction, disjunction, `true`, `false`; no negation), as in the
positive fragment of SMT-LIB assertions.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.Formula`, an inductive type declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#formula).

## Conjunction of a list of string formulas

Conjunction of a list of formulas.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.andChain`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#and-chain).

## Disjunction of a list of string formulas

Disjunction of a list of formulas.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.orChain`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#or-chain).

## Variables occurring in a string formula

The variables occurring in a formula.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.varsOfFormula`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#vars-of-formula).

## Satisfaction of a string atom

Satisfaction of an atom under an assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.SatAtom`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-atom).

## Satisfaction of a string formula

Satisfaction of a formula under an assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.Sat`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat).

## Satisfaction of a conjunction chain

Satisfaction of a conjunction chain: every member is satisfied.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sat_andChain`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-and-chain).

## Satisfaction of a disjunction chain

Satisfaction of a disjunction chain: one member is satisfied.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sat_orChain`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-or-chain).

## Atom satisfaction depends only on its variables

Satisfaction of an atom depends only on the values of its variables.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.satAtom_congr`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-atom-congr).

## Formula satisfaction depends only on its variables

Satisfaction depends only on the values of the variables in the formula.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sat_congr`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-congr).

## Boolean checker for atom satisfaction

Boolean checker for atom satisfaction. Regular membership uses
`EncodedRegex.memB`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.satAtomB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-atom-b).

## Correctness of the Boolean atom checker

The Boolean checker is correct.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.satAtomB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-atom-b-iff).

## Boolean checker for formula satisfaction

Boolean checker for formula satisfaction.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.satB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-b).

## Correctness of the Boolean formula checker

The Boolean checker is correct.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.satB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Syntax.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html#sat-b-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: String constraints: syntax and semantics](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/string-constraints-syntax-and-semantics)
