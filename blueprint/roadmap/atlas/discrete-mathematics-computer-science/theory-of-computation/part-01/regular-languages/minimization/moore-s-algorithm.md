---
declaration: section
origin: cited
lean: DFA.mooreStep, DFA.mooreIter, DFA.mooreIter_spec, DFA.mooreRel, DFA.subset_mooreRel, DFA.mem_mooreRel_iff, DFA.mooreSetoid, DFA.MooreState
statement: formalized
proof: formalized
---

# Moore's algorithm

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html).

## State equivalence by refinement

## Moore refinement step

Let $M$ be a DFA with state set $S$ and transition function
$\delta$. One round of Moore's refinement sends a set $E \subseteq S \times S$ of pairs of
states to the set of pairs $(p, q) \in S \times S$ such that $p$ is accepting if and only if
$q$ is accepting and, for every letter $a$, the pair $(\delta(p, a), \delta(q, a))$ lies in
$E$.

Formalized by `DFA.mooreStep`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-step).

## Stopping Moore iteration

Let $M$ be a DFA over a finite alphabet with finitely many
states, and write $R$ for one round of Moore's refinement. For a set $E$ of pairs of states of
$M$ and a budget $n \in \mathbb{N}$, the stopping Moore iteration is defined by recursion on $n$:
with budget $0$ it returns $E$; with budget $n + 1$ it returns $E$ if $R(E) = E$, and otherwise
the stopping Moore iteration from $R(E)$ with budget $n$.

Formalized by `DFA.mooreIter`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-iter).

## Output of the stopping Moore iteration

Let $M$ be a DFA over a finite alphabet with
finitely many states, and write $R$ for one round of Moore's refinement. For every
$n \in \mathbb{N}$ and every set $E$ of pairs of states of $M$, there is $k \le n$ such that the
stopping Moore iteration from $E$ with budget $n$ returns $R^k(E)$, and if $k < n$ then $R^k(E)$
is a fixed point of $R$, that is, $R(R^k(E)) = R^k(E)$.

Formalized by `DFA.mooreIter_spec`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-iter-spec).

## Moore's relation

For a DFA $M$ over a finite alphabet with finite set of states $Q$,
Moore's relation is the set of pairs of states obtained from $Q \times Q$ by repeating rounds of
Moore's refinement until a round changes nothing, for at most $|Q \times Q|$ rounds.

Formalized by `DFA.mooreRel`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-rel).

## Moore's relation contains every post-fixed point

Let $M$ be a DFA. If a set $Z$ of
pairs of states of $M$ is contained in its image under one round of Moore's refinement, then
$Z$ is contained in Moore's relation of $M$.

Formalized by `DFA.subset_mooreRel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#subset-moore-rel).

## Correctness of Moore's refinement

For a DFA $M$ over a finite alphabet with finitely
many states, two states $p$ and $q$ of $M$ are related by Moore's relation if and only if they
have the same continuation language: for every word $w$, $M$ started at $p$ accepts $w$ exactly
when $M$ started at $q$ accepts $w$.

Formalized by `DFA.mem_mooreRel_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#mem-moore-rel-iff).

## Moore equivalence on reachable states

For a DFA $M$, two reachable states $p$ and $q$
of $M$ are related when the pair $(p, q)$ lies in Moore's relation of $M$; this relation is an
equivalence relation on the reachable states of $M$.

Formalized by `DFA.mooreSetoid`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-setoid).

## States of Moore's automaton

For a DFA $M$, these are the equivalence classes of the
reachable states of $M$ under Moore equivalence, that is, under Moore's relation of $M$
restricted to reachable states. They are the states of Moore's minimal automaton.

Formalized by `DFA.MooreState`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-state).

## Moore class of a reachable state

Let $M$ be a DFA over a finite alphabet with finitely
many states. For a reachable state $s$ of $M$, its Moore class is the equivalence class of $s$
among the reachable states of $M$ under Moore's relation; it is a state of Moore's minimal
automaton of $M$.

Formalized by `DFA.mooreClass`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-class).

## Moore's minimal automaton

For a DFA $M$ over a finite alphabet with finitely many states,
Moore's minimal automaton of $M$ has as states the classes of reachable states of $M$ under
Moore's relation. Its start state is the class of the start state of $M$; reading a letter $a$
sends the class of a reachable state $s$ to the class of the state that $M$ reaches from $s$ on
$a$; and the class of $s$ is accepting exactly when $s$ is an accepting state of $M$.

These do not depend on the chosen member $s$, because Moore-related states agree on acceptance
and their successors on each letter are again Moore-related.

Formalized by `DFA.mooreDFA`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-dfa).

## Moore's automaton accepts the same language

For a DFA $M$ over a finite alphabet with
finitely many states, Moore's minimal automaton of $M$ accepts exactly the language accepted by
$M$.

Formalized by `DFA.mooreDFA_accepts`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-dfa-accepts).

## Continuation language of a Moore class

Let $M$ be a DFA over a finite alphabet with
finitely many states. Each state of Moore's minimal automaton of $M$, a class of reachable states
of $M$, is sent to the continuation language of any member $s$, the set of words that $M$
accepts when started at $s$; this is a reachable residual language of $M$. It does not depend on
the choice of $s$, because Moore-related states have the same continuation language.

Formalized by `DFA.mooreResidual`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-residual).

## Moore classes are the reachable residuals

Let $M$ be a DFA over a finite alphabet with
finitely many states. The states of Moore's minimal automaton of $M$ are in bijection with the
reachable residual languages of $M$: the bijection sends the class of a reachable state $s$ to
the continuation language of $s$, the set of words that $M$ accepts when started at $s$.

Formalized by `DFA.mooreEquiv`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#moore-equiv).

## Moore's automaton is the minimal automaton

Let $M$ be a DFA. Renaming each state of
Moore's minimal automaton of $M$, a class of reachable states, to the continuation language
accepted from its members turns Moore's automaton into exactly the minimized DFA of $M$, whose
states are the reachable continuation languages of $M$.

Formalized by `DFA.reindex_mooreDFA`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#reindex-moore-dfa).

## Moore's automaton has one state per Nerode class

For a DFA $M$ over a finite alphabet
with finitely many states, Moore's minimal automaton of $M$ has exactly as many states as there
are Nerode classes of the language accepted by $M$.

Formalized by `DFA.card_mooreState`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Moore.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Moore.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html#card-moore-state).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moore's algorithm](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/minimization/moore-s-algorithm)
