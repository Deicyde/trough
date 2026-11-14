---
declaration: proposition
origin: cited
lean: MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_laplace_psiI_main
statement: formalized
proof: formalized
---

# b-double-zeros

For $r>\sqrt{2}$ function $b(r)$ can be expressed as

$$
b(r)=-4\sin(\pi r^2/2)^2\,\int\limits_{0}^{i\infty}\psi_I(z)\,e^{\pi i r^2 \,z}\,dz.\qquad\text{(40)}
$$

## Depends on

- [psiI-psiT-psiS](def-psii-psit-psis.md)
- [disc-nonvanishing](../../modular-forms/part-02/cor-disc-nonvanishing.md)

## Proof

We denote the right hand side of (40) by $c(r)$. By Corollary [psiI-near-0-infty](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L634), the integral in (40) converges for $r>\sqrt{2}$. Then we rewrite it in the following way:

$$
c(r)=\int\limits_{-1}^{i\infty-1}\psi_I(z+1)\,e^{\pi i r^2 \,z}\,dz-2\int\limits_{0}^{i\infty}\psi_I(z)\,e^{\pi i r^2 \,z}\,dz+
\int\limits_{1}^{i\infty+1}\psi_I(z-1)\,e^{\pi i r^2 \,z}\,dz.
$$

From the Fourier expansion [(29)](README.md) we know that $\psi_I(z)=e^{-2\pi i z}+O(1)$ as $\Im(z)\to\infty$. By assumption $r^2>2$, hence we can deform the path of integration and write

$$
\begin{aligned}
\int\limits_{-1}^{i\infty-1}\psi_I(z+1)\,e^{\pi i r^2 \,z}\,dz=&
\int\limits_{-1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz+\int\limits_{i}^{i\infty}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz\qquad\text{(41)}\\
\int\limits_{1}^{i\infty+1}\psi_I(z-1)\,e^{\pi i r^2 \,z}\,dz=&
\int\limits_{-1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz+\int\limits_{i}^{i\infty}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz.
\end{aligned}
$$

We have

$$
\begin{aligned}c(r)=&\int\limits_{-1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz+\int\limits_{1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz
-2\int\limits_{0}^{i}\psi_I(z)\,e^{\pi i r^2 \,z}\,dz\qquad\text{(42)}\\
&+2\int\limits_{i}^{i\infty}(\psi_T(z)-\psi_I(z))\,e^{\pi i r^2 \,z}\,dz.
\end{aligned}
$$

Next, we check that the functions $\psi_I,\psi_T$, and $\psi_S$ satisfy the following identity:

$$
\psi_T+\psi_S=\psi_I.\qquad\text{(43)}
$$

Indeed, from definitions [(23)](def-psii-psit-psis.md)-[(25)](def-psii-psit-psis.md) we get

$$
\begin{aligned}\psi_T+\psi_S=&(h-h|_{-2}ST)|_{-2}T+(h-h|_{-2}ST)|_{-2}S\\
=&h|_{-2}T-h|_{-2}ST^2+h|_{-2}S-h|_{-2}STS.\end{aligned}
$$

Note that $ST^2S$ belongs to $\Gamma_0(2)$. Thus, since $h\in M^!_{-2}\Gamma_0(2)$ we get

$$
\psi_T+\psi_S=h|_{-2}T-h|_{-2}STS.
$$

Now we observe that $T$ and $STS(ST)^{-1}$ are also in $\Gamma_0(2)$. Therefore,

$$
\psi_T+\psi_S=h|_{-2}T-h|_{-2}STS=h|_{-2}-h|ST=\psi_I.
$$

Combining (42) and (43) we find

$$
\begin{aligned}c(r)=&\int\limits_{-1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz+\int\limits_{1}^{i}\psi_T(z)\,e^{\pi i r^2 \,z}\,dz
-2\int\limits_{0}^{i}\psi_I(z)\,e^{\pi i r^2 \,z}\,dz\\
&-2\int\limits_{i}^{i\infty}\psi_S(z)\,e^{\pi i r^2 \,z}\,dz\\
=&b(r).
\end{aligned}
$$

## Lean

Formalized as [`MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_laplace_psiI_main`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_laplace_psiI_main).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 650](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L650)
