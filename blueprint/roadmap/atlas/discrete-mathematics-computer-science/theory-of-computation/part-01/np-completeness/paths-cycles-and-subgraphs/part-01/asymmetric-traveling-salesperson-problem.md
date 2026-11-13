---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.AsymmetricTspInstance, MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.TourLength, MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.WellFormed, MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.AsymmetricTspFeasible, MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.asymmetricTspDec, MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.asymmetricTsp_npComplete
statement: formalized
---

# Asymmetric traveling salesperson problem

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html).

## Asymmetric TSP instances

An instance of the asymmetric traveling salesperson problem is a
triple $(n, w, B)$ consisting of a natural number $n$ (the number of cities), a weight matrix $w$
given as a list of rows, each row a list of natural numbers, and a natural number $B$ (the
bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.AsymmetricTspInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#asymmetric-tsp-instance).

## Length of a tour in the asymmetric TSP

Let $w$ be a weight matrix, given as a list of rows
of natural numbers, and let $t = (t_0, \dots, t_{L-1})$ be a list of natural numbers. The length
of the tour $t$ under $w$ is $\sum_{j=0}^{L-1} w_{t_j, t_{(j+1) \bmod L}}$, the sum of the weights
along the closed walk including the return edge from $t_{L-1}$ to $t_0$, where $w_{a,b}$ denotes
the entry in row $a$ and column $b$ of $w$, taken to be $0$ when that entry does not exist. In
particular the empty tour has length $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.TourLength`, a definition declared in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#tour-length).

## Well-formed asymmetric TSP instances

An asymmetric TSP instance $(n, w, B)$, with $n$ the
number of cities, $w$ the weight matrix and $B$ the bound, is well formed when $n > 0$, $w$ has
exactly $n$ rows, every row of $w$ has length $n$, and the diagonal entry $w_{a,a}$ in row $a$
and column $a$ is $0$ for every $a < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#well-formed).

## Feasible asymmetric TSP instances

An asymmetric TSP instance $(n, w, B)$ is feasible when
there is a list $t$ of natural numbers with no repeated entries, of length $n$ and containing
every $v < n$ (so $t$ lists the cities $0, \dots, n - 1$ in some order), whose tour length under
$w$ is at most $B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.AsymmetricTspFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#asymmetric-tsp-feasible).

## The asymmetric traveling salesperson decision problem

The asymmetric TSP decision problem
accepts a bitstring $x$ when $x$ decodes, under the canonical bitstring encoding of asymmetric TSP
instances, to an instance $(n, w, B)$ that is well formed and feasible, and rejects $x$
otherwise; in particular it rejects every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.asymmetricTspDec`, a definition declared in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#asymmetric-tsp-dec).

## TRAVELING SALESPERSON (ASYMMETRIC) is NP-complete

The asymmetric traveling salesperson
decision problem belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), TRAVELING SALESPERSON PROBLEM (asymmetric).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.AsymmetricTsp.asymmetricTsp_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/AsymmetricTspWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html#asymmetric-tsp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymmetric traveling salesperson problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/asymmetric-traveling-salesperson-problem)
