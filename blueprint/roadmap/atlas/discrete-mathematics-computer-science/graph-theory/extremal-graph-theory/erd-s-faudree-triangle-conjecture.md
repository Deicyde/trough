---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.ErdosProblem1034Wanted.JoinedToTwo, MathlibExt.GraphTheory.ErdosProblem1034Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem1034Wanted.disprovedForm, MathlibExt.GraphTheory.ErdosProblem1034Wanted.bookLowerBound, MathlibExt.GraphTheory.ErdosProblem1034Wanted.maTangUpperBound, MathlibExt.GraphTheory.ErdosProblem1034Wanted.k4FreeUpperBound, MathlibExt.GraphTheory.ErdosProblem1034Wanted.conjecture_refuted
statement: formalized
---

# Erdős–Faudree triangle conjecture

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html).

## Vertices joined to two vertices of a set

Let $G$ be a simple graph on a vertex type $V$
and let $T$ and $Y$ be finite sets of vertices. The set $Y$ is joined to two vertices of $T$ in
$G$ if every vertex $y \in Y$ is adjacent in $G$ to two distinct vertices $u, v \in T$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.JoinedToTwo`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#joined-to-two).

## Erdős–Faudree triangle conjecture

For every real $\varepsilon > 0$ the following holds
for all sufficiently large $n$: every simple graph $G$ on the vertex set $\{0, \dots, n-1\}$ with
more than $n^2/4$ edges contains a triangle $T$ and a set $Y$ of vertices, each adjacent in $G$
to two distinct vertices of $T$, with $|Y| > (1/2 - \varepsilon)n$.

This claim (Erdős Problem 1034) was disproved by Ma and Tang.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#conjecture).

## Negation of the Erdős–Faudree triangle conjecture

The proposition that the
Erdős–Faudree triangle conjecture fails, that is, that it is not the case that for every real
$\varepsilon > 0$ and all sufficiently large $n$, every simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ with more than $n^2/4$ edges contains a triangle $T$ and a set $Y$ of
vertices, each adjacent in $G$ to two distinct vertices of $T$, with $|Y| > (1/2 - \varepsilon)n$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.disprovedForm`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#disproved-form).

## Book lower bound for Erdős Problem 1034

For every real $\varepsilon > 0$ the following
holds for all sufficiently large $n$: every simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ with more than $n^2/4$ edges contains a triangle $T$ and a set $Y$ of
vertices, each adjacent in $G$ to two distinct vertices of $T$, with
$|Y| \ge (1/6 - \varepsilon)n$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.bookLowerBound`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#book-lower-bound).

## Ma–Tang upper bound for Erdős Problem 1034

For every real $\varepsilon > 0$ the following
holds for all sufficiently large $n$: there is a simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ with more than $n^2/4$ edges such that for every triangle $T$ of $G$, every
set $Y$ of vertices each adjacent in $G$ to two distinct vertices of $T$ satisfies
$|Y| \le (2 - \sqrt{5/2} + \varepsilon)n$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.maTangUpperBound`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#ma-tang-upper-bound).

## $K_4$-free upper bound for Erdős Problem 1034

For every real $\varepsilon > 0$ the
following holds for all sufficiently large $n$: there is a simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ that contains no $K_4$ and has more than $n^2/4$ edges, such that for every
triangle $T$ of $G$, every set $Y$ of vertices each adjacent in $G$ to two distinct vertices of
$T$ satisfies $|Y| \le (2\sqrt{3} - 3 + \varepsilon)n$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem1034Wanted.k4FreeUpperBound`, a definition declared in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#k4-free-upper-bound).

## The Erdős–Faudree triangle conjecture is false

It is not true that for every real
$\varepsilon > 0$ and all sufficiently large $n$, every simple graph on the vertex set
$\{0, \dots, n-1\}$ with more than $n^2/4$ edges contains a triangle $T$ and a set of more than
$(1/2 - \varepsilon)n$ vertices, each adjacent to two distinct vertices of $T$.

## Sources

- Ma and Tang (disproof with upper bound (2-√(5/2)+o(1))n; K₄-free sketch with (2√3-3+o(1))n), per erdosproblems.com/1034, https://www.erdosproblems.com/1034.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem1034Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem1034Wanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem1034Wanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Faudree triangle conjecture](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/erd-s-faudree-triangle-conjecture)
