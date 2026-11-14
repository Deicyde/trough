---
declaration: definition
origin: cited
lean: Exchangeability.Exchangeable
statement: formalized
---

# Exchangeable sequence

A sequence $(X_n)_{n \in \mathbb{N}}$ of random variables is *exchangeable* with respect to measure $\mu$ if for every $n \in \mathbb{N}$ and every permutation $\sigma$ of $\{0, \ldots, n-1\}$, the joint distribution of $(X_{\sigma(0)}, \ldots, X_{\sigma(n-1)})$ equals that of $(X_0, \ldots, X_{n-1})$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Exchangeability.Exchangeable`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.Exchangeable).

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 28](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L28)
