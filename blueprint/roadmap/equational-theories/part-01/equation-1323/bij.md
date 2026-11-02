---
declaration: lemma
origin: cited
lean: Eq1323.ϕ
statement: formalized
---

# Bijections

Let $G$ be a countably infinite abelian torsion group of exponent $2$. Then there exists a bijection $\phi_a: G \to \mathbb{Q}^\times$ for each $a \in G \backslash \{0\}$ such that $\phi_a(0) = 1$ and $\phi_a(a+b) = -\phi_a(b)$ for all $b \in G$, so in particular $\phi_a(a)=-1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Such a bijection can be easily constructed from the axiom of choice and a greedy algorithm, defining $\phi_a$ one pair $\{b,a+b\}$ at a time.

## Lean

Formalized as [`Eq1323.ϕ`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1323.ϕ).

## Sources

- [Equational Theories blueprint: chapter/1323.tex, line 27](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1323.tex#L27)
