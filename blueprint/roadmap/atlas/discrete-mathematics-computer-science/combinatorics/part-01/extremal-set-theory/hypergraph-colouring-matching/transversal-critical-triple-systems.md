---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.transversalCriticalMinDegreeSeven, MathlibExt.Combinatorics.TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.transversalCriticalMinDegreeSeven_refuted
statement: formalized
---

# Transversal-critical triple systems

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/transversal-critical-triple-systems/index.html).

## Erdős Problem 834 for transversal-critical triple systems

There exist $n \in \mathbb{N}$
and a $3$-uniform hypergraph $H$ on the vertex set $\{0, \dots, n-1\}$ such that some set of at
most $3$ vertices meets every edge of $H$, no set of at most $2$ vertices meets every edge of $H$,
for every edge $e$ of $H$ some set of at most $2$ vertices meets every edge of $H$ other than $e$,
and every vertex lies in at least $7$ edges of $H$.

Writing $\tau$ for the least size of a vertex set meeting every edge and $H - e$ for $H$ with the
edge $e$ removed, this asks for $\tau(H) = 3$ and $\tau(H - e) \le 2$ for every edge $e$, with
every vertex of degree at least $7$.

Formalized by `MathlibExt.Combinatorics.TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.transversalCriticalMinDegreeSeven`, a definition declared in [WantedExt/Combinatorics/TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/transversal-critical-triple-systems/index.html#transversal-critical-min-degree-seven).

## Erdős Problem 834 fails for transversal-critical triple systems

There are no
$n \in \mathbb{N}$ and $3$-uniform hypergraph $H$ on the vertex set $\{0, \dots, n-1\}$ such that
some set of at most $3$ vertices meets every edge of $H$, no set of at most $2$ vertices meets
every edge of $H$, for every edge $e$ of $H$ some set of at most $2$ vertices meets every edge of
$H$ other than $e$, and every vertex lies in at least $7$ edges of $H$.

Writing $\tau(H)$ for the least size of a vertex set meeting every edge of $H$ and $H - e$ for
$H$ with the edge $e$ removed, Li proved that a $3$-uniform hypergraph $H$ with $\tau(H) = 3$ and
$\tau(H - e) = 2$ for every edge $e$ has at most $10$ edges, so some vertex has degree at most $6$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #834, https://www.erdosproblems.com/834 (status SOLVED); resolution: R. Li, On an Erdős-Lovász problem: 3-critical 3-graphs of minimum degree 7, arXiv:2512.24850 (2025; unrefereed, accepted on erdosproblems.com/834), abstract and main theorem for the transversal interpretation: a 3-uniform hypergraph H with τ(H) = 3 and τ(H - e) = 2 for every edge e has at most 10 edges, in particular δ(H) ≤ 6, sharp for K₅⁽³⁾; erdosproblems.com/834: 'In the first formulation ... Li proves that a 3-critical 3-uniform hypergraph must have a vertex of degree ≤ 6', https://arxiv.org/abs/2512.24850.

Stated but not proved: `MathlibExt.Combinatorics.TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.transversalCriticalMinDegreeSeven_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransversalCriticalTripleSystemDegreeErdosProblem834Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/transversal-critical-triple-systems/index.html#transversal-critical-min-degree-seven-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transversal-critical triple systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/transversal-critical-triple-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/transversal-critical-triple-systems)
