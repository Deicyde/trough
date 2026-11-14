---
declaration: definition
origin: cited
lean: MIPRE.GapCompression.Sound, MIPRE.GapCompression.sound_tensor
statement: formalized
---

# Soundness of compression in a value model

A gap compression (an inhabitant of `MIPRE.GapCompression`) is *sound in the value model $\omega$* if for every $\lambda$-bounded verifier $\mathsf{V}$ and every $n \geq C_0$,

$$
\omega(\mathsf{V}_{2^n}) \leq \tfrac12 \ \Longrightarrow\
\omega(\mathsf{V}^{\mathrm{compr}}_n) \leq \tfrac12 ,
$$

at the answer bounds of the soundness clause of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md). That clause is soundness in the model $\mathrm{val}^*$. Soundness in the model ${\omega^{\mathrm{co}}}$ — the *commuting-operator soundness of compression* — is the model-$co$ case of the soundness clause of Lin's gap compression theorem (Lin25), and the one hypothesis of Theorems [Halting reduces to the commuting-operator value, from co-soundness](../part-02/thm-halting-co.md) and [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness](../part-02/thm-mipco-eq-core.md). No completeness clause in the commuting-operator model is asked for. It holds for the compression of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) (Theorem [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$](../part-07/thm-mipco-eq-core-unconditional.md)).

## Depends on

- [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md)
- [Value models](def-value-model.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)

## Lean

Formalized as [`MIPRE.GapCompression.Sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.Sound), [`MIPRE.GapCompression.sound_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.sound_tensor).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 827](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L827)
