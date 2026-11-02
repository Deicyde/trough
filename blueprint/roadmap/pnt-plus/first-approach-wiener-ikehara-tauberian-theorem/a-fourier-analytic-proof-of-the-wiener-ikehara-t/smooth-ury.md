---
declaration: lemma
origin: cited
lean: smooth_urysohn
statement: formalized
proof: formalized
---

# Smooth Urysohn lemma

If $I$ is a closed interval contained in an open interval $J$, then there exists a smooth function $\Psi: \mathbb{R} \to \mathbb{R}$ with $1_I \leq \Psi \leq 1_J$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

A standard analysis lemma, which can be proven by convolving $1_K$ with a smooth approximation to the identity for some interval $K$ between $I$ and $J$. Note that we have “SmoothBumpFunction”s on smooth manifolds in Mathlib, so this shouldn't be too hard...

## Lean

Formalized as [`smooth_urysohn`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/smooth_urysohn).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
