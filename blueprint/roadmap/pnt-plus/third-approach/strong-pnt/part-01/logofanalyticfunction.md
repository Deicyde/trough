---
declaration: theorem
origin: cited
lean: LogOfAnalyticFunction
statement: formalized
proof: formalized
---

# LogOfAnalyticFunction

Let $0\lt r\lt R$. Let $B:\overline{\mathbb{D}_{R}}\to\mathbb{C}$ be analytic on neighborhoods of points in $\overline{\mathbb{D}_{R}}$ with $B(z)\neq 0$ for all $z\in\overline{\mathbb{D}_{R}}$.Then there exists $J_B:\mathbb{D}_R\to\mathbb{C}$ that is analytic on neighborhoods of points in $\mathbb{D}_R$ such that

- $J_B(0)=0$
- $J_B'(z)=B'(z)/B(z)$ for all $z\in\overline{\mathbb{D}_r}$
- $\log|B(z)|-\log|B(0)|=\mathfrak{R}J_B(z)$ for all $z\in\mathbb{D}_R$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We let $J_B(z)=I_{B'/B}(z)$. Then clearly, $J_B(0)=0$. Now note that

$$
\begin{aligned}
I_{B'/B}(z)=z\int_0^1(B'/B)(tz)\,dt=\int_0^z(B'/B)(u)\,du.
\end{aligned}
$$

Thus by the fundamental theorem of calculus we have that $J_B'(z)=B'(z)/B(z)$. Now let $H(z)=\exp(J_B(z))/B(z)$ and note that

$$
H'(z)=(B(z)\,J_B'(z)-B'(z))\left(\frac{\exp(J_B(z))}{(B(z))^2}\right).
$$

Thus, $H$ is constant since we know that $B(z)\,J_B'(z)-B'(z)=0$ from $J_B'(z)=B'(z)/B(z)$. So since $H(0)=\exp(J_B(0))/B(0)=1/B(0)$ we know $H(z)=1/B(0)$ for all $z$. So we have,

$$
\frac{1}{B(0)}=\frac{\exp(J_B(z))}{B(z)}\implies\left|\frac{B(z)}{B(0)}\right|
=\exp(\mathfrak{R}J_B(z)).
$$

Taking the logarithm of both sides completes the proof.

## Lean

Formalized as [`LogOfAnalyticFunction`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogOfAnalyticFunction).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
