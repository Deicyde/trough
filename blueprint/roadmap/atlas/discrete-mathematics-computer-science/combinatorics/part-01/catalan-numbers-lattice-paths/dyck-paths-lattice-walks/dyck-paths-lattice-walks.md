---
declaration: section
origin: cited
lean: MetaMathlibExt.lindstrom_gessel_viennot, MetaMathlibExt.minimal_lattice_walk_count
statement: formalized
proof: formalized
---

# Dyck paths and lattice walks: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/index.html).

Statistics on Dyck paths (peaks, valleys, marked steps, subwords) and their variants (skew, rational, k-box Dyck paths), lattice walks with unit or diagonal steps, Delannoy numbers, Sulanke arrays, colored Dyck paths, and nonintersecting paths via the Lindström–Gessel–Viennot lemma.

## Lindström–Gessel–Viennot lemma

Let $R$ be a commutative ring, let $n$ be a natural
number, and let $E$ be a relation on a type $V$, read as a directed graph on $V$ with an edge
from $u$ to $v$ whenever $E(u, v)$. Suppose there is a function $r : V \to \mathbb{N}$ with
$r(u) < r(v)$ whenever $E(u, v)$, so the graph is acyclic. A path from $u$ to $w$ is a nonempty
list of vertices that starts at $u$, ends at $w$, and in which there is an edge from each vertex
to the next one. Let $A_0, \dots, A_{n-1}$ and $B_0, \dots, B_{n-1}$ be vertices, and suppose
that for all $i, j < n$ the paths from $A_i$ to $B_j$ form a finite set $P_{ij}$. Let $e$ be the
$n \times n$ matrix over $R$ with $e_{ij} = |P_{ij}|$. Suppose further that whenever $i < j$ and
$l < k$, every path from $A_i$ to $B_k$ shares a vertex with every path from $A_j$ to $B_l$. Let
$S$ be the finite set of families $(F_0, \dots, F_{n-1})$ in which each $F_i$ is a path from
$A_i$ to $B_i$ and $F_i$ and $F_j$ share no vertex whenever $i \ne j$. Then the number of
elements of $S$, taken in $R$, equals $\det e$.

## Sources

- https://en.wikipedia.org/wiki/Lindstr%C3%B6m%E2%80%93Gessel%E2%80%93Viennot_lemma

Formalized by `MetaMathlibExt.lindstrom_gessel_viennot`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LindstromGesselViennot.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LindstromGesselViennot.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/index.html#lindstrom-gessel-viennot).

## Minimal lattice walks with unit and diagonal steps

For all natural numbers $a$ and $b$,
the number of sequences of $\max(a, b)$ steps, each taken from $\{(1,0), (0,1), (1,1)\}$,
whose sum is $(a, b)$ equals $\binom{\max(a, b)}{\min(a, b)}$.

Every walk from the origin to $(a, b)$ with these steps has at least $\max(a, b)$ steps, since
each step raises each coordinate by at most $1$, and walks of exactly that length exist; so the
sequences counted are the minimal-length walks from the origin to $(a, b)$.

## Sources

- Jackson Evoniuk, Steven Klee, and Van Magnan, "Enumerating Minimal Length Lattice Paths," Journal of Integer Sequences 21 (2018), Article 18.3.6, Theorem (section Minimal walks for S = {(1,0),(0,1),(1,1)}, label sec2), lines 273–275, https://cs.uwaterloo.ca/journals/JIS/VOL21/Klee/klee2.tex

Formalized by `MetaMathlibExt.minimal_lattice_walk_count`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MinimalLatticeWalkCount.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MinimalLatticeWalkCount.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/index.html#minimal-lattice-walk-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dyck paths and lattice walks](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks)
