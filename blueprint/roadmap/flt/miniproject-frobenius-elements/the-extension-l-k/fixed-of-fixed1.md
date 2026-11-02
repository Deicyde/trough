---
declaration: proposition
origin: cited
---

# fixed\_of\_fixed1

Let $b_0 \in B/Q$. Suppose that $b_0$ is fixed by the stabilizer subgroup $D_Q$. Then $b_0$ is fixed by $\operatorname{Aut}(L/K)$.

## Depends on

- [IsFractionRing.stabilizerHom](../statement-of-the-theorem/isfractionring-stabilizerhom.md)

## Proof depends on

- [fixed\_of\_fixed1\_aux1](../the-extension-b-q-a-p/fixed-of-fixed1-aux1.md)
- [fixed\_of\_fixed1\_aux2](../the-extension-b-q-a-p/fixed-of-fixed1-aux2.md)

## Proof

Let $a,b\in B$ be elements from [fixed\_of\_fixed1\_aux2](../the-extension-b-q-a-p/fixed-of-fixed1-aux2.md). Let $M_b \in A[X]$ be the characteristic polynomial of $b$. We can map $M_b$ to $L[X]$ in two different ways: via $B[X]$ and via $K[X]$. Going via $B[X]$ tells us that the image of $M_b(X)$ in $L[X]$ is exactly

$$
(X - ab_0)^{\lvert D_Q\rvert}X^{\lvert G\rvert-\lvert D_Q\rvert}.
$$

But going via $K[X]$ tells us that this image lies in $K[X]$, so we must have $ab_0\in K$. Then $ab_0$ is fixed by $\operatorname{Aut}(L/K)$, and $a$ is nonzero in $L$ (since $a\notin Q$), so $b_0$ is fixed by $\operatorname{Aut}(L/K)$.

## Lean

The blueprint marks this as in Mathlib but names no declaration.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 281](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FrobeniusProject.tex#L281)
