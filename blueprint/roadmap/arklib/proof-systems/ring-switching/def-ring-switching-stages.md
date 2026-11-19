---
declaration: definition
origin: cited
lean: RingSwitching.Packing.Head.reduction, RingSwitching.Packing.TensorPrefix.head_verifier_eq, RingSwitching.Packing.ProductSumcheck.reduction
statement: formalized
---

# Stages of the ring-switching reduction

The reduction runs the following stages.

1. **Batching**. The prover sends the folded element $\hat s \in A$. The verifier checks the original claim against its column decomposition, $s = \sum_v \tilde{\mathrm{eq}}(v, r_{0..\kappa-1})\cdot \mathrm{decomposeColumns}(\hat s)_v$, then samples a batching challenge $r'' \in L^\kappa$, producing the target $s_0 = \sum_u \tilde{\mathrm{eq}}(u, r'')\cdot \mathrm{decomposeRows}(\hat s)_u$. Its certified batching loss is $\kappa/\lvert L\rvert$.
2. **Sum-check**. A degree-$2$ sum-check on the product of the public multilinear multiplier and $t'$ runs for $\ell'$ challenges, followed by a terminal message and check. Each challenge contributes $2/\lvert L\rvert$; the terminal check sends no challenge. Its accepted output is the contextual evaluation claim about the same $t'$ and oracle family.
3. **Opening**. The concrete Binius construction appends the Binary Basefold contextual opening. Its existing zero-message frontier formats the evaluation claim and may discard the query context; it does not insert another wire phase or change the committed polynomial.

## Depends on

- [Ring-switching profile](def-ring-switching-profile.md)
- [Multilinear packing](def-pack-mle.md)

## Lean

Formalized as [`RingSwitching.Packing.Head.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.Head.reduction), [`RingSwitching.Packing.TensorPrefix.head_verifier_eq`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.TensorPrefix.head_verifier_eq), [`RingSwitching.Packing.ProductSumcheck.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.ProductSumcheck.reduction).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 126](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L126)
