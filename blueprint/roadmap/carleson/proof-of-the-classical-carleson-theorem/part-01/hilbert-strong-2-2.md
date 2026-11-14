---
declaration: lemma
origin: cited
lean: Hilbert_strong_2_2
statement: formalized
proof: formalized
---

# Hilbert strong 2 2

Let $0\lt r$. Let $f$ be a bounded, measurable function on $\mathbb{R}$. Then

$$
\|H_rf\|_{2}\leq 2^{9} \|f\|_2,\qquad\text{(10)}
$$

where

$$
H_r f(x) := T_r f(x) = \int_{r\le |x-y|} \kappa(x-y) f(y) \, dy\qquad\text{(11)}
$$

## Depends on

- [modulated averaged projection](modulated-averaged-projection.md)
- [integrable bump convolution](integrable-bump-convolution.md)
- [Dirichlet approximation](dirichlet-approximation.md)

## Proof

*Proof of Hilbert strong 2 2.* We first show that if $f$ is supported in $[1, 4]$, then

$$
\|H_r f\|_{L^2[2, 3]} \le 2^{8} \|f\|_{L^2({\mathbb{R}})}\,.\qquad\text{(12)}
$$

Let $\tilde{f}$ be the $2\pi$-periodic extension of $f$ to $\mathbb{R}$. Let $N$ be the smallest integer larger than $\frac 1r$. Then, [(30)](dirichlet-approximation.md) shows that the kernels of $H_r$ and $2\pi L_N$ differ by at most $12k_r$ on $[-\pi, \pi]$. Consider $x \in [2,3]$. When computing $H_r f(x)$ and $2\pi L_N f(x)$, the kernels are computed at points of the form $x-y$ with $f(y) \ne 0$, i.e., $y \in [1,4]$. As $x\in [2,3]$, the difference $x-y$ is bounded in absolute value by $2$, and therefore belongs to $[-\pi, \pi]$, where the above bound holds.

It follows that, for $x \in [2,3]$,

$$
|H_r \tilde{f}(x)|\leq 2\pi |L_N \tilde{f}(x)|+12\left|\int_{0}^{2\pi}k_r(x-y)\tilde{f}(y)\, dy\right|.
$$

Taking $L^2$ norm and using its sub-additivity, we get

$$
\|H_r \tilde{f}\|_{L^2[2, 3]}\leq 2\pi \|L_N \tilde{f}\|_{L^2[0, 2\pi]}\, + 12\left(\int_{0}^{2\pi} \left|\int_{0}^{2\pi}k_r(x-y)\tilde{f}(y)\, dy\right|^2\, dx\right)^{\frac{1}{2}}.
$$

Since $\kappa$ is supported in $[-1,1]$, we have that $H_r\tilde{f}$ agrees with $H_r f$ on $[2,3]$. Using [modulated averaged projection](modulated-averaged-projection.md) and [integrable bump convolution](integrable-bump-convolution.md), we conclude

$$
\|H_r f\|_{L^2[2, 3]} \le 2\pi \|f\|_{L^2[0, 2\pi]} + 12 \cdot 17 \|f\|_{L^2[0, 2\pi]}\,,
$$

which gives (12).

Suppose now that $f$ is supported in $[c, c+3]$ for some $c \in {\mathbb{R}}$. Then the function $g(x) = f(x-c+1)$ is supported in $[1, 4]$. By a change of variables in (11), we have $H_r g(x ) = H_r f(x - c + 1)$. Thus, by (12)

$$
\|H_rf\|_{L^2[c+1, c+2]} = \|H_r g\|_{L^2[2,3]} \le 2^{8} \|g\|_2 = 2^8 \|f\|_2\,.\qquad\text{(13)}
$$

Let now $f$ be arbitrary. Since $\kappa(x) = 0$ for $|x| > 1$, we have for all $x \in [c+1, c+2]$

$$
H_rf(x) = H_r(f \mathbf{1}_{[c, c+3]})(x)\,.
$$

Thus

$$
\int_{c+1}^{c+2} |H_r f(x)|^2 \, \mathrm{d}x = \int_{c+1}^{c+2}|H_r(f \mathbf{1}_{[c, c+3]})(x)|^2 \, \mathrm{d}x\,.
$$

Applying the bound (13), this is

$$
\le 2^{16} \int_{c}^{c+3} |f(x)|^2 \, \mathrm{d}x\,.
$$

Summing over all $c \in \mathbb{Z}$, we obtain

$$
\int_{{\mathbb{R}}} |H_rf(x)|^2 \, \mathrm{d}x \le 3 \cdot 2^{16} \int_{{\mathbb{R}}} |f(x)|^2 \, \mathrm{d}x\,.
$$

This completes the proof.

## Lean

Formalized as [`Hilbert_strong_2_2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Hilbert_strong_2_2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8301](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8301)
