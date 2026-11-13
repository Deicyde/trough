---
declaration: section
origin: cited
lean: MetaMathlibExt.roadColoring', MetaMathlibExt.roadColoring
statement: formalized
proof: formalized
---

# Road coloring theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/road-coloring-theorem/index.html).

## Road coloring theorem for a finite vertex type

Let $V$ be a finite nonempty set and let
$\to$ be a relation on $V$, viewed as a directed graph on $V$ without parallel edges (loops
allowed). Suppose that the graph is strongly connected (for all $u, v \in V$ there is a directed
walk, possibly of length $0$, from $u$ to $v$), aperiodic (for every integer $d > 1$ there is a
closed directed walk of positive length not divisible by $d$), and of constant positive
out-degree (there is $k > 0$ such that every vertex has exactly $k$ out-neighbours). Then there
exist a natural number $\ell$ and a map $\delta : V \times \{0, \dots, \ell - 1\} \to V$ such that
for every $v \in V$ the map $c \mapsto \delta(v, c)$ is a bijection from $\{0, \dots, \ell - 1\}$
onto the out-neighbours of $v$, together with a word $c_1 \cdots c_m$ over $\{0, \dots, \ell - 1\}$
and a vertex $r$ such that following the labels $c_1, \dots, c_m$ in order from any vertex $v$
ends at $r$.

This form only assumes that $V$ is finite, as a property, rather than being given a finite set of
all its elements as data.

Formalized by `MetaMathlibExt.roadColoring'`, a theorem declared in [MathlibExt/Combinatorics/RoadColoring.lean, line 3835](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/RoadColoring.lean#L3835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/road-coloring-theorem/index.html#road-coloring).

## Road coloring theorem

Let $V$ be a finite nonempty set and let $\to$ be a relation
on $V$, viewed as a directed graph on $V$ without parallel edges (loops allowed). Suppose that the
graph is strongly connected (for all $u, v \in V$ there is a directed walk, possibly of length $0$,
from $u$ to $v$), aperiodic (for every integer $d > 1$ there is a closed directed walk of positive
length not divisible by $d$), and of constant positive out-degree (there is $k > 0$ such that
every vertex has exactly $k$ out-neighbours). Then there exist a natural number $\ell$ and a map
$\delta : V \times \{0, \dots, \ell - 1\} \to V$ such that for every $v \in V$ the map
$c \mapsto \delta(v, c)$ is a bijection from $\{0, \dots, \ell - 1\}$ onto the out-neighbours of
$v$, together with a word $c_1 \cdots c_m$ over $\{0, \dots, \ell - 1\}$ and a vertex $r$ such
that following the labels $c_1, \dots, c_m$ in order from any vertex $v$ ends at $r$.

## Sources

- https://en.wikipedia.org/wiki/Road_coloring_theorem

Formalized by `MetaMathlibExt.roadColoring`, a theorem declared in [MathlibExt/Combinatorics/RoadColoring.lean, line 3875](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/RoadColoring.lean#L3875). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/road-coloring-theorem/index.html#road-coloring-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Road coloring theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/road-coloring-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/directed-graphs/road-coloring-theorem)
