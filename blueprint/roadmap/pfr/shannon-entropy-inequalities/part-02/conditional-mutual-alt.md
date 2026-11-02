---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condMutualInfo_eq, ProbabilityTheory.condMutualInfo_eq'
statement: formalized
proof: formalized
---

# Alternate formula for conditional mutual information

We have

$$
\mathbb{I}[X:Y|Z] := \mathbb{H}[X|Z] + \mathbb{H}[Y|Z] - \mathbb{H}[X,Y|Z]
$$

and

$$
\mathbb{I}[X:Y|Z] := \mathbb{H}[X|Z] - \mathbb{H}[X|Y,Z].
$$

## Depends on

- [Conditional mutual information](conditional-mutual-def.md)

## Proof

Routine computation.

## Lean

Formalized as [`ProbabilityTheory.condMutualInfo_eq`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutualInfo_eq), [`ProbabilityTheory.condMutualInfo_eq'`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutualInfo_eq').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 282](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L282)
