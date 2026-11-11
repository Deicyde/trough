---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.GroupedYFastTrie, Cslib.Algorithms.Lean.GroupedYFastTrie.contents, Cslib.Algorithms.Lean.GroupedYFastTrie.mem_contents_iff, Cslib.Algorithms.Lean.GroupedYFastTrie.GroupOrdered, Cslib.Algorithms.Lean.GroupedYFastTrie.Valid, Cslib.Algorithms.Lean.GroupedYFastTrie.findGroup, Cslib.Algorithms.Lean.GroupedYFastTrie.repGe, Cslib.Algorithms.Lean.GroupedYFastTrie.member
statement: formalized
proof: formalized
---

# Y-fast trie

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html).

## Grouped y-fast trie

## Grouped y-fast trie

For natural numbers $w$ and $B$, a grouped y-fast trie over $w$-bit
keys with group bound $B$ consists of an x-fast trie over $w$-bit keys, which holds the
representatives, and a list of groups, each a list of $w$-bit keys. The structure itself imposes
no condition on these fields; the intended invariants (the representative trie is a valid x-fast
trie whose keys are exactly the group maxima, every group is nonempty, strictly sorted and of
length at most $B$, and the groups are in increasing order) are imposed by the validity
predicate.

Each group is a sorted list standing in for a balanced search tree; no complexity bound is
claimed.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#grouped-yfast-trie).

## Keys of a grouped y-fast trie

The key set of a grouped y-fast trie $t$ is the finite
set of all keys that occur in some group of $t$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#contents).

## Stored keys are the keys of the groups

For every grouped y-fast trie $t$ over $w$-bit
keys and every key $x$, $x$ lies in the contents of $t$ if and only if $x$ belongs to some group
of $t$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.mem_contents_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#mem-contents-iff).

## Ordered list of groups

A list of groups, each a list of $w$-bit keys, is group ordered
when every key of an earlier group is smaller than every key of a later group.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.GroupOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#group-ordered).

## Validity of a grouped y-fast trie

A grouped y-fast trie $t$ over keys in
$\{0, \dots, 2^w - 1\}$ with group bound $B$ is valid when its representative trie is a valid
x-fast trie; a key $r$ is stored in the representative trie exactly when $r$ is the last element
of some group of $t$; every group of $t$ is nonempty, has at most $B$ keys, and is strictly
increasing; and the groups of $t$ are ordered, that is, every key of an earlier group is smaller
than every key of a later group.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#valid).

## Group of a representative

For a grouped y-fast trie $t$ and a key $r$, the group of $r$
is the first group of $t$, in the order of the groups, whose last element is $r$, or the empty
list if no group of $t$ ends with $r$.

In a valid trie every group is strictly increasing, so its last element is its maximum.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.findGroup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#find-group).

## Least representative at or above a key

For a grouped y-fast trie $t$ and a key $x$,
the result is $x$ itself if the membership test of the representative x-fast trie of $t$ (a
single probe of its deepest level) reports $x$ as present. Otherwise it is the successor of $x$
in the representative x-fast trie, that is, the least representative greater than $x$, or
nothing if there is none.

When $t$ is valid, the result is the least representative $r$ with $x \le r$, and nothing
when there is no such representative.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.repGe`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#rep-ge).

## Membership query of a grouped y-fast trie

Given a grouped y-fast trie $t$ over $w$-bit
keys and a key $x$, the query first finds a representative $r$: $r = x$ if the membership probe of
the representative x-fast trie accepts $x$, and otherwise $r$ is the successor of $x$ in the
representative trie. If there is no such $r$, the query returns false. Otherwise it returns
whether $x$ belongs to the group owned by $r$, namely the first group of $t$ whose last element is
$r$ (the empty list if there is none).

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.member`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#member).

## Correctness of the y-fast trie membership query

Let $t$ be a valid grouped y-fast trie
over $w$-bit keys. Then for every key $x$, the membership query on $t$ (locate the least
representative at least $x$, then scan its group) returns true at $x$ if and only if $x$ lies in
the contents of $t$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.member_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#member-iff).

## Successor query in a grouped y-fast trie

For a grouped y-fast trie $t$ and a key
$x$, let $r$ be the least key greater than $x$ stored in the representative x-fast trie of
$t$; if there is none, the query returns nothing. Otherwise let $g$ be the first group of $t$
whose last element is $r$, or the empty list if no group has last element $r$. The query then
returns the first key of $g$ greater than $x$, or nothing if $g$ has no such key.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.successor`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#successor).

## Successor query returns the least larger stored key

Let $t$ be a valid grouped y-fast
trie and let $x$, $y$ be keys. The successor query for $x$ in $t$ returns $y$ if and only if
$y$ is stored in $t$, $x < y$, and $y \le z$ for every key $z$ stored in $t$ with $x < z$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.successor_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#successor-eq-some-iff).

## Successor query fails exactly when no larger key is stored

Let $t$ be a valid grouped
y-fast trie and $x$ a key. The successor query for $x$ in $t$ returns nothing if and only if no
key stored in $t$ is greater than $x$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.successor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#successor-eq-none-iff).

## The empty grouped y-fast trie

For every key length $w$ and group bound $B$, the empty
grouped y-fast trie has the empty x-fast trie as its trie of representatives and has no
groups.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#empty).

## The empty grouped y-fast trie is valid

For every key width $w$ and group bound $B$,
the empty grouped y-fast trie satisfies the grouped y-fast trie invariant.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#valid-empty).

## The empty grouped y-fast trie has no members

For all natural numbers $w$ and $B$ and
every $w$-bit key $x$, the membership query on the empty grouped y-fast trie over $w$-bit keys
with group bound $B$ returns false at $x$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.member_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#member-empty).

## The empty grouped y-fast trie has no successors

For every key $x$, the successor query
for $x$ in the empty grouped y-fast trie returns nothing.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.successor_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#successor-empty).

## Representative trie of a list

For a list $rs$ of $w$-bit keys, the representative
x-fast trie of $rs$ is obtained from the empty x-fast trie over $w$-bit keys by inserting the
elements of $rs$ one at a time, from first to last.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.mkReps`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#mk-reps).

## Inserting a list of keys into the empty x-fast trie gives a valid trie

For every list
of $w$-bit keys, the x-fast trie obtained from the empty x-fast trie by inserting the keys of
the list one at a time satisfies the x-fast trie invariant: each level holds exactly the
prefixes of that length of the stored keys.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.valid_mkReps`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#valid-mk-reps).

## Keys of the trie of representatives

For every list $L$ of $w$-bit keys, the x-fast
trie obtained by inserting the elements of $L$ one by one into the empty x-fast trie stores
exactly the elements of $L$: its key set is the set of elements of $L$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.contents_mkReps`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#contents-mk-reps).

## Grouped y-fast trie from a list of groups

For a list of groups $g_1, \dots, g_k$,
each a list of $w$-bit keys, and any group-size bound $B$, this is the grouped y-fast trie
whose groups are $g_1, \dots, g_k$ in this order and whose representative x-fast trie is
obtained from the empty x-fast trie by inserting the last element of each nonempty group,
in order. No condition on the groups is checked here; when a group is sorted, its last
element is its maximum.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.ofGroups`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#of-groups).

## Assembling a valid grouped y-fast trie from groups

Let $w$ and $B$ be natural numbers
and let $g_1, \dots, g_k$ be a list of groups, each a list of keys in $\{0, \dots, 2^w - 1\}$.
Suppose every group is nonempty, has at most $B$ keys, and is strictly increasing, and the
groups are ordered: every key of an earlier group is smaller than every key of a later group.
Then the grouped y-fast trie with group bound $B$ assembled from these groups, whose
representatives are the last elements of the groups, is valid.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.valid_ofGroups`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#valid-of-groups).

## Fuel-bounded chunking

Given a bound $B$, a fuel $n$ and a list $l$ of $w$-bit keys, the
fuel-bounded chunking is the empty list of chunks when $n = 0$ or $l$ is empty; otherwise it is
the chunk formed by the first $\min(B, |l|)$ elements of $l$, followed by the fuel-bounded
chunking with bound $B$ and fuel $n - 1$ of the remaining elements of $l$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.chunkGroupsAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#chunk-groups-aux).

## Chunking a list into groups

Given a bound $B$ and a list $l$ of $w$-bit keys, when
$B > 0$ the chunking of $l$ cuts $l$ from the left into consecutive chunks of exactly $B$
elements each, except that the last chunk holds the remaining one to $B$ elements; there are no
chunks when $l$ is empty. When $B = 0$, the chunking has no chunks if $l$ is empty and is the
single chunk $l$ otherwise.

So every chunk has at most $B$ elements when $B > 0$, but not when $B = 0$ and $l$ is
nonempty.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.chunkGroups`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#chunk-groups).

## Chunking with bound zero

For every nonempty list $l$ of $w$-bit keys, the chunking of
$l$ with bound $B = 0$ consists of the single chunk $l$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.chunkGroups_zero_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#chunk-groups-zero-of-ne).

## Chunking preserves the list

For every bound $B$ (including $B = 0$) and every list $l$
of $w$-bit keys, concatenating the chunks of the chunking of $l$ with bound $B$, in order,
gives back $l$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.flatten_chunkGroups`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#flatten-chunk-groups).

## Chunks of a sorted list

Let $B > 0$ and let $l$ be a strictly increasing list of
$w$-bit keys. Then every chunk of the chunking of $l$ into groups of at most $B$ keys is
nonempty, has at most $B$ elements, and is strictly increasing.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.chunkGroups_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#chunk-groups-spec).

## Chunks of a sorted list are ordered

Let $B$ be a natural number and let $l$ be a
strictly increasing list of $w$-bit keys. Then the chunk groups of $l$ with bound $B$ are group
ordered: every key of an earlier chunk is smaller than every key of a later chunk.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.groupOrdered_chunkGroups`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#group-ordered-chunk-groups).

## Grouped y-fast trie from a sorted list

For a group bound $B$ and a list $l$ of
$w$-bit keys, this is the grouped y-fast trie whose groups, in order, are consecutive pieces of
$l$ that together make up $l$, and whose representative x-fast trie is obtained from the empty
x-fast trie by inserting the last element of each group, in order. If $B > 0$, the groups are
obtained by repeatedly cutting off the first $B$ keys, so every group has exactly $B$ keys
except possibly the last, which has between one and $B$ keys. If $B = 0$, the only group is $l$
itself. In both cases there are no groups when $l$ is empty.

The construction is intended for strictly increasing $l$. It yields a valid trie when $B > 0$
and $l$ is strictly increasing, and an invalid one when $B = 0$ and $l$ is nonempty.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.ofSortedList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#of-sorted-list).

## Building from a sorted list gives a valid grouped y-fast trie

Let $w$ and $B$ be
natural numbers with $0 < B$, and let $l$ be a strictly increasing list of keys in
$\{0, \dots, 2^w - 1\}$. Then the grouped y-fast trie with group bound $B$ built from $l$ by
cutting it into consecutive groups of at most $B$ keys is valid.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.valid_ofSortedList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 659](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#valid-of-sorted-list).

## Building from a nonempty list with group bound zero gives an invalid trie

For every
natural number $w$ and every nonempty list $l$ of $w$-bit keys, the grouped y-fast trie with
group bound $B = 0$ built from $l$ is not valid.

With $B = 0$ the only group is $l$ itself, which has more than $0$ keys. For $B > 0$ and strictly
increasing $l$, the grouped y-fast trie built from $l$ is valid.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.not_valid_ofSortedList_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#not-valid-of-sorted-list-zero).

## Keys of the grouped y-fast trie built from a list

For every group bound $B$ (including
$B = 0$) and every list $l$ of $w$-bit keys, sorted or not, the key set of the grouped y-fast
trie built from $l$ with group bound $B$ is exactly the set of elements of $l$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.contents_ofSortedList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#contents-of-sorted-list).

## Membership in a trie built from a sorted list

Let $B > 0$ and let $l$ be a strictly
increasing list of $w$-bit keys. Then for every key $x$, the membership query on the grouped
y-fast trie built from $l$ with group bound $B$ returns true at $x$ if and only if $x$ belongs
to $l$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.member_ofSortedList_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#member-of-sorted-list-iff).

## Successor in the trie built from a sorted list

Let $B > 0$, let $l$ be a strictly
increasing list of $w$-bit keys, and let $x$, $y$ be keys. The successor query for $x$ in the
grouped y-fast trie built from $l$ with group bound $B$ returns $y$ if and only if $y$ belongs
to $l$, $x < y$, and $y \le z$ for every $z$ in $l$ with $x < z$.

Formalized by `Cslib.Algorithms.Lean.GroupedYFastTrie.successor_ofSortedList_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/YFastTrie.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html#successor-of-sorted-list-eq-some-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Y-fast trie](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/y-fast-trie)
