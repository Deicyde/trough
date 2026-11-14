---
declaration: lemma
origin: cited
lean: unbalancing
statement: formalized
proof: formalized
---

# unbalancing

Let $\epsilon\in(0,1)$ and $\nu:G\to\mathbb{R}_{\geq 0}$ be some probability measure such that $\widehat{\nu}\geq 0$. Let $f:G\to\mathbb{R}$. If $\lVert f\circ f\rVert_{p(\nu)}\geq \epsilon$ for some $p\geq 1$ then $\lVert f\circ f+1\rVert_{p'(\nu)}\geq 1+\tfrac{1}{2}\epsilon$ for $p'=120\epsilon^{-1}\log(3/\epsilon)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [nonneg_moments](nonneg-moments.md)

## Proof

Up to gaining a factor of 5 in $p'$, we can assume that $p\geq 5$ is an odd integer. Since the Fourier transforms of $f$ and $\nu$ are non-negative,

$$
\mathbb{E} \nu f^{p}= \widehat{\nu}\ast\widehat{f}^{(p)}(0_{\widehat{G}})\geq 0.
$$

It follows that, since $2\max(x,0)=x+\left\lvert x\right\rvert$ for $x\in\mathbb{R}$,

$$
2\langle \max(f,0),f^{p-1}\rangle_\nu=\mathbb{E} \nu f^{p}+\langle \left\lvert f\right\rvert,f^{p-1}\rangle_\nu\geq \lVert f\rVert_{p(\nu)}^p\geq \epsilon^p.
$$

Therefore, if $P=\{ x : f(x) \geq 0\}$, then $\langle 1_{P},f^{p}\rangle_\nu\geq \frac{1}{2}\epsilon^{p}$. Furthermore, if $T=\{ x\in P : f(x) \geq \tfrac{3}{4}\epsilon\}$ then $\langle 1_{P\backslash T},f^p\rangle_\nu \leq \tfrac{1}{4}\epsilon^{p}$, and hence by the Cauchy-Schwarz inequality,

$$
\nu(T)^{1/2}\lVert f\rVert_{2p(\nu)}^{p}\geq \langle 1_{T}, f^{p}\rangle_\nu \geq \tfrac{1}{4}\epsilon^{p}.
$$

On the other hand, by the triangle inequality

$$
\lVert f\rVert_{2p(\nu)}\leq 1+\lVert f+1\rVert_{2p(\nu)}\leq 3,
$$

or else we are done, with $p'=2p$. Hence $\nu(T)\geq (\epsilon/3)^{3p}$. It follows that, for any $p'\geq 1$,

$$
\lVert f+1\rVert_{p'(\nu)}\geq \langle 1_{T},\left\lvert f+1\right\rvert^{p'}\rangle_\nu^{1/p'}\geq  (1+\tfrac{3}{4}\epsilon)(\epsilon/3)^{3p/p'}.
$$

The desired bound now follows if we choose $p'=24\epsilon^{-1}\log(3/\epsilon)p$, using $1-x\leq e^{-x}$.

## Lean

Formalized as [`unbalancing`](https://yaeldillies.github.io/apap/docs/find/#doc/unbalancing).

## Sources

- [Kelley-Meka bound blueprint: chapter/unbalancing.tex, line 15](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/unbalancing.tex#L15)
