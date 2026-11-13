---
declaration: section
origin: cited
lean: Cslib.CTL.Formula, Cslib.CTL.Formula.bot, Cslib.CTL.Formula.or, Cslib.CTL.Formula.imp, Cslib.CTL.Formula.iff, Cslib.CTL.Formula.existsFinally, Cslib.CTL.Formula.forallNext, Cslib.CTL.Formula.forallFinally
statement: formalized
proof: formalized
---

# Computation tree logic

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html).

## CTL

## CTL formulas

The formulas of computation tree logic over a type $A$ of atoms are
generated as follows: every atom $a \in A$ is a formula, $\top$ is a formula, and if $\varphi$
and $\psi$ are formulas then so are the negation $\neg\varphi$, the conjunction
$\varphi \land \psi$, the existential next $\mathsf{EX}\,\varphi$, the existential until
$\mathsf{E}[\varphi\,\mathsf{U}\,\psi]$, the existential globally $\mathsf{EG}\,\varphi$ and the
universal until $\mathsf{A}[\varphi\,\mathsf{U}\,\psi]$.

The universal until is primitive rather than the classical translation through $\mathsf{EU}$
and $\mathsf{EG}$, which is unsound on transition systems with deadlocked states.

Formalized by `Cslib.CTL.Formula`, an inductive type declared in [CSLibExt/Logics/CTL/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#formula).

## Falsity in CTL

The CTL formula $\bot$ (falsity) is the negation $\neg\top$ of the formula
$\top$ (truth).

Formalized by `Cslib.CTL.Formula.bot`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#bot).

## CTL disjunction

For CTL formulas $\varphi$ and $\psi$, the disjunction
$\varphi \lor \psi$ is defined as $\neg(\neg\varphi \land \neg\psi)$.

Formalized by `Cslib.CTL.Formula.or`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#or).

## CTL implication

For CTL formulas $\varphi$ and $\psi$, the implication
$\varphi \to \psi$ is defined as the disjunction $\neg\varphi \lor \psi$.

Formalized by `Cslib.CTL.Formula.imp`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#imp).

## CTL bi-implication

For CTL formulas $\varphi$ and $\psi$, the bi-implication
$\varphi \leftrightarrow \psi$ is defined as the conjunction $(\varphi \to \psi) \land
(\psi \to \varphi)$ of the two implications.

Formalized by `Cslib.CTL.Formula.iff`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#iff).

## Exists finally

For a CTL formula $\varphi$, the formula $\mathsf{EF}\,\varphi$ is the
existential until $\mathsf{E}[\top \mathbin{\mathsf{U}} \varphi]$ with $\top$ on the left.

A state satisfies $\mathsf{EF}\,\varphi$ exactly when some state reachable from it satisfies
$\varphi$.

Formalized by `Cslib.CTL.Formula.existsFinally`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally).

## The CTL operator $\mathsf{AX}$

For a CTL formula $\varphi$, the formula
$\mathsf{AX}\,\varphi$ ("on all next states, $\varphi$") is defined as
$\neg\,\mathsf{EX}\,\neg\varphi$.

It holds at a state exactly when every successor of that state satisfies $\varphi$, so it holds
vacuously at a deadlocked state.

Formalized by `Cslib.CTL.Formula.forallNext`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-next).

## The CTL operator AF (inevitably)

`AF φ`: every maximal path reaches a state satisfying `φ`, as
`A[⊤ U φ]`.

Formalized by `Cslib.CTL.Formula.forallFinally`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-finally).

## The CTL operator $\mathrm{AG}$

For a CTL formula $\varphi$, the formula
$\mathrm{AG}\,\varphi$ is $\neg\,\mathrm{EF}\,\neg\varphi$. It holds at a state exactly when
every state reachable from it satisfies $\varphi$.

Formalized by `Cslib.CTL.Formula.forallGlobally`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-globally).

## Satisfaction of CTL formulas

Fix a labelled transition system and a valuation saying
which atoms hold at which states. Satisfaction of a CTL formula at a state $s$ is defined by
recursion on the formula. An atom $a$ holds at $s$ when the valuation makes $a$ true at $s$;
$\top$ always holds; $\neg\varphi$ holds when $\varphi$ does not; $\varphi \land \psi$ holds
when both $\varphi$ and $\psi$ hold; $\mathsf{EX}\,\varphi$ holds when there is a transition
from $s$, under some label, to a state satisfying $\varphi$; $\mathsf{E}[\varphi\,\mathsf{U}\,\psi]$
holds when some finite run $s = s_0, s_1, \dots, s_k$ has $\psi$ at $s_k$ and $\varphi$ at every
$s_j$ with $j < k$; $\mathsf{EG}\,\varphi$ holds when some infinite run $s = s_0, s_1, \dots$ has
$\varphi$ at every state; and $\mathsf{A}[\varphi\,\mathsf{U}\,\psi]$ holds when, first, every
infinite run $s = s_0, s_1, \dots$ has some $k$ with $\psi$ at $s_k$ and $\varphi$ at every $s_j$
with $j < k$, and second, every finite run $s = s_0, s_1, \dots, s_k$ whose last state $s_k$ has
no outgoing transition under any label has some $j \le k$ with $\psi$ at $s_j$ and $\varphi$ at
every $s_i$ with $i < j$.

Formalized by `Cslib.CTL.Satisfies`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#satisfies).

## Existential predecessor operator

For a labelled transition system and a predicate $Z$
on its states, a state $s$ satisfies $\mathrm{Pre}_\exists(Z)$ when some successor of $s$
satisfies $Z$: there are a label $a$ and a state $t$ satisfying $Z$ with a transition from $s$
to $t$ labelled $a$.

Formalized by `Cslib.CTL.PreExists`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#pre-exists).

## Serial transition systems

A labelled transition system is serial (total) when every
state $s$ has a successor: there are a label $a$ and a state $t$ with a transition from $s$ to
$t$ labelled $a$.

A serial system has no deadlocked states, and every maximal path in it is infinite.

Formalized by `Cslib.CTL.Serial`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#serial).

## Finite runs extend to infinite runs in serial systems

In a serial labelled transition
system, if $s_0, s_1, s_2, \dots$ is a finite run of length $k$, then there is an infinite run
$s'_0, s'_1, s'_2, \dots$ with $s'_i = s_i$ for every $i \le k$.

The extension iterates a chosen successor function from $s_k$, so it uses the axiom of choice.

Formalized by `Cslib.CTL.exists_omegaRun_extending_of_serial`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-omega-run-extending-of-serial).

## $\mathsf{EF}$ via finite runs

Let $\varphi$ be a CTL formula. In a labelled transition
system with a valuation of the atoms at its states, a state $s$ satisfies $\mathsf{EF}\,\varphi$ if
and only if there are a sequence of states $s_0, s_1, s_2, \dots$ with $s_0 = s$ and a natural
number $k$ such that the sequence is a finite run of length $k$ and $s_k$ satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsFinally_iff`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-iff).

## One-step expansion of $\mathrm{EU}$

Let $\varphi$ and $\psi$ be CTL formulas and $s$ a
state of a labelled transition system with a valuation of the atoms. Then $s$ satisfies
$\mathrm{E}[\varphi \mathbin{\mathrm{U}} \psi]$ if and only if either $s$ satisfies $\psi$, or
$s$ satisfies $\varphi$ and some successor of $s$ satisfies
$\mathrm{E}[\varphi \mathbin{\mathrm{U}} \psi]$.

Formalized by `Cslib.CTL.Satisfies.existsUntil_expansion`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-until-expansion).

## $\mathsf{EF}$ means reachability

Let $\varphi$ be a CTL formula. In a labelled transition
system with a valuation of the atoms at its states, a state $s$ satisfies $\mathsf{EF}\,\varphi$ if
and only if some state $t$ reachable from $s$ by a finite, possibly empty, sequence of transitions
satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsFinally_iff_reachable`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-iff-reachable).

## $\mathrm{AG}$ holds iff every reachable state satisfies the formula

Let $\varphi$ be a
CTL formula and $s$ a state of a labelled transition system with a valuation of the atoms.
Then $s$ satisfies $\mathrm{AG}\,\varphi$ if and only if every state $t$ reachable from $s$
(through a finite sequence of transitions, possibly empty) satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.forallGlobally_iff_reachable`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-globally-iff-reachable).

## Characterization of $\mathsf{AX}$

Let $s$ be a state of a labelled transition system
with an atom valuation, and let $\varphi$ be a CTL formula. Then $s$ satisfies
$\mathsf{AX}\,\varphi$ if and only if every state $t$ with a transition from $s$ to $t$, under
any label, satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.forallNext_iff`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-next-iff).

## Maximal-path form of $\mathrm{AF}$

Let $\varphi$ be a CTL formula and $s$ a state of a
labelled transition system with a valuation of the atoms. Then $s$ satisfies
$\mathrm{AF}\,\varphi$ if and only if both of the following hold: for every infinite run
$s_0, s_1, s_2, \dots$ with $s_0 = s$ there is some $k$ such that $s_k$ satisfies $\varphi$; and
for every finite run $s_0, s_1, s_2, \dots$ of length $k$ with $s_0 = s$ whose endpoint $s_k$
has no outgoing transition, there is some $j \le k$ such that $s_j$ satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.forallFinally_iff_omega_and_finite`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-finally-iff-omega-and-finite).

## $\mathsf{A}(\varphi\,\mathsf{U}\,\psi)$ at a deadlocked state

Let $s$ be a state of a
labelled transition system with an atom valuation, and suppose that $s$ is deadlocked: there is
no transition from $s$ under any label. Then for all CTL formulas $\varphi$ and $\psi$, $s$
satisfies $\mathsf{A}[\varphi\,\mathsf{U}\,\psi]$ if and only if $s$ satisfies $\psi$.

The infinite-run condition is vacuous, since an infinite run needs a step at index $0$, and the
constant finite run of length $0$ forces $\psi$ at $s$ itself.

Formalized by `Cslib.CTL.Satisfies.forallUntil_deadlock`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-until-deadlock).

## $\mathrm{AF}$ at a deadlocked state

Let $\varphi$ be a CTL formula and $s$ a state of a
labelled transition system with a valuation of the atoms. If $s$ has no outgoing transition,
then $s$ satisfies $\mathrm{AF}\,\varphi$ if and only if $s$ satisfies $\varphi$.

Formalized by `Cslib.CTL.Satisfies.forallFinally_deadlock`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-finally-deadlock).

## On serial systems $\mathrm{AF}$ is $\neg\mathrm{EG}\,\neg$

Let $\varphi$ be a CTL
formula and $s$ a state of a serial labelled transition system with a valuation of the atoms.
Then $s$ satisfies $\mathrm{AF}\,\varphi$ if and only if $s$ does not satisfy
$\mathrm{EG}\,\neg\varphi$.

A serial system has no deadlocked states, so every maximal path is infinite and $\mathrm{AF}$
recovers its classical form.

Formalized by `Cslib.CTL.Satisfies.forallFinally_iff_not_existsGlobally_not_of_serial`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-finally-iff-not-exists-globally-n).

## Classical form of $\mathsf{A}(\varphi\,\mathsf{U}\,\psi)$ on serial systems

Let $s$ be a
state of a serial labelled transition system with an atom valuation, and let $\varphi$ and $\psi$
be CTL formulas. Then $s$ satisfies $\mathsf{A}[\varphi\,\mathsf{U}\,\psi]$ if and only if $s$
satisfies neither $\mathsf{E}[\neg\psi\,\mathsf{U}\,(\neg\varphi \land \neg\psi)]$ nor
$\mathsf{EG}\,\neg\psi$. That is, no finite run from $s$ ends at a state satisfying
$\neg\varphi \land \neg\psi$ with $\neg\psi$ at all earlier states, and no infinite run from $s$
has $\neg\psi$ at every state.

The forward direction extends an $\mathsf{EU}$ witness to an infinite run; the backward
direction takes, on each infinite run, the least $\psi$-position and derives an $\mathsf{EU}$
witness from any earlier $\neg\varphi$-position.

Formalized by `Cslib.CTL.Satisfies.forallUntil_iff_classical_of_serial`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#forall-until-iff-classical-of-serial).

## One-step expansion of $\mathsf{EF}$

Let $\varphi$ be a CTL formula. In a labelled
transition system with a valuation of the atoms at its states, a state $s$ satisfies
$\mathsf{EF}\,\varphi$ if and only if $s$ satisfies $\varphi$ or $s$ satisfies
$\mathsf{EX}\,\mathsf{EF}\,\varphi$, that is, some successor of $s$ satisfies
$\mathsf{EF}\,\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsFinally_expansion`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-expansion).

## One-step expansion of $\mathsf{EG}$

Let $\varphi$ be a CTL formula. In a labelled
transition system with a valuation of the atoms at its states, a state $s$ satisfies
$\mathsf{EG}\,\varphi$ if and only if $s$ satisfies $\varphi$ and $s$ satisfies
$\mathsf{EX}\,\mathsf{EG}\,\varphi$, that is, some successor of $s$ satisfies
$\mathsf{EG}\,\varphi$.

Both directions are direct manipulations of infinite runs; no choice is needed.

Formalized by `Cslib.CTL.Satisfies.existsGlobally_expansion`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-globally-expansion).

## The $\mathsf{EF}$ functional

Given a labelled transition system, a valuation of the atoms
at its states, and a CTL formula $\varphi$, this is the map sending a set of states $Z$ to the set
of states that satisfy $\varphi$ or have some successor in $Z$.

Its least fixed point is the set of states satisfying $\mathsf{EF}\,\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsFinallyFun`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-fun).

## The $\mathsf{EF}$ operator

Given a labelled transition system, a valuation of the atoms at
its states, and a CTL formula $\varphi$, this is the monotone operator on sets of states, ordered by
inclusion, sending a set $Z$ to the set of states that satisfy $\varphi$ or have some successor in
$Z$.

Formalized by `Cslib.CTL.Satisfies.existsFinallyOrderHom`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-order-hom).

## The functional for $\mathrm{EG}$

Given a labelled transition system, a valuation of
the atoms and a CTL formula $\varphi$, this is the operator that sends a predicate $Z$ on states
to the predicate holding at a state $s$ when $s$ satisfies $\varphi$ and some successor of $s$
satisfies $Z$, that is, there are a label $a$ and a state $t$ with a transition from $s$ to $t$
labelled $a$ such that $Z$ holds at $t$.

Its greatest fixed point is the set of states satisfying $\mathrm{EG}\,\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsGloballyFun`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-globally-fun).

## The $\mathrm{EG}$ functional as a monotone operator

Given a labelled transition system,
a valuation of the atoms and a CTL formula $\varphi$, this is the monotone map on predicates on
states, ordered pointwise by implication, that sends a predicate $Z$ to the predicate holding at
a state $s$ when $s$ satisfies $\varphi$ and some successor of $s$ satisfies $Z$.

Formalized by `Cslib.CTL.Satisfies.existsGloballyOrderHom`, a definition declared in [CSLibExt/Logics/CTL/Basic.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-globally-order-hom).

## $\mathsf{EF}$ is a least fixed point

Fix a labelled transition system, a valuation of the
atoms at its states, and a CTL formula $\varphi$. Write $[\![\varphi]\!]$ for the set of states
satisfying $\varphi$ and $\mathrm{Pre}_\exists(Z)$ for the set of states having some successor in a
set of states $Z$. Then the set of states satisfying $\mathsf{EF}\,\varphi$ is the least fixed point
of the monotone operator $Z \mapsto [\![\varphi]\!] \cup \mathrm{Pre}_\exists(Z)$ on sets of states.

The fixed point is contained in $\mathsf{EF}\,\varphi$ by Park induction, using the one-step
expansion of $\mathsf{EF}$; the converse is induction on a path to a $\varphi$-state, unfolding the
fixed point once per step.

Formalized by `Cslib.CTL.Satisfies.existsFinally_eq_lfp`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-finally-eq-lfp).

## $\mathsf{EG}$ is a greatest fixed point

Fix a labelled transition system, a valuation of
the atoms at its states, and a CTL formula $\varphi$. Write $[\![\varphi]\!]$ for the set of states
satisfying $\varphi$ and $\mathrm{Pre}_\exists(Z)$ for the set of states having some successor in a
set of states $Z$. Then the set of states satisfying $\mathsf{EG}\,\varphi$ is the greatest fixed
point of the monotone operator $Z \mapsto [\![\varphi]\!] \cap \mathrm{Pre}_\exists(Z)$ on sets of
states.

The inclusion of $\mathsf{EG}\,\varphi$ in the fixed point is coinduction, using the one-step
expansion of $\mathsf{EG}$. The converse builds an infinite run by repeatedly choosing a successor
inside the fixed point, so it uses the axiom of choice.

Formalized by `Cslib.CTL.Satisfies.existsGlobally_eq_gfp`, a theorem declared in [CSLibExt/Logics/CTL/Basic.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/Basic.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html#exists-globally-eq-gfp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Computation tree logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/computation-tree-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/computation-tree-logic)
