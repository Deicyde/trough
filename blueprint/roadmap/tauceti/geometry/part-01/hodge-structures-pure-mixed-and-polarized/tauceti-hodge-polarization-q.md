---
declaration: def
origin: cited
lean: TauCeti.Hodge.Polarization.Q
statement: formalized
---

# TauCeti.Hodge.Polarization.Q

The complex bilinear form of a polarization, derived by complexifying the integral form.

```lean
TauCeti.Hodge.Polarization.Q.{u, v} {V : Type u} {Vℂ : Type v} [AddCommGroup V] [AddCommGroup Vℂ]
  [_root_.Module ℂ Vℂ] {ιℂ : V →ₗ[ℤ] Vℂ} {hℂ : IsBaseChange ℂ ιℂ} {n : ℤ}
  {hs : TauCeti.Hodge.HodgeStructure hℂ n} (P : TauCeti.Hodge.Polarization hℂ hs) :
  LinearMap.BilinForm ℂ Vℂ
```

## Depends on

- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.Polarization.Q`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Polarization.html#TauCeti.Hodge.Polarization.Q).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.Polarization.Q`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Polarization.html#TauCeti.Hodge.Polarization.Q)
- [Source of `TauCeti.Hodge.Polarization.Q` in TauCeti/Geometry/Hodge/Polarization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/Polarization.lean#L169)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
