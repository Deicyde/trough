---
declaration: lemma
origin: cited
lean: ProbabilityTheory.mutual_comp_comp_le
statement: formalized
proof: formalized
---

# Unconditional data processing inequality

Let $X,Y$ be random variables. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\mathbb{I}[f(X) : g(Y )] \leq \mathbb{I}[X : Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [One-sided unconditional data processing inequality](data-process-unc-one.md)
- [Commutativity and associativity of joint entropy](../../shannon-entropy-inequalities/part-01/entropy-comm.md)

## Proof

From [One-sided unconditional data processing inequality](data-process-unc-one.md), [Commutativity and associativity of joint entropy](../../shannon-entropy-inequalities/part-01/entropy-comm.md) we have $\mathbb{I}[f(X) : Y] \leq \mathbb{I}[X:Y]$ and $\mathbb{I}[f(X): g(Y)] \leq \mathbb{I}[f(X):Y]$, giving the claim.

## Lean

Formalized as [`ProbabilityTheory.mutual_comp_comp_le`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutual_comp_comp_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 21](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L21)
