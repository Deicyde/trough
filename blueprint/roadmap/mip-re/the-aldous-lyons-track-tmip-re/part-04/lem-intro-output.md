---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.Output.quantumValue_H, MIPRE.Tailored.Intro.Output.valStar_presented_le_output, MIPRE.Tailored.Intro.Output.outTV, MIPRE.Tailored.Intro.Output.qe, MIPRE.Tailored.Intro.Output.IntroSpec, MIPRE.Tailored.Intro.Output.lenOf_eq_of, MIPRE.Tailored.Intro.Output.extends_presented, MIPRE.Tailored.Intro.Output.valStar_outTV_le, MIPRE.Tailored.Intro.Output.soundness_seven, MIPRE.Tailored.Intro.Output.hasPerfectZPC_outTV, MIPRE.Tailored.Intro.Output.acceptsAsInput_ofTNFVT, MIPRE.Tailored.Intro.Output.delta_mul_le, MIPRE.Tailored.Intro.Output.lenOf_le_of_isBounded, MIPRE.Tailored.Intro.Output.maxLen_le_of_isBounded, MIPRE.Tailored.Intro.Output.soundness_contract
statement: formalized
proof: formalized
---

# The output tailored verifier, from a specification of its programs

Give the output tailored verifier at $\lambda$ the sampler of the introspection verifier and two programs which, at index $n$, output at every detyped question the presented game's lengths and at every pair its constraints. Then its $n$-th game extends the presented one, so it has the presented game's $\mathrm{val}^*$, which is at most the value of the introspection verifier's output on the input's normal form verifier; and a perfect strategy of the reference verifier's typed game meeting the conditions of Lemma [Completeness of the tailored presentation of the introspection verifier](lem-intro-presentation-complete.md) gives it a perfect ZPC strategy. For a $\lambda$-bounded tailored input whose normal form verifier is $C\lambda$-bounded, $C \geq 2$, with the programs meeting the specification at $C\lambda$: $\mathrm{val}^*$ of the output at $n \geq 1$ above $1 - \varepsilon$ gives $\mathrm{val}^*$ of the input at $2^n$ at least $1 - \delta(aC^a, b, \lambda, n, \varepsilon)$, with the introspection verifier's $a$ and $b$.

## Depends on

- [Soundness of the tailored presentation of the introspection verifier](lem-intro-presentation-sound.md)
- [Completeness of the tailored presentation of the introspection verifier](lem-intro-presentation-complete.md)
- [A tailored verifier as a bounded normal form verifier](lem-of-tnfvt.md)
- [Theorem Pauli basis test / quantum low individual degree test on the valid answers](../../background-results/part-02/cor-qld-valid.md)
- [Introspection soundness from the extracted Pauli strategy](../../structure-of-the-proof/part-05/lem-intro-extracted-soundness.md)
- [Supplying ambient introspection](../../structure-of-the-proof/part-06/lem-introspection-supply.md)
- [Domination and approximation in the two models](../../downstream-results/part-03/lem-povm-domination.md)
- [The Pauli basis test is sound in the tensor-product model](../../downstream-results/part-04/lem-qld-sound-in-tensor.md)
- [Extending a tailored game along its questions](../part-02/lem-tailored-extend.md)
- [A presentation of a game without weight on its loops](../part-02/lem-tailored-presents.md)

## Proof

The detyped game is the reference verifier's along the numbering of the detyped registers, and the reference verifier has the value of the introspection verifier's output. Its soundness at $C\lambda$, the identification of the input's normal form verifier's value with the input's, and $\delta(a, b, C\lambda, n, \varepsilon) \le \delta(aC^a, b, \lambda, n, \varepsilon)$ for $a \geq 1$, $C \geq 1$ and $\lambda n \geq 1$.

## Lean

Formalized as [`MIPRE.Tailored.Intro.Output.quantumValue_H`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.quantumValue_H), [`MIPRE.Tailored.Intro.Output.valStar_presented_le_output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.valStar_presented_le_output), [`MIPRE.Tailored.Intro.Output.outTV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.outTV), [`MIPRE.Tailored.Intro.Output.qe`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.qe), [`MIPRE.Tailored.Intro.Output.IntroSpec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.IntroSpec), [`MIPRE.Tailored.Intro.Output.lenOf_eq_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.lenOf_eq_of), [`MIPRE.Tailored.Intro.Output.extends_presented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.extends_presented), [`MIPRE.Tailored.Intro.Output.valStar_outTV_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.valStar_outTV_le), [`MIPRE.Tailored.Intro.Output.soundness_seven`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.soundness_seven), [`MIPRE.Tailored.Intro.Output.hasPerfectZPC_outTV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.hasPerfectZPC_outTV), [`MIPRE.Tailored.Intro.Output.acceptsAsInput_ofTNFVT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.acceptsAsInput_ofTNFVT), [`MIPRE.Tailored.Intro.Output.delta_mul_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.delta_mul_le), [`MIPRE.Tailored.Intro.Output.lenOf_le_of_isBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.lenOf_le_of_isBounded), [`MIPRE.Tailored.Intro.Output.maxLen_le_of_isBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.maxLen_le_of_isBounded), [`MIPRE.Tailored.Intro.Output.soundness_contract`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.soundness_contract).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1960](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1960)
