---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Commutativity.commDataProcessedG_of_commutativityPoints, MIPRE.LIDT.Co.Commutativity.commDataProcessedG, MIPRE.LIDT.Co.Commutativity.comMain_of_commutativityPoints, MIPRE.LIDT.Co.Commutativity.comMain
statement: formalized
proof: formalized
---

# Commutation of the slice measurements, in a symmetric model

Consider an $(\varepsilon, \delta, \gamma)$-good symmetric strategy in $S$ for the low individual degree test in $m + 1$ variables, with point measurements $A^w$ in $\mathcal{P}$ for $w \in \mathbb{F}_q^{m+1}$, written $w = (u, x)$ with $u \in \mathbb{F}_q^m$ and $x \in \mathbb{F}_q$. For each $x \in \mathbb{F}_q$ let $G^x$ be a projective submeasurement in $\mathcal{P}$ whose outcomes are the polynomials, and $Z^x \in \mathcal{P}$. Suppose that for some $\eta$:

1. *(consistency with the points)* $\mathop{\mathbb{E}}_{(u, x)} \mathrm{cons}\bigl(A^{(u, x)}, G^{x, [u]}\bigr) \leq \eta$, where $G^{x, [u]}$ is $G^x$ evaluated at $u$;
2. *(strong self-consistency)* $\mathop{\mathbb{E}}_x \sum_g \| (L(G^x_g) - R(G^x_g)) \Psi \|^2 \leq \eta$;
3. *(boundedness)* $Z^x \geq 0$ and $\mathop{\mathbb{E}}_u A^{(u, x)}_{g(u)} \leq Z^x$ for all $x$ and $g$, and $\mathop{\mathbb{E}}_x \mathrm{ev}\bigl(L(1 - G^x_{\mathrm{total}})\, R(Z^x)\bigr) \leq \eta$;

with uniformly random $u$ and $x$. Then, for independent uniformly random $x, y \in \mathbb{F}_q$,

$$
\mathop{\mathbb{E}}_{x, y} \sum_{g, h} \bigl\| L\bigl(G^x_g G^y_h - G^y_h G^x_g\bigr) \Psi \bigr\|^2 \leq 30\, m
\Bigl(\gamma^{1/4} + \eta^{1/4} + \Bigl(\frac{d}{q}\Bigr)^{1/4}\Bigr).
$$

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md)

## Proof depends on

- [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)
- [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.Commutativity.comMain` in `MIPRE/Background/LIDT/MIPStarRE/LDT/Commutativity/`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M7). It first bounds the commutators of the evaluated slice measurements $G^x_{[g(u) = a]}$ and $G^y_{[h(v) = b]}$, on average over two points $(u, x)$ and $(v, y)$, by $48\, m (\gamma^{1/2} + \eta^{1/2})$: a chain of comparisons, each a Cauchy–Schwarz estimate for the vector state, inserts the point measurements next to the slice measurements by consistency, exchanges the two points by the commutativity of points (Lemma [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md)) and removes them again, the boundedness controlling the mass that $G^x$ loses. It then passes from the evaluated to the full slice measurements: two distinct polynomials agree at a random point with probability at most $md/q$, so the evaluation loses at most that collision mass, and the closeness estimates of Lemma [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md) turn the bound into the displayed one, with its fourth roots. Where the vendored proof uses the permutation invariance of the state, the port uses $\mathrm{ev}(L(x)) = \mathrm{ev}(R(x))$ (Lemma [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)).

## Lean

Formalized as [`MIPRE.LIDT.Co.Commutativity.commDataProcessedG_of_commutativityPoints`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Commutativity.commDataProcessedG_of_commutativityPoints), [`MIPRE.LIDT.Co.Commutativity.commDataProcessedG`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Commutativity.commDataProcessedG), [`MIPRE.LIDT.Co.Commutativity.comMain_of_commutativityPoints`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Commutativity.comMain_of_commutativityPoints), [`MIPRE.LIDT.Co.Commutativity.comMain`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Commutativity.comMain).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3874](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3874)
