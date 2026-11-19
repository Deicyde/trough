---
declaration: theorem
origin: cited
lean: fiatShamir_perfectCompleteness, fiatShamir_completeness_randomOracle
statement: formalized
proof: formalized
---

# Fiat-Shamir Preserves Completeness

If an interactive reduction $R$ has perfect completeness, its Fiat–Shamir transform has perfect completeness for every fixed challenge table.

If $R$ has completeness error $\epsilon$, its Fiat–Shamir transform has completeness error $\epsilon$ when the challenge oracle is a lazily sampled random oracle shared by prover and verifier, starting from an empty cache. This needs only decidable equality of the oracle's query type. Both claims use the same input and output relations as $R$.

## Depends on

- [Fiat-Shamir Reduction Transformation](def-reduction-fiat-shamir.md)

## Proof

Each uniform interactive challenge has full support, so every honest transformed execution is an interactive branch, and verifier reconstruction replays exactly that branch. For the random oracle, the honest prover's queries are at distinct round indices and hence fresh, and reconstruction reads the cached answers.

## Lean

Formalized as [`fiatShamir_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/fiatShamir_perfectCompleteness), [`fiatShamir_completeness_randomOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/fiatShamir_completeness_randomOracle).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 136](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L136)
