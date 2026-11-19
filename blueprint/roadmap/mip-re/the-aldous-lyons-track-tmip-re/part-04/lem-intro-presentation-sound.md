---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.Sound.tdata, MIPRE.Tailored.Intro.Sound.decT, MIPRE.Tailored.Intro.Sound.lenR_le_len, MIPRE.Tailored.Intro.Sound.guards_of_readOK, MIPRE.Tailored.Intro.Sound.pauliFormatted_parsedT, MIPRE.Tailored.Intro.Sound.tdata_sound, MIPRE.Tailored.Intro.Sound.H, MIPRE.Tailored.Intro.Sound.valStar_tpresented_le
statement: formalized
proof: formalized
---

# Soundness of the tailored presentation of the introspection verifier

At the introspection verifier's canonical parameters, on every edge of its type graph, a pair of answers the typed tailored data accepts decodes — through the parsed answers read off the layout, re-encoded as the kernel's bytes — to a pair the reference verifier's typed predicate accepts. Hence the detyped tailored game has $\mathrm{val}^*$ at most the quantum value of the reference verifier's detyped game.

## Depends on

- [The typed tailored data of the introspection verifier](lem-intro-typed-cons.md)
- [Presenting a detyped game by a detyped tailored game](lem-presentation.md)
- [Typed sampler and its distribution](../../structure-of-the-proof/part-01/def-typed-sampler-interface.md)
- [The ambient compiler's resources and raw-game bridge](../../structure-of-the-proof/part-06/lem-intro-ambient-kernel.md)
- [The canonical sampler at every index](../../structure-of-the-proof/part-06/lem-intro-canonical-sampler.md)
- [The executable five-level introspection sampler](../../structure-of-the-proof/part-02/lem-intro-executable-sampler.md)
- [Executable quotient hiding and the finite decision kernel](../../structure-of-the-proof/part-06/lem-intro-quotient-kernel.md)
- [Introspection type graph and typed CL family](../../structure-of-the-proof/part-02/lem-intro-type-presentation.md)

## Proof

By Lemma [The typed tailored data of the introspection verifier](lem-intro-typed-cons.md) the readable conditions hold and the kernel's semantic check accepts the parsed answers. The readable conditions are the kernel's prefix guard and source-output condition, and parsed Pauli answers are formatted, so the kernel's completeness gives acceptance by the kernel program on the re-encoded answers, which is the typed predicate.

## Lean

Formalized as [`MIPRE.Tailored.Intro.Sound.tdata`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.tdata), [`MIPRE.Tailored.Intro.Sound.decT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.decT), [`MIPRE.Tailored.Intro.Sound.lenR_le_len`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.lenR_le_len), [`MIPRE.Tailored.Intro.Sound.guards_of_readOK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.guards_of_readOK), [`MIPRE.Tailored.Intro.Sound.pauliFormatted_parsedT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.pauliFormatted_parsedT), [`MIPRE.Tailored.Intro.Sound.tdata_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.tdata_sound), [`MIPRE.Tailored.Intro.Sound.H`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.H), [`MIPRE.Tailored.Intro.Sound.valStar_tpresented_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Sound.valStar_tpresented_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1893](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1893)
