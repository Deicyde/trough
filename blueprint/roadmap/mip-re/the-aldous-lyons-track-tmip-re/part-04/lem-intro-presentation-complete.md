---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.Complete.parsedT_enc, MIPRE.Tailored.Intro.Complete.length_encL, MIPRE.Tailored.Intro.Complete.encT, MIPRE.Tailored.Intro.Complete.okT, MIPRE.Tailored.Intro.Complete.tdata_complete, MIPRE.Tailored.Intro.Complete.hasPerfectZPC_tpresented
statement: formalized
proof: formalized
---

# Completeness of the tailored presentation of the introspection verifier

The parsed answer read off the layout's encoding of a well-formed byte answer is the kernel's decoding of it. Hence, on every edge, when the reference verifier's typed predicate accepts two well-formed byte answers whose encodings satisfy the readable conditions, the typed tailored data accepts the encodings; and a perfect PCC strategy of the reference verifier's typed game charging only such answers, with signed-permutation bit observables along the encoding, diagonal at the readable bits, gives a perfect ZPC strategy of the doubled detyped tailored game.

## Depends on

- [Soundness of the tailored presentation of the introspection verifier](lem-intro-presentation-sound.md)
- [Completeness of a presentation from a typed strategy](lem-presentation-typed.md)
- [The padded answer layout of question reduction](def-intro-layout.md)
- [The layout's round trip and lengths](lem-intro-layout.md)
- [Typed sampler and its distribution](../../structure-of-the-proof/part-01/def-typed-sampler-interface.md)
- [The ambient compiler's resources and raw-game bridge](../../structure-of-the-proof/part-06/lem-intro-ambient-kernel.md)
- [The canonical sampler at every index](../../structure-of-the-proof/part-06/lem-intro-canonical-sampler.md)
- [The executable five-level introspection sampler](../../structure-of-the-proof/part-02/lem-intro-executable-sampler.md)
- [Executable quotient hiding and the finite decision kernel](../../structure-of-the-proof/part-06/lem-intro-quotient-kernel.md)
- [Introspection type graph and typed CL family](../../structure-of-the-proof/part-02/lem-intro-type-presentation.md)

## Proof

The kernel's soundness turns acceptance by the kernel program into its semantic check on the decoded answers, which are the parsed encodings; Lemma [The typed tailored data of the introspection verifier](lem-intro-typed-cons.md) turns that into the constraints. The rest is Lemma [Completeness of a presentation from a typed strategy](lem-presentation-typed.md).

## Lean

Formalized as [`MIPRE.Tailored.Intro.Complete.parsedT_enc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.parsedT_enc), [`MIPRE.Tailored.Intro.Complete.length_encL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.length_encL), [`MIPRE.Tailored.Intro.Complete.encT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.encT), [`MIPRE.Tailored.Intro.Complete.okT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.okT), [`MIPRE.Tailored.Intro.Complete.tdata_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.tdata_complete), [`MIPRE.Tailored.Intro.Complete.hasPerfectZPC_tpresented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Complete.hasPerfectZPC_tpresented).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1918](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1918)
