---
declaration: section
origin: cited
lean: DFA.revDet, DFA.revDet_eval, DFA.revDet_accepts, DFA.revDet_eval_eq_iff, DFA.MidState, DFA.brzozowskiMid, DFA.BrzozowskiState, DFA.brzozowski
statement: formalized
proof: formalized
---

# Brzozowski's algorithm

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html).

## Determinized reversal

## Determinized reversal of a DFA

For a DFA $M$ with finitely many states, the determinized
reversal of $M$ is the subset construction applied to the reversal of $M$: its states are the sets
of states of $M$; reading a letter $a$ from a set $S$ leads to the set of states $q$ whose
$a$-successor in $M$ lies in $S$; its start state is the set of accepting states of $M$; and it
accepts exactly the sets that contain the start state of $M$.

Formalized by `DFA.revDet`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#rev-det).

## States reached in the determinized reversal

Let $M$ be a DFA with finitely many states
and $w$ a word. On input $w$, the determinized reversal of $M$ reaches the set of states $q$ of
$M$ from which $M$, reading $w$ backwards starting at $q$, ends in an accepting state.

Formalized by `DFA.revDet_eval`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#rev-det-eval).

## The determinized reversal accepts the reversed language

Let $M$ be a DFA with finitely
many states and $L$ its language, and write $w^R$ for the word $w$ read backwards. The
determinized reversal of $M$ accepts exactly the reversed language $L^R = \{w \mid w^R \in L\}$.

Formalized by `DFA.revDet_accepts`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#rev-det-accepts).

## Brzozowski's lemma

Let $M$ be a DFA with finitely many states in which every state is
reached from the start state by some word, and let $L$ be its language. Write $u^R$ for the word
$u$ read backwards, $L^R = \{u \mid u^R \in L\}$ for the reversed language, and
$w^{-1}K = \{v \mid wv \in K\}$ for the left quotient of a language $K$ by a word $w$. Then two
words $w$ and $w'$ lead the determinized reversal of $M$ from its start state to the same set of
states if and only if $w^{-1}L^R = w'^{-1}L^R$.

Formalized by `DFA.revDet_eval_eq_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#rev-det-eval-eq-iff).

## States of the intermediate Brzozowski automaton

For a deterministic finite automaton $M$
over a finite alphabet with finite state set $Q$, the subsets of $Q$ reachable from the start state
in the subset construction of the reversal of $M$.

They are found by a reachability search of at most $2^{|Q|}$ rounds, the number of subsets, which
stops as soon as a round adds nothing.

Formalized by `DFA.MidState`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#mid-state).

## The intermediate Brzozowski automaton

For a deterministic finite automaton $M$ over a
finite alphabet with finitely many states, the subset construction of the reversal of $M$,
restricted to the subsets reachable from its start state.

Formalized by `DFA.brzozowskiMid`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-mid).

## States of Brzozowski's automaton

For a deterministic finite automaton $M$ over a finite
alphabet with finitely many states, the subsets of states of the intermediate Brzozowski automaton
of $M$ that are reachable from the start state in the subset construction of its reversal.

Formalized by `DFA.BrzozowskiState`, an abbreviation declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-state).

## Brzozowski's automaton

For a deterministic finite automaton $M$ over a finite alphabet
with finitely many states, the subset construction of the reversal of the intermediate Brzozowski
automaton of $M$, restricted to the subsets reachable from its start state. Equivalently: reverse,
determinize by the subset construction and keep the reachable subsets, twice.

Formalized by `DFA.brzozowski`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski).

## Every state of the intermediate Brzozowski automaton is reachable

For a deterministic
finite automaton $M$ over a finite alphabet with finitely many states, every state of the
intermediate Brzozowski automaton of $M$ (the subset construction of the reversal of $M$
restricted to its reachable subsets) is reached from its start state by some word.

Formalized by `DFA.brzozowskiMid_surjective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-mid-surjective).

## Every state of Brzozowski's automaton is reachable

For a deterministic finite automaton
$M$ over a finite alphabet with finitely many states, every state of Brzozowski's automaton of $M$
is reached from its start state by some word.

Formalized by `DFA.brzozowski_surjective`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-surjective).

## Brzozowski's automaton accepts the language of the original automaton

For a deterministic
finite automaton $M$ over a finite alphabet with finitely many states, Brzozowski's automaton of
$M$ accepts exactly the language of $M$.

Formalized by `DFA.brzozowski_accepts`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-accepts).

## Brzozowski's automaton identifies exactly the Nerode equivalent words

For a deterministic
finite automaton $M$ over a finite alphabet with finitely many states and words $w$ and $w'$,
Brzozowski's automaton of $M$ reaches the same state on $w$ as on $w'$ if and only if $w$ and $w'$
are Nerode equivalent for the language of $M$, that is, have the same left quotient.

Formalized by `DFA.brzozowski_eval_eq_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-eval-eq-iff).

## Residual language of a state of Brzozowski's automaton

For a deterministic finite
automaton $M$ over a finite alphabet with finitely many states, the map that sends a state $p$ of
Brzozowski's automaton of $M$ to the language accepted by $M$ from the state that $M$ reaches on
$w$, where $w$ is a chosen word leading Brzozowski's automaton from its start state to $p$; this
language is one of the residual languages of the reachable states of $M$.

Formalized by `DFA.brzozowskiResidual`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-residual).

## States of Brzozowski's automaton as residual languages

For a deterministic finite
automaton $M$ over a finite alphabet with finitely many states, the bijection from the states of
Brzozowski's automaton of $M$ to the residual languages of the reachable states of $M$ that sends
each state $p$ to the language accepted by $M$ from the state that $M$ reaches on $w$, where $w$
is a chosen word leading Brzozowski's automaton from its start state to $p$.

Formalized by `DFA.brzozowskiEquiv`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#brzozowski-equiv).

## Brzozowski's automaton is the minimal automaton

Let $M$ be a DFA over a finite alphabet
with finitely many states, and let $L$ be its language. For a language $K$ and a word $w$, write
$w^{-1}K = \{v \mid wv \in K\}$ for the left quotient of $K$ by $w$. Every state of Brzozowski's
automaton of $M$ is reached by some word $w$; rename that state to $w^{-1}L$, which does not
depend on the choice of $w$. The renamed automaton is exactly the minimized DFA of $M$: its states
are the left quotients of $L$ by words, its start state is $L$, reading a letter $a$ (a word of
length one) sends $K$ to $a^{-1}K$, and it accepts the $K$ that contain the empty word.

Formalized by `DFA.reindex_brzozowski`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Brzozowski.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Brzozowski.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html#reindex-brzozowski).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brzozowski's algorithm](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/minimization/brzozowski-s-algorithm)
