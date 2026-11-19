---
declaration: lemma
origin: cited
lean: linearIndepOn_isGroupLikeElem
statement: formalized
proof: formalized
---

# Independence of group-like elements

The group-like elements in a bialgebra $A$ over a domain are linearly independent.

## Depends on

- [Group-like elements](0-grp-like.md)

## Proof depends on

- [The tensor product of linearly independent families](../tensor-product/0-tensor-lin-indep.md)

## Proof

Let's prove that any finite set $s$ of group-like elements is linearly independent, by induction on $s$.

$\emptyset$ is clearly linearly independent.

Assume now that the finite set $s$ of group-like elements is linearly independent, that $a \notin s$ is group-like, and let's show that $s \cup \{a\}$ is linearly independent too.

Assume there is some $c : A \to R$ such that $\sum_{x \in s} c_x x = c_a a$. Since $a$ and all elements of $s$ are group-like, we compute

$$
\begin{aligned}
\sum_{x, y \in s} c_x c_y x \otimes y
& = c_a ^ 2 a \otimes a \\
& = c_a ^ 2 \Delta(a) \\
& = c_a \Delta\left(\sum_{x \in s} c_x x\right) \\
& = \sum_{x \in s} c_a c_x \Delta(x) \\
& = \sum_{x \in s} c_a c_x x \otimes x
\end{aligned}
$$

By Lemma [The tensor product of linearly independent families](../tensor-product/0-tensor-lin-indep.md), the $x \otimes y$ are linearly independent and therefore $c_x ^ 2 = c_a c_x$ and $c_x c_y = 0$ if $x \ne y$.

If $c_x = 0$ for all $x \in s$, then we are clearly done. Else find $x \in s$ such that $c_x \ne 0$. From the above two equations, we get that $c_x = c_a$ and $c_y = 0$ for all $y \in s, y \ne x$. Therefore

$$
c_x x = \sum_{y \in s} c_y y = c_a a = c_x a
$$

and $x = a$. Contradiction.

## Lean

Formalized as [`linearIndepOn_isGroupLikeElem`](https://yaeldillies.github.io/toric/docs/find/#doc/linearIndepOn_isGroupLikeElem).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 326](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L326)
