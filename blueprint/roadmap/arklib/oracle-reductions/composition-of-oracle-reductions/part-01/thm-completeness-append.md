---
declaration: theorem
origin: cited
lean: Reduction.append_completeness_of_pure_verifiers
statement: formalized
---

# Completeness Preservation under Append

Let $R_1$ and $R_2$ have compatible input, intermediate, and output relations. Assume both verifiers are pure and total: each returns a deterministic function of its input statement and transcript, without oracle queries or rejection. Assume also that at least one of the following execution conditions holds:

- the first prover's output is a pure function of its final internal state;
- the second protocol is empty;
- the second protocol starts with a prover message.

Suppose $R_1$ is complete with error $\epsilon_1$ from $\mu$, and for every $s \in \Sigma$, $R_2$ is complete with error $\epsilon_2$ when initialized deterministically at $s$. Then $R_1.\mathsf{append}\ R_2$ is complete from $\mu$ with error $\epsilon_1 + \epsilon_2$.

## Depends on

- [Completeness](../../definitions/part-01/def-completeness.md)
- [Reduction Append](def-reduction-append.md)

## Lean

Stated as [`Reduction.append_completeness_of_pure_verifiers`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.append_completeness_of_pure_verifiers); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 127](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L127)
