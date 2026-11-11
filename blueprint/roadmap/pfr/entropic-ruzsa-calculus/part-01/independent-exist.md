---
declaration: lemma
origin: cited
lean: ProbabilityTheory.independent_copies, ProbabilityTheory.independent_copies', ProbabilityTheory.independent_copies_two, ProbabilityTheory.independent_copies3_nondep
statement: formalized
proof: formalized
---

# Existence of independent copies

Let $X_i : \Omega_i \to S_i$ be random variables for $i=1,\dots,k$. Then if one gives $\prod_{i=1}^k S_i$ the product measure of the laws of $X_i$, the coordinate functions $(x_j)_{j=1}^k \mapsto x_i$ are jointly independent random variables which are copies of the $X_1,\dots,X_k$.

## Depends on

- [Independent random variables](../../shannon-entropy-inequalities/part-02/independent-def.md)

## Proof

Explicit computation.

## Lean

Formalized as [`ProbabilityTheory.independent_copies`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.independent_copies), [`ProbabilityTheory.independent_copies'`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.independent_copies'), [`ProbabilityTheory.independent_copies_two`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.independent_copies_two), [`ProbabilityTheory.independent_copies3_nondep`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.independent_copies3_nondep).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 75](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L75)
