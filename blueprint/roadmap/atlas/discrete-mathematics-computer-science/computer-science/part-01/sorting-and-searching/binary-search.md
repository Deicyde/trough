---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.binSearchContains_eq_isSome, Cslib.Algorithms.Lean.binSearch_eq_some_iff, Cslib.Algorithms.Lean.binSearch_eq_none_iff, Cslib.Algorithms.Lean.binSearchContains_eq_true_iff, Cslib.Algorithms.Lean.binSearch_eq_some_iff_mem, Cslib.Algorithms.Lean.binSearch_eq_none_iff_not_mem, Cslib.Algorithms.Lean.binSearchContains_eq_true_iff_mem, Cslib.Algorithms.Lean.TimeM.lowerBound
statement: formalized
proof: formalized
---

# Binary search

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html).

## Array binary search membership test agrees with binary search

Let $A$ be an array with
entries in a type $\alpha$, let $k \in \alpha$, let $\mathrm{lt}$ be any Boolean-valued comparison
on $\alpha$, and let $\ell$ and $h$ be natural numbers. Lean core's Boolean binary search
membership test for $k$ in $A$, with comparison $\mathrm{lt}$ and bounds $\ell$ and $h$, returns
true exactly when Lean core's array binary search with the same arguments returns some element.

Formalized by `Cslib.Algorithms.Lean.binSearchContains_eq_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-contains-eq-is-some).

## Result of bounded binary search on a sorted array

Let $A = (a_0, \dots, a_{n-1})$ be an
array of length $n$ with entries in a linearly ordered type, with $a_i \le a_j$ whenever $i < j$.
Let $k$ and $a$ be elements of that type and $\ell$, $h$ natural numbers. Lean core's array binary
search for $k$ in $A$, with the strict order $<$ as comparison and inclusive bounds $\ell$ and
$h$, returns $a$ if and only if $a = k$ and there is an index $i < n$ with $\ell \le i \le h$ and
$a_i = k$.

The requirement $i < n$ reflects the implementation's clamping of an upper bound $h \ge n$ to
$n - 1$.

Formalized by `Cslib.Algorithms.Lean.binSearch_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-eq-some-iff).

## Bounded binary search on a sorted array fails exactly when the key is absent

Let
$A = (a_0, \dots, a_{n-1})$ be an array of length $n$ with entries in a linearly ordered type,
with $a_i \le a_j$ whenever $i < j$. Let $k$ be an element of that type and $\ell$, $h$ natural
numbers. Lean core's array binary search for $k$ in $A$, with the strict order $<$ as comparison
and inclusive bounds $\ell$ and $h$, returns no element if and only if there is no index $i < n$
with $\ell \le i \le h$ and $a_i = k$.

Formalized by `Cslib.Algorithms.Lean.binSearch_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-eq-none-iff).

## Bounded binary search membership test on a sorted array is correct

Let
$A = (a_0, \dots, a_{n-1})$ be an array of length $n$ with entries in a linearly ordered type,
with $a_i \le a_j$ whenever $i < j$. Let $k$ be an element of that type and $\ell$, $h$ natural
numbers. Lean core's Boolean binary search membership test for $k$ in $A$, with the strict order
$<$ as comparison and inclusive bounds $\ell$ and $h$, returns true if and only if there is an
index $i < n$ with $\ell \le i \le h$ and $a_i = k$.

Formalized by `Cslib.Algorithms.Lean.binSearchContains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-contains-eq-true-iff).

## Binary search on a sorted array finds exactly its members

Let $A$ be an array with entries
in a linearly ordered type, sorted so that an earlier entry is never greater than a later one, and
let $k$ and $a$ be elements of that type. Lean core's array binary search for $k$ over the whole of
$A$, with the strict order $<$ as comparison, returns $a$ if and only if $a = k$ and $k$ is an
entry of $A$.

Formalized by `Cslib.Algorithms.Lean.binSearch_eq_some_iff_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-eq-some-iff-mem).

## Binary search on a sorted array fails exactly on non-members

Let $A$ be an array with
entries in a linearly ordered type, sorted so that an earlier entry is never greater than a later
one, and let $k$ be an element of that type. Lean core's array binary search for $k$ over the
whole of $A$, with the strict order $<$ as comparison, returns no element if and only if $k$ is
not an entry of $A$.

Formalized by `Cslib.Algorithms.Lean.binSearch_eq_none_iff_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-eq-none-iff-not-mem).

## Binary search membership test on a sorted array is correct

Let $A$ be an array with
entries in a linearly ordered type, sorted so that an earlier entry is never greater than a later
one, and let $k$ be an element of that type. Lean core's Boolean binary search membership test
for $k$ over the whole of $A$, with the strict order $<$ as comparison, returns true if and only
if $k$ is an entry of $A$.

Formalized by `Cslib.Algorithms.Lean.binSearchContains_eq_true_iff_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Binary.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Binary.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#bin-search-contains-eq-true-iff-mem).

## Lower-bound search

Given an array $a = (a_0, \dots, a_{n-1})$ over a linearly ordered type and
a key $k$, lower-bound search maintains a half-open interval $[l, h)$ of indices, starting from
$[0, n)$. While $l < h$, it compares $a_m$ with $k$ at the midpoint
$m = l + \lfloor (h - l)/2 \rfloor$, charging one unit for this comparison, and continues with
$[m + 1, h)$ if $a_m < k$ and with $[l, m)$ otherwise. When $l = h$ it returns $l$.

When $a$ is sorted in nondecreasing order (or at least partitioned at $k$: every entry before the
returned index is $< k$ and every entry from that index on is $\ge k$), the result is the first
index $i$ with $k \le a_i$, or $n$ if every entry is below $k$. On an unsorted array the result is
unspecified: for $a = (2, 1)$ and $k = 2$ the search returns $2$, not the first index $0$ with
$k \le a_0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.lowerBound`, a definition declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#lower-bound).

## Correctness of lower-bound search

Let $a = (a_0, \dots, a_{n-1})$ be an array over a linearly
ordered type, sorted in nondecreasing order, let $k$ be a key, and let $\ell$ be the index returned
by lower-bound search for $k$ in $a$. Then $\ell \le n$, $a_j < k$ for every $j < \ell$, and
$k \le a_j$ for every $j$ with $\ell \le j < n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.lowerBound_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#lower-bound-spec).

## Comparison bound for lower-bound search

For every array $a$ of length $n$ over a linearly
ordered type and every key $k$, lower-bound search for $k$ in $a$ makes at most
$\lceil \log_2 (n + 1) \rceil$ element comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.lowerBound_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#lower-bound-time-le).

## Binary search for the first occurrence

Given an array $a = (a_0, \dots, a_{n-1})$ over a
linearly ordered type and a key $k$, binary search for the first occurrence of $k$ in $a$ runs
lower-bound search for $k$ in $a$, obtaining an index $\ell$. If $\ell < n$, it makes one further
comparison, charged one unit, and returns $\ell$ when $a_\ell = k$ and no index otherwise; if
$\ell \ge n$, it returns no index without further cost.

When $a$ is sorted in nondecreasing order, the result is the first index $i$ with $a_i = k$, or no
index when $k$ does not occur in $a$. On an unsorted array a present key can be missed and the
result can be no index.

Formalized by `Cslib.Algorithms.Lean.TimeM.binarySearchFirst?`, a definition declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#binary-search-first).

## Binary search returns the first occurrence of the key

Let $a = (a_0, \dots, a_{n-1})$ be
an array over a linearly ordered type, sorted in nondecreasing order, let $k$ be a key and let $i$
be a natural number. Binary search for the first occurrence of $k$ in $a$ returns the index $i$ if
and only if $i < n$, $a_i = k$, and $a_j < k$ for every $j < i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.binarySearchFirst?_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#binary-search-first-eq-some-iff).

## Binary search reports absence exactly when the key is absent

Let
$a = (a_0, \dots, a_{n-1})$ be an array over a linearly ordered type, sorted in nondecreasing
order, and let $k$ be a key. Binary search for the first occurrence of $k$ in $a$ returns no index
if and only if $a_i \ne k$ for every $i < n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.binarySearchFirst?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#binary-search-first-eq-none-iff).

## Exact comparison count of binary search for the first occurrence

Let $a$ be an array of
length $n$ over a linearly ordered type, let $k$ be a key, and let $\ell$ be the index returned by
lower-bound search for $k$ in $a$. The number of element comparisons made by binary search for the
first occurrence of $k$ in $a$ equals the number made by lower-bound search for $k$ in $a$, plus
$1$ if $\ell < n$ and plus $0$ otherwise.

Formalized by `Cslib.Algorithms.Lean.TimeM.binarySearchFirst?_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#binary-search-first-time).

## Comparison bound for binary search for the first occurrence

For every array $a$ of length
$n$ over a linearly ordered type and every key $k$, binary search for the first occurrence of $k$
in $a$ makes at most $\lceil \log_2 (n + 1) \rceil + 1$ element comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.binarySearchFirst?_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/LowerBound.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/LowerBound.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html#binary-search-first-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary search](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/binary-search/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/binary-search)
