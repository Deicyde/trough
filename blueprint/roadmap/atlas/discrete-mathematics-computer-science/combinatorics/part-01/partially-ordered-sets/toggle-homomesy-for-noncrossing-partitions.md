---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.ArcSet, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.IsNoncrossingArcSet, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggle, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggleOrder, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggleComposite, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.blockCount, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.noncrossingToggleBlockHomomesy, MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.noncrossingToggleBlockHomomesy_holds
statement: formalized
---

# Toggle homomesy for noncrossing partitions

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html).

## Arc sets

For a natural number $n$, an arc set on $n$ points is a finite set of ordered
pairs $(i, j)$, called arcs, with $i, j \in \{0, 1, \dots, n - 1\}$.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.ArcSet`, an abbreviation declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#arc-set).

## Noncrossing arc sets

An arc set $P$ on $n$ points is noncrossing when every arc
$(i, j) \in P$ has $i < j$ and any two distinct arcs $(i, j)$ and $(k, l)$ of $P$ satisfy
$i \ne k$, $j \ne l$, and not $i < k < j < l$. So distinct arcs do not cross and share
neither a left nor a right endpoint.

These arc sets are the linear representations of the noncrossing partitions of
$\{0, 1, \dots, n - 1\}$, in which the arcs join consecutive elements of each block.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.IsNoncrossingArcSet`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#is-noncrossing-arc-set).

## Toggle at an arc

For an arc $a = (i, j)$ and an arc set $P$ on $n$ points, the toggle
$\tau_{i,j}$ sends $P$ to $P \setminus \{a\}$ if $a \in P$; otherwise to $P \cup \{a\}$ if
$P \cup \{a\}$ is a noncrossing arc set; and otherwise it leaves $P$ unchanged.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggle`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#toggle).

## Toggle order

For a natural number $n$, the toggle order on $n$ points is the list of all
arcs $(i, i + d)$ with $d \ge 1$, $i \ge 0$ and $i + d \le n - 1$, ordered by length
$d = 1, \dots, n - 1$ and, for each length, by increasing left endpoint $i$. In $1$-indexed form it
is $(1,2), (2,3), \dots, (n-1,n), (1,3), \dots, (n-2,n), \dots, (1,n)$.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggleOrder`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#toggle-order).

## Toggle composite

The toggle composite $\sigma$ on $n$ points sends an arc set $P$ on $n$
points to the arc set obtained from $P$ by applying the toggles $\tau_{i,j}$ at the arcs
$(i, j)$ of the toggle order on $n$ points one after another, in the order of that list.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.toggleComposite`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#toggle-composite).

## Block count

The block count of an arc set $P$ on $n$ points is $n - |P|$, where the
subtraction is truncated at $0$.

When $P$ is a noncrossing arc set, this is the number of blocks of the noncrossing partition whose
linear representation is $P$.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.blockCount`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#block-count).

## Block-count homomesy claim for toggling noncrossing partitions

Let $\sigma_n$ be the
toggle composite on $n$ points and $\sigma_n^k$ its $k$-fold iterate. The claim states that for
every $n \ge 1$, every noncrossing arc set $P$ on $n$ points and every $L \ge 1$ with
$\sigma_n^L(P) = P$, twice the sum of the block counts of
$P, \sigma_n(P), \dots, \sigma_n^{L-1}(P)$ equals $L(n + 1)$. That is, the number of blocks is
homomesic under $\sigma_n$ with average $(n + 1)/2$.

## Sources

- AIM workshop Dynamical algebraic combinatorics, pre-workshop document, §5.4, Conjecture 5.8.

Formalized by `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.noncrossingToggleBlockHomomesy`, a definition declared in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#noncrossing-toggle-block-homomesy).

## Block-count homomesy for toggling noncrossing partitions

The block-count homomesy claim
holds: with $\sigma_n$ the toggle composite on $n$ points and $\sigma_n^k$ its $k$-fold iterate,
for every $n \ge 1$, every noncrossing arc set $P$ on $n$ points and every $L \ge 1$ with
$\sigma_n^L(P) = P$, twice the sum of the block counts of
$P, \sigma_n(P), \dots, \sigma_n^{L-1}(P)$ equals $L(n + 1)$.

## Sources

- AIM workshop Dynamical algebraic combinatorics, pre-workshop document, http://aimath.org/pastworkshops/dac_preworkshop.pdf, §5.4, Conjecture 5.8; resolution: D. Einstein, M. Farber, E. Gunawan, M. Joseph, M. Macauley, J. Propp and S. Rubinstein-Salzedo, Noncrossing partitions, toggles, and homomesies, Electron. J. Combin. 23 (2016), no. 3, Paper 3.52, arXiv:1510.06362, Theorem 4.5 and Corollary 4.7: for every partial Coxeter element w of the toggle group (each toggle τ_{i,j} at most once) containing every τ_{i,i+1}, in particular every Coxeter element, the block count β is (n + 1)/2-mesic on NC(n); σ toggles every arc exactly once, https://doi.org/10.37236/5648.

Stated but not proved: `MathlibExt.Combinatorics.NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.noncrossingToggleBlockHomomesy_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoncrossingToggleBlockHomomesyAIMOtherProblem36Wanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html#noncrossing-toggle-block-homomesy-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Toggle homomesy for noncrossing partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/partially-ordered-sets/toggle-homomesy-for-noncrossing-partitions)
