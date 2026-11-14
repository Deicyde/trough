---
declaration: lemma
origin: cited
lean: Groups.not_tSdhAssumption_univ
statement: formalized
---

# The assumption needs a restricted class

If $g_2\neq 1$ and $\varepsilon<1$, the $t$-SDH assumption fails over the class of all adversaries: a classical inverse of $a\mapsto g_2^{a}$ recovers $\tau$ from the reference string. A meaningful instance restricts $\mathcal{A}$, for example to generic, algebraic or resource-bounded adversaries.

## Depends on

- [$t$-SDH](def-tsdh.md)

## Lean

Stated as [`Groups.not_tSdhAssumption_univ`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.not_tSdhAssumption_univ); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: commitments/kzg.tex, line 45](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/kzg.tex#L45)
