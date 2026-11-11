---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.IsProductOfCommutators, MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.autFreeGroupCommutatorLengthUnbounded, MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.autFreeGroupCommutatorLengthUnbounded_holds, MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.IsProductOfCommutators, MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.commutatorWidth, MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.maxCommutatorWidthRatioIsOneSixth, MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.maxCommutatorWidthRatioIsOneSixth_holds, MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.IsProductOfCommutators
statement: formalized
---

# Commutator width

13 results, 9 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html).

## Products of at most $n$ commutators (Kourovka 14.15)

Let $G$ be a group and $n$ a natural
number. An element $z \in G$ is a product of at most $n$ commutators when there are $m \le n$ and
elements $x_1, y_1, \dots, x_m, y_m \in G$ with $z = [x_1, y_1] \cdots [x_m, y_m]$, where
$[x, y] = xyx^{-1}y^{-1}$; for $m = 0$ the empty product is the identity.

Formalized by `MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.IsProductOfCommutators`, a definition declared in [WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#is-product-of-commutators).

## Unbounded commutator length in Aut(Fₙ) (Kourovka 14.15)

The proposition that for every
$n \ge 3$, writing $F_n$ for the free group on $n$ generators, and for every natural number $k$,
some element of the derived subgroup of $\operatorname{Aut}(F_n)$ is not a product of at most $k$
commutators $xyx^{-1}y^{-1}$ of elements of $\operatorname{Aut}(F_n)$. This is the answer
$k_n = \infty$ to Bardakov's question, which asks for the supremum $k_n$ of the commutator lengths
of the elements of the derived subgroup of $\operatorname{Aut}(F_n)$.

Formalized by `MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.autFreeGroupCommutatorLengthUnbounded`, a definition declared in [WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#aut-free-group-commutator-length-unbound).

## Commutator length in Aut(Fₙ) is unbounded

Let $n \ge 3$ and let $F_n$ be the free group on
$n$ generators. For every natural number $k$ there is an element of the derived subgroup of
$\operatorname{Aut}(F_n)$ that is not a product of at most $k$ commutators $xyx^{-1}y^{-1}$ with
$x, y \in \operatorname{Aut}(F_n)$. Equivalently, the supremum $k_n$ of the commutator lengths of
the elements of the derived subgroup of $\operatorname{Aut}(F_n)$ is infinite.

This answers Kourovka Problem 14.15 (V. G. Bardakov): $\operatorname{Aut}(F_n)$ is acylindrically
hyperbolic (Genevois–Horbez), and acylindrically hyperbolic groups have infinite commutator width
(Bestvina–Bromberg–Fujiwara).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.15 (V. G. Bardakov); resolution: A. Genevois and C. Horbez, J. Topology 14 (2021), 963-991 (Aut F_n is acylindrically hyperbolic); M. Bestvina, K. Bromberg and K. Fujiwara, Algebr. Geom. Topol. 19 (2019), 477-489 (acylindrically hyperbolic groups have infinite commutator width), the Kourovka Notebook (21st issue) marks 14.15 solved: k_n = ∞ for n ≥ 3.

Stated but not proved: `MathlibExt.GroupTheory.AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.autFreeGroupCommutatorLengthUnbounded_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupCommutatorLengthKourovka14Problem15Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#aut-free-group-commutator-length-unbound-2).

## Products of a bounded number of commutators

For a group $G$, a natural number $m$ and
$g \in G$, $g$ is a product of at most $m$ commutators when there are $k \le m$ and
$a_1, b_1, \dots, a_k, b_k \in G$ with $g = [a_1, b_1] \cdots [a_k, b_k]$, where
$[a, b] = aba^{-1}b^{-1}$; for $k = 0$ the empty product is the identity.

Formalized by `MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.IsProductOfCommutators`, a definition declared in [WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#is-product-of-commutators-2).

## Commutator width of the derived subgroup

For a group $G$ with derived subgroup $G'$, the
commutator width $w(G')$ is the least positive integer $m$ such that every element of $G'$ is a
product of at most $m$ commutators $aba^{-1}b^{-1}$ with $a, b \in G$; it is $0$ when no such $m$
exists.

Formalized by `MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.commutatorWidth`, a definition declared in [WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#commutator-width).

## Bardakov's commutator width ratio claim (Kourovka 16.8)

The proposition that for every
finite non-abelian group $G$ the commutator width $w(G')$ of its derived subgroup $G'$ satisfies
$w(G')/|G| \le 1/6$, and that for the symmetric group $S_3$ equality holds:
$w(S_3')/|S_3| = 1/6$.

Formalized by `MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.maxCommutatorWidthRatioIsOneSixth`, a definition declared in [WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#max-commutator-width-ratio-is-one-sixth).

## The maximal commutator width ratio is one sixth

For every finite non-abelian group $G$,
the commutator width $w(G')$ of its derived subgroup satisfies $w(G')/|G| \le 1/6$, and for the
symmetric group $S_3$ equality holds, $w(S_3')/|S_3| = 1/6$; so Kourovka Problem 16.8 has a
positive answer.

The Kourovka Archive answers 16.8 "Yes, it is", citing Bonner (2008) for the bound; $S_3$ attains
it because its derived subgroup $A_3$ consists of commutators.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.8 (V. G. Bardakov); resolution: T. Bonner, J. Algebra 320 (2008), 3165-3171, Kourovka Archive, Problem 16.8 (Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.CommutatorWidthRatioKourovka16Problem8Wanted.maxCommutatorWidthRatioIsOneSixth_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CommutatorWidthRatioKourovka16Problem8Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#max-commutator-width-ratio-is-one-sixth-2).

## Products of at most $n$ commutators

An element $z$ of a group $G$ is a product of at most
$n$ commutators when $z = [x_1, y_1] \cdots [x_k, y_k]$ for some $k \le n$ and some
$x_1, y_1, \dots, x_k, y_k \in G$, where $[x, y] = x y x^{-1} y^{-1}$; for $k = 0$ the product is
the identity.

Formalized by `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.IsProductOfCommutators`, a definition declared in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#is-product-of-commutators-3).

## Unbounded commutator length

A group $G$ has unbounded commutator length when for every
natural number $n$ some element of the derived subgroup $[G, G]$ is not a product of at most $n$
commutators $x y x^{-1} y^{-1}$ with $x, y \in G$.

Formalized by `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.CommutatorLengthUnbounded`, a definition declared in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#commutator-length-unbounded).

## Kourovka Problem 14.13(a) (Bardakov)

The statement that there is a simple group $G$ such
that for every natural number $n$ some element of the derived subgroup $[G, G]$ is not a product of
at most $n$ commutators $x y x^{-1} y^{-1}$ with $x, y \in G$.

Formalized by `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.simpleGroupUnboundedCommutatorLength`, a definition declared in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#simple-group-unbounded-commutator-length).

## Kourovka Problem 14.13(b) (Bardakov)

The statement that there is a finitely presented
simple group $G$ such that for every natural number $n$ some element of the derived subgroup
$[G, G]$ is not a product of at most $n$ commutators $x y x^{-1} y^{-1}$ with $x, y \in G$.

Formalized by `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.finitelyPresentedSimpleGroupUnboundedCommutatorLength`, a definition declared in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#finitely-presented-simple-group-unbounde).

## A simple group with unbounded commutator length

There is a simple group $G$ such that for
every natural number $n$ some element of the derived subgroup $[G, G]$ is not a product of at most
$n$ commutators $x y x^{-1} y^{-1}$ with $x, y \in G$. This answers Kourovka Problem 14.13(a) in
the affirmative; the Kourovka Archive records examples constructed by Barge and Ghys, and finitely
generated ones by Muranov.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.13 (V. G. Bardakov); resolution: (a) J. Barge and É. Ghys, Math. Ann. 294 (1992), 235-265, and A. Muranov, Int. J. Algebra Comput. 17 (2007), 607-659 (finitely generated examples); (b) P.-E. Caprace and K. Fujiwara, Geom. Funct. Anal. 19 (2010), 1296-1319, Kourovka Archive, Problem 14.13 (answers: a) constructed; b) Yes, there does).

Stated but not proved: `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.simpleGroupUnboundedCommutatorLength_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#simple-group-unbounded-commutator-length-2).

## A finitely presented simple group with unbounded commutator length

There is a finitely
presented simple group $G$ such that for every natural number $n$ some element of the derived
subgroup $[G, G]$ is not a product of at most $n$ commutators $x y x^{-1} y^{-1}$ with
$x, y \in G$. This answers Kourovka Problem 14.13(b) in the affirmative; the Kourovka Archive cites
Caprace and Fujiwara.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.13 (V. G. Bardakov); resolution: (a) J. Barge and É. Ghys, Math. Ann. 294 (1992), 235-265, and A. Muranov, Int. J. Algebra Comput. 17 (2007), 607-659 (finitely generated examples); (b) P.-E. Caprace and K. Fujiwara, Geom. Funct. Anal. 19 (2010), 1296-1319, Kourovka Archive, Problem 14.13 (answers: a) constructed; b) Yes, there does).

Stated but not proved: `MathlibExt.GroupTheory.SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.finitelyPresentedSimpleGroupUnboundedCommutatorLength_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupUnboundedCommutatorLengthKourovka14Problem13Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html#finitely-presented-simple-group-unbounde-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Commutator width](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-width)
