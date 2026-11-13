---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups, Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_time, Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_mem, Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_correct, Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_length, Cslib.Algorithms.Lean.TimeM.medianOfMedians, Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_quickselect_of_length_le, Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_pure_none_of_length_le_rank
statement: formalized
proof: formalized
---

# Median of medians

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html).

## Group medians for median-of-medians selection

Given a list $xs$ over a linear
order, split $xs$ into consecutive blocks of five elements, the last of which may be shorter.
Sort each block $g$ by insertion sort and return, in block order, the entry at position
$\lfloor (|g| - 1)/2 \rfloor$ (counting from $0$) of each sorted block, that is, its lower
median. The cost is the total number of comparisons made by these insertion sorts.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups`, a definition declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-groups).

## Comparison cost of the group medians

For every list $xs$ of length $n$ over a linear
order, computing the group medians of $xs$ takes at most $2n$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-groups-time).

## Group medians come from the input

For every list $xs$ over a linear order, every
entry of the list of group medians of $xs$ is an element of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-groups-mem).

## Group medians are lower medians of their blocks

Let $xs$ be a list over a linear
order, and let $g_1, \dots, g_m$ be its consecutive blocks of five elements, the last of which
may be shorter. Then the list of group medians of $xs$ has the same length $m$, say
$x_1, \dots, x_m$, and for each $i$, writing $k_i = \lfloor (|g_i| - 1)/2 \rfloor$ and counting
elements of $g_i$ with multiplicity: $x_i$ belongs to $g_i$, at most $k_i$ elements of $g_i$
are less than $x_i$, and more than $k_i$ elements of $g_i$ are less than or equal to $x_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-groups-correct).

## Number of group medians

For every list $xs$ of length $n$ over a linear order, the
list of group medians of $xs$ has exactly $\lfloor (n + 4)/5 \rfloor = \lceil n/5 \rceil$
entries.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMediansGroups_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians/Groups.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-groups-length).

## Median-of-medians selection

Given a list $L$ over a linear order and a zero-based rank
$k$, median-of-medians selection returns either an element of $L$ or nothing, charging one unit
of cost per order comparison. If $k \ge |L|$, where $|L|$ is the length of $L$, it returns
nothing at no cost. Otherwise it runs the following recursive procedure on $(L, k)$ with a budget
of $|L|$ nested calls, returning nothing if the budget runs out. A list of length at most $140$
is handled by deterministic quickselect at the current rank. A longer list is cut into
consecutive groups of five entries, the last possibly shorter; each group is sorted by insertion
sort and its lower median is kept, giving a list $M$ of $m$ medians. The procedure recursively
selects the entry of $M$ at rank $\lfloor m/2 \rfloor$ as the pivot $x$ (returning nothing if
that call does), and splits the list by a three-way partition into the entries below $x$, equal
to $x$ and above $x$, with $b$ entries below and $e$ equal. If the current rank $r$ satisfies
$r < b$ it recurses on the lower part with rank $r$; if $b \le r < b + e$ it returns $x$;
otherwise it recurses on the upper part with rank $r - b - e$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians`, a definition declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians).

## Median-of-medians selection is quickselect on short lists

For every list $L$ of length
at most $140$ over a linearly ordered type and every natural number $k$, median-of-medians
selection of rank $k$ in $L$ coincides with timed quickselect of rank $k$ in $L$: both return
the same result and are charged the same number of comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_quickselect_of_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-eq-quickselect-of-leng).

## Out-of-range ranks cost no comparisons

For every list $L$ over a linearly ordered type
and every natural number $k$ at least the length of $L$, median-of-medians selection of rank $k$
in $L$ returns nothing and is charged zero comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_pure_none_of_length_le_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-eq-pure-none-of-length).

## Comparison bound for median-of-medians selection on short lists

For every list $L$ of
length $n \le 140$ over a linearly ordered type and every natural number $k$, median-of-medians
selection of rank $k$ in $L$ is charged at most $80n$ comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_base_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-base-time).

## Correctness of median-of-medians selection on short lists

Let $L$ be a list of length
at most $140$ over a linearly ordered type and let $k$ be a natural number. If median-of-medians
selection of rank $k$ in $L$ returns an element $x$, then $x$ occurs in $L$, the number of entries
of $L$ less than $x$, counted with multiplicity, is at most $k$, and $k$ is less than the number
of entries of $L$ that are at most $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_base_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-base-correct).

## Correctness of median-of-medians selection

Let $L$ be a list over a linearly ordered type
and let $k$ be a natural number. If median-of-medians selection of rank $k$ in $L$ returns an
element $x$, then $x$ occurs in $L$, the number of entries of $L$ less than $x$, counted with
multiplicity, is at most $k$, and $k$ is less than the number of entries of $L$ that are at
most $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-correct).

## Median-of-medians selection succeeds on valid ranks

For every list $L$ over a linearly
ordered type and every natural number $k$ less than the length of $L$, median-of-medians
selection of rank $k$ in $L$ returns some element.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_exists`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-exists).

## Median-of-medians selection fails exactly on out-of-range ranks

For every list $L$ over
a linearly ordered type and every natural number $k$, median-of-medians selection of rank $k$ in
$L$ returns nothing if and only if $k$ is at least the length of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-eq-none-iff).

## Median-of-medians selection agrees with sorting

For every list $L$ over a linearly
ordered type and every natural number $k$, median-of-medians selection of rank $k$ in $L$ returns
the entry at zero-based position $k$ of the insertion sort of $L$ by $\le$ when $k$ is less than
the length of $L$, and returns nothing otherwise.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_eq_getElem?_insertionSort`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-eq-get-elem-insertion).

## Set rank of a median-of-medians result

Let $L$ be a list without repeated entries over a
linear order and let $k \in \mathbb{N}$. If median-of-medians selection on $L$ at zero-based rank
$k$ returns an element $x$, then the set $\{y \in L : y \le x\}$ has exactly $k + 1$ elements.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_set_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-set-rank).

## One-based rank of a median-of-medians result

Let $L$ be a list without repeated entries
over a linear order and let $i \ge 1$. If median-of-medians selection on $L$ at zero-based rank
$i - 1$ returns an element $x$, then the set $\{y \in L : y \le x\}$ has exactly $i$ elements.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_source_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-source-rank).

## Median of medians selects every one-based rank

Let $L$ be a list without repeated
entries over a linear order, of length $n$, and let $1 \le i \le n$. Then median-of-medians
selection on $L$ at zero-based rank $i - 1$ returns an element $x$ of $L$, and the set
$\{y \in L : y \le x\}$ has exactly $i$ elements.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_source_exists`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-source-exists).

## Median of medians finds the lower median

Let $L$ be a nonempty list of length $n$ over a
linear order, and let $k = \lfloor (n - 1)/2 \rfloor$. Then median-of-medians selection on $L$ at
zero-based rank $k$ returns an element $x$ of $L$ such that at most $k$ entries of $L$ are less
than $x$ and more than $k$ entries of $L$ are at most $x$, where entries are counted with
repetition.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_lower_median`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-lower-median).

## Median of medians finds the upper median

Let $L$ be a nonempty list of length $n$ over a
linear order, and let $k = \lfloor n/2 \rfloor$. Then median-of-medians selection on $L$ at
zero-based rank $k$ returns an element $x$ of $L$ such that at most $k$ entries of $L$ are less
than $x$ and more than $k$ entries of $L$ are at most $x$, where entries are counted with
repetition.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_upper_median`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-upper-median).

## Size budget for the two median-of-medians recursive calls

Let $n$, $m$ and $p$ be natural
numbers with $n \ge 140$, $m \le \lfloor (n + 4)/5 \rfloor$ and
$p \le \lfloor 7n/10 \rfloor + 6$. Then $20m + 20p + n \le 20n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_child_size_budget`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-child-size-budget).

## Cost budget for one median-of-medians step

Let $n$, $m$, $p$, $a$, $c_1$ and $c_2$ be
natural numbers with $n \ge 140$, $m \le \lfloor (n + 4)/5 \rfloor$,
$p \le \lfloor 7n/10 \rfloor + 6$, $c_1 \le 20am$ and $c_2 \le 20ap$. Then
$c_1 + c_2 + an \le 20an$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_combine_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-combine-time).

## Median of medians makes linearly many comparisons

For every list $L$ of length $n$ over
a linear order and every $k \in \mathbb{N}$, median-of-medians selection on $L$ at rank $k$
charges at most $80n$ comparisons, where $n$ counts repeated entries.

Only order comparisons are charged; list construction, rank checks and recursion are free.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-time).

## Linear solution of the median-of-medians recurrence

Let $T : \mathbb{N} \to \mathbb{N}$
and $a \in \mathbb{N}$. Suppose that $T(n) \le 20an$ for every $n \le 140$, and that for every
$n > 140$ there are $m, p \in \mathbb{N}$ with $m \le \lfloor (n + 4)/5 \rfloor$,
$p \le \lfloor 7n/10 \rfloor + 6$ and $T(n) \le T(m) + T(p) + an$. Then $T(n) \le 20an$ for
every $n \in \mathbb{N}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.medianOfMedians_linear_recurrence`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/MedianOfMedians.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html#median-of-medians-linear-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Median of medians](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/median-of-medians/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/median-of-medians)
