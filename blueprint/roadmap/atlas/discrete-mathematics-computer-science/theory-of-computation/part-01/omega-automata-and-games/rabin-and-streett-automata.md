---
declaration: section
origin: cited
lean: Cslib.Automata.NA.Rabin, Cslib.Automata.NA.Rabin.mem_language_iff, Cslib.Automata.NA.Rabin.toMuller, Cslib.Automata.NA.Rabin.language_toMuller, Cslib.Automata.NA.Streett, Cslib.Automata.NA.Streett.mem_language_iff, Cslib.Automata.NA.Streett.toMuller, Cslib.Automata.NA.Streett.language_toMuller
statement: formalized
proof: formalized
---

# Rabin and Streett automata

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html).

## Rabin

## Rabin automaton

A Rabin automaton is a nondeterministic automaton together with a set
of Rabin pairs $(E, F)$, each a pair of sets of states. A run is accepting when some pair is
hit: the run visits $E$ infinitely often and $F$ only finitely often.

Formalized by `Cslib.Automata.NA.Rabin`, a structure declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#rabin).

## Membership in the language of a Rabin automaton

An infinite word $x$ is accepted by a
Rabin automaton $r$ if and only if there is a run $s$ of $r$ on $x$ and a Rabin pair $(E, F)$ of
$r$ such that $s$ visits $E$ infinitely often and visits $F$ only finitely often.

Formalized by `Cslib.Automata.NA.Rabin.mem_language_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#mem-language-iff).

## Muller presentation of a Rabin automaton

Given a Rabin automaton with set of Rabin
pairs $\mathcal{R}$, this is the Muller automaton with the same states, initial states and
transitions whose accepting family consists of the sets $S$ of states for which some pair
$(E, F) \in \mathcal{R}$ satisfies $S \cap E \neq \emptyset$ and $S \cap F = \emptyset$. A
Muller automaton accepts a run when the set of states that the run visits infinitely often
belongs to its accepting family.

Formalized by `Cslib.Automata.NA.Rabin.toMuller`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-muller).

## Rabin-to-Muller conversion preserves the language

If the state space is finite, then a
Rabin automaton $r$ accepts the same language as its Muller presentation: the Muller automaton
with the same transitions and initial states as $r$ whose acceptance sets are the sets $S$ of
states such that, for some Rabin pair $(E, F)$ of $r$, $S$ meets $E$ and is disjoint from $F$.

Formalized by `Cslib.Automata.NA.Rabin.language_toMuller`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#language-to-muller).

## Streett automaton

A Streett automaton is a nondeterministic automaton together with a
set of Streett pairs $(E, F)$, each a pair of sets of states. A run is accepting when every pair
is respected: if the run visits $E$ infinitely often then it also visits $F$ infinitely often.

Formalized by `Cslib.Automata.NA.Streett`, a structure declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#streett).

## Membership in the language of a Streett automaton

An infinite word $x$ is accepted by a
Streett automaton $r$ if and only if there is a run $s$ of $r$ on $x$ such that for every Streett
pair $(E, F)$ of $r$, if $s$ visits $E$ infinitely often then $s$ visits $F$ infinitely often.

Formalized by `Cslib.Automata.NA.Streett.mem_language_iff`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#mem-language-iff-2).

## Muller presentation of a Streett automaton

Given a Streett automaton with set of
Streett pairs $\mathcal{P}$, this is the Muller automaton with the same states, initial states
and transitions whose accepting family consists of the sets $S$ of states such that every pair
$(E, F) \in \mathcal{P}$ with $S \cap E \neq \emptyset$ also satisfies $S \cap F \neq \emptyset$.
A Muller automaton accepts a run when the set of states that the run visits infinitely often
belongs to its accepting family.

Formalized by `Cslib.Automata.NA.Streett.toMuller`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-muller-2).

## Streett-to-Muller conversion preserves the language

If the state space is finite, then a
Streett automaton $r$ accepts the same language as its Muller presentation: the Muller automaton
with the same transitions and initial states as $r$ whose acceptance sets are the sets $S$ of
states such that, for every Streett pair $(E, F)$ of $r$, if $S$ meets $E$ then $S$ meets $F$.

Formalized by `Cslib.Automata.NA.Streett.language_toMuller`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#language-to-muller-2).

## Rabin presentation of a parity automaton

Given a parity automaton with priority
function $\Omega$ from states to natural numbers, this is the Rabin automaton with the same
states, initial states and transitions whose Rabin pairs are the pairs $(E_i, F_i)$ for
$i \in \mathbb{N}$, where $E_i = \{s : \Omega(s) = 2i\}$ and $F_i = \{s : \Omega(s) > 2i\}$.

Formalized by `Cslib.Automata.NA.Parity.toRabin`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-rabin).

## Parity-to-Rabin conversion preserves the language

If the state space is finite, then a
parity automaton $a$ accepts the same language as its Rabin presentation: the Rabin automaton
with the same transitions and initial states as $a$ whose Rabin pairs are the pairs
$(E_i, F_i)$ for $i \in \mathbb{N}$, where $E_i$ is the set of states of priority $2i$ and
$F_i$ the set of states of priority greater than $2i$.

Formalized by `Cslib.Automata.NA.Parity.language_toRabin`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#language-to-rabin).

## Streett presentation of a parity automaton

Given a parity automaton with priority
function $\Omega$ from states to natural numbers, this is the Streett automaton with the same
states, initial states and transitions whose Streett pairs are the pairs $(E_i, F_i)$ for
$i \in \mathbb{N}$, where $E_i = \{s : \Omega(s) = 2i + 1\}$ and
$F_i = \{s : \Omega(s) > 2i + 1\}$.

Formalized by `Cslib.Automata.NA.Parity.toStreett`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-streett).

## Parity-to-Streett conversion preserves the language

If the state space is finite, then
a parity automaton $a$ accepts the same language as its Streett presentation: the Streett
automaton with the same transitions and initial states as $a$ whose Streett pairs are the pairs
$(E_i, F_i)$ for $i \in \mathbb{N}$, where $E_i$ is the set of states of priority $2i + 1$ and
$F_i$ the set of states of priority greater than $2i + 1$.

Formalized by `Cslib.Automata.NA.Parity.language_toStreett`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#language-to-streett).

## Muller presentation of a parity automaton

The Muller automaton of a parity automaton
is the Muller presentation of its Rabin presentation. It has the same states, initial states
and transitions, and its accepting family consists of the sets $S$ of states for which there
is a natural number $i$ such that $S$ contains a state of priority $2i$ and no state of
priority greater than $2i$. A Muller automaton accepts a run when the set of states that the
run visits infinitely often belongs to its accepting family.

Formalized by `Cslib.Automata.NA.Parity.toMuller`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-muller-3).

## Parity-to-Muller conversion preserves the language

If the state space is finite, then a
parity automaton accepts the same language as its Muller presentation, the Muller automaton
obtained by converting it to its Rabin presentation and that to a Muller automaton.

Formalized by `Cslib.Automata.NA.Parity.language_toMuller`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#language-to-muller-3).

## Streett automaton with the pairs of a Rabin automaton

Given a Rabin automaton, this is
the Streett automaton with the same states, initial states and transitions and the same set
of pairs.

For a fixed run and a pair $(E, F)$, the Streett condition (if the run visits $E$ infinitely
often, then it visits $F$ infinitely often) is the negation of the Rabin condition (the run
visits $E$ infinitely often and $F$ only finitely often).

Formalized by `Cslib.Automata.NA.Rabin.toStreett`, a definition declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#to-streett-2).

## Run-wise Rabin/Streett duality

Let $r$ be a Rabin automaton and let $s$ be an infinite
sequence of states. Then $s$ satisfies the Rabin condition of $r$, that is, for some Rabin pair
$(E, F)$ of $r$ the sequence $s$ visits $E$ infinitely often and $F$ only finitely often, if and
only if $s$ fails the Streett condition with the same pairs, that is, it is not the case that for
every Rabin pair $(E, F)$ of $r$, if $s$ visits $E$ infinitely often then $s$ visits $F$
infinitely often.

The sequence $s$ need not be a run of $r$. (For languages of nondeterministic automata there is
no such complementation statement, since complementation also swaps the run quantifier.)

Formalized by `Cslib.Automata.NA.Rabin.acceptsRun_iff_not_streett`, a theorem declared in [CSLibExt/Computability/Automata/NA/RabinStreett.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Automata/NA/RabinStreett.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html#accepts-run-iff-not-streett).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rabin and Streett automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/rabin-and-streett-automata)
