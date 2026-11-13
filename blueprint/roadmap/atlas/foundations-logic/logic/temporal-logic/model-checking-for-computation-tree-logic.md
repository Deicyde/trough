---
declaration: section
origin: cited
lean: Cslib.CTL.exists_maximalPath, Cslib.CTL.Satisfies.not_existsNext_top_iff, Cslib.CTL.Satisfies.forallUntil_bad_iff, Cslib.CTL.Satisfies.forallUntil_expansion_forward, Cslib.CTL.Satisfies.forallUntil_iff_not, Cslib.CTL.Satisfies.existsUntil_congr, Cslib.CTL.Satisfies.forallFinally_iff_not, Cslib.CTL.Satisfies.existsNext_iff_preExists
statement: formalized
proof: formalized
---

# Model checking for computation tree logic

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html).

## Duality

## Every state starts a maximal path

In a labelled transition system, for every state $s$
there is an infinite run $s_0, s_1, s_2, \dots$ with $s_0 = s$, or there are a sequence of states
$s_0, s_1, s_2, \dots$ with $s_0 = s$ and a $k$ such that $s_0, \dots, s_k$ is a finite run of
length $k$ and $s_k$ is deadlocked, that is, has no outgoing transition.

The proof iterates a chosen successor function and uses the axiom of choice.

Formalized by `Cslib.CTL.exists_maximalPath`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-maximal-path).

## Deadlocked states are exactly those satisfying ¬EX ⊤

A state $s$ of a labelled transition
system satisfies the CTL formula $\neg\mathsf{EX}\,\top$, under any valuation of the atoms, if and
only if $s$ is deadlocked: there is no label $a$ and state $t$ with a transition from $s$ to $t$
labelled $a$.

Formalized by `Cslib.CTL.Satisfies.not_existsNext_top_iff`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#not-exists-next-top-iff).

## Bad target of the deadlock-correct until duality

Let $\varphi$ and $\psi$ be CTL
formulas, and write $t \models \chi$ when the state $t$ of a labelled transition system satisfies
the formula $\chi$ under a given valuation of the atoms. Then
$t \models \neg\psi \land (\neg\varphi \lor \neg\mathsf{EX}\,\top)$ if and only if
$t \not\models \psi$ and either $t \not\models \varphi$ or $t$ is deadlocked, that is, there is no
label $a$ and state $u$ with a transition from $t$ to $u$ labelled $a$.

Formalized by `Cslib.CTL.Satisfies.forallUntil_bad_iff`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#forall-until-bad-iff).

## One-step unfolding of universal until, forward direction

Let $\varphi$ and $\psi$ be CTL
formulas, and write $s \models \chi$ when the state $s$ of a labelled transition system satisfies
the formula $\chi$ under a given valuation of the atoms. If
$s \models \mathsf{A}[\varphi \mathbin{\mathsf{U}} \psi]$, then either $s \models \psi$, or
$s \models \varphi$, $s$ has at least one outgoing transition, and every state $t$ reached from $s$
by a single transition with any label satisfies
$t \models \mathsf{A}[\varphi \mathbin{\mathsf{U}} \psi]$.

Formalized by `Cslib.CTL.Satisfies.forallUntil_expansion_forward`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#forall-until-expansion-forward).

## Deadlock-correct duality for universal until

Let $\varphi$ and $\psi$ be CTL formulas,
and write $s \models \chi$ when the state $s$ of a labelled transition system satisfies the
formula $\chi$ under a given valuation of the atoms. Then
$s \models \mathsf{A}[\varphi \mathbin{\mathsf{U}} \psi]$ if and only if neither
$s \models \mathsf{E}[\neg\psi \mathbin{\mathsf{U}} (\neg\psi \land (\neg\varphi \lor
\neg\mathsf{EX}\,\top))]$ nor $s \models \mathsf{EG}\,\neg\psi$.

Here $\neg\mathsf{EX}\,\top$ holds exactly at the deadlocked states, those with no outgoing
transition. So $\mathsf{A}[\varphi \mathbin{\mathsf{U}} \psi]$ fails at $s$ exactly when some
infinite run starting at $s$ stays in $\neg\psi$ forever, or some finite run starting at $s$ stays
in $\neg\psi$ up to a $\neg\psi$-state at which $\varphi$ fails or which is deadlocked.

Formalized by `Cslib.CTL.Satisfies.forallUntil_iff_not`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#forall-until-iff-not).

## Congruence of existential until in its target

In a labelled transition system with a
valuation of atoms, let $\rho$, $\alpha$ and $\beta$ be CTL formulas such that every state
satisfies $\alpha$ if and only if it satisfies $\beta$. Then every state $s$ satisfies
$\mathsf{E}[\rho \,\mathsf{U}\, \alpha]$ if and only if it satisfies
$\mathsf{E}[\rho \,\mathsf{U}\, \beta]$.

Formalized by `Cslib.CTL.Satisfies.existsUntil_congr`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-until-congr).

## Deadlock-correct duality for AF

In a labelled transition system with a valuation of
atoms, let $\varphi$ be a CTL formula. A state $s$ satisfies $\mathsf{AF}\,\varphi$ if and only
if $s$ satisfies neither $\mathsf{E}[\neg\varphi \,\mathsf{U}\, (\neg\varphi \wedge
\neg\mathsf{EX}\,\top)]$ nor $\mathsf{EG}\,\neg\varphi$.

This is the case $\mathsf{A}[\top \,\mathsf{U}\, \varphi]$ of the duality for universal until.
The formula $\neg\mathsf{EX}\,\top$ holds exactly at deadlocked states, so the first disjunct
catches finite maximal paths that end at a deadlock without reaching $\varphi$.

Formalized by `Cslib.CTL.Satisfies.forallFinally_iff_not`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#forall-finally-iff-not).

## Existential next via the predecessor operator

In a labelled transition system with a
valuation of atoms, let $\varphi$ be a CTL formula and write $\mathrm{Sat}(\varphi)$ for the set
of states satisfying $\varphi$. A state $s$ satisfies $\mathsf{EX}\,\varphi$ if and only if $s$
belongs to the existential predecessor set of $\mathrm{Sat}(\varphi)$, that is, some transition
leads from $s$ to a state satisfying $\varphi$.

Formalized by `Cslib.CTL.Satisfies.existsNext_iff_preExists`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-next-iff-pre-exists).

## The existential-until functional

In a labelled transition system with a valuation of
atoms, let $\varphi$ and $\psi$ be CTL formulas. The existential-until functional sends a set $Z$
of states to the set of states $s$ such that either $s$ satisfies $\psi$, or $s$ satisfies
$\varphi$ and some transition leads from $s$ to a state in $Z$.

Its least fixed point is the set of states satisfying $\mathsf{E}[\varphi \,\mathsf{U}\, \psi]$.

Formalized by `Cslib.CTL.Satisfies.existsUntilFun`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-until-fun).

## The existential-until functional as a monotone map

In a labelled transition system with
a valuation of atoms, let $\varphi$ and $\psi$ be CTL formulas. The map sending a set $Z$ of
states to the set of states $s$ such that either $s$ satisfies $\psi$, or $s$ satisfies $\varphi$
and some transition leads from $s$ to a state in $Z$, is monotone for inclusion; this is that
map, regarded as an order-preserving map on sets of states.

Formalized by `Cslib.CTL.Satisfies.existsUntilOrderHom`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-until-order-hom).

## Existential until as a least fixed point

In a labelled transition system with a
valuation of atoms, let $\varphi$ and $\psi$ be CTL formulas, write $\mathrm{Sat}(\chi)$ for the
set of states satisfying a formula $\chi$, and write $\mathrm{Pre}_\exists(Z)$ for the set of
states having a transition into a set $Z$ of states. Then the set of states satisfying
$\mathsf{E}[\varphi \,\mathsf{U}\, \psi]$ is the least fixed point of the monotone map
$Z \mapsto \mathrm{Sat}(\psi) \cup (\mathrm{Sat}(\varphi) \cap \mathrm{Pre}_\exists(Z))$ on sets
of states.

One inclusion is Park induction via the one-step expansion of
$\mathsf{E}[\varphi \,\mathsf{U}\, \psi]$; the other is induction on the length of the
witnessing finite run, unfolding the fixed point once per step.

Formalized by `Cslib.CTL.Satisfies.existsUntil_eq_lfp`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#exists-until-eq-lfp).

## Finite existential predecessor set

Let a labelled transition system have finitely many
states and finitely many labels, with decidable transitions. For a finite set $Z$ of states, its
existential predecessor set is the finite set of states $s$ for which there are a label $a$ and a
state $t \in Z$ with a transition from $s$ to $t$ labelled $a$.

It agrees with the existential predecessor operator applied to membership in $Z$.

Formalized by `Cslib.CTL.preExistsFin`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#pre-exists-fin).

## Finite existential-until set

Let $\mathcal{T}$ be a labelled transition system with
finitely many states and finitely many labels, decidable transitions and decidable equality of
states, and let $A$ and $B$ be sets of states. For a set $Z$ of states write
$\mathrm{Pre}_\exists(Z)$ for the set of states having a transition into $Z$. The
existential-until set with side set $A$ and target set $B$ is obtained by applying the map
$Z \mapsto B \cup (A \cap \mathrm{Pre}_\exists(Z))$ to the empty set $n$ times, where $n$ is the
number of states.

Since this map is monotone, the iteration has stabilized after $n$ steps and the result is its
least fixed point.

Formalized by `Cslib.CTL.eUntilFin`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#e-until-fin).

## Finite existential-globally set

Let $\mathcal{T}$ be a labelled transition system with
finitely many states and finitely many labels, decidable transitions and decidable equality of
states, and let $A$ be a set of states. For a set $Z$ of states write
$\mathrm{Pre}_\exists(Z)$ for the set of states having a transition into $Z$. The
existential-globally set of $A$ is obtained by applying the map
$Z \mapsto A \cap \mathrm{Pre}_\exists(Z)$ to the set of all states $n$ times, where $n$ is the
number of states.

Since this map is monotone, the iteration has stabilized after $n$ steps and the result is its
greatest fixed point.

Formalized by `Cslib.CTL.eGloballyFin`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#e-globally-fin).

## Correctness of the finite fixed-point computation of EU

Let a labelled transition system
have finitely many states and finitely many labels, with decidable transitions and decidable
equality of states, and fix a valuation of the atoms. For a finite set $Z$ of states let
$\mathrm{Pre}_\exists(Z)$ be the set of states with a transition into $Z$, and for finite sets
$A$ and $B$ of states let $\mathrm{EU}_{\mathrm{fin}}(A, B)$ be the least fixed point of
$Z \mapsto B \cup (A \cap \mathrm{Pre}_\exists(Z))$, computed by finite iteration. Let $\varphi$
and $\psi$ be CTL formulas and $A$ and $B$ finite sets of states such that a state lies in $A$
exactly when it satisfies $\varphi$, and lies in $B$ exactly when it satisfies $\psi$. Then every
state $s$ lies in $\mathrm{EU}_{\mathrm{fin}}(A, B)$ if and only if $s$ satisfies
$\mathsf{E}[\varphi \mathbin{\mathsf{U}} \psi]$.

Formalized by `Cslib.CTL.mem_eUntilFin_iff`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#mem-e-until-fin-iff).

## Correctness of the finite fixed-point computation of EG

Let a labelled transition system
have finitely many states and finitely many labels, with decidable transitions and decidable
equality of states, and fix a valuation of the atoms. For a finite set $Z$ of states let
$\mathrm{Pre}_\exists(Z)$ be the set of states with a transition into $Z$, and for a finite set
$A$ of states let $\mathrm{EG}_{\mathrm{fin}}(A)$ be the greatest fixed point of
$Z \mapsto A \cap \mathrm{Pre}_\exists(Z)$, computed by finite iteration. Let $\varphi$ be a CTL
formula and $A$ a finite set of states such that a state lies in $A$ exactly when it satisfies
$\varphi$. Then every state $s$ lies in $\mathrm{EG}_{\mathrm{fin}}(A)$ if and only if $s$
satisfies $\mathsf{EG}\,\varphi$.

Formalized by `Cslib.CTL.mem_eGloballyFin_iff`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#mem-e-globally-fin-iff).

## Finite-state CTL model checking by structural recursion

The set of states satisfying a CTL formula in a finite system,
computed by structural recursion: atoms by filtering the valuation,
`EX` by `preExistsFin`, `EU` and `EG` by the finite fixed points
`eUntilFin` and `eGloballyFin`, and `AU` by complementing the
deadlock-correct duality of `Satisfies.forallUntil_iff_not` (the
bad-target set is built from the complement sets of the subformulas
and `preExistsFin lts Finset.univ`, the set of non-deadlocked
states).

Formalized by `Cslib.CTL.sat`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#sat).

## Correctness of the CTL model checker

Let a labelled transition system have finitely many
states and finitely many labels, with decidable transitions and decidable equality of states, and
let the valuation of the atoms be decidable. For every CTL formula $\varphi$ and every state $s$,
the state $s$ lies in the set $\mathrm{sat}(\varphi)$ computed by the model checker if and only if
$s$ satisfies $\varphi$.

The proof is by induction on $\varphi$. The temporal cases use the correctness of the finite
fixed-point computations of $\mathsf{EU}$ and $\mathsf{EG}$, and the $\mathsf{AU}$ case also
identifies the computed bad-target set with the states satisfying the bad-target formula.

Formalized by `Cslib.CTL.mem_sat`, a theorem declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#mem-sat).

## The CTL model checker as a Boolean decision procedure

Let $\mathcal{T}$ be a labelled
transition system with finitely many states and finitely many labels, decidable transitions and
decidable equality of states, and let $V$ be a decidable valuation of atoms at states. For a state
$s$ and a CTL formula $\varphi$, the model checker returns true exactly when $s$ belongs to the
set of states that the satisfaction-set algorithm computes for $\varphi$ in $\mathcal{T}$ under
$V$.

Formalized by `Cslib.CTL.check`, a definition declared in [CSLibExt/Logics/CTL/ModelChecking.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTL/ModelChecking.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html#check).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Model checking for computation tree logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/model-checking-for-computation-tree-logic)
