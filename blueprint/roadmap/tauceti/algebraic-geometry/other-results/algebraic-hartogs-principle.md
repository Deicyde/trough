---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_isWeaklyRegular
statement: formalized
proof: formalized
---

# Algebraic Hartogs principle

Let `a, b` be a weakly `M`-regular sequence. If `D(a)` and
`D(b)` lie in the open subset `U` of `Spec R`, then `M → M~(U)` is bijective: every section of `M~`
over `U` comes from a unique element of `M`.

```lean
TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_isWeaklyRegular.{u} {R M : Type u}
  [CommRing R] [AddCommGroup M] [_root_.Module R M]
  {U : TopologicalSpace.Opens ↑(AlgebraicGeometry.PrimeSpectrum.Top R)} {a b : R}
  (h : RingTheory.Sequence.IsWeaklyRegular M [a, b]) (haU : PrimeSpectrum.basicOpen a ≤ U)
  (hbU : PrimeSpectrum.basicOpen b ≤ U) :
  Function.Bijective ⇑(AlgebraicGeometry.StructureSheaf.toOpenₗ R M U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_isWeaklyRegular`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.html#TauCeti.AlgebraicGeometry.StructureSheaf.toOpen%E2%82%97_bijective_of_isWeaklyRegular).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_isWeaklyRegular`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.html#TauCeti.AlgebraicGeometry.StructureSheaf.toOpen%E2%82%97_bijective_of_isWeaklyRegular)
- [Source of `TauCeti.AlgebraicGeometry.StructureSheaf.toOpenₗ_bijective_of_isWeaklyRegular` in TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Modules/Tilde/Hartogs.lean#L131)
