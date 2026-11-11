---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.ScottishBook44Wanted.LineInGraph, MathlibExt.Analysis.Calculus.ScottishBook44Wanted.DoublyRuledGraph, MathlibExt.Analysis.Calculus.ScottishBook44Wanted.doubly_ruled_graph_is_quadric
statement: formalized
---

# Doubly ruled surfaces

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces/index.html).

## Line lying in a graph

Let $f$ be a real-valued function of two real variables, and let
$x_0, y_0, u, v, w$ be real numbers. The line through $(x_0, y_0, f(x_0, y_0))$ with direction
$(u, v, w)$ lies in the graph of $f$ when $(u, v) \ne (0, 0)$ and
$f(x_0 + tu, y_0 + tv) = f(x_0, y_0) + tw$ for every real $t$.

Formalized by `MathlibExt.Analysis.Calculus.ScottishBook44Wanted.LineInGraph`, a definition declared in [WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces/index.html#line-in-graph).

## Doubly ruled graph

The graph of a real-valued function $f$ of two real variables is
doubly ruled when for every point $(x_0, y_0) \in \mathbb{R}^2$ there are $(u_1, v_1, w_1)$ and
$(u_2, v_2, w_2)$ in $\mathbb{R}^3$ such that the lines through $(x_0, y_0, f(x_0, y_0))$ with
directions $(u_1, v_1, w_1)$ and $(u_2, v_2, w_2)$ both lie in the graph of $f$, and $(u_2, v_2)$
is not a real multiple of $(u_1, v_1)$.

A line lying in the graph has a nonzero horizontal direction, so the last condition holds exactly
when the two lines are distinct.

Formalized by `MathlibExt.Analysis.Calculus.ScottishBook44Wanted.DoublyRuledGraph`, a definition declared in [WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces/index.html#doubly-ruled-graph).

## Doubly ruled graphs are planes or hyperbolic paraboloids

Let $f$ be a real-valued
function of two real variables whose graph is doubly ruled; no continuity of $f$ is assumed. Then
there are real numbers $a, b, c, d, e, g$ such that
$f(x, y) = ax^2 + bxy + cy^2 + dx + ey + g$ for all real $x$ and $y$, and either $a = b = c = 0$
(the graph is a plane) or $b^2 - 4ac > 0$ (the graph is a hyperbolic paraboloid).

This answers Steinhaus's Problem 44 of the Scottish Book, which asks whether such a surface, the
graph of a continuous function, must be a hyperbolic paraboloid, and whether this can be proved
without continuity. Banach answered both questions affirmatively, with a proof based on the remark
that any two lines on the surface either intersect or have parallel projections on the
$xy$-plane; planes are the degenerate doubly ruled case.

## Sources

- H. Steinhaus, Problem 44 of the Scottish Book; addendum in the Scottish Book, 30 July 1935: solved affirmatively by Banach, also without assuming continuity; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.Calculus.ScottishBook44Wanted.doubly_ruled_graph_is_quadric` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/ScottishBook44Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces/index.html#doubly-ruled-graph-is-quadric).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Doubly ruled surfaces](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/curves-and-surfaces/doubly-ruled-surfaces)
