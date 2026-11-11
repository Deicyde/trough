---
declaration: def
origin: cited
lean: TauCeti.GlobalNumberFields.ratModulusEquivGal
statement: formalized
---

# The ray class group of `ℚ` modulo `(n)·∞` is the Galois group of `ℚ(ζ_n)`

The
composite of `ratModulusEquivZMod` with the inverse of Mathlib's `galEquivZMod`: a ray class with
residue `a ∈ (ZMod n)ˣ` goes to the automorphism acting on the `n`-th roots of unity by
`ζ ↦ ζ ^ a`. It sends the ray class of a prime `p ∤ n` to the arithmetic Frobenius at `p`
(`isArithFrobAt_iff_eq_ratModulusEquivGal_idealClass`).

```lean
TauCeti.GlobalNumberFields.ratModulusEquivGal.{u_1} (n : ℕ) [NeZero n] (F : Type u_1) [Field F]
  [NumberField F] [IsCyclotomicExtension {n} ℚ F] :
  TauCeti.GlobalNumberFields.RayClassGroup (TauCeti.GlobalNumberFields.ratModulus n ⋯) ≃* Gal(F/ℚ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.ratModulusEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Cyclotomic/RayClass.html#TauCeti.GlobalNumberFields.ratModulusEquivGal).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.ratModulusEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Cyclotomic/RayClass.html#TauCeti.GlobalNumberFields.ratModulusEquivGal)
- [Source of `TauCeti.GlobalNumberFields.ratModulusEquivGal` in TauCeti/NumberTheory/NumberField/Global/Cyclotomic/RayClass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/Cyclotomic/RayClass.lean#L68)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/GlobalNumberFields/STATUS.md)
