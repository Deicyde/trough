---
declaration: definition
origin: cited
lean: Exchangeability.Contractable
statement: formalized
---

# Contractable sequence

A sequence $(X_n)_{n \in \mathbb{N}}$ is *contractable* with respect to measure $\mu$ if for all $m \in \mathbb{N}$ and all strictly increasing functions $k, k' : \mathrm{Fin}(m) \to \mathbb{N}$, the joint distribution of $(X_{k(0)}, \ldots, X_{k(m-1)})$ equals that of $(X_{k'(0)}, \ldots, X_{k'(m-1)})$.

## Depends on

- [Exchangeable sequence](def-exchangeable.md)

## Lean

Formalized as [`Exchangeability.Contractable`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.Contractable).

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 38](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L38)
