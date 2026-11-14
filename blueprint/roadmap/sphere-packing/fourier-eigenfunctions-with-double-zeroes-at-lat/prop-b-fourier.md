---
declaration: proposition
origin: cited
lean: MagicFunction.b.Fourier.eig_b
statement: formalized
---

# b-fourier

$b(x)$ satisfies [(2)](README.md).

## Depends on

- [b-schwartz](prop-b-schwartz.md)

## Proof

Here, we repeat the arguments used in the proof of Proposition [a-fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L277). We use identity [Proposition a-fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L277) and change contour integration in $z$ and Fourier transform in $x$. Thus we obtain

$$
\begin{aligned}
\mathcal{F}(b)(x)= & \int\limits_{-1}^{i}\psi_T(z)\,z^{-4}\,e^{\pi i \|x\|^2 (\frac{-1}{z})}\,dz
+ \int\limits_{1}^{i}\psi_T(z)\,z^{-4}\,e^{\pi i \|x\|^2 (\frac{-1}{z})}\,dz  \\
-& 2\,\int\limits_{0}^{i}\psi_I(z)\,z^{-4}\,e^{\pi i \|x\|^2 (\frac{-1}{z})}\,dz
- 2\,\int\limits_{i}^{i\infty}\psi_S(z)\,z^{-4}\,e^{\pi i \|x\|^2 (\frac{-1}{z})}\,dz.
\end{aligned}
$$

We make the change of variables $w=\frac{-1}{z}$ and arrive at

$$
\begin{aligned}
\mathcal{F}(b)(x)= & \int\limits_{1}^{i}\psi_T\Big(\frac{-1}{w}\Big)\,w^{2}\,e^{\pi i \|x\|^2 w}\,dw
+ \int\limits_{-1}^{i}\psi_T\Big(\frac{-1}{w}\Big)\,w^{2}\,e^{\pi i \|x\|^2 w}\,dw  \\
-& 2\,\int\limits_{i\infty}^{i}\psi_I\Big(\frac{-1}{w}\Big)\,w^{2}\,e^{\pi i \|x\|^2 w}\,dw
- 2\,\int\limits_{i}^{0}\psi_S\Big(\frac{-1}{w}\Big)\,w^{2}\,e^{\pi i \|x\|^2 w}\,dw.
\end{aligned}
$$

Now we observe that the definitions [Definition psiI-psiT-psiS](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L440)–[Definition psiI-psiT-psiS](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L440) imply

$$
\begin{aligned}
\psi_T|_{-2}S=&-\psi_T  \\
\psi_I|_{-2}S=&\psi_S  \\
\psi_S|_{-2}S=&\psi_I.
\end{aligned}
$$

Therefore, we arrive at

$$
\begin{aligned}
\mathcal{F}(b)(x)= & \int\limits_{1}^{i}-\psi_T(z)\,e^{\pi i \|x\|^2 z}\,dz
+ \int\limits_{-1}^{i}-\psi_T(z)\,e^{\pi i \|x\|^2 z}\,dz  \\
+& 2\,\int\limits_{i}^{i\infty}\psi_S(z)\,e^{\pi i \|x\|^2 z}\,dz
+ 2\,\int\limits_{0}^{i}\psi_I(z)\,e^{\pi i \|x\|^2 w}\,dw.
\end{aligned}
$$

Now from [Definition b-definition](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L491) we see that

$$
\mathcal{F}(b)(x)=-b(x).
$$

## Lean

Stated as [`MagicFunction.b.Fourier.eig_b`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.eig_b); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 587](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/construct-a-b.tex#L587)
