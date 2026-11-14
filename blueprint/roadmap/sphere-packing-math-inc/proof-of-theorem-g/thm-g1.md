---
declaration: theorem
origin: cited
lean: MagicFunction.g.CohnElkies.g_cohnElkies₁, MagicFunction.g.CohnElkies.g_cohnElkies₂, g_zero, fourier_g_zero
statement: formalized
proof: formalized
---

# g1

The function

$$
g(x):=\frac{\pi\,i}{8640}a(x)-\frac{i}{240\pi}\,b(x)
$$

satisfies conditions [(5)](../cohn-elkies-linear-programming-bounds/thm-g.md)–[(7)](../cohn-elkies-linear-programming-bounds/thm-g.md).

## Depends on

- [a-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-fourier.md)
- [b-fourier](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-b-fourier.md)
- [a-double-zeros](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-double-zeros.md)
- [b-double-zeros](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-b-double-zeros.md)
- [ineqA](prop-ineqa.md)
- [ineqB](prop-ineqb.md)
- [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a0.md)
- [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b0.md)

## Proof

First, we prove that [(5)](../cohn-elkies-linear-programming-bounds/thm-g.md) holds. By Propositions [a-double-zeros](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-double-zeros.md) and [b-double-zeros](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-b-double-zeros.md) we know that for $r>\sqrt{2}$

$$
g(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty A(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(16)}
$$

where

$$
A(t)=-t^2\phi_0(i/t)-\frac{36}{\pi^2}\,\psi_I(it).
$$

from the Proposition [ineqA](prop-ineqa.md) we know that $A(t)<0\quad\mbox{for}\;t\in(0,\infty).$ Therefore identity (16) implies [(5)](../cohn-elkies-linear-programming-bounds/thm-g.md).

Next, we prove [(6)](../cohn-elkies-linear-programming-bounds/thm-g.md). By Propositions [a-another-integral](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a-another-integral.md) and [b-another-integral](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b-another-integral.md) we know that for $r>0$

$$
\widehat{g}(r)=\frac{\pi}{2160}\,\sin(\pi r^2/2)^2\,\int\limits_0^\infty B(t)\,e^{-\pi r^2 t}\,dt\qquad\text{(17)}
$$

where

$$
B(t)=-t^2\phi_0(i/t)+\frac{36}{\pi^2}\,\psi_I(it).
$$

Finally, the property [(7)](../cohn-elkies-linear-programming-bounds/thm-g.md) readily follows from Proposition [a0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-01/prop-a0.md) and Proposition [b0](../fourier-eigenfunctions-with-double-zeroes-at-lat/part-02/prop-b0.md). This finishes the proof of Theorems g1 and [g](../cohn-elkies-linear-programming-bounds/thm-g.md).

## Lean

Formalized as [`MagicFunction.g.CohnElkies.g_cohnElkies₁`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.g_cohnElkies₁), [`MagicFunction.g.CohnElkies.g_cohnElkies₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.g_cohnElkies₂), [`g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_zero), [`fourier_g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/fourier_g_zero).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 228](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L228)
