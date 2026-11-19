---
declaration: lemma
origin: cited
lean: global_dichotomy
statement: formalized
proof: formalized
---

# global_dichotomy

Let $\epsilon >0$ and $\mu\equiv 1/N$. If $A,C\subseteq G$, where $C$ has density at least $\gamma$, and

$$
\left\lvert N\langle \mu_A\ast \mu_A,\mu_C\rangle -1\right\rvert>\epsilon
$$

then, if $f=(\mu_A-1/N)$, $\lVert f\circ f\rVert_{p(\mu)} \geq \epsilon /2N$ for $p=2\lceil \mathcal{L}{(}\gamma)\rceil$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ast_le_circ](ast-le-circ.md)
- [ast_expand](ast-expand.md)
- [circ_expand](circ-expand.md)

## Proof

By Hölder's inequality, for any $p\geq 1$

$$
\epsilon < \left\lvert  N\langle \mu_A \ast \mu_A - 1/N, \mu_C \rangle \right\rvert \leq \lVert \mu_A\ast \mu_A-1/N\rVert_p\gamma^{-1/p}N^{1-1/p}.
$$

In particular if we choose $p=2\lceil\mathcal{L}{(}\gamma)\rceil$ then $\gamma^{-1/p}\leq e^{1/2}\leq 2$ and so we deduce that, by Lemma [ast_expand](ast-expand.md),

$$
\lVert f\ast f\rVert_{p}\geq \tfrac{1}{2}\epsilon N^{1/p-1}.
$$

It remains to use Lemmas [ast_expand](ast-expand.md) and [circ_expand](circ-expand.md) and apply Lemma [ast_le_circ](ast-le-circ.md), and note that we can pass from the $L^p$ norm to the $L^p(\mu)$ norm losing a factor of $N^{1/p}$.

## Lean

Formalized as [`global_dichotomy`](https://yaeldillies.github.io/apap/docs/find/#doc/global_dichotomy).

## Sources

- [Kelley-Meka bound blueprint: chapter/ff.tex, line 103](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ff.tex#L103)
