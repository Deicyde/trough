---
declaration: section
origin: cited
lean: MetaMathlibExt.columnWeight, MetaMathlibExt.EvenTable, MetaMathlibExt.evenTableWeight
statement: formalized
proof: formalized
---

# Even tables in random determinant moments

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments/index.html).

## Column weight

Let $n$ be a natural number, $M$ a commutative monoid and
$f \colon \mathbb{N} \to M$ a function. A column is a finite list of entries from
$\{0, 1, \dots, n - 1\}$; for each $j$ in this range let $c_j$ be the number of times $j$ occurs
in the column. The weight of the column is the product $\prod_{j=0}^{n-1} f(c_j)$ in $M$.

## Sources

- Dominik Beck, Zelin Lv, and Aaron Potechin, *The Sixth Moment of Random Determinants*, Journal of Integer Sequences 26 (2023), Article 23.6.3, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Lv/lv3.tex>.

Formalized by `MetaMathlibExt.columnWeight`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ColumnWeight.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ColumnWeight.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments/index.html#column-weight).

## Even table

For natural numbers $k$ and $n$, an even $k \times n$ table is a $k \times n$
array of entries from $\{0, 1, \dots, n-1\}$ such that $k$ is even, every row is a permutation of
$\{0, 1, \dots, n-1\}$, and in every column each value that occurs there occurs an even number
of times.

Formalized by `MetaMathlibExt.EvenTable`, a structure declared in [MathlibExt/Combinatorics/Enumerative/EvenTableWeight.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/EvenTableWeight.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments/index.html#even-table).

## Weight of an even table

Let $M$ be a commutative monoid and $f : \mathbb{N} \to M$. The
weight of an even $k \times n$ table $t$ with respect to $f$ is the product of the column weights
of its $n$ columns with respect to $f$:

$$\prod_{j=0}^{n-1} \prod_{v=0}^{n-1} f(m_j(v)),$$

where $m_j(v)$ is the number of times the value $v$ occurs in column $j$ of $t$.

Formalized by `MetaMathlibExt.evenTableWeight`, a definition declared in [MathlibExt/Combinatorics/Enumerative/EvenTableWeight.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/EvenTableWeight.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments/index.html#even-table-weight).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Even tables in random determinant moments](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/designs-latin-squares/even-tables-in-random-determinant-moments)
