---
declaration: lemma
origin: cited
lean: Law.satisfies_fin_satisfies_nat
statement: formalized
---

# compatibility-between-magma-laws

\[Compatibility between magma laws over finite sets and the natural numbers\] Let $E$ be a magma law defined over $n$ variables and let $\tilde{E}$ be the same equation with variables ranging over the natural numbers (formally, $\tilde{E}$ is the image of $E$ under the canonical map from the finite set with $n$ elements to the natural numbers). Then any magma $M$ satisfies $E$ if and only if it satisfies $\tilde{E}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

In the forward direction, suppose $\phi : \mathbb{N} \to M$ is a substitution. Then the restriction of $\phi$ to the first $n$ natural numbers is a substitution for the variables of $E$, and since $M$ satisfies $E$, the law $E$ is true in $M$ under this substitution. Since $\tilde{E}$ is the same as $E$ under the substitution $\phi$, $M$ satisfies $\tilde{E}$.

In the reverse direction, suppose $\phi : \{0, 2, \ldots, n-1\} \to M$ is a substitution. Then $\phi$ can be extended to a substitution $\tilde{\phi} : \mathbb{N} \to M$ by setting $\tilde{\phi}(i) = \phi(i)$ for $i \leq n$ and $\tilde{\phi}(i) = 0$ for $i \geq n$. Since $M$ satisfies $\tilde{E}$ under the substitution $\tilde{\phi}$, it satisfies $E$ under the restriction of $\tilde{\phi}$ to the first $n$ natural numbers, which is precisely $\phi$. The special case where $n = 0$ is in fact impossible, since there cannot be an expression with no variables.

## Lean

Formalized as [`Law.satisfies_fin_satisfies_nat`](https://teorth.github.io/equational_theories/docs/find/#doc/Law.satisfies_fin_satisfies_nat).

## Sources

- [Equational Theories blueprint: chapter/metatheorems_from_invariants.tex, line 182](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/metatheorems_from_invariants.tex#L182)
