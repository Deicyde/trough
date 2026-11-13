---
declaration: section
origin: cited
lean: Cslib.PDL.Model, Cslib.PDL.Formula, Cslib.PDL.Program, Cslib.PDL.Formula.dia, Cslib.PDL.ProgRel, Cslib.PDL.Sat, Cslib.PDL.sat_box_seq, Cslib.PDL.sat_box_choice
statement: formalized
proof: formalized
---

# Propositional dynamic logic (PDL)

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html).

## PDL model

A model of propositional dynamic logic with set of worlds $W$ consists of a
binary accessibility relation $R_a$ on $W$ for each atomic action label $a$, and a valuation that
says which atoms are true at each world.

Formalized by `Cslib.PDL.Model`, a structure declared in [CSLibExt/Logics/PDL/Basic.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#model).

## PDL formulas

The formulas of propositional dynamic logic over a type of atoms and a type
of atomic action labels are the atoms $p$, falsity $\bot$, implications $\varphi \to \psi$ of
formulas, and boxes $[\alpha]\varphi$ of a program $\alpha$ and a formula $\varphi$. Formulas and
programs are defined by simultaneous induction.

Formalized by `Cslib.PDL.Formula`, an inductive type declared in [CSLibExt/Logics/PDL/Basic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#formula).

## PDL programs

The programs of propositional dynamic logic over a type of atoms and a type
of atomic action labels are the atomic actions $a$, sequential compositions $\alpha ; \beta$,
nondeterministic choices $\alpha \cup \beta$, iterations $\alpha^*$, and tests $\varphi?$ of a
formula $\varphi$. Programs and formulas are defined by simultaneous induction.

Formalized by `Cslib.PDL.Program`, an inductive type declared in [CSLibExt/Logics/PDL/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#program).

## Possibility in PDL

For a program $\alpha$ and a formula $\varphi$, the formula
$\langle\alpha\rangle\varphi$ is defined as $[\alpha](\varphi \to \bot) \to \bot$, that is, as
$\neg[\alpha]\neg\varphi$: possibility is the dual of necessity.

Formalized by `Cslib.PDL.Formula.dia`, a definition declared in [CSLibExt/Logics/PDL/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#dia).

## Relation denoted by a PDL program

In a model $M$, each program $\alpha$ denotes a binary
relation $R_\alpha$ on worlds: an atomic action $a$ denotes its accessibility relation $R_a$;
$(w, v) \in R_{\alpha;\beta}$ iff $(w, u) \in R_\alpha$ and $(u, v) \in R_\beta$ for some world
$u$; $R_{\alpha \cup \beta} = R_\alpha \cup R_\beta$; $R_{\alpha^*}$ is the reflexive-transitive
closure of $R_\alpha$; and $(w, v) \in R_{\varphi?}$ iff $w = v$ and $\varphi$ holds at $w$ in
$M$.

Formalized by `Cslib.PDL.ProgRel`, a definition declared in [CSLibExt/Logics/PDL/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#prog-rel).

## Satisfaction of PDL formulas

Truth of a formula at a world $w$ of a model $M$ is defined
by recursion: an atom $p$ holds at $w$ iff the valuation of $M$ makes $p$ true at $w$; $\bot$
holds nowhere; $\varphi \to \psi$ holds at $w$ iff $\psi$ holds at $w$ whenever $\varphi$ does;
and $[\alpha]\varphi$ holds at $w$ iff $\varphi$ holds at every world $v$ with
$(w, v) \in R_\alpha$, where $R_\alpha$ is the relation denoted by $\alpha$ in $M$.

Formalized by `Cslib.PDL.Sat`, a definition declared in [CSLibExt/Logics/PDL/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#sat).

## Box of a sequential composition

For every model $M$, world $w$, programs $\alpha$ and
$\beta$, and formula $\varphi$, the formula $[\alpha;\beta]\varphi$ holds at $w$ if and only if
$[\alpha][\beta]\varphi$ holds at $w$.

Formalized by `Cslib.PDL.sat_box_seq`, a theorem declared in [CSLibExt/Logics/PDL/Basic.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#sat-box-seq).

## Box of a choice

For every model $M$, world $w$, programs $\alpha$ and $\beta$, and formula
$\varphi$, the formula $[\alpha \cup \beta]\varphi$ holds at $w$ if and only if both
$[\alpha]\varphi$ and $[\beta]\varphi$ hold at $w$.

Formalized by `Cslib.PDL.sat_box_choice`, a theorem declared in [CSLibExt/Logics/PDL/Basic.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#sat-box-choice).

## Unfolding the box of an iteration

For every model $M$, world $w$, program $\alpha$ and
formula $\varphi$, the formula $[\alpha^*]\varphi$ holds at $w$ if and only if $\varphi$ holds at
$w$ and $[\alpha][\alpha^*]\varphi$ holds at $w$.

Formalized by `Cslib.PDL.sat_box_star_unfold`, a theorem declared in [CSLibExt/Logics/PDL/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#sat-box-star-unfold).

## Box of a test

For every model $M$, world $w$ and formulas $\psi$ and $\varphi$, the formula
$[\psi?]\varphi$ holds at $w$ if and only if $\varphi$ holds at $w$ whenever $\psi$ holds at $w$.

Formalized by `Cslib.PDL.sat_box_test`, a theorem declared in [CSLibExt/Logics/PDL/Basic.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#sat-box-test).

## The toggle model

The PDL model whose worlds are the two Booleans $\mathsf{true}$ and
$\mathsf{false}$, with a single atomic action $a$ and a single atom $p$: the action $a$ relates
each world $s$ exactly to its negation $\lnot s$, and $p$ holds exactly at $\mathsf{true}$.

Formalized by `Cslib.PDL.toggleModel`, a definition declared in [CSLibExt/Logics/PDL/Basic.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#toggle-model).

## Failure of $(a;a)\,p$ in the toggle model

In the toggle model, with atomic action $a$
and atom $p$, the formula $[a;a]\,p$ is not satisfied at the world $\mathsf{false}$.

Performing $a$ twice leads from $\mathsf{false}$ back to $\mathsf{false}$, where $p$ is false.

Formalized by `Cslib.PDL.toggle_not_box_seq_atom`, a theorem declared in [CSLibExt/Logics/PDL/Basic.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Basic.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html#toggle-not-box-seq-atom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Propositional dynamic logic (PDL)](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/propositional-dynamic-logic/propositional-dynamic-logic-pdl)
