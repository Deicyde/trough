---
declaration: theorem
origin: cited
lean: RingSwitching.Packing.RingSwitch.append_rbrKnowledgeSoundness, RingSwitching.Packing.RingSwitch.append_rbrError_sum
statement: formalized
---

# Closing a contextual opening

For the shared protocol, let $P$ and $E$ be the packing and opening algebras of packing data over a commutative base ring $B$. Let $C$ be a finite commutative ring with its uniform sampler, compatible $B$- and $P$-algebra structures, and the scalar-tower law for $B \to P \to C$. Assume $C$ has no zero divisors, coefficient transport $P \to C$ is injective, oracle compatibility is functional, and the batching rule has a separation certificate with error $\varepsilon_{\mathrm{batch}}$. Let an opening already be typed at the contextual evaluation relation for the same committed polynomial. Suppose it is round-by-round knowledge sound for all inputs in that relation and every fixed transcript prefix, with challenge-error function $\varepsilon_{\mathrm{open}}$. Then its composition with the shared protocol is round-by-round knowledge sound, with the appended component-error functions and total challenge error

$$
\varepsilon_{\mathrm{batch}} + \frac{2m}{\lvert C\rvert}
+ \sum_j \varepsilon_{\mathrm{open}}(j),
$$

where $m$ is the number of retained variables. There is no required map $E \to C$. Compatibility and functionality do not assert honest coverage. In the DP24 instance, $P = E = C = L$, $m = \ell'$ and $\varepsilon_{\mathrm{batch}} = \kappa/\lvert L\rvert$.

## Depends on

- [Round-by-round knowledge soundness of the prefix protocol](thm-ring-switching-core-soundness.md)
- [Round-by-Round Knowledge Soundness under a Guarded First Verifier](../../oracle-reductions/composition-of-oracle-reductions/part-01/thm-rbr-knowledge-soundness-append-guarded.md)

## Lean

Stated as [`RingSwitching.Packing.RingSwitch.append_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.RingSwitch.append_rbrKnowledgeSoundness), [`RingSwitching.Packing.RingSwitch.append_rbrError_sum`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.RingSwitch.append_rbrError_sum); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 213](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L213)
