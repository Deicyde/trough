---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsUniform.entropy_eq
statement: formalized
proof: formalized
---

# Entropy of uniform random variable

If $X$ is $S$-valued random variable, then $\mathbb{H}[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.

## Depends on

- [Entropy](entropy-def.md)

## Proof depends on

- [Concavity](../../applications-of-jensens-inequality/concave.md)

## Proof

Direct computation in one direction. Converse direction needs the strict Jensen inequality and [Concavity](../../applications-of-jensens-inequality/concave.md).

## Lean

Formalized as [`ProbabilityTheory.IsUniform.entropy_eq`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.IsUniform.entropy_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 52](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L52)
