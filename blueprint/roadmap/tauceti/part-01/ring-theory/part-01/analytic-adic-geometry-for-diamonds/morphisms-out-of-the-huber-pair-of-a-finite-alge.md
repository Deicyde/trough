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
- [Source of `TauCeti.Huber.Pair.finiteAlgebra.homEquiv` in TauCeti/RingTheory/Huber/ModuleTopology/Pair.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/ModuleTopology/Pair.lean#L153)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
