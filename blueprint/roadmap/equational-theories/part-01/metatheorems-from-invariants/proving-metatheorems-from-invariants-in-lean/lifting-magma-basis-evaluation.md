---
declaration: theorem
origin: cited
lean: MagmaLaw.models_iff_satisfies_ι
statement: formalized
---

# Evaluation theorem for lifting magma families

Suppose $E$ is an equation involving a set of variables $X$, and let $G$ be a lifting magma family.

Determining whether $E$ is satisfied by $G_X$ is equivalent to checking that $E$ is true with the specific substitution $\iota_X$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For the forward direction, suppose $E$ is satisfied by $G_X$. Then, by definition, any substitution of the variables in $E$ with elements of $G_X$ will yield a true equation. In particular, substituting according to $\iota_X$ will yield a true equation.

For the reverse direction, suppose that $E$ is true when evaluated with the substitution $\iota_X$. Now, consider an arbitrary substitution of variables $f : X \to G_X$. By the lifting magma family property, there is a magma homomorphism $\operatorname{lift}{f} : G_X \to G_X$ such that $\operatorname{lift}{f}(\iota_X(x)) = f(x)$ for all $x$ in $X$. In other words, applying the substitution $f$ is equivalent to first applying to substitution $\iota_X$ and then applying the homomorphism $\operatorname{lift}{f}$. Since $E$ is true when evaluated with the substitution $\iota_X$, it is also true after applying the homomorphism $\operatorname{lift}{f}$. Thus, $E$ is satisfied by $G_X$.

## Lean

Stated as [`MagmaLaw.models_iff_satisfies_ι`](https://teorth.github.io/equational_theories/docs/find/#doc/MagmaLaw.models_iff_satisfies_ι); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/metatheorems_from_invariants.tex, line 132](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/metatheorems_from_invariants.tex#L132)
