---
declaration: lemma
origin: cited
lean: PartialIntegration
statement: formalized
proof: formalized
---

# PartialIntegration

Let $f, g$ be once differentiable functions from $\mathbb{R}_{>0}$ to $\mathbb{C}$ so that $fg'$ and $f'g$ are both integrable, and $f\cdot g (x)\to 0$ as $x\to 0^+,\infty$. Then

$$
\int_0^\infty f(x)g'(x) dx = -\int_0^\infty f'(x)g(x)dx.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Partial integration.

## Lean

Formalized as [`PartialIntegration`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/PartialIntegration).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/MellinCalculus.lean)
