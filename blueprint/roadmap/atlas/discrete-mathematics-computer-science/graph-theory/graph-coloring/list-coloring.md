---
declaration: section
origin: cited
lean: SimpleGraph.IsListColorable, SimpleGraph.IsChoiceNumber, SimpleGraph.IsListColorable.mono, SimpleGraph.IsListColorable.colorable, MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.IsPartialListColoring, MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.conjecture, MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.conjecture_refuted, MathlibExt.GraphTheory.PartialListColoringWanted.IsListColoring
statement: formalized
---

# List coloring

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html).

## List colorability

A simple graph $G$ is $q$-list-colorable if, for every set of colors and
every assignment of a finite list $L(v)$ of at least $q$ colors to each vertex $v$, there is a
proper coloring $c$ of $G$ with $c(v) \in L(v)$ for every vertex $v$.

Formalized by `SimpleGraph.IsListColorable`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#is-list-colorable).

## Choice number

A natural number $q$ is the choice number of a simple graph $G$ if $G$ is
$q$-list-colorable but is not $r$-list-colorable for any $r < q$.

Formalized by `SimpleGraph.IsChoiceNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#is-choice-number).

## Monotonicity of list colorability

If a simple graph $G$ is $q$-list-colorable and
$q \le r$, then $G$ is $r$-list-colorable.

Formalized by `SimpleGraph.IsListColorable.mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#mono).

## List-colorable graphs are colorable

If a simple graph $G$ is $q$-list-colorable, then $G$
is $q$-colorable, that is, it has a proper coloring with $q$ colors.

Formalized by `SimpleGraph.IsListColorable.colorable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ListColoring.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#colorable).

## Partial list colorability

Let $G$ be a simple graph and assign to each vertex $v$ a finite
list $L(v)$ of colors. A finite set $S$ of vertices is partially list-colorable from $L$ when the
subgraph of $G$ induced by $S$ has a proper coloring $c$ with $c(v) \in L(v)$ for every
$v \in S$. No colors are assigned to vertices outside $S$.

Formalized by `MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.IsPartialListColoring`, a definition declared in [WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#is-partial-list-coloring).

## Albertson–Grossman–Haas partial list coloring conjecture

Let $G$ be a finite simple graph
on $n$ vertices whose choice number $q$ is positive, let $t \le q$ be a natural number, and assign
to each vertex $v$ a list $L(v)$ of exactly $t$ colors. Then there is a set $S$ of vertices of $G$
that is partially list-colorable from $L$ (the subgraph of $G$ induced by $S$ has a proper
coloring giving each vertex a color from its list) and satisfies $tn \le q|S|$, that is,
$|S| \ge tn/q$.

Formalized by `MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#conjecture).

## The partial list coloring conjecture is false

There exist a finite simple graph $G$ on
$n$ vertices whose choice number $q$ is positive, a natural number $t \le q$, and an assignment
to each vertex $v$ of a list $L(v)$ of exactly $t$ colors, such that every set $S$ of vertices
of $G$ whose induced subgraph has a proper coloring giving each vertex a color from its list
satisfies $q|S| < tn$.

Noel (arXiv:2609.23291, Sep 2026) gives a $14$-vertex graph with choice number $3$ and an
assignment of lists of exactly $2$ colors from which at most $9 < 28/3$ vertices can be properly
colored, so the conjectured bound $|S| \ge tn/q$ fails at $q = 3$, $t = 2$.

## Sources

- Jonathan A. Noel, The Partial List Colouring Conjecture is False, arXiv preprint (2026), arXiv:2609.23291, https://arxiv.org/abs/2609.23291.

Stated but not proved: `MathlibExt.Combinatorics.PartialListColoringProportionalBoundWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PartialListColoringProportionalBoundWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#conjecture-refuted).

## Proper list colouring of a vertex subset

Let $G$ be a graph on a finite vertex set $V$,
let $L$ assign to each vertex $v$ a finite list $L(v)$ of colours (natural numbers), and let
$S \subseteq V$. A map $f : V \to \mathbb{N}$ is a proper $L$-colouring of $S$ when
$f(v) \in L(v)$ for every $v \in S$ and $f(v) \ne f(w)$ for all adjacent $v, w \in S$.

Formalized by `MathlibExt.GraphTheory.PartialListColoringWanted.IsListColoring`, a definition declared in [WantedExt/GraphTheory/PartialListColoringWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PartialListColoringWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#is-list-coloring).

## Maximum number of list-colourable vertices

For a graph $G$ on a finite vertex set and an
assignment $L$ of a finite list $L(v)$ of natural-number colours to each vertex $v$, $\lambda_L$
is the largest $k$ such that some set of $k$ vertices of $G$ has a proper $L$-colouring.

Formalized by `MathlibExt.GraphTheory.PartialListColoringWanted.lambdaMax`, a definition declared in [WantedExt/GraphTheory/PartialListColoringWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PartialListColoringWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#lambda-max).

## The partial list colouring number $\lambda_t$

For a graph $G$ on a finite vertex set and
a natural number $t$, $\lambda_t$ is the minimum of $\lambda_L$ over all assignments $L$ of a
list $L(v)$ of exactly $t$ natural-number colours to each vertex $v$, where $\lambda_L$ is the
largest $k$ such that some set of $k$ vertices of $G$ has a proper $L$-colouring.

Formalized by `MathlibExt.GraphTheory.PartialListColoringWanted.lambdaMin`, a definition declared in [WantedExt/GraphTheory/PartialListColoringWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PartialListColoringWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#lambda-min).

## Iradmusa's partial list colouring conjecture

For every finite graph $G$ with choice
number $\chi_\ell$ and all natural numbers $r$, $s$ with $1 \le r \le s \le \chi_\ell$, one has
$\lambda_r / r \ge \lambda_s / s$, where $\lambda_t$ is the minimum, over all assignments of
lists of exactly $t$ colours to the vertices, of the largest number of vertices of $G$ that can
be properly coloured from their lists.

Formalized by `MathlibExt.GraphTheory.PartialListColoringWanted.conjecture`, a definition declared in [WantedExt/GraphTheory/PartialListColoringWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PartialListColoringWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#conjecture-2).

## The partial list colouring conjecture is false

There exist a finite graph $G$ with choice
number $\chi_\ell$ and natural numbers $r$, $s$ with $1 \le r \le s \le \chi_\ell$ such that
$\lambda_r / r < \lambda_s / s$, where $\lambda_t$ is the minimum, over all assignments of lists
of exactly $t$ colours to the vertices, of the largest number of vertices of $G$ that can be
properly coloured from their lists. So Iradmusa's partial list colouring conjecture fails.

Noel's counterexample (Theorem 1.1) is a 14-vertex graph (four triangles plus two terminals)
with choice number 3 and a 2-list assignment colouring at most 9 vertices, so
$\lambda_2 / 2 \le 9/2 < 14/3 = \lambda_3 / 3$.

## Sources

- Jonathan A. Noel, The Partial List Colouring Conjecture is False, arXiv preprint (2026), arXiv:2609.23291, https://arxiv.org/abs/2609.23291.

Stated but not proved: `MathlibExt.GraphTheory.PartialListColoringWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GraphTheory/PartialListColoringWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PartialListColoringWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html#conjecture-refuted-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List coloring](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/list-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/list-coloring)
