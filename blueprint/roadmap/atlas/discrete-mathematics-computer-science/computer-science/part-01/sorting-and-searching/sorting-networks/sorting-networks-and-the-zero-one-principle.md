---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SortingNetworks.Network, Cslib.Algorithms.Lean.SortingNetworks.comparator, Cslib.Algorithms.Lean.SortingNetworks.run, Cslib.Algorithms.Lean.SortingNetworks.Sorts, Cslib.Algorithms.Lean.SortingNetworks.comparator_comp, Cslib.Algorithms.Lean.SortingNetworks.run_comp, Cslib.Algorithms.Lean.SortingNetworks.comparator_perm, Cslib.Algorithms.Lean.SortingNetworks.run_perm
statement: formalized
proof: formalized
---

# Sorting networks and the zero-one principle

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html).

## Comparator network

A comparator network on $n$ wires is a finite list of pairs $(i, j)$
of wires $i, j \in \{0, \dots, n - 1\}$, each pair standing for the comparator $(i, j)$; the
comparators are applied in list order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Network`, an abbreviation declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#network).

## Comparator

Let $\alpha$ be a linear order, let $n$ be a natural number, and let $v$
assign a value $v(k) \in \alpha$ to each wire $k \in \{0, \dots, n - 1\}$. For wires $i$ and $j$,
the comparator $(i, j)$ sends $v$ to the assignment that has $\min(v(i), v(j))$ on wire $i$,
$\max(v(i), v(j))$ on wire $j$ when $j \ne i$, and $v(k)$ on every other wire $k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.comparator`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#comparator).

## Running a comparator network

Let $\alpha$ be a linear order. The output of a comparator
network on an assignment $v$ of a value in $\alpha$ to each of its $n$ wires is obtained by
starting from $v$ and applying the comparators of the network one after another, in list
order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.run`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#run).

## Networks that sort

A comparator network on $n$ wires sorts inputs over a linearly
ordered type $\alpha$ if, for every input $v$ assigning a value in $\alpha$ to each wire, the
output of running the network on $v$ is monotone in the wire order: for all wires $i \le j$, the
output value on wire $i$ is at most the output value on wire $j$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Sorts`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts).

## Comparators commute with monotone maps

Let $\alpha$ and $\beta$ be linear orders, let
$f : \alpha \to \beta$ be monotone, and let $n$ be a natural number. For all wires
$i, j \in \{0, \dots, n - 1\}$ and every assignment $v$ of a value in $\alpha$ to each wire, the
comparator $(i, j)$ applied to $f \circ v$ gives $f \circ w$, where $w$ is the output of the
comparator $(i, j)$ on $v$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.comparator_comp`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#comparator-comp).

## Networks commute with monotone maps

Let $\alpha$ and $\beta$ be linear orders and let
$f : \alpha \to \beta$ be monotone. For every comparator network on $n$ wires and every assignment
$v$ of a value in $\alpha$ to each wire, the output of the network on $f \circ v$ is $f \circ w$,
where $w$ is the output of the network on $v$.

## Sources

- CLRS, second edition, Lemma 27.1.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.run_comp`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#run-comp).

## A comparator permutes its inputs

Let $\alpha$ be a linear order and let $n$ be a natural
number. For all wires $i, j \in \{0, \dots, n - 1\}$ and every assignment $v$ of a value in
$\alpha$ to each wire, there is a permutation $\sigma$ of the wires such that the output of the
comparator $(i, j)$ on $v$ is $v \circ \sigma$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.comparator_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#comparator-perm).

## The output of a comparator network is a permutation of its input

Let $\alpha$ be a linear
order. For every comparator network on $n$ wires and every assignment $v$ of a value in $\alpha$
to each wire, there is a permutation $\sigma$ of the wires such that the output of the network
on $v$ is $v \circ \sigma$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.run_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#run-perm).

## The 0-1 principle

**The 0-1 principle** (CLRS Theorem 27.2): a network that sorts every Boolean input sorts
every input over every linear order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sorts_of_sorts_bool`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-of-sorts-bool).

## Boolean sorting test

The Boolean sorting test of a comparator network on $n$ wires
returns true exactly when, for every assignment $v$ of a Boolean value to each wire, the output
$w$ of the network on $v$ satisfies $w(i) \le w(j)$ for all wires $i \le j$, where
$\mathrm{false} < \mathrm{true}$.

It is computed by running the network on all $2^n$ Boolean inputs.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sortsBool`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-bool).

## The Boolean sorting test is correct

A comparator network passes the Boolean sorting test
if and only if it sorts inputs over the Booleans, that is, for every assignment of a Boolean
value to each wire, the output of the network is monotone in the wire order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sortsBool_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-bool-eq-true-iff).

## A network that passes the Boolean sorting test sorts over every linear order

If a
comparator network on $n$ wires passes the Boolean sorting test, then for every linear order
$\alpha$ it sorts inputs over $\alpha$: for every assignment $v$ of a value in $\alpha$ to each
wire, the output of the network on $v$ is monotone in the wire order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sorts_of_sortsBool`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/ZeroOne.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-of-sorts-bool-2).

## Spread of a Boolean input

For a Boolean input $v$ on $n$ wires, the spread of $v$ is the
input with natural-number values whose value on wire $i < n$ is $n + i$ if $v(i)$ is true and $i$
if $v(i)$ is false.

The values of the spread are pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.spread`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#spread).

## A Boolean input is a threshold of its spread

For every Boolean input $v$ on $n$ wires,
applying the threshold map that sends a natural number $k$ to true if $n \le k$ and to false
otherwise to the spread of $v$ gives back $v$: for every wire $i$, the spread of $v$ at $i$ is at
least $n$ exactly when $v(i)$ is true.

Since the threshold map is monotone, $v$ is a monotone image of its spread.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.decide_le_spread`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#decide-le-spread).

## Sorting distinct inputs suffices

A network that sorts every input with distinct natural
values sorts every input over every linear order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sorts_of_sorts_injective`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-of-sorts-injective).

## Rank among the values of an input

For a map $w$ from $\{0, \dots, n-1\}$ to the natural
numbers and an index $i < n$, the rank of $w(i)$ among the values of $w$ is the number of indices
$j < n$ with $w(j) < w(i)$. It is less than $n$, so it is again an index in $\{0, \dots, n-1\}$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.rank`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#rank).

## The ranking permutation

For an injective map $w$ from $\{0, \dots, n-1\}$ to the natural
numbers, the ranking permutation of $w$ is the permutation of $\{0, \dots, n-1\}$ that sends each
$i$ to the rank of $w(i)$ among the values of $w$, that is, to the number of indices $j$ with
$w(j) < w(i)$. Since $w$ is injective, this map is a bijection.

The ranking permutation has the same relative order as $w$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.rankPerm`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#rank-perm).

## The permutation principle

A comparator network on $n$ wires that sorts each of the $n!$
permutations $\sigma$ of $\{0, \dots, n-1\}$, viewed as the input whose value on wire $i$ is
$\sigma(i)$, sorts every input over every linear order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.sorts_of_sorts_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Permutations.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html#sorts-of-sorts-perm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sorting networks and the zero-one principle](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/sorting-networks/sorting-networks-and-the-zero-one-principle)
