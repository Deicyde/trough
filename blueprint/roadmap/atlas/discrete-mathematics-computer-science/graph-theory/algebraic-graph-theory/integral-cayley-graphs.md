---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.HasIntegralSpectrum, MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.involutionCayleyGraphIntegral, MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.threeCyclesOneTwo, MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.alternatingThreeCycleCayleyGraphIntegral, MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.involutionCayleyGraphIntegral_holds, MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.alternatingThreeCycleCayleyGraphIntegral_holds
statement: formalized
---

# Integral Cayley graphs

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html).

## Integer matrix with integral spectrum

A square integer matrix is integral: every complex root of its characteristic polynomial (every
eigenvalue) is an integer.

Formalized by `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.HasIntegralSpectrum`, a definition declared in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#has-integral-spectrum).

## The Kourovka 19.50(a) integrality claim

This is the proposition that for every finite
group $G$ and every subset $R \subseteq G$ such that every element of $R$ is an involution
($r^2 = 1$ and $r \ne 1$), $R$ is closed under conjugation ($g r g^{-1} \in R$ for all $r \in R$
and $g \in G$) and $R$ generates $G$, the Cayley graph $\mathrm{Cay}(G, R)$ is integral. Here
$\mathrm{Cay}(G, R)$ has vertex set $G$, distinct $x$ and $y$ being adjacent when $x^{-1} y \in R$
or $y^{-1} x \in R$, and a graph is integral when every eigenvalue of its integer adjacency matrix
(every complex root of the characteristic polynomial of that matrix) is an integer.

Formalized by `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.involutionCayleyGraphIntegral`, a definition declared in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#involution-cayley-graph-integral).

## The 3-cycles (1 2 k)

For a natural number $n$, this is the set of $3$-cycles $(1\,2\,k)$
with $3 \le k \le n$ in the symmetric group $S_n$. With the points numbered $0, 1, \dots, n - 1$,
these are the permutations $(0\,1\,k) = (0\,1)(1\,k)$ with $2 \le k < n$, products composed right
to left; the set is empty when $n < 3$.

Formalized by `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.threeCyclesOneTwo`, a definition declared in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#three-cycles-one-two).

## The Kourovka 19.50(b) integrality claim

For $n \ge 3$ let $S$ be the set of $3$-cycles
$(1\,2\,k)$ with $3 \le k \le n$ on the points $1, \dots, n$, and let $R = S \cup S^{-1}$, a subset
of the alternating group $A_n$. This is the proposition that for every $n \ge 3$ the Cayley graph
$\mathrm{Cay}(A_n, R)$ is integral. Here $\mathrm{Cay}(A_n, R)$ has vertex set $A_n$, distinct $x$
and $y$ being adjacent when $x^{-1} y \in R$ or $y^{-1} x \in R$, and a graph is integral when
every eigenvalue of its integer adjacency matrix (every complex root of the characteristic
polynomial of that matrix) is an integer.

Formalized by `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.alternatingThreeCycleCayleyGraphIntegral`, a definition declared in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#alternating-three-cycle-cayley-graph-int).

## Cayley graphs on normal sets of involutions are integral

Let $G$ be a finite group and let
$R \subseteq G$ be a set of involutions ($r^2 = 1$ and $r \ne 1$ for every $r \in R$) that is
closed under conjugation ($g r g^{-1} \in R$ for all $r \in R$ and $g \in G$) and generates $G$.
Then the Cayley graph $\mathrm{Cay}(G, R)$, whose vertices are the elements of $G$ with distinct
$x$ and $y$ adjacent when $x^{-1} y \in R$ or $y^{-1} x \in R$, is integral: every eigenvalue of
its integer adjacency matrix (every complex root of the characteristic polynomial of that matrix)
is an integer.

The Kourovka Archive proof: every eigenvalue of $\mathrm{Cay}(G, R)$ has the form
$\frac{1}{\chi(1)} \sum_{r \in R} \chi(r)$ for an irreducible character $\chi$ of $G$; this number
is rational because characters take integer values on involutions, and it is an algebraic integer.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.50 (D. V. Lytkina); resolution: (a) D. O. Revin, letter of 21 April 2018; A. Abdollahi, letter of 3 May 2018; (b) W. Guo, D. V. Lytkina, V. D. Mazurov and D. O. Revin, Integral Cayley graphs, Algebra Logic 58 (2019), no. 4, 297-305, doi:10.1007/s10469-019-09550-2, Kourovka Archive, Problem 19.50: (a) Yes, with a character-theoretic proof in the Archive (each eigenvalue is (1/χ(1)) ∑_{r ∈ R} χ(r), rational since characters take integer values on involutions); (b) Yes, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.involutionCayleyGraphIntegral_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#involution-cayley-graph-integral-holds).

## The 3-cycle Cayley graph of the alternating group is integral

For every $n \ge 3$, let $S$ be
the set of $3$-cycles $(1\,2\,k)$ with $3 \le k \le n$ in the alternating group $A_n$, and let
$R = S \cup S^{-1}$. Then the Cayley graph $\mathrm{Cay}(A_n, R)$, whose vertices are the elements
of $A_n$ with distinct $x$ and $y$ adjacent when $x^{-1} y \in R$ or $y^{-1} x \in R$, is
integral: every eigenvalue of its integer adjacency matrix (every complex root of the
characteristic polynomial of that matrix) is an integer.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.50 (D. V. Lytkina); resolution: (a) D. O. Revin, letter of 21 April 2018; A. Abdollahi, letter of 3 May 2018; (b) W. Guo, D. V. Lytkina, V. D. Mazurov and D. O. Revin, Integral Cayley graphs, Algebra Logic 58 (2019), no. 4, 297-305, doi:10.1007/s10469-019-09550-2, Kourovka Archive, Problem 19.50: (a) Yes, with a character-theoretic proof in the Archive (each eigenvalue is (1/χ(1)) ∑_{r ∈ R} χ(r), rational since characters take integer values on involutions); (b) Yes, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.IntegralCayleyGraphsKourovka19Problem50Wanted.alternatingThreeCycleCayleyGraphIntegral_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegralCayleyGraphsKourovka19Problem50Wanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html#alternating-three-cycle-cayley-graph-int-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral Cayley graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/integral-cayley-graphs)
