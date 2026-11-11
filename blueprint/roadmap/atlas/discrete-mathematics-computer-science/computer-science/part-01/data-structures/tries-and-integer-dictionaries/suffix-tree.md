---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SuffixTree.terminated, Cslib.Algorithms.Lean.SuffixTree.terminated_drop_eq_suffix_map, Cslib.Algorithms.Lean.SuffixTree.suffixEntries, Cslib.Algorithms.Lean.SuffixTree.nodup_terminated_drops, Cslib.Algorithms.Lean.SuffixTree.suffixTree, Cslib.Algorithms.Lean.SuffixTree.lookup_suffix, Cslib.Algorithms.Lean.SuffixTree.eq_drop_of_lookup_suffixTree, Cslib.Algorithms.Lean.SuffixTree.mem_suffixTree_keys
statement: formalized
proof: formalized
---

# Suffix tree

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html).

## Terminated string

For a list $s = (s_0, \dots, s_{n-1})$ over $\alpha$, the terminated
string of $s$ is the list $(\mathrm{some}\,s_0, \dots, \mathrm{some}\,s_{n-1}, \mathrm{none})$
over $\mathrm{Option}\,\alpha$: every symbol of $s$ tagged $\mathrm{some}$, followed by the
terminator $\mathrm{none}$.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.terminated`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#terminated).

## Suffixes of the terminated string

For a list $s$ over $\alpha$ and a natural number
$i \le |s|$, removing the first $i$ entries of the terminated string of $s$ gives the suffix
of $s$ starting at index $i$ with every symbol tagged $\mathrm{some}$, followed by
$\mathrm{none}$.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.terminated_drop_eq_suffix_map`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#terminated-drop-eq-suffix-map).

## Suffix entries of a string

For a list $s = (s_0, \dots, s_{n-1})$ over $\alpha$, let
$\hat s = (\mathrm{some}\,s_0, \dots, \mathrm{some}\,s_{n-1}, \mathrm{none})$ be its
terminated string. The suffix entries of $s$ are the list of pairs $(\hat s_{\ge i}, i)$ for
$i = 0, 1, \dots, n$ in increasing order, where $\hat s_{\ge i}$ is $\hat s$ with its first
$i$ entries removed: each nonempty suffix of $\hat s$ paired with its starting index.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.suffixEntries`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#suffix-entries).

## Terminated suffixes are distinct

Let $s$ be a list over $\alpha$. The lists obtained from
the terminated string of $s$ by removing its first $i$ symbols, for $i$ ranging over
$0, 1, \ldots, |s|$, are pairwise distinct.

They are distinct because their lengths differ.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.nodup_terminated_drops`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#nodup-terminated-drops).

## Suffix tree

For a list $s = (s_0, \dots, s_{n-1})$ over $\alpha$, let
$\hat s = (\mathrm{some}\,s_0, \dots, \mathrm{some}\,s_{n-1}, \mathrm{none})$ be its
terminated string over $\mathrm{Option}\,\alpha$. The suffix tree of $s$ is the radix trie
with keys over $\mathrm{Option}\,\alpha$ and natural-number values obtained from the empty
trie by inserting, for $i = n, n - 1, \dots, 0$ in this order, the suffix of $\hat s$
starting at index $i$ with value $i$.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.suffixTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#suffix-tree).

## Lookup of a suffix returns its starting index

Let $s$ be a list over $\alpha$ and $i$ a
natural number with $i \le |s|$. Looking up, in the suffix tree of $s$, the terminated string of
$s$ with its first $i$ symbols removed returns $i$.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.lookup_suffix`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#lookup-suffix).

## Lookup in the suffix tree returns starting indices

Let $s$ be a list over $\alpha$, let
$k$ be a list over $\alpha$ extended by a fresh terminator symbol, and let $i$ be a natural number.
If looking up $k$ in the suffix tree of $s$ returns $i$, then $i \le |s|$ and $k$ is the
terminated string of $s$ with its first $i$ symbols removed.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.eq_drop_of_lookup_suffixTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#eq-drop-of-lookup-suffix-tree).

## The stored keys of a suffix tree are its terminated suffixes

Let $s$ be a list over
$\alpha$. A key $k$ is stored in the suffix tree of $s$ if and only if there is a natural number
$i \le |s|$ such that $k$ is the terminated string of $s$ with its first $i$ symbols removed.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.mem_suffixTree_keys`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#mem-suffix-tree-keys).

## Stored keys of the suffix tree

For a list $s$ over $\alpha$, the stored keys of $s$ form
the list of keys stored in the suffix tree of $s$, in stored sibling order.

They are exactly the terminated suffixes. This concerns stored keys, not structural trie leaves:
a valid radix trie may carry values at internal nodes, and no leaf characterization is claimed.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.storedKeys`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#stored-keys).

## The suffix tree stores one key per suffix

For a list $s$ over $\alpha$, the list of
stored keys of the suffix tree of $s$ has length $|s| + 1$.

There is one key for each terminated suffix.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.storedKeys_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#stored-keys-length).

## A tagged pattern cannot reach past the terminator

For lists $p$ and $q$ over $\alpha$,
view their symbols in $\alpha$ extended by a fresh terminator symbol. If $p$ is a prefix of $q$
followed by the terminator, then $p$ is a prefix of $q$.

The terminator differs from every symbol of $\alpha$, so the pattern cannot reach past it.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.isPrefix_of_map_some_prefix_append_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#is-prefix-of-map-some-prefix-append-none).

## Infixes are prefixes of suffixes

For lists $s$ and $p$, $p$ is an infix (a contiguous
sublist) of $s$ if and only if there is a natural number $i$ such that $p$ is a prefix of the list
obtained from $s$ by removing its first $i$ symbols.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.isInfix_iff_exists_isPrefix_drop`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#is-infix-iff-exists-is-prefix-drop).

## Suffix-tree search finds exactly the prefixes of suffixes

For lists $s$ and $p$ over
$\alpha$, prefix search for $p$ (each symbol viewed in the alphabet extended by the terminator) in
the suffix tree of $s$ succeeds if and only if there is a natural number $i$ such that $p$ is a
prefix of the list obtained from $s$ by removing its first $i$ symbols.

Formalized by `Cslib.Algorithms.Lean.SuffixTree.hasPrefix_suffixTree_iff_exists`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#has-prefix-suffix-tree-iff-exists).

## Suffix-tree search finds exactly the infixes

For lists $s$ and $p$ over $\alpha$, prefix
search for $p$ (each symbol viewed in the alphabet extended by the terminator) in the suffix tree
of $s$ succeeds if and only if $p$ occurs in $s$ as a contiguous sublist (an infix).

Formalized by `Cslib.Algorithms.Lean.SuffixTree.hasPrefix_suffixTree_iff_isInfix`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SuffixTree.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html#has-prefix-suffix-tree-iff-is-infix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Suffix tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/suffix-tree)
