---
declaration: section
origin: cited
lean: Cslib.Epistemic.Model, Cslib.Epistemic.Formula, Cslib.Epistemic.Formula.not, Cslib.Epistemic.Formula.or, Cslib.Epistemic.Sat, Cslib.Epistemic.Valid, Cslib.Epistemic.not_valid_bot, Cslib.Epistemic.sat_or
statement: formalized
proof: formalized
---

# Epistemic logic

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html).

## Epistemic

## Epistemic models

Given a type of worlds $W$, a type of atoms and a type of agents, an
epistemic model consists of a binary accessibility relation $R_i$ on $W$ for each agent $i$ and a
valuation assigning to each world the atoms true there; the world type $W$ is required to be
nonempty.

Nonemptiness is assumed as for Kripke models: with no worlds, validity would hold vacuously and
even $\bot$ would be valid.

Formalized by `Cslib.Epistemic.Model`, a structure declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#model).

## Epistemic formulas

Given a type of atoms and a type of agents, the formulas of epistemic
logic are built inductively: every atom $p$ is a formula, falsity $\bot$ is a formula, if $\varphi$
and $\psi$ are formulas then so is the implication $\varphi \to \psi$, and if $\varphi$ is a
formula and $i$ is an agent then $K_i \varphi$ (read "agent $i$ knows $\varphi$") is a formula.

Formalized by `Cslib.Epistemic.Formula`, an inductive type declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#formula).

## Negation of epistemic formulas

The negation $\neg\varphi$ of an epistemic formula
$\varphi$ is the implication $\varphi \to \bot$.

Formalized by `Cslib.Epistemic.Formula.not`, a definition declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#not).

## Disjunction of epistemic formulas

The disjunction $\varphi \lor \psi$ of epistemic
formulas $\varphi$ and $\psi$ is the implication $\neg\varphi \to \psi$.

Formalized by `Cslib.Epistemic.Formula.or`, a definition declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#or).

## Satisfaction in an epistemic model

Satisfaction of an epistemic formula at a world $w$
of a model $M$ is defined by recursion on the formula, writing $R_i$ for the accessibility
relation of agent $i$ in $M$ and $K_i \varphi$ for the formula "agent $i$ knows $\varphi$": an
atom $a$ holds at $w$ when the valuation of $M$ makes $a$ true at $w$; $\bot$ holds at no world;
$\varphi \to \psi$ holds at $w$ when $\psi$ holds at $w$ whenever $\varphi$ does; and
$K_i \varphi$ holds at $w$ when $\varphi$ holds at every world $v$ with $w \mathrel{R_i} v$.

Formalized by `Cslib.Epistemic.Sat`, a definition declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#sat).

## Validity in an epistemic model

A formula $\varphi$ is valid in an epistemic model $M$
when $\varphi$ is satisfied at every world of $M$.

Formalized by `Cslib.Epistemic.Valid`, a definition declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#valid).

## Falsity is not valid in an epistemic model

In every epistemic model, the formula $\bot$
is not valid: it fails at some world.

The nonempty world set rules out vacuous validity.

Formalized by `Cslib.Epistemic.not_valid_bot`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#not-valid-bot).

## Satisfaction of a disjunction

In an epistemic model $M$, the disjunction
$\varphi \lor \psi$ of two formulas, defined as $\neg \varphi \to \psi$, is satisfied at a world
$w$ if and only if $\varphi$ is satisfied at $w$ or $\psi$ is satisfied at $w$.

Formalized by `Cslib.Epistemic.sat_or`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#sat-or).

## Distribution axiom K

Write $K_i \varphi$ for "agent $i$ knows $\varphi$". For every
epistemic model $M$, every agent $i$ and all formulas $\varphi$ and $\psi$, the formula
$K_i (\varphi \to \psi) \to (K_i \varphi \to K_i \psi)$ is valid in $M$: knowledge distributes
over implication.

Formalized by `Cslib.Epistemic.valid_know_dist`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#valid-know-dist).

## Truth axiom T

Write $K_i \varphi$ for "agent $i$ knows $\varphi$". Let $M$ be an
epistemic model in which the accessibility relation $R_i$ of agent $i$ is reflexive. Then for
every formula $\varphi$, the formula $K_i \varphi \to \varphi$ is valid in $M$.

Formalized by `Cslib.Epistemic.valid_know_truth`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#valid-know-truth).

## Positive introspection axiom 4

Write $K_i \varphi$ for "agent $i$ knows $\varphi$".
Let $M$ be an epistemic model in which the accessibility relation $R_i$ of agent $i$ is
transitive. Then for every formula $\varphi$, the formula $K_i \varphi \to K_i K_i \varphi$ is
valid in $M$.

Formalized by `Cslib.Epistemic.valid_know_pos`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#valid-know-pos).

## Negative introspection axiom 5

Write $K_i \varphi$ for "agent $i$ knows $\varphi$".
Let $M$ be an epistemic model in which the accessibility relation $R_i$ of agent $i$ is
euclidean: for all worlds $a$, $b$, $c$, if $a \mathrel{R_i} b$ and $a \mathrel{R_i} c$ then
$b \mathrel{R_i} c$. Then for every formula $\varphi$, the formula
$\neg K_i \varphi \to K_i \neg K_i \varphi$ is valid in $M$.

Formalized by `Cslib.Epistemic.valid_know_neg`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#valid-know-neg).

## The two-agent coin model

The epistemic model whose worlds are the two booleans, with
$\mathrm{true}$ read as heads and $\mathrm{false}$ as tails, with a single atom $p$ true exactly
at the heads world, and with two agents $0$ and $1$: agent $0$ sees the coin, so its
accessibility relation is equality of worlds, and agent $1$ does not, so its accessibility
relation relates every pair of worlds.

Formalized by `Cslib.Epistemic.muddy`, a definition declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#muddy).

## Agent 0 knows the coin is heads exactly at heads

Let $p$ be the atom "the coin is heads"
of the two-agent coin model. At a world $v$ of that model, the formula $K_0 p$ holds if and only
if $v$ is the heads world: agent $0$ sees the coin.

Formalized by `Cslib.Epistemic.sat_know_zero_atom`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#sat-know-zero-atom).

## Agent 0 knows the coin is tails exactly at tails

Let $p$ be the atom "the coin is heads"
of the two-agent coin model. At a world $v$ of that model, the formula $K_0 \neg p$ holds if and
only if $v$ is the tails world.

Formalized by `Cslib.Epistemic.sat_know_zero_not_atom`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#sat-know-zero-not-atom).

## Agent 1 does not know that the coin is heads

Let $p$ be the atom "the coin is heads" of
the two-agent coin model. The formula $K_1 p$ is false at the heads world: agent $1$ considers
the tails world possible.

Formalized by `Cslib.Epistemic.muddy_not_know_one_p_true`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#muddy-not-know-one-p-true).

## Agent 1 knows that agent 0 knows whether the coin is heads

Let $p$ be the atom "the coin
is heads" of the two-agent coin model. At every world of that model the formula
$K_1(K_0 p \lor K_0 \neg p)$ holds: agent $1$ knows that agent $0$ either knows $p$ or knows
$\neg p$.

Formalized by `Cslib.Epistemic.muddy_know_one_knows_whether`, a theorem declared in [CSLibExt/Logics/Epistemic/Basic.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Epistemic/Basic.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html#muddy-know-one-knows-whether).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Epistemic logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/epistemic-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/epistemic-logic)
