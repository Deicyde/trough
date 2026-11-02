---
declaration: corollary
origin: cited
---

# Description of graph

If $w,w'$ are words, then $w' \to w$ holds if and only if $w' \sim (Y \diamond Z) \diamond (w \diamond Z)$ for some words $Y,Z$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Description of equivalence](irred-desc.md)

## Proof

By replacing $w,w'$ with irreducible equivalents, we may assume without loss of generality that $w,w'$ are irreducible. By hypothesis, $w$ is equivalent to $w \diamond w'$. The claim now follows from [Description of equivalence](irred-desc.md).

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 73](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L73)
