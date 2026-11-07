---
declaration: def
origin: cited
lean: TauCeti.Huber.Pair.finiteAlgebra.homEquiv
statement: formalized
---

# Morphisms out of the Huber pair of a finite algebra

Morphisms of Huber pairs
`(B, B⁺) → (D, D⁺)` under `(A, A⁺)` are exactly the `A`-algebra maps `B → D`.

```lean
TauCeti.Huber.Pair.finiteAlgebra.homEquiv.{u_1, u_2, u_3} {A : Type u_1} [CommRing A]
  [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A]
  {S : TauCeti.Huber.Pair A} {B : Type u_2} [CommRing B] [Algebra A B] [Module.Finite A B]
  [TopologicalSpace B] [IsModuleTopology A B] [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B]
  {D : Type u_3} [CommRing D] [TopologicalSpace D] [IsTopologicalRing D]
  [TauCeti.Huber.IsHuberRing D] [Algebra A D] {V : TauCeti.Huber.Pair D} (χ : S.Hom V)
  (hχ : χ.toRingHom = algebraMap A D) :
  { ψ // ψ.comp (TauCeti.Huber.Pair.finiteAlgebra.algebraHom S B) = χ } ≃ (B →ₐ[A] D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.Pair.finiteAlgebra.homEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Pair.html#TauCeti.Huber.Pair.finiteAlgebra.homEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.Pair.finiteAlgebra.homEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Pair.html#TauCeti.Huber.Pair.finiteAlgebra.homEquiv)
- [Source of `TauCeti.Huber.Pair.finiteAlgebra.homEquiv` in TauCeti/RingTheory/Huber/ModuleTopology/Pair.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/ModuleTopology/Pair.lean#L153)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
