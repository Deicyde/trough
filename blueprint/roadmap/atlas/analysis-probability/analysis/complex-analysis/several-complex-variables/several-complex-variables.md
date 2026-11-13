---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.WeierstrassPreparationWanted.weierstrass_preparation
statement: formalized
proof: formalized
---

# Several complex variables: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/index.html).

Holomorphic functions on C^n: Hartogs extension and separate analyticity, Weierstrass preparation, complex Hessians.

## Weierstrass preparation theorem

Let $E$ be a finite-dimensional normed vector space over
$\mathbb{C}$ and let $f : E \times \mathbb{C} \to \mathbb{C}$ be analytic at $0$. Suppose that for
some $d \in \mathbb{N}$ and some $g : \mathbb{C} \to \mathbb{C}$ analytic at $0$ with $g(0) \ne 0$,
$f(0, w) = w^d g(w)$ for all $w$ in a neighbourhood of $0$. Then there are functions
$a_0, \dots, a_{d-1} : E \to \mathbb{C}$, each analytic at $0$ with $a_j(0) = 0$, a function
$u : E \times \mathbb{C} \to \mathbb{C}$ analytic at $0$ with $u(0) \ne 0$, and an open set
$U \subseteq E \times \mathbb{C}$ containing $0$ such that
$f(z, w) = u(z, w) \bigl(w^d + \sum_{j=0}^{d-1} a_j(z) w^j\bigr)$ for all $(z, w) \in U$.

## Sources

- Weierstrass preparation theorem in several complex variables; see Hörmander; Lean is finite-dimensional E × ℂ product form, order d slice factorization w^d g w, Weierstrass polynomial with vanishing coefficients and unit u, local open U, fixed field ℂ specialization.

Formalized by `MathlibExt.Analysis.Complex.WeierstrassPreparationWanted.weierstrass_preparation`, a theorem declared in [MathlibExt/Analysis/Complex/WeierstrassPreparation.lean, line 1683](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/WeierstrassPreparation.lean#L1683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/index.html#weierstrass-preparation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Several complex variables](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/several-complex-variables)
