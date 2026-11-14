---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.HonestChain.honest_zpc, MIPRE.Tailored.Intro.HonestChain.honest_zpc_ofTNFVT, MIPRE.Tailored.Intro.Output.completeness_contract
statement: formalized
proof: formalized
---

# The honest strategy is a perfect ZPC strategy

Let $W$ be a $\lambda$-bounded seven-level verifier and $n \geq 1$. A perfect PCC strategy of $W$ at $2^n$ whose answers at each question have the lengths a tailored verifier assigns to it, and whose answer bits are signed permutations, diagonal at the readable ones, gives the honest strategy of the reference verifier's typed game. That strategy is perfect and PCC, charges only answers of the layout whose readable conditions hold, and its bit observables along the layout are signed permutations, diagonal at the readable bits. A perfect ZPC strategy of a tailored input $V$ at $2^n$ gives such a strategy of its normal form verifier. Hence, for a $\lambda$-bounded tailored input whose normal form verifier is $C\lambda$-bounded, $C \geq 2$, with the output's programs meeting the specification at $C\lambda$: if $V$ has a perfect ZPC strategy at $2^n$, the output has one at $n$.

## Depends on

- [The output tailored verifier, from a specification of its programs](lem-intro-output.md)
- [Completeness of the tailored presentation of the introspection verifier](lem-intro-presentation-complete.md)
- [The bit observables of an encoded measurement](../part-03/lem-encoded-pvm-obs.md)
- [Weyl measurements are read out by signed permutations; II:2938](../part-03/lem-weyl-signed-perm.md)
- [Controlled signed permutations](../part-03/lem-controlled-signed-perm.md)
- [Binary measurements, the qubit Paulis and the Magic Square grid](../part-03/lem-binary-signed-perm.md)
- [The input strategy's answer bits](../part-03/lem-input-answer-bits.md)

## Proof

The honest strategy measures in the eigenbases of Weyl operators, in the computational basis, and by controlled sums over a control register; its answer bits are read out linearly or from the computational basis. Each of the three gives signed-permutation bit observables, diagonal for the computational-basis reads, which are the readable bits. The support condition is checked label by label. Then Lemma [The output tailored verifier, from a specification of its programs](lem-intro-output.md).

## Lean

Formalized as [`MIPRE.Tailored.Intro.HonestChain.honest_zpc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.HonestChain.honest_zpc), [`MIPRE.Tailored.Intro.HonestChain.honest_zpc_ofTNFVT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.HonestChain.honest_zpc_ofTNFVT), [`MIPRE.Tailored.Intro.Output.completeness_contract`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Output.completeness_contract).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1997](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1997)
