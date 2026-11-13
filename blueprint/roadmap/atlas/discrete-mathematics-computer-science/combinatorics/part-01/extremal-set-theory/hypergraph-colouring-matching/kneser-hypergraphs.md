---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.KneserHypergraphColoringErdosProblem780Wanted.kneserHypergraphColoring, MathlibExt.Combinatorics.KneserHypergraphColoringErdosProblem780Wanted.kneserHypergraphColoring_holds
statement: formalized
---

# Kneser hypergraphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/kneser-hypergraphs/index.html).

## Erdős's Kneser hypergraph problem

The statement that for all natural numbers
$n, k, r, t$ with $r \ge 1$, $t \ge 1$ and $n \ge kr + (t - 1)(k - 1)$, every coloring of the
$r$-element subsets of $\{0, \dots, n - 1\}$ with $t$ colors has a color class containing $k$
pairwise disjoint $r$-element subsets.

Formalized by `MathlibExt.Combinatorics.KneserHypergraphColoringErdosProblem780Wanted.kneserHypergraphColoring`, a definition declared in [WantedExt/Combinatorics/KneserHypergraphColoringErdosProblem780Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KneserHypergraphColoringErdosProblem780Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/kneser-hypergraphs/index.html#kneser-hypergraph-coloring).

## Alon–Frankl–Lovász theorem on Kneser hypergraphs

For all natural numbers $n, k, r, t$ with
$r \ge 1$, $t \ge 1$ and $n \ge kr + (t - 1)(k - 1)$, every coloring of the $r$-element subsets
of $\{0, \dots, n - 1\}$ with $t$ colors has a color class containing $k$ pairwise disjoint
$r$-element subsets.

Alon, Frankl and Lovász proved this for all positive $n, k, r, t$ (Theorem 1.1; the case $k = 2$
is Lovász's proof of Kneser's conjecture), and the bound on $n$ is sharp; erdosproblems.com/780
lists the problem as proved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #780, https://www.erdosproblems.com/780 (status PROVED); resolution: N. Alon, P. Frankl and L. Lovász, The chromatic number of Kneser hypergraphs, Trans. Amer. Math. Soc. 298 (1986), 359-370, Theorem 1.1: for positive integers n, k, r, t with n ≥ kr + (t - 1)(k - 1), if the r-subsets of an n-element set are partitioned into t families then one family contains k pairwise disjoint r-sets (conjectured by Erdős in 1973; k = 2 is Kneser's conjecture, proved by Lovász), https://web.math.princeton.edu/~nalon/PDFS/Publications/The%20chromatic%20number%20of%20Kneser%20hypergraphs.pdf.

Stated but not proved: `MathlibExt.Combinatorics.KneserHypergraphColoringErdosProblem780Wanted.kneserHypergraphColoring_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KneserHypergraphColoringErdosProblem780Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KneserHypergraphColoringErdosProblem780Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/kneser-hypergraphs/index.html#kneser-hypergraph-coloring-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kneser hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/kneser-hypergraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/kneser-hypergraphs)
