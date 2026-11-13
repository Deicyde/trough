---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SortingNetworks.Bitonic.cmp, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.Within, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_of_not_mem, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_const, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.halfCleaner, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_halfCleaner, Cslib.Algorithms.Lean.SortingNetworks.Bitonic.IsInterval
statement: formalized
proof: formalized
---

# Bitonic sorter

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html).

## Comparators on `ℕ`-indexed wires

## Comparator on natural-number-indexed wires

Let $\alpha$ be a linear order. For wires
$i, j \in \mathbb{N}$ and an assignment $f$ of values in $\alpha$ to the wires $x \in \mathbb{N}$,
the comparator $(i, j)$ applied to $f$ puts $\min(f(i), f(j))$ on wire $i$, puts
$\max(f(i), f(j))$ on wire $j$ when $j \ne i$, and leaves every other wire unchanged.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.cmp`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#cmp).

## Running a comparator network on natural-number-indexed wires

Let $\alpha$ be a
linear order. Given a list $ps$ of comparators, each a pair $(i, j)$ of natural numbers, and
an input $f : \mathbb{N} \to \alpha$ giving the value on each wire, running $ps$ on $f$
applies the comparators of $ps$ to the wire values one after another, from first to last. The
comparator $(i, j)$ puts the minimum of the values on wires $i$ and $j$ on wire $i$ and their
maximum on wire $j$, and leaves the other wires unchanged.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#run-n).

## Comparators within an interval

A list $ps$ of comparators, each a pair $(i, j)$ of
natural numbers, lies within $[l, h)$ if every comparator $(i, j)$ in $ps$ satisfies
$l \le i < h$ and $l \le j < h$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.Within`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#within).

## Locality of comparator networks

Let $\alpha$ be a linear order and let $ps$ be a list
of comparators $(i, j)$ on $\mathbb{N}$-indexed wires that all lie within $[l, h)$, that is,
$l \le i < h$ and $l \le j < h$ for every $(i, j)$ in $ps$. Then for every input
$f : \mathbb{N} \to \alpha$ and every wire $x$ with $x < l$ or $h \le x$, the value of wire $x$
after running $ps$ on $f$ is $f(x)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#run-n-of-not-mem).

## Constant blocks stay constant

Let $\alpha$ be a linear order, let $l, h \in \mathbb{N}$,
and let $c$ be a list of comparators on $\mathbb{N}$-indexed wires each of which joins two wires
$x$ with $l \le x < h$. If an input $f : \mathbb{N} \to \alpha$ takes the same value $a$ on
every wire $x$ with $l \le x < h$, then running $c$ on $f$ gives an output that also takes the
value $a$ on every such wire.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_const`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#run-n-const).

## Half-cleaner

For natural numbers $m$ and $b$, the half-cleaner on the block of wires
$[b, b + 2m)$ is the list of comparators $(b + i, b + m + i)$ for $i = 0, 1, \dots, m - 1$, in
this order: it compares wire $b + i$ with wire $b + m + i$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.halfCleaner`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#half-cleaner).

## Output of the half-cleaner

Let $\alpha$ be a linear order, let $m, b \in \mathbb{N}$, and
let $f : \mathbb{N} \to \alpha$ be an input on $\mathbb{N}$-indexed wires. Running the
half-cleaner on $[b, b + 2m)$ on $f$ puts $\min(f(b + i), f(b + m + i))$ on wire $b + i$ and
$\max(f(b + i), f(b + m + i))$ on wire $b + m + i$ for every $i < m$, and leaves the value $f(x)$
on every wire $x$ outside $[b, b + 2m)$ unchanged.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_halfCleaner`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#run-n-half-cleaner).

## Interval indicators

A sequence $s : \mathbb{N} \to \{0, 1\}$ is an interval indicator
of length $L$ if there are natural numbers $a \le e \le L$ such that for every $i < L$,
$s(i) = 1$ exactly when $a \le i < e$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.IsInterval`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#is-interval).

## Bitonic 0-1 sequences

A sequence $s : \mathbb{N} \to \{0, 1\}$ is bitonic of length $L$
if either $s$ or its complement $1 - s$ is an interval indicator of length $L$; that is, on the
positions $0, \dots, L - 1$ it has the form $0^a 1^b 0^c$ or $1^a 0^b 1^c$. Values of $s$ at
positions $i \ge L$ are unconstrained.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.IsBitonic`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#is-bitonic).

## The half-cleaner lemma

Let $m \in \mathbb{N}$ and let $s_0, s_1, \dots, s_{2m-1}$ be a
bitonic sequence of Booleans, ordered by $\mathrm{false} < \mathrm{true}$. For $i < m$ put
$\ell_i = \min(s_i, s_{i+m})$ and $u_i = \max(s_i, s_{i+m})$. Then either $\ell_i = \mathrm{false}$
for every $i < m$ and $u_0, \dots, u_{m-1}$ is bitonic, or $u_i = \mathrm{true}$ for every
$i < m$ and $\ell_0, \dots, \ell_{m-1}$ is bitonic.

The $\ell_i$ and $u_i$ are the outputs of the half-cleaner on $2m$ wires. This is CLRS Lemma 27.3
for bitonic $0$-$1$ sequences.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.halfClean_bitonic`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#half-clean-bitonic).

## Sorted on a block

A Boolean sequence $g : \mathbb{N} \to \mathrm{Bool}$ is sorted on
the block $[b, b + L)$ if $g(b + i) \le g(b + j)$ for all $i \le j < L$, where Booleans are
ordered by $\mathrm{false} < \mathrm{true}$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.SortedOn`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#sorted-on).

## Bitonic merger

The bitonic merger on the block of wires $[b, b + 2^k)$ is the list of
comparators defined by recursion on $k$. For $k = 0$ it is empty. On the block $[b, b + 2^{k+1})$
it is the half-cleaner on $[b, b + 2^{k+1})$, followed by the bitonic merger on $[b, b + 2^k)$,
followed by the bitonic merger on $[b + 2^k, b + 2^{k+1})$.

This is CLRS's `BITONIC-SORTER`.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicMerge`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-merge).

## The bitonic merger sorts every bitonic `0`-`1` input

Let $k, b \in \mathbb{N}$ and let $f$
assign a Boolean value to each wire $x \in \mathbb{N}$, with Booleans ordered by
$\mathrm{false} < \mathrm{true}$. If the sequence $f(b), f(b + 1), \dots, f(b + 2^k - 1)$ is
bitonic, then running the bitonic merger on the block $[b, b + 2^k)$ on $f$ gives an assignment
$g$ that is sorted on that block: $g(b + i) \le g(b + j)$ whenever $i \le j < 2^k$.

This is the correctness of CLRS's `BITONIC-SORTER`, proved by recursion on the half-cleaner
lemma.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicMerge_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-merge-sorts).

## Reversing the comparators conjugates the network by complement on Booleans

Let $ps$ be
a list of comparators on $\mathbb{N}$-indexed wires and let $ps'$ be obtained by replacing each
comparator $(i, j)$ in $ps$ by $(j, i)$. For every input $f : \mathbb{N} \to \mathrm{Bool}$ and
every wire $x$, the value of wire $x$ after running $ps'$ on $f$ is the negation of the value of
wire $x$ after running $ps$ on the complemented input $y \mapsto \lnot f(y)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.runN_swap`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#run-n-swap).

## Batcher's bitonic sorter on a block of wires

A comparator $(i, j)$ puts the minimum of
the values on wires $i$ and $j$ on wire $i$ and the maximum on wire $j$. Batcher's bitonic sorter
on the block of wires $[b, b + 2^k)$ is the list of comparators defined by recursion on $k$. For
$k = 0$ it is empty. On the block $[b, b + 2^{k+1})$ it is Batcher's bitonic sorter on
$[b, b + 2^k)$, followed by Batcher's bitonic sorter on $[b + 2^k, b + 2^{k+1})$ with every
comparator $(i, j)$ replaced by $(j, i)$, followed by the bitonic merger on $[b, b + 2^{k+1})$.

Reversing the comparators makes the second half sort downwards, so the merger receives a bitonic
sequence. (CLRS's `SORTER` instead sorts both halves up and uses `MERGER`.)

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicSortN`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-sort-n).

## The bitonic sorter sorts every `0`-`1` input

Let $k, b \in \mathbb{N}$ and let $f$ assign
a Boolean value to each wire $x \in \mathbb{N}$, with Booleans ordered by
$\mathrm{false} < \mathrm{true}$. Running Batcher's bitonic sorter on the block $[b, b + 2^k)$
on $f$ gives an assignment $g$ that is sorted on that block: $g(b + i) \le g(b + j)$ whenever
$i \le j < 2^k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicSortN_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-sort-n-sorts).

## Size of the half-cleaner

For all natural numbers $m$ and $b$, the half-cleaner on the
block of wires $[b, b + 2m)$ has exactly $m$ comparators.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.length_halfCleaner`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#length-half-cleaner).

## Size of the bitonic merger

For all natural numbers $k$ and $b$, the bitonic merger on
the block of wires $[b, b + 2^k)$ has $k \cdot 2^{k-1}$ comparators; precisely, twice its number
of comparators equals $k \cdot 2^k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.length_bitonicMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#length-bitonic-merge).

## Size of the bitonic sorter on a block of wires

For all natural numbers $k$ and $b$, the
bitonic sorter on the block of $\mathbb{N}$-indexed wires $[b, b + 2^k)$ has $k(k+1)2^k/4$
comparators; precisely, four times its number of comparators equals $k(k+1)2^k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.length_bitonicSortN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#length-bitonic-sort-n).

## Restricting comparators to finitely many wires

For a natural number $N$ and a list of
comparators on wires indexed by $\mathbb{N}$, this is the network on the $N$ wires
$0, \dots, N - 1$ that keeps, in their original order, the comparators $(i, j)$ with $i < N$
and $j < N$, and drops all the others.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.ofPairs`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#of-pairs).

## Extension of a Boolean vector by false

For $N \in \mathbb{N}$ and a Boolean vector
$v = (v_0, \dots, v_{N-1})$, its extension by $\mathrm{false}$ is the function on $\mathbb{N}$
that takes the value $v_j$ at each $j < N$ and the value $\mathrm{false}$ at each $j \ge N$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.extendFalse`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#extend-false).

## Transported comparator lists agree with the original on Boolean inputs

Let
$N \in \mathbb{N}$ and let $P$ be a list of comparators on natural-number-indexed wires, each of
which joins two wires below $N$. For every Boolean input $v$ on the wires $0, \dots, N - 1$, run
the network on $N$ wires obtained from $P$ on $v$ and extend its output by $\mathrm{false}$ to
all wires in $\mathbb{N}$; the result equals the result of running $P$ on the extension of $v$ by
$\mathrm{false}$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.ext_run_ofPairs`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#ext-run-of-pairs).

## Batcher's bitonic sorting network

For $k \in \mathbb{N}$, Batcher's bitonic sorting
network on $2^k$ wires is the comparator network on the wires $0, 1, \dots, 2^k - 1$ made of the
comparators of Batcher's bitonic sorter on the block $[0, 2^k)$ that join two wires below $2^k$
(in fact all of them), applied in the same order.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicSorter`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-sorter).

## Batcher's bitonic sorter sorts every input over every linear order

For every
$k \in \mathbb{N}$ and every linearly ordered type $\alpha$, Batcher's bitonic sorting network on
$2^k$ wires sorts inputs over $\alpha$: for every assignment $v$ of elements of $\alpha$ to the
wires $0, 1, \dots, 2^k - 1$, the output of the network on $v$ is monotone in the wire order.

The proof goes through the 0-1 principle.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.bitonicSorter_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#bitonic-sorter-sorts).

## Comparator count of Batcher's bitonic sorter

For every natural number $k$, Batcher's
bitonic sorting network on $2^k$ wires has $k(k+1)2^k/4$ comparators; precisely, four times its
number of comparators equals $k(k+1)2^k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.Bitonic.length_bitonicSorter`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/SortingNetworks/Bitonic.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html#length-bitonic-sorter).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bitonic sorter](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/sorting-networks/bitonic-sorter)
