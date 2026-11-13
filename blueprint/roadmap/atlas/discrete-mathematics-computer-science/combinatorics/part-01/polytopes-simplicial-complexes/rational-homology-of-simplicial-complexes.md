---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsSimplicialComplex, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.facesOfCard, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.boundaryMatrix, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.reducedBetti, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsRationallyAcyclic, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.link, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.topCard, MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsFacet
statement: formalized
proof: formalized
---

# Rational homology of simplicial complexes

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html).

## Finite abstract simplicial complex

A finite family $K$ of finite subsets of
$\mathbb{N}$ is a simplicial complex when it is closed under taking subsets: for every
$\sigma \in K$ and every $\tau \subseteq \sigma$, we have $\tau \in K$.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsSimplicialComplex`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#is-simplicial-complex).

## Faces with a given number of vertices

For a finite family $K$ of finite subsets of
$\mathbb{N}$ and $k \in \mathbb{N}$, the faces of $K$ with $k$ vertices are the members
$\sigma \in K$ with exactly $k$ elements (the faces of dimension $k - 1$).

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.facesOfCard`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#faces-of-card).

## Simplicial boundary matrix

For a finite family $K$ of finite subsets of $\mathbb{N}$ and
$k \in \mathbb{N}$, the boundary matrix $\partial_k$ of $K$ is the matrix over $\mathbb{Q}$ whose
rows are indexed by the faces of $K$ with $k$ vertices and whose columns are indexed by the faces
of $K$ with $k + 1$ vertices; its entry at $(\tau, \sigma)$ is $(-1)^i$ when $\tau$ is obtained
from $\sigma$ by removing its $i$-th smallest vertex, counting from $i = 0$, and $0$ otherwise.

It represents the boundary map from the faces with $k + 1$ vertices to the faces with $k$
vertices. For $k = 0$ it is the augmentation: every vertex has entry $1$ in the row of the empty
face.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.boundaryMatrix`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#boundary-matrix).

## Reduced rational Betti numbers

For a finite family $K$ of finite subsets of $\mathbb{N}$
and $k \in \mathbb{N}$, let $f_k$ be the number of faces of $K$ with $k$ vertices and let
$\partial_k$ be the boundary matrix of $K$ from the faces with $k + 1$ vertices to the faces with
$k$ vertices. The reduced Betti number of $K$ indexed by $k$ is the integer
$f_k - \operatorname{rank} \partial_{k-1} - \operatorname{rank} \partial_k$, with ranks over
$\mathbb{Q}$, where the term $\operatorname{rank} \partial_{k-1}$ is omitted when $k = 0$.

When $K$ is a simplicial complex this is $\dim_{\mathbb{Q}} \tilde H_{k-1}(K; \mathbb{Q})$, the
reduced rational homology in degree $k - 1$, indexed by the number $k$ of vertices of its faces.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.reducedBetti`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#reduced-betti).

## Rationally acyclic complexes

A finite family $K$ of finite subsets of $\mathbb{N}$ is
rationally acyclic when its reduced Betti number indexed by $k$ is $0$ for every $k \in \mathbb{N}$.

For a simplicial complex this says that all reduced rational homology of $K$ vanishes. The void
complex is acyclic; the complex $\{\emptyset\}$ is not, since
$\tilde H_{-1}(\{\emptyset\}; \mathbb{Q}) = \mathbb{Q}$.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsRationallyAcyclic`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#is-rationally-acyclic).

## Link

For a finite family $K$ of finite subsets of $\mathbb{N}$ and a finite set
$F \subseteq \mathbb{N}$, the link of $F$ in $K$ is
$\operatorname{link}_K(F) = \{G \in K \mid G \cap F = \emptyset,\ G \cup F \in K\}$.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.link`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#link).

## Largest face size

For a finite family $K$ of finite subsets of $\mathbb{N}$, the largest
face size of $K$ is the maximum number of elements of a member of $K$, and $0$ when $K$ is empty.

For a nonempty simplicial complex it is $\dim K + 1$; it is $0$ for both the void complex
$\emptyset$ and $\{\emptyset\}$.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.topCard`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#top-card).

## Facet

For a finite family $K$ of finite subsets of $\mathbb{N}$, a finite set
$F \subseteq \mathbb{N}$ is a facet of $K$ when $F \in K$ and $F$ is maximal under inclusion in
$K$: every $G \in K$ with $F \subseteq G$ equals $F$.

Formalized by `MathlibExt.Combinatorics.RationalSimplicialHomologyShared.IsFacet`, a definition declared in [WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RationalSimplicialHomologyShared.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html#is-facet).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rational homology of simplicial complexes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/rational-homology-of-simplicial-complexes)
