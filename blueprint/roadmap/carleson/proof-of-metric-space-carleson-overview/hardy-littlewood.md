---
declaration: proposition
origin: cited
lean: measure_biUnion_le_lintegral, hasStrongType_maximalFunction, measurable_maximalFunction, laverage_le_globalMaximalFunction
statement: formalized
proof: formalized
---

# Hardy–Littlewood

Let $\mathcal{B}$ be a finite collection of balls in $X$. If for some $\lambda>0$ and some measurable function $u:X\to [0,\infty)$ we have

$$
\int_{B} u(x)\, d\mu(x)\ge \lambda \mu(B)\qquad\text{(49)}
$$

for each $B\in \mathcal{B}$, then

$$
\lambda \mu(\bigcup \mathcal{B}) \le 2^{2a}\int_X u(x)\, d\mu(x)\, .\qquad\text{(50)}
$$

For every measurable function $v$ and $1\le p_1\lt p_2$ we have

$$
\|M_{\mathcal{B},p_1} v\|_{p_2}\le 2^{2a}\frac{p_2}{p_2-p_1} \|v\|_{p_2}\, .\qquad\text{(51)}
$$

Moreover, given any measurable bounded function $w: X \to {\mathbb{C}}$ there exists a measurable function $Mw: X \to [0, \infty)$ such that the following (52) and (53) hold. For each ball $B \subset X$ and each $x \in B$

$$
\frac{1}{\mu(B)} \int_{B} |w(y)| \, \mathrm{d}\mu(y) \le Mw(x)\qquad\text{(52)}
$$

and for all $1 \le p_1 < p_2 \le \infty$

$$
\|M(w^{p_1})^{\frac{1}{p_1}}\|_{p_2} \le 2^{4a} \frac{p_2}{p_2-p_1}\|w\|_{p_2}\,.\qquad\text{(53)}
$$

## Depends on

- [layer cake representation](../proof-of-vitali-covering-and-hardy-littlewood/layer-cake-representation.md)

## Proof

*Proof of Hardy–Littlewood.* Let the collection $\mathcal{B}$ be given. We first show (50).

We recursively choose a finite sequence $B_i\in \mathcal{B}$ for $i\ge 0$ as follows. Assume $B_{i'}$ is already chosen for $0\le i'\lt i$. If there exists a ball $B_{i}\in \mathcal{B}$ so that $B_{i}$ is disjoint from all $B_{i'}$ with $0\le i'\lt i$, then choose such a ball $B_i=B(x_i,r_i)$ with maximal $r_i$.

If there is no such ball, stop the selection and set $i'':=i$.

By disjointedness of the chosen balls and since $0 \le u$, we have

$$
\sum_{0\le i\lt i''}\int_{B_i} u(x)\, d\mu(x) \le \int_X u(x)\, d\mu(x)\, .
$$

By (49), we conclude

$$
\lambda \sum_{0\le i\lt i''}\mu(B_i)
\le \int_X u(x)\, d\mu(x)\, .\qquad\text{(54)}
$$

Let $x\in \bigcup \mathcal{B}$. Choose a ball $B'=B(x',r')\in \mathcal{B}$ such that $x\in B'$. If $B'$ is one of the selected balls, then

$$
x\in \bigcup _{0\le i< i''}B_i\subset \bigcup _{0\le i< i''}B(x_i,3r_i)\, .\qquad\text{(55)}
$$

If $B'$ is not one of the selected balls, then as it is not selected at time $i''$, there is a selected ball $B_i$ with $B'\cap B_i\neq \emptyset$. Choose such $B_i$ with minimal index $i$. As $B'$ is therefore disjoint from all balls $B_{i'}$ with $i'\lt i$ and as it was not selected in place of $B_i$, we have $r_i\ge r'$.

Using a point $y$ in the intersection of $B_i$ and $B'$, we conclude by the triangle inequality

$$
\rho(x_i,x')\le \rho(x_i,y)+\rho(x',y)\le r_i+r'\le 2r_i \, .
$$

By the triangle inequality again, we further conclude

$$
\rho(x_i,x)\le \rho(x_i,x')+\rho(x',x)\le 2r_i+r'\le 3r_i \, .
$$

It follows that

$$
x\in \bigcup _{0\le i< i''}B(x_i,3r_i)\, .\qquad\text{(56)}
$$

With (55) and (56), we conclude

$$
\bigcup \mathcal{B}\subset
\bigcup _{0\le i< i''}B(x_i,3r_i)\, .
$$

With the doubling property [(5)](../introduction/README.md) applied twice, we conclude

$$
\mu(\bigcup{\mathcal{B}})
\le \sum _{0\le i< i''}\mu (B(x_i,3r_i))
\le 2^{2a}\sum _{0\le i< i''}\mu (B_i)\, .\qquad\text{(57)}
$$

With (54) and (57) we conclude (50).

We turn to the proof of (51). We first consider the case $p_1=1$ and recall $M_{\mathcal{B}}=M_{\mathcal{B},1}$. We write for the $p_2$-th power of left-hand side of (51) with [layer cake representation](../proof-of-vitali-covering-and-hardy-littlewood/layer-cake-representation.md) and a change of variables

$$
\|M_{\mathcal{B}}u(x)\|_{p_2}^{p_2}
=p_2\int _0^{\infty}
\lambda^{p_2-1} \mu(\{x: M_{\mathcal{B}}u(x)\ge \lambda\}) d\lambda\,
$$

$$
=2^{p_2} p_2\int _0^{\infty}
\lambda^{p_2-1} \mu(\{x: M_{\mathcal{B}}u(x)\ge 2\lambda\}) d\lambda\, .\qquad\text{(58)}
$$

Fix $\lambda\ge 0$ and let $x\in X$ satisfy $M_{\mathcal{B}}u(x)\ge 2\lambda$. By definition of $M_{\mathcal{B}}$, there is a ball $B'\in \mathcal{B}$ such that $x\in B'$ and

$$
\int_{B'} u(y)\, d\mu(y)\ge 2\lambda \mu({B'}) \, .\qquad\text{(59)}
$$

Define $u_\lambda(y):=0$ if $|u(y)|\lt \lambda$ and $u_\lambda(y):=u(y)$ if $|u(y)|\ge \lambda$. Then with (59)

$$
\int_{B'} u_\lambda (y)\, d\mu(y)
=\int_{B'} u (y)\, d\mu(y)-
\int_{B'} (u-u_\lambda) (y) d\mu(y)\,
$$

$$
\ge 2\lambda \mu({B'})-
\int_{B'} (u-u_\lambda) (y) d\mu(y)\, .
$$

As $(u-u_\lambda)(y)\le \lambda$ by definition, we can estimate the last display by

$$
\ge 2\lambda \mu({B'})-
\int_{B'} \lambda \, d\mu(y)
=\lambda \mu({B'})\, .
$$

Hence $x$ is contained in $\bigcup(\mathcal{B}_\lambda)$, where $\mathcal{B}_\lambda$ is the collection of balls $B''$ in $\mathcal{B}$ such that

$$
\int_{B''} u_\lambda (y)\, d\mu(y)\ge \lambda \mu(B'')\, .
$$

We have thus seen

$$
\{x: M_{\mathcal{B}}u(x)\ge 2\lambda\}\subset
\bigcup \mathcal{B}_\lambda
\, .
$$

Applying (50) to the collection $\mathcal{B}_\lambda$ gives

$$
\lambda \mu(\{x: M_{\mathcal{B}}u(x)\ge 2\lambda\})\le
2^{2a}
\int u_\lambda (x)\, dx\, .
$$

With [layer cake representation](../proof-of-vitali-covering-and-hardy-littlewood/layer-cake-representation.md),

$$
\lambda \mu(\{x: M_{\mathcal{B}}u(x)\ge 2\lambda\})\le
2^{2a}
\int_0^\infty \mu (\{x: |u_\lambda (x)|\ge \lambda'\})\, d\lambda'\, .\qquad\text{(60)}
$$

By definition of $u_\lambda$, making a case distinction between $\lambda\ge \lambda'$ and $\lambda \lt \lambda'$, we see that

$$
\mu (\{x: |u_\lambda (x)|\ge \lambda'\})
\le
\mu (\{x: |u (x)|\ge \max(\lambda,\lambda')\})\, .\qquad\text{(61)}
$$

We obtain with (58), (60), and (61)

$$
\|M_{\mathcal{B}}u(x)\|_{p_2}^{p_2}
$$

$$
\le 2^{p_2+2a} p_2
\int_0^\infty \lambda^{p_2-2}
\int_0^\infty
\mu (\{x: |u (x)|\ge \max(\lambda,\lambda')\})
\, d\lambda'd\lambda\, .
$$

We split the integral into $\lambda\ge \lambda'$ and $\lambda\lt \lambda'$ and resolve the maximum correspondingly. We have for $\lambda\ge \lambda'$ with [layer cake representation](../proof-of-vitali-covering-and-hardy-littlewood/layer-cake-representation.md)

$$
\int_0^\infty \lambda^{p_2-2}
\int_0^\lambda
\mu (\{x: |u (x)|\ge \lambda\})
\, d\lambda'd\lambda
$$

$$
=\int_0^\infty \lambda^{p_2-1}
\mu (\{x: |u (x)|\ge \lambda\})
d\lambda.
$$

$$
=p_2^{-1} \|u\|_{p_2}^{p_2}\, .\qquad\text{(62)}
$$

We have for $\lambda< \lambda'$ with Fubini and [layer cake representation](../proof-of-vitali-covering-and-hardy-littlewood/layer-cake-representation.md)

$$
\int_0^\infty \lambda^{p_2-2}
\int_\lambda^\infty
\mu (\{x: |u(x)|\ge \lambda'\})
\, d\lambda'd\lambda.
$$

$$
=\int_0^\infty \int_0^{\lambda'}\lambda^{p_2-2}
\mu (\{x: |u (x)|\ge \lambda'\})
d\lambda d\lambda'.
$$

$$
=(p_2-1)^{-1}\int_0^\infty (\lambda')^{p_2-1}
\mu (\{x: |u(x)|\ge \lambda'\})
d\lambda'.
$$

$$
=(p_2-1)^{-1} p_2^{-1}\|u\|_{p_2}^{p_2}\, .\qquad\text{(63)}
$$

Adding the two estimates (62) and (63) gives

$$
\|M_{\mathcal{B}}u(x)\|_{p_2}^{p_2}
\le 2^{p_2+2a} (1+(p_2-1)^{-1})\|u\|_{p_2}^{p_2}
= 2^{p_2+2a} p_2(p_2-1)^{-1}\|u\|_{p_2}^{p_2}
\, .
$$

With $a\ge 1$ and $p_2>1$, taking the $p_2$-th root, we obtain (51). We turn to the case of general $1\le p_1\lt p_2$. We have

$$
M_{\mathcal{B},p_1}u=(M_{\mathcal{B}} (|u|^{p_1}))^{\frac 1{p_1}}\, .
$$

Applying the special case of (51) for $M_{\mathcal{B}}$ gives

$$
\|M_{\mathcal{B},p_1}u\|_{p_2}=
\|M_{\mathcal{B}} (|u|^{p_1})\|_{p_2/p_1}^{\frac 1{p_1}}
$$

$$
\le 2^{2a} (p_2/p_1) (p_2/p_1-1)^{-1}
\|(|u|^{p_1})\|_{p_2/p_1}^{\frac 1{p_1}}
=2^{2a} p_2(p_2-p_1)^{-1}\|u\|_{p_2}\, .
$$

This proves (51) in general.

Now we construct the operator $M$ satisfying (52) and (53). For each $k \in \mathbb{Z}$ we choose a countable set $C(2^k)$ as in [covering separable space](../proof-of-vitali-covering-and-hardy-littlewood/covering-separable-space.md).

Define

$$
\mathcal{B}_\infty = \{B(c, 2^k) \ : \ c \in C(2^k), k \in \mathbb{Z}\}\,.
$$

By [covering separable space](../proof-of-vitali-covering-and-hardy-littlewood/covering-separable-space.md), this is a countable collection of balls. We choose an enumeration $\mathcal{B}_\infty = \{B_1, \dotsc\}$ and define

$$
\mathcal{B}_n = \{B_1, \dotsc, B_n\}\,.
$$

We define

$$
Mw := 2^{2a}\sup_{n \in \mathbb{N}} M_{\mathcal{B}_n}w\,.
$$

This function is measurable for each measurable $w$, since it is a countable supremum of measurable functions. Estimate (53) follows immediately from (51) and the monotone convergence theorem.

It remains to show (52). Let $B = B(x, r) \subset X$. Let $k$ be the smallest integer such that $2^k \ge r$, in particular we have $2^k < 2r$. By definition of $C(2^k)$, there exists $c \in C(2^k)$ with $x \in B(c, 2^k)$. By the triangle inequality, we have $B(c, 2^k) \subset B(x, 4r)$, and hence by the doubling property [(5)](../introduction/README.md)

$$
\mu(B(c, 2^k)) \le 2^{2a} \mu(B(x,r))\,.
$$

It follows that for each $z \in B(x,r)$

$$
\begin{aligned}
\frac{1}{\mu(B(x,r))}\int_{B(x,r)} |w(y)| \, \mathrm{d}\mu(y) &\le \frac{2^{2a}}{\mu(B(c,2^k))}\int_{B(c,2^k)} |w(y)| \, \mathrm{d}\mu(y) \\
&\le Mw(z)\,.
\end{aligned}
$$

This completes the proof.

## Lean

Formalized as [`measure_biUnion_le_lintegral`](https://fpvandoorn.github.io/carleson/docs/find/#doc/measure_biUnion_le_lintegral), [`hasStrongType_maximalFunction`](https://fpvandoorn.github.io/carleson/docs/find/#doc/hasStrongType_maximalFunction), [`measurable_maximalFunction`](https://fpvandoorn.github.io/carleson/docs/find/#doc/measurable_maximalFunction), [`laverage_le_globalMaximalFunction`](https://fpvandoorn.github.io/carleson/docs/find/#doc/laverage_le_globalMaximalFunction).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 763](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L763)
