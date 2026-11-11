---
declaration: section
origin: cited
lean: Cslib.Modal.ModalRelations, Cslib.Modal.modalLanguage, Cslib.Modal.FrameRelations, Cslib.Modal.frameLanguage, Cslib.Modal.kripkeStructure, Cslib.Modal.frameStructure, Cslib.Modal.standardTranslation, Cslib.Modal.realize_standardTranslation
statement: formalized
proof: formalized
---

# Standard translation of modal logic

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html).

## Relation symbols of the modal first-order language

Relation symbols of the modal first-order language: accessibility `R` (binary) and a
unary predicate `P_a` for each atom `a`.

Formalized by `Cslib.Modal.ModalRelations`, an inductive type declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#modal-relations).

## The first-order modal language

For a set of atoms, the first-order language of modal
logic has no function symbols; its relation symbols are a binary symbol $R$ (accessibility)
and a unary symbol $P_a$ for each atom $a$.

Formalized by `Cslib.Modal.modalLanguage`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#modal-language).

## Relation symbols of the frame language

The relation symbols of the first-order frame
language, indexed by arity: a single binary symbol $R$ for accessibility, and no symbols of any
other arity.

Formalized by `Cslib.Modal.FrameRelations`, an inductive type declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#frame-relations).

## First-order language of Kripke frames

The first-order language of frames: no function symbols, one binary relation `R`.

Formalized by `Cslib.Modal.frameLanguage`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#frame-language).

## A Kripke model as a first-order structure

A Kripke model $M$ with set of worlds $W$
makes $W$ a structure for the modal language: the accessibility symbol $R$ is interpreted as
the accessibility relation of $M$, and the predicate $P_a$ for an atom $a$ holds at exactly
the worlds where $a$ is true under the valuation of $M$.

Formalized by `Cslib.Modal.kripkeStructure`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#kripke-structure).

## A frame as a first-order structure

A binary relation $r$ on a set $W$ (a bare Kripke
frame) makes $W$ a structure for the frame language, in which the accessibility symbol $R$ is
interpreted as $r$: $R(w, w')$ holds if and only if $r(w, w')$.

Formalized by `Cslib.Modal.frameStructure`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#frame-structure).

## Standard translation

For $n$ variables $x_0, \dots, x_{n-1}$ in scope and a term $t$
of the modal language for the current world, the standard translation $ST_t(\varphi)$ of a
modal formula $\varphi$ is the first-order formula over the modal language in these variables
defined by recursion on $\varphi$: $ST_t(a) = P_a(t)$ for an atom $a$; $ST_t(\bot) = \bot$;
$ST_t(\varphi \to \psi) = ST_t(\varphi) \to ST_t(\psi)$; and
$ST_t(\Box \varphi) = \forall x_n \, (R(t, x_n) \to ST_{x_n}(\varphi))$, where $x_n$ is a fresh
variable and $ST_{x_n}(\varphi)$ is taken with $n + 1$ variables in scope.

Formalized by `Cslib.Modal.standardTranslation`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#standard-translation).

## Correctness of the standard translation

Let $M$ be a Kripke model with set of worlds
$W$, viewed as a structure for the modal language. For every $n$, every term $t$ of the modal
language in the variables $x_0, \dots, x_{n-1}$, every modal formula $\varphi$ and every
assignment of worlds in $W$ to $x_0, \dots, x_{n-1}$, the standard translation of $\varphi$
with $n$ variables in scope and current-world term $t$ holds in $M$ under this assignment if
and only if $\varphi$ is satisfied in $M$ at the world that $t$ denotes under the
assignment.

Formalized by `Cslib.Modal.realize_standardTranslation`, a theorem declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#realize-standard-translation).

## Bisimulation-invariant formulas

A first-order formula $\alpha$ over the modal language,
with one variable $x$ and no other free variables, is bisimulation-invariant if for all Kripke
models $M$ and $N$ over the same atoms, every bisimulation $Z$ between $M$ and $N$ and all
worlds $w$ of $M$ and $v$ of $N$ with $Z(w, v)$, the formula $\alpha$ holds in $M$ (viewed as
a structure for the modal language) at $x = w$ if and only if it holds in $N$ at $x = v$.

Formalized by `Cslib.Modal.BisimulationInvariant`, a definition declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#bisimulation-invariant).

## Modal formulas are bisimulation-invariant under the standard translation

For every
modal formula $\varphi$, its standard translation $ST_x(\varphi)$ (the first-order formula over
the modal language whose single variable $x$ stands for the current world) is
bisimulation-invariant: for all Kripke models $M$ and $N$, every bisimulation $Z$ between $M$
and $N$ and all worlds $w$ of $M$ and $v$ of $N$ with $Z(w, v)$, the formula $ST_x(\varphi)$
holds in $M$ at $x = w$ if and only if it holds in $N$ at $x = v$.

Formalized by `Cslib.Modal.bisimulationInvariant_standardTranslation`, a theorem declared in [CSLibExt/Logics/Modal/StandardTranslation.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/StandardTranslation.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html#bisimulation-invariant-standard-translat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Standard translation of modal logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/standard-translation-of-modal-logic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/modal-logic/standard-translation-of-modal-logic)
