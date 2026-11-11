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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 248](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L248)
