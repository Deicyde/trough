---
declaration: section
origin: cited
lean: Cslib.Automata.NA.GenBuchi, Cslib.Automata.NA.GenBuchi.mem_language_iff, Cslib.Automata.NA.GenBuchi.nextCount, Cslib.Automata.NA.GenBuchi.nextCount_eq_self, Cslib.Automata.NA.GenBuchi.nextCount_eq_succ, Cslib.Automata.NA.GenBuchi.nextCount_eq_zero, Cslib.Automata.NA.GenBuchi.countSeq, Cslib.Automata.NA.GenBuchi.countSeq_zero
statement: formalized
proof: formalized
---

# Generalized Büchi automata

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html).

## Generalized Büchi automata and degeneralization

## Generalized Büchi automaton

A generalized Büchi automaton with states $S$ and symbols
$\Sigma$ is a nondeterministic automaton (a labelled transition relation on $S$ together with a
set of start states) equipped with a natural number $k$ and $k$ acceptance sets
$F_0, \dots, F_{k-1} \subseteq S$. A run is accepting when it visits every acceptance set
infinitely often.

Formalized by `Cslib.Automata.NA.GenBuchi`, a structure declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#gen-buchi).

## Language of a generalized Büchi automaton

An infinite word $x$ belongs to the language of
a generalized Büchi automaton $g$ with acceptance sets $F_0, \dots, F_{k-1}$ iff there is a run
$s$ of $g$ on $x$ such that for every $j < k$ there are infinitely many times $t$ with
$s_t \in F_j$. Here a run of $g$ on $x$ is an infinite sequence of states $s_0, s_1, \dots$ with
$s_0$ a start state and a transition from $s_i$ to $s_{i+1}$ labelled $x_i$ for every $i$.

Formalized by `Cslib.Automata.NA.GenBuchi.mem_language_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#mem-language-iff).

## Counter update for degeneralization

Let $g$ be a generalized Büchi automaton with
acceptance sets $F_0, \dots, F_{k-1}$. The counter update takes a counter value
$i \in \{0, \dots, k\}$ and a state $t$ of $g$ and returns a counter value in $\{0, \dots, k\}$:
if $i < k$, it returns $i + 1$ when $t \in F_i$ and $i$ when $t \notin F_i$; if $i = k$, it
returns $0$.

Formalized by `Cslib.Automata.NA.GenBuchi.nextCount`, a definition declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#next-count).

## The degeneralization counter stays when the awaited set is missed

Let $g$ be a
generalized Büchi automaton with acceptance sets $F_0, \dots, F_{k-1}$ and counter update
$\mathrm{next}$. If $i \in \{0, \dots, k\}$ satisfies $i < k$ and the state $t$ is not in $F_i$,
then $\mathrm{next}(i, t) = i$.

Formalized by `Cslib.Automata.NA.GenBuchi.nextCount_eq_self`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#next-count-eq-self).

## The degeneralization counter advances on a hit

Let $g$ be a generalized Büchi automaton
with acceptance sets $F_0, \dots, F_{k-1}$, let $i \in \{0, \dots, k\}$ be a counter value and let
$t$ be a state of $g$. If $i < k$ and $t \in F_i$, then the counter update of $i$ at $t$ is
$i + 1$.

Formalized by `Cslib.Automata.NA.GenBuchi.nextCount_eq_succ`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#next-count-eq-succ).

## The degeneralization counter resets at the top

Let $g$ be a generalized Büchi automaton
with $k$ acceptance sets and let $i \in \{0, \dots, k\}$ be a counter value. If $i = k$, then for
every state $t$ of $g$ the counter update of $i$ at $t$ is $0$.

Formalized by `Cslib.Automata.NA.GenBuchi.nextCount_eq_zero`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#next-count-eq-zero).

## Counter sequence of a state sequence

Let $g$ be a generalized Büchi automaton with $k$
acceptance sets and let $s = (s_0, s_1, \dots)$ be an infinite sequence of states. The counter
sequence $c_0, c_1, \dots$ of $s$, with values in $\{0, \dots, k\}$, is defined by $c_0 = 0$ and
$c_{n+1} = \mathrm{next}(c_n, s_{n+1})$, where $\mathrm{next}$ is the counter update of $g$. So
$c_n$ is the counter after reading the states $s_1, \dots, s_n$; the state $s_0$ is not read.

Formalized by `Cslib.Automata.NA.GenBuchi.countSeq`, a definition declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#count-seq).

## The counter sequence starts at zero

For every generalized Büchi automaton $g$ and every
infinite sequence of states $s$, the counter sequence of $s$ has value $0$ at time $0$.

Formalized by `Cslib.Automata.NA.GenBuchi.countSeq_zero`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#count-seq-zero).

## Recursion step of the counter sequence

Let $g$ be a generalized Büchi automaton, $s$ an
infinite sequence of states, and $c_0, c_1, \dots$ the counter sequence of $s$. For every $n$,
$c_{n+1} = \mathrm{next}(c_n, s_{n+1})$, where $\mathrm{next}$ is the counter update of $g$.

Formalized by `Cslib.Automata.NA.GenBuchi.countSeq_succ`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#count-seq-succ).

## The degeneralization counter waits for the awaited set

Let $g$ be a generalized Büchi
automaton with acceptance sets $F_0, \dots, F_{k-1}$, let $s$ be an infinite sequence of states
with counter sequence $c_0, c_1, \dots$, and let $i < k$ and $n$ satisfy $c_n = i$. If $m \ge n$
and $s_{j+1} \notin F_i$ for every $j$ with $n \le j < m$, then $c_m = i$.

Formalized by `Cslib.Automata.NA.GenBuchi.countSeq_stay`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#count-seq-stay).

## The degeneralization counter reaches every higher value

Let $g$ be a generalized Büchi
automaton with acceptance sets $F_0, \dots, F_{k-1}$, and let $s$ be an infinite sequence of
states that visits every $F_j$ infinitely often, with counter sequence $c_0, c_1, \dots$. Then
for every time $n$ and every $j$ with $c_n \le j \le k$ there is a time $m \ge n$ with $c_m = j$.

The distance $d = j - c_n$ appears in the statement as a separate variable, and the proof is by
induction on $d$: the first visit to the awaited set after time $n$ advances the counter by one
(the counter stays put until then).

Formalized by `Cslib.Automata.NA.GenBuchi.countSeq_reach`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#count-seq-reach).

## The degeneralization counter crosses every value below its target

Let $g$ be a
generalized Büchi automaton with acceptance sets $F_0, \dots, F_{k-1}$ and counter update
$\mathrm{next}$, let $s$ be an infinite sequence of states, and let $c_0, c_1, \dots$ be any
sequence in $\{0, \dots, k\}$ with $c_{n+1} = \mathrm{next}(c_n, s_{n+1})$ for every $n$. Let
$a \le b$ be times with $c_a = 0$ and $c_b = d \le k$, and suppose $c_t \ne k$ for every $t$ with
$a < t < b$. Then for every $j < d$ there is a time $t$ with $a \le t < b$ such that $c_t = j$,
$c_{t+1} = j + 1$ and $s_{t+1} \in F_j$.

The proof is by induction on $b$, case-splitting the last counter step into stay, advance, or
the impossible reset.

Formalized by `Cslib.Automata.NA.GenBuchi.counter_cross`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#counter-cross).

## Degeneralization of a generalized Büchi automaton

Let $g$ be a generalized Büchi
automaton with $k$ acceptance sets. Its degeneralization is the Büchi automaton over the same
alphabet whose states are the pairs $(s, i)$ of a state $s$ of $g$ and a counter value
$i \in \{0, \dots, k\}$. On a symbol $x$ there is a transition from $(s, i)$ to $(s', i')$ iff $g$
has a transition from $s$ to $s'$ on $x$ and $i'$ is the counter update of $i$ at the state $s'$.
The start states are the pairs $(s, 0)$ with $s$ a start state of $g$, and the accepting states
are the pairs $(s, k)$.

Formalized by `Cslib.Automata.NA.GenBuchi.toBuchi`, a definition declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#to-buchi).

## Degeneralization preserves the language

A word is accepted by the
degeneralized Büchi automaton iff it is accepted by the generalized Büchi
automaton.

Formalized by `Cslib.Automata.NA.GenBuchi.language_toBuchi`, a theorem declared in [CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Automata/NA/GeneralizedBuchi.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html#language-to-buchi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Büchi automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/generalized-b-chi-automata)
