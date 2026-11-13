---
declaration: section
origin: cited
lean: MetaMathlibExt.kovari_sos_turan, MetaMathlibExt.monomialGraph_girth_eight_classification
statement: formalized
---

# Extremal graph theory: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/index.html).

How many edges or copies of a subgraph a graph can have while avoiding a forbidden structure: Turán and Zarankiewicz problems, saturation, and extremal graphs of given girth.

## Kővári–Sós–Turán bound

Let $m, n, s, t$ be natural numbers with $s \ge 1$ and
$1 \le t \le n$. Let $z(m, n; s, t)$ be the Zarankiewicz number, the largest number of edges in a
bipartite graph with parts of sizes $m$ and $n$ that contains no copy of the complete bipartite
graph $K_{s,t}$. Then

$$z(m, n; s, t) \le (s - 1)^{1/t} (n - t + 1) m^{1 - 1/t} + (t - 1) m.$$

Proof: Double-count common right neighborhoods, apply the power-mean inequality, and take a real
$t$-th root, following Kővári–Sós–Turán (1954) and Jukna, Theorem 2.10.

## Sources

- https://en.wikipedia.org/wiki/Zarankiewicz_problem.

Formalized by `MetaMathlibExt.kovari_sos_turan`, a theorem declared in [MathlibExt/Combinatorics/Graph/KovariSosTuran.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Graph/KovariSosTuran.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/index.html#kovari-sos-turan).

## Monomial graphs of girth eight

Let $p$ be an odd prime, $e$ a natural number, $q = p^e$, and
$\mathbb{F}$ a field with $q$ elements, and suppose that either $p \ge 5$ and $e = 2^a 3^b$ for
some natural numbers $a, b$, or $3 \le q \le 10^{10}$. For natural numbers $m_2, n_2, m_3, n_3$,
let $G$ be the bipartite graph with two copies of $\mathbb{F}^3$ as its parts, in which
$(x_1, x_2, x_3)$ in the first part is adjacent to $(y_1, y_2, y_3)$ in the second part exactly
when $x_2 + y_2 = x_1^{m_2} y_1^{n_2}$ and $x_3 + y_3 = x_1^{m_3} y_1^{n_3}$, and let $\Gamma_3$
be the graph defined in the same way by $x_2 + y_2 = x_1 y_1$ and $x_3 + y_3 = x_1 y_1^2$. If
the girth of $G$ is at least $8$, then $G$ is isomorphic to $\Gamma_3$ and the girth of $G$ is
exactly $8$.

## Sources

- V. Dmytrenko, F. Lazebnik, and J. Williford, "On monomial graphs of girth eight", Finite Fields Appl. 13 (2007), 828–842, Theorem 3.

Stated but not proved: `MetaMathlibExt.monomialGraph_girth_eight_classification` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/MonomialGraphClassificationWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/MonomialGraphClassificationWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/index.html#monomial-graph-girth-eight-classificatio).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extremal graph theory](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory)
