---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ldBits, MIPRE.Tailored.AnsRed.Typed.arQr, MIPRE.Tailored.AnsRed.Typed.ldq, MIPRE.Tailored.AnsRed.Typed.oq, MIPRE.Tailored.AnsRed.Typed.roleStrat, MIPRE.Tailored.AnsRed.Typed.edgeFail
statement: formalized
---

# The per-role low-degree strategies

At the seed $(z, w) \in Z \times W$, the typed question of type $(r, \tau)$ carries the oracularized input question $y_r(z)$ of the role $r$ at $z$ and the seeded test's question of type $\tau$ of the sample the registers $w$ carry. The per-role strategy of $T$ at a role $r$ and an oracularized question $y$ is the strategy for the seeded low-degree test, with one codeword per slot of the role, that plays $T$ at the typed questions carrying $y$ and reads the role's codewords off its answers. The failure of $T$ at a pair of types and a seed is its failure at the two typed questions they determine.

## Depends on

- [The honest strategy of the answer-reduced game](def-ar-honest-strategy.md)
- [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ldBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldBits), [`MIPRE.Tailored.AnsRed.Typed.arQr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arQr), [`MIPRE.Tailored.AnsRed.Typed.ldq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldq), [`MIPRE.Tailored.AnsRed.Typed.oq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.oq), [`MIPRE.Tailored.AnsRed.Typed.roleStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.roleStrat), [`MIPRE.Tailored.AnsRed.Typed.edgeFail`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.edgeFail).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3133](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3133)
