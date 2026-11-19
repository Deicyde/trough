---
declaration: theorem
origin: cited
lean: g, g_nonpos, g_Fourier_nonneg, g_zero, fourier_g_zero
statement: formalized
---

# g1

The function

$$
g(x):=\frac{\pi\,i}{8640}a(x)+\frac{i}{240\pi}\,b(x)
$$

satisfies conditions [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44)–[Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44).

## Depends on

- [b-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/prop-b-fourier.md)
- [ineqA](prop-ineqa.md)
- [ineqB](prop-ineqb.md)
- [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/prop-a0.md)
- [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/prop-b0.md)

## Proof

First, we prove that [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44) holds. By Propositions [a-double-zeros](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L330) and [b-double-zeros](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L655) we know that for $r>\sqrt{2}$

$$
g(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty A(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(14)}
$$

where

$$
A(t)=-t^2\phi_0(i/t)-\frac{36}{\pi^2}\,\psi_I(it).
$$

from the Proposition [ineqA](prop-ineqa.md) we know that $A(t)<0\quad\mbox{for}\;t\in(0,\infty).$ Therefore identity (14) implies [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44).

Next, we prove [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44). By Propositions [a-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L378) and [b-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L699) we know that for $r>0$

$$
\widehat{g}(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty B(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(15)}
$$

where

$$
B(t)=-t^2\phi_0(i/t)+\frac{36}{\pi^2}\,\psi_I(it).
$$

Finally, the property [Theorem g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44) readily follows from Proposition [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/prop-a0.md) and Proposition [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/prop-b0.md). This finishes the proof of Theorems g1 and [g](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/cohn-elkies.tex#L44).

## Lean

Stated as [`g`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g), [`g_nonpos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_nonpos), [`g_Fourier_nonneg`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_Fourier_nonneg), [`g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_zero), [`fourier_g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/fourier_g_zero); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 235](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L235)
