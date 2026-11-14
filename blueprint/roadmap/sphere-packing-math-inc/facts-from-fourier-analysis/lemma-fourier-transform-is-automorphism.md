---
declaration: lemma
origin: cited
lean: SchwartzMap.fourierTransformCLM
statement: formalized
proof: formalized
---

# Fourier-transform-is-automorphism

The Fourier transform is a continuous, linear automorphism of the space of Schwartz functions.

## Depends on

- [Fourier-Transform](def-fourier-transform.md)
- [Schwartz-Space](def-schwartz-space.md)

## Proof

We do not elaborate here as the result already exists in Mathlib. We do, however, mention that the Lean implementation *defines* a continuous linear equivalence on the Schwartz space *using* the Fourier transform (see `SchwartzMap.fourierTransformCLM`). The ‘proof’ that for any Schwartz function $f$, its Fourier transform and its image under this continuous linear equivalence are, indeed, the same $\mathbb{R}^d \to \mathbb{R}$ function, is stated in Mathlib solely for the purpose of `rw` and `simp` tactics, and is proven simply by `rfl`.

## Lean

Formalized as [`SchwartzMap.fourierTransformCLM`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SchwartzMap.fourierTransformCLM).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 32](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L32)
