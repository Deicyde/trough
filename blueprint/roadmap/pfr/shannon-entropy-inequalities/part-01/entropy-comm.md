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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 90](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L90)
