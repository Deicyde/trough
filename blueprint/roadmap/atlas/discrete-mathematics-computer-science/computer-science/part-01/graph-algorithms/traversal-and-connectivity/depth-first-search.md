---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.DepthFirstSearch.Traversal, Cslib.Algorithms.Lean.DepthFirstSearch.dfs, Cslib.Algorithms.Lean.DepthFirstSearch.Internal.Steps, Cslib.Algorithms.Lean.DepthFirstSearch.IsLeftFirstDFS, Cslib.Algorithms.Lean.DepthFirstSearch.dfs_is_left_first, Cslib.Algorithms.Lean.DepthFirstSearch.IsLeftFirstDFS.eq_dfs, Cslib.Algorithms.Lean.DepthFirstSearch.preorder_sound, Cslib.Algorithms.Lean.DepthFirstSearch.preorder_complete
statement: formalized
proof: formalized
---

# Depth-first search

37 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html).

## Depth-first traversal record

A traversal over a vertex type $V$ consists of three lists: a
preorder (discovery order) list of vertices, a postorder (finish order) list of vertices, and a
list of parent pairs in $V \times V$, each stored as $(\text{child}, \text{parent})$.

No condition relating the three lists is imposed by the record itself.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.Traversal`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#traversal).

## Left-first depth-first search

Given a directed graph $G$ with ordered adjacency lists
and an ordered list of roots, depth-first search processes the roots from left to right,
skipping roots already visited. Visiting an unvisited vertex $v$ marks it visited and records its
discovery, then processes the out-neighbours of $v$ in adjacency-list order, visiting each one
not yet visited at that moment and recording $v$ as its parent, and finally records that $v$ has
finished. The result is the traversal consisting of the vertices in discovery order (preorder),
the vertices in finish order (postorder), and the (child, parent) pairs in the order the children
were discovered.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.dfs`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#dfs).

## Sequences of depth-first search machine steps

Zero or more independent DFS machine steps.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.Internal.Steps`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#steps).

## Left-first depth-first traversals

Let $G$ be a finite directed graph given by ordered
adjacency lists and let $r = (r_1, \dots, r_k)$ be a list of root vertices. A traversal $T$ is a
left-first DFS of $G$ from $r$ when some finite run of the following machine ends with an empty
work list and with recorded preorder, postorder and (child, parent) list equal to those of $T$.

The machine holds a work list of frames, each either "enter $v$ with parent $p$" (where the parent
$p$ may be absent) or "exit $v$", a set of visited vertices, and the three recorded lists. It starts
with the frames "enter $r_1$ with no parent", ..., "enter $r_k$ with no parent", no visited vertex
and empty recorded lists. A step removes the first frame of the work list. For "exit $v$" it
appends $v$ to the postorder. For "enter $v$ with parent $p$" it does nothing more if $v$ is
visited; otherwise it marks $v$ visited, appends $v$ to the preorder, appends $(v, p)$ to the
(child, parent) list if $p$ is present, and puts in front of the remaining work the frames
"enter $w$ with parent $v$" for the entries $w$ of the adjacency list of $v$, in order, followed by
"exit $v$".

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.IsLeftFirstDFS`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#is-left-first-dfs).

## Executable DFS meets the left-first specification

For every directed graph $G$ with
ordered adjacency lists and every ordered list of roots, the traversal computed by left-first
depth-first search of $G$ from these roots conforms to left-first DFS for $G$ and these roots.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.dfs_is_left_first`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#dfs-is-left-first).

## The left-first DFS specification determines the traversal

Let $G$ be a directed graph
with ordered adjacency lists, fix an ordered list of roots, and let $T$ be a traversal. If $T$
conforms to left-first DFS for $G$ and these roots, then $T$ equals the traversal computed by
left-first depth-first search of $G$ from these roots.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.IsLeftFirstDFS.eq_dfs`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#eq-dfs).

## Depth-first search discovers only reachable vertices

Let $G$ be a finite directed graph
given by ordered adjacency lists and let $R$ be a list of roots. Every vertex in the preorder
(discovery order) of the depth-first search of $G$ from $R$ is reachable in $G$ from some root
in $R$ by a directed path (possibly of length zero).

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.preorder_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#preorder-sound).

## Depth-first search discovers every reachable vertex

Let $G$ be a finite directed graph
given by ordered adjacency lists and let $R$ be a list of roots. If a vertex $v$ is reachable in
$G$ from some root in $R$ by a directed path (possibly of length zero), then $v$ occurs in the
preorder (discovery order) of the depth-first search of $G$ from $R$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.preorder_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#preorder-complete).

## Depth-first search discovers exactly the reachable vertices

Let $G$ be a finite directed
graph and $R$ a list of root vertices. A vertex $v$ occurs in the discovery order (preorder) of
the depth-first search of $G$ from $R$ if and only if there is a root $r$ in $R$ from which $v$
is reachable in $G$ by a directed path of length zero or more.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_preorder_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-preorder-iff-reachable).

## Depth-first search discovers each vertex at most once

For every finite directed graph $G$
given by ordered adjacency lists and every list $R$ of roots, the preorder (discovery order) of
the depth-first search of $G$ from $R$ contains no vertex twice.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.preorder_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#preorder-nodup).

## Depth-first search finishes exactly the reachable vertices

Let $G$ be a finite directed
graph and $R$ a list of root vertices. A vertex $v$ occurs in the finish order (postorder) of the
depth-first search of $G$ from $R$ if and only if there is a root $r$ in $R$ from which $v$ is
reachable in $G$ by a directed path of length zero or more.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_postorder_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-postorder-iff-reachable).

## DFS finishes each vertex at most once

Let $G$ be a finite directed graph and $R$ a list of
root vertices. The finish order (postorder) of the depth-first search of $G$ from $R$ contains no
vertex twice.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.postorder_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#postorder-nodup).

## Occurring before in a list

For elements $x$ and $y$ and a list $xs$, $x$ occurs before
$y$ in $xs$ when there are lists $a$, $b$ and $c$ such that $xs$ is the concatenation of $a$, the
element $x$, $b$, the element $y$ and $c$; that is, some occurrence of $x$ lies at a strictly
earlier position than some occurrence of $y$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.Before`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#before).

## Parent relation of a list of pairs

Given a list $P$ of (child, parent) pairs, $p$ is a
parent of $c$ in $P$ when the pair $(c, p)$ occurs in $P$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.ParentRel`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-rel).

## Roots of a DFS forest

The forest roots of a traversal $T$ are the vertices of the preorder
of $T$ that do not occur as the child in any (child, parent) pair recorded by $T$, listed in the
order in which they occur in the preorder.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.Traversal.forestRoots`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 950](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L950). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#forest-roots).

## DFS forest roots are distinct

For every finite directed graph $G$ given by ordered
adjacency lists and every list $r$ of root vertices, the list of forest roots of the left-first
depth-first search of $G$ from $r$ contains no vertex twice.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.forestRoots_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 956](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L956). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#forest-roots-nodup).

## A DFS forest root has no parent

Let $G$ be a finite directed graph given by ordered
adjacency lists, let $r$ be a list of root vertices, and let $v$ and $p$ be vertices. If $v$ is a
forest root of the left-first depth-first search of $G$ from $r$, then $(v, p)$ is not among the
(child, parent) pairs recorded by that search.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.forestRoot_has_no_parent`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 962](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#forest-root-has-no-parent).

## DFS parent pairs are graph edges

Let $G$ be a finite directed graph and $R$ a list of root
vertices, and run depth-first search on $G$ from $R$. If the pair $(c, p)$ occurs in the list of
(child, parent) pairs recorded by the search, then $G$ has a directed edge from $p$ to $c$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_edge`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 973](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L973). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-edge).

## No vertex is recorded twice as a DFS child

Let $G$ be a finite directed graph and $R$ a
list of root vertices, and run depth-first search on $G$ from $R$. In the list of
(child, parent) pairs recorded by the search, no vertex occurs as the child of more than one
entry; that is, the list of children has no repeated entries.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_children_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 981](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L981). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-children-nodup).

## Every discovered vertex is a forest root or has a unique parent

Let $G$ be a finite
directed graph given by ordered adjacency lists, let $r$ be a list of root vertices, and let $v$
be a vertex in the preorder of the left-first depth-first search of $G$ from $r$. Then $v$ is a
forest root of that search, or there is exactly one vertex $p$ such that $(v, p)$ is among the
(child, parent) pairs recorded by the search.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_forestRoots_or_existsUnique_parent`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 987](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-forest-roots-or-exists-unique-parent).

## In preorder, a DFS parent precedes its child

Let $G$ be a finite directed graph and $R$ a
list of root vertices, and run depth-first search on $G$ from $R$. If the pair $(c, p)$ occurs in
the list of (child, parent) pairs recorded by the search, then $p$ occurs strictly before $c$ in
the discovery order (preorder) of the search.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_before_child`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-before-child).

## A DFS child finishes before its parent

Let $G$ be a directed graph with ordered
adjacency lists and fix an ordered list of roots. If $(c, p)$ is one of the (child, parent) pairs
recorded by the left-first depth-first search of $G$ from these roots, then $c$ occurs before $p$
in the postorder (finish order) of that search.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.child_before_parent_postorder`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1018](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1018). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#child-before-parent-postorder).

## Decreasing finish order

For a directed graph $G$ with ordered adjacency lists and an
ordered list of roots, the decreasing finish order is the reverse of the postorder of the
left-first depth-first search of $G$ from those roots: the vertices that search visits, listed
from the latest finished to the earliest finished.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.decreasingFinish`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1031](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1031). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#decreasing-finish).

## In decreasing finish order, a DFS parent precedes its child

Let $G$ be a finite directed
graph and $R$ a list of root vertices, and run depth-first search on $G$ from $R$. If the pair
$(c, p)$ occurs in the list of (child, parent) pairs recorded by the search, then $p$ occurs
strictly before $c$ in the decreasing finish order, the reverse of the finish order.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_before_child_decreasingFinish`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1036](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1036). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-before-child-decreasing-finish).

## Decreasing finish order lists exactly the vertices reachable from the roots

Let $G$ be a
finite directed graph given by ordered adjacency lists, let $r$ be a list of root vertices, and let
$v$ be a vertex. Then $v$ occurs in the decreasing finish order of the left-first depth-first
search of $G$ from $r$ if and only if $v$ is reachable in $G$ from some vertex of $r$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_decreasingFinish_iff_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1043](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1043). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-decreasing-finish-iff-reachable).

## Decreasing finish order has no repeated vertices

For every directed graph $G$ with
ordered adjacency lists and every ordered list of roots, the decreasing finish order of the
depth-first search of $G$ from those roots contains no vertex twice.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.decreasingFinish_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1050](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1050). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#decreasing-finish-nodup).

## Parent chains in a DFS forest end at a forest root

Let $G$ be a finite directed graph and
$R$ a list of root vertices, and run depth-first search on $G$ from $R$. Say that $p$ is a recorded
parent of $c$ when the pair $(c, p)$ occurs in the list of (child, parent) pairs recorded by the
search, and call a discovered vertex with no recorded parent a forest root. Then for every
vertex $v$ in the discovery order (preorder) there are $k \ge 0$ and vertices
$v = v_0, v_1, \dots, v_k$ such that each $v_{i+1}$ is a recorded parent of $v_i$ and $v_k$ is a
forest root.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_chain_reaches_root`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-chain-reaches-root).

## The DFS parent relation is acyclic

Let $G$ be a finite directed graph and $R$ a list of
root vertices, and run depth-first search on $G$ from $R$. Say that $p$ is a recorded parent of $c$
when the pair $(c, p)$ occurs in the list of (child, parent) pairs recorded by the search. Then
there are no $k \ge 1$ and vertices $v_0, v_1, \dots, v_k$ with $v_k = v_0$ such that each
$v_{i+1}$ is a recorded parent of $v_i$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.parent_relation_acyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#parent-relation-acyclic).

## DFS forest roots are scheduled roots

Let $G$ be a finite directed graph given by ordered
adjacency lists, let $r$ be a list of root vertices, and let $v$ be a vertex. If $v$ is a forest
root of the left-first depth-first search of $G$ from $r$, then $v$ occurs in $r$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.forestRoot_mem_roots`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#forest-root-mem-roots).

## Depth-first search of the whole graph

For a directed graph $G$ with ordered adjacency
lists, the whole-graph traversal is the left-first depth-first search of $G$ whose roots are all
vertices of $G$, taken in the graph's fixed vertex enumeration order.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.dfsAll`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#dfs-all).

## Whole-graph DFS discovers every vertex

For every finite directed graph $G$ given by
ordered adjacency lists and every vertex $v$ of $G$, $v$ occurs in the preorder of the whole-graph
depth-first search of $G$, that is, the left-first depth-first search of $G$ whose roots are all
vertices of $G$ in the graph's vertex order.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_dfsAll_preorder`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-dfs-all-preorder).

## Whole-graph DFS finishes every vertex

For every finite directed graph $G$ given by ordered
adjacency lists and every vertex $v$ of $G$, $v$ occurs in the postorder of the whole-graph
depth-first search of $G$, that is, the left-first depth-first search of $G$ whose roots are all
vertices of $G$ in the graph's vertex order.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_dfsAll_postorder`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-dfs-all-postorder).

## Whole-graph decreasing finish order

For a directed graph $G$ with ordered adjacency
lists, the whole-graph decreasing finish order is the decreasing finish order of the left-first
depth-first search of $G$ whose roots are all vertices of $G$, taken in the graph's vertex
enumeration order; its vertices are listed from the latest finished to the earliest finished.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.decreasingFinishAll`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#decreasing-finish-all).

## Whole-graph decreasing finish order contains every vertex

For every finite directed graph
$G$ given by ordered adjacency lists and every vertex $v$ of $G$, $v$ occurs in the whole-graph
decreasing finish order of $G$, that is, the decreasing finish order of the left-first
depth-first search of $G$ whose roots are all vertices of $G$ in the graph's vertex order.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.mem_decreasingFinishAll`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#mem-decreasing-finish-all).

## Whole-graph decreasing finish order has no repeated vertices

For every directed graph
$G$ with ordered adjacency lists, the whole-graph decreasing finish order of $G$ contains no
vertex twice.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.decreasingFinishAll_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean, line 1210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearch.lean#L1210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#decreasing-finish-all-nodup).

## Exact transition count of depth-first search

Let $G$ be a finite directed graph with
ordered adjacency lists $N(v)$, whose entries may repeat, and let $R$ be a list of roots, possibly
with repetitions. Run the depth-first search machine from $R$ (each transition drops a pending
vertex that is already visited, discovers a new vertex, or finishes a vertex). Let
$v_1, \dots, v_k$ be the preorder of the depth-first search of $G$ from $R$. Then there is a
terminal machine state, with no work left, whose recorded output is the depth-first traversal of
$G$ from $R$ and which is reached from the initial state in exactly
$|R| + k + \sum_{i=1}^{k} |N(v_i)|$ transitions, where $|R|$ is the length of $R$ and $|N(v)|$
is the length of the adjacency list of $v$.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.dfs_exact_steps`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearchCosts.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearchCosts.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#dfs-exact-steps).

## Exact transition count of whole-graph depth-first search

Let $G$ be a finite directed
graph whose vertices are listed without repetition as $v_1, \dots, v_n$, with ordered adjacency
lists $N(v)$ whose entries may repeat. Run the depth-first search machine with roots
$v_1, \dots, v_n$ in this order (each transition drops a pending vertex that is already visited,
discovers a new vertex, or finishes a vertex). Then there is a terminal machine state, with no
work left, whose recorded output is the whole-graph depth-first traversal of $G$ and which is
reached from the initial state in exactly $2n + \sum_{i=1}^{n} |N(v_i)|$ transitions, where
$|N(v)|$ is the length of the adjacency list of $v$, counting repeated entries and self-loops.

Formalized by `Cslib.Algorithms.Lean.DepthFirstSearch.dfsAll_exact_steps`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/DepthFirstSearchCosts.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/DepthFirstSearchCosts.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html#dfs-all-exact-steps).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Depth-first search](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/depth-first-search)
