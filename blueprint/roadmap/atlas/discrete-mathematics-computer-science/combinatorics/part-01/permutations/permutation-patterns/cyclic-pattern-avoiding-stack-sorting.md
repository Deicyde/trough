---
declaration: section
origin: cited
lean: MetaMathlibExt.SameRelativeOrder, MetaMathlibExt.ContainsPatternSeq, MetaMathlibExt.ContainsConsecutivePatternSeq, MetaMathlibExt.restrictedStackSortAux, MetaMathlibExt.westStackSort, MetaMathlibExt.cyclicStackSort, MetaMathlibExt.consecutiveCyclicStackSort, MetaMathlibExt.cyclicSortingMachine
statement: formalized
---

# Cyclic-pattern-avoiding stack sorting

31 results, 21 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html).

## Sequences with the same relative order

Two finite sequences $s = s_1 \cdots s_\ell$ and
$p = p_1 \cdots p_m$ of natural numbers have the same relative order if $\ell = m$ and, for all
$1 \le i, j \le m$, $s_i < s_j$ holds if and only if $p_i < p_j$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.SameRelativeOrder`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#same-relative-order).

## Classical pattern containment in a sequence

A sequence $w$ of natural numbers contains
the pattern $p = p_1 \cdots p_k$ if some subsequence $u_1 \cdots u_k$ of $w$ (whose entries need
not be adjacent in $w$) has the same relative order as $p$: for all $a, b \in \{1, \dots, k\}$,
$u_a < u_b$ if and only if $p_a < p_b$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.ContainsPatternSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#contains-pattern-seq).

## Consecutive pattern containment

A sequence $w$ of natural numbers contains a sequence
$p = p_1 \cdots p_k$ as a consecutive pattern if some $k$ adjacent entries
$w_{i+1}, \dots, w_{i+k}$ of $w$ have the same relative order as $p$: for all
$a, b \in \{1, \dots, k\}$, $w_{i+a} < w_{i+b}$ if and only if $p_a < p_b$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1 (after Defant and Zheng).

Formalized by `MetaMathlibExt.ContainsConsecutivePatternSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#contains-consecutive-pattern-seq).

## Restricted stack-sorting from a given stack

Fix a property of finite sequences of natural
numbers, called bad. Given an input sequence $\pi$ and a stack (listed from top to bottom), read
$\pi$ from left to right. Before pushing the next entry $x$, pop the least number $k$ of entries
from the top of the stack such that the remaining stack with $x$ pushed on top, read from top to
bottom, is not bad (if there is no such $k$, the whole stack is popped and $x$ is pushed anyway);
popped entries are appended to the output in the order they are removed. When the input is
exhausted, the remaining stack is appended to the output from top to bottom. The map returns this
output.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1 (Berlow's map `s_T`).

Formalized by `MetaMathlibExt.restrictedStackSortAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#restricted-stack-sort-aux).

## West's stack-sorting map

For a finite sequence $\pi$ of natural numbers, $s(\pi)$ is
computed with a stack that starts empty. The entries of $\pi$ are read from left to right; before
the next entry $x$ is pushed, the fewest entries are popped from the top of the stack so that the
stack with $x$ on top, read from top to bottom, avoids the pattern $21$, and the popped entries
are appended to the output in the order in which they are popped. After the last entry has been
pushed, the stack is emptied from top to bottom onto the output.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.westStackSort`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#west-stack-sort).

## Cyclic-pattern-avoiding stack-sorting map

For a finite sequence $\sigma$ of natural
numbers, the map $s_{[\sigma]}$ sends a finite sequence $\pi$ of natural numbers to the output of
the following procedure. Read $\pi$ from left to right, starting with an empty stack. Before
pushing the next entry $x$, pop the fewest entries from the top of the stack such that the stack
with $x$ pushed on top, read from top to bottom, contains no rotation of $\sigma$ as a pattern (if
even the stack holding only $x$ contains one, the whole stack is popped and $x$ is pushed anyway);
popped entries are appended to the output in the order they are removed. Once $\pi$ is exhausted,
the remaining stack is appended to the output from top to bottom. Here a sequence $w$ contains
$p = p_1 \cdots p_m$ as a pattern when some subsequence $w_1' \cdots w_m'$ of $w$ satisfies
$w_i' < w_j' \iff p_i < p_j$ for all $1 \le i, j \le m$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.cyclicStackSort`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-stack-sort).

## Consecutive-cyclic-pattern-avoiding stack-sorting map

For a sequence $\sigma$, the map
$s^{[\sigma]}$ sends a sequence $\pi$ of natural numbers to the output of the following stack
procedure. Read $\pi$ from left to right, starting with an empty stack. Before pushing the next
entry $x$, pop the fewest entries from the top of the stack, sending them to the output in the
order they are removed, so that the stack with $x$ on top, read from top to bottom, contains no
rotation of $\sigma$ as a consecutive pattern (a block of adjacent entries with the same length
and relative order as the rotation); if no number of pops achieves this, pop the whole stack.
Then push $x$. When the input is exhausted, pop the stack from top to bottom onto the output.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.consecutiveCyclicStackSort`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#consecutive-cyclic-stack-sort).

## Cyclic avoidance machine

For a sequence $\sigma$, the cyclic avoidance machine
$SC_{[\sigma]} = s \circ s_{[\sigma]}$ sends a sequence $\pi$ of natural numbers to
$s(s_{[\sigma]}(\pi))$: it first applies the cyclic-pattern-avoiding stack-sorting map
$s_{[\sigma]}$, whose stack, read from top to bottom, avoids every rotation of $\sigma$ as a
pattern, and then West's stack-sorting map $s$, whose stack, read from top to bottom, avoids the
pattern $21$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.cyclicSortingMachine`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-sorting-machine).

## Stack-sorting examples

Let $s$ be West's stack-sorting map, $s_{[123]}$ the
cyclic-pattern-avoiding stack-sorting map for $123$, $s^{[123]}$ the
consecutive-cyclic-pattern-avoiding stack-sorting map for $123$, and
$SC_{[123]} = s \circ s_{[123]}$ the cyclic sorting machine for $123$. Then $s(3124) = 1234$,
$s_{[123]}(3124) = 2143$, $s^{[123]}(3124) = 4213$, $SC_{[123]}(3124) = 1234$,
$SC_{[123]}(1324) = 3124$ and $SC_{[123]}(231) = 123$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1, Figures 1-3.

Formalized by `MetaMathlibExt.stackSort_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#stack-sort-examples).

## Standardization

The standardization $\mathrm{st}(s)$ of a finite sequence
$s = s_1 s_2 \cdots s_k$ of natural numbers is obtained by replacing each entry $s_i$ by the number
of indices $j$ with $s_j \le s_i$. When the entries of $s$ are distinct, this number is the rank
of $s_i$: the $r$th smallest entry becomes $r$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.standardizeSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#standardize-seq).

## Heads of runs of consecutive integers

Given an optional previous entry $y$ and a sequence
$s_1 s_2 \cdots s_\ell$ of natural numbers, this lists, in order, the entries $s_i$ with
$s_i \ne s_{i-1} + 1$, where $s_0 = y$; if there is no previous entry, $s_1$ is always listed.
With no previous entry, these are the minima $a$ of the maximal blocks $a, a + 1, \dots, a + k$
of adjacent consecutive integers of the sequence.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.consecutiveRunHeads`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#consecutive-run-heads).

## Reduction of a sequence

The reduction $\operatorname{red}(s)$ of a finite sequence $s$ of
natural numbers is obtained in two steps. First, every maximal block of adjacent entries of the
form $a, a + 1, \ldots, a + k$ is replaced by its first entry $a$. Then the resulting sequence is
standardized: each of its entries $x$ is replaced by the number of its entries that are at most
$x$, which for distinct entries is the rank of $x$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.reductionSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#reduction-seq).

## Standardization and reduction examples

The standardization of $315$ is
$\mathrm{st}(315) = 213$, and the reduction of $16783425$ is $\mathrm{red}(16783425) = 15324$.
Here $\mathrm{st}$ replaces each entry by its rank, and $\mathrm{red}$ replaces each maximal block
of adjacent consecutive integers $a, a + 1, \dots, a + k$ by its minimum $a$ and then
standardizes.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.standardizeSeq_reductionSeq_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#standardize-seq-reduction-seq-examples).

## Push order of the superimpose operation

For finite sequences $a$ and $b$ of natural
numbers, $\mathrm{push}(a, b)$ is the sequence obtained by taking the first entry of $b$, then the
next two entries of $a$ (only one if just one is left), and repeating; once one of the two
sequences is exhausted, the remaining entries of the other follow in order.

For finite sequences $\sigma_1$ and $\sigma_2$ with reversals $\mathrm{rev}\,\sigma_1$ and
$\mathrm{rev}\,\sigma_2$, the sequence $\mathrm{push}(\mathrm{rev}\,\sigma_1,
\mathrm{rev}\,\sigma_2)$ is the order in which the superimpose operation
$\mathrm{si}(\sigma_1, \sigma_2)$ pushes the entries of $\sigma_1$ and $\sigma_2$ onto its stack.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 3.2.

Formalized by `MetaMathlibExt.superimposePush`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#superimpose-push).

## Superimpose operation

For finite sequences $\sigma_1$ and $\sigma_2$ of natural numbers,
let $p = \mathrm{push}(\mathrm{rev}\,\sigma_1, \mathrm{rev}\,\sigma_2)$ be the push order of the
superimpose operation on the reversed sequences. Then $\mathrm{si}(\sigma_1, \sigma_2)$ is the
reversal of $p$: the stack obtained by pushing the entries of $p$ in order onto an empty stack,
read from top to bottom.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 3.2.

Formalized by `MetaMathlibExt.superimpose`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#superimpose).

## Superimpose examples

For the superimpose operation $\mathrm{si}$,
$\mathrm{si}((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)) = (6, 7, 1, 8, 2, 3, 9, 4, 5, 10)$ and
$\mathrm{si}((1, 2), (3, 4, 5, 6)) = (3, 4, 5, 1, 2, 6)$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 3.2 and Example 1.

Formalized by `MetaMathlibExt.superimpose_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#superimpose-examples).

## The permutation $\xi_n$

For a natural number $n$, $\xi_n$ is the sequence listing the
elements of $\{1, \dots, n\}$ whose parity differs from that of $n$ in increasing order, followed
by the elements with the same parity as $n$ in increasing order. Thus
$\xi_n = 1, 3, \dots, n-1, 2, 4, \dots, n$ for even $n$, and
$\xi_n = 2, 4, \dots, n-1, 1, 3, \dots, n$ for odd $n$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.xiPermutation`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#xi-permutation).

## The parity-split permutations for six and seven

For $n \in \mathbb{N}$, let $\xi_n$ list
the elements of $[n] = \{1, \dots, n\}$ whose parity differs from that of $n$ in increasing order,
followed by the elements with the parity of $n$ in increasing order. Then $\xi_6 = 135246$ and
$\xi_7 = 2461357$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 1.

Formalized by `MetaMathlibExt.xiPermutation_six_seven`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#xi-permutation-six-seven).

## Good sequences of suffix extrema

A finite sequence $s = s_1 s_2 \cdots s_\ell$ of natural
numbers is good if every entry $s_i$ is the minimum or the maximum of
$s_i, s_{i+1}, \ldots, s_\ell$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 3.4.

Formalized by `MetaMathlibExt.IsGoodSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#is-good-seq).

## Permutations sorted by a map

For a map $f$ from finite sequences of natural numbers to
finite sequences of natural numbers and for $n \in \mathbb{N}$, $\mathrm{Sort}_n(f)$ is the finite
set of permutations $\pi$ of $[n] = \{1, \dots, n\}$, written as sequences, such that $f(\pi)$ is
the identity permutation $\mathrm{id}_n = 12 \cdots n$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Section 2.

Formalized by `MetaMathlibExt.sortedPermutations`, a definition declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#sorted-permutations).

## Small cases of good sequences and of sorting by the consecutive $321$-cyclic stack

The
sequence $51432$ is good (each entry is the minimum or the maximum of itself and all entries after
it), and among the six permutations of $\{1, 2, 3\}$ exactly $312$ and $321$ are sent to $123$ by
the consecutive-cyclic-pattern-avoiding stack-sorting map $s^{[321]}$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Sections 2 and 3.4.

Formalized by `MetaMathlibExt.isGoodSeq_consecutiveCyclicStackSort_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#is-good-seq-consecutive-cyclic-stack-sor).

## $n - 2$ passes of $SC_{(123)}$ sort every permutation, and $n - 3$ do not

Let $n \ge 3$
and let $SC_{[123]}^k$ be the $k$-fold iterate of the cyclic avoidance machine $SC_{[123]}$.
For every permutation $\pi$ of $[n] = \{1, \dots, n\}$, $SC_{[123]}^{n-2}(\pi) = 12 \cdots n$, and
the bound is tight: $SC_{[123]}^{n-3}(\xi_n) \ne 12 \cdots n$, where $\xi_n$ lists the elements of
$[n]$ of parity different from $n$ in increasing order, followed by those of the parity of $n$
in increasing order.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclicSortingMachine_123_iterate_sorts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-sorting-machine-123-iterate-sorts).

## Eventual periodicity of the identity under $SC_{(321)}$

Let $n \ge 4$, let
$c = \lceil (2n-1)/3 \rceil$, and let $SC_{[321]}^k$ be the $k$-fold iterate of the cyclic
avoidance machine $SC_{[321]}$. For every natural number $m \ge \lceil (n-1-c)/2 \rceil$,
$SC_{[321]}^m(12 \cdots n) = SC_{[321]}^{m+c}(12 \cdots n)$.

Equivalently, $c = \lfloor (2n+1)/3 \rfloor$ and
$\lceil (n-1-c)/2 \rceil = \lfloor (n-c)/2 \rfloor$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Theorem 2.

Stated but not proved: `MetaMathlibExt.cyclicSortingMachine_321_identity_orbit_period` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-sorting-machine-321-identity-orbi).

## No permutation of length at least four is sorted by the consecutive cyclic $123$-stack

Let $s^{[123]}$ be the consecutive-cyclic-pattern-avoiding stack-sorting map for $123$. For every
$n \ge 4$, no permutation of $[n] = \{1, \dots, n\}$ is mapped by $s^{[123]}$ to the identity
$12 \cdots n$; that is, the set $\mathrm{Sort}_n(s^{[123]})$ of permutations of $[n]$ that
$s^{[123]}$ maps to the identity has $0$ elements.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Theorem 3.

Stated but not proved: `MetaMathlibExt.sortedPermutations_consecutiveCyclicStackSort_123` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#sorted-permutations-consecutive-cyclic-s).

## Permutations sorted by the consecutive $321$-cyclic stack

Let $n \ge 2$, let
$s^{[321]}$ be the stack-sorting map whose stack, read from top to bottom, avoids every rotation
of $321$ as a consecutive pattern, and let $\mathrm{Sort}_n(s^{[321]})$ be the set of permutations
of $[n] = \{1, \dots, n\}$ that $s^{[321]}$ maps to the identity $12 \cdots n$. Then
$|\mathrm{Sort}_n(s^{[321]})| = 2^{n-2}$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Theorem 4.

Stated but not proved: `MetaMathlibExt.card_sortedPermutations_consecutiveCyclicStackSort_321` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#card-sorted-permutations-consecutive-cyc).

## Reducing before the $123$ cyclic sorting machine does not change the reduced output

For
every permutation $\pi$ of $[n] = \{1, \ldots, n\}$, applying the cyclic sorting machine
$\mathrm{SC}_{[123]}$ to the reduction $\operatorname{red}(\pi)$ and reducing the result gives the
reduction of $\mathrm{SC}_{[123]}(\pi)$:
$\operatorname{red}(\mathrm{SC}_{[123]}(\operatorname{red}(\pi))) =
\operatorname{red}(\mathrm{SC}_{[123]}(\pi))$.

Only this identity is stated; the lemma's further assertion that blocks $a, a+1, \ldots, a+k$ of
$\pi$ enter and leave the stack together is not part of the statement.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Lemma 1.

Stated but not proved: `MetaMathlibExt.reductionSeq_cyclicSortingMachine_123_reductionSeq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#reduction-seq-cyclic-sorting-machine-123).

## Reduction and iterates of $SC_{(123)}$

Let $\pi$ be a permutation of
$[n] = \{1, \dots, n\}$, written as a sequence, let $\mathrm{red}(\pi)$ be its reduction, of
length $\ell$, and let $SC_{[123]}^k$ be the $k$-fold iterate of the cyclic avoidance machine
$SC_{[123]}$. For every $k \ge 0$, $SC_{[123]}^k(\pi) = 12 \cdots n$ if and only if
$SC_{[123]}^k(\mathrm{red}(\pi)) = 12 \cdots \ell$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Corollary 1.

Stated but not proved: `MetaMathlibExt.cyclicSortingMachine_123_iterate_eq_id_iff_reductionSeq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-sorting-machine-123-iterate-eq-id).

## After one pass of the $123$ cyclic sorting machine, the reduction is shorter

For every
$n \ge 2$ and every permutation $\pi$ of $[n] = \{1, \ldots, n\}$, the reduction
$\operatorname{red}(\mathrm{SC}_{[123]}(\pi))$ of the image of $\pi$ under the cyclic sorting
machine $\mathrm{SC}_{[123]}$ has fewer than $n$ entries.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Lemma 2.

Stated but not proved: `MetaMathlibExt.length_reductionSeq_cyclicSortingMachine_123_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#length-reduction-seq-cyclic-sorting-mach).

## One pass of $SC_{(321)}$ on superimposed increasing runs

Let $n \ge 4$ and
$1 \le m < \lceil (2n-1)/3 \rceil = \lfloor (2n+1)/3 \rfloor$. Then the cyclic avoidance machine
$SC_{[321]}$ maps the superimposition $\mathrm{si}((1, \dots, m), (m+1, \dots, n))$ to
$\mathrm{si}((1, \dots, m+1), (m+2, \dots, n))$.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Lemma 3.

Stated but not proved: `MetaMathlibExt.cyclicSortingMachine_321_superimpose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#cyclic-sorting-machine-321-superimpose).

## First entry and tail of permutations sorted by the consecutive $321$-cyclic stack

Let
$n \ge 2$ and let $\mathrm{Sort}_n(s^{[321]})$ be the set of permutations of
$[n] = \{1, \ldots, n\}$ that the consecutive-cyclic-pattern-avoiding stack-sorting map
$s^{[321]}$ sends to the identity $12 \cdots n$. Every $\pi = \pi_1 \pi_2 \cdots \pi_n$ in
$\mathrm{Sort}_n(s^{[321]})$ has $\pi_1 = n$, and $\pi_2 \cdots \pi_n$ is good: each of its entries
is the minimum or the maximum of itself and all entries after it.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Lemma 4.

Stated but not proved: `MetaMathlibExt.head_tail_of_mem_sortedPermutations_consecutiveCyclicStackSort_321` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#head-tail-of-mem-sorted-permutations-con).

## Characterization of the permutations sorted by the consecutive $321$-cyclic stack

Let
$n \ge 2$ and let $\pi = \pi_1 \pi_2 \cdots \pi_n$ be a permutation of $[n] = \{1, \ldots, n\}$.
The consecutive-cyclic-pattern-avoiding stack-sorting map $s^{[321]}$ sends $\pi$ to the identity
$12 \cdots n$ (that is, $\pi \in \mathrm{Sort}_n(s^{[321]})$) if and only if $\pi_1 = n$ and
$\pi_2 \cdots \pi_n$ is good: each of its entries is the minimum or the maximum of itself and all
entries after it.

## Sources

- Alex Zhan and Stella Bie, *Cyclic-Pattern-Avoiding Stacks*, INTEGERS 26 (2026), Article A15, Corollary 2.

Stated but not proved: `MetaMathlibExt.mem_sortedPermutations_consecutiveCyclicStackSort_321_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CyclicPatternAvoidingStacksWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html#mem-sorted-permutations-consecutive-cycl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cyclic-pattern-avoiding stack sorting](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/cyclic-pattern-avoiding-stack-sorting)
