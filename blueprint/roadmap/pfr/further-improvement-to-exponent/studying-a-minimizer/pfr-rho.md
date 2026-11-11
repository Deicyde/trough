---
declaration: proposition
origin: cited
lean: rho_PFR_conjecture
statement: formalized
proof: formalized
---

# pfr-rho

For any random variables $Y_1,Y_2$, there exist a subgroup $H$ such that

$$
2\rho(U_H) \leq \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$\phi$-minimizers exist](phi-min-exist.md)
- [phi-minimizer-zero-distance](phi-minimizer-zero-distance.md)
- [phi-min-def](phi-min-def.md)
- [Rho invariant](../rho-functionals/rho-invariant.md)
- [Translate is uniform on symmetry group](../../the-100-version-of-pfr/sym-zero.md)

## Proof

Let $X_1,X_2$ be a $\phi$-minimizer. By [Proposition phi-minimizer-zero-distance](phi-minimizer-zero-distance.md) $d[X_1;X_2]=0$, which by [Definition phi-min-def](phi-min-def.md) implies $\rho(X_1)+\rho(X_2)\le \rho(Y_1) + \rho(Y_2) + \frac{1}{\eta} d[Y_1;Y_2]$ for every $\eta<1/8$. Take the limit at $\eta=1/8$ to get $\rho(X_1)+\rho(X_2)\le \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2]$. By [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) and [Distance nonnegative](../../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md) we have $d[X_1;X_1]=d[X_2;X_2]=0$, and by [Translate is uniform on symmetry group](../../the-100-version-of-pfr/sym-zero.md) there are $H_1:=\mathrm{Sym}[X_1],H_2:=\mathrm{Sym}[X_2]$ such that $X_1=U_{H_1}+x_1$ and $X_2=U_{H_2}+x_2$ for some $x_2$. By [Rho invariant](../rho-functionals/rho-invariant.md) we get $\rho(U_{H_1})+\rho(U_{H_2})\le \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2]$, and thus the claim holds for $H=H_1$ or $H=H_2$.

## Lean

Formalized as [`rho_PFR_conjecture`](https://teorth.github.io/pfr/docs/find/#doc/rho_PFR_conjecture).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 341](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L341)
