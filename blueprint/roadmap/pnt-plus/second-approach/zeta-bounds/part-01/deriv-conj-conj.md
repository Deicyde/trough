---
declaration: theorem
origin: cited
lean: deriv_conj_conj'
statement: formalized
proof: formalized
---

# deriv-conj-conj

Let $f : \mathbb{C} \to \mathbb{C}$ be a function at $p \in \mathbb{C}$ with derivative $a$. Then the derivative of the function $g(z) = \overline{f(\overline{z})}$ at $\overline{p}$ is $\overline{a}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We proceed by case analysis on whether $f$ is differentiable at $p$. If $f$ is differentiable at $p$, then we can apply the previous theorem. If $f$ is not differentiable at $p$, then neither is $g$, and both derivatives have the default value of zero.

## Lean

Formalized as [`deriv_conj_conj'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/deriv_conj_conj').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaConj.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaConj.lean)
