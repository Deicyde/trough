---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.kcomm, MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelComm, MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.IsEngel, MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLength, MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLengthPolynomialBound, MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLengthPolynomialBound_refuted, MathlibExt.GroupTheory.EngelElementSimpleGroupKourovka16Problem17Wanted.IsEngelElement, MathlibExt.GroupTheory.EngelElementSimpleGroupKourovka16Problem17Wanted.simpleGroupNoNontrivialEngelElement
statement: formalized
---

# Engel elements

12 results, 9 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html).

## Commutator for Engel lengths

For elements $x$ and $y$ of a group, the commutator is
$[x, y] = x^{-1} y^{-1} x y$ (the convention of the Kourovka Notebook).

Formalized by `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.kcomm`, a definition declared in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#kcomm).

## Iterated commutators for Engel lengths

For elements $h$ and $g$ of a group and a natural
number $l$, the iterated commutator $[h, g; l]$ is defined by $[h, g; 0] = h$ and
$[h, g; l + 1] = [[h, g; l], g]$, where $[x, y] = x^{-1} y^{-1} x y$; in particular
$[h, g; 1] = [h, g]$.

Formalized by `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelComm`, a definition declared in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#engel-comm).

## Bounded Engel element

An element $g$ of a group $G$ is an Engel element if there is an
$l \ge 1$ such that $[h, g; l] = 1$ for every $h \in G$, where $[h, g; 0] = h$,
$[h, g; i + 1] = [[h, g; i], g]$ and $[x, y] = x^{-1} y^{-1} x y$.

Formalized by `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.IsEngel`, a definition declared in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#is-engel).

## Engel length

For an element $g$ of a group $G$, the Engel length $l(g)$ is the least
$k \ge 1$ such that $[h, g; k] = 1$ for every $h \in G$, where $[h, g; 0] = h$,
$[h, g; i + 1] = [[h, g; i], g]$ and $[x, y] = x^{-1} y^{-1} x y$. If no such $k$ exists, that
is, if $g$ is not an Engel element, then $l(g) = 0$.

Formalized by `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLength`, a definition declared in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#engel-length).

## Roman'kov's problem on Engel lengths of products (Kourovka 11.88)

The statement that every
group $G$ has a polynomial $\varphi(x, y)$ in two variables with natural-number coefficients such
that $l(uv) \le \varphi(l(u), l(v))$ for all $u, v \in G$ for which $u$, $v$ and $uv$ are Engel
elements. Here $g \in G$ is an Engel element if there is a $k \ge 1$ with $[h, g; k] = 1$ for all
$h \in G$, and its Engel length $l(g)$ is the least such $k$, where $[h, g; 0] = h$,
$[h, g; i + 1] = [[h, g; i], g]$ and $[x, y] = x^{-1} y^{-1} x y$.

Natural coefficients lose nothing: on $\mathbb{N}^2$ every real polynomial is bounded by one with
natural coefficients.

Formalized by `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLengthPolynomialBound`, a definition declared in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#engel-length-polynomial-bound).

## Engel lengths of products admit no polynomial bound (Kourovka 11.88)

There is a group $G$
such that for every polynomial $\varphi(x, y)$ in two variables with natural-number coefficients
there are $u, v \in G$ such that $u$, $v$ and $uv$ are Engel elements and
$l(uv) > \varphi(l(u), l(v))$. Here $g \in G$ is an Engel element if there is a $k \ge 1$ with
$[h, g; k] = 1$ for all $h \in G$, and its Engel length $l(g)$ is the least such $k$, where
$[h, g; 0] = h$, $[h, g; i + 1] = [[h, g; i], g]$ and $[x, y] = x^{-1} y^{-1} x y$.

For a prime $p$, Dolbak builds finite $p$-groups $G_n$ (wreath products of a cyclic group of
order $p$ by groups $K_n$) with elements $c_n$ and $c_n^{-1} b_0$ of Engel length at most
$(n + 1)p - n + 1$ whose product $b_0$ has Engel length at least $p^n$. He takes the direct
product of the $G_n$ in the restricted sense (the direct sum, whose elements have finite support).
It is a single Engel group: an element of finite support has Engel length at most the largest
Engel length of its coordinates, and each $G_n$ is a finite $p$-group, hence nilpotent. (The
unrestricted product is not Engel: the element with $b_0$ in every coordinate has unbounded Engel
length.) Let $u_n$ and $v_n$ be $c_n$ and $c_n^{-1} b_0$ in coordinate $n$ and $1$ elsewhere: they
are Engel elements of length at most $(n + 1)p - n + 1$, and $u_n v_n$ has length at least $p^n$,
which exceeds every polynomial in the lengths of the factors (Theorem 1: there are Engel groups in
which the Engel length of a product of two elements is bounded by no polynomial in the Engel
lengths of the factors). The refutation of this statement uses only that $u_n$, $v_n$ and
$u_n v_n$ are Engel elements of one group. The Kourovka Archive answers 11.88 "No, it does not".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.88 (V. A. Roman'kov); resolution: L. V. Dolbak, The Engel length of the product of Engel elements, Siberian Math. J. 47, no. 1 (2006), 55-57, Theorem 1 and its proof; Kourovka Archive, Problem 11.88: "No, it does not", https://doi.org/10.1007/s11202-006-0006-9.

Stated but not proved: `MathlibExt.GroupTheory.EngelElementLengthPolynomialKourovka11Problem88Wanted.engelLengthPolynomialBound_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementLengthPolynomialKourovka11Problem88Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#engel-length-polynomial-bound-refuted).

## Engel element

An element $g$ of a group $G$ is an Engel element if for every $h \in G$
there is an $n \ge 0$ with $h_n = 1$, where $h_0 = h$ and $h_{i + 1} = [h_i, g]$ with
$[x, g] = x^{-1} g^{-1} x g$; that is, some iterated commutator $[h, g, \dots, g]$ is trivial.

Formalized by `MathlibExt.GroupTheory.EngelElementSimpleGroupKourovka16Problem17Wanted.IsEngelElement`, a definition declared in [WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#is-engel-element).

## Bludov's problem on Engel elements in simple groups (Kourovka 16.17)

The statement that no
non-abelian simple group contains an Engel element other than the identity: for every simple group
$G$ with elements $a$, $b$ such that $ab \ne ba$, every Engel element $g$ of $G$ satisfies $g = 1$.
Here $g$ is an Engel element if for every $h \in G$ some iterated commutator $[h, g, \dots, g]$ is
trivial, where $[x, g] = x^{-1} g^{-1} x g$.

Formalized by `MathlibExt.GroupTheory.EngelElementSimpleGroupKourovka16Problem17Wanted.simpleGroupNoNontrivialEngelElement`, a definition declared in [WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#simple-group-no-nontrivial-engel-element).

## Non-abelian simple groups can have nontrivial Engel elements (Kourovka 16.17)

There is a
non-abelian simple group $G$ (one with elements $a$, $b$ such that $ab \ne ba$) that contains
an Engel element $g \ne 1$. Here $g$ is an Engel element if for every $h \in G$ some iterated
commutator $[h, g, \dots, g]$ is trivial, where $[x, g] = x^{-1} g^{-1} x g$.

The Kourovka Archive answers 16.17 "No, it can" (Bludov): an involution is an Engel element in
any 2-group, so non-abelian simple 2-groups are counterexamples. Simple infinite 2-groups exist
by Archive 4.74(a), from the finitely generated infinite groups of exponent $2^n$ of Ivanov and
Lysënok and Zel'manov's solution of the restricted Burnside problem.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.17 (V. V. Bludov); resolution: V. V. Bludov, letter of 30 March 2006, as recorded in the Kourovka Archive; infinite simple 2-groups: Kourovka Archive, Problem 4.74(a) (S. V. Ivanov, Int. J. Algebra Comput. 4 (1994), 1-308; I. G. Lysënok, Izv. Math. 60 (1996), 453-654; E. I. Zel'manov, Math. USSR-Sb. 72 (1992), 543-565), Kourovka Archive, Problem 16.17 (No, it can: an involution is an Engel element in any 2-group, and non-abelian simple 2-groups exist).

Stated but not proved: `MathlibExt.GroupTheory.EngelElementSimpleGroupKourovka16Problem17Wanted.simpleGroupNoNontrivialEngelElement_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EngelElementSimpleGroupKourovka16Problem17Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#simple-group-no-nontrivial-engel-element-2).

## Right Engel element

For a natural number $n$, an element $a$ of a group $G$ is a right
$n$-Engel element when $[a, {}_n x] = 1$ for every $x \in G$, where $[y, x] = y^{-1} x^{-1} y x$
and $[a, {}_n x] = [\dots[[a, x], x], \dots, x]$ is the left-normed commutator with $n$ copies of
$x$ (so $[a, {}_0 x] = a$).

Formalized by `MathlibExt.GroupTheory.RightEngelPowerUpperCentralKourovka17Problem12Wanted.IsRightEngel`, a definition declared in [WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#is-right-engel).

## Abdollahi's question on right Engel subgroups (Kourovka Problem 17.12)

The statement that
there are functions $e, c \colon \mathbb{N} \to \mathbb{N}$ with $e(n) > 0$ for every $n$ such
that, for every natural number $n$, every nilpotent group $G$ and every normal subgroup $H$ of $G$
all of whose elements are right $n$-Engel elements of $G$, the subgroup $H^{e(n)}$ generated by the
$e(n)$-th powers of elements of $H$ is contained in the $c(n)$-th term $\zeta_{c(n)}(G)$ of the
upper central series of $G$.

Formalized by `MathlibExt.GroupTheory.RightEngelPowerUpperCentralKourovka17Problem12Wanted.rightEngelPowerUpperCentral`, a definition declared in [WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#right-engel-power-upper-central).

## Positive answer to Abdollahi's question on right Engel subgroups (Kourovka Problem 17.12)

There are functions $e, c \colon \mathbb{N} \to \mathbb{N}$ with $e(n) > 0$ for every $n$ such
that, for every natural number $n$, every nilpotent group $G$ and every normal subgroup $H$ of $G$
all of whose elements are right $n$-Engel elements of $G$, the subgroup $H^{e(n)}$ generated by the
$e(n)$-th powers of elements of $H$ is contained in the $c(n)$-th term $\zeta_{c(n)}(G)$ of the
upper central series of $G$.

Crosby and Traustason prove that there are positive integers $e(n)$, $c(n)$ such that
$[H^{e(n)}, {}_{c(n)} G] = 1$, that is $H^{e(n)} \le \zeta_{c(n)}(G)$, whenever $H$ is a normal
subgroup of $G$ consisting of right $n$-Engel elements and lying in some term of the upper central
series; in a nilpotent group every subgroup does. The Kourovka Archive answers 17.12 "Yes, there
are".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.12 (A. Abdollahi); resolution: P. G. Crosby and G. Traustason, J. Algebra 324 (2010), 875-883, main theorem as presented by G. Traustason, Right Engel subgroups (Ischia Group Theory 2010): for a normal right n-Engel subgroup H of G with H ≤ ζ_m(G) for some m, there are positive integers e(n), c(n) with [H^{e(n)}, _{c(n)} G] = 1; Kourovka Archive, Problem 17.12 (Yes, there are), http://www.dipmat2.unisa.it/ischiagrouptheory/IGT2010/talks/Traustason.pdf.

Stated but not proved: `MathlibExt.GroupTheory.RightEngelPowerUpperCentralKourovka17Problem12Wanted.rightEngelPowerUpperCentral_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/RightEngelPowerUpperCentralKourovka17Problem12Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html#right-engel-power-upper-central-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Engel elements](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/engel-elements)
