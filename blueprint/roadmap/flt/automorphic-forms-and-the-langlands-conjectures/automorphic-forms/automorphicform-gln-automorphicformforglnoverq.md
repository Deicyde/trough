---
declaration: definition
origin: cited
---

# AutomorphicForm.GLn.AutomorphicFormForGLnOverQ

A smooth function $f:\operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}}^f)\times\operatorname{GL}_n(\mathbb{R})\to\mathbb{C}$ is an $O_n(\mathbb{R})$-*automorphic form* on $\operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}})$ if it satisfies the following five conditions.

1. (periodicity) For all $g\in\operatorname{GL}_n(\mathbb{Q})$, we have $f(gx,gy)=f(x,y)$.
2. (has a finite level) There exists a compact open subgroup $U\subseteq\operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}}^f)$ such that $f(xu,y)=f(x,y)$ for all $u\in U$, $x\in \operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}}^f)$ and $y\in\operatorname{GL}_n(\mathbb{R})$.
3. (weight $\rho$) There exists a continuous finite-dimensional irreducible complex representation $\rho$ of $O_n(\mathbb{R})$ such that for every $(x,y)\in\operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}})$, the set of functions $k\mapsto f(x,yk)$ span a finite-dimensional complex vector space isomorphic as $O_n(\mathbb{R})$-representation to a direct sum of copies of $\rho$.
4. (has an infinite level) There is an ideal $I$ of the centre $Z_n$ described in the previous section, which has finite complex codimension, and which annihiliates the function $y \mapsto f(x,y)$ for all $x\in \operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}}^f)$. Note that this is a very fancy way of saying “the function satisfies some natural differential equations”. In the case of modular forms, the differential equations are the Cauchy-Riemann equations, which is why modular forms are holomorphic.
5. (growth condition) For every $x\in\operatorname{GL}_n(\mathbb{A}_{\mathbb{Q}}^f)$, the function $y\mapsto f(x,y)$ on $\operatorname{GL}_n(\mathbb{R})$ is slowly-increasing.

## Depends on

- [AutomorphicForm.GLn.IsSmooth](../smooth-functions/automorphicform-gln-issmooth.md)
- [AutomorphicForm.GLn.IsSlowlyIncreasing](../slowly-increasing-functions/automorphicform-gln-isslowlyincreasing.md)
- [AutomorphicForm.GLn.Weight](../weights-at-infinity/automorphicform-gln-weight.md)
- [instCentreAction](../the-action-of-the-universal-enveloping-algebra/instcentreaction.md)

## Lean

The blueprint names [`AutomorphicForm.GLn.AutomorphicFormForGLnOverQ`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/AutomorphicForm.GLn.AutomorphicFormForGLnOverQ).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch07exampleGLn.tex, line 128](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch07exampleGLn.tex#L128)
