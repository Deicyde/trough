---
declaration: lemma
origin: cited
lean: ProbabilityTheory.entropy_le_log_card, ProbabilityTheory.entropy_le_log_card_of_mem
statement: formalized
proof: formalized
---

# Jensen bound

If $X$ is an $S$-valued random variable, then $\mathbb{H}[X] \leq \log |S|$.

## Depends on

- [Entropy](entropy-def.md)

## Proof depends on

- [Concavity](../../applications-of-jensens-inequality/concave.md)

## Proof

This is a direct consequence of [Concavity](../../applications-of-jensens-inequality/concave.md) and Jensen's inequality.

## Lean

Formalized as [`ProbabilityTheory.entropy_le_log_card`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_le_log_card), [`ProbabilityTheory.entropy_le_log_card_of_mem`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_le_log_card_of_mem).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 24](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L24)
