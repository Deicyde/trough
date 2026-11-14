---
declaration: proposition
origin: cited
lean: di_in_ff
statement: formalized
proof: formalized
---

# di_in_ff

Let $\epsilon \in (0,1)$. If $A,C\subseteq \mathbb{F}_q^n$, where $C$ has density at least $\gamma$, and

$$
\left\lvert N\langle \mu_A\ast \mu_A,\mu_C\rangle -1\right\rvert> \epsilon
$$

then there is a subspace $V$ of codimension

$$
\leq 2^{171}\epsilon^{-24}\mathcal{L}{(}\alpha)^4\mathcal{L}{(}\gamma)^4.
$$

such that $\lVert 1_{A}\ast \mu_V\rVert_\infty \geq (1+\epsilon/32)\alpha$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [global_dichotomy](global-dichotomy.md)
- [unbalancing](../unbalancing/unbalancing.md)
- [ap_in_ff](ap-in-ff.md)
- [circ_expand](circ-expand.md)
- [sift_cor](../dependent-random-choice/sift-cor.md)

## Proof

By Lemma [global_dichotomy](global-dichotomy.md), if $f=\mu_A-1/N$,

$$
\lVert f\circ f\rVert_{p(\mu)}\geq \epsilon /2N,
$$

where $p=2\lceil \mathcal{L}{(}\gamma)\rceil\leq 4\mathcal{L}{(}\gamma)$. By Lemma [unbalancing](../unbalancing/unbalancing.md) there exists some $p'$ such that

$$
p'\leq 128\epsilon^{-1}\log(96/\epsilon)\mathcal{L}{(}\gamma)
$$

such that

$$
\lVert f\circ f+1/N\rVert_{p'(\mu)}\geq (1+\epsilon/4)/N.
$$

By Lemma [circ_expand](circ-expand.md) $f\circ f+1/N=\mu_A\circ \mu_A$.

Let $q=2\lceil p'+2^8\epsilon^{-2}\log(64/\epsilon)\rceil$. By Corollary [sift_cor](../dependent-random-choice/sift-cor.md), there are $A_1,A_2$, both of density $\geq \alpha^{2q}$ such that

$$
\langle \mu_{A_1}\circ \mu_{A_2},1_{S}\rangle \geq 1-\epsilon/32
$$

where

$$
S=\{x : \mu_A\circ \mu_A(x)\geq (1-\epsilon/16)\| \mu_A\circ \mu_A\|_{q(\mu)}\}.
$$

Since

$$
\| \mu_A\circ \mu_A\|_{q(\mu)}\geq \| \mu_A\circ \mu_A\|_{p'(\mu)}\geq (1+\epsilon/4)/N
$$

we know

$$
S\subseteq S'=\{x : \mu_A\circ \mu_A(x)\geq (1+\epsilon/8)/N\}.
$$

By Theorem [ap_in_ff](ap-in-ff.md) (applied with $\epsilon$ replaced by $\epsilon/32$) there is a subspace $V$ of codimension

$$
\leq 2^{37}\mathcal{L}{(}\alpha^{2q})^2\mathcal{L}{(}\epsilon\alpha^{2q}/32)^2\epsilon^{-2}
$$

such that

$$
\langle \mu_V\ast \mu_{A_1}\circ \mu_{A_2},1_{S'}\rangle \geq 1-\tfrac{1}{16}\epsilon.
$$

Using $\mathcal{L}{(}xy)\leq x^{-1}\mathcal{L}{(}y)$ we have

$$
\mathcal{L}{(}\epsilon \alpha^{2q}/32)\leq 32\epsilon^{-1}\mathcal{L}{(}\alpha^{2q}),
$$

and we also use $\mathcal{L}{(}x^y)\leq y\mathcal{L}{(}x)$ to simplify the codimension bound to

$$
\leq 2^{51}q^4\mathcal{L}{(}\alpha)^4\epsilon^{-4}.
$$

We further note that (using $\log x\leq x$ say)

$$
q\leq 2^{10}p'\epsilon^{-2}\log(64/\epsilon)\leq 2^{30}\epsilon^{-5}\mathcal{L}{(}\gamma).
$$

Therefore the desired codimension bound follows. Finally, by definition of $S'$, it follows that

$$
\begin{aligned}
(1+\epsilon/32)/N
&\leq ((1+\epsilon/8)/N)(1-\epsilon/16)\\
&\leq \langle \mu_V\ast \mu_{A_1}\circ \mu_{A_2},\mu_A\circ \mu_A\rangle\\
&\leq \lVert \mu_V\ast \mu_A\rVert_\infty \lVert \mu_{A}\ast \mu_{A_2}\circ \mu_{A_1}\rVert_1\\
&= \lVert \mu_V\ast 1_{A}\rVert_\infty\left\lvert A\right\rvert^{-1},
\end{aligned}
$$

and the proof is complete.

## Lean

Formalized as [`di_in_ff`](https://yaeldillies.github.io/apap/docs/find/#doc/di_in_ff).

## Sources

- [Kelley-Meka bound blueprint: chapter/ff.tex, line 123](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ff.tex#L123)
