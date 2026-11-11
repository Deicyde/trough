---
declaration: section
origin: cited
lean: MathlibExt.Analysis.AMR22Problem7082Wanted.UnitDisc, MathlibExt.Analysis.AMR22Problem7082Wanted.IsInjectiveInParam, MathlibExt.Analysis.AMR22Problem7082Wanted.IsAnalyticInDisc, MathlibExt.Analysis.AMR22Problem7082Wanted.IsNormalizedAtZero, MathlibExt.Analysis.AMR22Problem7082Wanted.AgreesOnDisc, MathlibExt.Analysis.AMR22Problem7082Wanted.conjecture, MathlibExt.Analysis.AMR22Problem7082Wanted.conjecture_holds
statement: formalized
---

# Holomorphic motions

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html).

## Open unit disc

The open unit disc $\mathbb{D}$ is the set of complex numbers $z$ with
$|z| < 1$, the open ball of radius $1$ about $0$ in $\mathbb{C}$.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.UnitDisc`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#unit-disc).

## Injectivity at each parameter of the disc

Let $\mathbb{D}$ be the open unit disc, $E$ a
set of complex numbers and $F$ a function assigning a complex number $F(w, z)$ to each pair of
complex numbers $w, z$. Condition (a) holds for $E$ and $F$ when, for every $z \in \mathbb{D}$,
the map $w \mapsto F(w, z)$ is injective on $E$.

This is condition (a) of Problem 7.82 in AMR-022-7082.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.IsInjectiveInParam`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#is-injective-in-param).

## Holomorphic dependence of a motion on the parameter

Let $\mathbb{D}$ be the open unit
disc, $E$ a set of complex numbers and $F$ a function assigning a complex number $F(w, z)$ to
each pair of complex numbers $w, z$. Condition (b) holds for $E$ and $F$ when, for every
$w \in E$, the map $z \mapsto F(w, z)$ is analytic on $\mathbb{D}$.

This is condition (b) of Problem 7.82 in AMR-022-7082.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.IsAnalyticInDisc`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#is-analytic-in-disc).

## Motion equal to the identity at parameter zero

Let $E$ be a set of complex numbers and
$F$ a function assigning a complex number $F(w, z)$ to each pair of complex numbers $w, z$.
Condition (c) holds for $E$ and $F$ when $F(w, 0) = w$ for every $w \in E$.

This is condition (c) of Problem 7.82 in AMR-022-7082.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.IsNormalizedAtZero`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#is-normalized-at-zero).

## Agreement of two motions on a set

Let $\mathbb{D}$ be the open unit disc, $E$ a set of
complex numbers, and $F$ and $G$ functions assigning complex numbers $F(w, z)$ and $G(w, z)$ to
each pair of complex numbers $w, z$. Then $G$ agrees with $F$ on $E$ when $G(w, z) = F(w, z)$
for every $w \in E$ and every $z \in \mathbb{D}$.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.AgreesOnDisc`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#agrees-on-disc).

## Extension problem for holomorphic motions

Let $\mathbb{D}$ be the open unit disc. The
proposition asserts the following. Let $E$ be a set of complex numbers and $F$ a function
assigning a complex number $F(w, z)$ to each pair of complex numbers $w, z$, such that (a) for
every $z \in \mathbb{D}$ the map $w \mapsto F(w, z)$ is injective on $E$, (b) for every
$w \in E$ the map $z \mapsto F(w, z)$ is analytic on $\mathbb{D}$, and (c) $F(w, 0) = w$ for
every $w \in E$. Then there is a function $G$ of the same kind that satisfies (a), (b) and (c)
with $E$ replaced by $\mathbb{C}$ and has $G(w, z) = F(w, z)$ for all $w \in E$ and all
$z \in \mathbb{D}$.

Conditions (a), (b) and (c) say that $F$ is a holomorphic motion of $E$ over $\mathbb{D}$; the
question, due to Sullivan, Thurston and Royden, is whether every such motion extends to a
holomorphic motion of the whole plane.

## Sources

- AMR-022-7082, Problem 7.82.

Formalized by `MathlibExt.Analysis.AMR22Problem7082Wanted.conjecture`, a definition declared in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#conjecture).

## Holomorphic motions of planar sets extend to the plane

Let $\mathbb{D}$ be the open unit
disc, $E$ a set of complex numbers and $F$ a function assigning a complex number $F(w, z)$ to
each pair of complex numbers $w, z$, such that (a) for every $z \in \mathbb{D}$ the map
$w \mapsto F(w, z)$ is injective on $E$, (b) for every $w \in E$ the map $z \mapsto F(w, z)$ is
analytic on $\mathbb{D}$, and (c) $F(w, 0) = w$ for every $w \in E$. Then there is a function
$G$ of the same kind that satisfies (a), (b) and (c) with $E$ replaced by $\mathbb{C}$ and has
$G(w, z) = F(w, z)$ for all $w \in E$ and all $z \in \mathbb{D}$.

This answers the extension problem for holomorphic motions affirmatively. It follows from
Słodkowski’s extended λ-lemma: every holomorphic motion over the unit disk extends to a
holomorphic motion of the Riemann sphere.

## Sources

- Zbigniew Słodkowski, Holomorphic motions and polynomial hulls, Proceedings of the American Mathematical Society 111 (1991), 347–355, https://doi.org/10.2307/2048323.

Stated but not proved: `MathlibExt.Analysis.AMR22Problem7082Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/AMR22Problem7082Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AMR22Problem7082Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Holomorphic motions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/holomorphic-motions)
