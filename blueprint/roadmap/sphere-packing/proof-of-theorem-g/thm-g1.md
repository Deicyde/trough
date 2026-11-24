---
declaration: theorem
origin: cited
lean: g, g_nonpos, g_Fourier_nonneg, g_zero, fourier_g_zero
statement: formalized
---

# g1

The function

$$
g(x):=\frac{\pi\,i}{8640}a(x)-\frac{i}{240\pi}\,b(x)
$$

satisfies conditions [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53)–[Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53).

## Depends on

- [a-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-fourier.md)
- [b-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b-fourier.md)
- [ineqA](prop-ineqa.md)
- [ineqB](prop-ineqb.md)
- [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a0.md)
- [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b0.md)

## Proof

Note first that, by Propositions [a-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-fourier.md) and [b-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b-fourier.md),

$$
\widehat{g}=\frac{\pi\,i}{8640}\,a+\frac{i}{240\pi}\,b.
$$

We prove that [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53) holds. By Propositions [a-double-zeros](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L392) and [b-double-zeros](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L750), parametrising the contours by $z = it$, we know that for $r>\sqrt{2}$

$$
a(r) = 4i\,\sin(\pi r^2/2)^2\int\limits_0^\infty t^2\,\phi_0(i/t)\,e^{-\pi r^2 t}\,dt, \qquad
b(r) = -4i\,\sin(\pi r^2/2)^2\int\limits_0^\infty \psi_I(it)\,e^{-\pi r^2 t}\,dt,
$$

and hence, since $\frac{\pi i}{8640}\cdot 4i = -\frac{\pi}{2160}$ and $\frac{i}{240\pi}\cdot 4i = -\frac{\pi}{2160}\cdot\frac{36}{\pi^2}$,

$$
g(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty A(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(14)}
$$

where $A$ is as in [(1)](prop-ineqa.md). From Proposition [ineqA](prop-ineqa.md) we know that $A(t)<0$ for $t\in(0,\infty)$. Therefore identity (14) implies [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53).

Next, we prove [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53). By Propositions [a-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L444) and [b-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L785) (which are valid on all of $[0, \infty)$), the same bookkeeping gives, for $r>0$,

$$
\widehat{g}(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty B(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(15)}
$$

where $B$ is as in [(3)](prop-ineqb.md), and $B(t) > 0$ for $t \in (0, \infty)$ by Proposition [ineqB](prop-ineqb.md). Hence $\widehat{g}(r) \geq 0$ for $r > 0$, and $\widehat{g}(0) = 1 > 0$ by the computation below.

Finally, the property [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53) readily follows from Proposition [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a0.md) and Proposition [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b0.md):

$$
g(0) = \widehat{g}(0) = \frac{\pi i}{8640}\cdot\frac{-8640\,i}{\pi} = 1.
$$

This finishes the proof of Theorems g1 and [g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/cohn-elkies.tex#L53).

## Lean

Stated as [`g`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g), [`g_nonpos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_nonpos), [`g_Fourier_nonneg`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_Fourier_nonneg), [`g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_zero), [`fourier_g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/fourier_g_zero); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 241](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/modform-ineq.tex#L241)
