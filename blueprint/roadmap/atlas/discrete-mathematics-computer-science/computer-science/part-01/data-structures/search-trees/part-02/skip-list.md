---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SkipList.Entry, Cslib.Algorithms.Lean.SkipList, Cslib.Algorithms.Lean.SkipList.empty, Cslib.Algorithms.Lean.SkipList.Valid, Cslib.Algorithms.Lean.SkipList.level, Cslib.Algorithms.Lean.SkipList.abstraction, Cslib.Algorithms.Lean.SkipList.heightOf, Cslib.Algorithms.Lean.SkipList.advanceAtLevel
statement: formalized
proof: formalized
---

# Skip list

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html).

## Skip-list node

A skip-list node consists of a key, a value and a natural number, the
height of its tower. The node itself does not require the height to be positive; positivity is
part of the validity invariant of skip lists.

Formalized by `Cslib.Algorithms.Lean.SkipList.Entry`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#entry).

## Skip list

A deterministic skip list with keys in $\alpha$ and values in $\beta$ is
represented by the list of its bottom-level nodes, each node an entry carrying a key in $\alpha$,
a value in $\beta$ and a tower height, a natural number. No ordering or height condition is
imposed by this structure.

Formalized by `Cslib.Algorithms.Lean.SkipList`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#skip-list).

## Empty skip list

The empty skip list is the skip list with no nodes.

Formalized by `Cslib.Algorithms.Lean.SkipList.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#empty).

## Valid skip list

Let $\alpha$ be a linearly ordered type. A skip list with keys in
$\alpha$ and values in $\beta$ is valid when the keys of its bottom-level nodes are strictly
increasing along the list and every node has a tower of positive height.

Formalized by `Cslib.Algorithms.Lean.SkipList.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#valid).

## Level of a skip list

For a skip list and a level index $i$ (levels are numbered from $0$
at the bottom), level $i$ is the list of key-value pairs $(k, v)$ of the stored nodes whose tower
height $h$ satisfies $i < h$, in the order in which these nodes appear in the bottom-level list
of the skip list.

Formalized by `Cslib.Algorithms.Lean.SkipList.level`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#level).

## Bottom-level abstraction of a skip list

The bottom-level abstraction of a skip list is
the association list obtained from its bottom-level nodes, in order, by keeping the key-value
pair $(k, v)$ of each node and forgetting its tower height.

Formalized by `Cslib.Algorithms.Lean.SkipList.abstraction`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#abstraction).

## Stored tower height of a key

For a key $k$ and a skip list $S$, the stored tower height
of $k$ in $S$ is the tower height of the first bottom-level node of $S$ whose key equals $k$
under the given Boolean equality test on keys; it is undefined when no node has key $k$.

Formalized by `Cslib.Algorithms.Lean.SkipList.heightOf`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#height-of).

## One level of skip-list search

Let $k$ be a search key, $i$ a zero-based level and $L$
a list of skip-list nodes. Let $P$ be the longest prefix of $L$ whose nodes all have keys less
than $k$. If some node of $P$ has tower height greater than $i$ (so it is visible at level
$i$), advancing at level $i$ returns the part of $L$ after the last such node; otherwise it
returns $L$ unchanged.

The returned suffix is the window that every lower level continues to scan.

Formalized by `Cslib.Algorithms.Lean.SkipList.advanceAtLevel`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#advance-at-level).

## Skip-list search window

Let $k$ be a key and let $H$ be the greatest tower height in a
skip list ($H = 0$ if the list is empty or every tower has height $0$). Start with the full list
of bottom-level nodes, and for each level $i$ from $H - 1$ down to $0$ in turn (no levels when
$H = 0$) replace the current list by the result of advancing at level $i$: within the longest
initial segment of the current list whose keys are all less than $k$, take the last node whose
tower height exceeds $i$ and keep only the nodes after it, leaving the list unchanged if there is
no such node. The search window for $k$ is the list that remains after these steps.

Formalized by `Cslib.Algorithms.Lean.SkipList.searchWindow`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#search-window).

## Skip-list lookup

The lookup of a key $k$ in a skip list computes the search window for
$k$, the suffix of the bottom-level nodes reached by descending from the highest level to level
$0$, and returns the value of the first node in the window whose key is $k$, or no value if the
window has no such node.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup).

## Skip-list insertion

To insert key $k$ with value $v$ and requested height $h$ into a
skip list, scan its bottom-level nodes in order, keeping every node whose key is less than $k$.
At the first node whose key is not less than $k$: if its key equals $k$, its value is replaced
by $v$ and its tower height is kept; if its key is greater than $k$, a new node with key $k$,
value $v$ and tower height $\max(1, h)$ is placed before it. If every key is less than $k$, the
new node is appended at the end.

Formalized by `Cslib.Algorithms.Lean.SkipList.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#insert).

## The empty skip list is valid

For every linearly ordered type $\alpha$ and every type
$\beta$, the empty skip list with keys in $\alpha$ and values in $\beta$ is valid.

Formalized by `Cslib.Algorithms.Lean.SkipList.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#valid-empty).

## Skip-list levels are sorted by key

If a skip list is valid, then for every level index
$i$ (levels are numbered from $0$ at the bottom), the keys in the list of key-value pairs visible
at level $i$ are strictly increasing: every pair has a strictly smaller key than every pair after
it.

Formalized by `Cslib.Algorithms.Lean.SkipList.level_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#level-pairwise).

## Each skip-list level is a subsequence of the level below

For every skip list and every
level index $i$ (levels are numbered from $0$ at the bottom), the list of key-value pairs visible
at level $i + 1$ is a subsequence, not necessarily contiguous, of the list of key-value pairs
visible at level $i$.

Formalized by `Cslib.Algorithms.Lean.SkipList.level_succ_sublist_level`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#level-succ-sublist-level).

## Keys of a valid skip list are distinct

If a skip list is valid, then the keys of the
pairs in its bottom-level abstraction, read in order, form a list without duplicates.

Formalized by `Cslib.Algorithms.Lean.SkipList.abstraction_keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#abstraction-keys-nodup).

## Keys on each skip-list level are distinct

If a skip list is valid, then for every level
index $i$ (levels are numbered from $0$ at the bottom), no key occurs twice in the list of
key-value pairs visible at level $i$.

Formalized by `Cslib.Algorithms.Lean.SkipList.level_keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#level-keys-nodup).

## One search step returns a suffix

For every search key, every level $i$ and every list
$L$ of skip-list nodes, advancing the search at level $i$ on $L$ returns a suffix of $L$.

Formalized by `Cslib.Algorithms.Lean.SkipList.advanceAtLevel_suffix`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#advance-at-level-suffix).

## The search window is a suffix of the bottom level

For every skip list and every key $k$,
the search window for $k$ is a suffix of the list of the skip list's bottom-level nodes.

Formalized by `Cslib.Algorithms.Lean.SkipList.searchWindow_suffix`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#search-window-suffix).

## Skip-list search agrees with bottom-level lookup

For every skip list and every key $k$,
the top-down skip-list lookup of $k$ returns the same result as looking up $k$ in the
bottom-level abstraction, the list of key-value pairs of all stored nodes in order: the value of
the first pair with key $k$, or no value if there is none.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup_eq_abstraction`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup-eq-abstraction).

## Insertion preserves skip-list validity

Let $\alpha$ be a linearly ordered type and
$\beta$ a type. If a skip list with keys in $\alpha$ and values in $\beta$ is valid, then for every
key $k \in \alpha$, value $v \in \beta$ and requested height $h \in \mathbb{N}$ (including
$h = 0$), inserting $k$ with value $v$ and requested height $h$ yields a valid skip list. This
covers both a new key and a key already present, whose value is replaced.

Formalized by `Cslib.Algorithms.Lean.SkipList.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#valid-insert).

## Lookup after insertion returns the inserted value

For every skip list, key $k$, value
$v$ and requested height $h$, looking up $k$ after inserting $k$ with value $v$ and requested
height $h$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup-insert).

## Skip-list insertion does not change lookup of other keys

Let $\alpha$ be a linearly
ordered type. For every skip list $S$ with keys in $\alpha$ and values in $\beta$, all keys $k$
and $k'$ in $\alpha$ with $k' \ne k$, every value $v \in \beta$ and every requested height
$h \in \mathbb{N}$, looking up $k'$ in the skip list obtained by inserting $k$ with value $v$ and
requested height $h$ into $S$ gives the same result as looking up $k'$ in $S$.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup-insert-of-ne).

## Reinsertion preserves tower height

Let $S$ be a valid skip list in which the key $k$
has stored tower height $h_0$. Then after inserting $k$ into $S$ with any value and any
requested height, the stored tower height of $k$ is still $h_0$.

Formalized by `Cslib.Algorithms.Lean.SkipList.heightOf_insert_of_present`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#height-of-insert-of-present).

## Height of a newly inserted key

If a key $k$ does not occur in a skip list $S$, then
after inserting $k$ into $S$ with any value and requested height $h$, the stored tower height
of $k$ is $\max(1, h)$.

Formalized by `Cslib.Algorithms.Lean.SkipList.heightOf_insert_of_absent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#height-of-insert-of-absent).

## Skip-list erasure

Given a key $k$ from a linearly ordered type and a skip list $S$, the
erasure of $k$ from $S$ is the skip list obtained by scanning the entries of $S$ in order: an
entry whose key is less than $k$ is kept and the scan continues; at the first entry whose key is
greater than $k$ the scan stops, and that entry and all later ones are kept; at the first entry
whose key equals $k$ that entry is removed, the scan stops, and all later entries are kept. Every
kept entry keeps its key, value and tower height.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase).

## Erasing from the empty skip list

For every key $k$, erasing $k$ from the empty skip list
gives the empty skip list.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase-empty).

## Erasing a key below the first entry

Let $e$ be a skip-list entry and $L$ a list of
entries. If a key $k$ is less than the key of $e$, then erasing $k$ from the skip list with entry
list $e$ followed by $L$ leaves the entry list $e$ followed by $L$ unchanged.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase_cons_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase-cons-of-lt).

## Erasing past a smaller first entry

Let $e$ be a skip-list entry and $L$ a list of
entries. If the key of $e$ is less than a key $k$, then erasing $k$ from the skip list with entry
list $e$ followed by $L$ gives the entry list consisting of $e$ followed by the entry list obtained
by erasing $k$ from the skip list with entry list $L$.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase_cons_of_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase-cons-of-gt).

## Erasing the key of the first entry

Let $e$ be a skip-list entry and $L$ a list of
entries, and consider the skip list whose entry list is $e$ followed by $L$. If a key $k$ equals
the key of $e$, then erasing $k$ from this skip list leaves the entry list $L$.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase_cons_of_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase-cons-of-eq).

## Erasure on a valid skip list filters out the key

If $S$ is a valid skip list and $k$ is
a key, then the entry list of the skip list obtained by erasing $k$ from $S$ is the entry list of
$S$ with every entry whose key equals $k$ removed, the remaining entries kept in their order.

Formalized by `Cslib.Algorithms.Lean.SkipList.erase_entries_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#erase-entries-filter).

## Erasure preserves skip-list validity

Let $L$ be a valid skip list, that is, its keys are
strictly increasing and every stored tower has positive height. For every key $k$, the skip list
obtained from $L$ by erasing $k$ is again valid.

Formalized by `Cslib.Algorithms.Lean.SkipList.valid_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#valid-erase).

## Erased keys are absent from a skip list

Let $L$ be a valid skip list, that is, its keys
are strictly increasing and every stored tower has positive height. For every key $k$, looking
up $k$ in the skip list obtained from $L$ by erasing $k$ returns no value.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup-erase).

## Erasure preserves lookups of other keys

If $S$ is a valid skip list and $k$, $k'$ are
keys with $k' \ne k$, then looking up $k'$ in the skip list obtained by erasing $k$ from $S$ gives
the same result as looking up $k'$ in $S$: the same value, or no value in both.

Formalized by `Cslib.Algorithms.Lean.SkipList.lookup_erase_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#lookup-erase-of-ne).

## The erased key has no stored height

If $S$ is a valid skip list and $k$ is a key, then
after erasing $k$ from $S$ the key $k$ has no stored tower height.

Formalized by `Cslib.Algorithms.Lean.SkipList.heightOf_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#height-of-erase).

## Erasure preserves the heights of other keys

If $S$ is a valid skip list and $k$, $k'$
are keys with $k' \ne k$, then the stored tower height of $k'$ in the skip list obtained by
erasing $k$ from $S$ is the same as in $S$; in particular $k'$ has no stored height in one exactly
when it has none in the other.

Formalized by `Cslib.Algorithms.Lean.SkipList.heightOf_erase_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#height-of-erase-of-ne).

## Erasure removes the key from every level

If $S$ is a valid skip list, $k$ is a key and
$i$ is a natural number, then the level-$i$ list of key-value pairs (levels numbered from $0$) of
the skip list obtained by erasing $k$ from $S$ is the level-$i$ list of $S$ with every pair whose
key equals $k$ removed, the remaining pairs kept in their order.

Formalized by `Cslib.Algorithms.Lean.SkipList.level_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SkipList/Erase.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html#level-erase).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Skip list](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/skip-list/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/skip-list)
