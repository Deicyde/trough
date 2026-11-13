---
declaration: section
origin: cited
lean: SimpleGraph.SArc, MetaMathlibExt.SimpleGraph.IsSArcTransitive, MetaMathlibExt.SimpleGraph.IsSArcRegular, SimpleGraph.arcDigraph
statement: formalized
proof: formalized
---

# Arc-transitive graphs

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html).

## $s$-arc

Let $X$ be a finite graph and $s$ a natural number. An *$s$-arc* in $X$ is a
sequence $(v_0, \dots, v_s)$ of vertices of $X$ such that $v_{i-1}$ and $v_i$ are adjacent for
$1 \le i \le s$, and $v_{i-1} \ne v_{i+1}$ for $0 < i < s$.

Formalized by `SimpleGraph.SArc`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html#sarc).

## $s$-arc transitive graph

A finite graph $G$ is $s$-arc transitive if its automorphism
group acts transitively on its $s$-arcs: for any two $s$-arcs $(u_0, \dots, u_s)$ and
$(v_0, \dots, v_s)$ of $G$ there is an automorphism $\varphi$ of $G$ with $\varphi(u_i) = v_i$
for every $i \le s$.

Formalized by `MetaMathlibExt.SimpleGraph.IsSArcTransitive`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html#is-sarc-transitive).

## $s$-arc regular graph

A finite graph $G$ is $s$-arc regular if it has at least one
$s$-arc and, for any two $s$-arcs $(u_0, \dots, u_s)$ and $(v_0, \dots, v_s)$ of $G$, there is
exactly one automorphism $\varphi$ of $G$ with $\varphi(u_i) = v_i$ for every $i \le s$.

Formalized by `MetaMathlibExt.SimpleGraph.IsSArcRegular`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html#is-sarc-regular).

## $s$-arc digraph

Let $X$ be a finite graph and $s$ a natural number. For an
$(s+1)$-arc $\gamma = (x_0, \dots, x_{s+1})$ of $X$, its *head* is the $s$-arc
$(x_1, \dots, x_{s+1})$ and its *tail* is the $s$-arc $(x_0, \dots, x_s)$. If $\alpha$ and
$\beta$ are $s$-arcs of $X$, then $\beta$ *follows* $\alpha$ if there is an $(s+1)$-arc of $X$
whose tail is $\alpha$ and whose head is $\beta$. The *$s$-arc digraph* $X^{(s)}$ is the directed
graph whose vertices are the $s$-arcs of $X$, with an arc from $\alpha$ to $\beta$ if and only if
$\beta$ follows $\alpha$.

Formalized by `SimpleGraph.arcDigraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/SArcs.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html#arc-digraph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arc-transitive graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/arc-transitive-graphs)
