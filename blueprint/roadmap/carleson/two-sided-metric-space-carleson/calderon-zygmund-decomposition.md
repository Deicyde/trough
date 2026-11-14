---
declaration: lemma
origin: cited
lean: encard_czBall3_le, tsum_czRemainder', aemeasurable_czApproximation, czApproximation_add_czRemainder, enorm_czApproximation_le, enorm_czApproximation_le_infinite, eLpNorm_czApproximation_le, support_czRemainder'_subset, integral_czRemainder', integral_czRemainder, eLpNorm_czRemainder'_le, eLpNorm_czRemainder_le, tsum_volume_czBall3_le, volume_univ_le, tsum_eLpNorm_czRemainder'_le, tsum_eLpNorm_czRemainder_le
statement: formalized
proof: formalized
---

# Calderon Zygmund decomposition

Let $f$ be a bounded, a.e. measurable function supported on a set of finite measure and let $\alpha>\frac{1}{\mu(X)}\int |f|\,d\mu$. Then there exists a bounded a.e. measurable function $g$ supported on a set of finite measure, a countable family of balls $B_{3,j}$ (where we allow $B_{3,1} = X$ in the special case that $\mu(X)\lt \infty$)

such that each $x\in X$ is contained in at most $2^{6a}$ of the $B_{3,j}$, and a countable family of a.e. measurable functions $\{b_j\}_{j\in J}$ such that for all $x \in X$

$$
f(x)= g(x) + \sum_{j} b_j(x)\qquad\text{(50)}
$$

and such that the following holds. For almost every $x\in X$,

$$
|g(x)|\leq 2^{3a} \alpha\,.\qquad\text{(51)}
$$

We have

$$
\int |g(y)|\, d\mu(y)\leq \int |f(y)|\, d\mu(y).\qquad\text{(52)}
$$

For every $j$

$$
\operatorname{supp} b_j \subset B_{3,j}\,.\qquad\text{(53)}
$$

For every $j$

$$
\int_{B_{3,j}} b_j(x)\, d\mu(x)=0,\qquad\text{(54)}
$$

and

$$
\int_{B_{3,j}} |b_j(x)|\, d\mu(x) \leq 2^{2a+1} \alpha \mu(B_{3,j}).\qquad\text{(55)}
$$

We have

$$
\sum_j \mu(B_{3,j})\leq \frac{2^{4a}}{\alpha}\int |f(y)|\, d\mu(y)\qquad\text{(56)}
$$

and

$$
\sum_{j}\int_{B_{3,j}} |b_j(y)|\, d\mu(y)\leq 2 \int |f(y)|\, d\mu(y)\,.\qquad\text{(57)}
$$

## Depends on

- [Ball covering](ball-covering.md)
- [Lebesgue differentiation](lebesgue-differentiation.md)
- [Maximal theorem](maximal-theorem.md)

## Proof

Let $E_\alpha:=\{x\in X: Mf(x)>\alpha\}$. Then $E_\alpha$ is open. Assume first that $E_\alpha \ne X$. We apply [Ball covering](ball-covering.md) with $O=E_\alpha$ to obtain the family $B_j, j\in J,$. Without loss of generality, we can assume $J={\mathbb{N}}$. Define inductively

$$
Q_j := B_{3,j} \setminus \left(\bigcup_{i\lt j} Q_i \cup \bigcup_{i>j} B_i \right).
$$

Then $B_j\subset Q_j\subset B_{3,j}$, the $Q_j$ are pairwise disjoint and $\bigcup_j Q_j = E_\alpha$. Define

$$
g(x):=\begin{cases}
f(x), & x\in X\setminus E_\alpha,\\
\frac{1}{\mu(Q_j)}\int_{Q_j} f(y)\, d\mu(y), &x\in Q_j,
\end{cases}\qquad\text{(58)}
$$

and, for each $j$,

$$
b_j(x):= \mathbf{1}_{Q_j}(x) \left(f(x)-\frac{1}{\mu(Q_j)}\int_{Q_j} f(y)\, d\mu(y) \right).
$$

Then (50), (53) and (54) are true by construction. Boundedness of $g$ is immediate from the definition, as is the fact that $\operatorname{\operatorname{supp}} g$ is contained within $\operatorname{\operatorname{supp}} f \cup \bigcup_j Q_j$. Now the fact that $\operatorname{\operatorname{supp}} g$ has finite measure follows from $\bigcup_j Q_j = E_\alpha$ and [(53)](../proof-of-metric-space-carleson-overview/hardy-littlewood.md).

For (51), we first do the case $x\in X\setminus E_\alpha$. By definition of $Mf$,

$$
\frac{1}{\mu(B)}\int_B |f(y)|\,d\mu(y) \le \alpha
$$

for every ball $B\subset X$ with $x\in B$. It follows by [Lebesgue differentiation](lebesgue-differentiation.md) that for almost every $x\in X\setminus E_\alpha$, $|f(x)|\le \alpha$. In the case $x\in E_\alpha$, there exists some $j\in J$ with $x\in Q_j$ and we have that

$$
\frac{1}{\mu(B_{7,j})} \int_{B_{7,j}} |f(y)| \,d\mu(y) \le \alpha\qquad\text{(59)}
$$

because $B_{7,j}\cap (X\setminus E_\alpha) \ne \emptyset$. We get

$$
|g(x)| \le \frac{1}{\mu(Q_j)}\int_{Q_j} |f(y)|\, d\mu(y) \le \frac{1}{\mu(B_j)}\int_{B_{7,j}} |f(y)| \, d\mu(y) \le 2^{3a}\alpha .
$$

To prove (52), we estimate

$$
\begin{aligned}
\int |g(z)|\, d\mu(z) &\le \int_{X\setminus E_\alpha} |f(z)|\, d\mu(z) + \sum_{j} \int_{Q_j}\frac{1}{\mu(Q_j)}\int_{Q_j}|f(y)|\, d\mu(y)\,d\mu(z) \\
&= \int |f(z)|\,d\mu(z).
\end{aligned}
$$

Using the triangle inequality, we have that

$$
\begin{aligned}
\int_{B_{3,j}} |b_j(y)|\, dy &\le \int_{Q_j} |f(y)|\, d\mu(y) + \int_{Q_j} \frac{1}{\mu(Q_j)}\int_{Q_j} |f(x)|\, d\mu(x)\, d\mu(y)\qquad\text{(60)}\\
&= 2 \int_{Q_j} |f(y)|\, dy.
\end{aligned}
$$

With (59), we estimate further

$$
\le 2 \int_{B_{7,j}} |f(y)|\, dy \le 2\mu(B_{7,j})\alpha \le 2^{2a+1} \alpha \mu(B_{3,j})
$$

to obtain (55). Further, summing up (60) in $j$ yields (57). At last, we estimate with [Maximal theorem](maximal-theorem.md)

$$
\sum_j \mu(B_{3,j}) \le 2^{2a} \sum_j \mu(B_j) \le 2^{2a} \mu(E_\alpha) \le \frac{2^{4a}}{\alpha}\int |f(y)|\, d\mu(y),
$$

proving (56).

Assume now that $E_\alpha = X$. It follows from [Maximal theorem](maximal-theorem.md) that then $\mu(X)\lt \infty$. Define

$$
g := \frac{1}{\mu(X)} \int |f(y)|\,d\mu(y)
$$

and

$$
b_1 := f - g.
$$

Then $f = g + b_1$ and $\operatorname{\operatorname{supp}} b_1 \subset B_{3,1}:=X$ and (50), (52), (53), (54) all hold immediately. By assumption, $\alpha>\frac{1}{\mu(X)}\int |f|\,d\mu = g$, so (51) holds. We also have, using the definitions and the same assumption,

$$
\int |b_1(y)|\, d\mu(y) \le 2 \int |f(y)|\,d\mu(y) \le 2\alpha\mu(X),
$$

which verifies both (57) and (55). Finally, by [Maximal theorem](maximal-theorem.md),

$$
\mu(X) \le \frac{2^{2a}}{\alpha} \int |f(y)|\,d\mu(y),
$$

which shows (56).

## Lean

Formalized as [`encard_czBall3_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/encard_czBall3_le), [`tsum_czRemainder'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tsum_czRemainder'), [`aemeasurable_czApproximation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/aemeasurable_czApproximation), [`czApproximation_add_czRemainder`](https://fpvandoorn.github.io/carleson/docs/find/#doc/czApproximation_add_czRemainder), [`enorm_czApproximation_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_czApproximation_le), [`enorm_czApproximation_le_infinite`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_czApproximation_le_infinite), [`eLpNorm_czApproximation_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/eLpNorm_czApproximation_le), [`support_czRemainder'_subset`](https://fpvandoorn.github.io/carleson/docs/find/#doc/support_czRemainder'_subset), [`integral_czRemainder'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/integral_czRemainder'), [`integral_czRemainder`](https://fpvandoorn.github.io/carleson/docs/find/#doc/integral_czRemainder), [`eLpNorm_czRemainder'_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/eLpNorm_czRemainder'_le), [`eLpNorm_czRemainder_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/eLpNorm_czRemainder_le), [`tsum_volume_czBall3_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tsum_volume_czBall3_le), [`volume_univ_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/volume_univ_le), [`tsum_eLpNorm_czRemainder'_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tsum_eLpNorm_czRemainder'_le), [`tsum_eLpNorm_czRemainder_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tsum_eLpNorm_czRemainder_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7696](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7696)
