---
declaration: section
origin: cited
lean: MetaMathlibExt.pascalEntry, MetaMathlibExt.pascalAlpha, MetaMathlibExt.pascalAlpha_eq, MetaMathlibExt.tsum_pascalAlpha_eq, MetaMathlibExt.tsum_pascalEntry_comm, MetaMathlibExt.tsum_pascalEntry_row, MetaMathlibExt.tsum_pascalAlpha_eq_geometric
statement: formalized
proof: formalized
---

# Pascal matrix

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html).

## Entries of the infinite Pascal matrix

For natural numbers $i$ and $j$, the entry of the
infinite Pascal matrix in row $i$ and column $j$ is the binomial coefficient $\binom{i}{j}$.

Formalized by `MetaMathlibExt.pascalEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#pascal-entry).

## Column generating functions of the Pascal matrix

For a natural number $j$ and a real
number $x$, the column generating function of the infinite Pascal matrix is
$\alpha_j(x) = \sum_{i \ge 0} \binom{i}{j} x^i$, where $\binom{i}{j}$ is the entry in row $i$ and
column $j$; the sum is taken to be $0$ when the series is not summable.

Formalized by `MetaMathlibExt.pascalAlpha`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#pascal-alpha).

## Closed form of the Pascal column generating functions

For every natural number $j$ and
every real number $x$ with $|x| < 1$, the column generating function $\alpha_j$ of the infinite
Pascal matrix satisfies $\alpha_j(x) = x^j / (1 - x)^{j+1}$.

Formalized by `MetaMathlibExt.pascalAlpha_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#pascal-alpha-eq).

## Summing the Pascal column generating functions

For every real number $x$ with
$|x| < 1/2$, the sum $\sum_{j \ge 0} \alpha_j(x)$ of the column generating functions of the
infinite Pascal matrix equals $\sum_{j \ge 0} \sum_{i \ge 0} \binom{i}{j} x^i$, where
$\binom{i}{j}$ is the entry in row $i$ and column $j$, and it also equals
$\sum_{j \ge 0} x^j / (1 - x)^{j+1}$.

Formalized by `MetaMathlibExt.tsum_pascalAlpha_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#tsum-pascal-alpha-eq).

## Reversing the order of summation in the Pascal matrix

For every real number $x$ with
$|x| < 1/2$, writing $\binom{i}{j}$ for the entry of the infinite Pascal matrix in row $i$ and
column $j$, we have
$\sum_{j \ge 0} \sum_{i \ge 0} \binom{i}{j} x^i = \sum_{i \ge 0} \sum_{j \ge 0} \binom{i}{j} x^i$,
and this sum equals $\frac{1}{1 - x} \sum_{j \ge 0} \left(\frac{x}{1 - x}\right)^j$.

Formalized by `MetaMathlibExt.tsum_pascalEntry_comm`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#tsum-pascal-entry-comm).

## Summing the Pascal matrix row by row

For every real number $x$ with $|x| < 1/2$,
writing $\binom{i}{j}$ for the entry of the infinite Pascal matrix in row $i$ and column $j$, we
have $\sum_{i \ge 0} x^i \sum_{j=0}^{i} \binom{i}{j} = \frac{1}{1 - 2x}$.

Formalized by `MetaMathlibExt.tsum_pascalEntry_row`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#tsum-pascal-entry-row).

## Total generating function of the Pascal matrix

For every real number $x$ with
$|x| < 1/2$, the sum $\sum_{j \ge 0} \alpha_j(x)$ of the column generating functions of the
infinite Pascal matrix equals $\sum_{i \ge 0} (2x)^i$, and
$\sum_{i \ge 0} (2x)^i = \frac{1}{1 - 2x}$.

Formalized by `MetaMathlibExt.tsum_pascalAlpha_eq_geometric`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PascalMatrix.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html#tsum-pascal-alpha-eq-geometric).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pascal matrix](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/pascal-matrix)
