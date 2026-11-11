---
declaration: structure
origin: cited
lean: TauCeti.Hodge.IsPolarization
statement: formalized
---

# TauCeti.Hodge.IsPolarization

The **Hodge–Riemann bilinear relations** for a fixed integral bilinear form `Q` on the lattice
of a weight-`n` Hodge structure.

The form is `(-1)^n`-symmetric and nondegenerate; its complexification annihilates
`F p × F (n + 1 - p)`; and `i^(p-q) Q x (conj x)` is a positive real number for every nonzero `x`
in the Hodge component `H^{p,q}`, where `q = n - p`.

```lean
TauCeti.Hodge.IsPolarization.{u, v} {V : Type u} {Vℂ : Type v} [AddCommGroup V] [AddCommGroup Vℂ]
  [_root_.Module ℂ Vℂ] {ιℂ : V →ₗ[ℤ] Vℂ} (hℂ : IsBaseChange ℂ ιℂ) {n : ℤ}
  (hs : TauCeti.Hodge.HodgeStructure hℂ n) (Q : LinearMap.BilinForm ℤ V) : Prop
```

## Depends on

- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.IsPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Polarization.html#TauCeti.Hodge.IsPolarization).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.IsPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Polarization.html#TauCeti.Hodge.IsPolarization)
- [Source of `TauCeti.Hodge.IsPolarization` in TauCeti/Geometry/Hodge/Polarization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Polarization.lean#L66)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
