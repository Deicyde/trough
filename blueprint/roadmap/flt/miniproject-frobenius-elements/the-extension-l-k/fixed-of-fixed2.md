---
declaration: proposition
origin: cited
---

# fixed\_of\_fixed2

Let $x \in L$. Suppose that $x$ is fixed by the stabilizer subgroup $D_Q$. Then $x$ is fixed by the automorphism group $\operatorname{Aut}(L/K)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [fixed\_of\_fixed1](fixed-of-fixed1.md)
- [Algebra.IsInvariant.isIntegral](../the-extension-b-a/algebra-isinvariant-isintegral.md)
- [IsAlgebraic.exists\_smul\_eq\_mul](isalgebraic-exists-smul-eq-mul.md)

## Proof

Since $(B/Q)/(A/Q)$ is algebraic by [Theorem Algebra.IsInvariant.isIntegral](../the-extension-b-a/algebra-isinvariant-isintegral.md), [Lemma IsAlgebraic.exists\_smul\_eq\_mul](isalgebraic-exists-smul-eq-mul.md) let's us write $x=b/a$ for $b \in B/Q$ and $a \in A/P$. Then $b$ is fixed by the stabilizer subgroup $D_Q$, and it suffices to show that $b$ is fixed by the automorphism group $\operatorname{Aut}(L/K)$. But this is exactly [Proposition fixed\_of\_fixed1](fixed-of-fixed1.md).

## Lean

The blueprint marks this as in Mathlib but names no declaration.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 318](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FrobeniusProject.tex#L318)
