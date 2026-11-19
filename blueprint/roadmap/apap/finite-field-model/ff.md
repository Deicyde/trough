---
declaration: theorem
origin: cited
lean: ff
statement: formalized
proof: formalized
---

# ff

Let $q$ be an odd prime power. If $A\subseteq \mathbb{F}_q^n$ with $\alpha=\left\lvert A\right\rvert/q^n$ has no non-trivial three-term arithmetic progressions then

$$
n \ll \mathcal{L}{(}\alpha)^9.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [no3aps_inner_prod](no3aps-inner-prod.md)
- [di_in_ff](di-in-ff.md)

## Proof

Let $t\geq 0$ be maximal such that there is a sequence of subspaces $\mathbb{F}_q^n=V_0\geq \cdots \geq V_t$ and associated $A_i\subseteq V_i$ with $A_0=A$ such that

1. for $0\leq i\leq t$ there exists $x_i$ such that $A_i\subseteq A-x_i$,

2. with $\alpha_i=\left\lvert A_i\right\rvert/\left\lvert V_i\right\rvert$ we have

    $$
    \alpha_{i+1}\geq \frac{65}{64}\alpha_i
    $$

    for $0\leq i\lt t$, and

3. $$
    \mathrm{codim} (V_{i+1}) \leq \mathrm{codim}(V_i)+O(\mathcal{L}{(}\alpha)^8)
    $$

    for $0\leq i\lt t$. (here the second summand should be replaced with whatever explicit codimension bound we get from the above).

Note this is well-defined since $t=0$ meets the requirements, and this process is finite and $t \ll \mathcal{L}{(}\alpha)$, since $\alpha_i\leq 1$ for all $i$. Therefore

$$
\mathrm{codim}(V_t) \ll \mathcal{L}{(}\alpha)^9.
$$

Suppose first that

$$
\lvert V_t\rvert\langle \mu_{A_t}\ast \mu_{A_t},\mu_{2\cdot A_t}\rangle<1/2.
$$

In this case we now apply Proposition [di_in_ff](di-in-ff.md) to $A_t\subseteq V_t$ with $\epsilon=1/2$ (note that $N=\lvert V_t\rvert$ and all inner product, $\mu$ etc, are relative to the ambient group $V_t$ now). Therefore there is a subspace $V\leq V_t$ of codimension (relative to $V_t$) $\ll \mathcal{L}{(}\alpha)^8$ such that there exists some $x\in V_t$ with

$$
\frac{\lvert (A_t-x)\cap V\rvert}{\lvert V\rvert}=1_{A_t}\ast \mu_V(x)=\| 1_{A_t}\ast \mu_V\|_\infty \geq (1+1/64)\alpha_t,
$$

which contradicts the maximality of $t$, letting $V_{t+1}=V$ and $A_{t+1}=(A_t-x)\cap V_t$.

Therefore

$$
\lvert V_t\rvert\langle \mu_{A_t}\ast \mu_{A_t},\mu_{2\cdot A_t}\rangle\geq 1/2.
$$

By Lemma [no3aps_inner_prod](no3aps-inner-prod.md) the left-hand side is equal to $\lvert V_t\rvert/\lvert A_t\rvert^2$, and therefore

$$
\alpha^2 \leq \alpha_t^2 \leq 2/\lvert V_t\rvert.
$$

By the codimension bound the right-hand side is at most

$$
2q^{O(\mathcal{L}{(}\alpha)^9)-n}.
$$

If $\alpha^2 \leq 2q^{-n/2}$ we are done, otherwise we deduce that $\mathcal{L}{(}\alpha)^9 \gg n$ as required.

## Lean

Formalized as [`ff`](https://yaeldillies.github.io/apap/docs/find/#doc/ff).

## Sources

- [Kelley-Meka bound blueprint: chapter/ff.tex, line 191](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ff.tex#L191)
