---
declaration: lemma
origin: cited
lean: drc
statement: formalized
proof: formalized
---

# drc

Let $p\geq 2$ be an even integer. Let $B_1,B_2\subseteq G$ and $\mu=\mu_{B_1}\circ\mu_{B_2}$. For any finite set $A\subseteq G$ and function $f:G\to\mathbb{R}_{\geq 0}$ there exist $A_1\subseteq B_1$ and $A_2\subseteq B_2$ such that

$$
\langle \mu_{A_1}\circ \mu_{A_2}, f\rangle \lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p\leq 2\langle (1_{A}\circ 1_{A})^p,f\rangle_\mu
$$

and

$$
\min\left( \frac{\left\lvert A_1\right\rvert}{\left\lvert B_1\right\rvert},\frac{\left\lvert A_2\right\rvert}{\left\lvert B_2\right\rvert}\right)\geq \frac{1}{4}\left\lvert A\right\rvert^{-2p}\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^{2p}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

First note that the statement is trivially true (with $A_1=B_1$ and $A_2=B_2$, say) if $\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p=0$. We can therefore assume this is $\neq 0$.

For $s\in G^{p}$ let $A_1(s)=B_1\cap (A+s_1)\cap\cdots\cap (A+s_{p})$, and similarly for $A_2(s)$. Note that

$$
\begin{aligned}
\langle (1_{A}\circ 1_{A})^p, f\rangle_\mu
&=\sum_{x} \mu_{B_1}\circ \mu_{B_2}(x)(1_{A}\circ 1_{A}(x))^pf(x)\\
&=\sum_{b_1,b_2}\mu_{B_1}(b_1)\mu_{B_2}(b_2)1_{A}\circ 1_{A}(b_1-b_2)^{p}f(b_1-b_2)\\
&=\sum_{b_1,b_2}\mu_{B_1}(b_1)\mu_{B_2}(b_2)\left( \sum_{t\in G}1_{A+t}(b_1)1_{A+t}(b_2)\right)^{p}f(b_1-b_2)\\
&=\sum_{b_1,b_2}\mu_{B_1}(b_1)\mu_{B_2}(b_2)\sum_{s\in G^p}1_{A_1(s)}(b_1)1_{A_2(s)}(b_2)f(b_1-b_2)\\
&=\left\lvert B_1\right\rvert^{-1}\left\lvert B_2\right\rvert^{-1}\sum_{s\in G^p}\langle 1_{A_1(s)}\circ 1_{A_2(s)}, f\rangle.
\end{aligned}
$$

In particular, applying this with $f\equiv 1$ we see that

$$
\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p=\left\lvert B_1\right\rvert^{-1}\left\lvert B_2\right\rvert^{-1}\sum_s\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
$$

and

$$
\frac{\langle (1_{A}\circ 1_{A})^p,f\rangle_\mu}{\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p}=\frac{\sum_{s}\langle 1_{A_1(s)}\circ 1_{A_2(s)}, f\rangle}{\sum_s \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert}=\eta,
$$

say. Let $M>0$ be some parameter, and let

$$
g(s) = \begin{cases} 1&\textrm{ if }0\lt \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert\lt M^2\textrm{ and }\\0&\textrm{ otherwise.}\end{cases}
$$

Then we have

$$
\sum_s g(s)\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
\lt \sum_s M\left\lvert A_1(s)\right\rvert^{1/2}\left\lvert A_2(s)\right\rvert^{1/2}.
$$

To see why, note first that each summand on the left-hand side is $\leq$ the corresponding summand on the right-hand side, arguing by cases on whether $g(s)=1$ or not. It therefore suffices to show that there exists some $s$ such that the summand on the left-hand side is $<$ the corresponding summand on the right-hand side.

If $g(s)=0$ for all $s$ then choose some $s$ such that $\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert\geq M^2$ (this must exist or else $\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert=0$ for all $s$, but then $\lVert 1_A\circ 1_A\rVert_{p(\mu)}^p=0$ by the above calculation). Otherwise, choose some $s$ such that $g(s)=1$, and note that for this $s$ we have, by definition of $s$,

$$
\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert\lt M\left\lvert A_1(s)\right\rvert^{1/2}\left\lvert A_2(s)\right\rvert^{1/2}.
$$

We now choose

$$
M=\tfrac{1}{2}\left\lvert A\right\rvert^{-p}(\left\lvert B_1\right\rvert\left\lvert B_2\right\rvert)^{1/2}\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^p,
$$

so that, by the Cauchy-Schwarz inequality,

$$
\begin{aligned}
\sum_s g(s)\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
&< M \sum_s \left\lvert A_1(s)\right\rvert^{1/2}\left\lvert A_2(s)\right\rvert^{1/2}\\
&\leq M\left( \sum_s \sum_{x\in G}1_{A_1(s)}(x)\right)^{1/2}\left( \sum_s \sum_{x\in G}1_{A_2(s)}(x)\right)^{1/2}\\
&= M\left\lvert A\right\rvert^p(\left\lvert B_1\right\rvert\left\lvert B_2\right\rvert)^{1/2}\\
&=\frac{1}{2}\sum_s \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
\end{aligned}
$$

and so

$$
\sum_s (1-g(s))\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
> \frac{1}{2}\sum_s \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
$$

whence

$$
\sum_s\langle 1_{A_1(s)}\circ 1_{A_2(s)},f\rangle =\eta \sum \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert
< 2\eta \sum_s \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert(1-g(s)).
$$

In particular there must exist some $s$ such that

$$
\langle 1_{A_1(s)}\circ 1_{A_2(s)},f\rangle< 2\eta \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert(1-g(s)).
$$

We claim this $s$ meets the requirements. The first is satisfied since the right-hand side is $\leq 2\eta \left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert$. The second is satisfied since the left-hand side is trivially $\geq 0$ and hence such an $s$ must satisfy $g(s)=0$, whence either $\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert\geq M^2$, that is,

$$
\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert\geq \frac{1}{4}\left\lvert A\right\rvert^{-2p}\left\lvert B_1\right\rvert\left\lvert B_2\right\rvert\lVert 1_{A}\circ 1_{A}\rVert_{p(\mu)}^{2p},
$$

or $\left\lvert A_1(s)\right\rvert\left\lvert A_2(s)\right\rvert=0$, which can't happen because then the right-hand side is $=0$.

The final bound now follows since $xy \leq \min(x,y)$ when $x,y\leq 1$.

## Lean

Formalized as [`drc`](https://yaeldillies.github.io/apap/docs/find/#doc/drc).

## Sources

- [Kelley-Meka bound blueprint: chapter/drc.tex, line 4](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/drc.tex#L4)
