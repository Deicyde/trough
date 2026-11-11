---
declaration: section
origin: cited
lean: Cslib.ωLanguage.Example.infinitelyOften, Cslib.ωLanguage.Example.eventuallyAlways, Cslib.ωLanguage.Example.compl_infinitelyOften, Cslib.ωLanguage.Example.infinitelyOftenNa, Cslib.ωLanguage.Example.eventuallyAlwaysNa
statement: formalized
proof: formalized
---

# Büchi automata for infinitely often and eventually always

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html).

## Infinitely often

For a set $p$ of symbols, the ω-language “infinitely often $p$”
consists of the infinite words $x_0 x_1 x_2 \ldots$ with $x_k \in p$ for infinitely many $k$.

Formalized by `Cslib.ωLanguage.Example.infinitelyOften`, a definition declared in [CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html#infinitely-often).

## Eventually always

For a set $p$ of symbols, the ω-language “eventually always $p$”
consists of the infinite words $x_0 x_1 x_2 \ldots$ for which there is an $N$ with $x_k \in p$
for all $k \ge N$.

Formalized by `Cslib.ωLanguage.Example.eventuallyAlways`, a definition declared in [CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html#eventually-always).

## Complement of “infinitely often”

For every set $p$ of symbols, the complement of the
ω-language of infinite words with infinitely many letters in $p$ is the ω-language of infinite
words whose letters are eventually all in the complement of $p$.

Formalized by `Cslib.ωLanguage.Example.compl_infinitelyOften`, a theorem declared in [CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html#compl-infinitely-often).

## Two-state Büchi automaton for “infinitely often”

For a set $p$ of symbols, this is the
nondeterministic Büchi automaton over the alphabet of symbols with states $\mathsf{true}$ and
$\mathsf{false}$, single start state $\mathsf{true}$ and single accepting state $\mathsf{true}$,
in which reading a letter $x$ from either state leads to exactly one state: $\mathsf{true}$ if
$x \in p$ and $\mathsf{false}$ otherwise. So the state records whether the last letter read was
in $p$.

Formalized by `Cslib.ωLanguage.Example.infinitelyOftenNa`, a definition declared in [CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html#infinitely-often-na).

## Two-state Büchi automaton for “eventually always”

For a set $p$ of symbols, this is the
nondeterministic Büchi automaton over the alphabet of symbols with states $\mathsf{false}$ and
$\mathsf{true}$, single start state $\mathsf{false}$ and single accepting state $\mathsf{true}$.
From $\mathsf{false}$ it may read any letter and move to either state; from $\mathsf{true}$ it
may read only letters in $p$, and then it stays in $\mathsf{true}$.

Formalized by `Cslib.ωLanguage.Example.eventuallyAlwaysNa`, a definition declared in [CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ExampleInfinitelyOften.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html#eventually-always-na).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Büchi automata for infinitely often and eventually always](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/b-chi-automata-for-infinitely-often-and-eventual)
