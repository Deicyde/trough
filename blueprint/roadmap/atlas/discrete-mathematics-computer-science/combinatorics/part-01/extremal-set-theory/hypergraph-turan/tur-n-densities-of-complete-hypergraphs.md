---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.completeHypergraphEdges, MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanNumber, MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanDensityRatio, MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanDensityComplete, MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.conjecture, MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.conjecture_refuted
statement: formalized
---

# Turán densities of complete hypergraphs

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html).

## Edges of the complete uniform hypergraph

For natural numbers $k$ and $m$, the edge
family of the complete $k$-uniform hypergraph on the vertex set $\{0, 1, \dots, m-1\}$ is the
family of all $k$-element subsets of $\{0, 1, \dots, m-1\}$.

## Sources

- [AIM-COMBINATORICS-0149], aim-combinatorics-notes.json notes[148], Source item 11.3, Section Complete hypergraphs, Workshop Hypergraph Turan problem, Source URL http://aimpl.org/hypergraphturan/1/.

Formalized by `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.completeHypergraphEdges`, a definition declared in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#complete-hypergraph-edges).

## Turán number of the complete $k$-graph on $k+1$ vertices

For natural numbers $k$ and
$n$, let $K_{k+1}^{(k)}$ be the complete $k$-uniform hypergraph on the vertex set
$\{0, 1, \dots, k\}$, whose edges are all $k$-element subsets of that set. The Turán number
$\mathrm{ex}(n, K_{k+1}^{(k)})$ is the largest size of a family $E$ of $k$-element subsets of
$\{0, 1, \dots, n-1\}$ that contains no copy of $K_{k+1}^{(k)}$, that is, for which there is no
injective map $f \colon \{0, 1, \dots, k\} \to \{0, 1, \dots, n-1\}$ such that the image under
$f$ of every edge of $K_{k+1}^{(k)}$ belongs to $E$.

## Sources

- [AIM-COMBINATORICS-0149], aim-combinatorics-notes.json notes[148], Source item 11.3, Section Complete hypergraphs, Workshop Hypergraph Turan problem, Source URL http://aimpl.org/hypergraphturan/1/.

Formalized by `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanNumber`, a definition declared in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#turan-number).

## Turán density ratio

For natural numbers $k$ and $n$, the Turán density ratio is the
real number $\mathrm{ex}(n, K_{k+1}^{(k)}) / \binom{n}{k}$, where
$\mathrm{ex}(n, K_{k+1}^{(k)})$ is the Turán number of the complete $k$-uniform hypergraph
$K_{k+1}^{(k)}$ on $k+1$ vertices, the largest number of $k$-element subsets of an $n$-element
set containing no copy of $K_{k+1}^{(k)}$. The ratio is defined to be $0$ when
$\binom{n}{k} = 0$, that is, when $n < k$.

## Sources

- [AIM-COMBINATORICS-0149], aim-combinatorics-notes.json notes[148], Source item 11.3, Section Complete hypergraphs, Workshop Hypergraph Turan problem, Source URL http://aimpl.org/hypergraphturan/1/.

Formalized by `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanDensityRatio`, a definition declared in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#turan-density-ratio).

## Turán density of the complete $k$-graph on $k+1$ vertices

For a natural number $k$,
the Turán density $\pi(K_{k+1}^{(k)})$ of the complete $k$-uniform hypergraph $K_{k+1}^{(k)}$
on $k+1$ vertices is the limit superior, as $n \to \infty$, of the Turán density ratios
$\mathrm{ex}(n, K_{k+1}^{(k)}) / \binom{n}{k}$, where $\mathrm{ex}(n, K_{k+1}^{(k)})$ is the
Turán number of $K_{k+1}^{(k)}$ and the ratio is taken to be $0$ when $\binom{n}{k} = 0$.

## Sources

- [AIM-COMBINATORICS-0149], aim-combinatorics-notes.json notes[148], Source item 11.3, Section Complete hypergraphs, Workshop Hypergraph Turan problem, Source URL http://aimpl.org/hypergraphturan/1/.

Formalized by `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.turanDensityComplete`, a definition declared in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#turan-density-complete).

## De Caen's conjecture on Turán densities of complete hypergraphs

For a natural number
$k$, let $\pi(K_{k+1}^{(k)})$ be the Turán density of the complete $k$-uniform hypergraph on
$k+1$ vertices. De Caen's conjecture asserts that $k \, (1 - \pi(K_{k+1}^{(k)})) \to \infty$
as $k \to \infty$.

## Sources

- [AIM-COMBINATORICS-0149], aim-combinatorics-notes.json notes[148], Source item 11.3, Section Complete hypergraphs, Workshop Hypergraph Turan problem, Source URL http://aimpl.org/hypergraphturan/1/.

Formalized by `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#conjecture).

## De Caen's conjecture is false

It is not the case that $k \, (1 - \pi(K_{k+1}^{(k)}))$
tends to $\infty$ as $k \to \infty$, where $\pi(K_{k+1}^{(k)})$ is the Turán density of the
complete $k$-uniform hypergraph $K_{k+1}^{(k)}$ on $k+1$ vertices.

Pikhurko (Adv. Math. 464 (2025) 110148, Theorem 1.1) proves
$T(n, k+1, k) \le \frac{6.239}{k+1} \binom{n}{k}$ for all $n > k \ge 1$, where $T(n, k+1, k)$
is the least number of $k$-element subsets of an $n$-element set such that every
$(k+1)$-element subset contains one of them; hence $k \, (1 - \pi(K_{k+1}^{(k)})) \le 6.239$
for every $k \ge 1$, and the paper states that this disproves de Caen's conjecture.

## Sources

- O. Pikhurko, Constructions of Turán systems that are tight up to a multiplicative constant, Advances in Mathematics 464 (2025), 110148, https://pikhurko.github.io/E/Pikhurko25am.pdf.

Stated but not proved: `MathlibExt.Combinatorics.DeCaenTuranDefectGrowthWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DeCaenTuranDefectGrowthWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán densities of complete hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-densities-of-complete-hypergraphs)
