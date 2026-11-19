---
declaration: definition
origin: cited
lean: Plonk.Assembly.oracleReduction, Plonk.Assembly.rel, Plonk.GrandProduct.InputRelation
statement: formalized
---

# Plonk oracle reduction

The input relation holds for a wire table when the gate polynomial built from the table and $\mathit{pi}$ vanishes on $H$, and the wire values satisfy every copy constraint. The reduction is the sequential composition of four stages, with six rounds in total.

1. **Wire reveal.** The prover sends the wire table as one polynomial oracle.
2. **Grand product.** The verifier sends the permutation challenges $(\beta,\gamma)$ jointly. The prover replies with the accumulator polynomial $Z$. The output claim is that three residual polynomials vanish on $H$.
3. **Power batch.** The verifier sends one challenge $\alpha$ and the three residuals are combined with coefficients $1,\alpha,\alpha^2$ (Definition [Generator Batching](../simple-oracle-reductions/part-01/def-generator-batch.md)).
4. **Quotient.** The prover sends the quotient polynomial and the verifier checks the quotient identity at a random point (Definition [Quotient Zero Test](../simple-oracle-reductions/part-01/def-quotient-zero-test.md)). The output relation accepts every output.

Every earlier oracle is retained up to the terminal check.

## Depends on

- [SendSingleWitness Oracle Reduction](../simple-oracle-reductions/part-01/def-sendsinglewitness-oracle-reduction.md)
- [Generator Batching](../simple-oracle-reductions/part-01/def-generator-batch.md)
- [Quotient Zero Test](../simple-oracle-reductions/part-01/def-quotient-zero-test.md)

## Lean

Formalized as [`Plonk.Assembly.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.oracleReduction), [`Plonk.Assembly.rel`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.Assembly.rel), [`Plonk.GrandProduct.InputRelation`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Plonk.GrandProduct.InputRelation).

## Sources

- [ArkLib blueprint: proof_systems/plonk.tex, line 18](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/plonk.tex#L18)
