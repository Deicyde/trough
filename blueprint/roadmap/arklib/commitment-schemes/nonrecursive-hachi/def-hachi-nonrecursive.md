---
declaration: definition
origin: cited
lean: ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive, ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening, ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete, ArkLib.Lattices.Ajtai.InnerOuter.nonrecursiveLiftCom
statement: formalized
---

# Nonrecursive Hachi

Key generation samples the public matrices of the inner-outer Ajtai commitment. The committer decomposes the coefficients in balanced base $b$ and commits with the inner and outer matrices. The opening proves an evaluation claim through the chain: input adapter, bridge, quadratic evaluation, ring switching to a linear relation, lift, batching, nested zero-check and sumcheck. A terminal step closes the chain: the prover sends the lifted witness in the clear and the verifier checks the reduced evaluation claim on it. The opening is therefore not succinct. The scheme is generic in the commitment used by the lift step. The concrete instance commits to the lifted witness with an Ajtai matrix of $\mu_0+n_0\lceil\log_{b_0}q\rceil$ columns, whose quotient block is decomposed in base $b_0$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursive), [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveOpening), [`ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachiNonrecursiveConcrete), [`ArkLib.Lattices.Ajtai.InnerOuter.nonrecursiveLiftCom`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.nonrecursiveLiftCom).

## Sources

- [ArkLib blueprint: commitments/hachi.tex, line 26](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/hachi.tex#L26)
