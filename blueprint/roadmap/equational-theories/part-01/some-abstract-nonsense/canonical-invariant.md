---
declaration: theorem
origin: cited
---

# Canonical invariant

Let $\Gamma$ be a theory with some alphabet $X$, and let $M_{X,\Gamma}$ be a free magma with alphabet $X$ subject to $\Gamma$, with associated map $\iota_{X,\Gamma}: X \to M_{X,\Gamma}$. Then for any $w,w' \in M_X$, we have

$$
\Gamma \models w \simeq w' \text{ if and only if } \varphi_{\iota_{X,\Gamma}}(w) = \varphi_{\iota_{X,\Gamma}}(w').
$$

## Depends on

- [Free magma relative to a theory](free-theory.md)

## Proof depends on

- [Existence and uniqueness of free magmas](freemag-exist.md)

## Proof

By [Existence and uniqueness of free magmas](freemag-exist.md) we may take $M_{X,\Gamma}$ to be the canonical free magma constructed in the proof of that theorem. The claim is then clear from expanding out definitions.

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 51](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L51)
