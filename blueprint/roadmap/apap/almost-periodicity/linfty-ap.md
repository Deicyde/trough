---
declaration: theorem
origin: cited
lean: AlmostPeriodicity.linfty_almost_periodicity
statement: formalized
proof: formalized
---

# $L_\infty$ almost periodicity

Let $\epsilon\in (0,1]$. Let $K\geq 2$ and $A,S\subseteq G$ with $\lvert A+S\rvert\leq K\lvert A\rvert$. Let $B,C\subseteq G$. Let $\eta=\min(1,\lvert C\rvert/\lvert B\rvert)$. There exists $T\subseteq G$ such that

$$
\lvert T\rvert \geq K^{-4096\lceil \mathcal{L}{\eta}\rceil\epsilon^{-2}}\lvert S\rvert
$$

such that for any $t\in T$ we have

$$
\| \tau_t(\mu_A\ast 1_B\ast \mu_C)-\mu_A\ast 1_B\ast \mu_C\|_{\infty}\leq \epsilon.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$L_p$ almost periodicity](lp-ap.md)

## Proof

Let $T$ be as given in [$L_p$ almost periodicity](lp-ap.md) with $f=1_B$ and $m=\lceil \mathcal{L}{\eta}\rceil$ and $\epsilon=\epsilon/e$. (The size bound on $T$ follows since $e^2\leq 8$.) Fix $t\in T$ and let $F=\tau_t(\mu_A\ast 1_B)-\mu_A\ast 1_B$. We have, for any $x\in G$,

$$
(\tau_t(\mu_A\ast 1_B\ast \mu_C)-\mu_A\ast 1_B\ast \mu_C)(x)=F\ast \mu_C(x)=\sum_y F(y)\mu_{C}(x-y)=\sum_yF(y)\mu_{x-C}(y).
$$

By Hölder's inequality, this is (in absolute value), for any $m\geq 1$,

$$
\lVert F\rVert_{2m}\lVert \mu_{x-C}\rVert_{1+\frac{1}{2m-1}}.
$$

By the construction of $T$ the first factor is at most $\frac{\epsilon}{e}\| 1_B\|_{2m}=\frac{\epsilon}{e}\lvert B\rvert^{1/2m}$. We have by calculation

$$
\lVert \mu_{x-C}\rVert_{1+\frac{1}{2m-1}}=\lvert x-C\rvert^{-1/2m}=\lvert C\rvert^{-1/2m}.
$$

Therefore we have shown that

$$
\| \tau_t(\mu_A\ast 1_B\ast \mu_C)-\mu_A\ast 1_B\ast \mu_C\|_{\infty}\leq \frac{\epsilon}{e}(\lvert C\rvert/\lvert B\rvert)^{-1/2m}.
$$

The claim now follows since, by choice of $m$,

$$
(\lvert C\rvert/\lvert B\rvert)^{-1/2m}\leq e
$$

(dividing into cases as to whether $\eta=1$ or not).

## Lean

Formalized as [`AlmostPeriodicity.linfty_almost_periodicity`](https://yaeldillies.github.io/apap/docs/find/#doc/AlmostPeriodicity.linfty_almost_periodicity).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 144](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ap.tex#L144)
