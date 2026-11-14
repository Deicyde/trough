---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.exists_mul_involute_eq, MIPRE.LowDegree.mul_self_bijective, MIPRE.LowDegree.exists_mul_involute_eq_of_charTwo, MIPRE.LowDegree.binarySquareRoot, MIPRE.LowDegree.coeff_binarySquareRoot, MIPRE.LowDegree.binarySquareRoot_mul_self, MIPRE.LowDegree.binarySquareRoot_mul_involute
statement: formalized
proof: formalized
---

# Self-dualization in the group algebra

Let $R$ be a commutative ring on which $x \mapsto x^2$ is a bijection and let $\tau$ be a ring automorphism of $R$. Then every $u \in R$ with $\tau(u) = u$ is of the form $a \cdot \tau(a)$.

Squaring *is* a bijection of the group algebra $\mathbb{F}[G]$ when $\mathbb{F}$ is a finite field of characteristic two and $G$ is a finite abelian group of odd order. For $\mathbb{F}=\mathbb{F}_2$, its inverse has the explicit coefficient formula $b(g)=u(g+g)$. This $b$ satisfies $b^2=u$, and $b\tau(b)=u$ whenever $\tau(u)=u$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For the first statement, let $b$ be the square root of $u$. Then $\tau(b)^2 = \tau(b^2) = \tau(u) = u = b^2$, so $\tau(b) = b$ by injectivity of squaring, and $b \cdot \tau(b) = b^2 = u$.

For the second, squaring is additive in characteristic two, and on a single generator $\delta_g r$ it is $\delta_{g + g} r^2$. Doubling is injective on $G$: if $(a - b) + (a - b) = 0$ then the additive order of $a - b$ divides both $2$ and $\left\vert {G} \right\vert$, which are coprime because $\left\vert {G} \right\vert$ is odd. So the coefficient of $x^2$ at $g + g$ is the square of the coefficient of $x$ at $g$, and $x^2 = 0$ forces $x = 0$. Squaring is then injective, because $(x - y)^2 = x^2 - y^2$ in characteristic two, and injective implies bijective on a finite set. Over $\mathbb{F}_2$ the coefficients are fixed by squaring, so the displayed coefficient permutation gives the square root directly. The following lemma implements that permutation in the ambient cost model.

## Lean

Formalized as [`MIPRE.LowDegree.exists_mul_involute_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_mul_involute_eq), [`MIPRE.LowDegree.mul_self_bijective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.mul_self_bijective), [`MIPRE.LowDegree.exists_mul_involute_eq_of_charTwo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_mul_involute_eq_of_charTwo), [`MIPRE.LowDegree.binarySquareRoot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.binarySquareRoot), [`MIPRE.LowDegree.coeff_binarySquareRoot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.coeff_binarySquareRoot), [`MIPRE.LowDegree.binarySquareRoot_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.binarySquareRoot_mul_self), [`MIPRE.LowDegree.binarySquareRoot_mul_involute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.binarySquareRoot_mul_involute).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6389](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6389)
