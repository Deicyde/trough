---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.StringMatching.computeTransition, Cslib.Algorithms.Lean.StringMatching.computeTransition_spec, Cslib.Algorithms.Lean.StringMatching.computeTransition_time_le, Cslib.Algorithms.Lean.StringMatching.patternAutomaton, Cslib.Algorithms.Lean.StringMatching.patternAutomaton_state, Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches, Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches_time, Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches_ret
statement: formalized
proof: formalized
---

# String matching with finite automata

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html).

## Transition table of the string-matching automaton

Let $P$ be a pattern of length $m$
over the alphabet $\{0, \dots, A-1\}$ and write $P_k$ for its prefix of length $k$. This timed
computation returns a table of $(m+1)A$ entries in $\{0, \dots, m\}$, stored row by row: for
each state $q \le m$ and symbol $a < A$, the entry at index $qA + a$ is found by trying
$k = \min(m, q+1)$ and then each smaller value in turn, and is the first $k$ for which $P_k$ is
a suffix of the word $P_q a$ (the candidate $k = 0$ is always accepted). The cost counts
one unit for each candidate $k$ tried, one for each symbol comparison executed when comparing
$P_k$ with the last $k$ symbols of $P_q a$ (left to right, stopping at the first mismatch), one
for each move to a smaller candidate, and one for each table entry written.

## Sources

- CLRS fourth edition section 32.3, decreasing-candidate row-major construction.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeTransition`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#compute-transition).

## Correctness of the string-matching transition table

Let $P$ be a pattern of length $m$
over the alphabet $\{0, \dots, A-1\}$ and write $P_k$ for its prefix of length $k$. For every
state $q \le m$ and symbol $a < A$, the entry at index $qA + a$ of the transition table of $P$
is the greatest $k \le m$ such that $P_k$ is a suffix of the word $P_q a$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeTransition_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#compute-transition-spec).

## Cost bound for the string-matching transition table

For every pattern of length $m$
over the alphabet $\{0, \dots, A-1\}$, the cost of computing its transition table is at most
$2A(m+1)^3$.

The cost counts executed candidates, symbol comparisons, failed decrements and table writes.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeTransition_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#compute-transition-time-le).

## String-matching automaton

For a pattern $P$ of length $m$ over the alphabet
$\{0, \dots, A-1\}$, the string-matching automaton of $P$ is the deterministic finite automaton
with states $\{0, \dots, m\}$, input symbols $\{0, \dots, A-1\}$, start state $0$, accepting set
$\{m\}$, and transition from state $q$ on symbol $a$ given by the entry at index $qA + a$ of the
transition table of $P$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.patternAutomaton`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#pattern-automaton).

## The string-matching automaton tracks the longest matched prefix

Let $P$ be a pattern of
length $m$ over the alphabet $\{0, \dots, A-1\}$ and write $P_k$ for its prefix of length $k$.
For every word $w$ over this alphabet, the state that the string-matching automaton of $P$
reaches from its start state after reading $w$ is the greatest $k \le m$ such that $P_k$ is a
suffix of $w$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.patternAutomaton_state`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#pattern-automaton-state).

## Finite-automaton string matcher

Let $P$ be a pattern of length $m$ and $T$ a text over
the alphabet $\{0, \dots, A-1\}$. This timed computation first computes the transition table of
$P$, then runs through $T$ starting in state $0$: on reading the $i$-th symbol $a$ of $T$ in
state $q$ it moves to the state given by the table entry at index $qA + a$, and if that state is
$m$ it reports the shift $i - m$. If $m = 0$, the shift $0$ is also reported before the scan.
It returns the reported shifts in the order found. The cost is that of computing the table,
plus two units for each symbol of $T$ (a table lookup and an acceptance test), plus one unit for
each reported shift.

The table is computed once, before the single pass over the text, and the scan does not reset
after a match, so overlapping occurrences are reported.

Formalized by `Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#finite-automaton-matches).

## Exact cost of the finite-automaton matcher

For every pattern $P$ and text $T$ over the
alphabet $\{0, \dots, A-1\}$, where $T$ has length $n$, the cost of the finite-automaton matcher
on $P$ and $T$ equals the cost of computing the transition table of $P$, plus $2n$, plus the
number of shifts the matcher returns.

Formalized by `Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches_time`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#finite-automaton-matches-time).

## Correctness of the finite-automaton matcher

For every pattern $P$ and text $T$ over the
alphabet $\{0, \dots, A-1\}$, the list of shifts returned by the finite-automaton matcher equals
the list returned by the naive string matcher.

So it is the complete increasing list of zero-based shifts at which $P$ occurs in $T$, including
overlapping occurrences and, for the empty pattern, every boundary.

Formalized by `Cslib.Algorithms.Lean.StringMatching.finiteAutomatonMatches_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/FiniteAutomaton.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html#finite-automaton-matches-ret).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: String matching with finite automata](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/string-algorithms/string-matching-with-finite-automata)
