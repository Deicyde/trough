---
declaration: instance
origin: cited
lean: TauCeti.Floer.SphericalCapClass.instAddTorsor
statement: formalized
---

# The cap classes of a contractible loop form a torsor under the spherical period group, on a path-connected space

```lean
TauCeti.Floer.SphericalCapClass.instAddTorsor {X : Type} [TopologicalSpace X] {x : X}
  {ω : ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat ℤ) 2).obj ↧ℤ).obj ↧X) →+ ℝ}
  {c : ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat ℤ) 2).obj ↧ℤ).obj ↧X) →+ ℤ}
  {γ : LoopSpace X x} [PathConnectedSpace X] [Nonempty (TauCeti.Floer.RawCap γ)] :
  AddTorsor (TauCeti.Floer.SphericalPeriodGroup ω c) (TauCeti.Floer.SphericalCapClass ω c γ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.SphericalCapClass.instAddTorsor`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Loop.html#TauCeti.Floer.SphericalCapClass.instAddTorsor).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.SphericalCapClass.instAddTorsor`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Loop.html#TauCeti.Floer.SphericalCapClass.instAddTorsor)
- [Source of `TauCeti.Floer.SphericalCapClass.instAddTorsor` in TauCeti/Geometry/Symplectic/Floer/Cap/Loop.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/Cap/Loop.lean#L429)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
