---
declaration: theorem
origin: cited
lean: Fri.FoldTrace.query_soundness_distance
statement: formalized
proof: formalized
---

# fri-query-error

Fix a commitment trace with no bad folding challenge and let $\delta$ be the initial word's relative distance from its Reed–Solomon code. The probability of acceptance on $t$ independent uniform initial-domain queries is at most $(1-\min\{\theta,\delta\})^t$.

## Depends on

- [fri-folding-failure](def-fri-folding-failure.md)

## Proof

If the final word is not in its code, acceptance is impossible. Otherwise any set of accepting initial positions of density at least $1-\theta$ agrees with one original codeword: project the positions through each fold, observe that density cannot decrease, and lift agreement backwards. Thus the accepting density is at most $1-\min\{\theta,\delta\}$. Independent repetitions raise this density to the $t$th power.

## Lean

Formalized as [`Fri.FoldTrace.query_soundness_distance`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldTrace.query_soundness_distance).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 58](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L58)
