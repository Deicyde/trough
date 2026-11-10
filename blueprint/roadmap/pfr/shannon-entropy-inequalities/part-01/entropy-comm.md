---
declaration: lemma
origin: cited
lean: ProbabilityTheory.entropy_comm, ProbabilityTheory.entropy_assoc
statement: formalized
proof: formalized
---

# Commutativity and associativity of joint entropy

If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\mathbb{H}[X, Y] = \mathbb{H}[Y, X]$ and $\mathbb{H}[X, (Y,Z)] = \mathbb{H}[(X,Y), Z]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Entropy and relabeling](relabeled-entropy.md)

## Proof

Set up an injection from $(X,Y)$ to $(Y,X)$ and use [Entropy and relabeling](relabeled-entropy.md) for the first claim. Similarly for the second claim.

## Lean

Formalized as [`ProbabilityTheory.entropy_comm`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_comm), [`ProbabilityTheory.entropy_assoc`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_assoc).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 90](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L90)
