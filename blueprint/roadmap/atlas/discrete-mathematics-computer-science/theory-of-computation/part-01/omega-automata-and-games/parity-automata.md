---
declaration: section
origin: cited
lean: Cslib.Automata.NA.Parity, Cslib.Automata.NA.Parity.run_parityEven_or_parityOdd, Cslib.Automata.NA.Buchi.toParity, Cslib.Automata.NA.Buchi.language_toParity
statement: formalized
proof: formalized
---

# Parity automata

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html).

## Parity

## Nondeterministic parity automaton

A nondeterministic parity automaton with states in $Q$
and symbols in $\Sigma$ is a nondeterministic automaton (a transition relation labelled by
symbols on $Q$, together with a set of start states) with a priority $p(q) \in \mathbb{N}$
assigned to each state $q \in Q$.

Formalized by `Cslib.Automata.NA.Parity`, a structure declared in [CSLibExt/Computability/Automata/NA/Parity.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/Parity.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html#parity).

## Every state sequence of a finite parity automaton has a parity winner

Let $\mathcal{A}$
be a nondeterministic parity automaton with finitely many states and priority function $p$. For
every infinite sequence of states $s_0, s_1, s_2, \dots$, the priority sequence
$p(s_0), p(s_1), p(s_2), \dots$ satisfies the even or the odd max-parity condition: the largest
priority occurring infinitely often exists and is even, or it exists and is odd.

Formalized by `Cslib.Automata.NA.Parity.run_parityEven_or_parityOdd`, a theorem declared in [CSLibExt/Computability/Automata/NA/Parity.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/Parity.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html#run-parity-even-or-parity-odd).

## Büchi automata as parity automata

A nondeterministic Büchi automaton is turned into the
nondeterministic parity automaton with the same states, transitions and start states, in which
every accepting state has priority $2$ and every other state has priority $1$.

Formalized by `Cslib.Automata.NA.Buchi.toParity`, a definition declared in [CSLibExt/Computability/Automata/NA/Parity.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/Parity.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html#to-parity).

## Büchi-to-parity conversion preserves the language

Every nondeterministic Büchi automaton
accepts the same language of infinite words as its presentation as a parity automaton (priority
$2$ on accepting states, $1$ elsewhere).

Formalized by `Cslib.Automata.NA.Buchi.language_toParity`, a theorem declared in [CSLibExt/Computability/Automata/NA/Parity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/Parity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html#language-to-parity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/parity-automata)
