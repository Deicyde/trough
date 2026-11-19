---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.exists_seven, MIPRE.Introspection.seven, MIPRE.Introspection.CompiledSoundness.output_soundness, MIPRE.Introspection.sevenConstant, MIPRE.Introspection.sevenConstant_spec, MIPRE.Introspection.one_le_sevenConstant, MIPRE.Introspection.sevenC, MIPRE.Introspection.sevenC_spec, MIPRE.Introspection.sevenOutput_soundness
statement: formalized
proof: formalized
---

# Supplying ambient introspection

The ambient contract `MIPRE.Introspection 7` is inhabited. The fixed instance `MIPRE.Introspection.seven` supplies the introspection input to the compression pipeline. It has one common all-index resource exponent and the required soundness profile, and handles the exceptional zero cases. Its scope is the ambient contract at $\ell=7$; Theorem [Introspection](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3993) separately states the source-model result for arbitrary fixed depth. The compiler is defined explicitly, its constants chosen once, and its soundness field is the $\mathrm{val}^*$ instance of a soundness theorem that holds in every value model in which the Pauli basis test is sound (Theorem [Introspection is sound in ${\omega^{\mathrm{co}}}$, given the Pauli basis test](../../downstream-results/part-04/thm-intro-sound-co.md)).

## Depends on

- [Ambient introspection contract](def-introspection-contract.md)
- [The ambient compiler's resources and raw-game bridge](lem-intro-ambient-kernel.md)
- [Full question transport and actual QLD extraction](lem-intro-numbered-transport.md)

## Proof depends on

- [Completeness of introspection](../part-02/lem-intro-completeness.md)
- [The Pauli basis test is sound in the tensor-product model](../../downstream-results/part-04/lem-qld-sound-in-tensor.md)

## Proof

Choose one even canonical parameter constant that absorbs the QLD field-size tails, and use the proved clocked universal machine. Combine the sampler, decider, cutoff and description estimates into one resource exponent. Encode the supported honest finite strategy to obtain ambient perfect PCC completeness, using the zero-index branch separately. For positive-index soundness, restrict to the enforced answer cutoff, detype, decode finite answers and apply actual QLD extraction followed by the source-game bound. Absorb the fixed detyping loss into the profile constants. These constructions fill every field of the ambient contract; their axiom audit contains only `propext`, `Classical.choice` and `Quot.sound`. For the cost model and the PCC representation they work in, see Remarks [Runtime normalization obligation](../README.md) and [Source PCC and the required representation bridge](../../foundations/README.md).

## Lean

Formalized as [`MIPRE.Introspection.exists_seven`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_seven), [`MIPRE.Introspection.seven`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.seven), [`MIPRE.Introspection.CompiledSoundness.output_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CompiledSoundness.output_soundness), [`MIPRE.Introspection.sevenConstant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sevenConstant), [`MIPRE.Introspection.sevenConstant_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sevenConstant_spec), [`MIPRE.Introspection.one_le_sevenConstant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.one_le_sevenConstant), [`MIPRE.Introspection.sevenC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sevenC), [`MIPRE.Introspection.sevenC_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sevenC_spec), [`MIPRE.Introspection.sevenOutput_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sevenOutput_soundness).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4068](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4068)
