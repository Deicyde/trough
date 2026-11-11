---
declaration: section
origin: cited
lean: Group.Generators.growth, Group.Generators.HasPolynomialGrowth, Group.Generators.growth_zero, Group.Generators.growth_pos, Group.Generators.growth_le_card, Group.Generators.hasPolynomialGrowth_of_finite, Group.Generators.HasPolynomialGrowth.growth_pos
statement: formalized
proof: formalized
---

# Growth of groups

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html).

## Growth function of a generating family

Let $P$ be a generating family of a group $G$.
The growth function $\gamma_P$ of $P$ assigns to each natural number $n$ the number of elements
$g \in G$ whose word length with respect to $P$ is at most $n$, that is, the cardinality of the
ball of radius $n$ in the word metric of $P$; when this ball is infinite, $\gamma_P(n)$ is taken
to be $0$.

Formalized by `Group.Generators.growth`, a definition declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#growth).

## Polynomial growth

Let $P$ be a generating family of a group $G$, with growth function
$\gamma_P$. Then $P$ has polynomial growth if, for every natural number $n$, the ball of radius
$n$ (the set of elements of $G$ of word length at most $n$ with respect to $P$) is finite, and
there are natural numbers $C$ and $d$ such that $\gamma_P(n) \le C (n + 1)^d$ for every
natural number $n$.

Formalized by `Group.Generators.HasPolynomialGrowth`, a definition declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#has-polynomial-growth).

## The growth function at radius zero

For every generating family $P$ of a group $G$, the
growth function of $P$ takes the value $1$ at $0$: the ball of radius $0$ consists of the identity
element alone.

Formalized by `Group.Generators.growth_zero`, a lemma declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#growth-zero).

## The growth function of a finite group is positive

For every generating family $P$ of a
finite group $G$ and every natural number $n$, the growth function of $P$ is positive at $n$: the
ball of radius $n$ contains the identity.

Formalized by `Group.Generators.growth_pos`, a lemma declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#growth-pos).

## The growth function is bounded by the order of the group

For every generating family $P$
of a finite group $G$ and every natural number $n$, the value of the growth function of $P$ at $n$
is at most the order of $G$, since every ball is a subset of $G$.

Formalized by `Group.Generators.growth_le_card`, a lemma declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#growth-le-card).

## Finite groups have polynomial growth

Every generating family of a finite group has
polynomial growth: its growth function is bounded by the order of the group, a polynomial of
degree $0$.

Formalized by `Group.Generators.hasPolynomialGrowth_of_finite`, a theorem declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#has-polynomial-growth-of-finite).

## Polynomial growth makes the growth function positive

If a generating family $P$ of a
group $G$ has polynomial growth, then the growth function of $P$ is positive at every natural
number $n$.

Formalized by `Group.Generators.HasPolynomialGrowth.growth_pos`, a lemma declared in [MathlibExt/GroupTheory/GroupGrowth.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GroupGrowth.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html#growth-pos-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Growth of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/growth-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/geometric-group-theory/growth-of-groups)
