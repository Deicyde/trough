---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Trie, Cslib.Algorithms.Lean.Trie.empty, Cslib.Algorithms.Lean.Trie.lookup, Cslib.Algorithms.Lean.Trie.insert, Cslib.Algorithms.Lean.Trie.Valid, Cslib.Algorithms.Lean.Trie.entries, Cslib.Algorithms.Lean.Trie.lookup_empty, Cslib.Algorithms.Lean.Trie.lookup_insert_same
statement: formalized
proof: formalized
---

# Trie

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html).

## Trie

A trie with keys that are lists over $\alpha$ and values in $\beta$ is a node
consisting of an optional value in $\beta$ and a finite list of children, each child being a pair
of a letter in $\alpha$ and a trie. The letters labelling the children need not be distinct.

Formalized by `Cslib.Algorithms.Lean.Trie`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#trie).

## Empty trie

The empty trie is the trie consisting of a single root node that stores no
value and has no children, so it contains no key-value entries.

Formalized by `Cslib.Algorithms.Lean.Trie.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#empty).

## Trie lookup

The lookup of a key (a list over $\alpha$) in a trie returns an optional
value in $\beta$, by recursion on the key. For the empty key it is the optional value stored at
the root. For a key with first letter $a$ followed by the key $k$, it fails if no child of the
root is labelled $a$, and otherwise it is the lookup of $k$ in the first child labelled $a$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup).

## Trie insertion

Inserting a value $v$ at a key $k$ (a list of letters) in a trie stores $v$
at the node reached by following $k$ from the root, replacing any value stored there. Along the
way, a missing child is created as an empty trie and appended after its siblings, an existing
child is updated in place, and all other values and children are unchanged.

Formalized by `Cslib.Algorithms.Lean.Trie.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#insert).

## Valid trie

Validity of tries is defined inductively: a trie node with optional value $v$
and child list $c$ is valid when the letters labelling the children in $c$ are pairwise distinct
and every child trie in $c$ is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#valid).

## Entries of a trie

The entries of a trie are the list of its key-value pairs, where a key
is a list of letters. If the root stores a value $v$, the list begins with the pair consisting of
the empty key and $v$; it continues, for each child in the stored sibling order, with the entries
$(k, w)$ of that child, in order, each rewritten as $(a k, w)$, where $a$ is the letter labelling
the child and $a k$ is the key $k$ with $a$ prepended.

Formalized by `Cslib.Algorithms.Lean.Trie.entries`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#entries).

## Lookup in the empty trie

For every key $k$, looking up $k$ in the empty trie returns no
value.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-empty).

## Lookup after insertion in a trie

Let $\alpha$ be a type with decidable equality. For
every trie $T$ with keys that are lists over $\alpha$ and values in $\beta$, every key $k$ and
every value $v \in \beta$, looking up $k$ in the trie obtained from $T$ by inserting $v$ at $k$
returns $v$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_insert_same`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-insert-same).

## Trie insertion leaves other keys unchanged

For every trie $T$, all keys $k \ne k'$ and
every value $v$, looking up $k$ in the trie obtained by inserting $v$ at $k'$ in $T$ gives the
same result as looking up $k$ in $T$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-insert-of-ne).

## Valid trie nodes have distinct child keys

If a trie node with optional value $v$ and
child list $c$ is valid, then the letters labelling the children in $c$ are pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid.nodup_child_keys`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#nodup-child-keys).

## Validity of the empty trie

The empty trie is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid.empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#empty-2).

## Insertion preserves trie validity

If a trie $T$ is valid, then for every key $k$ (a list
of letters) and every value $v$, the trie obtained by inserting $v$ at $k$ in $T$ is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid.insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#insert-2).

## Trie lookup agrees with the entries

For every valid trie $T$, every key $k$ and every
value $v$, looking up $k$ in $T$ returns $v$ if and only if $(k, v)$ is one of the entries of
$T$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_eq_some_iff_mem_entries`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-eq-some-iff-mem-entries).

## Lookup equivalence of tries

Two tries $T$ and $T'$ are lookup-equivalent when, for every
key $k$, looking up $k$ in $T$ gives the same result as looking up $k$ in $T'$.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-equiv).

## Reflexivity of trie lookup equivalence

Every trie is lookup-equivalent to itself.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv.refl`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#refl).

## Symmetry of trie lookup equivalence

If a trie $T$ is lookup-equivalent to a trie $T'$,
then $T'$ is lookup-equivalent to $T$.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv.symm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#symm).

## Transitivity of trie lookup equivalence

If a trie $T_1$ is lookup-equivalent to a trie
$T_2$ and $T_2$ is lookup-equivalent to a trie $T_3$, then $T_1$ is lookup-equivalent to $T_3$.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv.trans`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#trans).

## Lookup-equivalent valid tries have the same entries

Let $T$ and $T'$ be valid tries
with keys that are lists over $\alpha$ and values in $\beta$, and suppose $T$ and $T'$ are
lookup-equivalent. Then for every key $k$ and every value $v \in \beta$, the pair $(k, v)$
occurs in the entry list of $T$ if and only if it occurs in the entry list of $T'$.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv.mem_entries_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#mem-entries-iff).

## Insertions at distinct keys commute in a trie

For every trie $T$, all keys $k_1 \ne k_2$
and all values $v_1, v_2$, inserting $v_1$ at $k_1$ and then $v_2$ at $k_2$ gives a trie that is
lookup-equivalent to the one obtained by inserting $v_2$ at $k_2$ and then $v_1$ at $k_1$.

Formalized by `Cslib.Algorithms.Lean.Trie.LookupEquiv.insert_comm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#insert-comm).

## Empty trie nodes

The empty-node test is true on a trie node exactly when the node
carries no value and has no children; when deletion leaves a child in this state, the child is
removed from its parent.

Formalized by `Cslib.Algorithms.Lean.Trie.isEmptyNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#is-empty-node).

## Characterization of empty nodes

The empty-node test is true on a trie $t$ exactly when
$t$ is the node with no value and no children, that is, the empty trie.

Formalized by `Cslib.Algorithms.Lean.Trie.isEmptyNode_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#is-empty-node-eq-true-iff).

## Setting a child in a trie's child list

Let $L$ be a list of pairs $(k, c)$ of a key $k$
in $\alpha$ and a trie $c$ (the children of a trie node), let $a$ be a key and $t$ a trie, and
call $t$ empty when it carries no value and has no children. Setting the child at $a$ to $t$
in $L$ gives the following list. If no entry of $L$ has key $a$, the result is $L$ itself when
$t$ is empty, and $L$ with $(a, t)$ appended at the end otherwise. If some entry of $L$ has key
$a$, the entries before the first such entry are kept; that entry is replaced in place by
$(a, t)$, or removed when $t$ is empty; and every later entry with key $a$ is removed, while
later entries with other keys are kept in their order.

Thus the order of the surviving entries is preserved and at most one entry with key $a$
remains, even when $L$ has repeated keys. Deletion from a trie uses this operation to prune
empty nodes.

Formalized by `Cslib.Algorithms.Lean.Trie.setChild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#set-child).

## Looking up a child just set

Let $L$ be a list of letter–trie pairs, $a$ a letter and
$c$ a trie, and let $L'$ be obtained from $L$ by setting the child at $a$ to $c$ (removing the
entries at $a$ instead when $c$ has neither value nor children). Looking up $a$ in $L'$ finds
nothing when $c$ has neither value nor children, and finds $c$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_setChild_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-set-child-self).

## Setting a child leaves the other children unchanged

Let $L$ be a list of letter–trie
pairs, $c$ a trie and $a \ne b$ letters, and let $L'$ be obtained from $L$ by setting the child
at $b$ to $c$ (removing the entries at $b$ instead when $c$ has neither value nor children).
Then looking up $a$ in $L'$ gives the same result as looking up $a$ in $L$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_setChild_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-set-child-of-ne).

## Setting a child preserves the child-list part of validity

Let $L$ be a list of
letter–trie pairs whose letters are pairwise distinct and whose tries are all valid, let $c$
be a valid trie and $a$ a letter. Then the list obtained from $L$ by setting the child at $a$
to $c$ (removing the entries at $a$ instead when $c$ has neither value nor children) again has
pairwise distinct letters, and every trie in it is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.setChild_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#set-child-valid).

## Setting a child preserves validity

Let a trie node with value $v$ and child list $L$ be
valid, let $c$ be a valid trie and $a$ a letter. Then the node with value $v$ whose child list
is obtained from $L$ by setting the child at $a$ to $c$ (removing the entries at $a$ instead
when $c$ has neither value nor children) is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid.setChild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#set-child-2).

## Deletion from a trie

Deleting a key $k$ (a list of letters) from a trie $t$ works by
recursion on $k$. If $k$ is empty, the root of $t$ loses its value and keeps its children. If
$k$ consists of a first letter $a$ followed by a key $k'$ and the root of $t$ has no child at
$a$, then $t$ is unchanged. Otherwise $k'$ is deleted from the first child at $a$. If the
result has neither value nor children, every entry at $a$ is removed from the root's child
list; if not, the first entry at $a$ is replaced by the result and any later entries at $a$
are removed. The root's value and the other children, in their order, are kept.

Deleting an absent key leaves every lookup unchanged.

Formalized by `Cslib.Algorithms.Lean.Trie.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#delete).

## A deleted key is absent

For every trie $t$ and every key $k$, looking up $k$ in the
trie obtained from $t$ by deleting $k$ finds no value.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_delete_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-delete-self).

## Deletion does not affect other keys

For every trie $t$ and all keys $k \ne k'$, looking
up $k$ in the trie obtained from $t$ by deleting $k'$ gives the same result as looking up $k$
in $t$.

Formalized by `Cslib.Algorithms.Lean.Trie.lookup_delete_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#lookup-delete-of-ne).

## Deletion preserves trie validity

If a trie $t$ is valid, that is, every node has distinct
child keys and valid child tries, then for every key $k$ the trie obtained from $t$ by deleting
$k$ is valid.

Formalized by `Cslib.Algorithms.Lean.Trie.Valid.delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/Trie/Delete.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html#delete-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trie](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/trie)
