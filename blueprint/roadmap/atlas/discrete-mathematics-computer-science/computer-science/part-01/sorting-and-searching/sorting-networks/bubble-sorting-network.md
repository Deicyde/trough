---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SortingNetworks.Bubble.adjacent, Cslib.Algorithms.Lean.SortingNetworks.Bubble.pass, Cslib.Algorithms.Lean.SortingNetworks.Bubble.passes, Cslib.Algorithms.Lean.SortingNetworks.Bubble.bubble, Cslib.Algorithms.Lean.SortingNetworks.Bubble.pass_spec, Cslib.Algorithms.Lean.SortingNetworks.Bubble.Settled, Cslib.Algorithms.Lean.SortingNetworks.Bubble.bubble_sorts, Cslib.Algorithms.Lean.SortingNetworks.Bubble.length_pass
statement: formalized
proof: formalized
---

# Bubble sorting network

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html).

## Adjacent comparator

For $n$ wires and an index $i$, this is the comparator on
wires $i$ and $i + 1$ when $i + 1 < n$, and nothing when wire $i + 1$ does not exist.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.adjacent`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#adjacent).

## Bubble pass

On $n$ wires, the bubble pass ending at wire $m$ is the comparator
network $(0, 1), (1, 2), \ldots, (m - 1, m)$, applied in this order, where a comparator
$(i, i + 1)$ is left out when wire $i + 1$ does not exist (that is, when $i + 1 \ge n$).

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.pass`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#pass).

## Successive bubble passes

On $n$ wires and for a number $m$, this is the comparator
network obtained by concatenating the bubble passes ending at wires $m - 1, m - 2, \ldots, 0$,
in this order; for $m = 0$ it is empty.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.passes`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#passes).

## Bubble sorting network

The bubble sorting network on $n$ wires is the comparator
network obtained by concatenating the bubble passes ending at wires $n - 1, n - 2, \ldots, 0$,
in this order, where the bubble pass ending at wire $k$ consists of the comparators
$(0, 1), (1, 2), \ldots, (k - 1, k)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.bubble`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#bubble).

## Effect of one bubble pass

Let $w$ be an input on $n$ wires with values in a linearly
ordered type, let $m < n$, and let $w'$ be the output of the bubble pass ending at wire $m$
(the comparators $(0, 1), \ldots, (m - 1, m)$) run on $w$. Then $w'_i = w_i$ for every wire
$i > m$; $w'_i \le w'_m$ for every wire $i \le m$; and for every wire $i \le m$ there is a wire
$j \le m$ with $w'_i = w_j$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.pass_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#pass-spec).

## Settled top wires

Let $w$ assign to each of $n$ wires a value in a linearly ordered
type, and let $m$ be a natural number. Then $w$ is settled from $m$ when $w_i \le w_j$ for all
wires $m \le i \le j$ (the wires $m, \ldots, n - 1$ are sorted) and $w_i \le w_j$ for all
wires $i < m \le j$ (they hold the largest values). This is the invariant before the bubble
pass ending at wire $m - 1$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.Settled`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#settled).

## The bubble network sorts

**The bubble network sorts** every input over every linear order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.bubble_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#bubble-sorts).

## Size of a bubble pass

On $n$ wires, for every $m < n$ the bubble pass ending at wire
$m$ has exactly $m$ comparators.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.length_pass`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#length-pass).

## Size of the bubble sorting network

For every $n$, the bubble sorting network on $n$
wires has $n(n - 1)/2$ comparators: twice its number of comparators is $n(n - 1)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bubble.length_bubble`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bubble.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html#length-bubble).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bubble sorting network](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bubble-sorting-network)
