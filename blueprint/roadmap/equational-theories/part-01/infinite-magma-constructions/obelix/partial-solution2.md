---
declaration: definition
origin: cited
---

# partial-solution2

A *partial solution* for an Obelix is a partial function $f : G \to G$ with the properties:

- $f$ has finite domain.
- $f$ is injective.
- $f$ maps the identity (of $G$, so, 0) to the identity.
- If $x$ is in the domain of $f$, and $f(x)$ is in the domain, then so is $f^2(x) - f(x)$.
- If $x$ is in the domain of $f$, and $f(x)$ is in the domain, then $f(f^2(x) - f(x)) = f(x) - x$. This is well-defined by property (4).
- The function $x - f(x)$, which is defined on the same domain as $f$, is injective.
- If $x$ is in the domain of $f$ but $f(x)$ isn't in the domain, then $x - f(x)$ isn't in the domain or image of $f$.

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 215](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L215)
