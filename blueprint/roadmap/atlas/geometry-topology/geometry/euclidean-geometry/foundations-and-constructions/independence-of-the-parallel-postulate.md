---
declaration: section
origin: cited
lean: MathlibExt.Geometry.ParallelPostulateWanted.Geometry.TarskiAbsolute, MathlibExt.Geometry.ParallelPostulateWanted.Geometry.Euclidean, MathlibExt.Geometry.ParallelPostulateWanted.Geometry.parallel_postulate_independent
statement: formalized
---

# Independence of the parallel postulate

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate/index.html).

## Tarski's absolute plane geometry

A model of Tarski's absolute plane geometry is a type
$M$ of points with a betweenness relation $B$ and a congruence relation $C$, where $B(a, b, c)$
means that $b$ lies between $a$ and $c$ (allowing $b = a$ or $b = c$) and $C(a, b, c, d)$ means
that the segment $ab$ is congruent to the segment $cd$, satisfying the following axioms, in which
unbound variables range over all points of $M$ (axioms A1–A9 and A11 of
Schwabhäuser–Szmielew–Tarski, that is, all of Tarski's axioms except the Euclidean axiom A10):
(A1) $C(a, b, b, a)$;
(A2) if $C(a, b, c, d)$ and $C(a, b, e, f)$, then $C(c, d, e, f)$;
(A3) if $C(a, b, c, c)$, then $a = b$;
(A4) there is a point $x$ with $B(a, b, x)$ and $C(b, x, c, d)$;
(A5) if $a \ne b$, $B(a, b, c)$, $B(a', b', c')$, $C(a, b, a', b')$, $C(b, c, b', c')$,
$C(a, d, a', d')$ and $C(b, d, b', d')$, then $C(c, d, c', d')$;
(A6) if $B(a, b, a)$, then $a = b$;
(A7) if $B(a, p, c)$ and $B(b, q, c)$, then there is a point $x$ with $B(p, x, b)$ and
$B(q, x, a)$;
(A8) there are points $a, b, c$ such that none of $B(a, b, c)$, $B(b, c, a)$ and
$B(c, a, b)$ holds;
(A9) if $p \ne q$, $C(p, a, q, a)$, $C(p, b, q, b)$ and $C(p, c, q, c)$, then $B(a, b, c)$,
$B(b, c, a)$ or $B(c, a, b)$;
(A11) for all sets $X, Y \subseteq M$, if there is a point $a$ with $B(a, x, y)$ for all
$x \in X$ and $y \in Y$, then there is a point $b$ with $B(x, b, y)$ for all $x \in X$ and
$y \in Y$.

Formalized by `MathlibExt.Geometry.ParallelPostulateWanted.Geometry.TarskiAbsolute`, a class declared in [WantedExt/Geometry/ParallelPostulateWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ParallelPostulateWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate/index.html#tarski-absolute).

## Tarski's Euclidean axiom

For a model $M$ of Tarski's absolute plane geometry with
betweenness relation $B$, where $B(a, b, c)$ means that $b$ lies between $a$ and $c$ (allowing
$b = a$ or $b = c$), the Euclidean axiom A10 holds in $M$ when for all points $a, b, c, d, t$ of
$M$ with $B(a, d, t)$, $B(b, d, c)$ and $a \ne d$ there are points $x$ and $y$ of $M$ with
$B(a, b, x)$, $B(a, c, y)$ and $B(x, t, y)$.

In the presence of the other axioms of absolute geometry, this axiom is equivalent to Euclid's
parallel postulate.

Formalized by `MathlibExt.Geometry.ParallelPostulateWanted.Geometry.Euclidean`, a definition declared in [WantedExt/Geometry/ParallelPostulateWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ParallelPostulateWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate/index.html#euclidean).

## Independence of the parallel postulate

Tarski's Euclidean axiom A10 is independent of
Tarski's axioms of absolute plane geometry: there is a model of absolute plane geometry in which
the Euclidean axiom holds, and there is a model of absolute plane geometry in which it fails.

## Sources

- Independence of Euclid's parallel postulate; the hyperbolic-plane models are due to E. Beltrami (1868) and F. Klein (1871). Tarski's axiomatization: W. Schwabhäuser, W. Szmielew, A. Tarski, Metamathematische Methoden in der Geometrie, Springer (1983). Formalized in HOL Light by John Harrison and in Isabelle by Tim Makarios (T.J.M. Makarios, A Mechanical Verification of the Independence of Tarski's Euclidean Axiom, MSc thesis, Victoria University of Wellington, 2012; Isabelle/AFP entry Tarskis_Geometry). Problem `parallel_postulate_independent` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.ParallelPostulateWanted.Geometry.parallel_postulate_independent` is written with `theorem_wanted` in [WantedExt/Geometry/ParallelPostulateWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ParallelPostulateWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate/index.html#parallel-postulate-independent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independence of the parallel postulate](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/foundations-and-constructions/independence-of-the-parallel-postulate)
