---
declaration: proposition
origin: cited
lean: Rel.permutativeExtension'
statement: formalized
proof: formalized
---

# completing orbits

Let $R : \tau \to \tau \to \mathsf{Prop}$ be a one-to-one relation. Let $s : \operatorname{\mathsf{Set}} \tau$ be an infinite set such that $\#\operatorname{\mathsf{field}} R \leq \#s$, and $\operatorname{\mathsf{field}} R$ and $s$ are disjoint. Then there is a permutative relation $S$ such that $R \leq S$ and $\operatorname{\mathsf{coim}} S \subseteq \operatorname{\mathsf{field}} R \cup s$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [completing restricted orbits](prop-completing-restricted-orbits.md)

## Proof

Define the orbit restriction $(s, f, \pi)$ for $\operatorname{\mathsf{field}} R$ over $\mathsf{Unit}$. Note that for this to be defined, we used the inequality

$$
\#s \geq \max(\aleph_0, \#\operatorname{\mathsf{field}} R)
$$

Use [completing restricted orbits](prop-completing-restricted-orbits.md) to obtain a permutative relation $T$ extending $R$ defined on $\operatorname{\mathsf{field}} R \cup s$.

## Lean

Formalized as [`Rel.permutativeExtension'`](https://leanprover-community.github.io/con-nf/doc/find/#doc/Rel.permutativeExtension').

## Sources

- [Consistency of New Foundations blueprint: chapters/auxiliary.tex, line 85](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L85)
