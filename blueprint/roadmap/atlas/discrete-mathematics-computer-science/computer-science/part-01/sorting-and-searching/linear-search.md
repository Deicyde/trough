---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.linearSearch, Cslib.Algorithms.Lean.TimeM.ret_linearSearch, Cslib.Algorithms.Lean.TimeM.linearSearch_eq_some_iff, Cslib.Algorithms.Lean.TimeM.linearSearch_eq_none_iff, Cslib.Algorithms.Lean.TimeM.linearSearch_time_nil, Cslib.Algorithms.Lean.TimeM.linearSearch_time_cons, Cslib.Algorithms.Lean.TimeM.linearSearch_time_eq_of_ret_eq_some, Cslib.Algorithms.Lean.TimeM.linearSearch_time_eq_of_ret_eq_none
statement: formalized
proof: formalized
---

# Linear search

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html).

## Linear search

Given a predicate $p$ on a type $\alpha$ and a list $L$ of elements of
$\alpha$, linear search scans $L$ from the front and returns the index of the first element of $L$
that satisfies $p$, or no index if no element does, together with a cost that counts one unit for
each evaluation of $p$. On the empty list it returns no index at cost $0$. On a list with head $x$
and tail $T$ it evaluates $p(x)$ at a cost of one unit; if $p(x)$ is true it returns the index $0$,
and otherwise it searches $T$, adds one to the index found there (if any), and adds the cost of
that search.

No cost is charged for list operations, index arithmetic, or control flow.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch`, a definition declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search).

## Linear search returns the first satisfying index

For every predicate $p$ on a type
$\alpha$ and every list $L = (x_0, \dots, x_{n-1})$ over $\alpha$, the index returned by linear
search for $p$ on $L$ (ignoring its cost) equals the result of the standard library's
first-index search: the least $i < n$ with $p(x_i)$ true, or no index if $p(x_i)$ is false for
every $i < n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ret_linearSearch`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#ret-linear-search).

## Characterization of a successful linear search

For every predicate $p$ on a type
$\alpha$, every list $L = (x_0, \dots, x_{n-1})$ over $\alpha$ and every natural number $i$,
linear search for $p$ on $L$ returns the index $i$ if and only if $i < n$, $p(x_i)$ is true, and
$p(x_j)$ is false for every $j < i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-eq-some-iff).

## Linear search fails exactly when no element satisfies the predicate

For every predicate
$p$ on a type $\alpha$ and every list $L$ over $\alpha$, linear search for $p$ on $L$ returns no
index if and only if $p(x)$ is false for every element $x$ of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-eq-none-iff).

## Cost of linear search on the empty list

For every predicate $p$ on a type $\alpha$, linear
search for $p$ on the empty list has cost $0$: it evaluates $p$ zero times.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_time_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-time-nil).

## Cost recurrence for linear search

For every predicate $p$ on a type $\alpha$, every
$x \in \alpha$ and every list $T$ over $\alpha$, the cost of linear search for $p$ on the list
with head $x$ and tail $T$ is $1$ if $p(x)$ is true, and $1$ plus the cost of linear search for
$p$ on $T$ if $p(x)$ is false. The head costs one evaluation of $p$, and the tail is searched only
when the head fails.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_time_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-time-cons).

## Cost of a successful linear search

For every predicate $p$ on a type $\alpha$, every
list $L$ over $\alpha$ and every natural number $i$, if linear search for $p$ on $L$ returns the
index $i$, then its cost is $i + 1$: it evaluates $p$ exactly $i + 1$ times.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_time_eq_of_ret_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-time-eq-of-ret-eq-some).

## Cost of an unsuccessful linear search

For every predicate $p$ on a type $\alpha$ and
every list $L$ over $\alpha$, if linear search for $p$ on $L$ returns no index, then its cost is
the length of $L$: it evaluates $p$ once for every element of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_time_eq_of_ret_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-time-eq-of-ret-eq-none).

## Linear search costs at most the list length

For every predicate $p$ on a type $\alpha$
and every list $L$ over $\alpha$, the cost of linear search for $p$ on $L$ is at most the length
of $L$: it evaluates $p$ at most once for every element of $L$.

Formalized by `Cslib.Algorithms.Lean.TimeM.linearSearch_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Search/Linear.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Search/Linear.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html#linear-search-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear search](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/linear-search/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/sorting-and-searching/linear-search)
