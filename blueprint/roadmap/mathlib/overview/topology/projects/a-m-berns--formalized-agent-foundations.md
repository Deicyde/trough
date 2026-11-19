---
declaration: lemma
origin: cited
lean: FactoredSpaces.structIndepGiven_iff_forall_condIndepVar_of_nonempty, FactoredSpaces.structIndepGiven_iff_forall_condIndepVar, FactoredSpaces.condIndepVar_of_structIndepGiven, FactoredSpaces.structIndepGiven_of_forall_condIndepVar, FactoredSpaces.structIndepGiven_of_open
statement: formalized
proof: formalized
---

# Formalized Agent Foundations

[A-M-Berns/Formalized-Agent-Foundations](https://github.com/A-M-Berns/Formalized-Agent-Foundations) at commit [857e901d](https://github.com/A-M-Berns/Formalized-Agent-Foundations/tree/857e901dccf0021a7a0db9515caab76f3828c8f3), 2026-11-09.

> Lean 4 formalizations of important papers in agent foundations and open-source game theory, built on [Mathlib](https://github.com/leanprover-community/mathlib4) and the [Foundation](https://github.com/FormalizedFormalLogic/Foundation) library of the Formalized Formal Logic project.

*Quoted from [README.md](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/README.md), Apache-2.0.*

## Depends on

- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Kleene's recursion theorem](../../../thousand-plus/general-topics-history-and-foundations/kleenes-recursion-theorem.md)
- [Conditional expectation](../../probability-theory/definitions-in-probability-theory/conditional-expectation.md)
- [Szpilrajn extension theorem](../../../thousand-plus/general-topics-history-and-foundations/szpilrajn-extension-theorem.md)
- [In terms of general recursive functions](../../logic-and-computation/computability/computable-function/in-terms-of-general-recursive-functions.md)
- [Primitive recursive function](../../logic-and-computation/computability/primitive-recursive-function.md)
- [Hilbert projection theorem](../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Geometric law](../../probability-theory/random-variables-and-their-laws/geometric-law.md)
- [Conditional probability](../../probability-theory/definitions-in-probability-theory/conditional-probability.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`FactoredSpaces.structIndepGiven_iff_forall_condIndepVar_of_nonempty`](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/FactoredSpaces/MainTheorem.lean#L19) (lemma)
- [`FactoredSpaces.structIndepGiven_iff_forall_condIndepVar`](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/FactoredSpaces/MainTheorem.lean#L63) (theorem)
- [`FactoredSpaces.condIndepVar_of_structIndepGiven`](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/FactoredSpaces/MainTheorem.lean#L82) (lemma)
- [`FactoredSpaces.structIndepGiven_of_forall_condIndepVar`](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/FactoredSpaces/MainTheorem.lean#L91) (lemma)
- [`FactoredSpaces.structIndepGiven_of_open`](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/FactoredSpaces/MainTheorem.lean#L102) (theorem)

No file its headlines import, directly or not (8 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.31.0, Mathlib at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- 348 .lean files; its Lean libraries `ModalAgents`, `LogicalInduction`, `CartesianFrames`, `FiniteFactoredSets`, `Condensation`, `FactoredSpaces` and 7 more hold 347, declaring 12,658 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/A-M-Berns/Formalized-Agent-Foundations/blob/857e901dccf0021a7a0db9515caab76f3828c8f3/LICENSE)).

## Builds on

- Mathlib, at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- `complexitylib` (https://github.com/A-M-Berns/complexitylib) at `1b0d1075`.
- `EconCSLib` (https://github.com/gametheoryinlean/EconCSLib) at `55229910`.
- `Foundation` (https://github.com/FormalizedFormalLogic/Foundation) at `41d20b51`.

## Placement

Of its imports of Mathlib modules in an overview area, 32 of 201 are in Topology, 2.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (32 of 201 imports, 2.1×), Data structures (31 of 201 imports, 1.1×), Analysis (45 of 201 imports, 0.8×). *Proof depends on* lists 8 of the 54 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [A-M-Berns/Formalized-Agent-Foundations at 857e901d](https://github.com/A-M-Berns/Formalized-Agent-Foundations/tree/857e901dccf0021a7a0db9515caab76f3828c8f3)
