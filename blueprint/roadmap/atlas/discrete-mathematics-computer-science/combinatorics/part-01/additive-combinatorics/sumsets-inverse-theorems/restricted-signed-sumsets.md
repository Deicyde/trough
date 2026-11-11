---
declaration: section
origin: cited
lean: MetaMathlibExt.restrictedSumset, MetaMathlibExt.restrictedSignedSumset, MetaMathlibExt.mem_restrictedSumset_iff, MetaMathlibExt.mem_restrictedSignedSumset_iff, MetaMathlibExt.orderedFinset, MetaMathlibExt.initialSegment, MetaMathlibExt.IsIndexedAP, MetaMathlibExt.scaleFinset
statement: formalized
---

# Restricted signed sumsets

35 results, 15 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html).

## Restricted sumset

For a natural number $h$ and a finite subset $A$ of an additive
commutative monoid $G$, the restricted sumset $h^{\wedge} A$ is the set of all sums
$\sum_{a \in B} a$ with $B$ an $h$-element subset of $A$, that is, the sums of $h$ distinct
elements of $A$. In particular $0^{\wedge} A = \{0\}$.

The source works in the integers; here $G$ is an arbitrary additive commutative monoid.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Definition of restricted sumset.

Formalized by `MetaMathlibExt.restrictedSumset`, a definition declared in [MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#restricted-sumset).

## Restricted signed sumset

For a natural number $h$ and a finite set $A$ of integers, the
restricted signed sumset $h^{\wedge}_{\pm} A$ is the set of all integers
$\sum_{a \in B} a - 2 \sum_{a \in N} a$, where $B$ ranges over the $h$-element subsets of $A$ and
$N$ ranges over the subsets of $B$. These are the sums of the elements of $B$ in which the
elements of $N$ are given a negative sign.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Definition of restricted signed sumset.

Formalized by `MetaMathlibExt.restrictedSignedSumset`, a definition declared in [MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#restricted-signed-sumset).

## Coefficient description of the restricted sumset

For a natural number $h$, a finite set
$A$ of integers and an integer $x$, $x$ lies in the restricted sumset $h^{\wedge} A$ if and only
if there is a function $c : \mathbb{Z} \to \mathbb{Z}$ with $c(a) \in \{0, 1\}$ for every
$a \in A$, $\sum_{a \in A} c(a) = h$ and $x = \sum_{a \in A} c(a)\, a$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Definition of restricted sumset.

Formalized by `MetaMathlibExt.mem_restrictedSumset_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#mem-restricted-sumset-iff).

## Coefficient description of the restricted signed sumset

For a natural number $h$, a
finite set $A$ of integers and an integer $x$, $x$ lies in the restricted signed sumset
$h^{\wedge}_{\pm} A$ if and only if there is a function $c : \mathbb{Z} \to \mathbb{Z}$ with
$c(a) \in \{-1, 0, 1\}$ for every $a \in A$, $\sum_{a \in A} |c(a)| = h$ and
$x = \sum_{a \in A} c(a)\, a$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Definition of restricted signed sumset.

Formalized by `MetaMathlibExt.mem_restrictedSignedSumset_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/RestrictedSignedSumset.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#mem-restricted-signed-sumset-iff).

## Set of values of a finite integer sequence

For a sequence $a_0, \dots, a_{k-1}$ of
integers, this is the finite set $\{a_i : 0 \le i < k\}$ of its values.

No order or injectivity is assumed; the statements that use it assume what they need.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, notation for ordered finite sets.

Formalized by `MetaMathlibExt.orderedFinset`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#ordered-finset).

## Initial segment of a finite integer sequence

For a sequence $a_0, \dots, a_{k-1}$ of
integers and a natural number $n$, the initial segment of length $n$ is the set
$\{a_i : 0 \le i < k,\ i < n\}$ of the values at indices below $n$; it is the set of all values
of the sequence when $n \ge k$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, notation for initial subsets.

Formalized by `MetaMathlibExt.initialSegment`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#initial-segment).

## Finite integer sequences in arithmetic progression

A sequence $a_0, \dots, a_{k-1}$ of
integers is an arithmetic progression with common difference $d$ if $d > 0$ and
$a_{i+1} = a_i + d$ for every $i$ with $i + 1 < k$.

The condition is stated on adjacent terms, so no nonemptiness assumption is needed to name a
first term.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, definition of arithmetic progression.

Formalized by `MetaMathlibExt.IsIndexedAP`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#is-indexed-ap).

## Dilation of a finite set of integers

For an integer $d$ and a finite set $B$ of
integers, the dilation $d \cdot B$ is the set $\{db : b \in B\}$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, dilation notation.

Formalized by `MetaMathlibExt.scaleFinset`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#scale-finset).

## The first $k$ odd positive integers

For a natural number $k$, this is the set of integers
$\{1, 3, \dots, 2k - 1\} = \{2i + 1 : 0 \le i < k\}$; it is empty when $k = 0$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, odd-progression notation.

Formalized by `MetaMathlibExt.oddProgression`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#odd-progression).

## Values of a finite integer sequence after its first term

For a sequence
$a_0, \dots, a_{k-1}$ of integers, this is the set $\{a_i : 1 \le i < k\}$. When the sequence is
strictly increasing, it is the set $A' = A \setminus \{a_0\}$ obtained from
$A = \{a_0, \dots, a_{k-1}\}$ by removing its least element.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, notation `A'`.

Formalized by `MetaMathlibExt.tailFinset`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#tail-finset).

## Zero-based integer interval

For a natural number $k$, the integer interval $[0, k-1]$ is
the set $\{0, 1, \dots, k-1\}$ of integers $i$ with $0 \le i < k$; it is empty when $k = 0$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, interval notation.

Formalized by `MetaMathlibExt.zeroInterval`, a definition declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#zero-interval).

## The restricted signed 4-fold sumset of $\{1, 3, 5, 7, 9\}$

The restricted signed 4-fold
sumset $4^{\wedge}_{\pm} \{1, 3, 5, 7, 9\}$ has exactly $25$ elements.

This is an extremal five-element set of positive integers in Theorem 10 of the source: it
attains that theorem's lower bound $25$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 10 example.

Formalized by `MetaMathlibExt.card_restrictedSignedSumset_four_odd_five`, a theorem declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-odd-f).

## The restricted signed 4-fold sumset of $\{0, 1, 2, 4, 6\}$

The restricted signed 4-fold
sumset $4^{\wedge}_{\pm} \{0, 1, 2, 4, 6\}$ has exactly $21 = 8 \cdot 5 - 19$ elements.

This is the extremal value $8k - 19$ at $k = 5$ of the lower bound in Theorem 11 of the source.
Since $\{0, 1, 2, 4, 6\}$ differs from $d \cdot \{0, 1, 2, 3, 4\}$ for every integer $d$, it
refutes the inverse sentence of that theorem (the counterexample is ours, not the paper's).

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 11 (lower bound `8k - 19` at `k = 5`).

Formalized by `MetaMathlibExt.card_restrictedSignedSumset_four_counterexample`, a theorem declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-count).

## $\{0, 1, 2, 4, 6\}$ is not a dilate of $\{0, 1, 2, 3, 4\}$

For every integer $d$, the
set $\{0, 1, 2, 4, 6\}$ differs from the dilation
$d \cdot \{0, 1, 2, 3, 4\} = \{0, d, 2d, 3d, 4d\}$.

Indeed, $1 = di$ with $0 \le i \le 4$ forces $d = \pm 1$, and then $6$ is not of the form $di$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 11 (inverse sentence, `A = d * [0,k-1]`).

Formalized by `MetaMathlibExt.ne_scaleFinset_zeroInterval_five`, a theorem declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#ne-scale-finset-zero-interval-five).

## The restricted signed 3-fold sumset of $\{1, 2, 3, 4\}$

The restricted signed 3-fold
sumset $3^{\wedge}_{\pm} \{1, 2, 3, 4\}$ has exactly $19$ elements.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Definition of restricted signed sumset.

Formalized by `MetaMathlibExt.card_restrictedSignedSumset_three_four`, a theorem declared in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-three-four).

## Lower bounds for restricted signed sumsets of nonnegative integers

Let $h$ and $k$ be
integers with $1 \le h \le k$, let $A$ be a set of $k$ nonnegative integers, and write
$h^{\wedge}_{\pm} A$ for the restricted signed $h$-fold sumset of $A$. If $0 \notin A$, then
$2|h^{\wedge}_{\pm} A| \ge 4(hk - h^2) + h(h+1) + 2$; if $0 \in A$, then
$2|h^{\wedge}_{\pm} A| \ge 4(hk - h^2) + h(h-1) + 2$.

The source states these bounds divided by $2$. Its remark that they are optimal for
$h = 1$, $h = 2$ and $h = k$ is not part of this statement.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_general_lower_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-general-lo).

## Nathanson's bound for restricted sumsets and its inverse

Let $A$ be a nonempty finite
set of $k$ integers and let $h$ be a natural number with $1 \le h \le k$. Then the restricted
sumset $h^{\wedge} A$ has at least $hk - h^2 + 1$ elements. Moreover, if $k \ge 5$ and
$2 \le h \le k - 2$, then $h^{\wedge} A$ has exactly $hk - h^2 + 1$ elements if and only if there
are integers $a$ and $d > 0$ such that $A$ is the arithmetic progression of length $k$ with
first term $a$ and difference $d$, that is, $A = \{a + nd : 0 \le n < k\}$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_restrictedSumset_ge_and_eq_iff_ap` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-sumset-ge-and-eq-iff-ap).

## Restricted signed sumsets of arithmetic progressions with one more term than summands

Let $h \ge 3$ be a natural number and let $a_1 < a_2 < \cdots < a_{h+1}$ be positive integers that
form an arithmetic progression with common difference $d > 0$, that is, $a_{i+1} = a_i + d$ for
$1 \le i \le h$. Let $A = \{a_1, \ldots, a_{h+1}\}$ and let $h^{\wedge}_{\pm} A$ be the
restricted signed sumset of $A$. Then $|h^{\wedge}_{\pm} A| \ge (h+1)^2$ if $d = 2a_1$, and
$|h^{\wedge}_{\pm} A| \ge (h+1)^2 + 1$ otherwise. Moreover, $|h^{\wedge}_{\pm} A| = (h+1)^2$ if
and only if $d = 2a_1$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 3.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ap_h_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ap-h-add-o).

## Lower bound for restricted signed sumsets of arithmetic progressions

Let $h \ge 3$ and
$k \ge h + 1$ be natural numbers, and let $a_1 < a_2 < \cdots < a_k$ be integers with $a_1 > 0$
that form an arithmetic progression with common difference $d > 0$, that is,
$a_{i+1} = a_i + d$ for $1 \le i < k$. Let $A = \{a_1, \ldots, a_k\}$ and let $h^{\wedge}_{\pm} A$
be the restricted signed sumset of $A$. Then $|h^{\wedge}_{\pm} A| \ge 2hk - h^2 + 1$ if
$d = 2a_1$, and $|h^{\wedge}_{\pm} A| \ge 2hk - h^2 + 2$ otherwise. Moreover,
$|h^{\wedge}_{\pm} A| = 2hk - h^2 + 1$ if and only if $d = 2a_1$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Corollary 1.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ap_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ap-ge).

## Restricted signed sumsets of arithmetic progressions containing zero

Let $h$ and $k$ be
natural numbers with $4 \le h \le k - 1$, and let $0 = a_1 < a_2 < \cdots < a_k$ be nonnegative
integers that form an arithmetic progression with common difference $d > 0$, that is,
$a_{i+1} = a_i + d$ for $1 \le i < k$. Let $A = \{a_1, \ldots, a_k\}$ and let $h^{\wedge}_{\pm} A$
be the restricted signed sumset of $A$. Then $|h^{\wedge}_{\pm} A| = 2hk - h(h+1) + 1$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 4.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ap_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ap-zero).

## Inverse theorem for the extremal restricted signed sumset of positive integers

Let $h$
and $k$ be natural numbers with $4 \le h \le k - 1$, and let
$A = \{a_1 < a_2 < \cdots < a_k\}$ be a set of $k$ positive integers. Write
$A_{h+1} = \{a_1, \dots, a_{h+1}\}$, $A' = \{a_2, \dots, a_k\}$ and $-A' = \{-x : x \in A'\}$.
Suppose that the restricted signed sumset $h^{\wedge}_{\pm} A$ has exactly $2hk - h^2 + 1$
elements and that at least one of the following holds:
(a) there is $d > 0$ with $a_{i+1} = a_i + d$ for all $1 \le i < k$;
(b) $A_{h+1} = \{b + nd : 0 \le n \le h\}$ for some integers $b$ and $d > 0$;
(c) $h^{\wedge}_{\pm} A_{h+1}$ has at least $(h+1)^2$ elements and $4 \le h \le k - 3$;
(d) $h^{\wedge}_{\pm} A = h^{\wedge}(-A') \cup h^{\wedge}_{\pm} A_{h+1} \cup h^{\wedge} A'$, where
$h^{\wedge}$ is the restricted sumset, and $A' = \{b + nd : 0 \le n < k - 1\}$ for some
integers $b$ and $d > 0$;
(e) $h^{\wedge}_{\pm} A_{h+1}$ has at least $(h+1)^2$ elements and
$A' = \{b + nd : 0 \le n < k - 1\}$ for some integers $b$ and $d > 0$.
Then $A = a_1 \cdot \{1, 3, \dots, 2k - 1\} = \{(2i - 1) a_1 : 1 \le i \le k\}$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 5.

Stated but not proved: `MetaMathlibExt.eq_scaled_oddProgression_of_extremal` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#eq-scaled-odd-progression-of-extremal).

## Inverse theorem for the extremal restricted signed sumset of sets containing zero

Let
$h$ and $k$ be natural numbers with $4 \le h \le k - 1$, and let
$A = \{a_0 < a_1 < \cdots < a_{k-1}\}$ be a set of $k$ nonnegative integers with $a_0 = 0$.
Write $A_h = \{a_0, \dots, a_h\}$, $A' = \{a_1, \dots, a_{k-1}\}$ and
$-A' = \{-x : x \in A'\}$. Suppose that the restricted signed sumset $h^{\wedge}_{\pm} A$ has
exactly $2hk - h(h+1) + 1$ elements and that at least one of the following holds:
(a) there is $d > 0$ with $a_{i+1} = a_i + d$ for all $0 \le i < k - 1$;
(b) $A_h = \{b + nd : 0 \le n \le h\}$ for some integers $b$ and $d > 0$;
(c) $h^{\wedge}_{\pm} A_h$ has at least $h(h+1) + 1$ elements and $4 \le h \le k - 3$;
(d) $h^{\wedge}_{\pm} A = h^{\wedge}(-A') \cup h^{\wedge}_{\pm} A_h \cup h^{\wedge} A'$, where
$h^{\wedge}$ is the restricted sumset, and $A' = \{b + nd : 0 \le n < k - 1\}$ for some
integers $b$ and $d > 0$;
(e) $h^{\wedge}_{\pm} A_h$ has at least $h(h+1) + 1$ elements and
$A' = \{b + nd : 0 \le n < k - 1\}$ for some integers $b$ and $d > 0$.
Then $A = a_1 \cdot \{0, 1, \dots, k - 1\} = \{i a_1 : 0 \le i < k\}$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 6.

Stated but not proved: `MetaMathlibExt.eq_scaled_zeroInterval_of_extremal` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#eq-scaled-zero-interval-of-extremal).

## Restricted signed sumsets of sets with Fibonacci-type growth

Let $h \ge 3$ and let
$a_1 < a_2 < \dots < a_{h+1}$ be positive integers such that $a_i \ge a_{i-1} + a_{i-2}$ for
every $i$ with $4 \le i \le h + 1$. Write $h^{\wedge}_{\pm} A$ for the restricted signed
$h$-fold sumset of $A = \{a_1, \dots, a_{h+1}\}$. Then $|h^{\wedge}_{\pm} A| \ge (h+1)^2 + 1$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 7.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ge_of_fibonacci_growth` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ge-of-fibo).

## Restricted signed sumsets under gap conditions

Let $h \ge 3$ and let
$a_1 < a_2 < \dots < a_{h+1}$ be positive integers such that $a_3 - a_2 < 2a_1$ and
$a_2 - a_1 < 2(a_i - a_{i-1})$ for every $i$ with $4 \le i \le h + 1$. Write
$h^{\wedge}_{\pm} A$ for the restricted signed $h$-fold sumset of $A = \{a_1, \dots, a_{h+1}\}$.
Then $|h^{\wedge}_{\pm} A| \ge (h+1)^2 + 1$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 8.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ge_of_gap_conditions` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ge-of-gap).

## Lower bound for restricted signed 4-fold sumsets of positive integers

Let $k \ge 5$,
let $A$ be a set of $k$ positive integers, and write $4^{\wedge}_{\pm} A$ for the restricted
signed 4-fold sumset of $A$. Then $|4^{\wedge}_{\pm} A| \ge 8k - 15$. Moreover,
$|4^{\wedge}_{\pm} A| = 8k - 15$ if and only if $A = m \cdot \{1, 3, \dots, 2k - 1\}$, where
$m = \min A$ and $m \cdot B = \{mb : b \in B\}$.

The source states only that equality forces this form; the converse is included here.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 9.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge).

## Restricted signed fourfold sumsets of five positive integers

Let $A$ be a set of five
positive integers and let $4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. For an
integer $m$ and a set $B$ of integers write $m \cdot B = \{mb : b \in B\}$. Then
$|4^{\wedge}_{\pm} A| \ge 25$, and $|4^{\wedge}_{\pm} A| = 25$ if and only if
$A = m \cdot \{1, 3, 5, 7, 9\}$ for $m = \min A$.

The source states the equality case only in the direction that equality forces this form; the
converse is included here.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 10.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_five_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-five).

## Lower bound for restricted signed 4-fold sumsets of nonnegative sets containing zero

Let $k \ge 5$, let $A$ be a set of $k$ nonnegative integers with $0 \in A$, and write
$4^{\wedge}_{\pm} A$ for the restricted signed 4-fold sumset of $A$. Then
$|4^{\wedge}_{\pm} A| \ge 8k - 19$.

The inverse statement of the source, that equality forces $A = d \cdot \{0, 1, \dots, k - 1\}$
for some integer $d$ (where $d \cdot B = \{db : b \in B\}$), is omitted: $A = \{0, 1, 2, 4, 6\}$
has $|4^{\wedge}_{\pm} A| = 21 = 8 \cdot 5 - 19$ but is not of that form.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Theorem 11.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_nonnegative_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-nonne).

## Extending a restricted signed sumset bound from the first $h+1$ elements

Let $h \ge 3$
and $k \ge h + 1$, let $a_1 < a_2 < \dots < a_k$ be positive integers, and let $t \ge 0$ be an
integer. Put $A = \{a_1, \dots, a_k\}$ and $A_{h+1} = \{a_1, \dots, a_{h+1}\}$, and write
$h^{\wedge}_{\pm} B$ for the restricted signed $h$-fold sumset of a finite set $B$. If
$|h^{\wedge}_{\pm} A_{h+1}| \ge (h+1)^2 + t$, then $|h^{\wedge}_{\pm} A| \ge 2hk - h^2 + 1 + t$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 1.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_ge_of_initialSegment` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-ge-of-init).

## Restricted signed 4-fold sumsets when exactly one gap differs from twice the minimum

Let $a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let $A = \{a_1, \dots, a_5\}$,
and write $4^{\wedge}_{\pm} A$ for the restricted signed 4-fold sumset of $A$. If exactly one
of the four gaps $a_{i+1} - a_i$ with $i \in \{1, 2, 3, 4\}$ differs from $2a_1$, then
$|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_one_exceptional_gap` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of).

## Restricted signed fourfold sumsets when exactly two gaps differ from twice the least element

**Restricted signed fourfold sumsets when exactly two gaps differ from twice the least
element.** Let $a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let
$A = \{a_1, \ldots, a_5\}$ and let $4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. If
exactly two of the four gaps $a_{i+1} - a_i$ ($1 \le i \le 4$) differ from $2a_1$, then
$|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 4.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_two_exceptional_gaps` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-2).

## Restricted signed fourfold sumsets when exactly one gap equals twice the least element

Let $a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let $A = \{a_1, \ldots, a_5\}$ and
let $4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. If exactly one of the four gaps
$a_{i+1} - a_i$ ($1 \le i \le 4$) equals $2a_1$, then $|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 5.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_one_regular_gap` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-3).

## Restricted signed fourfold sumsets when no gap equals twice the least element and the first and third gaps differ

**Restricted signed fourfold sumsets when no gap equals twice the least element and the first
and third gaps differ.** Let $a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let
$A = \{a_1, \ldots, a_5\}$ and let $4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. If
none of the four gaps $a_{i+1} - a_i$ ($1 \le i \le 4$) equals $2a_1$ and
$a_4 - a_3 \ne a_2 - a_1$, then $|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 6.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_unequal_outer_gaps` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-4).

## Restricted signed fourfold sumsets when no gap equals twice the least element, the first and third gaps agree, and the last two gaps do not sum to twice the least element

**Restricted signed fourfold sumsets when no gap equals twice the least element, the first and
third gaps agree, and the last two gaps do not sum to twice the least element.** Let
$a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let $A = \{a_1, \ldots, a_5\}$ and let
$4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. If none of the four gaps
$a_{i+1} - a_i$ ($1 \le i \le 4$) equals $2a_1$, $a_4 - a_3 = a_2 - a_1$ and
$a_5 - a_3 \ne 2a_1$, then $|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 7.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_equal_outer_gaps_ne` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-5).

## Restricted signed fourfold sumsets when no gap equals twice the least element, the first and third gaps agree, and the last two gaps sum to twice the least element

**Restricted signed fourfold sumsets when no gap equals twice the least element, the first and
third gaps agree, and the last two gaps sum to twice the least element.** Let
$a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let $A = \{a_1, \ldots, a_5\}$ and let
$4^{\wedge}_{\pm} A$ be the restricted signed sumset of $A$. If none of the four gaps
$a_{i+1} - a_i$ ($1 \le i \le 4$) equals $2a_1$, $a_4 - a_3 = a_2 - a_1$ and
$a_5 - a_3 = 2a_1$, then $|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 8.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_equal_outer_gaps_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-6).

## Restricted signed 4-fold sumsets when no gap equals twice the minimum

Let
$a_1 < a_2 < a_3 < a_4 < a_5$ be integers with $a_1 > 0$, let $A = \{a_1, \dots, a_5\}$, and
write $4^{\wedge}_{\pm} A$ for the restricted signed 4-fold sumset of $A$. If
$a_{i+1} - a_i \ne 2a_1$ for every $i \in \{1, 2, 3, 4\}$, then $|4^{\wedge}_{\pm} A| \ge 26$.

## Sources

- Mohan, Raj Kumar Mistri, Ram Krishna Pandey, *Some Direct and Inverse Problems for the Restricted Signed Sumset in the Set of Integers*, INTEGERS 24 (2024), Article A81, Lemma 9.

Stated but not proved: `MetaMathlibExt.card_restrictedSignedSumset_four_ge_of_no_regular_gap` is written with `theorem_wanted` in [WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RestrictedSignedSumsetWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html#card-restricted-signed-sumset-four-ge-of-7).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted signed sumsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/restricted-signed-sumsets)
