---
declaration: section
origin: cited
lean: DFA.symmDiff, DFA.reachStep, DFA.reachable, DFA.mem_reachable_iff, DFA.start_mem_reachable, DFA.step_mem_reachable, DFA.reachableWithin, DFA.reachableWithin_eq_reachable
statement: formalized
proof: formalized
---

# Decision procedures for finite automata

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html).

## Symmetric difference of two DFAs

For DFAs $M$ and $N$ over the same alphabet, with sets of
states $\sigma$ and $\sigma'$, this is the product DFA with set of states $\sigma \times \sigma'$
whose start state is the pair of the start states of $M$ and $N$, whose transition takes $(p, q)$
on a letter $a$ to the pair of the state to which $M$ moves from $p$ on $a$ and the state to which
$N$ moves from $q$ on $a$, and whose accepting states are the pairs $(p, q)$ such that $p$ is an
accepting state of $M$ or $q$ is an accepting state of $N$, but not both.

It accepts exactly the words on which $M$ and $N$ disagree.

Formalized by `DFA.symmDiff`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#symm-diff).

## One round of the DFA reachability search

Let $M$ be a DFA over a finite alphabet
$\alpha$. The round sends a finite set $S$ of states of $M$ to the set consisting of the start
state of $M$ and of every state that the transition function of $M$ takes some $s \in S$ to on
some letter $a \in \alpha$.

Formalized by `DFA.reachStep`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reach-step).

## Reachable states of a DFA

Let $M$ be a DFA over a finite alphabet whose set of states
$\sigma$ is finite and has decidable equality. The reachable states of $M$ form the finite set
obtained from the empty set by applying one round of the DFA reachability search for $M$ exactly
$|\sigma|$ times, where $|\sigma|$ is the number of states of $M$.

Since the round is monotone, this set is its least fixed point, and a state lies in it exactly
when $M$ reaches it from its start state on some word.

Formalized by `DFA.reachable`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reachable).

## A state is reachable exactly when some word leads to it

Let $M$ be a DFA over a finite
alphabet with finitely many states. A state $s$ of $M$ is in the set of reachable states of $M$
if and only if there is a word $w$ such that running $M$ on $w$ from its start state ends in $s$.

Formalized by `DFA.mem_reachable_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#mem-reachable-iff).

## The start state is reachable

For a DFA $M$ over a finite alphabet with finitely many
states, the start state of $M$ belongs to the reachable states of $M$.

Formalized by `DFA.start_mem_reachable`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#start-mem-reachable).

## Reachable states are closed under transitions

Let $M$ be a DFA over a finite alphabet whose
set of states is finite and has decidable equality. If a state $s$ of $M$ is reachable from the
start state, then for every letter $a$ the state to which $M$ moves from $s$ on $a$ is also
reachable from the start state.

Formalized by `DFA.step_mem_reachable`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#step-mem-reachable).

## Early-stopping DFA reachability search

Let $M$ be a DFA over a finite alphabet whose set
of states has decidable equality. For a natural number $n$ and a finite set $S$ of states of $M$,
the reachability search from $S$ with at most $n$ rounds returns $S$ when $n = 0$. When
$n = k + 1$, it returns $S$ if one round of the reachability search for $M$ sends $S$ to $S$
itself, and otherwise it returns the search from the image of $S$ under that round with at most
$k$ rounds.

Formalized by `DFA.reachableWithin`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reachable-within).

## The early-stopping search finds exactly the reachable states

Let $M$ be a DFA over a
finite alphabet with finitely many states. For every natural number $n$ at least the number of
states of $M$, the early-stopping reachability search for $M$ from the empty set with at most $n$
rounds returns the set of reachable states of $M$.

Since the search stops once a round changes nothing, a generous bound costs nothing.

Formalized by `DFA.reachableWithin_eq_reachable`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reachable-within-eq-reachable).

## Accessible part of a DFA, by a bounded search

Let $M$ be a DFA over a finite alphabet
$\alpha$ with a finite state set $\sigma$ with decidable equality, and let $n \ge |\sigma|$. The
accessible part of $M$ found with $n$ rounds is the DFA over $\alpha$ whose states are the states
found by the reachability search from the empty set with at most $n$ rounds, whose start state is
the start state of $M$, whose transition function is that of $M$ restricted to these states, and
whose accepting states are those of them that $M$ accepts.

Since $n \ge |\sigma|$, the search finds exactly the states that some word leads to from the start
state of $M$, and it stops as soon as a round adds nothing, so a larger bound costs nothing.

Formalized by `DFA.accessiblePartWithin`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#accessible-part-within).

## Accessible part of a DFA

Let $M$ be a DFA over a finite alphabet $\alpha$ with a finite
state set $\sigma$ with decidable equality. The accessible part of $M$ is its accessible part found
by the reachability search with $|\sigma|$ rounds: the DFA over $\alpha$ whose states are the
states found by the reachability search from the empty set with at most $|\sigma|$ rounds (exactly
the states that some word leads to from the start state of $M$), whose start state is the start
state of $M$, whose transition function is that of $M$ restricted to these states, and whose
accepting states are those of them that $M$ accepts.

Formalized by `DFA.accessiblePart`, an abbreviation declared in [CSLibExt/Computability/Decidability/Regular.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#accessible-part).

## Every state of the accessible part is reached

Let $M$ be a DFA over a finite alphabet
$\alpha$ with a finite state set $\sigma$ with decidable equality, and let $n \ge |\sigma|$. For
every state $p$ of the accessible part of $M$ found with $n$ rounds, some word $w$ leads the
accessible part from its start state to $p$.

Formalized by `DFA.accessiblePartWithin_surjective`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#accessible-part-within-surjective).

## Emptiness test for DFAs

For a DFA $M$ over a finite alphabet with finitely many states,
the emptiness test returns true exactly when none of the reachable states of $M$ is an
accepting state.

Formalized by `DFA.isEmptyB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-empty-b).

## The emptiness test decides emptiness of DFAs

Let $M$ be a DFA over a finite alphabet
with finitely many states. The emptiness test applied to $M$ returns true if and only if the
language accepted by $M$ is empty.

Formalized by `DFA.isEmptyB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-empty-b-iff).

## Universality test for DFAs

For a DFA $M$ over a finite alphabet with finitely many
states, the universality test applied to $M$ is the emptiness test applied to the complement of
$M$: the DFA with the same states, start state and transitions whose accepting states are the
states that $M$ does not accept.

Formalized by `DFA.isUnivB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-univ-b).

## The universality test decides universality of DFAs

Let $M$ be a DFA over a finite
alphabet with finitely many states. The universality test applied to $M$ returns true if and
only if $M$ accepts every word over the alphabet.

Formalized by `DFA.isUnivB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-univ-b-iff).

## Equivalence test for DFAs

Let $M$ and $N$ be DFAs over the same finite alphabet, with
finite state sets with decidable equality and decidable sets of accepting states. Their symmetric
difference is the product DFA on pairs of states that starts at the pair of start states, moves on
a letter by moving both components, and accepts a pair $(p, q)$ when exactly one of the statements
"$M$ accepts $p$" and "$N$ accepts $q$" holds. The equivalence test of $M$ and $N$ is the emptiness
test of their symmetric difference: the Boolean that is true exactly when no pair of states
reachable from the start pair is accepting.

Formalized by `DFA.equivB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#equiv-b).

## Correctness of the equivalence test for DFAs

Let $M$ and $N$ be DFAs over the same finite
alphabet, with finite state sets with decidable equality and decidable sets of accepting states.
The equivalence test of $M$ and $N$ returns true if and only if $M$ and $N$ accept the same
language.

Formalized by `DFA.equivB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#equiv-b-iff).

## Acceptance test for encoded DFAs

For an encoded DFA $D$ over an alphabet $\alpha$ with
decidable equality and a word $w$ over $\alpha$, the acceptance test is the Boolean that is true
exactly when the state reached by running $D$ on $w$ from its start state is in the list of
accepting states of $D$.

Formalized by `Cslib.Automata.EncodedDFA.acceptsB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#accepts-b).

## One round of the list reachability search

Let $s_0 \in \mathbb{N}$, let $\mathrm{next}$
assign to each $s \in \mathbb{N}$ a list $\mathrm{next}(s)$ of natural numbers, and let $B$ and $R$
be lists of natural numbers. The round from $s_0$ with successors $\mathrm{next}$ kept inside $B$
sends the list $R$ of states found so far to the following list: write $s_0$ followed, for each
$s$ in $R$ in order, by $s$ and then the list $\mathrm{next}(s)$; keep the entries that lie in $B$;
then delete every entry that occurs again later in the list.

Its entries are therefore the numbers in $B$ that are $s_0$, an element $s$ of $R$, or an element
of $\mathrm{next}(s)$ for some $s$ in $R$, each listed once.

Formalized by `Cslib.Automata.EncodedDFA.reachRound`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reach-round).

## Bounded reachability search on lists of states

Let $s_0 \in \mathbb{N}$, let
$\mathrm{next}$ assign to each $s \in \mathbb{N}$ a list $\mathrm{next}(s)$ of natural numbers, and
let $B$ be a list of natural numbers. One search round sends a list $R$ to the list obtained by
writing $s_0$ followed, for each $s$ in $R$ in order, by $s$ and then the list $\mathrm{next}(s)$,
keeping the entries that lie in $B$, and deleting every entry that occurs again later; its entries
are the elements of $B$ that are $s_0$, an element of $R$, or an element of $\mathrm{next}(s)$ for
some $s$ in $R$, each listed once. The search returns the result of applying this round $|B|$
times to the empty list, where $|B|$ is the length of $B$.

When $B$ contains $s_0$ and is closed under $\mathrm{next}$, a number is an entry of the returned
list exactly when it is reachable from $s_0$ by finitely many, possibly zero, steps from some $s$
to an element of $\mathrm{next}(s)$.

Formalized by `Cslib.Automata.EncodedDFA.reachN`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reach-n).

## Correctness of the bounded reachability search

Let $s_0 \in \mathbb{N}$, let
$\mathrm{next}$ assign to every natural number a list of natural numbers, its successors, and let
$B$ be a list of natural numbers that contains $s_0$ and is closed under successors: whenever $s$
is in $B$ and $t$ is a successor of $s$, then $t$ is in $B$. Then a natural number $t$ is in the
list computed by the reachability search from $s_0$ through $\mathrm{next}$ within $B$ if and
only if $t$ is reachable from $s_0$ in zero or more successor steps.

Formalized by `Cslib.Automata.EncodedDFA.mem_reachN_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#mem-reach-n-iff).

## Reachable states of an encoded DFA

For an encoded DFA $D$ over an alphabet $\alpha$ with
decidable equality, the reachable states of $D$ form the list returned by the bounded reachability
search on lists of states started at the start state of $D$, kept inside the states of $D$, in
which the successors of a state $s$ are the states that the transition function of $D$ takes $s$
to on the letters of $D$, in the order of the letters.

A natural number lies in this list exactly when the automaton denoted by $D$ reaches it from its
start state on some word.

Formalized by `Cslib.Automata.EncodedDFA.reachable`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#reachable-2).

## Emptiness test for encoded DFAs

For an encoded DFA $D$ over an alphabet $\alpha$ with
decidable equality, the emptiness test is the Boolean that is true exactly when no entry of the
list of reachable states of $D$ is in the accepting list of $D$.

It returns true exactly when the language of $D$ is empty.

Formalized by `Cslib.Automata.EncodedDFA.isEmptyB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-empty-b-2).

## Coded pairs of states of two encoded DFAs

For encoded DFAs $D$ and $E$ over the same
alphabet, code a pair $(s, t)$ of natural numbers by its image $\langle s, t \rangle \in \mathbb{N}$
under Mathlib's pairing function. This is the list of the numbers $\langle s, t \rangle$ with $s$
running over the states of $D$ in their listed order and, for each $s$, $t$ running over the
states of $E$ in their listed order.

Formalized by `Cslib.Automata.EncodedDFA.pairStates`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#pair-states).

## Successors of a pair of states

Let $D$ and $E$ be encoded DFAs over the same alphabet,
and let $p \in \mathbb{N}$ code the pair of states $(s, t)$ under the pairing bijection
$\mathbb{N} \times \mathbb{N} \to \mathbb{N}$. The successors of $p$ form the list that has, for
each letter $a$ in the letters of $D$ followed by the letters of $E$, the code of the pair made of
the step of $D$ from $s$ on $a$ and the step of $E$ from $t$ on $a$.

Formalized by `Cslib.Automata.EncodedDFA.pairNext`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#pair-next).

## Reachable pairs of states of two encoded DFAs

For encoded DFAs $D$ and $E$ over the same
alphabet, code a pair $(s, t)$ of natural numbers by its image $\langle s, t \rangle \in \mathbb{N}$
under Mathlib's pairing function. The reachable pairs of $D$ and $E$ form the list returned by the
bounded reachability search on lists of states started at $\langle s_D, s_E \rangle$, where $s_D$
and $s_E$ are the start states of $D$ and $E$, kept inside the list of coded pairs of states of
$D$ and $E$, and in which the successors of a number $p = \langle s, t \rangle$ are the numbers
$\langle s', t' \rangle$ with $s'$ and $t'$ the states that the transition functions of $D$ and
$E$ take $s$ and $t$ to on the same letter $a$, for $a$ running over the letters of $D$ followed
by the letters of $E$.

A number lies in this list exactly when it is $\langle q, r \rangle$ for the states $q$ and $r$
that $D$ and $E$ reach on some common word.

Formalized by `Cslib.Automata.EncodedDFA.pairReachable`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#pair-reachable).

## Equivalence test for encoded DFAs

Let $D$ and $E$ be encoded DFAs over an alphabet
$\alpha$ with decidable equality. The equivalence test of $D$ and $E$ is the Boolean that is true
exactly when, for every entry $p$ of the list of reachable pairs of states of $D$ and $E$, writing
$p = \langle s, t \rangle$ with Mathlib's pairing function, $s$ is in the accepting list of $D$ if
and only if $t$ is in the accepting list of $E$.

It returns true exactly when $D$ and $E$ have the same language.

Formalized by `Cslib.Automata.EncodedDFA.equivB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#equiv-b-2).

## Universality test for encoded DFAs

For an encoded DFA $D$ over an alphabet $\alpha$ with
decidable equality, the universality test is the Boolean that is true exactly when every entry of
the list of reachable states of $D$ is in the accepting list of $D$.

It returns true exactly when the language of $D$ contains every word over $\alpha$.

Formalized by `Cslib.Automata.EncodedDFA.isUnivB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#is-univ-b-2).

## An encoded DFA on its listed states

For an encoded DFA $D$, this is the DFA whose set of
states is the finite set of states of $D$ (its start state and the targets of its listed
transitions), whose start state is the start state of $D$, whose transition function is that of
$D$ restricted to these states, and whose accepting states are those in the accepting list of
$D$.

Formalized by `Cslib.Automata.EncodedDFA.toFinDFA`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#to-fin-dfa).

## A long accepted word makes the language of an encoded DFA infinite

Let $D$ be an
encoded DFA and let $N$ be the length of the list of states of $D$. If $D$ accepts a word of
length at least $N$, then the language of $D$ is infinite.

The proof pumps the word, using the pumping lemma for DFAs.

Formalized by `Cslib.Automata.EncodedDFA.infinite_of_mem_of_le`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#infinite-of-mem-of-le).

## Accepted words of length between the number of listed states and twice it

Let $D$ be an
encoded DFA over an alphabet $\alpha$ with decidable equality, and let $N$ be the length of its
list of states. For every natural number $n$ and every word $w$ of length $n$ in the language of
$D$ with $N \le n$, the language of $D$ contains a word $v$ whose length $|v|$ satisfies
$N \le |v| < 2N$.

Formalized by `Cslib.Automata.EncodedDFA.exists_mem_le_lt`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#exists-mem-le-lt).

## Words of a given length

For a finite alphabet $\alpha$ given with an enumeration of its
letters and for $n \in \mathbb{N}$, the list of the words of length $n$ over $\alpha$: starting
from the list whose only entry is the empty word, it replaces $n$ times each word $w$ of the
current list by the words $a w$ for the letters $a$ of $\alpha$, in their enumeration order.

Formalized by `Cslib.Automata.EncodedDFA.wordsOfLength`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#words-of-length).

## Infiniteness test for encoded DFAs

Let $D$ be an encoded DFA over a finite alphabet and
let $N$ be the length of its list of states. The infiniteness test is the Boolean that is true
exactly when the language of $D$ contains a word $w$ with $N \le |w| < 2N$; it checks every word
of each length $N + i$ with $0 \le i < N$.

Formalized by `Cslib.Automata.EncodedDFA.infiniteB`, a definition declared in [CSLibExt/Computability/Decidability/Regular.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#infinite-b).

## Correctness of the infiniteness test for encoded DFAs

For every encoded DFA $D$ over a
finite alphabet, the infiniteness test returns true on $D$ if and only if the language of $D$ is
infinite.

Formalized by `Cslib.Automata.EncodedDFA.infiniteB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#infinite-b-iff).

## Acceptance for DFAs is decidable

For every alphabet $\alpha$ with decidable equality and
a primitive recursive encoding, the property of a pair $(D, w)$ of an encoded DFA $D$ over
$\alpha$ and a word $w$ over $\alpha$ that $w$ belongs to the language of $D$ is decidable by a
multi-stack machine. This is the problem $A_{\mathrm{DFA}}$.

## Sources

- Sipser, *Introduction to the Theory of Computation*, Theorem 4.1.

Formalized by `Cslib.Automata.EncodedDFA.tm2Decidable_mem_language`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#tm2-decidable-mem-language).

## Emptiness of DFAs is decidable

For every alphabet $\alpha$ with decidable equality and a
primitive recursive encoding, the property of an encoded DFA over $\alpha$ that its language is
empty is decidable by a multi-stack machine. This is the problem $E_{\mathrm{DFA}}$.

## Sources

- Sipser, *Introduction to the Theory of Computation*, Theorem 4.4.

Formalized by `Cslib.Automata.EncodedDFA.tm2Decidable_language_eq_zero`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 734](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L734). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#tm2-decidable-language-eq-zero).

## Equivalence of DFAs is decidable

For every alphabet $\alpha$ with decidable equality and
a primitive recursive encoding, the property of a pair of encoded DFAs over $\alpha$ that their
languages are equal is decidable by a multi-stack machine. This is the problem
$\mathrm{EQ}_{\mathrm{DFA}}$.

## Sources

- Sipser, *Introduction to the Theory of Computation*, Theorem 4.5.

Formalized by `Cslib.Automata.EncodedDFA.tm2Decidable_language_eq`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#tm2-decidable-language-eq).

## Universality of DFAs is decidable

For every alphabet $\alpha$ with decidable equality and
a primitive recursive encoding, the property of an encoded DFA over $\alpha$ that its language is
the set of all words over $\alpha$ is decidable by a multi-stack machine. This is the problem
$\mathrm{ALL}_{\mathrm{DFA}}$.

Formalized by `Cslib.Automata.EncodedDFA.tm2Decidable_language_eq_top`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#tm2-decidable-language-eq-top).

## Infiniteness of DFAs is decidable

For every finite alphabet $\alpha$, given with an
enumeration of its letters, decidable equality and a primitive recursive encoding, the property
of an encoded DFA over $\alpha$ that its language is infinite is decidable by a multi-stack
machine. This is the problem $\mathrm{INFINITE}_{\mathrm{DFA}}$.

Formalized by `Cslib.Automata.EncodedDFA.tm2Decidable_language_infinite`, a theorem declared in [CSLibExt/Computability/Decidability/Regular.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Regular.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html#tm2-decidable-language-infinite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decision procedures for finite automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/decision-procedures-for-finite-automata)
