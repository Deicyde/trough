---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.kernelGens, MIPRE.Tailored.Intro.kernelGens_correct, MIPRE.Tailored.Intro.linRows, MIPRE.Tailored.Intro.regKerGens, MIPRE.Tailored.Intro.kerGens_regKerGens
statement: formalized
proof: formalized
---

# Kernel generators of a register-local linear map

The binary kernel program, run on the rows of the matrix of a register-local linear map, outputs vectors in its kernel that span it. So it provides the kernel generators the hiding comparisons need.

## Depends on

- [The auxiliary checks as linear constraints](lem-intro-aux-cons.md)

## Proof

The program's correctness, read in the sampler's encoding of vectors.

## Lean

Formalized as [`MIPRE.Tailored.Intro.kernelGens`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.kernelGens), [`MIPRE.Tailored.Intro.kernelGens_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.kernelGens_correct), [`MIPRE.Tailored.Intro.linRows`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.linRows), [`MIPRE.Tailored.Intro.regKerGens`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.regKerGens), [`MIPRE.Tailored.Intro.kerGens_regKerGens`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.kerGens_regKerGens).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1943](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1943)
