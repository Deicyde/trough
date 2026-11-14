---
declaration: corollary
origin: cited
lean: sifting_cor
statement: formalized
proof: formalized
---

# sift_cor

Let $\epsilon,\delta>0$ and $p\geq \max(2,\epsilon^{-1}\log(2/\delta))$ be an even integer and $\mu\equiv 1/N$. If $A\subseteq G$ has density $\alpha$ and

$$
S = \{ x : \mu_A\circ \mu_A(x) \geq (1-\epsilon)\| \mu_A\circ \mu_A\|_{p(\mu)}\}
$$

then there are $A_1,A_2\subseteq G$ such that

$$
\langle \mu_{A_1}\circ \mu_{A_2}, 1_S\rangle \geq 1-\delta
$$

and both $A_1$ and $A_2$ have density

$$
\geq \frac{1}{4}\alpha^{2p}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [sift](sift.md)

## Proof

We apply Lemma [sift](sift.md) with $B_1=B_2=G$. It remains to note that

$$
\| 1_A\circ 1_A\|_{p(\mu)}\geq \| 1_A\circ 1_A\|_{1(\mu)}=\lvert A\rvert^2/N.
$$

## Lean

Formalized as [`sifting_cor`](https://yaeldillies.github.io/apap/docs/find/#doc/sifting_cor).

## Sources

- [Kelley-Meka bound blueprint: chapter/drc.tex, line 95](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/drc.tex#L95)
