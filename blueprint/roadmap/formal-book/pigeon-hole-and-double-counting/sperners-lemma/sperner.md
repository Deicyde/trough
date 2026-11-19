---
declaration: lemma
origin: cited
lean: chapter28.sperner_odd
statement: formalized
proof: formalized
---

# Sperner's Lemma

Suppose that some “big” triangle with vertices $V_1, V_2, V_3$ is triangulated (that is, decomposed into a finite number of “small” triangles that fit together edge-by-edge). Assume that the vertices in the triangulation get “colors” from the set $\{1, 2, 3\}$ such that $V_i$ receives the color $i$ (for each $i$), and only the colors $i$ and $j$ are used for vertices along the edge from $V_i$ to $V_j$ (for $i \neq j$), while the interior vertices are colored arbitrarily with $1$, $2$, or $3$. Then in the triangulation there must be a small “tricolored” triangle, which has all three different vertex colors.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Handshaking](../graphs/handshaking.md)

## Proof

We will prove a stronger statement: The number of tricolored triangles is not only nonzero, it is always *odd*.

Consider the dual graph to the triangulation, but don't take all its edges — only those which cross an edge that has endvertices with the (different) colors $1$ and $2$. Thus we get a “partial dual graph” which has degree $1$ at all vertices that correspond to tricolored triangles, degree $2$ for all triangles in which the two colors $1$ and $2$ appear, and degree $0$ for triangles that do not have both colors $1$ and $2$. Thus only the tricolored triangles correspond to vertices of odd degree (of degree $1$).

However, the vertex of the dual graph which corresponds to the outside of the triangulation has odd degree: in fact, along the big edge from $V_1$ to $V_2$, there is an odd number of changes between $1$ and $2$. Thus an odd number of edges of the partial dual graph crosses this big edge, while the other big edges cannot have both $1$ and $2$ occurring as colors.

Now since the number of odd-degree vertices in any finite graph is even (by equation (4)), we find that the number of small triangles with three different colors (corresponding to odd inside vertices of our dual graph) is odd.

## Lean

Formalized as [`chapter28.sperner_odd`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.sperner_odd).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 329](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L329)
