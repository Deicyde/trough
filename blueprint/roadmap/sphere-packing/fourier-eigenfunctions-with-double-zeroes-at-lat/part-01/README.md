---
navigation: transparent
---

# phi4-phi2-phi0 to perm-J12

- [phi4-phi2-phi0](def-phi4-phi2-phi0.md)

These functions are holomorphic on $\mathfrak{H}$: their numerators are built from the holomorphic functions $E_2$, $E_4$ and $E_6$, and $\Delta$ does not vanish on $\mathfrak{H}$ (Corollary [disc-nonvanishing](../../modular-forms/part-02/cor-disc-nonvanishing.md)).

The function $\phi_0(z)$ is not modular; however, it satisfies the following transformation rules:

- [phi0-transform](lemma-phi0-transform.md)

For our formalization, we choose rectangular contours for the first and the second integral, and write it as follows.

- [a-definition](def-a-definition.md)

In the original paper, the integrals $I_1$ and $I_2$ are combined, as well as $I_3$ and $I_4$, with the contours running from $\mp 1$ to $i$. Since the integrands are holomorphic on $\mathfrak{H}$ (multiply out [(7)](lemma-phi0-transform.md)), the choice of contours between these endpoints does not matter; we choose rectangular ones, as these are the contours to which the Cauchy–Goursat theorem is most easily applied. In the formalisation, each $I_j$ is written as an integral over the real parametrising variable $t \in [0,1]$ (or $t \in [1, \infty)$ for $I_6$).

## Bounds for the Integrands

The key estimate is the following bound for quotients by $\Delta$, applicable to all integrands appearing in the definitions of $a$ and $b$.

- [mod-div-disc-bound](lemma-mod-div-disc-bound.md)

When $f(z)$ is a (quasi)modular form, we can take $k$ to be the weight of $f$.

*The proof of [Lemma mod-div-disc-bound](lemma-mod-div-disc-bound.md) is shown with its statement.*

To apply Lemma [mod-div-disc-bound](lemma-mod-div-disc-bound.md) to $\phi_0$, $\phi_{-2}$ and $\phi_{-4}$ — and, later, to the $\psi$-functions — we need to know that the numerators have Fourier expansions with polynomially growing coefficients, and we need their leading exponents. For a function $f$ with Fourier expansion as in Lemma [mod-div-disc-bound](lemma-mod-div-disc-bound.md), write $n_0(f)$ for the smallest index with $c_f(n_0(f)) \neq 0$. The following closure property reduces both questions to the corresponding facts about $E_2$, $E_4$, $E_6$ and the $H$-functions.

As corollaries, we have the following bounds for $\phi_0$, $\phi_{-2}$, and $\phi_{-4}$.

Note that we can take the constants $C_0$, $C_{-2}$, and $C_{-4}$ as

$$
\begin{aligned}
C_0 &= 9 \cdot 240^2 \cdot e^{\pi} \cdot \frac{E_4'(i/2)^{2}}{\Delta(i/2)}  \\
C_{-2} &= 3 \cdot \frac{E_4(i/2) E_4'(i/2)}{\Delta(i/2)}  \\
C_{-4} &= e^{-\pi} \cdot \frac{E_4(i/2)^{2}}{\Delta(i/2)}.
\end{aligned}
$$

## Decay of the Integrals $I_j$

- [bound-I1-I3-I5](lem-bound-i1-i3-i5.md)

For the integrals $I_2$, $I_4$, and $I_6$, whose contours do not touch the real axis, the decay is exponential.

- [bound-I2-I4-I6](lem-bound-i2-i4-i6.md)

The bound appearing in Lemma [bound-I1-I3-I5](lem-bound-i1-i3-i5.md) decays faster than any polynomial as $r \to \infty$; this is a consequence of standard facts about the $\Gamma$ function. We state the lemma for an arbitrary exponent $\alpha > 0$, so that it also applies (with $\alpha = \pi$) to the analogous bounds for $b$ in Lemma [bound-J1-J3-J5](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L642) below.

## Smoothness of the Integrals $I_j$, and Schwartzness of $a$

The functions $I_j$ are *not* Schwartz functions on $\mathbb{R}$: the bounds above degrade into exponential *growth* as $r \to -\infty$, and $I_6$ is not even defined by a convergent integral for $r \leq -2$. This is harmless: $a(x) = a_\mathrm{rad}(\|x\|^2)$ only sees $a_\mathrm{rad}$ on $[0, \infty)$, and Lemma [Ij-smooth](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L280) shows that $a_\mathrm{rad}$ satisfies the hypotheses of Corollary [schwartz-of-nonneg-decay](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L187) with $\theta = -2$.

- [a-schwartz](prop-a-schwartz.md)

## The Eigenfunction Property of $a$

We now prove that $a$ satisfies condition (1). The Fourier transform acts on the summands of $a$ by permuting them: writing (by a slight abuse of notation) $I_j$ also for the radial function $x \mapsto I_j(\|x\|^2)$ on $\mathbb{R}^8$, we shall show

$$
\begin{aligned}
\mathcal{F}(I_1 + I_2) &= I_3 + I_4,\qquad\text{(15)}\\
\mathcal{F}(I_5) &= I_6.\qquad\text{(16)}\end{aligned}
$$

- [perm-I12](lemma-perm-i12.md)
- [perm-I56](lemma-perm-i56.md)
- [perm-I-reverse](lemma-perm-i-reverse.md)
- [a-fourier](prop-a-fourier.md)

## Double Zeroes of $a$

Next, we check that $a$ has double zeroes at all $\Lambda_8$-lattice points of length greater then $\sqrt{2}$. The contour deformations in this argument involve unbounded contours; the following consequence of the Cauchy–Goursat theorem, which is available in Mathlib, is what we need.

- [Cauchy–Goursat for unbounded rectangular contours](lem-cg-unbounded.md)

Using [Corollary phi0-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L138), [Corollary phi2-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L159), and [Corollary phi4-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L170), we can control the behavior of $\phi_0$ near $0$ and $i\infty$.

In particular, fix a vertical strip $x_1 \leq \Re z \leq x_2$ and let $r > 2$. By [(7)](lemma-phi0-transform.md), $\phi_0(-1/z)\, z^2 = z^2 \phi_0(z) - \frac{12 i}{\pi} z\, \phi_{-2}(z) - \frac{36}{\pi^2}\phi_{-4}(z)$, and on the strip $|z|$ is bounded by a multiple of $\Im z$ when $\Im z \geq 1$. Hence there is a constant $C$, depending on $x_1$ and $x_2$, such that the integrand $\phi_0(-1/z)\, z^2\, e^{\pi i r z}$ is bounded by $C e^{\pi (2 - r)\Im z}$ for $\Im z \geq 1$ and $x_1 \leq \Re z \leq x_2$. So it tends to $0$ as $\Im(z) \to \infty$, uniformly on the strip, and is integrable on vertical rays in the strip; the same applies to its translates by $\pm 1$. The bound is *not* uniform in $\Re z$ over all of $\mathbb{C}$ (the factor $z^2$ grows along horizontal lines), which is why Lemma [Cauchy–Goursat for unbounded rectangular contours](lem-cg-unbounded.md) is stated for a fixed strip. This provides the hypotheses of Lemma [Cauchy–Goursat for unbounded rectangular contours](lem-cg-unbounded.md) in the following proof, applied to the strips $-1 \leq \Re z \leq 0$ and $0 \leq \Re z \leq 1$ with $y = 1$. (In the radial variable, these are inputs of the form $r = \|x\|^2 > 2$, i.e. $\|x\| > \sqrt 2$.)

The factor $\sin(\pi r^2/2)^2$ vanishes to second order at $r = \sqrt{2n}$ for every integer $n$, so Proposition [a-double-zeros](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L392) exhibits the required double zeroes of $a$ at all $\Lambda_8$-vectors of length greater than $\sqrt 2$.

## Special Values of $a$

Finally, we find another convenient integral representation for $a$ and compute the value of $a$ at $0$.

From the identity [Proposition a-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L444) we see that the values $a(r)$ are in $i\mathbb{R}$ for all $r\in\mathbb{R}_{\geq0}$.

- [a0](prop-a0.md)

## The Integrands for $b$

Now we construct function $b$. To this end we consider the function

- [ h](def-h.md)

It is easy to see that $h\in M^!_{-2}(\Gamma_0(2))$. Indeed, first we check that $h|_{-2}\gamma=h$ for all $\gamma\in\Gamma_0(2)$. Since the group $\Gamma_0(2)$ is generated by elements $\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)$ and $\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ it suffices to check that $h$ is invariant under their action. This follows immediately from [(10)](../../modular-forms/part-02/lemma-theta-transform-s-t.md)–[(12)](../../modular-forms/part-02/lemma-theta-transform-s-t.md) and [(17)](def-h.md). Next we analyze the poles of $h$. It is known (8, Chapter I Lemma 4.1) that $\theta_{10}$ has no zeros in the upper-half plane and hence $h$ has poles only at the cusps. At the cusp $i\infty$ this modular form has the Fourier expansion

$$
h(z)\,=\,q^{-1} + 16 - 132 q + 640 q^2 - 2550 q^3+O(q^4).
$$

Let $I=\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)$, $T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$, and $S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ be elements of $\Gamma_1$.

- [psiI-psiT-psiS](def-psii-psit-psis.md)

The weight $2$ transformation laws of the $H$-functions (Lemma [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md)) yield explicit expressions for the $\psi$-functions.

- [psi-explicit](lemma-psi-explicit.md)

The same computations give the following relations, which we use repeatedly; all follow from Definition [psiI-psiT-psiS](def-psii-psit-psis.md), Lemma [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md) and the cocycle property of the slash action.

- [psi-slash-relations](lemma-psi-slash-relations.md)

For the growth estimates it is convenient to express the $\psi$-functions, like the $\phi$-functions, as quotients by $\Delta$.

Now, we are ready to define function $b$. Again, the definition here is slightly different from that in (12), where all the contours are chosen to be the straight lines.

- [b-definition](def-b-definition.md)

By Lemma [psi-slash-relations](lemma-psi-slash-relations.md), the integrands of $J_1, \ldots, J_5$ can be rewritten in a form exactly parallel to those of $I_1, \ldots, I_5$, with $\psi_S$ playing the role of $\phi_0$:

$$
\begin{aligned}
J_1(r) &= \int_{-1}^{-1 + i} \psi_S\!\left(\frac{-1}{z + 1}\right) (z + 1)^2\, e^{\pi i r z} \, \mathrm{d} z,
& J_3(r) &= \int_{1}^{1 + i} \psi_S\!\left(\frac{-1}{z - 1}\right) (z - 1)^2\, e^{\pi i r z} \, \mathrm{d} z,\qquad\text{(37)}\\
J_2(r) &= \int_{-1 + i}^{i} \psi_S\!\left(\frac{-1}{z + 1}\right) (z + 1)^2\, e^{\pi i r z} \, \mathrm{d} z,
& J_4(r) &= \int_{1 + i}^{i} \psi_S\!\left(\frac{-1}{z - 1}\right) (z - 1)^2\, e^{\pi i r z} \, \mathrm{d} z, \\
J_5(r) &= -2\int_{0}^{i} \psi_S\!\left(\frac{-1}{z}\right) z^2\, e^{\pi i r z} \, \mathrm{d} z.
\end{aligned}
$$

The proofs of the analytic properties of $b$ below follow those for $a$ with these expressions in place of the $\phi_0$-integrands; we record the statements and indicate only the differences.

## Schwartzness of $b$

As in the case of $a(x)$, we start with exponential bounds for the $\psi$-functions.

Note the asymmetry with the $a$-side: since $\psi_S$ decays like $e^{-\pi \Im z}$ rather than $e^{-2\pi \Im z}$, the integral defining $J_6$ converges (and defines a smooth function) only for $r > -1$, whereas $I_6$ converged for $r > -2$. Arguing exactly as in Lemma [Ij-smooth](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L280), the functions $J_1, \ldots, J_5$ are smooth on $\mathbb{R}$ and $J_6$ is smooth on $(-1, \infty)$, with all derivatives of all $J_j$ decaying rapidly on $[0, \infty)$ by Lemmas [bound-J1-J3-J5](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L642), [bound-J2-J4-J6](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L652) and [integral-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L250) (the latter applied with $\alpha = \pi$). Corollary [schwartz-of-nonneg-decay](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L187) then applies with $\theta = -1$, the cutoff transitioning on $[-1/2, 0]$.

- [b-schwartz](prop-b-schwartz.md)

## The Eigenfunction Property of $b$

The Fourier transform also permutes the summands of $b$, but with a sign change:

$$
\begin{aligned}
\mathcal{F}(J_1 + J_2) &= -(J_3 + J_4),\qquad\text{(38)}\\
\mathcal{F}(J_5) &= -J_6.\qquad\text{(39)}\end{aligned}
$$

- [perm-J12](lemma-perm-j12.md)
