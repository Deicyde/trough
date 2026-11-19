---
declaration: lemma
origin: cited
lean: support_holderApprox_subset, enorm_holderApprox_sub_le, iLipENorm_holderApprox_le
statement: formalized
proof: formalized
---

# Lipschitz Holder approximation

Let $z\in X$ and $R>0$. Let $\varphi: X \to \mathbb{C}$ be a function supported in the ball $B:=B(z,R)$ with finite norm $\|\varphi\|_{C^\tau(B(z, 2R))}$. Let $0\lt t \leq 1$. There exists a function $\tilde \varphi : X \to \mathbb{C}$, supported in $B(z,2R)$, such that for every $x\in X$

$$
|\varphi(x) - \tilde \varphi(x)| \leq (t/2)^{\tau} \|\varphi\|_{C^\tau(B(z,2R))}\qquad\text{(1)}
$$

and

$$
\|\tilde \varphi\|_{\operatorname{\operatorname{Lip}}(B(z,2R))} \leq 2^{4a}t^{-1-a} \|\varphi\|_{C^{\tau}(B(z,2R))}\, .\qquad\text{(2)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Define for $x,y\in X$ the Lipschitz and thus measurable function

$$
L(x,y) := \max\{0, 1 - \frac{\rho(x,y)}{tR}\}\, .
$$

We have that $L(x,y)\neq 0$ implies

$$
y\in B(x, tR)\, .\qquad\text{(3)}
$$

We have for $y\in B(x, 2^{-1}tR)$ that

$$
|L(x,y)|\ge 2^{-1} \ .\qquad\text{(4)}
$$

Hence

$$
\int L(x,y) \, \mathrm{d}\mu(y)\ge 2^{-1}\mu(B(x, 2^{-1}tR))\, .
$$

Let $n$ be the smallest integer so that

$$
2^n t\ge 1\, .\qquad\text{(5)}
$$

Iterating $n+2$ times the doubling condition [(5)](../introduction/README.md), we obtain

$$
\int L(x,y) \, \mathrm{d}\mu(y)\ge 2^{-1-a(n+2)}\mu(B(x, 2R))\, .\qquad\text{(6)}
$$

Now define

$$
\tilde \varphi(x) := \left(\int L(x,y) \, \mathrm{d}\mu(y)\right)^{-1}\int L(x,y) \varphi(y) \, \mathrm{d}\mu(y)\, .
$$

Using that $\varphi$ is supported in $B(z,R)$ and (3), we have that $\tilde{\varphi}$ is supported in $B(z,2R)$.

We prove (1). For any $x\in X$, using that $L$ is nonnegative,

$$
\left(\int L(x,y) \, \mathrm{d}\mu(y)\right)
|\varphi(x) - \tilde \varphi(x)|\qquad\text{(7)}
$$

$$
= \left| \int L(x,y)(\varphi(x) - \varphi(y)) \, \mathrm{d}\mu(y)\right|\, .\qquad\text{(8)}
$$

Using (3), we estimate the last display by

$$
\le \int_{B(x, tR)} L(x,y)|\varphi(x) - \varphi(y)| \, \mathrm{d}\mu(y)\, .\qquad\text{(9)}
$$

We claim that in this integral, $|\varphi(x) - \varphi(y)|\le \rho(x,y)^\tau \|\varphi\|_{C^\tau(B(z, 2R))}(2R)^{-\tau}$. Indeed, if $x$ or $y$ does not belong to $B(z, 2R)$, then the other point is not in $B(z,R)$ as $\rho(x,y)\le tR \le R$. Therefore, $\varphi(x)=\varphi(y)=0$ since $\varphi$ is supported in $B (z, R)$. Otherwise, both points are in $B(z, 2R)$, and the inequality follows from the definition of $\|\varphi\|_{C^\tau(B(z, 2R))}$.

Therefore, we can estimate the last display further by

$$
\le \left(\int_{B(x, tR)} L(x,y)
\rho(x,y)^\tau \, \mathrm{d}\mu(y) \right)\|\varphi\|_{C^\tau(B(z, 2R))}(2R)^{-\tau}\, .\qquad\text{(10)}
$$

Using the condition on the domain of integration to estimate $\rho(x,y)$ by $tR$ and then expanding the domain by positivity of the integrand, we estimate this further by

$$
\le \left(\int L(x,y) \, \mathrm{d}\mu(y)\right)
\|\varphi\|_{C^\tau(B(z, 2R))} (t/2)^{\tau} \, .\qquad\text{(11)}
$$

Dividing the string of inequalities from (7) to (11) by the positive integral of $L$ proves (1).

We turn to (2). For every $x\in X$, we have

$$
\left|\int L(x,y) \, \mathrm{d}\mu(y)\right||\tilde{\varphi}(x)|
=\left|\int L(x,y) {\varphi}(y)\, \mathrm{d}\mu(y)\right|
$$

$$
\le \left|\int L(x,y) \, \mathrm{d}\mu(y)\right| \sup_{x'\in X}
|{\varphi}(x')|\ .
$$

As $\varphi$ is supported on $B$, dividing by the integral of $L$, we obtain

$$
|\tilde{\varphi}(x)|\le \sup_{x'\in B}
|{\varphi}(x')|\le \|\varphi\|_{C^\tau(B(z, 2R))}\ .\qquad\text{(12)}
$$

If $\rho(x,x')\ge R$, then we have by the triangle inequality

$$
R\frac{|\tilde{\varphi}(x') - \tilde \varphi(x)|}{\rho(x,x')} \le
2\sup_{x''\in X} |\tilde{\varphi}(x'')|\le 2\|\varphi\|_{C^\tau(B(z, 2R))}\, .\qquad\text{(13)}
$$

Now assume $\rho(x,x')< R$. For $y\in X$ we have by the triangle inequality and a two fold case distinction for the maximum in the definition of $L$,

$$
|L(x,y) - L(x',y)| \le \frac{\rho(x,x')}{tR}.\qquad\text{(14)}
$$

We compute with (14), first adding and subtracting a term in the integral,

$$
\left(\int L(x,y) \, \mathrm{d}\mu(y)\right)
|\tilde{\varphi}(x') - \tilde \varphi(x)|=
$$

$$
\left|\int L(x,y) \tilde{\varphi}(x')
-L(x,y) \tilde{\varphi}(x)
+L(x',y) \tilde{\varphi}(x')-
L(x',y) \tilde{\varphi}(x')
\, \mathrm{d}\mu(y)\right|\,.
$$

Grouping the second and third and the first and fourth term, we obtain using the definition of $\tilde \varphi$ and Fubini,

$$
\le \left| \int (L(x',y)-L(x,y)) \varphi(y) \, \mathrm{d}\mu(y)\right|\qquad\text{(15)}
$$

$$
+ \left| \int L(x,y) \, \mathrm{d}\mu(y)-\int L(x',y) \, \mathrm{d}\mu(y)\right||\tilde{\varphi}(x')|\qquad\text{(16)}
$$

$$
\le 2 \int |L(x,y) -L(x',y)| \, \mathrm{d}\mu(y)
\|\varphi\|_{C^\tau(B(z, 2R))}\, ,\qquad\text{(17)}
$$

where in the last inequality we have used (12). Using further (14) and the support of $L$, we estimate the last display by

$$
\le 2 \frac{\rho(x,x')} {tR}\mu(B(x,tR)\cup B(x',tR))
\|\varphi\|_{C^\tau(B(z, 2R))}\, .\qquad\text{(18)}
$$

Using $\rho(x,x')\lt R$ and the triangle inequality, we estimate the last display by

$$
\le 2
\frac{\rho(x,x')} {tR}
\mu(B(x,2R))
\|\varphi\|_{C^\tau(B(z, 2R))}\, .\qquad\text{(19)}
$$

Dividing by the integral over $L$ and using (6) and (5), we obtain

$$
\frac {R |\tilde{\varphi}(x') - \tilde \varphi(x)|}{\rho(x,x')}
\le 2^{2+a(n+2)}t^{-1}\|\varphi\|_{C^\tau(B(z, 2R))} \le
2^{2+3a} t^{-1-a} \|\varphi\|_{C^\tau(B(z, 2R))}\, .\qquad\text{(20)}
$$

Combining (13) and (20) using $a\ge 4$ and $t\le 1$ and adding (12) proves (2) and completes the proof of Lipschitz Holder approximation.

## Lean

Formalized as [`support_holderApprox_subset`](https://fpvandoorn.github.io/carleson/docs/find/#doc/support_holderApprox_subset), [`enorm_holderApprox_sub_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_holderApprox_sub_le), [`iLipENorm_holderApprox_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/iLipENorm_holderApprox_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6460](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6460)
