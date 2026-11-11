---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SparseTable, Cslib.Algorithms.Lean.SparseTable.omin, Cslib.Algorithms.Lean.SparseTable.omin_self, Cslib.Algorithms.Lean.SparseTable.level, Cslib.Algorithms.Lean.SparseTable.level_length, Cslib.Algorithms.Lean.SparseTable.getElem?_level, Cslib.Algorithms.Lean.SparseTable.nextLevel, Cslib.Algorithms.Lean.SparseTable.buildStep
statement: formalized
proof: formalized
---

# Sparse table

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html).

## Sparse Table

## Sparse table

A sparse table over a type $\alpha$ consists of an array of elements of
$\alpha$, called its data, and an array of arrays of elements of $\alpha$, called its levels.

The intended meaning is that level $k$ stores the minima of the length-$2^k$ slices of the data;
data and levels are stored as arrays so that entry lookup is random access. Arbitrary values need
not relate data and levels at all; validity ties every stored level to this specification, tables
produced by the construction are valid, and query correctness is stated for valid tables.

Formalized by `Cslib.Algorithms.Lean.SparseTable`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#sparse-table).

## Option minimum

For a type $\alpha$ with a minimum operation, the option minimum extends
$\min$ to optional values (elements of $\alpha$ or none): on two elements $a, b$ of $\alpha$ it
returns $\min(a, b)$, and none is a neutral element on either side.

Formalized by `Cslib.Algorithms.Lean.SparseTable.omin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#omin).

## Idempotence of the option minimum

For every linearly ordered type $\alpha$ and every
optional value $a$ (an element of $\alpha$ or none), the option minimum of $a$ with itself is $a$.

This is what lets two overlapping query intervals count their overlap twice.

Formalized by `Cslib.Algorithms.Lean.SparseTable.omin_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#omin-self).

## Levels of a sparse table

For a list $a$ over a type with a minimum operation $\min$, the
levels of $a$ are defined recursively: level $0$ is $a$, and if level $k$ is
$\ell = (\ell_0, \dots, \ell_{m-1})$, then level $k + 1$ is the list of the values
$\min(\ell_i, \ell_{i+2^k})$ for $0 \le i < m - 2^k$ (empty when $m \le 2^k$).

Over a linear order, element $i$ of level $k$ is the minimum of the $2^k$ consecutive elements
of $a$ starting at index $i$, and only start indices whose interval fits in $a$ get an element.

Formalized by `Cslib.Algorithms.Lean.SparseTable.level`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#level).

## Length of a level

For a list $a$ of length $n$ over a type with a minimum operation
and a natural number $k$, level $k$ of $a$ has length $\max(n + 1 - 2^k, 0)$: one element for
each start index $i$ with $i + 2^k \le n$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.level_length`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#level-length).

## Levels hold interval minima

Let $a = (a_0, \dots, a_{n-1})$ be a list over a linearly
ordered type, and let $k$ and $i$ be natural numbers with $i + 2^k \le n$. Then level $k$ of $a$
has an element at index $i$, and it equals $\min(a_i, a_{i+1}, \dots, a_{i+2^k-1})$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.getElem?_level`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#get-elem-level).

## Next level of a sparse table row

For a type with a minimum operation, an array
$(r_0, \dots, r_{n-1})$ and a natural number $k$, the next level is the array of length
$n - 2^k$ (empty when $2^k \ge n$) whose entry $i$ is $\min(r_i, r_{i + 2^k})$.

The construction of a sparse table computes each level once from the previous one this way.

Formalized by `Cslib.Algorithms.Lean.SparseTable.nextLevel`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#next-level).

## One step of the sparse-table construction

Work over a type with a minimum operation
$\min$. Given a pair $(r, L)$ of a current row $r$ (an array of length $|r|$) and an array $L$
of the rows recorded so far, and a natural number $k$, the build step returns the pair
$(r', L')$, where $L'$ is $L$ with $r$ appended at the end, and $r'$ is the array whose
entry $i$ is $\min(r_i, r_{i+2^k})$ for each $i$ with $i + 2^k < |r|$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.buildStep`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#build-step).

## Building a sparse table

For a list $a$ of length $n$ over a type with a minimum
operation $\min$, the sparse table built from $a$ has data $a$ and
$\lfloor \log_2 n \rfloor + 1$ stored rows, where $\lfloor \log_2 0 \rfloor$ is taken to be $0$.
The rows are produced by iterating the build step for $k = 0, 1, \dots, \lfloor \log_2 n \rfloor$,
starting from the current row $a$ and no recorded rows. So row $0$ is $a$, and entry $i$ of
row $k + 1$ is $\min(x_i, x_{i+2^k})$, where $x$ is row $k$ and $i + 2^k$ is less than the
length of $x$. Each row is computed once, from its predecessor.

Formalized by `Cslib.Algorithms.Lean.SparseTable.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#build).

## Valid sparse table

A sparse table over a type with a minimum operation, whose data is a
list $a$ of length $n$, is valid when it has exactly $m + 1$ levels, where
$m = \lfloor \log_2 n \rfloor$ for $n \ge 1$ and $m = 0$ for $n = 0$, and for each $k \le m$ its
level $k$ is the list $L_k$ defined by $L_0 = a$ and, for $x = L_j$, $L_{j+1}$ is the list of
length $|x| - 2^j$ (empty when $2^j \ge |x|$) whose entry $i$ is $\min(x_i, x_{i + 2^j})$. For a
linear order, $L_k$ is the list of minima of the length-$2^k$ slices of $a$.

Tables produced by the construction are valid, an arbitrary value such as data $(1)$ with the
single level $(99)$ is not, and query correctness is stated only for valid tables.

Formalized by `Cslib.Algorithms.Lean.SparseTable.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#valid).

## Built sparse tables are valid

For every list $a$ over a type with a minimum operation,
the sparse table built from $a$ is valid: its stored rows are exactly the levels
$0, 1, \dots, \lfloor \log_2 n \rfloor$ of $a$, in this order, where $n$ is the length of $a$
and $\lfloor \log_2 0 \rfloor$ is taken to be $0$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.build_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#build-valid).

## Sparse-table entries

For a sparse table $t$ and natural numbers $k$ and $i$, the entry
of $t$ at row $k$ and index $i$ is element $i$ of the $k$-th stored row of $t$ (both counted
from $0$) when $t$ has a $k$-th row and that row has an element at index $i$; otherwise the
entry is undefined. Both lookups are random-access array lookups.

Formalized by `Cslib.Algorithms.Lean.SparseTable.entry`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#entry).

## Rows of a valid sparse table are its levels

Let $t$ be a valid sparse table over a type
with a minimum operation, with data $d$ of length $n$, and let $k \le \lfloor \log_2 n \rfloor$,
where $\lfloor \log_2 0 \rfloor$ is taken to be $0$. Then for every index $i$, the entry of $t$
at row $k$ and index $i$ is defined exactly when level $k$ of $d$ has an element at index $i$,
and in that case the two are equal.

Formalized by `Cslib.Algorithms.Lean.SparseTable.entry_eq_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#entry-eq-of-valid).

## Entries of a built sparse table are interval minima

Let $a = (a_0, \dots, a_{n-1})$ be
a list over a linearly ordered type, and let $k$ and $i$ be natural numbers with
$i + 2^k \le n$. Then the entry of the sparse table built from $a$ at row $k$ and index $i$ is
defined and equals $\min(a_i, a_{i+1}, \dots, a_{i+2^k-1})$.

No separate bound on $k$ is needed: $i + 2^k \le n$ already implies
$k \le \lfloor \log_2 n \rfloor$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.entry_build_eq_min?`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#entry-build-eq-min).

## Entries of a valid sparse table are interval minima

Let $t$ be a valid sparse table
over a linearly ordered type, with data $d = (d_0, \dots, d_{n-1})$, and let $k$ and $i$ be
natural numbers with $i + 2^k \le n$. Then the entry of $t$ at row $k$ and index $i$ is
defined and equals $\min(d_i, d_{i+1}, \dots, d_{i+2^k-1})$.

Formalized by `Cslib.Algorithms.Lean.SparseTable.entry_eq_min?_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#entry-eq-min-of-valid).

## Sparse table range-minimum query

For a sparse table $t$ over a type with a minimum operation
and natural numbers $l, r$, the query over $[l, r)$ returns none when $r \le l$. Otherwise, with
$k = \lfloor \log_2 (r - l) \rfloor$, it returns the option minimum (the minimum, with none as a
neutral element on either side) of the entries of $t$ at level $k$ and indices $l$ and $r - 2^k$,
in this order, where an entry not stored in $t$ counts as none.

Formalized by `Cslib.Algorithms.Lean.SparseTable.query`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#query).

## Correctness of queries on valid sparse tables

Let $t$ be a valid sparse table over a
linearly ordered type whose data is the list $(a_0, \dots, a_{n-1})$, and let $l, r$ be natural
numbers with $r \le n$. Then the range-minimum query over $[l, r)$ on $t$ returns the minimum of
the slice $(a_l, \dots, a_{r-1})$ (none when $r \le l$, where the slice is empty).

Only the premise $r \le n$ is needed: for reversed bounds $r \le l$ both sides are none.

Formalized by `Cslib.Algorithms.Lean.SparseTable.query_eq_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#query-eq-of-valid).

## Correctness of sparse table queries

Let $a = (a_0, \dots, a_{n-1})$ be a list over a
linearly ordered type and let $l, r$ be natural numbers with $r \le n$. Then the range-minimum
query over $[l, r)$ on the sparse table built from $a$ returns the minimum of the slice
$(a_l, \dots, a_{r-1})$ (none when $r \le l$, where the slice is empty).

No ordering premise $l \le r$ is needed.

Formalized by `Cslib.Algorithms.Lean.SparseTable.query_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#query-build).

## Whole-range sparse table query

For every list $a$ of length $n$ over a linearly ordered
type, the range-minimum query over $[0, n)$ on the sparse table built from $a$ returns the
minimum of $a$ (none when $a$ is empty).

Formalized by `Cslib.Algorithms.Lean.SparseTable.query_build_all`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/SparseTable.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html#query-build-all).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sparse table](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/range-query-structures/sparse-table)
