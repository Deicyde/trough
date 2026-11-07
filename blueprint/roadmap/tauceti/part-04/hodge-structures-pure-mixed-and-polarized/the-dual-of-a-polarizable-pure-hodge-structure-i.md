---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.IsPolarizable.dual
statement: formalized
proof: formalized
---

# The dual of a polarizable pure Hodge structure is polarizable

```lean
TauCeti.Hodge.IsPolarizable.dual.{u, v} {V : Type u} {Vℂ : Type v} [AddCommGroup V]
  [Module.Free ℤ V] [Module.Finite ℤ V] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℂ : V →ₗ[ℤ] Vℂ}
  {hℂ : IsBaseChange ℂ ιℂ} {n : ℤ} {hs : TauCeti.Hodge.HodgeStructure hℂ n}
  (h : TauCeti.Hodge.IsPolarizable hℂ hs) : TauCeti.Hodge.IsPolarizable ⋯ hs.dual
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [Self-duality is invertible up to a nonzero integer](self-duality-is-invertible-up-to-a-nonzero-integ.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.IsPolarizable.dual`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/SelfDuality.html#TauCeti.Hodge.IsPolarizable.dual).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.IsPolarizable.dual`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/SelfDuality.html#TauCeti.Hodge.IsPolarizable.dual)
- [Source of `TauCeti.Hodge.IsPolarizable.dual` in TauCeti/Geometry/Hodge/SelfDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/SelfDuality.lean#L217)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
