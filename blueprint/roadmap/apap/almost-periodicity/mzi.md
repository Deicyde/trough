---
declaration: lemma
origin: cited
lean: Real.marcinkiewicz_zygmund', Real.marcinkiewicz_zygmund
statement: formalized
proof: formalized
---

# Marcinkiewicz-Zygmund inequality

Let $m\geq 1$. If $f:G\to\mathbb{R}$ is such that $\mathbb{E}_x f(x)=0$ and $\left\lvert f(x)\right\rvert\leq 2$ for all $x$ then

$$
\mathbb{E}_{x_1,\ldots,x_n} \left\lvert \sum_{i=1}^n f(x_i)\right\rvert^{2m} \leq (4mn)^{m}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $S$ be the left-hand side. Since $0=\mathbb{E}_y f(y)$ we have, by the triangle inequality, and Hölder's inequality,

$$
\begin{aligned}
S
& = \mathbb{E}_{x_1, \dots, x_n}\left\lvert \sum_i f(x_i) - \mathbb{E}_{y_i} f(y_i)\right\rvert^{2m} \\
& = \mathbb{E}_{x_1, \dots, x_n} \left\lvert\mathbb{E}_{y_i}\left( \sum_i f(x_i) - f(y_i)\right)\right\rvert^{2m} \\
& \le \mathbb{E}_{x_1,\dots,y_n} \left\lvert \sum_i f(x_i) - f(y_i)\right\rvert^{2m}
\end{aligned}
$$

Changing the role of $x_i$ and $y_i$ makes no difference here, but multiplies the $i$ summand by $\{-1,+1\}$, and therefore for any $\epsilon_i\in\{-1,+1\}$,

$$
S \leq\mathbb{E}_{x_1,\ldots,y_n}\left\lvert \sum_i \epsilon_i(f(x_i)-f(y_i))\right\rvert^{2m}.
$$

In particular, if we sample $\epsilon_i\in\{-1,+1\}$ uniformly at random, then

$$
S \leq\mathbb{E}_{\epsilon_i} \mathbb{E}_{x_1,\ldots,y_n}\left\lvert \sum_i \epsilon_i(f(x_i)-f(y_i))\right\rvert^{2m}.
$$

We now change the order of expectation and consider the expectation over just $\epsilon_i$, viewing the $f(x_i)-f(y_i)=z_i$, say, as fixed quantities. For any $z_i$ we can expand $\mathbb{E}_{\epsilon_i} \lvert \sum_i \epsilon_iz_i\rvert^{2m}$ and then bound it from above, using the triangle inequality and $\left\lvert z_i\right\rvert\leq 4$, by

$$
4^{2m}\sum_{k_1+\cdots+k_n=2m}\binom{2m}{k_1,\ldots,k_n}\left\lvert \mathbb{E}\epsilon_1^{k_1}\cdots \epsilon_n^{k_n}\right\rvert.
$$

The inner expectation vanishes unless each $k_i$ is even, when it is trivially one. Therefore the above quantity is exactly

$$
\sum_{l_1+\cdots+l_n=m}\binom{2m}{2l_1,\ldots,2l_n}\leq m^mn^m,
$$

since for any $l_1+\cdots+l_n=m$,

$$
\binom{2m}{2l_1,\ldots,2l_n}\leq m^m\binom{m}{l_1,\ldots,l_n}.
$$

This can be seen, for example, by writing both sides out using factorials, yielding

$$
\frac{(2m)!}{(2l_1)!\cdots (2l_n)!}\leq \frac{(2m)!}{2^mm!}\frac{m!}{l_1!\cdots l_n!}\leq m^m\frac{m!}{l_1!\cdots l_n!}.
$$

## Lean

Formalized as [`Real.marcinkiewicz_zygmund'`](https://yaeldillies.github.io/apap/docs/find/#doc/Real.marcinkiewicz_zygmund'), [`Real.marcinkiewicz_zygmund`](https://yaeldillies.github.io/apap/docs/find/#doc/Real.marcinkiewicz_zygmund).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 5](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ap.tex#L5)
