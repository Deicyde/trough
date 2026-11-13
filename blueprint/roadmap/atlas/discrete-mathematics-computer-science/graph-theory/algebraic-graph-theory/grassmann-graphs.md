---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.GrVertex, MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.Gr, MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.SubGr, MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.Φ, MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.theorem_1_12
statement: formalized
---

# Grassmann graphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html).

## Vertices of the Grassmann graph

For natural numbers $k$ and $\ell$, the vertices of the
Grassmann graph $\mathrm{Gr}(k, \ell)$ are the $\ell$-dimensional linear subspaces of
$\mathbb{F}_2^k$.

Formalized by `MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.GrVertex`, an abbreviation declared in [WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html#gr-vertex).

## Grassmann graph over $\mathbb{F}_2$

For natural numbers $k$ and $\ell$, the Grassmann
graph $\mathrm{Gr}(k, \ell)$ has as vertices the $\ell$-dimensional linear subspaces of
$\mathbb{F}_2^k$, and two distinct such subspaces $L$ and $L'$ are adjacent when
$\dim(L \cap L') = \ell - 1$.

Formalized by `MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.Gr`, a definition declared in [WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html#gr).

## Grassmann vertices between two subspaces

For natural numbers $k$ and $\ell$ and linear
subspaces $A$ and $B$ of $\mathbb{F}_2^k$, $\mathrm{Gr}(k, \ell)[A, B]$ is the finite set of
vertices $L$ of the Grassmann graph $\mathrm{Gr}(k, \ell)$, that is of $\ell$-dimensional
subspaces of $\mathbb{F}_2^k$, with $A \subseteq L \subseteq B$. If $A \not\subseteq B$ the set
is empty.

This is the set $\mathrm{Gr}_{k,\ell}[A, B]$ on page 13 of Khot, Minzer and Safra, Pseudorandom
sets in Grassmann graph have near-perfect expansion.

Formalized by `MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.SubGr`, a definition declared in [WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html#sub-gr).

## Edge expansion of a vertex set

Let $G$ be a simple graph on a finite vertex set $V$ and
let $S \subseteq V$ be nonempty. Let $d$ be the degree in $G$ of a fixed vertex of $S$, chosen
once for each $S$. The expansion of $S$ is the rational number
$\Phi_G(S) = |E(S, V \setminus S)| / (d \cdot |S|)$, where $E(S, V \setminus S)$ is the set of
edges of $G$ with one endpoint in $S$ and the other in $V \setminus S$; it is $0$ when $d = 0$.

For a $d$-regular graph, $d$ is the common degree and this is Definition 1.8 of Khot, Minzer and
Safra, which also asks that $|S| \le |V|/2$; neither regularity nor that bound is assumed here.

Formalized by `MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.Φ`, a definition declared in [WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html#untitled).

## Non-expanding sets in the Grassmann graph (Khot–Minzer–Safra)

For every real $\alpha$
with $0 < \alpha < 1$ there are a real $\varepsilon > 0$ and a natural number $r$ such that for
all sufficiently large natural numbers $\ell$ and, for each such $\ell$, all sufficiently large
natural numbers $k$, the following holds. For subspaces $A$ and $B$ of $\mathbb{F}_2^k$, let
$\mathrm{Gr}(k, \ell)[A, B]$ be the set of vertices $L$ of the Grassmann graph
$\mathrm{Gr}(k, \ell)$ with $A \subseteq L \subseteq B$. Let $S$ be a nonempty set of at most
half of the vertices of $\mathrm{Gr}(k, \ell)$ whose edge expansion in $\mathrm{Gr}(k, \ell)$
satisfies $\Phi(S) \le \alpha$. Then there are subspaces $A \subseteq B$ of $\mathbb{F}_2^k$
such that the dimension of $A$ plus the codimension $k - \dim B$ of $B$ is at most $r$ and
$|S \cap \mathrm{Gr}(k, \ell)[A, B]| / |\mathrm{Gr}(k, \ell)[A, B]| \ge \varepsilon$.

## Sources

- S. Khot, D. Minzer, and M. Safra, `Pseudorandom sets in Grassmann graph have near-perfect expansion`, Annals of Math, 198 (1) 2023. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_pseudorandom_grassmann` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.PseudorandomGrassmannWanted.PseudorandomGrassmann.theorem_1_12` is written with `theorem_wanted` in [WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PseudorandomGrassmannWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html#theorem-1-12).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Grassmann graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/grassmann-graphs)
