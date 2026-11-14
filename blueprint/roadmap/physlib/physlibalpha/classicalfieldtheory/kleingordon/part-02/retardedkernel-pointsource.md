---
declaration: module
origin: cited
lean: KleinGordon.retardedPointSource_eq_kernel_translate, KleinGordon.tendsto_fourierPairing_translate
statement: formalized
proof: formalized
---

# The boundary value formula for point sources

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.PointSource`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean): 2 declarations, 2 with a docstring.

> The retarded response of a point source at `p` is the boundary value of the resolvent pairing of
> the translated test function.

## i. Overview

> By transposition the retarded response of a compactly supported distribution `T` tested against `f`
> is `T` applied to the advanced solution of `f` (`retardedDistribution_apply`). For a point source
> at `p` the advanced solution of `f` at `p` is the retarded kernel applied to the translate of `f`.
> The boundary value formula for the kernel (`tendsto_fourierPairing`) then holds for the translate.
> This gives the formula for every finite combination of point sources.

## ii. Key results

> - `retardedPointSource_eq_kernel_translate` : the point source at `p` is the kernel at the origin
>   applied to the translate.
> - `tendsto_fourierPairing_translate` : the retarded response of a point source at `p` is the
>   boundary value of the resolvent pairing of the translate.

## iv. References

> None.

## A. Translation

> - `retardedPointSource_eq_kernel_translate` : the point source at `p` as a translate.

## B. The boundary value

> - `tendsto_fourierPairing_translate` : the boundary value for a point source at `p`.

**`KleinGordon.retardedPointSource_eq_kernel_translate`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean#L65).

> The retarded point source at `p` is the retarded kernel at the origin applied to the
> translate.

```lean
lemma retardedPointSource_eq_kernel_translate (m : ℝ) (p : SpaceTime d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    retardedPointSource m p φ =
      retardedPointSource m (0 : SpaceTime d) (precompTranslationCLM p φ)
```

**`KleinGordon.tendsto_fourierPairing_translate`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean#L81).

> **The boundary value formula for a point source.** The retarded response of the point source
> at `p` tested against `φ` is the limit for `ε → 0+` of the resolvent pairing of the translate of
> `φ`. By transposition this is the response of the distribution `δ_p`.

```lean
lemma tendsto_fourierPairing_translate (m : ℝ) (p : SpaceTime d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    Filter.Tendsto (fun ε : ℝ =>
      (fourierPairing (m ^ 2) ε (ofTestFunction (precompTranslationCLM p φ))).re)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds (retardedDistribution m (deltaCompact p) φ))
```

## Depends on

- [Poincaré covariance for distributional sources](covariance-distributions.md)
- [The Fourier form of the tempered retarded kernel](retardedkernel-fourierform.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/PointSource.lean)
