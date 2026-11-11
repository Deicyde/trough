---
declaration: section
origin: cited
lean: ClassBreadth.elementBreadth, ClassBreadth.breadth, ClassBreadth.card_carrier_dvd_card, ClassBreadth.exists_card_carrier_eq_pow, ClassBreadth.elementBreadth_eq_of_card_eq, ClassBreadth.pow_elementBreadth_eq_card, ClassBreadth.carrier_mk_one, ClassBreadth.elementBreadth_one
statement: formalized
proof: formalized
---

# Breadth of a finite group

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html).

## Breadth of an element

Let $G$ be a finite group, $p$ a natural number and $g \in G$,
and write $g^G$ for the conjugacy class of $g$. When $p \ge 2$, the breadth
$\operatorname{br}_p(g)$ of $g$ is $\lfloor \log_p |g^G| \rfloor$, the largest natural number
$k$ with $p^k \le |g^G|$; when $p \le 1$, it is $0$.

If $p$ is prime and $G$ is a $p$-group, then $|g^G|$ is a power of $p$, so
$p^{\operatorname{br}_p(g)} = |g^G|$.

Formalized by `ClassBreadth.elementBreadth`, a definition declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#element-breadth).

## Breadth of a finite group

For a finite group $G$ and a natural number $p$, the breadth
$\operatorname{br}_p(G)$ of $G$ is the maximum of the element breadths $\operatorname{br}_p(g)$
over all $g \in G$.

Formalized by `ClassBreadth.breadth`, a definition declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#breadth).

## Conjugacy class sizes divide the group order

In a finite group $G$, the number of
elements of the conjugacy class of any $g \in G$ divides the order $|G|$.

Formalized by `ClassBreadth.card_carrier_dvd_card`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#card-carrier-dvd-card).

## Conjugacy classes of a finite $p$-group have $p$-power size

Let $p$ be a prime and
$G$ a finite $p$-group. For every $g \in G$ there is a natural number $k$ such that the
conjugacy class of $g$ has exactly $p^k$ elements.

Formalized by `ClassBreadth.exists_card_carrier_eq_pow`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#exists-card-carrier-eq-pow).

## Breadth from an exact class size

Let $G$ be a finite group, $p$ a prime, $k$ a natural
number and $g \in G$. If the conjugacy class of $g$ has exactly $p^k$ elements, then the breadth
$\operatorname{br}_p(g)$ of $g$ equals $k$.

Formalized by `ClassBreadth.elementBreadth_eq_of_card_eq`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#element-breadth-eq-of-card-eq).

## Class sizes in a $p$-group via breadth

Let $p$ be a prime, $G$ a finite $p$-group and
$g \in G$, and write $g^G$ for the conjugacy class of $g$. Then the breadth
$\operatorname{br}_p(g)$ of $g$ satisfies $p^{\operatorname{br}_p(g)} = |g^G|$.

Formalized by `ClassBreadth.pow_elementBreadth_eq_card`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#pow-element-breadth-eq-card).

## The conjugacy class of the identity

In every group, the conjugacy class of the identity
element $1$ is the singleton $\{1\}$.

Formalized by `ClassBreadth.carrier_mk_one`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#carrier-mk-one).

## Breadth of the identity

In a finite group, the breadth $\operatorname{br}_p(1)$ of the
identity element $1$ is $0$ for every natural number $p$.

Formalized by `ClassBreadth.elementBreadth_one`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#element-breadth-one).

## Element breadth is at most the group breadth

Let $G$ be a finite group and $p$ a
natural number. For every $g \in G$, the breadth $\operatorname{br}_p(g)$ of $g$ is at most
the breadth $\operatorname{br}_p(G)$ of $G$.

Formalized by `ClassBreadth.elementBreadth_le_breadth`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#element-breadth-le-breadth).

## The group breadth is attained

Let $G$ be a finite group and $p$ a natural number.
There is an element $g \in G$ whose breadth $\operatorname{br}_p(g)$ equals the breadth
$\operatorname{br}_p(G)$ of $G$.

Formalized by `ClassBreadth.exists_breadth_eq_elementBreadth`, a theorem declared in [MathlibExt/GroupTheory/ClassBreadth.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassBreadth.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html#exists-breadth-eq-element-breadth).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Breadth of a finite group](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/conjugacy-classes/breadth-of-a-finite-group)
