---
declaration: definition
origin: cited
lean: Exchangeability.ConditionallyIID
statement: formalized
---

# Conditionally i.i.d. sequence

A sequence $(X_n)_{n \in \mathbb{N}}$ is *conditionally i.i.d.* with respect to measure $\mu$ if there exists a probability kernel $\nu : \Omega \to \mathrm{Measure}(\alpha)$ such that for any strictly monotone $k : \mathrm{Fin}(m) \to \mathbb{N}$, the joint distribution of $(X_{k(0)}, \ldots, X_{k(m-1)})$ equals the mixture $\mu.\mathrm{bind}(\omega \mapsto \nu(\omega)^{\otimes m})$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Exchangeability.ConditionallyIID`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.ConditionallyIID).

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 49](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L49)
