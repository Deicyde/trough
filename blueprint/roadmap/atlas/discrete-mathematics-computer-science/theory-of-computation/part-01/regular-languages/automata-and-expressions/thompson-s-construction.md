---
declaration: section
origin: cited
lean: Cslib.Automata.Thompson.zeroAut, Cslib.Automata.Thompson.oneAut, Cslib.Automata.Thompson.charAut, Cslib.Automata.Thompson.union, Cslib.Automata.Thompson.concat, Cslib.Automata.Thompson.star, Cslib.Automata.Thompson.State, Cslib.Automata.Thompson.toεNFA
statement: formalized
proof: formalized
---

# Thompson's construction

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html).

## Basic automata

## The ε-NFA with no states

Over an alphabet $\alpha$, this is the ε-NFA whose set of
states is empty; consequently it has no start states, no accepting states and no transitions.

Formalized by `Cslib.Automata.Thompson.zeroAut`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#zero-aut).

## One-state automaton

The ε-NFA over the alphabet $\alpha$ with a single state, which is both
its start state and its accepting state, and no moves at all (neither letter moves nor
ε-moves).

Formalized by `Cslib.Automata.Thompson.oneAut`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#one-aut).

## Single-letter automaton

For a letter $a$ of the alphabet $\alpha$, this is the ε-NFA over
$\alpha$ with two states, a start state and an accepting state, and a single move, which reads $a$
and goes from the start state to the accepting state; it has no other moves and no ε-moves.

Formalized by `Cslib.Automata.Thompson.charAut`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#char-aut).

## Union of ε-NFAs

Given ε-NFAs $M$ with state set $\sigma$ and $N$ with state set $\tau$ over
the same alphabet, their union is the ε-NFA on the disjoint union $\sigma \sqcup \tau$ whose moves
are the moves of $M$ and the moves of $N$, whose start states are the start states of $M$ and of
$N$, and whose accepting states are the accepting states of $M$ and of $N$.

Formalized by `Cslib.Automata.Thompson.union`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#union).

## Concatenation of ε-NFAs

Given ε-NFAs $M$ with state set $\sigma$ and $N$ with state set
$\tau$ over the same alphabet, their concatenation is the ε-NFA on the disjoint union
$\sigma \sqcup \tau$ whose moves are the moves of $M$, the moves of $N$, and an ε-move from every
accepting state of $M$ to every start state of $N$. Its start states are the start states of $M$
and its accepting states are the accepting states of $N$.

Formalized by `Cslib.Automata.Thompson.concat`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#concat).

## Kleene star of an ε-NFA

Given an ε-NFA $M$ with state set $\sigma$, its star automaton has
the states of $M$ together with one new state $q_0$, which is its only start state and its only
accepting state. Its moves are the moves of $M$, an ε-move from $q_0$ to every start state of $M$,
and an ε-move from every accepting state of $M$ to $q_0$.

Formalized by `Cslib.Automata.Thompson.star`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#star).

## States of Thompson's automaton

The state set $S(r)$ of Thompson's automaton of a regular
expression $r$ is defined by structural recursion: $S(0)$ is empty, $S(\varepsilon)$ has one
element, $S(a)$ has two elements for a letter $a$, both $S(P + Q)$ and $S(PQ)$ are the disjoint
union $S(P) \sqcup S(Q)$, and $S(P^*)$ is $S(P)$ together with one new element.

Formalized by `Cslib.Automata.Thompson.State`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#state).

## Thompson's construction

To each regular expression $r$ over an alphabet $\alpha$ it assigns
an ε-NFA over $\alpha$ with state set $S(r)$, the states of Thompson's automaton of $r$, by
structural recursion: $0$ goes to the automaton with no states, $\varepsilon$ to the one-state
automaton, a letter $a$ to the single-letter automaton of $a$, $P + Q$ to the union of the
automata of $P$ and $Q$, $PQ$ to their concatenation, and $P^*$ to the star automaton of the
automaton of $P$.

Formalized by `Cslib.Automata.Thompson.toεNFA`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#to-nfa).

## Correctness of Thompson's construction

The automaton accepts exactly the words the
regular expression matches.

Formalized by `Cslib.Automata.Thompson.accepts_toεNFA`, a theorem declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#accepts-to-nfa).

## Thompson state count

The state count $n(r)$ of a regular expression $r$ is defined by
structural recursion: $n(0) = 0$, $n(\varepsilon) = 1$, $n(a) = 2$ for a letter $a$,
$n(P + Q) = n(P) + n(Q)$, $n(PQ) = n(P) + n(Q)$ and $n(P^*) = n(P) + 1$.

It is the number of states of Thompson's automaton of $r$.

Formalized by `Cslib.Automata.Thompson.numStates`, a definition declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#num-states).

## Number of states of Thompson's automaton

For every regular expression $r$, the number of
states of Thompson's automaton of $r$ is $n(r)$, the Thompson state count of $r$: $n(0) = 0$,
$n(\varepsilon) = 1$, $n(a) = 2$ for a letter $a$, $n(P + Q) = n(P) + n(Q)$, $n(PQ) = n(P) + n(Q)$
and $n(P^*) = n(P) + 1$.

Formalized by `Cslib.Automata.Thompson.card_state`, a theorem declared in [CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/EpsilonNA/Thompson.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html#card-state).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thompson's construction](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/thompson-s-construction)
