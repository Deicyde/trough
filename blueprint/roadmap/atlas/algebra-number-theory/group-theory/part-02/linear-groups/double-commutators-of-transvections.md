---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.IsElementaryTransvection, MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.doubleCommutatorWithTransvectionsUnipotent, MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.doubleCommutatorWithTransvectionsUnipotent_refuted
statement: formalized
---

# Double commutators of transvections

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections/index.html).

## Elementary transvection

For a ring $R$ and $n \in \mathbb{N}$, a matrix
$\tau \in \mathrm{GL}_n(R)$ is an elementary transvection when $\tau = 1 + r e_{ij}$ for some
indices $i \ne j$ and some nonzero $r \in R$, where $e_{ij}$ is the matrix unit with $1$ in
position $(i, j)$ and $0$ elsewhere.

Formalized by `MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.IsElementaryTransvection`, a definition declared in [WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections/index.html#is-elementary-transvection).

## Petechuk's double commutator question (Kourovka 10.46)

The statement that for every
nontrivial associative ring $R$ with identity, every $n \ge 3$ and every
$\sigma \in \mathrm{GL}_n(R)$ there are elementary transvections
$\tau_1, \tau_2 \in \mathrm{GL}_n(R)$ such that $[[\sigma, \tau_1], \tau_2]$ is unipotent, that
is, $[[\sigma, \tau_1], \tau_2] - 1$ is a nilpotent matrix, where $[x, y] = x y x^{-1} y^{-1}$.

In the problem, transvections are read as elementary transvections.

Formalized by `MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.doubleCommutatorWithTransvectionsUnipotent`, a definition declared in [WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections/index.html#double-commutator-with-transvections-uni).

## Petechuk's double commutator question has a negative answer (Kourovka 10.46)

There are a
nontrivial associative ring $R$ with identity, an integer $n \ge 3$ and a matrix
$\sigma \in \mathrm{GL}_n(R)$ such that for all elementary transvections
$\tau_1, \tau_2 \in \mathrm{GL}_n(R)$ the matrix $[[\sigma, \tau_1], \tau_2] - 1$ is not nilpotent,
that is, $[[\sigma, \tau_1], \tau_2]$ is not unipotent. Here $[x, y] = x y x^{-1} y^{-1}$, and an
elementary transvection is a matrix $1 + r e_{ij}$ with $i \ne j$ and $r \in R$ nonzero, where
$e_{ij}$ is the matrix unit with $1$ in position $(i, j)$ and $0$ elsewhere.

Muliarchyk (Theorem 1.1) shows the following for every field $k$ and $n \ge 2$. Let $R$ be the
free associative $k$-algebra on generators $x_{ij}, y_{ij}$ ($1 \le i, j \le n$) modulo the
relations $XY = YX = I$, where $X = (x_{ij})$, $Y = (y_{ij})$ and $I$ is the $n \times n$ identity
matrix; $R$ is nonzero. Then every nonempty iterated commutator of $X \in \mathrm{GL}_n(R)$ with
nonidentity unipotent matrices is nonunipotent.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 10.46 (V. M. Petechuk); resolution: K. Muliarchyk, A counterexample to Kourovka Notebook Problem 10.46: unipotent commutators over noncommutative algebras, preprint (2026), Theorem 1.1 (over R = k⟨x_ij, y_ij⟩ / (XY = YX = I) every nonempty iterated commutator of X with nonidentity unipotent matrices is nonunipotent); the Kourovka Notebook (21st issue) marks 10.46 solved, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka_10.46_solution.pdf.

Stated but not proved: `MathlibExt.GroupTheory.TransvectionCommutatorUnipotentKourovka10Problem46Wanted.doubleCommutatorWithTransvectionsUnipotent_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TransvectionCommutatorUnipotentKourovka10Problem46Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections/index.html#double-commutator-with-transvections-uni-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Double commutators of transvections](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/linear-groups/double-commutators-of-transvections)
