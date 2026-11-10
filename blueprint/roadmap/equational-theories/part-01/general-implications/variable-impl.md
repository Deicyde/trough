---
declaration: theorem
origin: cited
lean: Law.MagmaLaw.SameCount.derive
statement: formalized
---

# Criterion for implication

If $w \simeq w'$ is such that every variable appears the same number of times in both $w$ and $w'$, and $w \simeq w'$ implies another law $w'' \simeq w'''$, then every variable appears the same number of times in both $w''$ and $w'''$.

## Depends on

Its statement uses no other node that has an article here.

## Proof

Consider the magma $\mathrm{MS}$ of multisets over an arbitrary set $A$ (which can be seen as finitely supported maps $A\rightarrow \mathbb{N}$), with the multiset addition law $+$. By hypothesis, this magma satisfies $w \simeq w'$, and hence $w'' \simeq w'''$, giving the claim by comparing the orders of the elements of $A$ appearing in $w''$ and $w'''$ in this magma.

## Lean

Stated as [`Law.MagmaLaw.SameCount.derive`](https://teorth.github.io/equational_theories/docs/find/#doc/Law.MagmaLaw.SameCount.derive); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/general_implications.tex, line 96](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/general_implications.tex#L96)
