---
declaration: section
origin: cited
lean: LinearMap.BilinForm.prod, LinearMap.BilinForm.prod_apply, LinearMap.BilinForm.nondegenerate_prod_iff, LinearMap.BilinForm.dualSubmodule_prod
statement: formalized
proof: formalized
---

# Orthogonal product of bilinear forms

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html).

## Orthogonal products

## Orthogonal product of bilinear forms

Let $B_1$ and $B_2$ be bilinear forms on modules
$M_1$ and $M_2$ over a commutative semiring $R$. Their orthogonal product $B_1 \oplus B_2$ is the
bilinear form on $M_1 \times M_2$ given by
$(B_1 \oplus B_2)((x_1, x_2), (y_1, y_2)) = B_1(x_1, y_1) + B_2(x_2, y_2)$.

Formalized by `LinearMap.BilinForm.prod`, a definition declared in [MathlibExt/LinearAlgebra/BilinearForm/Prod.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/Prod.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html#prod).

## Evaluation of an orthogonal product

Let $B_1$ and $B_2$ be bilinear forms on modules
$M_1$ and $M_2$ over a commutative semiring $R$, with orthogonal product $B_1 \oplus B_2$ on
$M_1 \times M_2$. For all $x = (x_1, x_2)$ and $y = (y_1, y_2)$ in $M_1 \times M_2$,
$(B_1 \oplus B_2)(x, y) = B_1(x_1, y_1) + B_2(x_2, y_2)$.

Formalized by `LinearMap.BilinForm.prod_apply`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/Prod.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/Prod.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html#prod-apply).

## Nondegeneracy of an orthogonal product

Let $B_1$ and $B_2$ be bilinear forms on modules
$M_1$ and $M_2$ over a commutative semiring $R$. Their orthogonal product $B_1 \oplus B_2$ on
$M_1 \times M_2$ is nondegenerate (both left- and right-separating) if and only if $B_1$ and
$B_2$ are both nondegenerate.

Formalized by `LinearMap.BilinForm.nondegenerate_prod_iff`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/Prod.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/Prod.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html#nondegenerate-prod-iff).

## Dual submodule of an orthogonal product

Let $R$ be a commutative ring, let $S$ be a
field that is an $R$-algebra, and let $M_1$, $M_2$ be vector spaces over $S$ that are also
$R$-modules compatibly with $R \to S$. For a bilinear form $B$ over $S$ on such a space $M$ and an
$R$-submodule $N$ of $M$, the dual of $N$ is
$N^\vee = \{x \in M : B(x, y) \in R \text{ for all } y \in N\}$, where $R$ stands for its image
in $S$. Let $B_1$, $B_2$ be bilinear forms over $S$ on $M_1$, $M_2$, and let $B_1 \oplus B_2$ be
their orthogonal product on $M_1 \times M_2$, given by
$(B_1 \oplus B_2)((x_1, x_2), (y_1, y_2)) = B_1(x_1, y_1) + B_2(x_2, y_2)$. Then for all
$R$-submodules $N_1 \subseteq M_1$ and $N_2 \subseteq M_2$, the dual of $N_1 \times N_2$ with
respect to $B_1 \oplus B_2$ is $N_1^\vee \times N_2^\vee$, where $N_1^\vee$ and $N_2^\vee$ are
taken with respect to $B_1$ and $B_2$.

Formalized by `LinearMap.BilinForm.dualSubmodule_prod`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/Prod.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/Prod.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html#dual-submodule-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orthogonal product of bilinear forms](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/orthogonal-product-of-bilinear-forms)
