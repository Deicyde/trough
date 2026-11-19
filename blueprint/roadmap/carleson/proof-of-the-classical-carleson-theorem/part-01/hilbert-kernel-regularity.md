---
declaration: lemma
origin: cited
lean: Hilbert_kernel_regularity
statement: formalized
proof: formalized
---

# Hilbert kernel regularity

For $x,y,y'\in {\mathbb{R}}$ with $x\neq y,y'$ and

$$
2|y-y'|\le |x-y|\, ,\qquad\text{(21)}
$$

we have

$$
|\kappa(x-y) - \kappa(x-y')|\le 2^{8}\frac{1}{|x-y|} \frac{|y-y'|}{|x-y|}\, .\qquad\text{(22)}
$$

## Depends on

- [lower secant bound](lower-secant-bound.md)

## Proof

Upon replacing $y$ by $y-x$ and $y'$ by $y'-x$ on the left-hand side of (21), we can assume that $x = 0$. Then the assumption (21) implies that $y$ and $y'$ have the same sign. Since $\kappa(y) = \bar \kappa(-y)$ we can assume that they are both positive. Then it follows from (21) that

$$
\frac{y}{2} \le y' \,.
$$

We distinguish four cases. If $y, y' \le 1$, then we have

$$
|\kappa(-y) - \kappa(-y')| = \left| \frac{1 - y}{1- e^{-iy}} - \frac{1 - y'}{1- e^{-iy'}}\right|
$$

and by the fundamental theorem of calculus

$$
= \left| \int_{y'}^{y} \frac{-1 + e^{-it} + i(1-t)e^{it}}{(1 - e^{-it})^2} \,dt \right|\,.
$$

Using $y' \ge \frac{y}{2}$ and [lower secant bound](lower-secant-bound.md), we bound this by

$$
\le |y - y'| \sup_{\frac{y}{2} \le t \le 1} \frac{3}{|1 - e^{-it}|^2} \le 3 |y-y'| (2 \frac{2}{y})^2 \le 2^{6} \frac{|y-y'|}{|y|^2}\,.
$$

If $y \le 1$ and $y' > 1$, then $\kappa(-y') = 0$ and we have from the first case

$$
|\kappa(-y) - \kappa(-y')| = |\kappa(-y) - \kappa(-1)| \le 2^{6} \frac{|y-1|}{|y|^2} \le 2^{6} \frac{|y-y'|}{|y|^2}\,.
$$

Similarly, if $y > 1$ and $y' \le 1$, then $\kappa(-y) = 0$ and we have from the first case

$$
|\kappa(-y) - \kappa(-y')| = |\kappa(-y') - \kappa(-1)| \le 2^{6} \frac{|y'-1|}{|y'|^2} \le 2^{6} \frac{|y-y'|}{|y'|^2}\,.
$$

Using again $y' \ge \frac{y}{2}$, we bound this by

$$
\le 2^{6} \frac{|y-y'|}{|y / 2|^2} = 2^{8} \frac{|y-y'|}{|y|^2}
$$

Finally, if $y, y' > 1$ then

$$
|\kappa(-y) - \kappa(-y')| = 0 \le 2^{8} \frac{|y-y'|}{|y|^2}\,.
$$

## Lean

Formalized as [`Hilbert_kernel_regularity`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Hilbert_kernel_regularity).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8452](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8452)
