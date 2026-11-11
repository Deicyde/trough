---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.IsPolarizable.internalHom
statement: formalized
proof: formalized
---

# Polarizable pure Hodge structures are closed under internal homs

The internal hom of
weights `n₁` and `n₂` is polarizable of weight `n₂ - n₁`.

```lean
TauCeti.Hodge.IsPolarizable.internalHom.{u₁, u₂, v₁, v₂} {V₁ : Type u₁} {V₂ : Type u₂}
  {W₁ : Type v₁} {W₂ : Type v₂} [AddCommGroup V₁] [Module.Free ℤ V₁] [Module.Finite ℤ V₁]
  [AddCommGroup V₂] [AddCommGroup W₁] [_root_.Module ℂ W₁] [AddCommGroup W₂] [_root_.Module ℂ W₂]
  {ι₁ : V₁ →ₗ[ℤ] W₁} {ι₂ : V₂ →ₗ[ℤ] W₂} {h₁ : IsBaseChange ℂ ι₁} {h₂ : IsBaseChange ℂ ι₂}
  {n₁ n₂ : ℤ} {hs₁ : TauCeti.Hodge.HodgeStructure h₁ n₁} {hs₂ : TauCeti.Hodge.HodgeStructure h₂ n₂}
  (h : TauCeti.Hodge.IsPolarizable h₁ hs₁) (h' : TauCeti.Hodge.IsPolarizable h₂ hs₂) :
  TauCeti.Hodge.IsPolarizable ⋯ (hs₁.internalHom hs₂)
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Proof depends on

- [The dual of a polarizable pure Hodge structure is polarizable](the-dual-of-a-polarizable-pure-hodge-structure-i.md)
- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.IsPolarizable.internalHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/InternalHom/Polarization.html#TauCeti.Hodge.IsPolarizable.internalHom).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.IsPolarizable.internalHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/InternalHom/Polarization.html#TauCeti.Hodge.IsPolarizable.internalHom)
- [Source of `TauCeti.Hodge.IsPolarizable.internalHom` in TauCeti/Geometry/Hodge/InternalHom/Polarization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/InternalHom/Polarization.lean#L90)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
