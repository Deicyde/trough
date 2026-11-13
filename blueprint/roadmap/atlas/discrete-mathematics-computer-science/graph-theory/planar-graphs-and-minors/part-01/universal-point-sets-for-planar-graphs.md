---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.IsStraightLinePlanarEmbedding, MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.IsUniversalPointSet, MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.ExistsSubquadraticUniversalPointSet, MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.ExistsSubquadraticUniversalPointSet_holds
statement: formalized
---

# Universal point sets for planar graphs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html).

## Universal point sets

## Straight-line planar embedding

A map $p$ from the vertex set of a simple graph $G$ to
$\mathbb{R}^2$ is a crossing-free straight-line embedding of $G$ if $p$ is injective, the closed
segments $[p(u), p(v)]$ and $[p(x), p(y)]$ of any two different edges $uv$ and $xy$ meet only in
points $p(z)$ with $z$ an endpoint of both edges, and no vertex $w$ other than $u$ and $v$ has
$p(w)$ on the segment $[p(u), p(v)]$ of an edge $uv$.

Formalized by `MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.IsStraightLinePlanarEmbedding`, a definition declared in [WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html#is-straight-line-planar-embedding).

## Universal point set for planar graphs

A finite set $P \subseteq \mathbb{R}^2$ is
universal for $n$-vertex planar graphs if every straight-line planar simple graph $G$ on the
vertex set $\{0, \dots, n-1\}$ has a crossing-free straight-line embedding $p$ with $p(v) \in P$
for every vertex $v$.

Formalized by `MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.IsUniversalPointSet`, a definition declared in [WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html#is-universal-point-set).

## Subquadratic universal point sets

The statement that there is a function
$f : \mathbb{N} \to \mathbb{N}$ with $f(n)/n^2 \to 0$ as $n \to \infty$ such that for every $n$
some finite set of at most $f(n)$ points of $\mathbb{R}^2$ is a universal point set for
$n$-vertex planar graphs.

Formalized by `MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.UPSS.ExistsSubquadraticUniversalPointSet`, a definition declared in [WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html#exists-subquadratic-universal-point-set).

## Planar graphs have subquadratic universal point sets

There is a function
$f : \mathbb{N} \to \mathbb{N}$ with $f(n)/n^2 \to 0$ as $n \to \infty$ such that for every $n$
some finite set $P$ of at most $f(n)$ points of $\mathbb{R}^2$ is a universal point set for
$n$-vertex planar graphs: every straight-line planar simple graph on the vertex set
$\{0, \dots, n-1\}$ has a crossing-free straight-line embedding with all its vertices in $P$.

Taylor Gordon (Theorem 1 of the cited preprint) constructs universal point sets of size
$n \exp(O(\sqrt{\log n}))$ for $n$-vertex planar graphs, using small superpatterns and the
reduction of Bannister, Cheng, Devanny and Eppstein.

## Sources

- Taylor Gordon, Almost Linear Universal Point Sets for Planar Graphs, arXiv preprint (2026), arXiv:2609.10916, https://arxiv.org/abs/2609.10916; Michael J. Bannister, Zhanpeng Cheng, William E. Devanny and David Eppstein, Superpatterns and Universal Point Sets, arXiv:1308.0403, https://arxiv.org/abs/1308.0403.

Stated but not proved: `MathlibExt.GraphTheory.UniversalPointSetsSubquadraticWanted.ExistsSubquadraticUniversalPointSet_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/UniversalPointSetsSubquadraticWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html#exists-subquadratic-universal-point-set-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Universal point sets for planar graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/universal-point-sets-for-planar-graphs)
