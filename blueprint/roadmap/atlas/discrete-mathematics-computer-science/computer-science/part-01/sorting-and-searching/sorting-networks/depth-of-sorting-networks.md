---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE.append, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_of_not_mem, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_congr, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE.append_disjoint, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_swap, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levelsTab
statement: formalized
proof: formalized
---

# Depth of sorting networks

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html).

## Levels

## Comparator levels under earliest scheduling

Given a list of comparators on
$\mathbb{N}$-indexed wires, each a pair $(i, j)$ of wires, and a starting level $\ell(x)$ for
every wire $x$, process the comparators in order, keeping a current level for each wire, initially
$\ell$: a comparator $(i, j)$ whose wires currently have levels $a$ and $b$ sets the current levels
of both wires $i$ and $j$ to $\max(a, b) + 1$ and leaves every other level unchanged. The result
is the level of each wire after all the comparators, that is, when each comparator runs as early
as possible, one level after the later of its two wires.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#levels).

## Depth bound for a comparator list

A list of comparators on wires indexed by $\mathbb{N}$
has depth at most $d$ when, starting with every wire at level $0$ and scheduling each comparator
one level after the later of its two wires, every wire ends at level at most $d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#depth-le).

## Depth of sequential composition of comparator lists

If a list $p$ of comparators on wires
indexed by $\mathbb{N}$ has depth at most $d$ and a list $q$ of comparators has depth at most
$e$, then the concatenation of $p$ followed by $q$ has depth at most $d + e$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE.append`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#append).

## Comparators inside a block leave levels outside it unchanged

Let $ps$ be a list of
comparators all of whose wires lie in $[a, b)$. Then for all initial levels
$\ell : \mathbb{N} \to \mathbb{N}$ and every wire $x$ with $x < a$ or $b \le x$, the level of $x$
after $ps$ starting from $\ell$ is $\ell(x)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#levels-of-not-mem).

## Levels inside a block depend only on initial levels inside it

Let $ps$ be a list of
comparators all of whose wires lie in $[a, b)$, and let $\ell, \ell' : \mathbb{N} \to \mathbb{N}$
be initial levels that agree on every wire in $[a, b)$. Then for every wire $x$ in $[a, b)$, the
level of $x$ after $ps$ starting from $\ell$ equals the level of $x$ after $ps$ starting from
$\ell'$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_congr`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#levels-congr).

## Parallel composition of comparator lists on adjacent blocks

Let $a$, $m$, $b$, $d$ be
natural numbers, and let $p$ and $q$ be lists of comparators on wires indexed by $\mathbb{N}$, where
every comparator of $p$ joins two wires in $[a, m)$ and every comparator of $q$ joins two wires in
$[m, b)$. If $p$ and $q$ both have depth at most $d$, then the concatenation of $p$ followed by
$q$ also has depth at most $d$: the two lists run in parallel.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.DepthLE.append_disjoint`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#append-disjoint).

## Swapping the wires of every comparator does not change levels

For every list $ps$ of
comparators and all initial levels $\ell : \mathbb{N} \to \mathbb{N}$, the levels after the list
obtained from $ps$ by replacing each comparator $(i, j)$ with $(j, i)$, starting from $\ell$, equal
the levels after $ps$ starting from $\ell$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levels_swap`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#levels-swap).

## Tabulated levels

Given a list $ps$ of comparators and a table $t$ of natural numbers
$t_0, \dots, t_{N-1}$, the tabulated levels are computed by processing the comparators in order:
a comparator $(i, j)$ sets both entries $t_i$ and $t_j$ to $\max(t_i, t_j) + 1$, where an entry
outside the table reads as $0$ and a write outside the table is ignored.

Evaluating the levels directly re-reads both wires' earlier levels at every comparator, a cost
exponential in the depth; this computes the same values in time proportional to the network size
times $N$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.levelsTab`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#levels-tab).

## Tabulated levels agree with levels

Let $t$ be a list of natural numbers of length $N$ and
let $ps$ be a list of comparators all of whose wires lie in $[0, N)$. Extend $t$ to all wires by
setting $t_y = 0$ for $y \ge N$. Then for every wire $x$, the entry at position $x$ of the
tabulated levels of $ps$ starting from the table $t$ (read as $0$ when $x \ge N$) equals the level
of wire $x$ after $ps$, starting from the initial levels $y \mapsto t_y$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.getD_levelsTab`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#get-d-levels-tab).

## The half-cleaner has depth at most $1$

For all natural numbers $m$ and $b$, the
half-cleaner on the block of $2m$ wires $b, \dots, b + 2m - 1$ has depth at most $1$: its
comparators join pairwise disjoint pairs of wires.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.depthLE_halfCleaner`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#depth-le-half-cleaner).

## The bitonic merger has depth at most $k$

For all natural numbers $k$ and $b$, the bitonic
merger on the block of $2^k$ wires $b, b + 1, \dots, b + 2^k - 1$ has depth at most $k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.depthLE_bitonicMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#depth-le-bitonic-merge).

## Depth of the bitonic sorter's comparator list

For all natural numbers $k$ and $b$, the
comparator list of Batcher's bitonic sorter on the block of $2^k$ wires
$b, b + 1, \dots, b + 2^k - 1$ has depth at most $d$ for some natural number $d$ with
$2d \le k(k+1)$; that is, its depth is at most $k(k+1)/2$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.depthLE_bitonicSortN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#depth-le-bitonic-sort-n).

## Influence sets of wires

Given a list $ps$ of comparators on wires indexed by $\mathbb{N}$
and an assignment $S$ of a finite set of natural numbers to each wire, the influence sets after
$ps$ are computed by processing the comparators in order: a comparator $(i, j)$ replaces the
current sets of both wires $i$ and $j$ by their union, and leaves the sets of all other wires
unchanged. Starting from $S(x) = \{x\}$, the set of a wire tracks the inputs it can depend on.

Evaluating this definition directly re-reads both wires' earlier sets at every comparator, a cost
exponential in the depth, so it serves as a proof device only.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.influence`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#influence).

## Influence sets grow at most exponentially with the level

Let $p$ be a list of comparators
on wires indexed by $\mathbb{N}$. Let $S$ assign to each wire a finite set of natural numbers and
let $\ell$ assign to each wire a natural number, such that $|S(x)| \le 2^{\ell(x)}$ for every
wire $x$. For each wire $x$, let $L(x)$ be the level of $x$ after $p$ starting from the levels
$\ell$. Then for every wire $x$, the influence set of $x$ after $p$ starting from $S$ has at most
$2^{L(x)}$ elements.

In particular, a wire at level $l$ depends on at most $2^l$ inputs.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.card_influence_le`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#card-influence-le).

## Outputs depend only on the influence set

Let $f_0, g_0 : \mathbb{N} \to \alpha$ be two
inputs with values in a linear order $\alpha$, let $S$ assign to each wire $x$ a finite set $S(x)$
of input positions, and let $F, G : \mathbb{N} \to \alpha$ be wire values such that for every wire
$x$, if $f_0$ and $g_0$ agree on $S(x)$, then $F(x) = G(x)$. Then for every list of comparators
and every wire $x$, if $f_0$ and $g_0$ agree on the influence set of $x$ obtained from $S$ through
the comparators, running the comparators on $F$ and on $G$ gives the same value at wire $x$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_congr_influence`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#run-n-congr-influence).

## Comparators inside $(0, n)$ keep a false value inside $(0, n)$

Let $n$ be a natural
number, let $p$ be a list of comparators, each joining two wires in $[0, n)$, and let $f$ assign a
Boolean value to each wire in $\mathbb{N}$. If $f(y)$ is false for some $y < n$, then after
running $p$ on $f$ some wire $y < n$ carries the value false.

The smaller value moves to the first wire of each comparator.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.exists_false_runN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#exists-false-run-n).

## Sorting comparator lists on $n$ wires have depth at least $\log_2 n$

Let $ps$ be a list
of comparators on wires indexed by $\mathbb{N}$, all of whose wires lie in $[0, n)$, and let $d$
be a natural number. Suppose that for every Boolean input $v$ on the wires $0, \dots, n - 1$,
extended by $\mathrm{false}$ to the wires $\ge n$, the output $w$ of $ps$ satisfies
$w_i \le w_j$ whenever $i \le j < n$ (with $\mathrm{false} < \mathrm{true}$). If $ps$ has depth at
most $d$, then $n \le 2^d$.

The smallest output depends on every input, and a wire at level $d$ depends on at most $2^d$
inputs.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.le_two_pow_of_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#le-two-pow-of-sorts).

## The bitonic sorting comparator list on $2^k$ wires has depth at least $k$

For all natural
numbers $k$ and $d$, if the comparator list of Batcher's bitonic sorter on the wires
$0, \dots, 2^k - 1$ has depth at most $d$, then $k \le d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.le_of_depthLE_bitonicSortN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#le-of-depth-le-bitonic-sort-n).

## Comparator list of a network

The comparators of a network on $n$ wires, in order, with
each comparator $(i, j)$ written as the pair of natural numbers $(i, j)$, forgetting that
$i, j < n$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Network.toPairs`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#to-pairs).

## Depth bound for a comparator network

A comparator network on $n$ wires has depth at most
$d$ when its list of comparators, read as pairs of wire numbers in $\mathbb{N}$, has depth at
most $d$: starting with every wire at level $0$ and scheduling each comparator one level after the
later of its two wires, every wire ends at level at most $d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Network.DepthLE`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#depth-le-2).

## Every sorting network on $n$ wires has depth at least $\log_2 n$

Let $C$ be a comparator
network on $n$ wires and $d$ a natural number. If $C$ sorts every Boolean input (its output is
monotone in the wire order for every input in $\{\mathrm{false}, \mathrm{true}\}^n$, with
$\mathrm{false} < \mathrm{true}$) and $C$ has depth at most $d$, then $n \le 2^d$.

By the 0-1 principle, the hypothesis implies that $C$ sorts every input over every linear order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Network.le_two_pow_of_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#le-two-pow-of-sorts-2).

## Batcher's bitonic sorting network has depth at most $k(k+1)/2$

For every natural number
$k$, Batcher's bitonic sorting network on $2^k$ wires has depth at most $d$ for some natural
number $d$ with $2d \le k(k+1)$; that is, its depth is at most $k(k+1)/2$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.bitonicSorter_depthLE`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#bitonic-sorter-depth-le).

## Batcher's bitonic sorter on $2^k$ wires has depth at least $k$

For all natural numbers
$k$ and $d$, if Batcher's bitonic sorting network on $2^k$ wires has depth at most $d$, then
$k \le d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.le_of_bitonicSorter_depthLE`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Depth.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html#le-of-bitonic-sorter-depth-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Depth of sorting networks](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/sorting-networks/depth-of-sorting-networks)
