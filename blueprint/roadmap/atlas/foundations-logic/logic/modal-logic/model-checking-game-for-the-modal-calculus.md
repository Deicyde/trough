---
declaration: section
origin: cited
lean: Cslib.Modal.MuCalculus.Game.GamePosition, Cslib.Modal.MuCalculus.Game.Player, Cslib.Modal.MuCalculus.Game.Move, Cslib.Modal.MuCalculus.Game.Owner, Cslib.Modal.MuCalculus.Game.prio, Cslib.Modal.MuCalculus.Game.NoMoves, Cslib.Modal.MuCalculus.Game.TerminalWin, Cslib.Modal.MuCalculus.Game.ParityWin
statement: formalized
proof: formalized
---

# Model-checking game for the modal μ-calculus

97 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html).

## Position of the μ-calculus model-checking game

A position of the μ-calculus model-checking game: the formula, the world, and
the stack of enclosing fixpoint binders, innermost first.

Formalized by `Cslib.Modal.MuCalculus.Game.GamePosition`, an abbreviation declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#game-position).

## Player of the μ-calculus model-checking game

The player to move: `true` is Verifier, `false` is Refuter.

Formalized by `Cslib.Modal.MuCalculus.Game.Player`, an abbreviation declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#player).

## Moves of the μ-calculus model-checking game

Fix a Kripke model $M$ with accessibility
relation $R$. A game position $(\varphi, w, s)$ consists of a μ-calculus formula $\varphi$ (with
de Bruijn variables), a world $w$ and a stack $s$ of fixpoint binders, innermost first. The
moves are exactly the following. From $(\varphi \wedge \psi, w, s)$ and from
$(\varphi \vee \psi, w, s)$ to $(\varphi, w, s)$ and to $(\psi, w, s)$. From
$(\Box \varphi, w, s)$ and from $(\Diamond \varphi, w, s)$ to $(\varphi, v, s)$ for every world
$v$ with $w R v$. From $(\mu \varphi, w, s)$ to $(\varphi, w, s')$, where $s'$ is $s$ with
$\mu \varphi$ pushed on top, and likewise from $(\nu \varphi, w, s)$ to $(\varphi, w, s'')$,
where $s''$ is $s$ with $\nu \varphi$ pushed on top. From $(x_n, w, s)$, where $x_n$ is the
variable with de Bruijn index $n$ and $n$ is less than the length of $s$, to $(s_n, w, t)$,
where $s_n$ is the entry of $s$ at index $n$ (counting from $0$) and $t$ is $s$ with its first
$n + 1$ entries removed.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.Move`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#move).

## Owner of a game position

The owner of a game position $(\varphi, w, s)$ is Verifier when
$\varphi$ is a disjunction, a diamond formula or a greatest fixed point, and Refuter for every
other formula.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.Owner`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#owner).

## Priority of a game position

Only fixpoint-binder positions carry a priority. For a
formula $\varphi$, a world $w$ and a binder stack $s$ of length $k$, the position
$(\mu X.\,\varphi, w, s)$, whose formula is the least fixpoint with body $\varphi$, has priority
$2k+1$, the position $(\nu X.\,\varphi, w, s)$, whose formula is the greatest fixpoint with body
$\varphi$, has priority $2k+2$, and every other position has no priority. Priorities strictly
increase with nesting depth, so the outermost binder regenerated infinitely often has the least
priority.

This is the nesting-depth refinement of the alternation-depth priority assignment: same-type
nesting counts toward the depth, which only refines the order (outer still strictly below inner)
and keeps parity tied to the binder kind. Fixed priorities ($\mu \mapsto 1$, $\nu \mapsto 2$)
under the greatest-recurring-priority rule would let an inner vacuous $\nu$ dominate an outer
$\mu$: in $\mu X.\,\nu Y.\,X$, whose denotation is empty, Verifier would win the only play.

## Sources

- E. A. Emerson and C. S. Jutla, "Tree automata, μ-calculus and determinacy", *Proceedings of FOCS 1991*, 368-377; C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6; J. A. Bradfield, "The modal μ-calculus alternation hierarchy is strict", *Theoretical Computer Science* 195 (1998), 133-153 (alternation depth).

Formalized by `Cslib.Modal.MuCalculus.Game.prio`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#prio).

## Positions with no moves

In a Kripke model $M$, a game position $p$ has no moves when
there is no position $q$ such that going from $p$ to $q$ is a move of the model-checking game
in $M$.

Formalized by `Cslib.Modal.MuCalculus.Game.NoMoves`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#no-moves).

## Winner at a terminal position

Let $M$ be a Kripke model and $\mathit{env}$ an environment
assigning a predicate on worlds to every index. At a game position $(\varphi, w, st)$, where $st$
is the stack of enclosing fixpoint binders and $|st|$ its length, Verifier wins exactly when
$\varphi$ is an atom $a$ true at $w$, a negated atom $\neg a$ with $a$ false at $w$, $\top$, a
box $\Box\psi$, or a variable with de Bruijn index $n \ge |st|$ such that
$\mathit{env}(n - |st|)$ holds at $w$. At every other position (a variable with index
$n < |st|$, $\bot$, a diamond, a conjunction, a disjunction or a fixpoint) Refuter wins.

The condition is consulted only at positions with no moves: a box with no successors leaves
Refuter stuck and a diamond with no successors leaves Verifier stuck, while a bound variable,
a conjunction, a disjunction and a fixpoint always have a move. The environment index is
shifted by $|st|$ because each binder on the stack shifts de Bruijn indices by one.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.TerminalWin`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#terminal-win).

## Parity winning condition

For an infinite sequence of game positions $p_0, p_1, \dots$,
Verifier wins by the parity condition when there is an even priority $e$ such that infinitely
many positions $p_n$ have priority $e$, and every priority $e' < e$ is the priority of only
finitely many positions $p_n$. Equivalently, some priority occurs infinitely often and the least
such priority is even; in particular, if no priority occurs infinitely often, Verifier does not
win. Only fixpoint-binder positions carry a priority, so the other positions do not affect the
outcome.

The least-priority convention is what makes outer binders dominate: an outer binder has a smaller
priority than any binder nested inside it.

## Sources

- E. A. Emerson and C. S. Jutla, "Tree automata, μ-calculus and determinacy", *Proceedings of FOCS 1991*, 368-377.

Formalized by `Cslib.Modal.MuCalculus.Game.ParityWin`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#parity-win).

## Verifier strategy

A Verifier strategy for the model-checking game on a Kripke model $M$
is a map $\sigma$ from game positions to game positions such that, at every Verifier-owned
position $p$ from which some move exists, there is a move from $p$ to $\sigma(p)$.

The move-respecting condition is what makes Verifier's winning meaningful: without it, a
strategy could "win" by choosing a non-move at a Verifier position, leaving no
legal play at all.

Formalized by `Cslib.Modal.MuCalculus.Game.Strategy`, a structure declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#strategy).

## Finite plays consistent with a strategy

Fix a Kripke model $M$ and a Verifier strategy
$\sigma$. The finite plays from a position $p$ that follow $\sigma$ are the lists of positions
defined inductively: the one-element list $[p]$ is such a play; and if the game has a move from
$p$ to $q$, where $q$ is the position chosen by $\sigma$ at $p$ whenever Verifier owns $p$, then
$p$ followed by any such play from $q$ is such a play from $p$.

A play need not end at a position with no moves: every finite prefix counts.

Formalized by `Cslib.Modal.MuCalculus.Game.PlayFrom`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#play-from).

## Last position of a play

The last position of a finite list of game positions is its
final entry when the list is nonempty; the empty list has no last position.

Formalized by `Cslib.Modal.MuCalculus.Game.playLast`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#play-last).

## Winning strategy from a position

Let $M$ be a Kripke model, $\mathit{env}$ an environment
assigning a predicate on worlds to every index, $\sigma$ a Verifier strategy for the
model-checking game on $M$ and $p$ a game position. A play is consistent with $\sigma$ when each
step is a move and, at every Verifier-owned position, goes to the position chosen by $\sigma$.
The strategy $\sigma$ wins from $p$ in $\mathit{env}$ when every finite play from $p$ consistent
with $\sigma$ whose last position has no moves ends in a position that is a terminal win for
Verifier in $\mathit{env}$, and every infinite play from $p$ consistent with $\sigma$ satisfies
the parity condition.

Formalized by `Cslib.Modal.MuCalculus.Game.StrategyWins`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#strategy-wins).

## Verifier has a winning strategy

For a Kripke model $M$, an environment $\mathit{env}$
and a game position $p$, Verifier wins from $p$ when some Verifier strategy $\sigma$ in the
model-checking game on $M$ wins from $p$ in environment $\mathit{env}$: every complete finite
$\sigma$-consistent play from $p$ ends at a terminal winning position, and every infinite
$\sigma$-consistent play from $p$ satisfies the parity condition.

Formalized by `Cslib.Modal.MuCalculus.Game.VerifierWins`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#verifier-wins).

## Formulas closed at depth $d$

Closedness of a μ-calculus formula $\varphi$ (with de Bruijn
variables) at a depth $d \in \mathbb{N}$ is defined by recursion on $\varphi$: atoms, negated
atoms, $\bot$ and $\top$ are closed at every depth; the variable with index $n$ is closed at
depth $d$ exactly when $n < d$; $\varphi \wedge \psi$ and $\varphi \vee \psi$ are closed at
depth $d$ when both $\varphi$ and $\psi$ are; $\Box\varphi$ and $\Diamond\varphi$ are closed at
depth $d$ when $\varphi$ is; and $\mu\varphi$ and $\nu\varphi$ are closed at depth $d$ when
$\varphi$ is closed at depth $d + 1$. Thus every free variable of $\varphi$ refers to one of $d$
enclosing binders.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6 (de Bruijn variables).

Formalized by `Cslib.Modal.MuCalculus.Game.ClosedAt`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#closed-at).

## Closed formulas

A μ-calculus formula $\varphi$ is closed when it is closed at depth $0$,
that is, when it has no free variables.

Formalized by `Cslib.Modal.MuCalculus.Game.Closed`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#closed).

## Closedness is monotone in the depth

Let $\varphi$ be a μ-calculus formula and let
$d \le d'$ be natural numbers. If $\varphi$ is closed at depth $d$ (every free variable of
$\varphi$ is less than $d$), then $\varphi$ is closed at depth $d'$: more enclosing binders can
only bind more variables.

Formalized by `Cslib.Modal.MuCalculus.Game.ClosedAt.mono`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#mono).

## Satisfaction depends only on the environment below the closure depth

Let $M$ be a
Kripke model, $\varphi$ a μ-calculus formula and $d$ a natural number such that $\varphi$ is
closed at depth $d$: every occurrence of a variable with de Bruijn index $n$ lying under $k$
fixpoint binders of $\varphi$ satisfies $n < d + k$. If two environments $\mathit{env}$ and
$\mathit{env}'$, each assigning a predicate on worlds to every index, agree at every index
$n < d$, then for every world $w$, $\varphi$ is satisfied at $w$ in $M$ under $\mathit{env}$ if
and only if it is satisfied at $w$ in $M$ under $\mathit{env}'$.

In particular, satisfaction of a closed formula is independent of the environment.

## Sources

- D. Kozen, *Results on the propositional μ-calculus*, Theoretical Computer Science 27 (1983), 333-354.

Formalized by `Cslib.Modal.MuCalculus.Game.sat_eq_of_closedAt`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#sat-eq-of-closed-at).

## Closed formulas are environment-independent

Let $M$ be a Kripke model and $\varphi$ a
closed μ-calculus formula, that is, one with no free variables. For any two environments
$\mathrm{env}$ and $\mathrm{env}'$, each assigning a set of worlds to every variable index, and
every world $w$, $\varphi$ is satisfied at $w$ in $M$ under $\mathrm{env}$ if and only if it is
satisfied at $w$ in $M$ under $\mathrm{env}'$.

Formalized by `Cslib.Modal.MuCalculus.Game.sat_closed`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#sat-closed).

## The one-world reflexive Kripke model

The Kripke model with a single world, which is
related to itself, and a single atom, which is false at that world.

Formalized by `Cslib.Modal.MuCalculus.Game.counterexampleModel`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#counterexample-model).

## A least fixpoint over a vacuous greatest fixpoint

The μ-calculus formula
$\mu X.\, \nu Y.\, X$ over a one-element type of atoms: a least fixpoint whose body is a greatest
fixpoint whose body is the variable $X$ bound by the outer least fixpoint, so the variable $Y$
bound by the inner greatest fixpoint never occurs.

Its denotation is empty: the outer functional is the identity, and the least fixed point of the
identity on predicates is the empty predicate.

Formalized by `Cslib.Modal.MuCalculus.Game.counterexampleFormula`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#counterexample-formula).

## Starting position of the regression play

The game position consisting of the formula
$\mu X.\,\nu Y.\,X$, the unique world of the one-world model, and the empty binder stack.

Formalized by `Cslib.Modal.MuCalculus.Game.cePos0`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-pos0).

## Second position of the regression play

The game position consisting of the formula
$\nu Y.\,X$, the unique world of the one-world model, and the binder stack
$[\mu X.\,\nu Y.\,X]$. Here $X$ is the de Bruijn variable $1$, which refers to the binder
$\mu X$ on the stack.

Formalized by `Cslib.Modal.MuCalculus.Game.cePos1`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-pos1).

## Third position of the regression play

The game position consisting of the variable $X$,
the unique world of the one-world model, and the binder stack $[\nu Y.\,X,\ \mu X.\,\nu Y.\,X]$,
listed innermost first. Here $X$ is the de Bruijn variable $1$, which refers to the outer binder
$\mu X$.

Formalized by `Cslib.Modal.MuCalculus.Game.cePos2`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-pos2).

## Step map of the regression play

Let $\Phi = \mu X.\, \nu Y.\, X$ be the regression
formula over the one-element type of atoms, and write game positions over the one-element type
of worlds as (formula, world, stack of enclosing binders, innermost first). For every world $w$,
the step map sends $(\Phi, w, [\,])$ to $(\nu Y.\, X, w, [\Phi])$, sends
$(\nu Y.\, X, w, [\Phi])$ to $(X, w, [\nu Y.\, X, \Phi])$, and sends
$(X, w, [\nu Y.\, X, \Phi])$ to $(\Phi, w, [\,])$, where $X$ is the variable bound by the
outer $\mu$; every other game position is sent to itself.

Formalized by `Cslib.Modal.MuCalculus.Game.ceNext`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-next).

## The regression play

Write $\ast$ for the unique world, and consider the game positions
(formula, world, binder stack listed innermost first)
$P_0 = (\mu X.\,\nu Y.\,X,\ \ast,\ [\,])$, $P_1 = (\nu Y.\,X,\ \ast,\ [\mu X.\,\nu Y.\,X])$ and
$P_2 = (X,\ \ast,\ [\nu Y.\,X,\ \mu X.\,\nu Y.\,X])$. Let $s$ be the step map sending $P_0$ to
$P_1$, $P_1$ to $P_2$ and $P_2$ to $P_0$, and fixing every other position. The regression play is
the sequence of positions $p_0 = P_0$, $p_{n+1} = s(p_n)$, which cycles through $P_0, P_1, P_2$.

These are the successive positions of the model-checking game for $\mu X.\,\nu Y.\,X$ on the
one-world model.

Formalized by `Cslib.Modal.MuCalculus.Game.cePlay`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-play).

## Regression cycle, first step

Let $\Phi = \mu X.\, \nu Y.\, X$ be the regression formula,
$\ast$ the unique world, and write game positions as (formula, world, stack of enclosing
binders, innermost first). The step map of the regression play sends the first cycle position
$(\Phi, \ast, [\,])$ to the second cycle position $(\nu Y.\, X, \ast, [\Phi])$.

Formalized by `Cslib.Modal.MuCalculus.Game.ceNext_cePos0`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-next-ce-pos0).

## Regression cycle, second step

Let $\Phi = \mu X.\, \nu Y.\, X$ be the regression formula,
$\ast$ the unique world, and write game positions as (formula, world, stack of enclosing
binders, innermost first). The step map of the regression play sends the second cycle position
$(\nu Y.\, X, \ast, [\Phi])$ to the third cycle position $(X, \ast, [\nu Y.\, X, \Phi])$, where
$X$ is the variable bound by the outer $\mu$.

Formalized by `Cslib.Modal.MuCalculus.Game.ceNext_cePos1`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-next-ce-pos1).

## Regression cycle, third step

Let $\Phi = \mu X.\, \nu Y.\, X$ be the regression formula,
$\ast$ the unique world, and write game positions as (formula, world, stack of enclosing
binders, innermost first). The step map of the regression play sends the third cycle position
$(X, \ast, [\nu Y.\, X, \Phi])$, where $X$ is the variable bound by the outer $\mu$, back to
the first cycle position $(\Phi, \ast, [\,])$.

Formalized by `Cslib.Modal.MuCalculus.Game.ceNext_cePos2`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-next-ce-pos2).

## The regression play stays on the cycle

For every $n \in \mathbb{N}$, the position at
step $n$ of the regression play is the first, the second or the third cycle position.

Formalized by `Cslib.Modal.MuCalculus.Game.cePlay_mem`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-play-mem).

## The regression play has period three

Number the positions of the regression play
from $0$. For every natural number $n$, its position number $n + 3$ equals its position
number $n$.

Formalized by `Cslib.Modal.MuCalculus.Game.cePlay_period`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-play-period).

## The regression play returns to its start every three steps

Number the positions of
the regression play of $\mu X.\,\nu Y.\,X$ from $0$. For every natural number $k$, its
position number $3k$ is its starting position: the formula $\mu X.\,\nu Y.\,X$ at the unique
world, with the empty binder stack.

Formalized by `Cslib.Modal.MuCalculus.Game.cePlay_mul_three`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-play-mul-three).

## The regression play is a play

For every $n \in \mathbb{N}$, in the model-checking game
on the one-world regression model there is a move from the position at step $n$ of the
regression play to the position at step $n + 1$.

Formalized by `Cslib.Modal.MuCalculus.Game.cePlay_moves`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-play-moves).

## Priority of the outer binder in the regression play

The starting position of the
regression play, consisting of the formula $\mu X.\,\nu Y.\,X$, the unique world and the empty
binder stack, has priority $1$: a $\mu$-binder position with $k$ binders on the stack has
priority $2k + 1$, and here $k = 0$.

Under fixed priorities ($\mu \mapsto 1$, $\nu \mapsto 2$) the greatest priority recurring on this
play would be $2$ (even, Verifier wins); with priorities increasing with nesting depth (the inner
$\nu$ here has priority $4$) and the least-priority rule, the least binder priority recurring on
this play is $1$ (odd, Refuter wins).

Formalized by `Cslib.Modal.MuCalculus.Game.ce_prio0`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-prio0).

## Priority of the inner binder in the regression play

The second position of the
regression play, consisting of the formula $\nu Y.\,X$, the unique world and the binder stack
$[\mu X.\,\nu Y.\,X]$, has priority $4$: a $\nu$-binder position with $k$ binders on the stack
has priority $2k + 2$, and here $k = 1$.

Formalized by `Cslib.Modal.MuCalculus.Game.ce_prio1`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ce-prio1).

## Verifier loses the infinite play of $\mu X.\, \nu Y.\, X$

Consider the infinite
sequence of positions of the model-checking game for $\mu X.\, \nu Y.\, X$ (with one-element
types of worlds and atoms) that starts at this formula with empty binder stack and repeats three
steps: unfold $\mu X$, unfold $\nu Y$, and follow the variable $X$ back to the formula with empty
stack. This play does not satisfy the parity condition: it is not the case that the least binder
priority occurring infinitely often is even.

Formalized by `Cslib.Modal.MuCalculus.Game.counterexample_parityWin_false`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#counterexample-parity-win-false).

## $\mu X.\, \nu Y.\, X$ is false in the one-world model

In the Kripke model with a single
world, which is related to itself, and a single atom, which is false there, under the environment
that assigns the empty set to every variable, the formula $\mu X.\, \nu Y.\, X$ is not satisfied
at the unique world.

This agrees with the model-checking game, where Verifier loses the play of this formula.

Formalized by `Cslib.Modal.MuCalculus.Game.counterexample_sat_false`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#counterexample-sat-false).

## Fixpoint-free formulas

The fixpoint-free formulas over a type of atoms are built from
atoms $p$, negated atoms $\neg p$, $\bot$ and $\top$ by conjunction $\varphi \land \psi$,
disjunction $\varphi \lor \psi$, necessity $\Box\varphi$ and possibility $\Diamond\varphi$.

These are the formulas of basic modal logic in negation normal form: the μ-calculus formulas with
no fixpoint operators and no variables.

Formalized by `Cslib.Modal.MuCalculus.Game.FixFreeFormula`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#fix-free-formula).

## Embedding of the fixpoint-free fragment into the μ-calculus

The map from fixpoint-free
formulas to μ-calculus formulas defined by recursion: atoms, negated atoms, $\bot$ and $\top$
go to the same atom, negated atom, $\bot$ and $\top$, and $\varphi \wedge \psi$,
$\varphi \vee \psi$, $\Box \varphi$ and $\Diamond \varphi$ go to the conjunction, disjunction,
box and diamond of the images of $\varphi$ and $\psi$.

Formalized by `Cslib.Modal.MuCalculus.Game.FixFreeFormula.toMu`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#to-mu).

## Backward-induction winning region of the fixpoint-free fragment

Let $M$ be a Kripke
model with accessibility relation $R$. For a fixpoint-free formula $\varphi$ and a world $w$,
"$\varphi$ is winning at $w$" is defined by recursion on $\varphi$: an atom $a$ is winning at
$w$ iff $a$ is true at $w$ in $M$; a negated atom $\lnot a$ iff $a$ is not true at $w$; $\bot$
is never winning and $\top$ is always winning; $\varphi \land \psi$ is winning at $w$ iff both
$\varphi$ and $\psi$ are; $\varphi \lor \psi$ iff $\varphi$ or $\psi$ is; $\Box \varphi$ iff
$\varphi$ is winning at every $v$ with $w \mathrel{R} v$; and $\Diamond \varphi$ iff $\varphi$
is winning at some $v$ with $w \mathrel{R} v$.

Verifier has a winning strategy in the model-checking game from the position $(\varphi, w, [])$
with empty stack exactly when $\varphi$ is winning at $w$.

Formalized by `Cslib.Modal.MuCalculus.Game.Wins`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins).

## Backward-induction winning equals satisfaction on the fixpoint-free fragment

For every
Kripke model $M$, environment $\mathit{env}$, fixpoint-free formula $\varphi$ and world $w$, $w$
lies in the backward-induction winning region of $\varphi$ if and only if $w$ satisfies the
μ-calculus embedding of $\varphi$ in $M$ under $\mathit{env}$.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.wins_iff_sat`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-iff-sat).

## Size of a μ-calculus formula

The size $|\varphi|$ of a μ-calculus formula $\varphi$ is
the number of nodes of its syntax tree: an atom, a negated atom, a variable, $\bot$ and $\top$
have size $1$; $|\varphi \wedge \psi| = |\varphi \vee \psi| = |\varphi| + |\psi| + 1$; and
$|\Box\varphi| = |\Diamond\varphi| = |\mu\varphi| = |\nu\varphi| = |\varphi| + 1$.

Formalized by `Cslib.Modal.MuCalculus.Game.MuFormula.size`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#size).

## Partial inverse of the fixpoint-free embedding

The partial map from μ-calculus formulas
to fixpoint-free formulas defined by recursion: an atom, a negated atom, $\bot$ and $\top$ are
sent to the same formula; a conjunction or disjunction is sent to the conjunction or
disjunction of the values at its two parts, and $\Box\psi$, $\Diamond\psi$ to the box or diamond
of the value at $\psi$, whenever those values are defined; the map is undefined at variables
and at least and greatest fixpoints, and at every formula with a part where it is undefined.

It inverts the embedding of fixpoint-free formulas into μ-calculus formulas on its image.

Formalized by `Cslib.Modal.MuCalculus.Game.toMuInv`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#to-mu-inv).

## The partial inverse recovers fixpoint-free formulas

For every fixpoint-free formula
$\varphi$, the partial inverse of the embedding of fixpoint-free formulas into μ-calculus
formulas is defined at the image of $\varphi$ under the embedding, with value $\varphi$.

Formalized by `Cslib.Modal.MuCalculus.Game.toMuInv_toMu`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#to-mu-inv-to-mu).

## The embedding inverts the partial inverse

For every μ-calculus formula $\psi$ and every
fixpoint-free formula $\varphi$: if the partial inverse of the embedding of fixpoint-free
formulas into μ-calculus formulas is defined at $\psi$ with value $\varphi$, then the embedding
sends $\varphi$ to $\psi$.

Formalized by `Cslib.Modal.MuCalculus.Game.toMu_toMuInv`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 618](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#to-mu-to-mu-inv).

## The fixpoint-free embedding is injective

The embedding of fixpoint-free formulas into
μ-calculus formulas is injective: distinct fixpoint-free formulas have distinct images.

This is what lets the canonical fragment game recover a fragment formula from an
embedded game position.

Formalized by `Cslib.Modal.MuCalculus.Game.FixFreeFormula.toMu_injective`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#to-mu-injective).

## Wins-guided move

Let $M$ be a Kripke model, and identify each fixpoint-free formula with
its embedding into the μ-calculus. For a μ-calculus formula $\psi$, a world $w$ and a stack $s$
of fixpoint binders, the Wins-guided move at the game position $(\psi, w, s)$ is the following
position. If $s$ is empty and $\psi$ is a fixpoint-free disjunction $\psi_1 \lor \psi_2$, it is
$(\psi_1, w, [])$ when $\psi_1$ is winning at $w$ (in the backward-induction winning region of
the fixpoint-free fragment) and $(\psi_2, w, [])$ otherwise. If $s$ is empty and $\psi$ is a
fixpoint-free formula $\Diamond \psi_1$, it is $(\psi_1, v, [])$ for a chosen successor $v$ of
$w$ at which $\psi_1$ is winning, if one exists; otherwise $(\psi_1, v, [])$ for a chosen
successor $v$ of $w$, if one exists; otherwise $(\psi, w, [])$. In every other case: at a
disjunction $\varphi_1 \lor \varphi_2$ it is $(\varphi_1, w, s)$; at $\Diamond \varphi_1$ it is
$(\varphi_1, v, s)$ for a chosen successor $v$ of $w$ if one exists, and $(\psi, w, s)$
otherwise; at $\nu \varphi_1$ it is $(\varphi_1, w, s')$, where $s'$ is $s$ with
$\nu \varphi_1$ pushed on top; and at every remaining formula (the positions owned by Refuter)
it is $(\psi, w, s)$.

Only the left disjunct is tested: if a fixpoint-free disjunction is winning at $w$ and its left
disjunct is not, then its right disjunct is.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.winsMove`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-move).

## The Wins-guided move at a disjunction

Let $M$ be a Kripke model, $\varphi_1$ and
$\varphi_2$ fixpoint-free formulas and $w$ a world in the backward-induction winning region of
$\varphi_1 \vee \varphi_2$. Then for some $i \in \{1, 2\}$, $w$ lies in the backward-induction
winning region of $\varphi_i$ and the Wins-guided move at the position made of the embedding of
$\varphi_1 \vee \varphi_2$, the world $w$ and the empty binder stack is the position made of the
embedding of $\varphi_i$, the world $w$ and the empty stack.

Formalized by `Cslib.Modal.MuCalculus.Game.winsMove_or`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-move-or).

## The Wins-guided move at a diamond

Let $M$ be a Kripke model, $\varphi$ a fixpoint-free
formula and $w$ a world in the backward-induction winning region of $\Diamond \varphi$. Then
there is a successor $v$ of $w$ in $M$ lying in the backward-induction winning region of
$\varphi$ such that the Wins-guided move at the position made of the embedding of
$\Diamond \varphi$, the world $w$ and the empty binder stack is the position made of the
embedding of $\varphi$, the world $v$ and the empty stack.

Formalized by `Cslib.Modal.MuCalculus.Game.winsMove_dia`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-move-dia).

## The Wins-guided move is legal

For a Kripke model $M$ and a game position $p$ owned by
Verifier from which some move exists, the Wins-guided move at $p$ is a legal move of the
model-checking game on $M$ from $p$.

Formalized by `Cslib.Modal.MuCalculus.Game.winsMove_isMove`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-move-is-move).

## Wins-guided strategy

For a Kripke model $M$, the Wins-guided strategy is the Verifier
strategy of the model-checking game on $M$ that chooses, at each game position $(\psi, w, s)$,
the Wins-guided move at $(\psi, w, s)$. At every Verifier-owned position that has a move, this
choice is a legal move.

Formalized by `Cslib.Modal.MuCalculus.Game.winsStrategy`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 855](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L855). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-strategy).

## Finite plays are nonempty

Let $M$ be a Kripke model, $\sigma$ a Verifier strategy and
$p$ a game position. Every finite play from $p$ consistent with $\sigma$ is a nonempty list of
positions.

Formalized by `Cslib.Modal.MuCalculus.Game.PlayFrom.ne_nil`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 862](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L862). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#ne-nil).

## Prepending to a nonempty play keeps the last position

For a game position $p$ and a
nonempty list $ps$ of game positions, the list obtained by prepending $p$ to $ps$ has the same
last position as $ps$.

Formalized by `Cslib.Modal.MuCalculus.Game.playLast_cons`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 870](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L870). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#play-last-cons).

## Fragment moves decrease the formula size

Let $M$ be a Kripke model, $\varphi$ a
fixpoint-free formula and $w$ a world. Every move of the model-checking game in $M$ from the
position $(\varphi, w, [\,])$, with $\varphi$ embedded in the μ-calculus and the empty stack, leads
to a position $(\varphi', w', [\,])$ for some fixpoint-free formula $\varphi'$ and world $w'$,
and the size of $\varphi'$ is strictly smaller than the size of $\varphi$ (sizes of the embedded
μ-calculus formulas).

Formalized by `Cslib.Modal.MuCalculus.Game.move_of_toMu`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 877](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L877). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#move-of-to-mu).

## No infinite play from a fragment position

Let $M$ be a Kripke model, $\varphi$ a
fixpoint-free formula and $w$ a world. There is no sequence of game positions
$p_0, p_1, p_2, \dots$ with $p_0 = (\varphi, w, [\,])$ (the embedded formula with the empty
stack) such that each step from $p_n$ to $p_{n+1}$ is a move of the model-checking game in $M$.
The reason is that every move strictly decreases the formula size.

Formalized by `Cslib.Modal.MuCalculus.Game.no_infinite_play_of_fixFree`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 907](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L907). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#no-infinite-play-of-fix-free).

## Winning strategies stay winning along consistent moves

Let $M$ be a Kripke model,
$\mathit{env}$ an environment and $\sigma$ a Verifier strategy for the model-checking game on
$M$. If $\sigma$ wins from a position $p$ in $\mathit{env}$, and $q$ is a position reachable from
$p$ by one move that is the position chosen by $\sigma$ at $p$ whenever Verifier owns $p$, then
$\sigma$ also wins from $q$ in $\mathit{env}$.

Formalized by `Cslib.Modal.MuCalculus.Game.strategyWins_of_move`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 931](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L931). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#strategy-wins-of-move).

## Wins-guided strategy wins finite plays (auxiliary induction)

The Wins-guided strategy wins every complete finite play from a winning
fragment position.

Formalized by `Cslib.Modal.MuCalculus.Game.winsStrategy_wins_finite_aux`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-strategy-wins-finite-aux).

## Wins-guided strategy wins every complete finite play

The Wins-guided strategy wins every complete finite play from a winning
fragment position.

Formalized by `Cslib.Modal.MuCalculus.Game.winsStrategy_wins_finite`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-strategy-wins-finite).

## Game-vs-satisfaction, strategy direction

Let $M$ be a Kripke model, $\mathit{env}$ an
environment assigning a set of worlds to each variable index, $\varphi$ a fixpoint-free formula
and $w$ a world in the backward-induction winning region of $\varphi$. Then Verifier has a
winning strategy, in environment $\mathit{env}$, in the model-checking game on $M$ from the
position made of the μ-calculus embedding of $\varphi$, the world $w$ and the empty binder stack.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.wins_implies_verifierWins`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1052](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1052). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-implies-verifier-wins).

## Inversion for disjunction moves

Let $M$ be a Kripke model, $\varphi$ and $\psi$
μ-calculus formulas, $w$ a world and $s$ a stack of fixpoint binders. If going from the game
position $(\varphi \vee \psi, w, s)$ to a position $q$ is a move of the model-checking game in
$M$, then $q$ is $(\varphi, w, s)$ or $(\psi, w, s)$: the world and the stack are unchanged.

Formalized by `Cslib.Modal.MuCalculus.Game.Move.or_cases`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1064](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1064). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#or-cases).

## Moves from a diamond position

In the model-checking game on a Kripke model $M$, every
move from the position with formula $\Diamond\varphi$, world $w$ and binder stack $s$ goes to the
position with formula $\varphi$, world $v$ and the same stack $s$, for some world $v$ accessible
from $w$ in $M$.

Formalized by `Cslib.Modal.MuCalculus.Game.Move.dia_cases`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1073](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1073). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#dia-cases).

## Game-vs-satisfaction, converse direction

Let $M$ be a Kripke model, $\mathit{env}$ an
environment assigning a set of worlds to each variable index, $\varphi$ a fixpoint-free formula
and $w$ a world. If Verifier has a winning strategy, in environment $\mathit{env}$, in the
model-checking game on $M$ from the position made of the μ-calculus embedding of $\varphi$, the
world $w$ and the empty binder stack, then $w$ lies in the backward-induction winning region of
$\varphi$.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.verifierWins_implies_wins`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1083](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1083). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#verifier-wins-implies-wins).

## Backward-induction winning equals game winning on the fixpoint-free fragment

For every
Kripke model $M$, environment $\mathit{env}$, fixpoint-free formula $\varphi$ and world $w$, $w$
lies in the backward-induction winning region of $\varphi$ if and only if Verifier has a winning
strategy, in environment $\mathit{env}$, in the model-checking game on $M$ from the position made
of the μ-calculus embedding of $\varphi$, the world $w$ and the empty binder stack.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.wins_iff_verifierWins`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#wins-iff-verifier-wins).

## Positions of the totalized fragment game

A position of the totalized fragment game, over
a type of atoms and a type of worlds, is either an embedded position $(\varphi, w)$ of a
fixpoint-free formula $\varphi$ and a world $w$, standing for the model-checking game position
$(\varphi, w, [])$ with $\varphi$ embedded as a μ-calculus formula and the empty fixpoint stack,
or one of two absorbing states: the winning state, where Verifier has won, and the losing state,
where Refuter has won.

Since the arena contains no fixpoint positions and every move between embedded positions
strictly decreases the formula, priority $0$ on embedded positions is sound. An embedded
position with no moves leads to the winning state if it is a terminal win for Verifier and to
the losing state otherwise, and both absorbing states loop to themselves, so the game has no
dead ends and is a parity game.

Formalized by `Cslib.Modal.MuCalculus.Game.FragPos`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-pos).

## Projection of game positions onto the fragment arena

A game position with empty binder
stack whose formula is the μ-calculus reading of a fixpoint-free formula $\varphi$, at world $w$,
is sent to the embedded position $(\varphi, w)$. Every other game position (one whose formula
contains a fixpoint operator or a variable, or one with a nonempty stack) is sent to the losing
state.

The losing state is a default that is never reached on plays that stay in the arena, since every
move from an embedded position lands on an embedded position.

## Sources

- C. Stirling, *Modal and Temporal Properties of Processes*, Springer 2001, Chapter 6.

Formalized by `Cslib.Modal.MuCalculus.Game.fragOfGamePos`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-of-game-pos).

## Projection of an embedded position

For every fixpoint-free formula $\varphi$ and world
$w$, projecting the game position with formula $\varphi$ (read as a μ-calculus formula), world $w$
and empty binder stack onto the fragment arena gives the embedded position $(\varphi, w)$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragOfGamePos_toMu`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-of-game-pos-to-mu).

## Moves of the totalized fragment game

Let $M$ be a Kripke model and $e$ an environment,
and read each fixpoint-free formula $\varphi$ as a μ-calculus formula. The totalized fragment game
of $M$ and $e$ has these moves: from an embedded position $(\varphi, w)$ to $(\varphi', w')$
whenever the model-checking game of $M$ has a move from $(\varphi, w)$ to $(\varphi', w')$ with
empty binder stacks; from $(\varphi, w)$ to the winning state when the game position
$(\varphi, w)$ with empty stack has no moves and is won by Verifier in environment $e$; from
$(\varphi, w)$ to the losing state when that game position has no moves and is not won by
Verifier; and from each of the winning and losing states to itself.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-move).

## Owners in the totalized fragment game

In the totalized fragment game, an embedded
position $(\varphi, w)$ of a fixpoint-free formula $\varphi$ at a world $w$ is owned by the even
player if Verifier owns the model-checking game position $(\varphi, w, [])$ (with $\varphi$
embedded as a μ-calculus formula and the empty fixpoint stack), and by the odd player otherwise,
that is, when Refuter owns it. The absorbing winning and losing states are both owned by the
even player.

Verifier plays the even player; the moves at the absorbing states are forced, so their owner
does not matter.

Formalized by `Cslib.Modal.MuCalculus.Game.fragOwner`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-owner).

## Priorities in the totalized fragment game

In the totalized fragment game, every embedded
position $(\varphi, w)$ of a fixpoint-free formula $\varphi$ at a world $w$ has priority $0$, the
absorbing winning state has priority $0$, and the absorbing losing state has priority $1$.

So an infinite play that eventually stays at the winning state is won by the even player, and
one that eventually stays at the losing state by the odd player. Priority $0$ on embedded
positions is sound because the arena contains no fixpoint positions and every move between
embedded positions strictly decreases the formula, so no infinite play visits only embedded
positions.

Formalized by `Cslib.Modal.MuCalculus.Game.fragPriority`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-priority).

## Fragment parity game

Let $M$ be a Kripke model and $\rho$ an environment, and write
$(\varphi, w, [])$ for the game position with formula $\varphi$, world $w$ and empty binder
stack. The fragment game of $M$ and $\rho$ is the parity game on the totalized fragment
positions defined as follows. An embedded position $(\varphi, w)$ moves to $(\varphi', w')$
when $(\varphi, w, [])$ has a move to $(\varphi', w', [])$ in the model-checking game on $M$;
if $(\varphi, w, [])$ has no moves, $(\varphi, w)$ moves to the winning state when
$(\varphi, w, [])$ is a terminal win in $\rho$ and to the losing state otherwise; the winning
and losing states move only to themselves. The even player owns both absorbing states and the
embedded positions $(\varphi, w)$ such that Verifier owns $(\varphi, w, [])$; the odd player
owns the other embedded positions. Embedded positions and the winning state have priority $0$;
the losing state has priority $1$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragmentGame`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#fragment-game).

## The absorbing win state

In the totalized fragment game on a Kripke model $M$ with
environment $\mathit{env}$, every move from the absorbing Verifier-wins state $\mathrm{win}$
leads back to it: if $\mathrm{win}$ moves to $v$, then $v = \mathrm{win}$.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove.win_eq`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#win-eq).

## The losing state is absorbing

In the fragment game of a Kripke model $M$ and an
environment $\rho$, every move from the losing state goes to the losing state.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove.lose_eq`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#lose-eq).

## Fragment moves between embedded positions are game moves

Let $M$ be a Kripke model,
$\mathrm{env}$ an environment, $\varphi, \varphi'$ fixpoint-free formulas and $w, w'$ worlds. If
the totalized fragment game has a move from the embedded position $(\varphi, w)$ to the embedded
position $(\varphi', w')$, then the model-checking game has a move from $(\varphi, w, [])$ to
$(\varphi', w', [])$, where the fixpoint-free formulas are viewed as μ-calculus formulas and
$[]$ is the empty binder stack.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove.pos_move_iff`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#pos-move-iff).

## Moves to the winning state come from terminal winning positions

Let $M$ be a Kripke
model, $\mathrm{env}$ an environment, $\varphi$ a fixpoint-free formula and $w$ a world. If the
totalized fragment game has a move from the embedded position $(\varphi, w)$ to the absorbing
winning state, then the game position $(\varphi, w, [])$, with $\varphi$ viewed as a μ-calculus
formula and an empty binder stack, has no moves, and Verifier wins there as a terminal position
in the environment $\mathrm{env}$.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove.pos_toWin`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#pos-to-win).

## Moves to the losing state come from terminal losing positions

Let $M$ be a Kripke model,
$\mathrm{env}$ an environment, $\varphi$ a fixpoint-free formula and $w$ a world. If the
totalized fragment game has a move from the embedded position $(\varphi, w)$ to the absorbing
losing state, then the game position $(\varphi, w, [])$, with $\varphi$ viewed as a μ-calculus
formula and an empty binder stack, has no moves, and Verifier does not win there as a terminal
position in the environment $\mathrm{env}$.

Formalized by `Cslib.Modal.MuCalculus.Game.FragMove.pos_toLose`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#pos-to-lose).

## Owner of an embedded position in the totalized fragment game

For every fixpoint-free
formula $\varphi$ and world $w$, the even player owns the embedded position $(\varphi, w)$ of the
totalized fragment game if and only if Verifier owns the model-checking game position
$(\varphi, w, [])$, with $\varphi$ embedded as a μ-calculus formula and the empty fixpoint stack.

Formalized by `Cslib.Modal.MuCalculus.Game.fragOwner_pos_eq_even`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-owner-pos-eq-even).

## Canonical next move induced by a bespoke strategy

Let $M$ be a Kripke model,
$\mathit{env}$ an environment and $\sigma$ a Verifier strategy for the model-checking game on
$M$. Write $\langle \psi, v \rangle$ for the game position with the embedding of a
fixpoint-free formula $\psi$, the world $v$ and the empty binder stack. The canonical next move
is the map on positions of the fragment arena defined as follows. The absorbing states
$\mathrm{win}$ and $\mathrm{lose}$ are sent to themselves. A fragment position $(\varphi, w)$
such that $\langle \varphi, w \rangle$ has a move to some $\langle \varphi', w' \rangle$ is
sent, if Verifier owns $\langle \varphi, w \rangle$, to the projection into the fragment arena
of the position that $\sigma$ chooses there (an embedded position $\langle \varphi', w' \rangle$
projects to $(\varphi', w')$, every other game position to $\mathrm{lose}$), and otherwise to a
fragment position $(\varphi', w')$ chosen, by the axiom of choice, among those with a move from
$\langle \varphi, w \rangle$ to $\langle \varphi', w' \rangle$. A fragment position
$(\varphi, w)$ with no such move is sent to $\mathrm{win}$ if $\langle \varphi, w \rangle$
satisfies the terminal winning condition for Verifier in environment $\mathit{env}$, and to
$\mathrm{lose}$ otherwise.

Formalized by `Cslib.Modal.MuCalculus.Game.canonicalNext`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#canonical-next).

## The canonical move follows the bespoke strategy at Verifier positions with a move

Let
$M$ be a Kripke model, $\mathit{env}$ an environment and $\sigma$ a Verifier strategy for the
model-checking game on $M$. Write $\langle \psi, v \rangle$ for the game position with the
embedding of a fixpoint-free formula $\psi$, the world $v$ and the empty binder stack. Let
$\varphi$ be a fixpoint-free formula and $w$ a world such that Verifier owns
$\langle \varphi, w \rangle$ and $\langle \varphi, w \rangle$ has a move to some
$\langle \varphi'', w'' \rangle$. Then there are a fixpoint-free formula $\varphi'$ and a world
$w'$ such that the canonical next move induced by $\sigma$ (in environment $\mathit{env}$) sends
the fragment position $(\varphi, w)$ to the fragment position $(\varphi', w')$, and $\sigma$
chooses $\langle \varphi', w' \rangle$ at $\langle \varphi, w \rangle$.

Formalized by `Cslib.Modal.MuCalculus.Game.canonicalNext_pos_of_owner`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#canonical-next-pos-of-owner).

## Positional strategy induced by a bespoke strategy

The canonical positional strategy induced by a bespoke strategy.

Formalized by `Cslib.Modal.MuCalculus.Game.fragStrategy`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-strategy).

## Game position of a fragment position

Given a default game position $p_0$, an embedded
fragment position $(\varphi, w)$ is sent to the game position with formula $\varphi$, world $w$
and empty binder stack, and the absorbing winning and losing states are both sent to $p_0$.

The default is never used on plays that stay among embedded positions.

Formalized by `Cslib.Modal.MuCalculus.Game.fragToPos`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-to-pos).

## Segment of a fragment play as game positions

Let $p_0$ be a game position and let
$\pi = \pi_0 \pi_1 \pi_2 \dots$ be an infinite sequence of positions of the totalized fragment
game. For natural numbers $s$ and $k$, the segment of $\pi$ from $s$ of length $k + 1$ is the
list of game positions obtained from $\pi_s, \pi_{s+1}, \dots, \pi_{s+k}$, in this order, by
sending each embedded position $(\varphi, w)$ to the game position with formula $\varphi$, world
$w$ and empty binder stack, and each of the absorbing winning and losing states to $p_0$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragSegment`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-segment).

## Splitting off the head of a segment

Let $p_0$ be a model-checking game position and $\pi$
an infinite sequence of positions of the totalized fragment game. For each $i$, let $\hat\pi_i$ be
$p_0$ if $\pi_i$ is an absorbing state; if $\pi_i$ is the embedded position $(\varphi, w)$ of a
fixpoint-free formula $\varphi$ and a world $w$, let $\hat\pi_i$ be the game position
$(\varphi, w, [])$, with $\varphi$ embedded as a μ-calculus formula and the empty fixpoint stack.
For all natural numbers $s$ and $k$, the segment $[\hat\pi_s, \dots, \hat\pi_{s+k+1}]$ of $\pi$ is
the list with head $\hat\pi_s$ followed by the segment $[\hat\pi_{s+1}, \dots, \hat\pi_{s+k+1}]$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragSegment_cons`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1477](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-segment-cons).

## Segments of canonical plays through fragment positions are bespoke plays

Let $M$ be a
Kripke model, $\mathit{env}$ an environment and $\sigma$ a Verifier strategy for the
model-checking game on $M$. Write $\langle \psi, v \rangle$ for the game position with the
embedding of a fixpoint-free formula $\psi$, the world $v$ and the empty binder stack. Let $\pi$
be a play of the fragment game of $M$ and $\mathit{env}$ that conforms to the canonical
positional strategy induced by $\sigma$, and let $s, k \in \mathbb{N}$. Suppose every $\pi_i$
with $s \le i \le s + k$ is a fragment position $(\varphi_i, w_i)$, not $\mathrm{win}$ or
$\mathrm{lose}$. Then the list
$\langle \varphi_s, w_s \rangle, \langle \varphi_{s+1}, w_{s+1} \rangle, \dots,
\langle \varphi_{s+k}, w_{s+k} \rangle$ is a finite play from $\langle \varphi_s, w_s \rangle$
consistent with $\sigma$: each position has a game move to the next, and at Verifier-owned
positions the next position is the one $\sigma$ chooses.

Formalized by `Cslib.Modal.MuCalculus.Game.canonical_playFrom_segment`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#canonical-play-from-segment).

## Plays of the totalized fragment game stay at the winning state

Let $M$ be a Kripke model
and $\mathit{env}$ an environment assigning a set of worlds to each free-variable index. If
$\pi$ is a play of the totalized fragment game of $M$ and $\mathit{env}$ and $\pi_k$ is the
absorbing winning state, then $\pi_n$ is the winning state for every $n \ge k$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragPlay_eq_win_of_le`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-play-eq-win-of-le).

## Plays of the totalized fragment game stay at the losing state

Let $M$ be a Kripke model
and $\mathit{env}$ an environment assigning a set of worlds to each free-variable index. If
$\pi$ is a play of the totalized fragment game of $M$ and $\mathit{env}$ and $\pi_k$ is the
absorbing losing state, then $\pi_n$ is the losing state for every $n \ge k$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragPlay_eq_lose_of_le`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-play-eq-lose-of-le).

## Sequences that stay at the win state are won by the even player

Let $M$ be a Kripke
model and $\mathit{env}$ an environment for free variables. If an infinite sequence
$\pi_0 \pi_1 \pi_2 \dots$ of positions of the totalized fragment game of $M$ and $\mathit{env}$
has a $k_0$ such that $\pi_n$ is the absorbing winning state for all $n \ge k_0$, then $\pi$ is
won by the even player in that game.

Formalized by `Cslib.Modal.MuCalculus.Game.wonBy_even_of_eventually_win`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#won-by-even-of-eventually-win).

## Sequences that stay at the lose state are won by the odd player

Let $M$ be a Kripke
model and $\mathit{env}$ an environment for free variables. If an infinite sequence
$\pi_0 \pi_1 \pi_2 \dots$ of positions of the totalized fragment game of $M$ and $\mathit{env}$
has a $k_0$ such that $\pi_n$ is the absorbing losing state for all $n \ge k_0$, then $\pi$ is
won by the odd player in that game.

Formalized by `Cslib.Modal.MuCalculus.Game.wonBy_odd_of_eventually_lose`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#won-by-odd-of-eventually-lose).

## Segments are nonempty

Let $p_0$ be a model-checking game position and $\pi$ an infinite
sequence of positions of the totalized fragment game. For all natural numbers $s$ and $k$, the
segment of $\pi$ from index $s$ to index $s + k$, read as a list of model-checking game positions
with $p_0$ standing for the absorbing states, is not the empty list.

Formalized by `Cslib.Modal.MuCalculus.Game.fragSegment_ne_nil`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1601](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-segment-ne-nil).

## Last position of a segment

Let $p_0$ be a model-checking game position and $\pi$ an
infinite sequence of positions of the totalized fragment game. For each $i$, let $\hat\pi_i$ be
$p_0$ if $\pi_i$ is an absorbing state; if $\pi_i$ is the embedded position $(\varphi, w)$ of a
fixpoint-free formula $\varphi$ and a world $w$, let $\hat\pi_i$ be the game position
$(\varphi, w, [])$, with $\varphi$ embedded as a μ-calculus formula and the empty fixpoint stack.
For all natural numbers $s$ and $k$, the segment $[\hat\pi_s, \dots, \hat\pi_{s+k}]$ has a last
position, and it is $\hat\pi_{s+k}$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragSegment_playLast`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-segment-play-last).

## Winning Verifier strategies transfer to the fragment game

Let $M$ be a Kripke model,
$\rho$ an environment, $\sigma$ a Verifier strategy of the model-checking game on $M$,
$\varphi$ a fixpoint-free formula and $w$ a world. If $\sigma$ wins in environment $\rho$ from
the game position with formula $\varphi$, world $w$ and empty binder stack, then the positional
strategy of the even player induced by $\sigma$ wins from the embedded position $(\varphi, w)$
in the fragment game of $M$ and $\rho$.

Every play conforming to the induced strategy reaches the absorbing winning state: it cannot
reach the losing state, by the finite-play clause for $\sigma$ applied to the segment before the
first losing state, and it cannot stay among embedded positions forever, since fragment moves
strictly decrease the formula.

Formalized by `Cslib.Modal.MuCalculus.Game.fragment_bespoke_to_canonical`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1626](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#fragment-bespoke-to-canonical).

## Moves of the totalized fragment game, by cases

Let $M$ be a Kripke model and $e$ an
environment, and read each fixpoint-free formula $\varphi$ as a μ-calculus formula. Every move
from $a$ to $b$ in the totalized fragment game of $M$ and $e$ is of one of five kinds: $a$ and $b$
are embedded positions $(\varphi, w)$ and $(\varphi', w')$ and the model-checking game of $M$ has a
move from $(\varphi, w)$ to $(\varphi', w')$ with empty binder stacks; or $a = (\varphi, w)$, $b$ is
the winning state, and the game position $(\varphi, w)$ with empty stack has no moves and is won by
Verifier in environment $e$; or $a = (\varphi, w)$, $b$ is the losing state, and that game position
has no moves and is not won by Verifier; or $a$ and $b$ are both the winning state; or $a$ and $b$
are both the losing state.

Formalized by `Cslib.Modal.MuCalculus.Game.fragMove_cases`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1717](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-move-cases).

## Verifier's positional strategies make a game move at Verifier positions that have one

Let $M$ be a Kripke model, $\mathit{env}$ an environment, and $\sigma$ any positional strategy of
the even player (Verifier) in the fragment game of $M$ and $\mathit{env}$. Write
$\langle \psi, v \rangle$ for the game position with the embedding of a fixpoint-free formula
$\psi$, the world $v$ and the empty binder stack. Let $\varphi$ be a fixpoint-free formula and
$w$ a world such that the even player owns the fragment position $(\varphi, w)$ and, in the
model-checking game on $M$, $\langle \varphi, w \rangle$ has a move to some
$\langle \varphi'', w'' \rangle$. Then $\sigma$ sends $(\varphi, w)$ to a fragment position
$(\varphi', w')$ such that $\langle \varphi, w \rangle$ has a move to
$\langle \varphi', w' \rangle$; in particular $\sigma$ does not move to the absorbing state
$\mathrm{win}$ or $\mathrm{lose}$.

Formalized by `Cslib.Modal.MuCalculus.Game.canonical_next_pos`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#canonical-next-pos).

## The lose play

For a fixpoint-free formula $\varphi$ and a world $w$, the lose play is the
infinite sequence of positions of the fragment arena that is at the position $(\varphi, w)$ at
time $0$ and at the absorbing losing state at every later time. It is used for terminal losing
positions $(\varphi, w)$.

Formalized by `Cslib.Modal.MuCalculus.Game.losePlay`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#lose-play).

## The lose play starts at its fragment position

For a fixpoint-free formula $\varphi$
and a world $w$, the lose play from $(\varphi, w)$ is at the fragment-arena position
$(\varphi, w)$ at time $0$.

Formalized by `Cslib.Modal.MuCalculus.Game.losePlay_zero`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1774](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#lose-play-zero).

## The lose play stays at the losing state

For every fixpoint-free formula $\varphi$,
world $w$ and natural number $n$, the lose play from $(\varphi, w)$ is at the losing state at
time $n + 1$.

Formalized by `Cslib.Modal.MuCalculus.Game.losePlay_succ`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1777](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#lose-play-succ).

## Terminal losing positions are not won by the even player

Let $M$ be a Kripke model,
$\mathit{env}$ an environment assigning a set of worlds to each free-variable index, $\varphi$ a
fixpoint-free formula and $w$ a world. If the model-checking game position $(\varphi, w, [])$,
with $\varphi$ embedded as a μ-calculus formula and the empty fixpoint stack, has no moves in $M$
and is not a terminal win for Verifier in $M$ under $\mathit{env}$, then the embedded position
$(\varphi, w)$ of the totalized fragment game of $M$ and $\mathit{env}$ is not in the winning
region of the even player.

The play that moves from $(\varphi, w)$ to the losing state and stays there conforms to every
strategy of the even player and is won by the odd player.

Formalized by `Cslib.Modal.MuCalculus.Game.fragPos_not_mem_winningRegion_of_terminal_lose`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#frag-pos-not-mem-winning-region-of-termi).

## The fragment game's winning region is contained in Wins

Let $M$ be a Kripke model,
$\rho$ an environment, $\varphi$ a fixpoint-free formula and $w$ a world. If the embedded
position $(\varphi, w)$ lies in the winning region of the even player in the fragment game of
$M$ and $\rho$, then the backward-induction winning condition $\mathrm{Wins}_M(\varphi, w)$
holds.

The proof is by induction on $\varphi$, using that the winning region is closed under the
opponent's moves and under the moves of a winning strategy, so no strategy composition is
needed.

Formalized by `Cslib.Modal.MuCalculus.Game.fragment_canonical_to_wins`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1851](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#fragment-canonical-to-wins).

## Wins is the winning region of the fragment game

Let $M$ be a Kripke model, $\rho$ an
environment, $\varphi$ a fixpoint-free formula and $w$ a world. Then the backward-induction
winning condition $\mathrm{Wins}_M(\varphi, w)$ holds if and only if the embedded position
$(\varphi, w)$ lies in the winning region of the even player in the fragment game of $M$ and
$\rho$.

Formalized by `Cslib.Modal.MuCalculus.Game.fragmentWins_iff_winningRegion`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusGame.lean, line 1968](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/MuCalculusGame.lean#L1968). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html#fragment-wins-iff-winning-region).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Model-checking game for the modal μ-calculus](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/model-checking-game-for-the-modal-calculus)
