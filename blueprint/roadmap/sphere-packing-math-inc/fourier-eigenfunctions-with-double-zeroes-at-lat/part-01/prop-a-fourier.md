---
declaration: proposition
origin: cited
lean: MagicFunction.a.Fourier.eig_a
statement: formalized
proof: formalized
---

# a-fourier

$a(x)$ satisfies [(1)](../README.md).

## Depends on

- [Ek-Fourier](../../modular-forms/part-01/lemma-ek-fourier.md)
- [E2](../../modular-forms/part-01/def-e2.md)
- [a-definition](def-a-definition.md)
- [Gaussian-Fourier](../../facts-from-fourier-analysis/lemma-gaussian-fourier.md)
- [a-schwartz](prop-a-schwartz.md)

## Proof

We recall that the Fourier transform of a Gaussian function is

$$
\mathcal{F}(e^{\pi i \|x\|^2 z})(y)=z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z}) }.\qquad\text{(18)}
$$

Next, we exchange the contour integration with respect to $z$ variable and Fourier transform with respect to $x$ variable in [(8)](def-a-definition.md). This can be done, since the corresponding double integral converges absolutely. In this way we obtain

$$
\begin{aligned}
\widehat{a}(y)=&\int\limits_{-1}^i\phi_0\Big(\frac{-1}{z+1}\Big)\,(z+1)^2\,z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z})}\,dz
+\int\limits_{1}^i\phi_0\Big(\frac{-1}{z-1}\Big)\,(z-1)^2\,z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z})}\,dz \\
-&2\int\limits_{0}^i\phi_0\Big(\frac{-1}{z}\Big)\,z^2\,z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z})}\,dz +2\int\limits_{i}^{i\infty}\phi_0(z)\,z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z})}\,dz.
\end{aligned}
$$

Now we make a change of variables $w=\frac{-1}{z}$. We obtain

$$
\begin{aligned}
\widehat{a}(y)=&\int\limits_{1}^i\phi_0\Big(1-\frac{1}{w-1}\Big)\,(\frac{-1}{w}+1)^2\,w^{2}\,e^{\pi i \|y\|^2 \,w}\,dw\\
+&\int\limits_{-1}^i\phi_0\Big(1-\frac{1}{w+1}\Big)\,(\frac{-1}{w}-1)^2\,w^2\,e^{\pi i \|y\|^2 \,w}\,dw\\
-&2\int\limits_{i \infty}^i\phi_0(w)\,e^{\pi i \|y\|^2 \,w}\,dw +2\int\limits_{i}^{0}\phi_0\Big(\frac{-1}{w}\Big)\,w^{2}\,e^{\pi i \|y\|^2 \,w}\,dw.
\end{aligned}
$$

Since $\phi_0$ is $1$-periodic we have

$$
\begin{aligned}
\widehat{a}(y)\,=\,&\int\limits_{1}^i\phi_0\Big(\frac{-1}{z-1}\Big)\,(z-1)^2\,e^{\pi i \|y\|^2 \,z}\,dz
+\int\limits_{-1}^i\phi_0\Big(\frac{-1}{z+1}\Big)\,(z+1)^2\,e^{\pi i \|y\|^2 \,z}\,dz \\
+&2\int\limits_{i}^{i\infty}\phi_0(z)\,e^{\pi i \|y\|^2 \,z}\,dz
-2\int\limits_{0}^{i}\phi_0\Big(\frac{-1}{z}\Big)\,z^{2}\,e^{\pi i \|y\|^2 \,z}\,dz \\
\,=\,&a(y).
\end{aligned}
$$

This finishes the proof of the proposition.

## Lean

Formalized as [`MagicFunction.a.Fourier.eig_a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.eig_a).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 280](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L280)
