---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id
statement: formalized
proof: formalized
---

# Self-duality is invertible up to a nonzero integer

For a polarization of `V`, there is a
Hodge morphism `g : V^*(-n) → V` such that composing it with self-duality, in either order, is
multiplication by a nonzero natural number `c`. Over `ℚ`, `c⁻¹ • g` is the inverse of
self-duality.

```lean
TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id.{u, v} {V : Type u} {Vℂ : Type v}
  [AddCommGroup V] [Module.Free ℤ V] [Module.Finite ℤ V] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ]
  {ιℂ : V →ₗ[ℤ] Vℂ} {hℂ : IsBaseChange ℂ ιℂ} {n : ℤ} {hs : TauCeti.Hodge.HodgeStructure hℂ n}
  (P : TauCeti.Hodge.Polarization hℂ hs) :
  ∃ c,
    c ≠ 0 ∧
      ∃ g,
        P.toDualHom.comp g = c • TauCeti.Hodge.HodgeStructure.Hom.id hs.dualTateTwist ∧
          g.comp P.toDualHom = c • TauCeti.Hodge.HodgeStructure.Hom.id hs
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/SelfDuality.html#TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/SelfDuality.html#TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id)
- [Source of `TauCeti.Hodge.Polarization.exists_comp_toDualHom_eq_nsmul_id` in TauCeti/Geometry/Hodge/SelfDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/SelfDuality.lean#L171)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
