---
declaration: section
origin: cited
lean: Cslib.Automata.NA.Buchi.Step, Cslib.Automata.NA.Buchi.HasLasso, Cslib.Automata.NA.Buchi.mem_language_iff, Cslib.Automata.NA.Buchi.lasso_mem_language, Cslib.Automata.NA.Buchi.hasLasso_of_mem, Cslib.Automata.NA.Buchi.language_nonempty_iff_hasLasso, Cslib.Automata.NA.Buchi.exists_lasso_word_of_nonempty, Cslib.Automata.NA.Buchi.exists_mTr_iff_reflTransGen
statement: formalized
proof: formalized
---

# Emptiness of Büchi automata

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html).

## Symbol-forgetting transition graph of a Büchi automaton

For a nondeterministic Büchi
automaton, the transition graph has an edge from a state $s$ to a state $t$ exactly when the
automaton has a transition from $s$ to $t$ reading some symbol.

Formalized by `Cslib.Automata.NA.Buchi.Step`, a definition declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#step).

## Lasso of a Büchi automaton

A nondeterministic Büchi automaton has a lasso if there are a
start state $s_0$ and an accepting state $s$ such that the automaton can move from $s_0$ to $s$ by
reading some finite word $u$, and from $s$ back to $s$ by reading some nonempty finite word
$v$.

Formalized by `Cslib.Automata.NA.Buchi.HasLasso`, a definition declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#has-lasso).

## Büchi acceptance condition

A nondeterministic Büchi automaton accepts an infinite word
$x = x_0 x_1 x_2 \cdots$ if and only if it has a run on $x$, that is, a sequence of states
$s_0 s_1 s_2 \cdots$ with $s_0$ a start state and a transition from $s_k$ to $s_{k+1}$ reading
$x_k$ for every $k$, such that $s_k$ is an accepting state for infinitely many $k$.

Formalized by `Cslib.Automata.NA.Buchi.mem_language_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#mem-language-iff).

## Lassos give accepted ultimately periodic words

Let $\mathcal{A}$ be a nondeterministic
Büchi automaton over a nonempty alphabet. Suppose $s_0$ is a start state and $s$ an accepting
state of $\mathcal{A}$, that reading the finite word $u$ the automaton can move from $s_0$ to $s$,
and that reading a nonempty finite word $v$ it can move from $s$ back to $s$. Then $\mathcal{A}$
accepts the infinite word $u v^\omega = u v v v \cdots$.

Formalized by `Cslib.Automata.NA.Buchi.lasso_mem_language`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#lasso-mem-language).

## An accepted word yields a lasso

If a nondeterministic Büchi automaton with finitely many
states accepts some infinite word, then it has a lasso: some accepting state is visited twice
along an accepting run, and the run between the two visits is the cycle.

Formalized by `Cslib.Automata.NA.Buchi.hasLasso_of_mem`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#has-lasso-of-mem).

## Lasso characterization of Büchi nonemptiness

For finitely many states, the language
of a nondeterministic Büchi automaton is nonempty iff some accepting state is reachable from a
start state and lies on a nonempty cycle.

Formalized by `Cslib.Automata.NA.Buchi.language_nonempty_iff_hasLasso`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#language-nonempty-iff-has-lasso).

## Nonempty Büchi languages contain ultimately periodic words

Let $A$ be a
nondeterministic Büchi automaton with finitely many states over a nonempty alphabet. If $A$
accepts some infinite word, then there are finite words $u$ and $v$ with $v$ nonempty such that
$A$ accepts the ultimately periodic word $u v^\omega = u v v v \cdots$.

Formalized by `Cslib.Automata.NA.Buchi.exists_lasso_word_of_nonempty`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#exists-lasso-word-of-nonempty).

## Reachability by words is reachability in the transition graph

For states $s$ and $t$ of
a nondeterministic Büchi automaton, the automaton can move from $s$ to $t$ by reading some finite
word (possibly empty) if and only if $t$ is reachable from $s$ in zero or more steps of the
transition graph, which has an edge from $p$ to $q$ when some symbol takes $p$ to $q$.

Formalized by `Cslib.Automata.NA.Buchi.exists_mTr_iff_reflTransGen`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#exists-m-tr-iff-refl-trans-gen).

## Nonempty words and paths of positive length

For states $s$ and $t$ of a
nondeterministic Büchi automaton, the automaton can move from $s$ to $t$ by reading some nonempty
finite word if and only if $t$ is reachable from $s$ in one or more steps of the transition
graph, which has an edge from $p$ to $q$ when some symbol takes $p$ to $q$.

Formalized by `Cslib.Automata.NA.Buchi.exists_ne_nil_mTr_iff_transGen`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#exists-ne-nil-m-tr-iff-trans-gen).

## The lasso condition in the transition graph

A nondeterministic Büchi automaton has a
lasso if and only if there are a start state $s_0$ and an accepting state $s$ such that $s$ is
reachable from $s_0$ in zero or more steps of the transition graph and $s$ is reachable from
itself in one or more steps; the transition graph has an edge from $p$ to $q$ when some symbol
takes $p$ to $q$.

Formalized by `Cslib.Automata.NA.Buchi.hasLasso_iff_reachable`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#has-lasso-iff-reachable).

## Finite set of start states

For a nondeterministic Büchi automaton with finitely many
states and a decidable start set, this is the set of its start states, viewed as a finite set.

Formalized by `Cslib.Automata.NA.Buchi.startFin`, a definition declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#start-fin).

## Lasso states of a finite Büchi automaton

For a nondeterministic Büchi automaton with
finitely many states, decidable equality of states, a finite alphabet, and decidable transitions,
start set and accepting set, the lasso states form the finite set of accepting states $s$ that are
reachable from some start state in zero or more transitions and lie on a nonempty cycle, that is,
$s$ is reachable from itself in one or more transitions.

The set is computed by one reachability closure from all start states, then one cycle closure for
each reachable accepting state; each closure takes as many rounds as there are states.

Formalized by `Cslib.Automata.NA.Buchi.lassoStates`, a definition declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#lasso-states).

## Lasso detection by finite reachability

Let $A$ be a nondeterministic Büchi automaton
with finitely many states and finitely many symbols, with decidable equality of states, and whose
transitions, start states and accepting states are decidable. Then $A$ has a lasso if and only if
its set of lasso states, computed by finite reachability closures as the accepting states that are
reachable from a start state and lie on a nonempty cycle, is nonempty.

Formalized by `Cslib.Automata.NA.Buchi.hasLasso_iff_lassoStates_nonempty`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#has-lasso-iff-lasso-states-nonempty).

## Büchi emptiness test

For a nondeterministic Büchi automaton with finitely many states and
finitely many symbols, with decidable equality of states, and whose transitions, start states and
accepting states are decidable, the emptiness test returns true exactly when the automaton has no
lasso. It decides this by computing the set of lasso states; by the lasso characterization, it
returns true iff no infinite word is accepted.

With $n$ states, $f$ reachable accepting states and $k$ symbols, the computation performs at most
$f + 1$ reachability closures of $O(n^3 k)$ transition tests each.

Formalized by `Cslib.Automata.NA.Buchi.isEmptyB`, a definition declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#is-empty-b).

## Correctness of the Büchi emptiness test

For a nondeterministic Büchi automaton with
finitely many states and finitely many symbols, with decidable equality of states, and whose
transitions, start states and accepting states are decidable, the emptiness test returns true if
and only if the automaton accepts no infinite word.

Formalized by `Cslib.Automata.NA.Buchi.isEmptyB_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/BuchiEmptiness.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html#is-empty-b-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emptiness of Büchi automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/emptiness-of-b-chi-automata)
