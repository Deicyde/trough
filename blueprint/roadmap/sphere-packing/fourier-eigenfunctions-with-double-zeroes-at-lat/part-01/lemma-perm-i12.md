---
declaration: lemma
origin: cited
lean: MagicFunction.a.Fourier.perm_I₁_I₂
statement: formalized
---

# perm-I12

[(15)](README.md) holds: $\mathcal{F}(I_1 + I_2) = I_3 + I_4$.

## Depends on

- [a-definition](def-a-definition.md)
- [phi0-transform](lemma-phi0-transform.md)
- [a-schwartz](prop-a-schwartz.md)

## Proof

Fix $\xi \in \mathbb{R}^8$ and write $F_j := \mathcal{F}(I_j(\|\cdot\|^2))$. The double integral defining $F_1(\xi)$ converges absolutely — the estimates of Lemmas [bound-I1-I3-I5](lem-bound-i1-i3-i5.md) and [bound-I2-I4-I6](lem-bound-i2-i4-i6.md) bound the inner integral uniformly by a Schwartz-type bound in $x$ — so by Fubini's theorem we may exchange the Fourier integral with the contour integral. Lemma [Gaussian-Fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L15) then gives

$$
\begin{aligned}
F_1(\xi) &= \int_{-1}^{-1+i} \phi_0\left(\frac{-1}{z+1}\right) (z+1)^2\, z^{-4}\, e^{\pi i \|\xi\|^2 (\frac{-1}{z})}\, \mathrm{d} z,
\end{aligned}
$$

and similarly for $F_2$ with contour from $-1 + i$ to $i$. We substitute $w = -1/z$, which maps the two segments onto circular arcs from $1$ to $\frac{1+i}{2}$ and from $\frac{1+i}{2}$ to $i$ respectively, and compute, using the $1$-periodicity [(6)](lemma-phi0-transform.md) of $\phi_0$,

$$
\phi_0\left(-1-\frac{1}{w-1}\right)\left(\frac{-1}{w}+1\right)^2 w^2 = \phi_0\left(\frac{-1}{w-1}\right)(w-1)^2,
$$

so that $F_1(\xi) + F_2(\xi)$ is the integral of $\phi_0\left(\frac{-1}{w-1}\right)(w-1)^2 e^{\pi i \|\xi\|^2 w}$ along the concatenated arc from $1$ to $i$. This integrand is holomorphic on $\mathfrak{H}$ (multiply out [(7)](lemma-phi0-transform.md)) and continuous up to the boundary, so by the Cauchy–Goursat theorem the arc may be replaced by the rectangular path $1 \to 1 + i \to i$. The two resulting integrals are precisely $I_3(\|\xi\|^2)$ and $I_4(\|\xi\|^2)$.

## Lean

Stated as [`MagicFunction.a.Fourier.perm_I₁_I₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.perm_I₁_I₂); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 310](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L310)
