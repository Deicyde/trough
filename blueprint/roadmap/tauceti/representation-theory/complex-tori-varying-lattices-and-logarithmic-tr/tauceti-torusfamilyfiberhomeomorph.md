---
declaration: def
origin: cited
lean: TauCeti.torusFamilyFiberHomeomorph
statement: formalized
---

# TauCeti.torusFamilyFiberHomeomorph

The canonical identification of the translation quotient at `y` with the literal fibre
of the total period quotient. It sends `[v]` to `[y, v]` and needs no lattice basis.

```lean
TauCeti.torusFamilyFiberHomeomorph.{u_1, u_2, u_3} {Y : Type u_1} {Λ : Type u_2} {E : Type u_3}
  [AddCommGroup Λ] [AddCommGroup E] (P : Y → Λ →ₗ[ℤ] E) (y : Y) [TopologicalSpace Y]
  [TopologicalSpace E] [ContinuousAdd E] (hcont : ∀ (l : Λ), Continuous fun y => (P y) l) :
  AddAction.orbitRel.Quotient (↥(P y).range) E ≃ₜ ↑{z | TauCeti.torusFamilyProjection P z = y}
```

## Depends on

- [TauCeti.torusFamilyProjection](tauceti-torusfamilyprojection.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyFiberHomeomorph`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Fiber.html#TauCeti.torusFamilyFiberHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyFiberHomeomorph`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Fiber.html#TauCeti.torusFamilyFiberHomeomorph)
- [Source of `TauCeti.torusFamilyFiberHomeomorph` in TauCeti/Algebra/Module/ZLattice/Family/Fiber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Family/Fiber.lean#L111)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
