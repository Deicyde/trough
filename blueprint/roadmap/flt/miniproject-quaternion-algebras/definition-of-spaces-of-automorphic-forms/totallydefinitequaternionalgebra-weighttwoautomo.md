---
declaration: definition
origin: cited
lean: TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm
statement: formalized
---

# TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm

The space of $R$-valued *automorphic forms* for $D^\times$ is the set of functions $f:D_{\mathbb{A}^\infty}^\times\to R$ satisfying the following axioms:

- $f(dg)=f(g)$ for all $d\in D^\times$ and $g\in D_{\mathbb{A}^\infty}^\times$.
- $f(gz)=f(g)$ for all $g\in D_{\mathbb{A}^\infty}^\times$.
- There exists a compact open subgroup $U\subseteq (D_{\mathbb{A}^f}^\times)$ such that $f(gu)=f(g)$ for all $g\in D_{\mathbb{A}^\infty}^\times$ and $u\in U$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/QuaternionAlgebraProject.tex, line 86](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/QuaternionAlgebraProject.tex#L86)
