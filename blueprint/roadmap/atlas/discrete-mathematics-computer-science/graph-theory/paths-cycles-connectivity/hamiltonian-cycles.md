---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.DiracWanted.dirac, SimpleGraph.IsHamiltonian.of_cyclic_list, MathlibExt.Combinatorics.SimpleGraph.OreWanted.ore, MathlibExt.Combinatorics.PlanarGraphPrismHamiltonicityWanted.conjecture, MathlibExt.Combinatorics.PlanarGraphPrismHamiltonicityWanted.conjecture_refuted
statement: formalized
---

# Hamiltonian cycles

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html).

## Dirac's theorem

Let $G$ be a finite simple graph with $n \ge 3$ vertices in which every
vertex has degree at least $n/2$. Then $G$ is Hamiltonian, that is, it has a cycle that visits
every vertex exactly once.

## Sources

- G. A. Dirac, Some Theorems on Abstract Graphs, Proc. London Math. Soc. s3-2 (1952), 69–81, DOI 10.1112/plms/s3-2.1.69.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.DiracWanted.dirac`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Dirac.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Dirac.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html#dirac).

## A cyclic listing of the vertices gives a Hamiltonian cycle

Let $G$ be a simple graph on a
finite vertex set $V$, and let $v_0, v_1, \dots, v_n$ be a list of vertices with $v_0 = v_n$ in
which $v_{i-1}$ and $v_i$ are adjacent in $G$ for each $1 \le i \le n$. If $v_1, \dots, v_n$ are
pairwise distinct, every vertex of $V$ is among them, and $n \ge 3$, then $G$ is Hamiltonian: it
has a cycle that visits every vertex exactly once.

Formalized by `SimpleGraph.IsHamiltonian.of_cyclic_list`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/HamiltonianCycle.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/HamiltonianCycle.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html#of-cyclic-list).

## Ore's theorem

Let $G$ be a simple graph on a finite vertex set $V$ with $|V| \ge 3$. If
$\deg u + \deg v \ge |V|$ for every pair of distinct nonadjacent vertices $u$ and $v$, then $G$
is Hamiltonian.

## Sources

- O. Ore, Note on Hamilton Circuits, Amer. Math. Monthly 67 (1960), 55, DOI 10.2307/2308928.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.OreWanted.ore`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Ore.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Ore.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html#ore).

## Prism-Hamiltonicity conjecture for 3-connected planar graphs

For every finite simple
graph $G$ that is $3$-vertex-connected and straight-line planar, the prism
$G \mathbin{\square} K_2$, the Cartesian product of $G$ with the complete graph on two
vertices, is Hamiltonian.

Formalized by `MathlibExt.Combinatorics.PlanarGraphPrismHamiltonicityWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PlanarGraphPrismHamiltonicityWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PlanarGraphPrismHamiltonicityWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html#conjecture).

## Špacapan's counterexample to prism-Hamiltonicity

The prism-Hamiltonicity conjecture for
3-connected planar graphs is false: there is a finite simple graph $G$ that is
$3$-vertex-connected and straight-line planar whose prism $G \mathbin{\square} K_2$ is not
Hamiltonian.

## Sources

- S. Špacapan, A counterexample to prism-hamiltonicity of 3-connected planar graphs, Journal of Combinatorial Theory, Series B 148 (2021), 46–52, https://arxiv.org/abs/1906.06683.

Stated but not proved: `MathlibExt.Combinatorics.PlanarGraphPrismHamiltonicityWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PlanarGraphPrismHamiltonicityWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PlanarGraphPrismHamiltonicityWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hamiltonian cycles](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/hamiltonian-cycles)
