---
declaration: lemma
origin: cited
---

# fixed\_of\_fixed1\_aux1

There exist elements $a,b \in B$, with $a \notin Q$ and $a$ in the image of $A$ such that for all $g\in G$,

- If $g \cdot Q = Q$, then $g \cdot b \equiv a \pmod{Q}$.
- If $g \cdot Q \neq Q$, then $g \cdot b \equiv 0 \pmod{Q}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Algebra.IsInvariant.charpoly\_mem\_lifts](../the-extension-b-a/algebra-isinvariant-charpoly-mem-lifts.md)

## Proof

The ideals $g \cdot Q \neq Q$ are not contained in $Q$. Since $Q$ is a prime ideal, this implies that the intersection of all $g \cdot Q \neq Q$ is still not contained in $Q$. Then we can find an element $c \notin Q$ with $c \in g \cdot Q$ for all $g \cdot Q \neq Q$. Let $F_c$ be the characteristic polynomial of $c$, and write $F_c(X) \equiv X^j R(X) \pmod{Q}$. Let $a$ be the coefficient of $X^j$ in $F_c(X)$, and choose $R(X)$ so that $R(0) = a$. Let $b = R(0) - R(c)$. Note that $F_c(c) = 0$ and $c \not\equiv 0 \pmod{Q}$, so $R(c) \equiv 0 \pmod{Q}$. Then $b \equiv a \pmod{Q}$, so $g \cdot b \equiv a \pmod{Q}$ whenever $g \cdot Q = Q$. But if $g \cdot Q \neq Q$, then $c \equiv 0 \pmod {g \cdot Q}$. Then $b \equiv 0 \pmod {g \cdot Q}$, so $g \cdot b \equiv 0 \pmod{Q}$ whenever $g \cdot Q \neq Q$.

## Lean

The blueprint marks this as in Mathlib but names no declaration.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 209](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FrobeniusProject.tex#L209)
