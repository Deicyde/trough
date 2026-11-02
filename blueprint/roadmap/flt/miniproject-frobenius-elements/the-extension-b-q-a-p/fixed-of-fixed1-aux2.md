---
declaration: lemma
origin: cited
---

# fixed\_of\_fixed1\_aux2

Let $b_0 \in B$. Suppose that the image of $b_0$ in the quotient $B/Q$ is fixed by the stabilizer subgroup $D_Q$. Then there exist elements $a,b \in B$, with $a\notin Q$ and $a$ in the image of $A$ such that for all $g\in G$,

- If $g \cdot Q = Q$, then $g \cdot b \equiv ab_0 \pmod{Q}$.
- If $g \cdot Q \neq Q$, then $g \cdot b \equiv 0 \pmod{Q}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [fixed\_of\_fixed1\_aux1](fixed-of-fixed1-aux1.md)

## Proof

Multiply the $b$ from [Lemma fixed\_of\_fixed1\_aux1](fixed-of-fixed1-aux1.md) by $b_0$.

## Lean

The blueprint marks this as in Mathlib but names no declaration.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 238](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FrobeniusProject.tex#L238)
