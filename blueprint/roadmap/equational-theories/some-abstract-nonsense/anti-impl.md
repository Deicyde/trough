---
declaration: corollary
origin: cited
---

# Criterion for anti-implication

Let $\Gamma$ be a theory with some alphabet $X$, and let $M_{X,\Gamma}$ be a free magma with alphabet $X$ subject to $\Gamma$, with associated map $\iota_{X,\Gamma}: X \to M_{X,\Gamma}$. Let $w \simeq w'$ and $w'' \simeq w'''$ be laws with alphabet $X$. If one has

$$
\varphi_{\iota_{X,\Gamma}}(w) = \varphi_{\iota_{X,\Gamma}}(w')
$$

but

$$
\varphi_{\iota_{X,\Gamma}}(w'') \neq \varphi_{\iota_{X,\Gamma}}(w'''),
$$

then the law $w \simeq w'$ cannot imply the law $w'' \simeq w'''$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Canonical invariant](canonical-invariant.md)

## Proof

By [Canonical invariant](canonical-invariant.md), the hypothesis $\iota_{X,\Gamma}(w) = \iota_{X,\Gamma}(w')$ is equivalent to $\Gamma \models w \simeq w'$, and the hypothesis $\iota_{X,\Gamma}(w'') \neq \iota_{X,\Gamma}(w''')$ is equivalent to $\Gamma \not\models w'' \simeq w'''$. The claim follows.

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 64](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L64)
