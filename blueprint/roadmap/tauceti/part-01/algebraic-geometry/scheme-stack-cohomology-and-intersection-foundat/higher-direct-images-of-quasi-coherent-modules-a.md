---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage
statement: formalized
proof: formalized
---

# Higher direct images of quasi-coherent modules are quasi-coherent

For a quasi-compact
quasi-separated morphism `f : X ⟶ Y` and a quasi-coherent `𝒪_X`-module `M`, every higher direct
image `Rⁿ f_* M` is quasi-coherent.

```lean
AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage.{u} {X Y : AlgebraicGeometry.Scheme}
  (f : X ⟶ Y) [AlgebraicGeometry.QuasiCompact f] [AlgebraicGeometry.QuasiSeparated f]
  (M : X.Modules) [SheafOfModules.IsQuasicoherent M] (n : ℕ) :
  SheafOfModules.IsQuasicoherent ((AlgebraicGeometry.Scheme.Hom.higherDirectImage f n).obj M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/HigherDirectImage/Quasicoherent.html#AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/HigherDirectImage/Quasicoherent.html#AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage)
- [Source of `AlgebraicGeometry.Scheme.Hom.isQuasicoherent_higherDirectImage` in TauCeti/AlgebraicGeometry/Cohomology/HigherDirectImage/Quasicoherent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Cohomology/HigherDirectImage/Quasicoherent.lean#L170)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
