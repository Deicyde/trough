---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField
statement: formalized
proof: formalized
---

# TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField

An upper break of a finite abelian extension is detected in a cyclic subextension. The
subextension can be chosen with trivial upper ramification groups at every later index, so the
specified break is its last break. Its local-field structures are the canonical ones induced
from the base field.

```lean
TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField.{u_1, u_2}
  (K : Type u_1) (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [IsAbelianGalois K L] (u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain) :
  TauCeti.LocalFieldsRamification.UpperJump K L u ↔
    ∃ F,
      IsCyclic Gal(↥F/K) ∧
        TauCeti.LocalFieldsRamification.UpperJump K (↥F) u ∧
          ∀ (v : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain),
            u < v → TauCeti.LocalFieldsRamification.upperRamificationGroup K (↥F) v = ⊥
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Herbrand's theorem in the upper numbering](herbrands-theorem-in-the-upper-numbering.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/CyclicReduction.html#TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/CyclicReduction.html#TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField)
- [Source of `TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField` in TauCeti/NumberTheory/LocalField/Herbrand/CyclicReduction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Herbrand/CyclicReduction.lean#L80)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
