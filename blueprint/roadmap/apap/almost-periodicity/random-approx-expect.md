---
declaration: lemma
origin: cited
lean: AlmostPeriodicity.lemma28
statement: formalized
proof: formalized
---

# random_approx_expect

Let $\epsilon>0$ and $m\geq 1$. Let $A\subseteq G$ and $f:G\to \mathbb{C}$. If $k\geq 64m\epsilon^{-2}$ then the set

$$
L = \{{\vec{a}}\in A^k : \|\tfrac{1}{k}\sum_{i=1}^k f(x-a_i)-\mu_A\ast f\|_{2m}
\le \epsilon \| f\|_{2m}\}.
$$

has size at least $\lvert A \rvert^k/2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Complex-valued Marcinkiewicz-Zygmund inequality](mzi-complex.md)

## Proof

Note that if $a\in A$ is chosen uniformly at random then, for any fixed $x\in G$,

$$
\mathbb{E} f(x-a_i)= \frac{1}{\left\lvert A\right\rvert}\sum_{a\in A}f(x-a)=\frac{1}{\left\lvert A\right\rvert}1_{A}\ast f(x)=\mu_A\ast f(x).
$$

Therefore, if we choose $a_1,\ldots,a_k\in A$ independently uniformly at random, for any fixed $x\in G$ and $1\leq i\leq k$, the random variable $f(x-a_i)-f\ast \mu_A(x)$ has mean zero. By the Marcinkiewicz-Zygmund inequality Lemma [Marcinkiewicz-Zygmund inequality](mzi.md), therefore,

$$
\begin{gathered}
\mathbb{E}\left\lvert  \frac{1}{k}\sum_i f(x-a_i)-f\ast \mu_A(x)\right\rvert^{2m} \leq \\(16m/k)^mk^{-1} \mathbb{E} \sum_i \left\lvert f(x-a_i)-f\ast \mu_A(x)\right\rvert^{2m}.
\end{gathered}
$$

We now sum both sides over all $x\in G$. By the triangle inequality, for any fixed $1\leq i\leq k$ and $a_i\in A$,

$$
\begin{aligned}
\sum_{x\in G} \left\lvert f(x-a_i)-f\ast \mu_A(x)\right\rvert^{2m}
&\leq 2^{2m-1}\sum_{x\in G}\left\lvert f(x-a_i)\right\rvert^{2m}+\sum_{x\in G}\left\lvert f\ast \mu_A(x)\right\rvert^{2m}\\
&\leq 2^{2m-1}\left( \lVert f\rVert_{2m}^{2m}+\lVert f\ast \mu_A\rVert_{2m}^{2m}\right).
\end{aligned}
$$

We note that $\lVert \mu_A\rVert_1=\frac{1}{\left\lvert A\right\rvert}\sum_{x\in A}1_{A}(x)=\left\lvert A\right\rvert/\left\lvert A\right\rvert=1$, and hence by Young's inequality, $\lVert f\ast \mu_A\rVert_{2m}\leq \lVert f\rVert_{2m}$, and so

$$
\sum_{x\in G} \left\lvert f(x-a_i)-f\ast \mu_A(x)\right\rvert^{2m}\leq 2^{2m}\lVert f\rVert_{2m}^{2m}.
$$

It follows that

$$
\mathbb{E}_{a_1,\ldots,a_k\in A}\lVert \frac{1}{k}\sum_i\tau_{a_i}f-f\ast \mu_A\rVert_{2m}^{2m}\leq
(64m/k)^m\lVert f\rVert_{2m}^{2m}.
$$

In particular, if $k\geq 64\epsilon^{-2}m$ then the right-hand side is at most $(\frac{\epsilon}{2}\lVert f\rVert_{2m})^{2m}$ as required.

## Lean

Formalized as [`AlmostPeriodicity.lemma28`](https://yaeldillies.github.io/apap/docs/find/#doc/AlmostPeriodicity.lemma28).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 54](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ap.tex#L54)
