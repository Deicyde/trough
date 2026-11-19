---
declaration: theorem
origin: cited
lean: AlmostPeriodicity.linfty_almost_periodicity_boosted
statement: formalized
proof: formalized
---

# linfty_ap_boosted

Let $\epsilon\in (0,1]$ and $k\geq 1$. Let $K\geq 2$ and $A,S\subseteq G$ with $\lvert A+S\rvert\leq K\lvert A\rvert$. Let $B,C\subseteq G$. Let $\eta=\min(1,\lvert C\rvert/\lvert B\rvert)$. There exists $T\subseteq G$ such that

$$
\lvert T\rvert \geq K^{-4096\lceil \mathcal{L}{\eta}\rceil k^2\epsilon^{-2}}\lvert S\rvert
$$

such that

$$
\| \mu_T^{(k)}\ast \mu_A\ast 1_B\ast \mu_C-\mu_A\ast 1_B\ast \mu_C\|_{\infty}\leq \epsilon.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$L_\infty$ almost periodicity](linfty-ap.md)

## Proof

Let $T$ be as in Theorem [$L_\infty$ almost periodicity](linfty-ap.md) with $\epsilon$ replaced by $\epsilon/k$. Note that, for any $x\in G$,

$$
\mu_T^{(k)}\ast \mu_A\ast 1_B\ast \mu_C(x)=\frac{1}{\lvert T\rvert^k}\sum_{t_1,\ldots,t_k\in T}\tau_{t_1+\cdots+t_k}\mu_A\ast 1_B\ast \mu_C(x).
$$

It therefore suffices (by the triangle inequality) to show, for any fixed $x\in G$ and $t_1,\ldots,t_k\in T$, that with $F=\mu_A\ast 1_B\ast \mu_C$, we have

$$
\lvert \tau_{t_1+\cdots+t_k}F(x)-F(x)\rvert \leq \epsilon.
$$

This follows by the triangle inequality applied $k$ times if we knew that, for $1\leq l\leq k$,

$$
\lvert \tau_{t_1+\cdots+t_l}F(x)-\tau_{t_1+\cdots+t_{l-1}}F(x)\rvert \leq \epsilon/k.
$$

We can write the left-hand side as

$$
\lvert \tau_{t_1+\cdots+t_l}F(x)-\tau_{t_1+\cdots+t_{l-1}}F(x)\rvert=\lvert \tau_{t_l}F(x-t_1-\cdots-t-{l-1})-F(x-t_1-\cdots-t-{l-1})\rvert.
$$

The right-hand side is at most

$$
\| \tau_{t_l}F-F\|_\infty
$$

and we are done by choice of $T$.

## Lean

Formalized as [`AlmostPeriodicity.linfty_almost_periodicity_boosted`](https://yaeldillies.github.io/apap/docs/find/#doc/AlmostPeriodicity.linfty_almost_periodicity_boosted).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 175](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ap.tex#L175)
