---
declaration: section
origin: cited
lean: Combinatorics.Line.reindex, Combinatorics.Line.reindex_apply, Combinatorics.Subspace.comp, Combinatorics.Subspace.comp_apply, Combinatorics.Subspace.compLine, Combinatorics.Subspace.compLine_apply, Combinatorics.Subspace.reindex_compLine, Combinatorics.Subspace.comp_compLine
statement: formalized
proof: formalized
---

# Density Hales–Jewett theorem

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html).

## Line

## Reindexing a combinatorial line

A combinatorial line $l$ in $\alpha^\iota$ assigns to each
coordinate $i \in \iota$ either a fixed value in $\alpha$ or the free variable, with at least one
free coordinate. Given a bijection $e : \iota \to \iota'$, the reindexing of $l$ along $e$ is the
combinatorial line in $\alpha^{\iota'}$ that assigns to each coordinate $j \in \iota'$ what $l$
assigns to the coordinate $e^{-1}(j)$.

Formalized by `Combinatorics.Line.reindex`, a definition declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#reindex).

## Points of a reindexed line

Let $l$ be a combinatorial line in $\alpha^\iota$, let
$e : \iota \to \iota'$ be a bijection, and for $a \in \alpha$ write $l(a) \in \alpha^\iota$ for the
point of $l$ whose free coordinates equal $a$. Then for every $a \in \alpha$ and every
$j \in \iota'$, the $j$-th coordinate of the point at $a$ of the reindexing of $l$ along $e$ equals
the $e^{-1}(j)$-th coordinate of $l(a)$.

Formalized by `Combinatorics.Line.reindex_apply`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#reindex-apply).

## Composition of combinatorial subspaces

A combinatorial subspace $V$ of $\alpha^\iota$ with
parameter set $\eta$ assigns to each coordinate $i \in \iota$ either a fixed value in $\alpha$ or a
parameter in $\eta$, with every parameter assigned to some coordinate. Let $V$ be such a subspace
and let $W$ be a combinatorial subspace of $\alpha^\eta$ with parameter set $\eta'$. The composite
$V \circ W$ is the combinatorial subspace of $\alpha^\iota$ with parameter set $\eta'$ that assigns
to a coordinate $i$ the fixed value $a$ if $V$ assigns $a$ to $i$, and assigns to $i$ what $W$
assigns to the coordinate $e \in \eta$ if $V$ assigns the parameter $e$ to $i$.

Formalized by `Combinatorics.Subspace.comp`, a definition declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#comp).

## Evaluating a composite subspace

Let $V$ be a combinatorial subspace of $\alpha^\iota$ with
parameter set $\eta$ and let $W$ be a combinatorial subspace of $\alpha^\eta$ with parameter set
$\eta'$; view each subspace as its map from parameter values to points. Then for every
$x \in \alpha^{\eta'}$, the composite $V \circ W$ sends $x$ to $V(W(x))$.

Formalized by `Combinatorics.Subspace.comp_apply`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#comp-apply).

## Image of a combinatorial line in a combinatorial subspace

Let $V$ be a combinatorial
subspace of $\alpha^\iota$ with parameter set $\eta$ and let $l$ be a combinatorial line in
$\alpha^\eta$. The image $V_* l$ is the combinatorial line in $\alpha^\iota$ that has the fixed
value $a$ at each coordinate $i$ to which $V$ assigns the fixed value $a$, and has at each
coordinate $i$ to which $V$ assigns a parameter $e \in \eta$ what $l$ has at the coordinate $e$
(the free variable or a fixed value).

Formalized by `Combinatorics.Subspace.compLine`, a definition declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#comp-line).

## Points of the image of a line

Let $V$ be a combinatorial subspace of $\alpha^\iota$ with
parameter set $\eta$, viewed as its map $x \mapsto V(x)$ from parameter values to points, and let
$l$ be a combinatorial line in $\alpha^\eta$, with $l(a)$ the point of $l$ whose free coordinates
equal $a$. Then for every $a \in \alpha$, the point at $a$ of the image line $V_* l$ is
$V(l(a))$.

Formalized by `Combinatorics.Subspace.compLine_apply`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#comp-line-apply).

## Reindexing commutes with images of lines

Let $V$ be a combinatorial subspace of
$\alpha^\iota$ with parameter set $\eta$, let $e : \iota \to \iota'$ be a bijection, and let $l$ be
a combinatorial line in $\alpha^\eta$. Let $V^e$ be the combinatorial subspace of $\alpha^{\iota'}$
with parameter set $\eta$ that assigns to each coordinate $j \in \iota'$ what $V$ assigns to the
coordinate $e^{-1}(j)$. Then the image of $l$ under $V^e$ is the reindexing along $e$ of the image
of $l$ under $V$.

Formalized by `Combinatorics.Subspace.reindex_compLine`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#reindex-comp-line).

## Images of lines under composite subspaces

Let $V$ be a combinatorial subspace of
$\alpha^\iota$ with parameter set $\eta$, let $W$ be a combinatorial subspace of $\alpha^\eta$ with
parameter set $\eta'$, and let $l$ be a combinatorial line in $\alpha^{\eta'}$. Then the image of
$l$ under the composite $V \circ W$ equals the image under $V$ of the image of $l$ under $W$, that
is, $(V \circ W)_* l = V_*(W_* l)$.

Formalized by `Combinatorics.Subspace.comp_compLine`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#comp-comp-line).

## Graham–Rothschild theorem for combinatorial lines

Let $\alpha$ be a finite nonempty alphabet,
let $\kappa$ be a finite nonempty set of colors and let $m$ be a natural number. Then there is a
natural number $N$ such that for every coloring $C$ of the combinatorial lines in $\alpha^N$ with
colors in $\kappa$ there are a combinatorial subspace $V$ of $\alpha^N$ with parameter set
$\{0, \dots, m - 1\}$ and a color $z \in \kappa$ such that for every combinatorial line $l$ in
$\alpha^m$, the image $V_* l$ of $l$ in $V$ satisfies $C(V_* l) = z$.

Formalized by `Combinatorics.Subspace.exists_lines_mono_in_high_dimension_fin`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#exists-lines-mono-in-high-dimension-fin).

## Density Hales–Jewett theorem

Write $[k] = \{0, 1, \dots, k - 1\}$. A combinatorial line in
$[k]^N$ is given by a nonempty set of free coordinates and a fixed value in $[k]$ at every other
coordinate; its $k$ points are obtained by giving all free coordinates a common value $a \in [k]$.
For every natural number $k \ge 2$ and every real $\delta > 0$ there is a natural number $N$ such
that every set $A \subseteq [k]^N$ with $\delta k^N \le |A|$ contains all $k$ points of some
combinatorial line in $[k]^N$.

Proof: We follow the density-increment route of Dodos–Kanellopoulos–Tyros, with the binary
case supplied by Sperner's theorem and the Graham–Rothschild theorem for lines.

## Sources

- H. Furstenberg and Y. Katznelson, J. Anal. Math. 57 (1991) and Hales-Jewett, Trans. AMS 106 (1963); Lean states finitary density form over `Fin N → Fin k` with coloring version as corollary.

Formalized by `MathlibExt.Combinatorics.DensityHalesJewettWanted.density_hales_jewett`, a theorem declared in [MathlibExt/Combinatorics/DensityHalesJewett.lean, line 5127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/DensityHalesJewett.lean#L5127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html#density-hales-jewett).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Density Hales–Jewett theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/density-hales-jewett-theorem)
