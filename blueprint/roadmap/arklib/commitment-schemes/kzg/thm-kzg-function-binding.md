---
declaration: theorem
origin: cited
lean: Groups.arsdhCondition, Groups.arsdhAssumption, KZG.CommitmentScheme.function_binding_reduces_to_arsdh, KZG.CommitmentScheme.function_binding
statement: formalized
---

# KZG function binding

An ARSDH adversary receives the same reference string and outputs a set $S\subseteq\mathbb{Z}_p$ and $h_1,h_2\in G_1$. With $Z_S(X)=\prod_{s\in S}(X-s)$, it wins when $|S|=n+1$, $Z_S(\tau)\neq 0$, $h_1\neq 1$ and $h_2=h_1^{1/Z_S(\tau)}$. A function-binding adversary outputs a commitment and $L$ query-value pairs, and wins when every opening is accepted but no polynomial of degree at most $n$ takes all $L$ values. Assume $n\geq 1$, $p\geq n+2$, $g_1\neq 1$ and $e(g_1,g_2)\neq 1_{G_T}$. Then every function-binding adversary wins with probability at most the ARSDH success probability of an explicit reduction, and at most $\varepsilon$ when ARSDH holds with error $\varepsilon$ over a class containing that reduction.

## Depends on

- [KZG commitment scheme](def-kzg.md)

## Lean

Stated as [`Groups.arsdhCondition`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.arsdhCondition), [`Groups.arsdhAssumption`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Groups.arsdhAssumption), [`KZG.CommitmentScheme.function_binding_reduces_to_arsdh`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.function_binding_reduces_to_arsdh), [`KZG.CommitmentScheme.function_binding`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.function_binding); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: commitments/kzg.tex, line 70](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/kzg.tex#L70)
