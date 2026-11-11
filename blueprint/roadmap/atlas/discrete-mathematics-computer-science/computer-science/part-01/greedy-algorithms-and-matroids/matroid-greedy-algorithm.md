---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.matroidGreedyScan, Cslib.Algorithms.Lean.TimeM.matroidGreedy, Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_time, Cslib.Algorithms.Lean.TimeM.matroidGreedy_time, Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_append, Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_spec, Cslib.Algorithms.Lean.TimeM.matroidGreedy_indep, Cslib.Algorithms.Lean.TimeM.matroidGreedy_isBase
statement: formalized
proof: formalized
---

# Matroid greedy algorithm

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html).

## Greedy scan with an independence oracle

Given an oracle $O$ that accepts or rejects each
finite subset of a type $\alpha$, a finite set $S \subseteq \alpha$ and a list $e_1, \dots, e_n$ of
elements of $\alpha$, the greedy scan processes $e_1, \dots, e_n$ in order, starting with $S$ as
the current set: it replaces the current set $T$ by $T \cup \{e_i\}$ if $O$ accepts
$T \cup \{e_i\}$, and leaves it unchanged otherwise. It returns the final current set and charges
one unit of time per element processed.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan).

## Greedy algorithm on a matroid

Given an oracle $O$ that accepts or rejects each finite
subset of a type $\alpha$ and a list $L$ of elements of $\alpha$, the greedy algorithm starts from
the empty set, processes the elements of $L$ in order, adds an element $e$ to the current set $T$
when $O$ accepts $T \cup \{e\}$ and leaves $T$ unchanged otherwise, and returns the final set. It
charges one unit of time per element processed.

## Sources

- CLRS, third edition, Section 16.4, procedure GREEDY, without its sorting step.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedy`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy).

## Running time of the greedy scan

For every oracle $O$ on finite subsets of a type
$\alpha$, every finite set $S \subseteq \alpha$ and every list $L$ of elements of $\alpha$, the
greedy scan with oracle $O$ from $S$ over $L$ takes time exactly the length of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan-time).

## Running time of the matroid greedy algorithm

For every oracle $O$ on finite subsets of a
type $\alpha$ and every list $L$ of elements of $\alpha$, the greedy algorithm with oracle $O$ on
$L$ takes time exactly the length of $L$, one oracle query per element.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedy_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-time).

## The greedy scan over a concatenation

For every oracle $O$ on finite subsets of a type
$\alpha$, every finite set $S \subseteq \alpha$ and all lists $P$ and $Q$ of elements of $\alpha$,
the set returned by the greedy scan with oracle $O$ from $S$ over $P$ followed by $Q$ equals the
set returned by the greedy scan with oracle $O$ over $Q$ starting from the set that the scan with
oracle $O$ from $S$ over $P$ returns.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_append`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan-append).

## Invariant of the greedy scan

Let $M$ be a matroid on a type $\alpha$, let $O$ be an oracle
that accepts a finite set $A \subseteq \alpha$ exactly when $A$ is independent in $M$, let $S$ be a
finite independent set of $M$ and $L$ a list of elements of $\alpha$, and let $T$ be the set
returned by the greedy scan with oracle $O$ from $S$ over $L$. Then $T$ is independent in $M$, and
for every element $e$ of $L$ with $e \notin T$, the set $T \cup \{e\}$ is not independent in $M$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan-spec).

## The matroid greedy result is independent

Let $M$ be a matroid on a type $\alpha$ and let
$O$ be an oracle that accepts a finite set $A \subseteq \alpha$ exactly when $A$ is independent in
$M$. For every list $L$ of elements of $\alpha$, the set returned by the greedy algorithm with
oracle $O$ on $L$ is independent in $M$, and each of its elements occurs in $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedy_indep`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-indep).

## The matroid greedy result is a base

Let $M$ be a matroid on a type $\alpha$ with ground set
$E$, and let $O$ be an oracle that accepts a finite set $A \subseteq \alpha$ exactly when $A$ is
independent in $M$. For every list $L$ in which an element of $\alpha$ occurs if and only if it lies
in $E$, the set returned by the greedy algorithm with oracle $O$ on $L$ is a base of $M$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedy_isBase`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-is-base).

## Threshold counts of the matroid greedy result

Let $M$ be a matroid on a type $\alpha$, let
$O$ be an oracle that accepts a finite set $A \subseteq \alpha$ exactly when $A$ is independent in
$M$, and let $w : \alpha \to \mathbb{N}$ be a weight function. Let $L$ be a list of elements of
$\alpha$ in nonincreasing order of weight (whenever $a$ occurs before $b$ in $L$, $w(b) \le w(a)$),
and let $G$ be the set returned by the greedy algorithm with oracle $O$ on $L$. Then for every
finite independent set $I$ of $M$ whose elements all occur in $L$ and every $t \in \mathbb{N}$, the
number of $x \in I$ with $w(x) > t$ is at most the number of $x \in G$ with $w(x) > t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.card_filter_le_matroidGreedy`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#card-filter-le-matroid-greedy).

## Optimality of the matroid greedy algorithm

Let $M$ be a matroid on a type $\alpha$, let $O$
be an oracle that accepts a finite set $A \subseteq \alpha$ exactly when $A$ is independent in $M$,
and let $w : \alpha \to \mathbb{N}$ be a weight function. Let $L$ be a list of elements of $\alpha$
in nonincreasing order of weight (whenever $a$ occurs before $b$ in $L$, $w(b) \le w(a)$), and let
$G$ be the set returned by the greedy algorithm with oracle $O$ on $L$. Then every finite
independent set $I$ of $M$ whose elements all occur in $L$ satisfies
$\sum_{x \in I} w(x) \le \sum_{x \in G} w(x)$.

## Sources

- CLRS, third edition, Theorem 16.11.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedy_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/MatroidGreedy.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-optimal).

## Independence system

A predicate $\mathrm{indep}$ on the finite subsets of a type
$\alpha$ is an independence system when the empty set is independent and every subset of an
independent set is independent.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsIndepSystem`, a structure declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#is-indep-system).

## A scan inside an independent set keeps everything

Let $\alpha$ be a type, let
$\mathrm{indep}$ be an independence system on the finite subsets of $\alpha$ and let $I$ be an
independent set. For every list $L$ of elements of $I$ and every finite set $S \subseteq I$, the
greedy scan of $L$ starting from $S$ returns $S$ together with all elements of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_of_subset`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan-of-subset).

## A scan that accepts nothing

Let $\alpha$ be a type, let $\mathrm{indep}$ be an
independence oracle on the finite subsets of $\alpha$, let $S$ be a finite subset of $\alpha$
and let $L$ be a list of elements of $\alpha$ such that $\mathrm{indep}$ rejects $S \cup \{e\}$
for every $e$ in $L$. Then the greedy scan of $L$ starting from $S$ returns $S$.

Formalized by `Cslib.Algorithms.Lean.TimeM.matroidGreedyScan_of_forall_not`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#matroid-greedy-scan-of-forall-not).

## Greedy optimality

Let $\alpha$ be a finite type and let $\mathrm{indep}$ be an
independence oracle on the finite subsets of $\alpha$. The greedy algorithm is optimal for
$\mathrm{indep}$ when, for every weight function $w : \alpha \to \mathbb{N}$ and every list $L$
that contains every element of $\alpha$ exactly once, in nonincreasing order of $w$, the set $T$
returned by the matroid greedy algorithm on $L$ with oracle $\mathrm{indep}$ satisfies
$\sum_{x \in I} w(x) \le \sum_{x \in T} w(x)$ for every finite set $I$ independent under
$\mathrm{indep}$.

Finiteness of $\alpha$ keeps this from holding vacuously: on an infinite type no list contains
every element.

Formalized by `Cslib.Algorithms.Lean.TimeM.GreedyOptimal`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#greedy-optimal).

## Greedy optimality gives the augmentation axiom

Let $\alpha$ be a finite type and let
$\mathrm{indep}$ be an independence system on the finite subsets of $\alpha$ for which the greedy
algorithm is optimal. If $I$ and $J$ are independent sets with $|I| < |J|$, then some element
$e \in J$ with $e \notin I$ makes $I \cup \{e\}$ independent.

Formalized by `Cslib.Algorithms.Lean.TimeM.augment_of_greedyOptimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#augment-of-greedy-optimal).

## Greedy-optimal independence systems are matroids

Let $\alpha$ be a finite type and let
$\mathrm{indep}$ be an independence system on the finite subsets of $\alpha$ for which the greedy
algorithm is optimal. Then there is a matroid $M$ on $\alpha$ whose ground set is all of
$\alpha$ such that a finite set $S \subseteq \alpha$ is independent in $M$ exactly when $S$ is
independent under $\mathrm{indep}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.exists_matroid_of_greedyOptimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#exists-matroid-of-greedy-optimal).

## Rado–Edmonds theorem

Let $\alpha$ be a finite type and let $\mathrm{indep}$ be an
independence system on the finite subsets of $\alpha$. The greedy algorithm is optimal for
$\mathrm{indep}$ if and only if there is a matroid $M$ on $\alpha$ whose ground set is all of
$\alpha$ such that a finite set $S \subseteq \alpha$ is independent in $M$ exactly when $S$ is
independent under $\mathrm{indep}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedyOptimal_iff_exists_matroid`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/GreedyMatroidCharacterization.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html#greedy-optimal-iff-exists-matroid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matroid greedy algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/greedy-algorithms-and-matroids/matroid-greedy-algorithm)
