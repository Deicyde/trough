---
declaration: section
origin: cited
lean: Cslib.Algorithms.SAT.Horn.IsHorn, Cslib.Algorithms.SAT.Horn.bodyIn, Cslib.Algorithms.SAT.Horn.derive, Cslib.Algorithms.SAT.Horn.close, Cslib.Algorithms.SAT.Horn.leastModel, Cslib.Algorithms.SAT.Horn.leastModel_le, Cslib.Algorithms.SAT.Horn.satisfies_leastModel_iff, Cslib.Algorithms.SAT.Horn.hornSat
statement: formalized
proof: formalized
---

# Horn satisfiability

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html).

## Horn formula

A CNF formula is a Horn formula when every clause contains at most one
distinct positive literal.

Formalized by `Cslib.Algorithms.SAT.Horn.IsHorn`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#is-horn).

## Body of a clause contained in a set

For a finite set $T$ of variables and a CNF
clause $C$, this Boolean test is true exactly when every negative literal of $C$ has its
variable in $T$.

Formalized by `Cslib.Algorithms.SAT.Horn.bodyIn`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#body-in).

## Forward-chaining step

For a CNF formula $\varphi$ and a finite set $T$ of variables,
the derived set consists of the variables $x$ such that some clause of $\varphi$ contains the
positive literal $x$ and has every one of its negative literals on a variable in $T$.

Formalized by `Cslib.Algorithms.SAT.Horn.derive`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#derive).

## Forward-chaining closure

For a CNF formula $\varphi$ and a finite set $T$ of
variables, the closure of $T$ is computed by iterating the forward-chaining step of $\varphi$:
if every variable derived from $T$ already lies in $T$, the closure is $T$; otherwise it is the
closure of the union of $T$ with the derived variables.

The iteration terminates because each step that does not stop adds a variable of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.Horn.close`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#close).

## Least model candidate

For a CNF formula $\varphi$, the least model candidate is the
assignment that makes a variable true exactly when it lies in the forward-chaining closure of
the empty set under $\varphi$.

Formalized by `Cslib.Algorithms.SAT.Horn.leastModel`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#least-model).

## On Horn formulas, the least model candidate lies below every model

Let $\varphi$ be a
Horn CNF formula and $\sigma$ an assignment satisfying $\varphi$. Every variable that the least
model candidate of $\varphi$ makes true is also true under $\sigma$.

Formalized by `Cslib.Algorithms.SAT.Horn.leastModel_le`, a theorem declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#least-model-le).

## Horn satisfiability via the least model

A Horn CNF formula $\varphi$ is satisfiable if
and only if its least model candidate satisfies $\varphi$.

Formalized by `Cslib.Algorithms.SAT.Horn.satisfies_leastModel_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#satisfies-least-model-iff).

## Horn satisfiability test

For a CNF formula $\varphi$, the Horn satisfiability test
returns the Boolean truth value of $\varphi$ under its least model candidate.

Formalized by `Cslib.Algorithms.SAT.Horn.hornSat`, a definition declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#horn-sat).

## Correctness of the Horn satisfiability test

If $\varphi$ is a Horn CNF formula, then
the Horn satisfiability test returns true on $\varphi$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Algorithms.SAT.Horn.hornSat_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/Horn/Basic.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/Horn/Basic.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html#horn-sat-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Horn satisfiability](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/horn-satisfiability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/propositional-logic/horn-satisfiability)
