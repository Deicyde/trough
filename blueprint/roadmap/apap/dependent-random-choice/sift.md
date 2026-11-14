---
declaration: lemma
origin: cited
lean: sifting
statement: formalized
proof: formalized
---

# sift

Let $\epsilon,\delta >0$ and $p\geq \max(2,\epsilon^{-1}\log(2/\delta))$ be an even integer. Let $B_1,B_2\subseteq G$, and let $\mu=\mu_{B_1}\circ\mu_{B_2}$. For any finite set $A\subseteq G$, if

$$
S=\{ x\in G: 1_{A}\circ 1_{A}(x)>(1-\epsilon)\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}\},
$$

then there are $A_1\subseteq B_1$ and $A_2\subseteq B_2$ such that

$$
\langle \mu_{A_1}\circ\mu_{A_2},1_{S}\rangle \geq 1-\delta
$$

and

$$
\min\left( \frac{\left\lvert A_1\right\rvert}{\left\lvert B_1\right\rvert},\frac{\left\lvert A_2\right\rvert}{\left\lvert B_2\right\rvert}\right)\geq \frac{1}{4}\left\lvert A\right\rvert^{-2p}\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^{2p}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [drc](drc.md)

## Proof

Apply Lemma [drc](drc.md) with $f=1_{G\backslash S}$. This produces some $A_1\subseteq B_1$ and $A_2\subseteq B_2$ such that

$$
\langle \mu_{A_1}\circ \mu_{A_2}, 1_{G\backslash S}\rangle\leq 2\frac{\langle (1_{A}\circ 1_{A})^p,1_{G\backslash S}\rangle_\mu}{\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p}
$$

and

$$
\min\left( \frac{\left\lvert A_1\right\rvert}{\left\lvert B_1\right\rvert},\frac{\left\lvert A_2\right\rvert}{\left\lvert B_2\right\rvert}\right)\geq \frac{1}{4}\left\lvert A\right\rvert^{-2p}\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^{2p}.
$$

It then suffices to note that

$$
\langle \mu_{A_1}\circ \mu_{A_2},1_{S}\rangle=1-\langle \mu_{A_1}\circ \mu_{A_2},1_{G\backslash S}\rangle
$$

and by definition of $S$ we have

$$
\langle (1_{A}\circ 1_{A})^p,1_{G\backslash S}\rangle_\mu\leq (1-\epsilon)^p\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p\sum_{x}\mu(x)=(1-\epsilon)^p\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p.
$$

Now use the fact that $p\geq \epsilon^{-1}\log(2/\delta)$ together with the inequality $1-x\leq e^{-x}$ to deduce that the right-hand side is $\leq \tfrac{\delta}{2}\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p$.

## Lean

Formalized as [`sifting`](https://yaeldillies.github.io/apap/docs/find/#doc/sifting).

## Sources

- [Kelley-Meka bound blueprint: chapter/drc.tex, line 68](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/drc.tex#L68)
