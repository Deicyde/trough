---
declaration: theorem
origin: cited
lean: ShiftTwoBound
statement: formalized
proof: formalized
---

# ShiftTwoBound

For all $\delta\in (0,1)$ and $t\in\mathbb{R}$ with $|t|\geq 2$ we have

$$
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta+2it)\right)\ll\log|t|.
$$

## Depends on

- [ZeroWindow](zerowindow.md)

## Proof depends on

- [SumBoundI](sumboundi.md)

## Proof

Note that, for $\rho\in\mathcal{Z}_{2t}$

$$
\begin{aligned}
\Re \left(\frac{1}{1+\delta+2it-\rho}\right)
&=\Re \left(\frac{1+\delta-2it-\overline{\rho}}
{(1+\delta+2it-\rho)(1+\delta-2it-\overline{\rho})}\right) \\
&=\frac{\Re (1+\delta-2it-\overline{\rho})}{|1+\delta+2it-\rho|^2}
=\frac{1+\delta-\Re \rho}{(1+\delta-\Re \rho)^2+(2t-\mathfrak{I}\rho)^2}.
\end{aligned}
$$

Now since $\rho\in\mathcal{Z}_{2t}$, we have that $|\rho-(3/2+2it)|\leq 3/4$. So, we have $\Re \rho\in[3/4,9/4]$ and $\mathfrak{I}\rho\in[2t-3/4,2t+3/4]$. Additionally, we know that $\zeta(\rho)=0$. This implies the stronger condition that $\Re \rho\in[3/4,1]$. Thus,

$$
\delta\leq 1+\delta-\Re \rho\qquad\text{and}\qquad
(1+\delta-\Re \rho)^2+(2t-\mathfrak{I}\rho)^2\leq 25/16+9/16=17/8.
$$

Which implies that

$$
0\lt \frac{8}{17}\,\delta
\leq\frac{1+\delta-\Re \rho}{(1+\delta-\Re \rho)^2+(2t-\mathfrak{I}\rho)^2}
=\Re \left(\frac{1}{1+\delta+2it-\rho}\right).\qquad\text{(4)}
$$

Note that, from Lemma [SumBoundI](sumboundi.md), we have

$$
\sum_{\rho\in\mathcal{Z}_{2t}}m_\zeta(\rho)\,
\Re \left(\frac{1}{1+\delta+2it-\rho}\right)
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta+2it)\right)
\leq\left|\frac{\zeta'}{\zeta}(1+\delta+2it)
-\sum_{\rho\in\mathcal{Z}_{2t}}\frac{m_\zeta(\rho)}{1+\delta+2it-\rho}\right|
\ll\log|2t|.
$$

Since $m_\zeta(\rho)\geq 0$ for all $\rho\in\mathcal{Z}_{2t}$, the inequality from Equation (4) tells us that by subtracting the sum from both sides we have

$$
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta+2it)\right)\ll\log|2t|.
$$

Noting that $\log|2t|=\log(2)+\log|t|\leq2\log|t|$ completes the proof.

## Lean

Formalized as [`ShiftTwoBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ShiftTwoBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
