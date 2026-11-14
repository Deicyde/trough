---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.Ajtai.InnerOuter.iteration, ArkLib.Lattices.Ajtai.InnerOuter.hachi_iteration_coordinateWiseSpecialSoundWithEscape, ArkLib.Lattices.Ajtai.InnerOuter.evaluation
statement: formalized
---

# Special soundness of one Hachi iteration

Assume $q\equiv 5\pmod 8$, $(2\omega)^2\lt q$, $\tau>0$, $2^\alpha>0$, $b-1\leq\gamma$, $1\lt b\leq q/2$, $\lfloor b/2\rfloor\leq\gamma$, $(\mu_0+n_0\lceil\log_b q\rceil)\cdot 2^{\alpha}\leq 2^{m_0}$ and $n_0\leq 2^{m_1}$. Then the verifier of one iteration, from the bridge through the final sumcheck evaluation, is coordinate-wise special sound with escape, from the polynomial-evaluation relation to the reduced evaluation claim on the committed table. Appending the terminal check gives the complete evaluation argument with the composed certificate.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`ArkLib.Lattices.Ajtai.InnerOuter.iteration`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.iteration), [`ArkLib.Lattices.Ajtai.InnerOuter.hachi_iteration_coordinateWiseSpecialSoundWithEscape`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.hachi_iteration_coordinateWiseSpecialSoundWithEscape), [`ArkLib.Lattices.Ajtai.InnerOuter.evaluation`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.Ajtai.InnerOuter.evaluation); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: commitments/hachi.tex, line 74](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/hachi.tex#L74)
