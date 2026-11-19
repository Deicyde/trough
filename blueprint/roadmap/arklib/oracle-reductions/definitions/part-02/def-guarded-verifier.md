---
declaration: definition
origin: cited
lean: Verifier.IsGuarded, Verifier.GuardedForm, Verifier.isGuarded_iff_isTotalQueryBound_zero
statement: formalized
---

# Guarded Verifier

A verifier is **guarded** if there are a Boolean check and a deterministic output map such that, on every statement and full transcript, it returns the output map's value when the check passes and aborts otherwise. Pure verifiers are the special case with the trivially true check. When the output statement type is nonempty, a verifier is guarded exactly when its verdict makes no query to the shared oracle. A *guarded form* carries the check and the output map as data.

## Depends on

- [Type Signature of a Verifier](../part-01/def-verifier.md)

## Lean

Formalized as [`Verifier.IsGuarded`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.IsGuarded), [`Verifier.GuardedForm`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.GuardedForm), [`Verifier.isGuarded_iff_isTotalQueryBound_zero`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.isGuarded_iff_isTotalQueryBound_zero).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 771](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L771)
