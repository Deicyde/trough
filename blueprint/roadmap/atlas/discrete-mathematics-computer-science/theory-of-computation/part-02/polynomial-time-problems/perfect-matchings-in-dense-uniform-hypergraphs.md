---
declaration: section
origin: cited
lean: MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.perfectMatchingProblem, MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.denseHypergraphPerfectMatchingInP, MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.denseHypergraphPerfectMatchingInP_holds
statement: formalized
---

# Perfect matchings in dense uniform hypergraphs

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs/index.html).

## Perfect matching in uniform hypergraphs with a codegree condition

For a natural number
$k$ and a rational $c$, $\mathrm{PM}(k, c)$ is the decision problem on bitstrings that decodes an
input as a pair $(n, E)$ of a natural number $n$ and a list $E$ of lists of natural numbers, and
accepts it iff every list in $E$ consists of $k$ distinct vertices below $n$, $k \mid n$, every
$(k-1)$-element subset of $\{0, \dots, n-1\}$ is contained in at least $cn$ edges of the
hypergraph $H$ whose edges are the vertex sets of the lists in $E$, and $H$ has a perfect
matching, that is, $n/k$ pairwise disjoint edges. Inputs that do not decode are rejected.

Formalized by `MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.perfectMatchingProblem`, a definition declared in [WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs/index.html#perfect-matching-problem).

## Ruciński's question on perfect matchings in dense hypergraphs

The statement that for every
natural number $k \ge 2$ and every rational $c$ with $1/k \le c < 1/2$, the decision problem
$\mathrm{PM}(k, c)$ is in the complexity class P. Here $\mathrm{PM}(k, c)$ accepts a list of edges
of a $k$-uniform hypergraph $H$ on the vertices $0, \dots, n-1$ iff every edge consists of $k$
distinct vertices below $n$, $k \mid n$, every $(k-1)$-element set of vertices lies in at least
$cn$ edges of $H$, and $H$ has a perfect matching; inputs that do not decode are rejected. This is
the positive answer to Ruciński's question (Oberwolfach Combinatorics, Probability and Computing,
2006, Problem 5).

Formalized by `MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.denseHypergraphPerfectMatchingInP`, a definition declared in [WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs/index.html#dense-hypergraph-perfect-matching-in-p).

## Perfect matchings in dense hypergraphs are decidable in polynomial time

Resolved true: Keevash, Knox and Mycroft give a polynomial-time algorithm when the minimum codegree
is at least `n/k + γn` for a fixed `γ > 0`, and Han extends it to minimum codegree at least `n/k`,
so the problem is in `P` for every `1/k ≤ c < 1/2`. Inputs whose edge count is below what the
codegree condition forces are rejected first, so `n` is polynomial in the input size whenever the
remaining checks run. Source: A. Ruciński, in Combinatorics, Probability and Computing, Oberwolfach
Reports 3 (2006), no. 48, p. 2929, Problem 5, DOI 10.4171/OWR/2006/48; resolution: P. Keevash, F.
Knox and R. Mycroft, Polynomial-time perfect matchings in dense hypergraphs, Adv. Math. 269 (2015),
265-334, arXiv:1307.2608 (c > 1/k); J. Han, Decision problem for perfect matchings in dense
k-uniform hypergraphs, Trans. Amer. Math. Soc. 369 (2017), 5197-5218, arXiv:1409.5931 (c = 1/k), KKM
main theorem (codegree ≥ n/k + γn) and Han main theorem (codegree ≥ n/k): polynomial-time decision,
https://arxiv.org/abs/1409.5931.

Stated but not proved: `MathlibExt.Complexity.DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.denseHypergraphPerfectMatchingInP_holds` is written with `theorem_wanted` in [WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/DenseHypergraphPerfectMatchingOWR1386Problem015Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs/index.html#dense-hypergraph-perfect-matching-in-p-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect matchings in dense uniform hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/perfect-matchings-in-dense-uniform-hypergraphs)
