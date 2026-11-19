---
declaration: lemma
origin: cited
lean: I1_prop_1, I3_prop_1, I2_prop_2, I3_prop_2, I3_prop_3_1, I3_prop_3_2
statement: formalized
proof: formalized
---

# basic grid structure

For each $-S\le k\le S$ and $1\le j\le 3$ the following holds.

If $j\neq 2$ and for some $x\in X$ and $y_1,y_2\in Y_k$ we have

$$
x\in I_j(y_1,k)\cap I_j(y_2,k),\qquad\text{(10)}
$$

then $y_1=y_2$.

If $j\neq 1$, then

$$
B(o, 4D^S-2D^k)\subset \bigcup_{y\in Y_k} I_j(y,k)\, .\qquad\text{(11)}
$$

We have for each $y\in Y_k$,

$$
B(y,\frac 12 D^k) \subset I_3(y,k)\subset
B(y,4D^k).\qquad\text{(12)}
$$

## Depends on

- [cover big ball](cover-big-ball.md)

## Proof

We prove these statements simultaneously by induction on the ordered set of pairs $(y,k)$. Let $-S\le k\le S$.

We first consider (10) for $j=1$. If $k=-S$, disjointedness of the sets $I_1(y,-S)$ follows by definition of $I_1$ and $Y_k$. If $k>-S$, assume $x$ is in $I_1(y_m,k)$ for $m=1,2$. Then, for $m=1,2$, there is $z_m\in Y_{k-1}\cap B(y_m,D^k)$ with $x\in I_3(z_m,k-1)$. Using (10) inductively for $j=3$, we conclude $z_1=z_2$. This implies that the balls $B(y_1, D^k)$ and $B(y_2, D^k)$ intersect. By construction of $Y_k$, this implies $y_1=y_2$. This proves (10) for $j=1$.

We next consider (10) for $j=3$. Assume $x$ is in $I_3(y_m,k)$ for $m=1,2$ and $y_m\in Y_k$. If $x$ is in $X_k$, then by definition [(9)](README.md), $x\in I_1(y_m,k)$ for $m=1,2$. As we have already shown (10) for $j=1$, we conclude $y_1=y_2$. This completes the proof in case $x\in X_k$, and we may assume $x$ is not in $X_k$. By definition [(9)](README.md), $x$ is not in $I_3(z,k)$ for any $z$ with $z\lt y_1$ or $z\lt y_2$. Hence, neither $y_1\lt y_2$ nor $y_2\lt y_1$, and by totality of the order of $Y_k$, we have $y_1=y_2$. This completes the proof of (10) for $j=3$.

We show (11) for $j=2$. In case $k=-S$, this follows from [cover big ball](cover-big-ball.md). Assume $k>-S$. Let $x$ be a point of $B(o, 4D^S-2D^k)$. By induction, there is $y'\in Y_{k-1}$ such that $x\in I_3(y',k-1)$. Using the inductive statement (12), we obtain $x\in B(y',4D^{k-1})$. As $D>4$, by applying the triangle inequality with the points, $o$, $x$, and $y'$, we obtain that $y'\in B(o, 4D^S-D^k)$. By [cover big ball](cover-big-ball.md), $y'$ is in $B(y,2D^k)$ for some $y\in Y_k$. It follows that $x\in I_2(y,k)$. This proves (11) for $j=2$.

We show (11) for $j=3$. Let $x\in B(o, 4D^S-2D^k)$. In case $x\in X_k$, then by definition of $X_k$ we have $x\in I_1(y,k)$ for some $y\in Y_k$ and thus $x\in I_3(y,k)$. We may thus assume $x\not\in X_k$. As we have already seen (11) for $j=2$, there is $y\in Y_k$ such that $x\in I_2(y,k)$. We may assume this $y$ is minimal with respect to the order in $Y_k$. Then $x\in I_3(y,k)$. This proves (11) for $j=3$.

Next, we show the first inclusion in (12). Let $x\in B(y,\frac 12 D^k)$. As $I_1(y,k)\subset I_3(y,k)$, it suffices to show $x\in I_1(y,k)$. If $k=-S$, this follows immediately from the assumption on $x$ and the definition of $I_1$. Assume $k>-S$. By the inductive statement (11) and $D>4$, there is a $y'\in Y_{k-1}$ such that $x\in I_3(y',k-1)$. By the inductive statement (12), we conclude $x\in B(y',4D^{k-1})$. By the triangle inequality with points $x$, $y$, $y'$, and $D\geq8$, we have $y'\in B(y,D^k)$. It follows by definition [(8)](README.md) that $I_3(y',k-1)\subset I_1(y,k)$, and thus $x\in I_3(y,k)$. This proves the first inclusion in (12).

We show the second inclusion in (12). Let $x\in I_3(y,k)$. As $I_1(y,k)\subset I_2(y,k)$ directly from the definition [(8)](README.md), it follows by definition [(9)](README.md) that $x\in I_2(y,k)$. By definition [(8)](README.md), there is $y'\in Y_{k-1}\cap B(y,2D^k)$ with $x\in I_3(y',k-1)$. By induction, $x\in B(y', 4D^{k-1})$. By the triangle inequality applied to the points $x,y',y$ and $D>4$, we conclude $x\in B(y,4D^k)$. This shows the second inclusion in (12) and completes the proof of the lemma.

## Lean

Formalized as [`I1_prop_1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I1_prop_1), [`I3_prop_1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I3_prop_1), [`I2_prop_2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I2_prop_2), [`I3_prop_2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I3_prop_2), [`I3_prop_3_1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I3_prop_3_1), [`I3_prop_3_2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/I3_prop_3_2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1430](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1430)
