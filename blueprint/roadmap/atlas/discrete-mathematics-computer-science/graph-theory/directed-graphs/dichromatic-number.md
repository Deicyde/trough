---
declaration: section
origin: cited
lean: SimpleGraph.IsOrientation, SimpleGraph.IsDirectedCycle, SimpleGraph.DichromaticColorable, SimpleGraph.dichromaticNumber, SimpleGraph.DichromaticColorable.dichromaticNumber_eq_sInf, SimpleGraph.IsOrientation.of_edgeless, SimpleGraph.DichromaticColorable.of_edgeless
statement: formalized
proof: formalized
---

# Dichromatic number

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html).

## Orientations of a graph

Let $G$ be a simple graph on a vertex set $V$. A binary relation
$D$ on $V$ is an orientation of $G$ if $D(u, v)$ holds only when $u$ and $v$ are adjacent in $G$,
and for every pair of adjacent vertices $u$ and $v$ exactly one of $D(u, v)$ and $D(v, u)$
holds.

Formalized by `SimpleGraph.IsOrientation`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#is-orientation).

## Closed directed walks

Let $D$ be a binary relation on a set $V$, viewed as a digraph,
let $n$ be a natural number, and let $f_0, f_1, \dots, f_{n+1}$ be elements of $V$. The sequence
$(f_0, \dots, f_{n+1})$ is a closed directed walk of length $n + 1$ in $D$ if $f_0 = f_{n+1}$ and
$D(f_i, f_{i+1})$ holds for every $i$ with $0 \le i \le n$.

Vertices may repeat, so this is a closed walk of positive length rather than a directed cycle in
the strict sense.

Formalized by `SimpleGraph.IsDirectedCycle`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#is-directed-cycle).

## Dichromatically $k$-colourable graphs

Let $G$ be a simple graph on a vertex set $V$ and
let $k$ be a natural number. Then $G$ is dichromatically $k$-colourable if for every orientation
$D$ of $G$ there is a map $c \colon V \to \{0, \dots, k - 1\}$, not required to be a proper
colouring, such that no closed directed walk of positive length in $D$ has all of its vertices of
the same colour under $c$.

Since every closed directed walk of positive length contains a directed cycle, this is the same as
asking for a colouring with no monochromatic directed cycle.

Formalized by `SimpleGraph.DichromaticColorable`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#dichromatic-colorable).

## Dichromatic number

The dichromatic number of a simple graph $G$ is the least natural
number $k$ such that $G$ is dichromatically $k$-colourable, taken in $\mathbb{N} \cup \{\infty\}$;
it is $\infty$ if $G$ is dichromatically $k$-colourable for no natural number $k$.

Formalized by `SimpleGraph.dichromaticNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#dichromatic-number).

## The dichromatic number as a least natural number

Let $G$ be a simple graph. If $G$ is
dichromatically $n$-colourable for some natural number $n$, then the dichromatic number of $G$
equals the least natural number $k$ such that $G$ is dichromatically $k$-colourable.

Formalized by `SimpleGraph.DichromaticColorable.dichromaticNumber_eq_sInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#dichromatic-number-eq-s-inf).

## The empty orientation of an edgeless graph

If a simple graph $G$ has no edges, then the
empty relation on its vertex set, the digraph with no arcs, is an orientation of $G$.

Formalized by `SimpleGraph.IsOrientation.of_edgeless`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#of-edgeless).

## Edgeless graphs are dichromatically $1$-colourable

If a simple graph $G$ has no edges,
then $G$ is dichromatically $1$-colourable.

No orientation of $G$ has an arc, so there is no closed directed walk of positive length.

Formalized by `SimpleGraph.DichromaticColorable.of_edgeless`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Dichromatic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html#of-edgeless-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dichromatic number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/dichromatic-number/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/directed-graphs/dichromatic-number)
