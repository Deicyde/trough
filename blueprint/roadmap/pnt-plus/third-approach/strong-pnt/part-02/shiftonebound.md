---
declaration: theorem
origin: cited
lean: ShiftOneBound
statement: formalized
proof: formalized
---

# ShiftOneBound

There exists $C>0$ such that for all $\delta\in(0,1)$ and $t\in\mathbb{R}$ with $|t|\geq 2$; if $\zeta(\rho)=0$ with $\rho=\sigma+it$, then

$$
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)
\leq -\frac{1}{1+\delta-\sigma}+C\log|t|.
$$

## Depends on

- [ZeroWindow](zerowindow.md)

## Proof depends on

- [SumBoundI](sumboundi.md)

## Proof

Note that for $\rho'\in\mathcal{Z}_t$

$$
\begin{aligned}
\mathfrak{R}\left(\frac{1}{1+\delta+it-\rho'}\right)&=\mathfrak{R}\left(
\frac{1+\delta-it-\overline{\rho'}}{(1+\delta+it-\rho')(1+\delta-it-\overline{\rho'})}\right)
\\
&=\frac{\mathfrak{R}(1+\delta-it-\overline{\rho'})}{|1+\delta+it-\rho'|^2}
=\frac{1+\delta-\mathfrak{R}\rho'}{(1+\delta-\mathfrak{R}\rho')^2+(t-\mathfrak{I}\rho')^2}.
\end{aligned}
$$

Now since $\rho'\in\mathcal{Z}_t$, we have that $|\rho'-(3/2+it)|\leq 3/4$. So, we have $\mathfrak{R}\rho'\in[3/4,9/4]$ and $\mathfrak{I}\rho'\in[t-3/4,t+3/4]$. Additionally, we know that $\zeta(\rho')=0$. This implies the stronger condition that $\mathfrak{R}\rho'\in[3/4,1]$. Thus,

$$
\delta\leq 1+\delta-\mathfrak{R}\rho'
\qquad\text{and}\qquad
(1+\delta-\mathfrak{R}\rho')^2+(t-\mathfrak{I}\rho')^2\leq 25/16+9/16=17/8.
$$

Which implies that

$$
0\lt \frac{8}{17}\,\delta\leq\frac{1+\delta-\mathfrak{R}\rho'}{(1+\delta-\mathfrak{R}\rho')^2
+(t-\mathfrak{I}\rho')^2}=\mathfrak{R}\left(\frac{1}{1+\delta+it-\rho'}\right).\qquad\text{(5)}
$$

Note that, from Lemma [SumBoundI](sumboundi.md), we have

$$
\sum_{\rho'\in\mathcal{Z}_t}m_\zeta(\rho')\,\mathfrak{R}\left(
\frac{1}{1+\delta+it-\rho'}\right)-\mathfrak{R}\left(
\frac{\zeta'}{\zeta}(1+\delta+it)\right)\leq
\left|\frac{\zeta'}{\zeta}(1+\delta+it)
-\sum_{\rho'\in\mathcal{Z}_t}\frac{m_\zeta(\rho')}{1+\delta+it-\rho'}\right|\ll\log|t|.
$$

Now we proceed via cases. If $\rho\in\mathcal{Z}_t$, then $\mathcal{Z}_t=\rho\sqcup(\mathcal{Z}_t\setminus\rho)$ and the inequality from Equation (5) tells us that by subtracting the sum over all $\rho'\in\mathcal{Z}_t\setminus\{\rho\}$ from both sides we have

$$
\frac{m_\zeta(\rho)}{\mathfrak{R}(1+\delta+it-\rho)}
-\mathfrak{R}\left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)\ll\log|t|.
$$

But of course we have that $\mathfrak{R}(1+\delta+it-\rho)=1+\delta-\sigma$. So subtracting this term from both sides and recalling the implied constant we have

$$
-\mathfrak{R}\left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)\leq
-\frac{m_\zeta(\rho)}{1+\delta-\sigma}+C\log|t|.
$$

We have that $\sigma\leq 1$ since $\zeta$ is zero free on the right half plane $\sigma>1$. Thus, $0<1+\delta-\sigma$. Noting this in combination with the fact that $1\leq m_\zeta(\rho)$ gives us that

$$
-\mathfrak{R}\left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)\leq
-\frac{m_\zeta(\rho)}{1+\delta-\sigma}+C\log|t|\leq-\frac{1}{1+\delta-\rho}+(7+C)\log|t|.
$$

Now if $\rho\not\in\mathcal{Z}_t$, then $|\sigma-3/2|=|\rho-(3/2+it)|>3/4$ since $\zeta(\rho)=0$. Additionally, $\sigma\leq 1$ since $\zeta(\rho)=0$, thus $3/2-\sigma=|\sigma-3/2|>3/4$. So it follows that

$$
\frac{1}{1+\delta-\sigma}<4<7\log 2\leq 7\log|t|.
$$

Thus, by subtracting the sum over $\rho'\in\mathcal{Z}_t$ from both sides we have

$$
-\mathfrak{R}\left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)\leq
C\log|t|\leq-\frac{1}{1+\delta-\rho}+(7+C)\log|t|.
$$

## Lean

Formalized as [`ShiftOneBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ShiftOneBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
