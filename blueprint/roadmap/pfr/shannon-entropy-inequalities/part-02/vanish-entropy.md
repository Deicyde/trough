---
declaration: lemma
origin: cited
lean: ProbabilityTheory.mutualInfo_eq_zero
statement: formalized
proof: formalized
---

# Vanishing of mutual information

If $X,Y$ are random variables, then $\mathbb{I}[X:Y] = 0$ if and only if $X,Y$ are independent.

## Depends on

- [Mutual information](../part-01/information-def.md)
- [Independent random variables](independent-def.md)

## Proof depends on

- [Concavity](../../applications-of-jensens-inequality/concave.md)

## Proof

An application of the equality case of Jensen's inequality and [Concavity](../../applications-of-jensens-inequality/concave.md).

## Lean

Formalized as [`ProbabilityTheory.mutualInfo_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 248](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L248)
