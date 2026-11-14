---
declaration: definition
origin: cited
lean: MIPRE.LIDT.Simul.SoundIn, MIPRE.LIDT.Simul.SoundCo, MIPRE.LIDT.Simul.tuplePOVMAIn, MIPRE.LIDT.Simul.tuplePOVMBIn, MIPRE.LIDT.Simul.evalTuplePOVMIn, MIPRE.LIDT.Simul.ApproxSoundIn
statement: formalized
---

# The low-individual-degree test is sound in a model

The seeded CL test is *sound in the bipartite model* if the conclusion of Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md) holds for the projective strategies in the model, with the extracted measurements in the players' algebras: for $q = 2^k$, $m \mid q$ and $d, \mathrm{ldc} \geq 1$, every projective strategy in the model passing the seeded test with $\mathrm{ldc}$ codewords with probability at least $1 - \varepsilon$ admits projective measurements $G^\textsc{A}$ in the first player's algebra and $G^\textsc{B}$ in the second's, of tuples of polynomials of individual degree at most $d$, whose evaluations at a uniform point are consistent with the other player's point measurement, and which are consistent with each other, all with error at most $\delta_{\mathrm{CL}}(\varepsilon, q, m, d, \mathrm{ldc})$. It is *sound in the commuting-operator model* if it is sound in the model of every commuting-operator strategy (Definition [Bipartite model](../part-02/def-bipartite-model.md)). A value model $\omega$ is *approached in models where the test is sound* if for every game $\mathfrak{G}$ and every $0 \leq t < \omega(\mathfrak{G})$ there is a projective strategy for $\mathfrak{G}$ of value greater than $t$ in a bipartite model on a Hilbert space in which the test is sound and which $\omega$ dominates.

## Depends on

- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)
- [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)
- [The padded multi-codeword game adapter](../../background-results/part-01/lem-lidt-ldc-adapter.md)
- [Absorbing the simultaneous reduction's error](../../background-results/part-01/lem-lidt-ldc-error.md)

## Lean

Formalized as [`MIPRE.LIDT.Simul.SoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundIn), [`MIPRE.LIDT.Simul.SoundCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundCo), [`MIPRE.LIDT.Simul.tuplePOVMAIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMAIn), [`MIPRE.LIDT.Simul.tuplePOVMBIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMBIn), [`MIPRE.LIDT.Simul.evalTuplePOVMIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.evalTuplePOVMIn), [`MIPRE.LIDT.Simul.ApproxSoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.ApproxSoundIn).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1681](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1681)
