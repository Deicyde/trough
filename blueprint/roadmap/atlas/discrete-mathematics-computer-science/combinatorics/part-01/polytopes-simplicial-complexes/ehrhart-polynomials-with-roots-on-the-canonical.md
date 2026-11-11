---
declaration: section
origin: cited
lean: MetaMathlibExt.canonicalLine, MetaMathlibExt.hStarCoeff, MetaMathlibExt.IsSNN, MetaMathlibExt.clQuadraticProduct, MetaMathlibExt.IsCLWithParameters, MetaMathlibExt.IsCL, MetaMathlibExt.bBasis, MetaMathlibExt.pBasis
statement: formalized
---

# Ehrhart polynomials with roots on the canonical line

47 results, 29 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html).

## Canonical line

The canonical line $\mathrm{CL}$ is the vertical line of complex numbers
with real part $-1/2$, that is, $\mathrm{CL} = \{z \in \mathbb{C} : \operatorname{Re} z = -1/2\}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Definition of `CL`.

Formalized by `MetaMathlibExt.canonicalLine`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#canonical-line).

## The h-star coefficients of a polynomial

Let $f$ be a complex polynomial of degree $d$,
with $d = 0$ for the zero polynomial. For a natural number $i$, the $i$-th $h^*$-coefficient of
$f$ is

$$h^*_i(f) = \sum_{j=0}^{i} (-1)^j \binom{d+1}{j} f(i-j),$$

the coefficient of $t^i$ in the power series $(1-t)^{d+1} \sum_{k \ge 0} f(k)\, t^k$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of the `h*`-polynomial.

Formalized by `MetaMathlibExt.hStarCoeff`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#h-star-coeff).

## SNN polynomials

For a complex polynomial $f$ of degree $d$ and a natural number $i$, let
$h^*_i(f)$ be the coefficient of $t^i$ in $(1 - t)^{d+1} \sum_{k \ge 0} f(k)\, t^k$. Then $f$ is
SNN when $f \ne 0$ and its $h^*$-coefficients $h^*_0(f), \dots, h^*_d(f)$ are real and
nonnegative.

Coefficients beyond the degree, which vanish by the generating-series identity, are not part of
the condition.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of SNN-polynomial.

Formalized by `MetaMathlibExt.IsSNN`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#is-snn).

## Product of quadratic canonical-line factors

For a finite list $c_1, \dots, c_m$ of real
numbers, this is the monic complex polynomial $\prod_{k=1}^{m} (X^2 + X + c_k)$; the empty list
gives the constant polynomial $1$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, factored definition of CL-polynomials.

Formalized by `MetaMathlibExt.clQuadraticProduct`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#cl-quadratic-product).

## CL-polynomials with given parameters

Let $f$ be a complex polynomial of degree $d$, let
$a$ be a real number, and let $c_1, \dots, c_m$ be a list of real numbers. Then $f$ is a
CL-polynomial with scale $a$ and parameters $c_1, \dots, c_m$ when $a \ne 0$, every $c_i \ge 1/4$,
$m = \lfloor d/2 \rfloor$, and $f = a \prod_{i=1}^{m} (X^2 + X + c_i)$ if $d$ is even and
$f = a (2X + 1) \prod_{i=1}^{m} (X^2 + X + c_i)$ if $d$ is odd.

The parameters form a list so that later statements can refer to individual parameters.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of CL-polynomial.

Formalized by `MetaMathlibExt.IsCLWithParameters`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#is-clwith-parameters).

## CL-polynomials

A complex polynomial $f$ of degree $d$ is a CL-polynomial when there are
a real number $a \ne 0$ and real numbers $c_1, \dots, c_m \ge 1/4$ with $m = \lfloor d/2 \rfloor$
such that $f = a \prod_{i=1}^{m} (X^2 + X + c_i)$ if $d$ is even and
$f = a (2X + 1) \prod_{i=1}^{m} (X^2 + X + c_i)$ if $d$ is odd.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of CL-polynomial.

Formalized by `MetaMathlibExt.IsCL`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#is-cl).

## The basis polynomials $b^d_j$

For natural numbers $d$ and $j$, $b^d_j$ is the complex
polynomial $b^d_j = \prod_{i=0}^{d-1} (X + d - j - i)$.

Integer constants are used before mapping to $\mathbb{C}$, avoiding any convention about rising
versus falling Pochhammer symbols.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of `bᵈⱼ`.

Formalized by `MetaMathlibExt.bBasis`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#b-basis).

## Symmetric basis polynomials

For natural numbers $d$ and $j$, let $b^d_j$ be the complex
polynomial $\prod_{i=0}^{d-1} (X + d - j - i)$. The polynomial $p^d_j$ is $b^d_j$ if $2j = d$, and
$b^d_j + b^d_{d-j}$ otherwise, where $d - j$ is truncated at $0$ (so $p^d_j = b^d_j + b^d_0$ when
$j > d$).

Statements that use $p^d_j$ assume $j \le d$, where the truncation plays no role.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of `pᵈⱼ`.

Formalized by `MetaMathlibExt.pBasis`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis).

## The basis polynomial $p^1_0$

The symmetric basis polynomial $p^1_0$ equals the complex
polynomial $2X + 1$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, characteristic case of the `pᵈⱼ` definition.

Formalized by `MetaMathlibExt.pBasis_one_zero`, a theorem declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis-one-zero).

## The basis polynomial $p^2_0$

The symmetric basis polynomial $p^2_0$ equals the complex
polynomial $2(X^2 + X + 1)$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, characteristic case of the `pᵈⱼ` definition.

Formalized by `MetaMathlibExt.pBasis_two_zero`, a theorem declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis-two-zero).

## Interlacing lists

Let $r$ be a binary relation on a type $\alpha$ and let $d \ge 0$.
A list $(a_1, \dots, a_d)$ interlaces a list $(b_1, \dots, b_{d+1})$ with respect to $r$ when
$b_1 \mathrel{r} a_1 \mathrel{r} b_2 \mathrel{r} \cdots \mathrel{r} a_d \mathrel{r} b_{d+1}$,
that is, $b_k \mathrel{r} a_k$ and $a_k \mathrel{r} b_{k+1}$ for $1 \le k \le d$. Two lists
interlace only when the second has exactly one more entry than the first; in particular the
empty list interlaces every one-element list.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of interlacing.

Formalized by `MetaMathlibExt.ListInterlaces`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#list-interlaces).

## Alternating lists of equal length

Let $r$ be a binary relation on a type $\alpha$ and
let $n \ge 0$. A list $(a_1, \dots, a_n)$ alternates with a list $(b_1, \dots, b_n)$ with
respect to $r$ when
$a_1 \mathrel{r} b_1 \mathrel{r} a_2 \mathrel{r} \cdots \mathrel{r} a_n \mathrel{r} b_n$,
that is, $a_k \mathrel{r} b_k$ for $1 \le k \le n$ and $b_k \mathrel{r} a_{k+1}$ for
$1 \le k < n$. Two empty lists alternate, and lists of different lengths never alternate.

This equal-length companion of interlacing is used only for the same-degree clauses in Fisk's
Leibniz rule.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 2 (quoting Fisk, Lemma 1.26).

Formalized by `MetaMathlibExt.ListAlternates`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#list-alternates).

## Real interlacing

Let $f$ and $g$ be real polynomials. Then $f$ interlaces $g$ when $f$ and
$g$ are nonzero with $\deg g = \deg f + 1$, the real roots of $f$, listed with multiplicity, are
exactly $a_1 \le \dots \le a_d$ where $d = \deg f$, the real roots of $g$, listed with
multiplicity, are exactly $b_1 \le \dots \le b_{d+1}$ (so all roots of $f$ and $g$ are real), and
the roots alternate as $b_1 \le a_1 \le b_2 \le a_2 \le \dots \le a_d \le b_{d+1}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of real interlacing.

Formalized by `MetaMathlibExt.RealInterlaces`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#real-interlaces).

## Alternating roots of equal-degree real polynomials

Let $f$ and $g$ be real polynomials.
Their roots alternate when $f$ and $g$ are nonzero of the same degree $n$, the real roots of $f$,
listed with multiplicity, are exactly $a_1 \le \dots \le a_n$, those of $g$ are exactly
$b_1 \le \dots \le b_n$ (so all roots of $f$ and $g$ are real), and either
$a_1 \le b_1 \le a_2 \le b_2 \le \dots \le a_n \le b_n$ or
$b_1 \le a_1 \le b_2 \le a_2 \le \dots \le b_n \le a_n$.

This equal-degree notion is used for two clauses of Fisk's Leibniz rule.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 2 (quoting Fisk, Lemma 1.26).

Formalized by `MetaMathlibExt.RealAlternates`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#real-alternates).

## Interlacing on the canonical line

A complex polynomial $f$ CL-interlaces a complex
polynomial $g$ when $f$ and $g$ are nonzero, $\deg g = \deg f + 1$, all roots of $f$ and of $g$
lie on the canonical line, and, writing $d = \deg f$ and listing the roots with multiplicity as
$a_1, \dots, a_d$ for $f$ and $b_1, \dots, b_{d+1}$ for $g$, each list sorted by increasing
imaginary part, they alternate:
$\operatorname{Im} b_1 \le \operatorname{Im} a_1 \le \operatorname{Im} b_2 \le \cdots \le
\operatorname{Im} a_d \le \operatorname{Im} b_{d+1}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of CL-interlacing.

Formalized by `MetaMathlibExt.CLInterlaces`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#clinterlaces).

## Real-rooted polynomials

A real polynomial $f$ has only real roots when $f \ne 0$ and the
number of real roots of $f$, counted with multiplicity, equals the degree of $f$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 2 (quoting Fisk, Lemma 1.26).

Formalized by `MetaMathlibExt.HasOnlyRealRoots`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#has-only-real-roots).

## Lattice points as real points

A lattice point $x = (x_1, \dots, x_d) \in \mathbb{Z}^d$
is regarded as the point of $\mathbb{R}^d$ with the same coordinates $x_1, \dots, x_d$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of a lattice polytope.

Formalized by `MetaMathlibExt.latticePointToReal`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#lattice-point-to-real).

## Lattice polytopes

The lattice polytope spanned by a finite set $V \subseteq \mathbb{Z}^d$
is the convex hull in $\mathbb{R}^d$ of the points of $V$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of a lattice polytope.

Formalized by `MetaMathlibExt.latticePolytope`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#lattice-polytope).

## Full-dimensional sets

A subset $P$ of $\mathbb{R}^d$ is full-dimensional when it is
nonempty and the direction of its affine span is all of $\mathbb{R}^d$ (equivalently, the affine
span of $P$ is $\mathbb{R}^d$).

Nonemptiness matters only for $d = 0$: the empty subset of $\mathbb{R}^0$ has an affine span
whose direction $\{0\}$ is all of $\mathbb{R}^0$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, full-dimensional lattice-polytope convention.

Formalized by `MetaMathlibExt.IsFullDimensional`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#is-full-dimensional).

## Polynomial counting the lattice points of dilates

Let $V \subseteq \mathbb{Z}^d$ be a
finite set and let $P \subseteq \mathbb{R}^d$ be the lattice polytope spanned by $V$, its convex
hull. A complex polynomial $E$ counts the lattice points of $P$ when, for every natural number
$k$, $E(k)$ equals the ordinary Ehrhart count $|kP \cap \mathbb{Z}^d|$, the number of points of
$\mathbb{Z}^d$ of the form $kx$ with $x$ a rational point of $P$.

By Ehrhart's theorem such a polynomial exists, and it is unique.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of the Ehrhart polynomial.

Formalized by `MetaMathlibExt.EhrhartCounts`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#ehrhart-counts).

## Binomial polynomial

For an integer $n$ and a natural number $d$, the binomial polynomial
$\binom{X+n}{d}$ is the real polynomial $\frac{1}{d!} \prod_{i=0}^{d-1} (X + n - i)$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 7.

Formalized by `MetaMathlibExt.binomialPolynomial`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#binomial-polynomial).

## Complex binomial polynomial

For an integer $n$ and a natural number $d$, the complex
binomial polynomial $\binom{X+n}{d} \in \mathbb{C}[X]$ is

$$\binom{X+n}{d} = \frac{1}{d!} \prod_{i=0}^{d-1} (X + n - i).$$

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 3 (quoting Braun and Develin, Theorem 2.3).

Formalized by `MetaMathlibExt.complexBinomialPolynomial`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#complex-binomial-polynomial).

## Model polynomial

For a natural number $d$, the model polynomial is the complex
polynomial $M_d = \binom{X+d}{d} + \binom{X}{d}$, where for an integer $n$ the binomial
polynomial $\binom{X+n}{d}$ is $\frac{1}{d!}\prod_{i=0}^{d-1} (X + n - i)$.

For $d \ge 1$, $d!\,M_d$ is the symmetric basis polynomial $p^d_0$; the paper emphasizes that
$M_d$ need not be an Ehrhart polynomial.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 3 (quoting Braun and Develin, Theorem 2.3).

Formalized by `MetaMathlibExt.modelPolynomial`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#model-polynomial).

## Property (♢)

For a complex polynomial $f$ of degree $d$ and a natural number $i$, let
$h^*_i(f)$ be the coefficient of $t^i$ in $(1 - t)^{d+1} \sum_{k \ge 0} f(k)\, t^k$. Then $f$ has
property (♢) when $f \ne 0$ and its $h^*$-coefficients $h^*_0(f), \dots, h^*_d(f)$ are real,
nonnegative and palindromic, that is, $h^*_i(f) = h^*_{d-i}(f)$ for $0 \le i \le d$.

For CL-polynomials the paper notes that palindromicity is automatic; it is kept here as part of
the property.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of `(♢)`.

Formalized by `MetaMathlibExt.HasDiamond`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#has-diamond).

## The set $\Omega_d$ of attainable canonical-line roots

For a natural number $d$,
$\Omega_d$ is the set of complex numbers $z$ on the canonical line such that $z$ is a root of
some CL-polynomial of degree $d$ satisfying $(\diamondsuit)$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, definition of `Ω_d`.

Formalized by `MetaMathlibExt.canonicalLineRootSet`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#canonical-line-root-set).

## Functional equation versus palindromic h-star coefficients

Let $f$ be a nonzero complex
polynomial of degree $d$ with $h^*$-coefficients $h^*_0(f), \dots, h^*_d(f)$. Then
$f(X-1) = (-1)^d f(-X)$ as polynomials if and only if $h^*_i(f) = h^*_{d-i}(f)$ for every
$i \le d$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 1 (quoting Corollary 2.2 in Kölbl's [11]).

Stated but not proved: `MetaMathlibExt.functionalEquation_iff_hStar_palindromic` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#functional-equation-iff-h-star-palindrom).

## Values of CL-polynomials on the canonical line

If $f$ is a CL-polynomial of degree $d$,
then for every $z$ on the canonical line there is a real number $r$ with $f(z) = r\, i^d$; that
is, $f$ maps the canonical line into $\mathbb{R}\, i^d$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 2.

Stated but not proved: `MetaMathlibExt.cl_value_on_canonicalLine` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#cl-value-on-canonical-line).

## $p^d_0$ CL-interlaces $p^{d+1}_0$

For every natural number $d \ge 1$, the symmetric
basis polynomial $p^d_0$ CL-interlaces $p^{d+1}_0$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 4.

Stated but not proved: `MetaMathlibExt.pBasis_zero_interlaces_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis-zero-interlaces-succ).

## CL-interlacing of $p^d_0$ with a perturbation of $p^{d+1}_0$

For every natural number
$d \ge 1$ and every real number $w > 0$, the symmetric basis polynomial $p^d_0$ CL-interlaces
the polynomial $p^{d+1}_0 + w \, (2X + 1) \, p^d_0$.

The orientation follows the numbered statement in the INTEGERS version; the arXiv wording
differs.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 5.

Stated but not proved: `MetaMathlibExt.pBasis_zero_interlaces_perturbation` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis-zero-interlaces-perturbation).

## Multiplying by $2X+1$ preserves SNN

For every complex polynomial $f$, if $f$ is an SNN
polynomial, then so is $(2X + 1) f$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 6.

Stated but not proved: `MetaMathlibExt.two_mul_X_add_one_preserves_snn` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#two-mul-x-add-one-preserves-snn).

## Multiplying a binomial polynomial by a quadratic

For an integer $n$ and a natural number
$k$, write $\binom{X+n}{k} = \frac{1}{k!} \prod_{i=0}^{k-1} (X + n - i)$ for the real binomial
polynomial. Let $d$ and $j$ be natural numbers with $0 < d$ and $j \le d$, and let $c$ be a real
number. Then

$$
(X^2 + X + c) \binom{X+d-j}{d} = \alpha \binom{X+d-j+2}{d+2} + \beta \binom{X+d-j+1}{d+2} +
\gamma \binom{X+d-j}{d+2},
$$

where $\alpha = j^2 + j + c$, $\beta = 2(dj - j^2 + d + 1 - c)$ and
$\gamma = d^2 - 2dj - j + j^2 + d + c$.

The paper assumes $c \ge 1/4$; the identity holds for every real $c$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 7.

Stated but not proved: `MetaMathlibExt.quadratic_mul_binomialPolynomial` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#quadratic-mul-binomial-polynomial).

## Fisk's Leibniz rule for interlacing

Let $f, f_1, g, g_1$ be real polynomials with
positive leading coefficients, each having only real roots, such that $f$ and $g$ have no common
real root, $f_1$ interlaces $f$, and $g_1$ interlaces $g$. Then $f_1 g_1$ interlaces
$f g_1 + f_1 g$, the polynomial $f g_1 + f_1 g$ interlaces $f g$, the roots of $f g_1 + f_1 g$
alternate with those of $f g_1$ and with those of $f_1 g$, and $f g_1 + f_1 g$ has only real
roots.

Here $p$ interlaces $q$ when $p$ and $q$ are nonzero, $\deg q = \deg p + 1$, and both have only
real roots, whose sorted lists $a_1 \le \dots \le a_n$ and $b_1 \le \dots \le b_{n+1}$ (with
multiplicity) satisfy $b_1 \le a_1 \le b_2 \le \dots \le a_n \le b_{n+1}$. The roots of $p$ and
$q$ alternate when $p$ and $q$ are nonzero of the same degree $n$ and have only real roots, whose
sorted lists satisfy $a_1 \le b_1 \le \dots \le a_n \le b_n$ or
$b_1 \le a_1 \le \dots \le b_n \le a_n$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 2 (quoting Fisk, Lemma 1.26, “Leibnitz rule”).

Stated but not proved: `MetaMathlibExt.leibniz_rule_interlacing` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#leibniz-rule-interlacing).

## Coefficientwise limits preserve real interlacing

Let $(f_n)$ and $(g_n)$ be sequences
of real polynomials with only real roots, and let $f$ and $g$ be nonzero real polynomials such
that, for every $k$, the coefficient of $X^k$ in $f_n$ tends to that in $f$ and the coefficient
of $X^k$ in $g_n$ tends to that in $g$ as $n \to \infty$. Suppose that for all sufficiently
large $n$ the degree of $f_n$ equals the degree of $f$ and the degree of $g_n$ equals the degree
of $g$, and that $f_n$ interlaces $g_n$ for every $n$, in the sense of real interlacing. Then $f$
interlaces $g$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 3 (quoting Fisk, Corollary 1.41).

Stated but not proved: `MetaMathlibExt.coefficientwise_limit_interlaces` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#coefficientwise-limit-interlaces).

## Small sorted CL parameters give an SNN polynomial

Let $f$ be a complex polynomial of
degree $d$, let $a > 0$ be real, and let $c_0 \le c_1 \le \dots \le c_{m-1}$ be real numbers, each
at least $1/4$, with $m = \lfloor d/2 \rfloor$, such that $f = a \prod_{k=0}^{m-1} (X^2 + X + c_k)$
if $d$ is even and $f = a (2X + 1) \prod_{k=0}^{m-1} (X^2 + X + c_k)$ if $d$ is odd. Suppose that
$c_k \le 2k + 2$ for every $k$ when $d$ is odd, and $c_k \le 2k + 1$ for every $k$ when $d$ is
even. Then $f$ is an SNN polynomial.

The hypothesis $a > 0$ is needed: for $d = 1$, $a = -1$ and no parameters, $f = -(2X + 1)$ is not
SNN, since its zeroth $h^*$-coefficient is $f(0) = -1 < 0$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 5.

Stated but not proved: `MetaMathlibExt.sorted_cl_parameters_are_snn` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#sorted-cl-parameters-are-snn).

## Classical bounds on Ehrhart roots

Let $P \subseteq \mathbb{R}^d$ be a full-dimensional
lattice polytope, the convex hull of a finite set of points of $\mathbb{Z}^d$, and let $E$ be a
complex polynomial with $E(k) = |kP \cap \mathbb{Z}^d|$ for every natural number $k$. Then every
complex root $\alpha$ of $E$ satisfies $|\alpha| \le 1 + (d+1)!$, and every real root $\alpha$
of $E$ satisfies $-d \le \alpha < \lfloor d/2 \rfloor$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 1 (quoting Beck, De Loera, Develin, Pfeifle, and Stanley, Theorem 1.2).

Stated but not proved: `MetaMathlibExt.ehrhart_root_classical_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#ehrhart-root-classical-bounds).

## Braun's disc for Ehrhart roots

Let $P \subseteq \mathbb{R}^d$ be a full-dimensional
lattice polytope, the convex hull of a finite set of points of $\mathbb{Z}^d$, and let $E$ be a
complex polynomial with $E(k) = |kP \cap \mathbb{Z}^d|$ for every natural number $k$. Then every
root $\alpha$ of $E$ lies in the closed disc centered at $-1/2$ with radius $d(d - 1/2)$, that
is, $|\alpha + 1/2| \le d(d - 1/2)$.

By Ehrhart's theorem, $E$ has degree $d$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 2 (quoting Braun, Theorem 1).

Stated but not proved: `MetaMathlibExt.ehrhart_roots_in_braun_disc` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#ehrhart-roots-in-braun-disc).

## Asymptotics of the largest root of the model polynomial

For $d \ge 0$ let
$M_d = \binom{X+d}{d} + \binom{X}{d}$ be the model polynomial. Let $(\beta_d)_{d \ge 0}$ be a
sequence of complex numbers such that for every $d \ge 1$, $\beta_d$ is a root of $M_d$ and
$|\gamma| \le |\beta_d|$ for every root $\gamma$ of $M_d$. Then
$|\beta_d + \tfrac12| - d^2/\pi = O(1)$ as $d \to \infty$.

No condition is placed on $\beta_0$ because $M_0$ is constant; this does not affect the
asymptotic statement.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 3 (quoting Braun and Develin, Theorem 2.3).

Stated but not proved: `MetaMathlibExt.maximal_model_root_asymptotic` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#maximal-model-root-asymptotic).

## Hibi's lower bound

Let $P \subseteq \mathbb{R}^d$ be the lattice polytope spanned by a
finite set of points of $\mathbb{Z}^d$, and suppose that $P$ is full-dimensional. Let $E$ be a
complex polynomial with $E(k) = |kP \cap \mathbb{Z}^d|$ for every natural number $k$, and write
$h^*_i$ for the $h^*$-coefficients of $E$. If $h^*_d \ne 0$, then
$\operatorname{Re} h^*_1 \le \operatorname{Re} h^*_k$ for every $k$ with $1 \le k < d$.

The $h^*$-coefficients are defined as complex numbers, so the inequality compares real parts.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 5 (quoting Hibi's lower bound theorem).

Stated but not proved: `MetaMathlibExt.hibi_lower_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#hibi-lower-bound).

## The set of attainable canonical-line roots is connected

For every positive integer $d$,
the set $\Omega_d$ of canonical-line roots of degree-$d$ CL-polynomials satisfying
$(\diamondsuit)$ is a nonempty connected subset of $\mathbb{C}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 6.

Stated but not proved: `MetaMathlibExt.canonicalLineRootSet_isConnected` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#canonical-line-root-set-is-connected).

## Parameter bound for SNN CL-polynomials

Let $f$ be a complex polynomial of degree $d$
that is a CL-polynomial with real scale $a$ and list of real parameters $c_1, \dots, c_m$, and
suppose that $f$ is SNN. Then for each parameter $c_k$ there is a real number $\beta$ such that
$-\tfrac12 + \beta i$ is a root of the symmetric basis polynomial $p^d_0$ and
$c_k \le \tfrac14 + \beta^2$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 7 (restatement of Theorem 4).

Stated but not proved: `MetaMathlibExt.cl_parameter_bounded_by_pBasis_root` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#cl-parameter-bounded-by-p-basis-root).

## CL-span

The CL-span of a complex polynomial $f$ is the convex hull, in $\mathbb{C}$
viewed as a real vector space, of the set of roots of $f$ lying on the canonical line, the line
of complex numbers with real part $-1/2$. Here the zero polynomial is regarded as having no
roots, so its CL-span is empty.

When nonempty, the CL-span is an interval of the canonical line.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Section 2 (definition of `clspan`).

Formalized by `MetaMathlibExt.clspan`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#clspan).

## CL-span of the zero polynomial

The zero polynomial has empty CL-span (its root multiset
is empty).

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Section 2 (definition of `clspan`).

Formalized by `MetaMathlibExt.clspan_zero`, a theorem declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#clspan-zero).

## Vertices of the standard reflexive simplex

For a natural number $d$, this is the finite
set of integer points $\{e_1, \dots, e_d, (-1, \dots, -1)\} \subseteq \mathbb{Z}^d$, where
$e_1, \dots, e_d$ are the standard basis vectors of $\mathbb{Z}^d$, so that
$(-1, \dots, -1) = -(e_1 + \dots + e_d)$. These points are the vertices of the standard
reflexive simplex $\Delta^d_{\mathrm{sr}}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Section 2.2 (definition of `Δᵈ_sr`).

Formalized by `MetaMathlibExt.standardReflexiveSimplexVertices`, a definition declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#standard-reflexive-simplex-vertices).

## The all-minus-one vector is a vertex of the standard reflexive simplex

For every natural
number $d$, let $e_1, \dots, e_d$ be the standard basis vectors of $\mathbb{Z}^d$. Then the
point $-(e_1 + \dots + e_d) = (-1, \dots, -1)$ belongs to the vertex set
$\{e_1, \dots, e_d, -(e_1 + \dots + e_d)\}$ of the standard reflexive simplex $\Delta^d_{sr}$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Section 2.2 (definition of `Δᵈ_sr`).

Formalized by `MetaMathlibExt.neg_one_mem_standardReflexiveSimplexVertices`, a theorem declared in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#neg-one-mem-standard-reflexive-simplex-v).

## The symmetric basis polynomials on the canonical line

Let $d \ge 1$ and $j$ be natural
numbers with $2j \le d$, let $p^d_j$ be the symmetric basis polynomial, and let $i$ be the
imaginary unit. Then:
(a) the real part of $p^d_j(it - \tfrac12) / i^d$ tends to $+\infty$ as the real number $t$
tends to $+\infty$;
(b) if $2j \ne d$, then for every real $t$ we have $p^d_j(it - \tfrac12) = 0$ if and only if
there is a real number $r$ with
$\prod_{k=0}^{d-2j-1} \bigl(it - \tfrac12 + (d - j) - k\bigr) = r \, i^{d-2j+1}$, that is,
the falling factorial $(it - \tfrac12 + d - j)_{d-2j}$ lies in $\mathbb{R} \, i^{d-2j+1}$;
(c) if $j \ge 1$, then the CL-span of $p^d_j$ is contained in the CL-span of $p^d_{j-1}$.

The values in (a) are real by Remark 1 of the paper. The paper also allows $d = 0$, where (a)
fails because $p^0_0 = 1$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Lemma 3.

Stated but not proved: `MetaMathlibExt.pBasis_canonicalLine_properties` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#p-basis-canonical-line-properties).

## CL-span bound for SNN CL-polynomials

Let $f$ be a complex polynomial of degree $d$ that
is both a CL-polynomial and an SNN polynomial. Then the CL-span of $f$ is contained in the
CL-span of the symmetric basis polynomial $p^d_0$.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Theorem 4.

Stated but not proved: `MetaMathlibExt.clspan_subset_clspan_pBasis_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#clspan-subset-clspan-p-basis-zero).

## Ehrhart CL-spans of reflexive polytopes in dimension at most 9

Let $d \le 9$, let
$P \subseteq \mathbb{R}^d$ be the convex hull of a finite set of integer points, and suppose
that $P$ is reflexive. Let $\Delta^d_{sr}$ be the standard reflexive simplex, with vertices
$e_1, \dots, e_d$ and $-(e_1 + \cdots + e_d)$. Let $E$ and $E'$ be complex polynomials such
that, for every natural number $k$, $E(k)$ is the number of integer points of $kP$ and $E'(k)$
is the number of integer points of $k\Delta^d_{sr}$. Then
$\operatorname{clspan} E \subseteq \operatorname{clspan} E'$.

Reflexivity is Hibi's interior-point characterization, up to a lattice translation, which does
not change the Ehrhart polynomial.

## Sources

- Max Kölbl, *Properties of Ehrhart Polynomials Whose Roots Lie on the Canonical Line*, INTEGERS 25 (2025), Article A68, Proposition 4.

Stated but not proved: `MetaMathlibExt.clspan_ehrhart_subset_standardReflexiveSimplex` is written with `theorem_wanted` in [WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/CanonicalLineEhrhartWanted.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html#clspan-ehrhart-subset-standard-reflexive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ehrhart polynomials with roots on the canonical line](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/ehrhart-polynomials-with-roots-on-the-canonical)
