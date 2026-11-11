---
declaration: section
origin: cited
lean: WeierstrassCurve.Affine.frobeniusTrace, WeierstrassCurve.Affine.natCard_point_eq_natCard_affineSolutions_add_one, WeierstrassCurve.Affine.natCard_point_le_two_mul_natCard_add_one, WeierstrassCurve.Affine.natCard_point_eq_natCard_add_one_sub_frobeniusTrace, WeierstrassCurve.Affine.natCard_point_add_frobeniusTrace_eq, MetaMathlibExt.exists_isElliptic_frobeniusTrace_eq_iff, MetaMathlibExt.ramanujan_iff_nontrivial_zeros_re_eq_half, MetaMathlibExt.isWeilNumber_of_ramanujan
statement: formalized
---

# Point counts and Frobenius traces

10 results, 5 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html).

## Frobenius trace

Let $W$ be a Weierstrass curve over a finite field $F$ with $q$ elements,
and let $\#W(F)$ be the number of nonsingular $F$-points of $W$, counting the point at infinity.
The Frobenius trace of $W$ is the integer $a_q(W) = q + 1 - \#W(F)$.

Formalized by `WeierstrassCurve.Affine.frobeniusTrace`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#frobenius-trace).

## Point count from affine solutions

Let $W$ be an elliptic curve in Weierstrass form over a
finite field $F$. The number of $F$-points of $W$, counting the point at infinity, is one more than
the number of pairs $(x, y) \in F \times F$ satisfying the Weierstrass equation of $W$.

Formalized by `WeierstrassCurve.Affine.natCard_point_eq_natCard_affineSolutions_add_one`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#nat-card-point-eq-nat-card-affine-soluti).

## Upper bound on the point count

Let $W$ be a Weierstrass curve over a finite field $F$
with $q$ elements. The number of nonsingular $F$-points of $W$, counting the point at infinity, is
at most $2q + 1$.

Each $x \in F$ lies under at most two affine points, since the Weierstrass equation is quadratic
in $y$.

Formalized by `WeierstrassCurve.Affine.natCard_point_le_two_mul_natCard_add_one`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#nat-card-point-le-two-mul-nat-card-add-o).

## Point count from the Frobenius trace

Let $W$ be a Weierstrass curve over a finite field
$F$ with $q$ elements, and let $\#W(F)$ be the number of nonsingular $F$-points of $W$, counting
the point at infinity. Then $\#W(F) = q + 1 - a_q(W)$, where $a_q(W)$ is the Frobenius trace of
$W$.

Formalized by `WeierstrassCurve.Affine.natCard_point_eq_natCard_add_one_sub_frobeniusTrace`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#nat-card-point-eq-nat-card-add-one-sub-f).

## Point count plus Frobenius trace

Let $W$ be a Weierstrass curve over a finite field $F$
with $q$ elements, and let $\#W(F)$ be the number of nonsingular $F$-points of $W$, counting the
point at infinity. Then $\#W(F) + a_q(W) = q + 1$, where $a_q(W)$ is the Frobenius trace of $W$.

Formalized by `WeierstrassCurve.Affine.natCard_point_add_frobeniusTrace_eq`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/PointCount.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#nat-card-point-add-frobenius-trace-eq).

## Waterhouse's theorem on Frobenius traces

Let $p$ be a prime, let $a \ge 1$, and let $F$
be a finite field with $q = p^a$ elements. An integer $\beta$ is the Frobenius trace
$q + 1 - \#E(F)$ of some elliptic curve $E$ over $F$ if and only if $\beta^2 \le 4q$ and one of
the following holds:
1. $\gcd(\beta, p) = 1$;
2. $a$ is even and $\beta = \pm 2p^{a/2}$;
3. $a$ is even, $p \not\equiv 1 \pmod 3$ and $\beta = \pm p^{a/2}$;
4. $a$ is odd, $p = 2$ or $p = 3$, and $\beta = \pm p^{(a+1)/2}$;
5. $a$ is odd, or $a$ is even and $p \not\equiv 1 \pmod 4$, and $\beta = 0$.

The paper states a one-to-one correspondence between $F$-isogeny classes of elliptic curves and
these integers; the statement above describes its image. Injectivity is Tate's isogeny theorem.

## Sources

- Daniel Vallières, *Elliptic Curves over Finite Fields and Ramanujan Graphs on Two Vertices*, INTEGERS 24 (2024), Article A8, Theorem 6.

Stated but not proved: `MetaMathlibExt.exists_isElliptic_frobeniusTrace_eq_iff` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#exists-is-elliptic-frobenius-trace-eq-if).

## Ihara's criterion for Ramanujan graphs

Let $q \ge 2$ be a natural number and let $A$ be a
symmetric $n \times n$ matrix with integer entries. Every complex root $\mu \ne q + 1$ of the
characteristic polynomial of $A$ satisfies $|\mu| \le 2\sqrt{q}$ if and only if, for every such
root $\mu \ne q + 1$, every complex number $s$ with $1 - \mu q^{-s} + q^{1 - 2s} = 0$ has real
part $1/2$.

When $A$ is the adjacency matrix of a $(q + 1)$-regular graph $X$, the left side says that $X$ is
Ramanujan. Writing $\zeta_X$ for the Ihara zeta function of $X$, the numbers $s$ on the right are
the non-trivial zeros of $Q_X(s) = \zeta_X(q^{-s})^{-1}$, that is, the zeros of
$P_X(q^{-s}) = \prod_{\mu \ne q + 1} (1 - \mu q^{-s} + q^{1 - 2s})$. The roots $\mu$ are real
because $A$ is symmetric. The paper also assumes that $X$ is connected and regular and has at
least two vertices; these assumptions are not needed, since the equivalence holds root by root.

## Sources

- Daniel Vallières, *Elliptic Curves over Finite Fields and Ramanujan Graphs on Two Vertices*, INTEGERS 24 (2024), Article A8, Theorem 2.

Stated but not proved: `MetaMathlibExt.ramanujan_iff_nontrivial_zeros_re_eq_half` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#ramanujan-iff-nontrivial-zeros-re-eq-hal).

## Ramanujan graphs give Weil numbers

Let $q$ be a natural number and let $A$ be a symmetric
$n \times n$ matrix with integer entries such that every complex root $\mu \ne q + 1$ of its
characteristic polynomial satisfies $|\mu| \le 2\sqrt{q}$. Let $\mu \ne q + 1$ be a complex root
of the characteristic polynomial of $A$ and let $\alpha \in \mathbb{C}$ satisfy
$\alpha^2 - \mu\alpha + q = 0$. Then $\alpha$ is an algebraic integer, and every complex root of
the minimal polynomial of $\alpha$ over $\mathbb{Q}$ has absolute value $\sqrt{q}$; that is,
$\alpha$ is a Weil $q$-number.

When $A$ is the adjacency matrix of a $(q + 1)$-regular graph $X$, the hypothesis says that $X$ is
Ramanujan, and the numbers $\alpha$ are the inverse roots of
$P_X(u) = \prod_{\mu \ne q + 1} (1 - \mu u + q u^2)$. The paper takes $q = p^a$ and $X$
connected; neither assumption is needed.

## Sources

- Daniel Vallières, *Elliptic Curves over Finite Fields and Ramanujan Graphs on Two Vertices*, INTEGERS 24 (2024), Article A8, Proposition 1.

Stated but not proved: `MetaMathlibExt.isWeilNumber_of_ramanujan` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#is-weil-number-of-ramanujan).

## Elliptic curves with point count divisible by 4 and Ramanujan graphs on two vertices

Let
$p$ be an odd prime, let $a \in \{1, 2\}$, and let $F$ be a finite field with $q = p^a$ elements. A
natural number $N$ is the number $\#E(F)$ of $F$-points (counting the point at infinity) of some
elliptic curve $E$ over $F$ with $4 \mid N$ if and only if there are natural numbers $l$ and $m$
with $N = 2m$, $2l + m = q + 1$, $m > 0$ and $(2l - m)^2 \le 4q$.

In graph terms, $X(l, m)$ is the two-vertex graph with $l$ loops at each vertex and $m$ edges
between the two vertices. For such $l$ and $m$ it is $(q + 1)$-regular, it is connected exactly
when $m > 0$, and its non-trivial eigenvalue is $2l - m$, so the last condition says that $X(l, m)$
is Ramanujan. The paper states a bijection from $F$-isogeny classes of such curves to these
graphs; the statement above is its point-count form, and injectivity on isogeny classes is Tate's
theorem.

## Sources

- Daniel Vallières, *Elliptic Curves over Finite Fields and Ramanujan Graphs on Two Vertices*, INTEGERS 24 (2024), Article A8, Theorem 8.

Stated but not proved: `MetaMathlibExt.exists_isElliptic_card_eq_iff_ramanujan_two_vertices` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#exists-is-elliptic-card-eq-iff-ramanujan).

## Ordinary elliptic curves with point count divisible by 4 and Ramanujan graphs on two vertices

**Ordinary elliptic curves with point count divisible by 4 and Ramanujan graphs on two
vertices.** Let $p$ be an odd prime, let $a \ge 1$, and let $F$ be a finite field with $q = p^a$
elements. A natural number $N$ is the number $\#E(F)$ of $F$-points (counting the point at
infinity) of some elliptic curve $E$ over $F$ with $4 \mid N$ whose Frobenius trace
$q + 1 - \#E(F)$ is coprime to $p$ if and only if there are natural numbers $l$ and $m$ with
$N = 2m$, $2l + m = q + 1$, $m > 0$, $(2l - m)^2 \le 4q$ and $2m \not\equiv 1 \pmod p$.

A Frobenius trace coprime to $p$ is the paper's criterion for $E$ to be ordinary; since $p \mid q$,
the trace $q + 1 - 2m$ is coprime to $p$ exactly when $2m \not\equiv 1 \pmod p$. In graph terms,
$X(l, m)$ is the two-vertex graph with $l$ loops at each vertex and $m$ edges between the two
vertices; it is $(q + 1)$-regular, connected exactly when $m > 0$, and Ramanujan exactly when
$(2l - m)^2 \le 4q$. The paper states a bijection from $F$-isogeny classes of such curves to these
graphs; the statement above is its point-count form, and injectivity on isogeny classes is Tate's
theorem.

## Sources

- Daniel Vallières, *Elliptic Curves over Finite Fields and Ramanujan Graphs on Two Vertices*, INTEGERS 24 (2024), Article A8, Theorem 9.

Stated but not proved: `MetaMathlibExt.exists_ordinary_card_eq_iff_ramanujan_two_vertices` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/EllipticCurve/WaterhouseTracesWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html#exists-ordinary-card-eq-iff-ramanujan-tw).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Point counts and Frobenius traces](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/point-counts-and-frobenius-traces)
