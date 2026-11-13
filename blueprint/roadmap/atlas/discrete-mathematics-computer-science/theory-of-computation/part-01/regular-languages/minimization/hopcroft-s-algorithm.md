---
declaration: section
origin: cited
lean: DFA.Hopcroft.preimage, DFA.Hopcroft.Splits, DFA.Hopcroft.splitBlock, DFA.Hopcroft.smaller, DFA.Hopcroft.newSplitters, DFA.Hopcroft.roundP, DFA.Hopcroft.roundW, DFA.Hopcroft.accBlock
statement: formalized
proof: formalized
---

# Hopcroft's algorithm

66 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html).

## Preimage of a set under a letter

For a DFA $M$ with transition function $\delta$, a set
$C$ of states and a letter $a$, the preimage of $C$ under $a$ is the set of states $q$ with
$\delta(q, a) \in C$.

Formalized by `DFA.Hopcroft.preimage`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#preimage).

## A set of states split by another

A set $D$ of states is split by a set $P$ of states
when $D$ contains both a state in $P$ and a state not in $P$, that is, when $D \cap P$ and
$D \setminus P$ are both nonempty.

Formalized by `DFA.Hopcroft.Splits`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splits).

## Splitting a block by a set

For sets $P$ and $D$ of states, splitting $D$ by $P$ gives
the two-element list $[D \cap P,\ D \setminus P]$ if both of these sets are nonempty, and the
one-element list $[D]$ otherwise.

Formalized by `DFA.Hopcroft.splitBlock`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#split-block).

## Smaller of two finite sets of states

For finite sets $A$ and $B$ of states, the
smaller one is $A$ if $|A| \le |B|$ and $B$ otherwise; on a tie in cardinality it is $A$.

Formalized by `DFA.Hopcroft.smaller`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#smaller).

## New splitters for a split block

Given a waiting list $W$ of pairs of a set of states and a
letter and sets $S$ and $D$ of states, write $D_1 = D \cap S$ and $D_2 = D \setminus S$. The new
waiting entries for $D$ consist, for each letter $b$ in the enumeration order of the alphabet,
of both $(D_1, b)$ and $(D_2, b)$ if $(D, b)$ is in $W$, and otherwise of the single entry
$(E, b)$, where $E$ is the smaller of $D_1$ and $D_2$ by cardinality ($D_1$ on a tie).

Formalized by `DFA.Hopcroft.newSplitters`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#new-splitters).

## One refinement round of the partition

For a DFA $M$ with transition function $\delta$, a
list $P$ of blocks of states, a set $C$ of states and a letter $a$, let
$S = \{q : \delta(q, a) \in C\}$ be the preimage of $C$ under $a$. The partition after the
splitter $(C, a)$ replaces each block $D$ of $P$, in order, by the two blocks $D \cap S$ and
$D \setminus S$ when both are nonempty, and keeps $D$ otherwise.

Formalized by `DFA.Hopcroft.roundP`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#round-p).

## One update of the waiting list

For a DFA $M$ with transition function $\delta$, a list $P$
of blocks of states, a list $W$ of pairs of a set of states and a letter, a set $C$ of states and a
letter $a$, let $S = \{q : \delta(q, a) \in C\}$ be the preimage of $C$ under $a$, and say that $S$
splits a set $D$ when $D$ meets both $S$ and its complement. The waiting list after the splitter
$(C, a)$, from the rest $W$ of the waiting list, consists of the entries of $W$ whose set is not
split by $S$, followed, for each block $D$ of $P$ split by $S$ in order, by the new splitters for
$D$: for each letter $b$ in the enumeration order of the alphabet, both $(D \cap S, b)$ and
$(D \setminus S, b)$ if $(D, b)$ is in $W$, and otherwise the single entry $(E, b)$, where $E$ is
the smaller of $D \cap S$ and $D \setminus S$ by cardinality ($D \cap S$ on a tie).

Formalized by `DFA.Hopcroft.roundW`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#round-w).

## Block of accepting states

For a DFA $M$ with finite state set $Q$, this is the set
$F \subseteq Q$ of accepting states of $M$, as a finite set.

Formalized by `DFA.Hopcroft.accBlock`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#acc-block).

## Rejecting states

For a DFA $M$ with state set $Q$ and set of accepting states $F$, the
rejecting block is the set $Q \setminus F$ of states of $M$ that are not accepting.

Formalized by `DFA.Hopcroft.rejBlock`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#rej-block).

## Hopcroft's initial partition

For a DFA $M$ with finite state set $Q$ and set of accepting
states $F$, the initial partition is the list of blocks $F$, $Q \setminus F$, in this order, with
any empty block removed.

Formalized by `DFA.Hopcroft.initP`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#init-p).

## Hopcroft's initial waiting list

Let $M$ be a DFA with finite state set $Q$, set of
accepting states $F$ and finite alphabet $\Sigma$. If $F$ and $Q \setminus F$ are both nonempty,
the initial waiting list consists of the splitters $(S, b)$ for every letter $b \in \Sigma$, where
$S = F$ if $|F| \le |Q \setminus F|$ and $S = Q \setminus F$ otherwise; if one of $F$ and
$Q \setminus F$ is empty, the initial waiting list is empty.

Formalized by `DFA.Hopcroft.initW`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#init-w).

## Hopcroft's refinement loop

Let $M$ be a DFA. Given a round budget $k$, a partition $P$
of the states of $M$ (a list of blocks) and a waiting list $W$ of splitters $(C, a)$, each a block
$C$ with a letter $a$, the loop returns the pair $(P, W)$ unchanged if $k = 0$ or $W$ is empty.
Otherwise it removes the first splitter $(C, a)$ from $W$, replaces $P$ by the partition after the
splitter $(C, a)$ and the remaining waiting list by the waiting list after the splitter $(C, a)$,
and continues with budget $k - 1$.

Formalized by `DFA.hopcroftLoop`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop).

## Hopcroft's partition

Let $M$ be a DFA with finite state set $Q$ over a finite alphabet
$\Sigma$. Hopcroft's partition of $M$ is the partition returned by Hopcroft's loop run from the
initial partition and the initial waiting list with a budget of $|\Sigma| \cdot (|Q| + 1)$
rounds.

Formalized by `DFA.hopcroftPartition`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-partition).

## Hopcroft's relation

For a DFA $M$ with finitely many states, Hopcroft's relation is the
set of pairs $(p, q)$ of states of $M$ such that $p$ and $q$ lie in a common block of Hopcroft's
partition.

Formalized by `DFA.hopcroftRel`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-rel).

## Partitions of the states

A list $P$ of sets of states is a partition into nonempty
blocks when entries of $P$ at different positions are disjoint, every entry of $P$ is nonempty,
and every state lies in some entry of $P$.

Formalized by `DFA.Hopcroft.IsPartition`, a structure declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#is-partition).

## Lying in a common block

For a list $P$ of sets of states, two states $p$ and $q$ are
related by $P$ when some block $D$ of $P$ contains both $p$ and $q$.

Formalized by `DFA.Hopcroft.Rel`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#rel).

## A block contains both or neither of two related states

Let $P$ be a list of sets of
states that is a partition into nonempty blocks, let $C$ be an entry of $P$, and let $p$ and $q$
be states lying in a common entry of $P$. Then $p \in C$ if and only if $q \in C$.

Formalized by `DFA.Hopcroft.IsPartition.mem_iff_of_rel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#mem-iff-of-rel).

## A partition has at most as many blocks as there are states

If a list $P$ of sets of
states is a partition into nonempty blocks, then the length of $P$ is at most the number $|Q|$ of
states.

Formalized by `DFA.Hopcroft.IsPartition.length_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#length-le).

## Pieces of a split block lie on one side

Let $S$ and $D$ be sets of states. Every piece of
$D$ split by $S$ (the two sets $D \cap S$ and $D \setminus S$ if $D$ meets both $S$ and its
complement, and $D$ itself otherwise) is contained in $S$ or disjoint from $S$: any two states
$x$ and $y$ of the piece satisfy $x \in S \iff y \in S$.

Formalized by `DFA.Hopcroft.side_of_mem_splitBlock`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#side-of-mem-split-block).

## Effect of one splitter on the common-block relation

Let $M$ be a DFA with transition
function $\delta$, $P$ a list of blocks of states, $C$ a set of states and $a$ a letter. Two states
$p$ and $q$ lie in a common block after the splitter $(C, a)$ is applied to $P$ if and only if
they lie in a common block of $P$ and $\delta(p, a) \in C \iff \delta(q, a) \in C$.

Formalized by `DFA.Hopcroft.rel_roundP_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#rel-round-p-iff).

## Number of blocks after one round

Let $M$ be a DFA with transition function $\delta$, let
$P$ be a list of sets of states, $C$ a set of states and $a$ a letter, and let
$\mathrm{pre} = \{q : \delta(q, a) \in C\}$. The partition after the splitter $(C, a)$, which
replaces each entry $D$ of $P$ meeting both $\mathrm{pre}$ and its complement by
$D \cap \mathrm{pre}$ and $D \setminus \mathrm{pre}$, has length equal to the length of $P$ plus
the number of entries of $P$ (counted with repetition) that meet both $\mathrm{pre}$ and its
complement.

Formalized by `DFA.Hopcroft.length_roundP`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#length-round-p).

## Growth of the waiting list in one round

Let $M$ be a DFA with transition function
$\delta$ over a finite alphabet $\Sigma$, let $P$ be a list of sets of states with no repeated
entries, let $W$ be a list of pairs of a set of states and a letter, let $C$ be a set of states
and $a$ a letter, and let $S = \{q : \delta(q, a) \in C\}$ be the preimage of $C$ under $a$. Then
the waiting list after the splitter $(C, a)$, computed from the blocks $P$ and the rest $W$ of the
waiting list, has length at most $|W| + |\Sigma| \cdot k$, where $k$ is the number of entries of
$P$ split by $S$, that is, meeting both $S$ and its complement.

Formalized by `DFA.Hopcroft.length_roundW_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#length-round-w-le).

## Invariants of Hopcroft's loop

Let $M$ be a DFA with transition function $\delta$. A list
$P$ of sets of states and a waiting list $W$ of pairs $(C, b)$ of a set of states $C$ and a letter
$b$ satisfy the invariants when: (i) $P$ is a partition of the states into nonempty blocks;
(ii) for every $(C, b)$ in $W$, $C$ is an entry of $P$; (iii) for every letter $b$ and all states
$p$, $q$ lying in a common entry of $P$, if for every $C$ with $(C, b)$ in $W$ the states
$\delta(p, b)$ and $\delta(q, b)$ are both in $C$ or both outside $C$, then $\delta(p, b)$ and
$\delta(q, b)$ lie in a common entry of $P$; (iv) any two states lying in a common entry of $P$
are both accepting or both rejecting; and (v) any two states from which $M$ accepts the same
language lie in a common entry of $P$.

Formalized by `DFA.Hopcroft.Inv`, a structure declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#inv).

## One round preserves the invariants

Let $M$ be a DFA, $P$ a list of blocks of states, $W$
a list of pairs of a set of states and a letter, $C$ a set of states and $a$ a letter. If $P$ and
the waiting list obtained by putting $(C, a)$ in front of $W$ satisfy the invariants of
Hopcroft's loop, then so do the partition after the splitter $(C, a)$ and the waiting list after
the splitter $(C, a)$ from the rest $W$.

Formalized by `DFA.Hopcroft.Inv.round`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#round).

## With an empty waiting list, blocks are the classes of equal continuation languages

Let
$M$ be a DFA and $P$ a list of blocks of states such that $P$ with the empty waiting list
satisfies the invariants of Hopcroft's loop. Then two states $p$ and $q$ lie in a common block of
$P$ if and only if they accept the same continuation languages, that is, $M$ accepts a word from
$p$ exactly when it accepts it from $q$.

With an empty waiting list the invariants say that $P$ is a right congruence refining acceptance.

Formalized by `DFA.Hopcroft.Inv.rel_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#rel-iff).

## The invariants hold initially

For every DFA $M$ with finitely many states over a finite
alphabet, Hopcroft's initial partition and initial waiting list satisfy the invariants of
Hopcroft's loop.

Formalized by `DFA.Hopcroft.inv_init`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#inv-init).

## Termination of Hopcroft's loop

Let $M$ be a DFA with finite state set $Q$ over a finite
alphabet $\Sigma$, let $P$ be a partition of the states given as a list of blocks, let $W$ be a
waiting list of splitters, and let $k$ be a natural number. If $P$ and $W$ satisfy the invariants
of Hopcroft's loop and $|W| + |\Sigma| \cdot (|Q| - |P|) \le k$, where $|P|$ and $|W|$ are the
lengths of the lists, then Hopcroft's loop run from $(P, W)$ with a budget of $k$ rounds ends with
an empty waiting list, and the partition and waiting list it returns again satisfy the invariants.

The invariants make $P$ a partition into nonempty blocks, so $|P| \le |Q|$ and the difference
$|Q| - |P|$ is not truncated.

Formalized by `DFA.hopcroftLoop_spec`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 626](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-spec).

## Hopcroft's waiting list is exhausted

Let $M$ be a DFA with finite state set $Q$ over a
finite alphabet $\Sigma$. Hopcroft's loop, run from the initial partition and the initial waiting
list with a budget of $|\Sigma| \cdot (|Q| + 1)$ rounds, ends with an empty waiting list.

Formalized by `DFA.hopcroftLoop_waiting_eq_nil`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-waiting-eq-nil).

## Hopcroft's final partition is a partition

For a DFA $M$, Hopcroft's final partition of
$M$ is a partition of the states of $M$ into nonempty blocks.

Formalized by `DFA.isPartition_hopcroftPartition`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#is-partition-hopcroft-partition).

## Correctness of Hopcroft's algorithm

For a DFA $M$, two states $p$ and $q$ share a block
of Hopcroft's final partition of $M$ exactly when the language accepted by $M$ from $p$ equals the
language accepted by $M$ from $q$.

Formalized by `DFA.mem_hopcroftRel_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#mem-hopcroft-rel-iff).

## Hopcroft's partition is Moore's relation

For every DFA $M$ with finitely many states over
a finite alphabet, Hopcroft's relation of $M$, the set of pairs of states lying in a common block
of Hopcroft's partition, equals Moore's state equivalence of $M$ as a set of pairs of states.

Formalized by `DFA.hopcroftRel_eq_mooreRel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-rel-eq-moore-rel).

## Moore classes are Hopcroft blocks

For a DFA $M$ and reachable states $p$ and $q$ of $M$,
the classes of $p$ and $q$ under Moore's equivalence on reachable states (the states of Moore's
minimal automaton) are equal if and only if $p$ and $q$ share a block of Hopcroft's final
partition of $M$.

Formalized by `DFA.mooreClass_eq_iff_mem_hopcroftRel`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 697](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L697). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#moore-class-eq-iff-mem-hopcroft-rel).

## Blocks of Hopcroft's partition are language classes

Let $M$ be a DFA, $D$ a block of
Hopcroft's final partition of $M$ and $p$ a state in $D$. Then a state $q$ lies in $D$ if and only
if the language accepted by $M$ from $q$ equals the language accepted by $M$ from $p$.

Formalized by `DFA.mem_block_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Hopcroft.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/Hopcroft.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#mem-block-iff).

## The smaller of two sets has at most half their total size

The smaller of two sets has at most half their combined size: it is one of the two
sets, so twice its size is at most the sum of the two sizes.

Formalized by `DFA.Hopcroft.two_mul_smaller_card_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#two-mul-smaller-card-le).

## The smaller part of a split has at most half the size

If two disjoint sets union to `D`, the smaller of them has at most half the size of
`D`.

Formalized by `DFA.Hopcroft.two_mul_smaller_card_le_of_split`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#two-mul-smaller-card-le-of-split).

## Halving chains shrink blocks by a factor of at least $2^k$

After `k` halving steps, the initial block is at least `2 ^ k` times the final block.
The halving hypothesis is stated for the cardinalities only; no subset hypothesis is
needed.

Formalized by `DFA.Hopcroft.mul_pow_le_card_of_halving_chain`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#mul-pow-le-card-of-halving-chain).

## The smaller-half counting lemma

In a chain of blocks where each step at least
halves the size, a block containing a given state can occur at most `Nat.log 2 n` times
past the start, where `n` is the number of states. In Hopcroft's algorithm, the successive
smaller halves containing one fixed state form such a chain: each of them is the smaller
half of a split of the previous block containing that state.

## Sources

- J. E. Hopcroft, "An `n log n` algorithm for minimizing states in a finite automaton", Theory of Machines and Computations, 1971; the counting argument is presented in J. Berstel, L. Boasson, O. Carton and I. Fagnot, "Minimization of automata", 2010.

Formalized by `DFA.Hopcroft.smaller_half_chain_le_log`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#smaller-half-chain-le-log).

## New splitters are halves of the split block

Every entry `newSplitters` adds for a block `D` is a half of `D` (one of the two sides
of the split by `pre`), or the smaller half.

Formalized by `DFA.Hopcroft.mem_newSplitters`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#mem-new-splitters).

## Smaller-half splitters have at most half the block size

A smaller-half entry added by `newSplitters` for a block `D` has at most half the size
of `D`: the two halves are disjoint and union to `D`. No split hypothesis is needed: the
halves of any block partition it.

Formalized by `DFA.Hopcroft.two_mul_card_le_of_mem_newSplitters_smaller`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#two-mul-card-le-of-mem-new-splitters-sma).

## Trace of splitters popped by Hopcroft's algorithm

The splitters popped by Hopcroft's loop, in order: the same recursion as
`DFA.hopcroftLoop`, collecting each popped splitter. The cost of processing one popped
splitter `(C, a)` is `(preimage M C a).card + 1`: one predecessor visit per state whose
`a`-successor lies in `C`, plus `O(1)` per-splitter overhead. See `hopcroftCost`.
`hopcroftLoop_eq_hopcroftLoop_of_length` proves this trace records exactly the
splitters the loop pops, so the trace cannot drift from the loop.

Formalized by `DFA.Hopcroft.hopcroftSplitters`, a definition declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-splitters).

## Predecessor cost of a Hopcroft splitter trace

The predecessor cost of a splitter trace: for each popped splitter `(C, a)`, one
predecessor visit per state in the preimage `preimage M C a`, plus `1` per-splitter
overhead. This is the quantity the total-work bound constrains
to `O(|Σ| n log n)`. Charging splitter size `C.card` instead
would undercount: if all `n` states transition on `a` to one state `q`, processing the
singleton splitter `({q}, a)` costs `n` predecessor visits while `C.card` charges
only `1`.

Formalized by `DFA.Hopcroft.hopcroftCost`, a definition declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost).

## The splitter trace records exactly the splitters the loop pops

The loop and the
trace recurse on the same state, so they take the same number of steps. The two
theorems below make the correspondence usable: the trace length is at most `k`, and
running the loop for exactly the trace's length gives the full loop result, so the trace
contains every splitter the loop pops and no others.

Formalized by `DFA.Hopcroft.hopcroftSplitters_length_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-splitters-length-le).

## Hopcroft splitter trace length equals loop fuel

The trace and the loop take the same number of steps: the trace length is the fuel
the loop consumed, i.e. the loop would stop after exactly that many rounds if run with
only that much fuel.

Formalized by `DFA.Hopcroft.hopcroftLoop_eq_hopcroftLoop_of_length`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftCost.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-eq-hopcroft-loop-of-length).

## Splitter count of a state and letter

Number of splitters with letter `b` containing `q`, with multiplicity.
This applies both to the waiting list and to the actual popped trace.

Formalized by `DFA.Hopcroft.splitterCount`, a definition declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count).

## Splitter count of newly added splitters

Replacement contributes one token at a state in the parent block;
otherwise only membership in the smaller half contributes a token.

Formalized by `DFA.Hopcroft.splitterCount_newSplitters`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-new-splitters).

## Splitter count update after one Hopcroft round

The exact token update at a state. Only its unique parent block can
contribute a new token, even when other blocks split in the same round.

Formalized by `DFA.Hopcroft.splitterCount_roundW`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-round-w).

## Waiting entries give positive splitter count

A waiting entry supplies a token; duplicate entries remain counted.

Formalized by `DFA.Hopcroft.splitterCount_pos_of_mem`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-pos-of-mem).

## Refined Hopcroft blocks lie inside their old blocks

A refined block containing `q` is a subset of the old block
containing `q`. Both partitions are the canonical Hopcroft partitions.

Formalized by `DFA.Hopcroft.IsPartition.subset_of_mem_roundP`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#subset-of-mem-round-p).

## Potential inequality for one Hopcroft refinement round

One refinement cannot increase logarithmic block-size credit plus
pending-token credit. Replacing a pending splitter spends no new credit;
adding a nonpending smaller half spends one logarithmic unit.

Formalized by `DFA.Hopcroft.splitterCount_round_potential`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-round-potential).

## Splitter count bound along a Hopcroft execution

Total state/letter charging along the actual execution. The bound
includes initial tokens and tokens still pending through replacements.
No amortized bound is assumed in the execution invariant.

Formalized by `DFA.Hopcroft.splitterCount_hopcroftSplitters_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-hopcroft-splitters-le).

## Initial splitter count is at most one

Initially there is at most one token for each state and letter.

Formalized by `DFA.Hopcroft.splitterCount_initW_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-init-w-le).

## Hopcroft visits each of $n$ states at most $\log_2 n + 1$ times per letter

Each state is processed with a fixed letter at most `log₂ n + 1`
times during any prefix of the actual initialized Hopcroft execution.

Formalized by `DFA.Hopcroft.splitterCount_init_trace_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#splitter-count-init-trace-le).

## Popped Hopcroft splitters are nonempty

Every popped splitter has a nonempty block, including splitters whose
predecessor set is empty.

Formalized by `DFA.Hopcroft.nonempty_of_mem_hopcroftSplitters`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorklist.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#nonempty-of-mem-hopcroft-splitters).

## Hopcroft predecessor-work as splitter counts plus pops

Double counting visits by source state and letter, retaining every
incoming transition even when many sources have the same successor.

Formalized by `DFA.Hopcroft.hopcroftCost_eq_sum_splitterCount`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-eq-sum-splitter-count).

## Number of pops bounded by the total splitter count

A nonempty popped block pays for its pop, even if its preimage is
empty. This bounds the `+1` term independently of predecessor visits.

Formalized by `DFA.Hopcroft.length_le_sum_splitterCount`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#length-le-sum-splitter-count).

## Total predecessor-work bound

**Total predecessor-work bound**, including one unit for every pop,
for every prefix of the initialized execution. No runtime claim is made
for the scanning implementation or for initialization.

Formalized by `DFA.Hopcroft.hopcroftCost_init_trace_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-init-trace-le).

## $O(|\Sigma| n \log n)$ bound on Hopcroft predecessor-work

A uniform `O(|Σ| n log n)` bound, with the explicit constant `4`.
The condition `n ≥ 2` is essential when absorbing the additive unit
into the logarithm. This concerns predecessor-work, not scan runtime.

Formalized by `DFA.Hopcroft.hopcroftCost_init_trace_le_log`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-init-trace-le-log).

## Predecessor-work bound for the complete Hopcroft run

The bound for the complete terminating minimization execution.
`DFA.hopcroftLoop_waiting_eq_nil` proves this fuel exhausts the queue;
`hopcroftLoop_eq_hopcroftLoop_of_length` ties the trace to its result.

Formalized by `DFA.Hopcroft.hopcroftCost_complete_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-complete-le).

## No initial Hopcroft splitters with at most one state

With at most one state, the accepting/rejecting split has an empty
side, so the algorithm has no initial splitters.

Formalized by `DFA.Hopcroft.initW_eq_nil_of_card_le_one`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#init-w-eq-nil-of-card-le-one).

## Zero Hopcroft predecessor-work with at most one state

Zero predecessor-work for zero/one-state boundary parameters.
This does not assert that constructing the initial partition costs zero.

Formalized by `DFA.Hopcroft.hopcroftCost_eq_zero_of_card_le_one`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-eq-zero-of-card-le-one).

## Zero Hopcroft predecessor-work over an empty alphabet

An empty alphabet causes no predecessor-work, for any state count.

Formalized by `DFA.Hopcroft.hopcroftCost_eq_zero_of_alphabet_card_eq_zero`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWork.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-cost-eq-zero-of-alphabet-card-e).

## Hopcroft loop with recorded predecessor-work

The actual loop with predecessor-visit and pop events recorded in
CSLib's `TimeM`. Pure scans are not charged in this event model.

Formalized by `DFA.Hopcroft.hopcroftLoopWork`, a definition declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-work).

## Instrumented Hopcroft loop returns the original result

Instrumentation preserves the exact loop result.

Formalized by `DFA.Hopcroft.hopcroftLoopWork_ret`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-work-ret).

## Recorded Hopcroft cost equals the work of the popped trace

The recorded cost is exactly the work of the actual popped trace.

Formalized by `DFA.Hopcroft.hopcroftLoopWork_time`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-work-time).

## Recorded Hopcroft cost obeys the predecessor-work bound

The canonical cost monad records the proved total predecessor-work
bound for every initialized execution prefix.

Formalized by `DFA.Hopcroft.hopcroftLoopWork_init_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-work-init-le).

## Instrumented complete Hopcroft run returns the minimization partition

At the proved terminating fuel, instrumentation returns the original
correct minimization partition and an empty waiting list.

Formalized by `DFA.Hopcroft.hopcroftLoopWork_complete_ret`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/Congruences/HopcroftWorkTimeM.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html#hopcroft-loop-work-complete-ret).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hopcroft's algorithm](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/minimization/hopcroft-s-algorithm)
