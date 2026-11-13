---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimplicialSphereShared.FiniteSimplicialSphere, MathlibExt.Combinatorics.SimplicialSphereShared.faceCount, MathlibExt.Combinatorics.SimplicialSphereShared.extendedFaceCount, MathlibExt.Combinatorics.SimplicialSphereShared.hVector, MathlibExt.Combinatorics.DehnSommervilleWanted.Combinatorics.DehnSommerville.dehn_sommerville
statement: formalized
---

# Face numbers of simplicial spheres

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html).

## Finite simplicial sphere

For a natural number $d$, a finite simplicial $(d-1)$-sphere
is a geometric simplicial complex $K$ in the Euclidean space $\mathbb{R}^d$ with finitely many
faces whose underlying space is homeomorphic to the unit sphere
$S^{d-1} = \{x \in \mathbb{R}^d : \|x\| = 1\}$.

Formalized by `MathlibExt.Combinatorics.SimplicialSphereShared.FiniteSimplicialSphere`, a structure declared in [WantedExt/Combinatorics/SimplicialSphereShared.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimplicialSphereShared.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html#finite-simplicial-sphere).

## Face numbers of a simplicial sphere

For a finite simplicial $(d-1)$-sphere $X$ and a
natural number $k$, $f_k(X)$ is the number of $k$-dimensional faces of $X$, that is, of faces
with exactly $k+1$ vertices.

Formalized by `MathlibExt.Combinatorics.SimplicialSphereShared.faceCount`, a definition declared in [WantedExt/Combinatorics/SimplicialSphereShared.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimplicialSphereShared.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html#face-count).

## Extended face numbers

For a finite simplicial $(d-1)$-sphere $X$ and a natural number
$i$, the $i$-th extended face number of $X$ is $1$ if $i = 0$, and is the number $f_{i-1}(X)$ of
$(i-1)$-dimensional faces of $X$ if $i \ge 1$. Thus it equals $f_{i-1}(X)$ under the convention
$f_{-1}(X) = 1$.

Formalized by `MathlibExt.Combinatorics.SimplicialSphereShared.extendedFaceCount`, a definition declared in [WantedExt/Combinatorics/SimplicialSphereShared.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimplicialSphereShared.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html#extended-face-count).

## The h-vector of a simplicial sphere

For a finite simplicial $(d-1)$-sphere $X$ and a
natural number $j$,

$$h_j(X) = \sum_{i=0}^{j} (-1)^{j-i} \binom{d-i}{j-i} f_{i-1}(X),$$

where $f_{i-1}(X)$ is the number of $(i-1)$-dimensional faces of $X$ for $i \ge 1$,
$f_{-1}(X) = 1$, and $d - i$ is read as $0$ when $i > d$.

Formalized by `MathlibExt.Combinatorics.SimplicialSphereShared.hVector`, a definition declared in [WantedExt/Combinatorics/SimplicialSphereShared.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimplicialSphereShared.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html#h-vector).

## Dehn–Sommerville equations

Let $X$ be a finite simplicial $(d-1)$-sphere, that is, a
finite geometric simplicial complex in $\mathbb{R}^d$ whose underlying space is homeomorphic to
the unit sphere of $\mathbb{R}^d$. Then for every natural number $j \le d$, the h-vector of $X$
satisfies $h_j = h_{d-j}$. Here $h_j = \sum_{i=0}^{j} (-1)^{j-i} \binom{d-i}{j-i} f_{i-1}$,
where $f_{-1} = 1$ and $f_k$ is the number of $k$-dimensional faces of $X$.

## Sources

- M. Dehn (1905); D. M. Y. Sommerville (1927); see Stanley, *Combinatorics and Commutative Algebra*. Knill, *Some fundamental theorems in mathematics*, §142. Problem `dehn_sommerville` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.DehnSommervilleWanted.Combinatorics.DehnSommerville.dehn_sommerville` is written with `theorem_wanted` in [WantedExt/Combinatorics/DehnSommervilleWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DehnSommervilleWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html#dehn-sommerville).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Face numbers of simplicial spheres](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/face-numbers-of-simplicial-spheres)
