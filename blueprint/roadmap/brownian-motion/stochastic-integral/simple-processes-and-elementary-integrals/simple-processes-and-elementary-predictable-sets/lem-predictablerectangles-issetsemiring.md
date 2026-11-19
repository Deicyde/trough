---
declaration: lemma
origin: cited
lean: MeasureTheory.Filtration.isSetSemiring_predictableRectangles
statement: formalized
proof: formalized
---

# predictableRectangles_isSetSemiring

The class $\mathcal{R}_T$ of predictable rectangles is a semi-ring of sets.

## Depends on

- [Predictable rectangles](def-predictablerectangles.md)

## Proof

Take two elements $A, B \in \mathcal{R}_T$ . If only one of $A, B$ is of the form $\{0\} \times F$, they are disjoint, so both the intersection and the difference are trivially in $\mathcal{R}_T$ . If both are of this form, then $A\cap B$, $A\setminus B\in\mathcal{R}_T$ follows from the fact that $\mathcal{F}_0$ is a $\sigma$-algebra.

Let then $A=(s, t] \times F$ and $B=(s', t'] \times F'$ . We shall understand $(s,t]$ as the empty set if $s \ge t$ . Both $F \cap F'$ and $F \setminus F'$ are in $\mathcal{F}_{s \vee s'}$ . It is now clear that $A\cap B$ is a predictable rectangle, since

$$
A \cap B
=
(s \vee s', t \wedge t'] \times (F \cap F').
$$

Finally, let $I=(s,t]$ and $J=(s',t']$. Then

$$
(I\times F)\setminus(J\times F')
=
((I\setminus J)\times F)
\cup
((I\cap J)\times(F\setminus F')).
$$

The union is disjoint, and

$$
I\setminus J
=
(s,t\wedge s']\cup(s\vee t',t].
$$

Hence $A\setminus B$ is a disjoint union of at most three predictable rectangles. Indeed, $F\in\mathcal{F}_{s\vee t'}$ by monotonicity of the filtration, and $F\setminus F'\in\mathcal{F}_{s\vee s'}$ as noted earlier.

## Lean

Formalized as [`MeasureTheory.Filtration.isSetSemiring_predictableRectangles`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.isSetSemiring_predictableRectangles).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 140](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L140)
