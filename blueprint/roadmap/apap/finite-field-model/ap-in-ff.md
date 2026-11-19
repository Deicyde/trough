---
declaration: theorem
origin: cited
lean: ap_in_ff
statement: formalized
proof: formalized
---

# ap_in_ff

If $A_1,A_2,S\subseteq \mathbb{F}_q^n$ are such that $A_1$ and $A_2$ both have density at least $\alpha$ then there is a subspace $V$ of codimension

$$
\mathrm{codim}(V)\leq 2^{27}\mathcal{L}{(}\alpha)^2\mathcal{L}{(}\epsilon \alpha)^2\epsilon^{-2}
$$

such that

$$
\left\lvert \langle \mu_V\ast \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle-\langle \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle\right\rvert\leq \epsilon.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Chang's lemma](../changs-lemma/chang.md)
- [linfty_ap_boosted](../almost-periodicity/linfty-ap-boosted.md)

## Proof

(In this proof we write $G=\mathbb{F}_q^n$.) Let $k=\lceil \mathcal{L}{(}\epsilon\alpha/4)\rceil$. Note that $\lvert A_1+G\rvert=\lvert G\rvert\leq \alpha^{-1}\lvert A\rvert$. Furthermore, $\lvert A_2\rvert/\lvert S\rvert\geq \alpha$. Therefore by Theorem [linfty_ap_boosted](../almost-periodicity/linfty-ap-boosted.md) there exists some $T\subseteq G$ with

$$
\lvert T\rvert \geq \exp(-2^{16}\mathcal{L}{(}\alpha)^2k^2\epsilon^{-2})\lvert S\rvert
$$

such that

$$
\| \mu_T^{(k)}\ast \mu_{A_1}\ast \mu_{A_2}\circ 1_{S}-\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}\|_{\infty}\leq \epsilon/4.
$$

Let $\Delta=\Delta_{1/2}(\mu_T)$ and

$$
V = \{ x \in G : \gamma(x)=1\textrm{ for all }\gamma\in\Delta\}.
$$

Note that

$$
\langle \mu_V\ast \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle = \langle \mu_V,\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}\rangle=\frac{1}{\left\lvert V\right\rvert}\sum_{v\in V}\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(v)
$$

and

$$
\langle \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle = \mu_{A_1}\ast \mu_{A_2}\circ1_{S}(0).
$$

Therefore

$$
\left\lvert \langle \mu_V\ast \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle-\langle \mu_{A_1}\ast \mu_{A_2},1_{S}\rangle\right\rvert\leq \frac{1}{\left\lvert V\right\rvert}\sum_{v\in V}\left\lvert \mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(v)-\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(0)\right\rvert.
$$

In particular it suffices to show that, for any $v\in V$,

$$
\left\lvert \mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(v)-\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(0)\right\rvert\leq \epsilon.
$$

By the triangle inequality and construction of $T$, it suffices to show that

$$
\left\lvert \mu_T^{(k)}\ast \mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(v)-\mu_T^{(k)}\ast\mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(0)\right\rvert\leq \epsilon/2.
$$

By the Fourier transform we have, for any $x\in G$,

$$
\mu_T^{(k)}\ast \mu_{A_1}\ast \mu_{A_2}\circ 1_{S}(x)=\frac{1}{N}\sum_{\gamma\in \widehat{G}}\widehat{\mu_T}(\gamma)^k\widehat{\mu_{A_1}}(\gamma)\widehat{\mu_{A_2}}(\gamma)\widehat{1_{-S}}(\gamma)\gamma(x).
$$

Therefore the left-hand side of the desired inequality is, by the triangle inequality, at most

$$
\frac{1}{N}\sum_{\gamma\in \widehat{G}}\left\lvert \widehat{\mu_T}(\gamma)\right\rvert^k\left\lvert \widehat{\mu_{A_1}}(\gamma)\widehat{\mu_{A_2}}(\gamma)\widehat{1_{-S}}(\gamma)\right\rvert\left\lvert \gamma(v)-1\right\rvert.
$$

By choice of $v\in V$ the summand vanishes when $\gamma\in\Delta$. When $\gamma\not\in \Delta$ the summand is bounded above by

$$
2^{1-k}\left\lvert \widehat{\mu_{A_1}}(\gamma)\widehat{\mu_{A_2}}(\gamma)\widehat{1_{-S}}(\gamma)\right\rvert.
$$

Therefore the left-hand side of the desired inequality is at most

$$
2^{1-k}\frac{1}{N}\sum_{\gamma}\left\lvert \widehat{\mu_{A_1}}(\gamma)\widehat{\mu_{A_2}}(\gamma)\widehat{1_{-S}}(\gamma)\right\rvert\leq 2^{1-k}\left\lvert S\right\rvert\frac{1}{N}\sum_{\gamma}\left\lvert \widehat{\mu_{A_1}}(\gamma)\widehat{\mu_{A_2}}(\gamma)\right\rvert
$$

using the trivial bound $\lvert\widehat{1_{S}}\rvert\leq \left\lvert S\right\rvert$. By the Cauchy-Schwarz inequality the sum on the right is at most

$$
\left( \sum_\gamma \left\lvert \widehat{\mu_{A_1}}\right\rvert^2\right)^{1/2}\left( \sum_\gamma \left\lvert \widehat{\mu_{A_2}}\right\rvert^2\right)^{1/2}.
$$

By Parseval's identity this is at most $\alpha^{-1}$. Therefore the desired inequality follows from

$$
2^{1-k}\left\lvert S\right\rvert\frac{1}{N}\alpha^{-1}\leq 2^{1-k}\alpha^{-1}\leq \epsilon/2.
$$

It remains to check the codimension of $V$. For this, let $\Delta'\subseteq \Delta$ be as provided by Chang's lemma, Lemma [Chang's lemma](../changs-lemma/chang.md), so that

$$
\Delta\subseteq \left\{ \sum_{\gamma\in\Delta'}c_\gamma \gamma : c_\gamma\in \{-1,0,1\} \right\}.
$$

Let

$$
W= \{ x \in G : \gamma(x)=1\textrm{ for all }\gamma\in\Delta'\}.
$$

It follows that $W\leq V$, so it suffices to bound the codimension of $W$. This we can bound trivially using the bound from Chang's lemma and the fact that $\mathcal{L}{(}\delta)=\log(e^2/\delta)\leq 2+\log(1/\delta)\leq 4\log(1/\delta)$, provided $\log(1/\delta)\geq 1$, so

$$
\left\lvert \Delta'\right\rvert\leq  \lceil 4e\mathcal{L}(\delta)\rceil\leq 2^7\log(1/\delta),
$$

where

$$
\delta=\left\lvert T\right\rvert/N\geq \exp(-2^{16}\mathcal{L}{(}\alpha)^2k^2\epsilon^{-2}),
$$

so

$$
\mathrm{codim}(V)\leq \left\lvert \Delta'\right\rvert\leq 2^{23}\mathcal{L}{(}\alpha)^2k^2\epsilon^{-2}\leq 2^{25}\mathcal{L}{(}\alpha)^2\mathcal{L}{(}\epsilon \alpha/4)^2\epsilon^{-2},
$$

and now use $\mathcal{L}{(}\epsilon\alpha/4)\leq 2\mathcal{L}{(}\epsilon\alpha)$, say.

## Lean

Formalized as [`ap_in_ff`](https://yaeldillies.github.io/apap/docs/find/#doc/ap_in_ff).

## Sources

- [Kelley-Meka bound blueprint: chapter/ff.tex, line 3](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ff.tex#L3)
