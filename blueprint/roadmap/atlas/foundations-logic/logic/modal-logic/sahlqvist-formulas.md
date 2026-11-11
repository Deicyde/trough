---
declaration: section
origin: cited
lean: Cslib.Modal.IsPositive, Cslib.Modal.IsNegative, Cslib.Modal.boxPow, Cslib.Modal.IsSahlqvistAntecedent, Cslib.Modal.Formula.atoms, Cslib.Modal.IsSahlqvistImplication, Cslib.Modal.IsSahlqvist, Cslib.Modal.isSahlqvist_axiomB
statement: formalized
proof: formalized
---

# Sahlqvist formulas

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html).

## Positive modal formulas

Positive and negative modal formulas are defined by simultaneous
recursion: every atom is positive, $\bot$ is positive, $\varphi \to \psi$ is positive if
$\varphi$ is negative and $\psi$ is positive, and $\Box\varphi$ is positive if $\varphi$ is
positive.

Positive formulas are closed under $\wedge$, $\vee$, $\Box$ and $\Diamond$, which are encoded
through $\to$, $\bot$ and $\Box$.

Formalized by `Cslib.Modal.IsPositive`, a definition declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-positive).

## Negative modal formulas

Negative and positive modal formulas are defined by simultaneous
recursion: no atom is negative, $\bot$ is negative, $\varphi \to \psi$ is negative if $\varphi$
is positive and $\psi$ is negative, and $\Box\varphi$ is negative if $\varphi$ is negative.

Negative formulas are closed under $\wedge$, $\vee$, $\Box$ and $\Diamond$, which are encoded
through $\to$, $\bot$ and $\Box$.

Formalized by `Cslib.Modal.IsNegative`, a definition declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-negative).

## Iterated box

For a natural number $k$ and a modal formula $\varphi$, the iterated box
$\Box^k \varphi$ is defined by $\Box^0 \varphi = \varphi$ and
$\Box^{k+1} \varphi = \Box\,\Box^k \varphi$.

Formalized by `Cslib.Modal.boxPow`, a definition declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#box-pow).

## Sahlqvist antecedents

The Sahlqvist antecedents form the smallest class of modal
formulas that contains every boxed atom $\Box^k p$ (an atom $p$ under $k \ge 0$ boxes) and every
negative formula, and is closed under $\wedge$, $\vee$ and $\Diamond$.

Formalized by `Cslib.Modal.IsSahlqvistAntecedent`, an inductive type declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-sahlqvist-antecedent).

## Atoms of a modal formula

The set of atoms (propositional variables) occurring in a modal
formula.

Formalized by `Cslib.Modal.Formula.atoms`, a definition declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#atoms).

## Sahlqvist implications

A modal formula is a Sahlqvist implication if it is an implication
$\alpha \to \beta$ whose antecedent $\alpha$ is a Sahlqvist antecedent and whose consequent
$\beta$ is a positive formula.

Formalized by `Cslib.Modal.IsSahlqvistImplication`, a definition declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-sahlqvist-implication).

## Sahlqvist formulas

The Sahlqvist formulas form the smallest class of modal formulas that
contains every Sahlqvist implication, is closed under $\wedge$ and $\Box$, and contains
$\varphi \vee \psi$ whenever $\varphi$ and $\psi$ are Sahlqvist formulas with no atom in common.

The side condition on disjunction is essential: arbitrary disjunction leaves the correspondence
class. $\Diamond$ is not part of this outer closure; it belongs to the grammar of Sahlqvist
antecedents. For example, the boxed Sahlqvist implication $\Box(p \to \Box\Diamond p)$ is a
Sahlqvist formula.

Formalized by `Cslib.Modal.IsSahlqvist`, an inductive type declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-sahlqvist).

## The B axiom is a Sahlqvist formula

For every atom $p$, the instance $p \to \Box\Diamond p$
of the B axiom is a Sahlqvist formula: its antecedent $p$ is a boxed atom with zero boxes and its
consequent $\Box\Diamond p$ is positive.

Formalized by `Cslib.Modal.isSahlqvist_axiomB`, a theorem declared in [CSLibExt/Logics/Modal/Sahlqvist.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Sahlqvist.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html#is-sahlqvist-axiom-b).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sahlqvist formulas](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/sahlqvist-formulas/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/modal-logic/sahlqvist-formulas)
