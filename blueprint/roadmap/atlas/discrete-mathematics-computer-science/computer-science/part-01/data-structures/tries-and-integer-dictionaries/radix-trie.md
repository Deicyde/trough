---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.RadixTrie, Cslib.Algorithms.Lean.RadixTrie.empty, Cslib.Algorithms.Lean.RadixTrie.commonPrefix, Cslib.Algorithms.Lean.RadixTrie.commonPrefix_self, Cslib.Algorithms.Lean.RadixTrie.commonPrefix_append_append, Cslib.Algorithms.Lean.RadixTrie.commonPrefix_spec, Cslib.Algorithms.Lean.RadixTrie.append_drop_commonPrefix_left, Cslib.Algorithms.Lean.RadixTrie.commonPrefix_drop_spec
statement: formalized
proof: formalized
---

# Radix trie

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html).

## Radix Trie

## Radix trie

For types $\alpha$ and $\beta$, a radix trie with keys that are lists over
$\alpha$ and values in $\beta$ is a node made of an optional value in $\beta$ and a finite list of
child edges, each a pair of a label, which is a list over $\alpha$, and a radix trie (the
subtree at the end of the edge).

No invariant is built into the type: labels may be empty and sibling labels may share first
symbols. The radix-trie invariant is imposed separately.

Formalized by `Cslib.Algorithms.Lean.RadixTrie`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#radix-trie).

## Empty radix trie

The empty radix trie is the single node that stores no value and has no
child edges; it contains no key-value entries.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#empty).

## Longest common prefix

For lists $s$ and $t$ over a type with decidable equality, the
longest common prefix of $s$ and $t$ is defined by recursion: it is empty if $s$ or $t$ is
empty; if $s$ has first element $a$ and rest $s'$, and $t$ has first element $b$ and rest $t'$,
it is $a$ followed by the longest common prefix of $s'$ and $t'$ when $a = b$, and empty when
$a \ne b$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix).

## Longest common prefix of a list with itself

For every list $s$ over a type with decidable
equality, the longest common prefix of $s$ and $s$ is $s$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix-self).

## A shared prefix factors out of the longest common prefix

Write $uv$ for the list $u$
followed by the list $v$. For lists $p$, $s$ and $t$ over a type with decidable equality, the
longest common prefix of $ps$ and $pt$ is $p$ followed by the longest common prefix of $s$ and
$t$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix_append_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix-append-append).

## Characterization of the longest common prefix

Let $s$ and $t$ be lists over a type with
decidable equality, with longest common prefix $p$. Then there are lists $s'$ and $t'$ such that
$s$ is $p$ followed by $s'$, $t$ is $p$ followed by $t'$, and either $s'$ is empty, or $t'$ is
empty, or $s'$ and $t'$ are both nonempty with different first elements.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix-spec).

## A list is its common prefix with another list followed by the rest

Let $s$ and $t$ be
lists over a type with decidable equality, and let $p$ be the longest common prefix of $s$ and
$t$. Then $s$ is $p$ followed by the list obtained by dropping the first $|p|$ elements of $s$,
where $|p|$ is the length of $p$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.append_drop_commonPrefix_left`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#append-drop-common-prefix-left).

## Longest common prefix in terms of dropped remainders

Let $s$ and $t$ be lists over a type
with decidable equality, let $p$ be their longest common prefix, of length $n$, and let $s'$ and
$t'$ be the lists obtained from $s$ and $t$ by dropping their first $n$ elements. Then $s$ is $p$
followed by $s'$, $t$ is $p$ followed by $t'$, and either $s'$ is empty, or $t'$ is empty, or
$s'$ and $t'$ are both nonempty with different first elements.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix_drop_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix-drop-spec).

## When the common prefix is the second list, the first list extends it

Let $s$ and $t$ be
lists over a type with decidable equality. If the longest common prefix of $s$ and $t$ is $t$,
then $s$ is $t$ followed by the list obtained by dropping the first $|t|$ elements of $s$, where
$|t|$ is the length of $t$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.append_of_commonPrefix_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#append-of-common-prefix-eq).

## The longest common prefix of a list and its prefix

Let $s$, $t$ and $u$ be lists over a
type with decidable equality. If $s$ is $t$ followed by $u$, then the longest common prefix of
$s$ and $t$ is $t$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.commonPrefix_eq_of_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#common-prefix-eq-of-append).

## Edge search by first symbol

Given a symbol $c$ and a list of edges, each a pair of a
label (a list of symbols) and a subtree, this returns the first edge in the list whose label
starts with $c$, or nothing if no label starts with $c$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.findEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#find-edge).

## Replacing the child edge for a symbol

Given a symbol $c$, an edge $e$ (a pair of a label
and a radix trie) and a list of child edges, this operation replaces the first edge of the list
whose label starts with $c$ by $e$ and keeps all other edges in order. If no label in the list
starts with $c$, it appends $e$ at the end of the list.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.replaceEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#replace-edge).

## Radix trie lookup

Looking up a key, a list over $\alpha$, in a radix trie returns an
optional value. At a node, the empty key returns the value stored at the node, if any. A
nonempty key $k$ with first symbol $c$ goes to the first child edge whose label starts with $c$.
If there is no such edge, or its label $\ell$ is not a prefix of $k$, the lookup returns no
value; otherwise it continues in the subtree of that edge with $k$ minus its first $|\ell|$
symbols.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup).

## Radix trie lookup of a nonempty key at a node

Let $k$ be a nonempty key with first symbol
$c$, and consider a node with children $C$ (a list of edges, each a label with a subtree),
whatever value the node stores. If no edge of $C$ has a label starting with $c$, looking up $k$
at the node returns no value. Otherwise let $(\ell, T')$ be the first such edge of $C$: if the
longest common prefix of $k$ and $\ell$ is $\ell$, the lookup returns the lookup in $T'$ of the
key obtained from $k$ by dropping its first $|\ell|$ symbols, and otherwise it returns no value.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_node_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-node-cons).

## Lookup in the empty radix trie

For every key $k$, looking up $k$ in the empty radix
trie returns no value.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-empty).

## Insertion into a radix trie

Inserting a value $v$ at a key $k$ (a list of symbols) into a
radix trie works as follows. If $k$ is empty, the root's value becomes $v$. Otherwise let $c$ be
the first symbol of $k$. If no child edge of the root has a label starting with $c$, a new edge
labelled $k$ leading to a leaf storing $v$ is added after the existing edges. Otherwise take the
first such edge, with label $\ell$ and subtree $s$, let $q$ be the longest common prefix of $k$
and $\ell$, and replace that edge in place. If $k = \ell = q$, the edge keeps label $\ell$ and
leads to $s$ with its root value set to $v$. If $k = q$ but $\ell$ is longer, the edge is
labelled $q$ and leads to a new node storing $v$ whose only edge is the rest of $\ell$ leading
to $s$. If $\ell = q$ but $k$ is longer, the edge keeps label $\ell$ and leads to $s$ with $v$
inserted at the rest of $k$. If both are longer than $q$, the edge is labelled $q$ and leads to
a new node with no value and two edges: the rest of $\ell$ leading to $s$, then the rest of $k$
leading to a leaf storing $v$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#insert).

## Lookup of a key just inserted into a radix trie

For every radix trie $T$, key $k$ and
value $v$, looking up $k$ in the trie obtained from $T$ by inserting $v$ at $k$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_insert_same`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-insert-same).

## Insertion into a radix trie leaves lookups of other keys unchanged

For every radix
trie $T$, all keys $k \ne k'$ and every value $v$, looking up $k$ in the trie obtained from $T$
by inserting $v$ at $k'$ gives the same result as looking up $k$ in $T$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-insert-of-ne).

## Path-compressed root

A radix trie is path-compressed at its root when its root node stores
a value or has at least two child edges.

A value-free node with at most one child could be merged into the edge above it, which a radix
trie rules out for every node reached by an edge; the root of the whole trie has no incoming edge
and is exempt.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.RootCompact`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#root-compact).

## Valid radix trie

Validity of radix tries is defined inductively: a node is valid when every
label of its child edges is nonempty, the first symbols of the labels of its child edges are
pairwise distinct, and for each child edge the subtree at its end is valid and path-compressed at
its root (its root stores a value or has at least two child edges).

Thus every value-free node other than the root has at least two children, so no unary value-free
node remains to be merged into its parent edge.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#valid).

## The empty radix trie is valid

For all types $\alpha$ and $\beta$, the empty radix trie whose
keys are lists over $\alpha$ and whose values lie in $\beta$ is valid.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid.empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#empty-2).

## Sibling edge labels start with distinct symbols

If a radix-trie node with child edges
$(\ell_1, t_1), \dots, (\ell_n, t_n)$ is valid, then the first symbols of the labels
$\ell_1, \dots, \ell_n$ are pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid.nodup_child_heads`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#nodup-child-heads).

## Children of a valid node are path-compressed

If a radix-trie node is valid, then for each
of its child edges, the subtree at the end of that edge is path-compressed at its root: its root
stores a value or has at least two child edges.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid.rootCompact_child`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#root-compact-child).

## Insertion preserves validity of radix tries

If $t$ is a valid radix trie, then for every
key $k$ and value $v$, the trie obtained by inserting $v$ at $k$ in $t$ is valid.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid.insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#insert-2).

## Entries of a radix trie

The entries of a radix trie are its key-value pairs, listed
recursively. For a node with child edges $(\ell_1, t_1), \dots, (\ell_n, t_n)$ in stored order,
the list starts with the pair $(\varepsilon, v)$, where $\varepsilon$ is the empty key, if the
node stores a value $v$; it continues with the entries of $t_1$ with $\ell_1$ prepended to
every key, then the entries of $t_2$ with $\ell_2$ prepended, and so on up to $t_n$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.entries`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#entries).

## Stored keys of a radix trie

The stored keys of a radix trie form the list of the keys of
its entries, in the same order.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.keys`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1692](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#keys).

## Lookup agrees with the entries of a valid radix trie

For a valid radix trie $T$, every
key $k$ and every value $v$, looking up $k$ in $T$ returns $v$ if and only if the pair $(k, v)$
occurs in the list of entries of $T$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_eq_some_iff_mem_entries`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-eq-some-iff-mem-entries).

## Stored keys of a valid radix trie are the keys with a successful lookup

For a valid
radix trie $T$ and every key $k$, $k$ is a stored key of $T$ if and only if looking up $k$ in
$T$ returns some value.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.mem_keys_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 1893](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L1893). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#mem-keys-iff).

## Stored keys of a valid radix trie are distinct

If $t$ is a valid radix trie, then its
list of stored keys has no duplicates.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.Valid.keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#keys-nodup).

## Prefix search in a radix trie

For a radix trie $t$ and a pattern $p$ (a list of symbols),
prefix search returns a boolean computed as follows. If $p$ is empty, it is true exactly when
$t$ stores at least one key. Otherwise let $c$ be the first symbol of $p$ and take the first
child edge of the root whose label starts with $c$; if there is none, the answer is false. If
that edge has label $\ell$ and subtree $s$, then: when $p$ is a prefix of $\ell$, the answer is
whether $s$ stores at least one key; otherwise, when $\ell$ is a prefix of $p$, the search
continues in $s$ with $p$ minus its first $|\ell|$ symbols; otherwise the answer is false.

On valid radix tries this decides whether some stored key has $p$ as a prefix.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.hasPrefix`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#has-prefix).

## Prefix search is correct on valid radix tries

For a valid radix trie $t$ and a list $p$
of symbols, prefix search for $p$ in $t$ succeeds if and only if some stored key $k$ of $t$ has
$p$ as a prefix.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.hasPrefix_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#has-prefix-eq-true-iff).

## Radix trie built from a list of key-value pairs

The trie built from the empty list is the
empty trie, and the trie built from a list with head $(k, v)$ and tail $L$ is the trie built from
$L$ with the value $v$ inserted at the key $k$. Later pairs in the list are thus inserted first,
so on duplicate keys the head-most value wins.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.buildFrom`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#build-from).

## Every listed key is present in the built radix trie

For a list $L$ of key-value pairs, if
$(k, v)$ belongs to $L$, then looking up $k$ in the radix trie built from $L$ returns some
value.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_buildFrom_exists_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-build-from-exists-of-mem).

## Lookups in a radix trie built from a list come from the list

For every list $L$ of
key-value pairs, if looking up a key $k$ in the radix trie built from $L$ returns a value $v$,
then the pair $(k, v)$ occurs in $L$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.mem_of_lookup_buildFrom`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#mem-of-lookup-build-from).

## Keys of a radix trie built from a list

For every list $L$ of key-value pairs and every
key $k$, $k$ is a stored key of the radix trie built from $L$ if and only if the pair $(k, v)$
occurs in $L$ for some value $v$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.mem_keys_buildFrom`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#mem-keys-build-from).

## Lookup in a radix trie built from a list with distinct keys

Let $L$ be a list of
key-value pairs, whose keys are lists over $\gamma$, in which no key occurs twice. If the pair
$(k, v)$ occurs in $L$, then looking up $k$ in the radix trie built from $L$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.RadixTrie.lookup_buildFrom_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean, line 2376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/RadixTrie.lean#L2376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html#lookup-build-from-of-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radix trie](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/radix-trie)
