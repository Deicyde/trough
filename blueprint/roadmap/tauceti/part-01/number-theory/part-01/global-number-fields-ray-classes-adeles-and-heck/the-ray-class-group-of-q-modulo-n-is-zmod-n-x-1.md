---
declaration: def
origin: cited
lean: TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod
statement: formalized
---

# The ray class group of `ℚ` modulo `(n)` is `(ZMod n)ˣ ⧸ {±1}`

Without the real place, a
fractional ideal of `ℚ` prime to `n` has the two generators `±a` on an equal footing, so its ray
class is the residue of a generator modulo `n`, up to sign.

```lean
TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod (n : ℕ) (hn : n ≠ 0) :
  TauCeti.GlobalNumberFields.RayClassGroup (TauCeti.GlobalNumberFields.ratFiniteModulus n hn) ≃*
    (ZMod n)ˣ ⧸ Subgroup.zpowers (-1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/Rat.html#TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/Rat.html#TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod)
- [Source of `TauCeti.GlobalNumberFields.ratFiniteModulusEquivZMod` in TauCeti/NumberTheory/NumberField/Global/RayClass/Rat.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Global/RayClass/Rat.lean#L360)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/GlobalNumberFields/STATUS.md)
