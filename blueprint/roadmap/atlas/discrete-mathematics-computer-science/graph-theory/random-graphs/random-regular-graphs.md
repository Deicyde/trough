---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.regularGraphs, MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.ratioDeviationProb, MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.independenceRatioConverges, MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.independenceRatioConverges_holds, MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.nonsingularFraction, MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.regularGraphAdjacencyNonsingular, MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.regularGraphAdjacencyNonsingular_holds
statement: formalized
---

# Random regular graphs

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html).

## Regular simple graphs on a labelled vertex set

For natural numbers $n$ and $d$, the
finite set of all $d$-regular simple graphs on the vertex set $\{0, \dots, n - 1\}$; the uniformly
random $d$-regular graph on $n$ vertices is uniform on this set. It is empty when $nd$ is odd or
$1 \le n \le d$.

Formalized by `MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.regularGraphs`, a definition declared in [WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#regular-graphs).

## Deviation probability of the independence ratio of a random regular graph

For natural
numbers $n$ and $d$ and real numbers $c$ and $\varepsilon$, the probability that the independence
ratio $\alpha(G)/n$ of a uniformly random $d$-regular simple graph $G$ on the vertex set
$\{0, \dots, n - 1\}$ differs from $c$ by more than $\varepsilon$, where $\alpha(G)$ is the
independence number of $G$: the number of $d$-regular simple graphs $G$ on this vertex set with
$|\alpha(G)/n - c| > \varepsilon$ divided by the number of all $d$-regular simple graphs on it,
or $0$ when there is no $d$-regular simple graph on it. For $n = 0$ the ratio $\alpha(G)/n$ is
read as $0$.

Formalized by `MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.ratioDeviationProb`, a definition declared in [WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#ratio-deviation-prob).

## Bollobás's question on the independence ratio of random regular graphs

The statement
that for every integer $d \ge 1$ there is a real number $c$ such that, for every $\varepsilon > 0$,
the probability that the independence ratio $\alpha(G)/n$ of a uniformly random $d$-regular simple
graph $G$ on the vertex set $\{0, \dots, n - 1\}$ differs from $c$ by more than $\varepsilon$
tends to $0$ as $n \to \infty$. Here $\alpha(G)$ is the independence number of $G$, the largest
size of an independent set of vertices, and the probability is taken to be $0$ for the $n$ with
no $d$-regular simple graph on $n$ vertices.

The question whether this holds is due to Bollobás and is Question 18 in Abért's list of problems.

Formalized by `MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.independenceRatioConverges`, a definition declared in [WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#independence-ratio-converges).

## The independence ratio of random regular graphs converges

For every integer $d \ge 1$
there is a real number $c$ such that, for every $\varepsilon > 0$, the probability that the
independence ratio $\alpha(G)/n$ of a uniformly random $d$-regular simple graph $G$ on the vertex
set $\{0, \dots, n - 1\}$ differs from $c$ by more than $\varepsilon$ tends to $0$ as
$n \to \infty$. Here $\alpha(G)$ is the independence number of $G$, the largest size of an
independent set of vertices, and the probability is taken to be $0$ for the $n$ with no
$d$-regular simple graph on $n$ vertices.

## Sources

- M. Abért, Some questions (2010), Question 18 (B. Bollobás), https://www.renyi.hu/~abert/questions.pdf; resolution: M. Bayati, D. Gamarnik and P. Tetali, Combinatorial approach to the interpolation method and scaling limits in sparse random graphs, Ann. Probab. 41 (2013), no. 3, 1803-1826, DOI 10.1214/12-AOP816, arXiv:0912.2444, Theorem 3: for every r and every model of §2 (independent sets included, H(G) = size of a largest independent set) there is H(r) with lim N^{-1} H(G(N, r)) = H(r) w.h.p. (N along Nr even); §1: G(N, r) is chosen uniformly from the r-regular graphs on N nodes and the result resolves the question whether |I_N|/N converges in probability; §2: results proved w.h.p. for the configuration model carry over to simple regular graphs, https://arxiv.org/abs/0912.2444.

Stated but not proved: `MathlibExt.Combinatorics.RandomRegularIndependenceRatioAMR11Problem0018Wanted.independenceRatioConverges_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomRegularIndependenceRatioAMR11Problem0018Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#independence-ratio-converges-holds).

## Proportion of regular graphs with nonsingular adjacency matrix

For natural numbers $d$
and $n$, this is the real number obtained by dividing the number of $d$-regular simple graphs on
the vertex set $\{0, 1, \ldots, n-1\}$ whose adjacency matrix has nonzero determinant over
$\mathbb{Q}$ by the number of all $d$-regular simple graphs on that vertex set; it is $0$ when
there is no $d$-regular simple graph on that vertex set. It is the probability that the adjacency
matrix of the uniformly random $d$-regular graph $G(n, d)$ is nonsingular.

Nonsingularity over $\mathbb{Q}$ is the same as nonsingularity over $\mathbb{R}$.

Formalized by `MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.nonsingularFraction`, a definition declared in [WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#nonsingular-fraction).

## Vu's problem on nonsingular adjacency matrices of random regular graphs

This is the
statement that for every natural number $d \ge 3$, the probability that the adjacency matrix of
the uniformly random $d$-regular simple graph on $n$ labeled vertices is nonsingular tends to $1$
as $n \to \infty$, where $n$ runs over the natural numbers with $nd$ even. Here the probability is
the proportion of the $d$-regular simple graphs on $\{0, 1, \ldots, n-1\}$ whose adjacency matrix
has nonzero determinant over $\mathbb{Q}$.

The restriction to $nd$ even is natural: $d$-regular graphs on $n$ vertices exist only for such
$n$.

Formalized by `MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.regularGraphAdjacencyNonsingular`, a definition declared in [WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#regular-graph-adjacency-nonsingular).

## Nonsingularity of adjacency matrices of random regular graphs

For every natural number
$d \ge 3$, the probability that the adjacency matrix of the uniformly random $d$-regular simple
graph on $n$ labeled vertices has nonzero determinant (over $\mathbb{Q}$, equivalently over
$\mathbb{R}$) tends to $1$ as $n \to \infty$ along the natural numbers $n$ with $nd$ even.

Huang proved more: for every fixed $d \ge 3$ there is $c > 0$ such that the adjacency matrix of a
random $d$-regular directed or undirected graph on $n$ vertices is singular with probability at
most $n^{-c}$ for all large $n$, in the configuration model and, by contiguity, in the uniform
model.

## Sources

- V. Vu, problem (1) of the problem session, in Combinatorics, Oberwolfach Reports 11 (2014), Report 01/2014, pp. 84-85, DOI 10.4171/OWR/2014/01; resolution: J. Huang, Invertibility of adjacency matrices for random d-regular graphs, Duke Math. J. 170 (2021), no. 18, 3977-4032, DOI 10.1215/00127094-2021-0006, arXiv:1807.06465, Theorem 1.3: for fixed d ≥ 3, P(A is singular in R) ≤ n^(-c) for n sufficiently large (directed and undirected d-regular graphs); Section 1.1: by a contiguity argument the results hold for the uniform model, https://arxiv.org/abs/1807.06465.

Stated but not proved: `MathlibExt.Combinatorics.RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.regularGraphAdjacencyNonsingular_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RegularGraphAdjacencyNonsingularOWR12861Problem026Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html#regular-graph-adjacency-nonsingular-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random regular graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/random-regular-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/random-graphs/random-regular-graphs)
