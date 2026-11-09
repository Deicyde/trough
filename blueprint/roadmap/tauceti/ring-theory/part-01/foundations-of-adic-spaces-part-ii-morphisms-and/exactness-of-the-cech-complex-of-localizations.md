---
declaration: theorem
origin: cited
lean: TauCeti.cechComplexLocalization_exact
statement: formalized
proof: formalized
---

# Exactness of the Čech complex of localizations

If `ι` is finite and the `f i` generate
the unit ideal, the Čech complex of localizations of `M` is exact in every positive degree.

```lean
TauCeti.cechComplexLocalization_exact.{u_1, u_2, u_3} {R : Type u_1} [CommRing R] (M : Type u_2)
  [AddCommGroup M] [_root_.Module R M] {ι : Type u_3} (f : ι → R) [LinearOrder ι] [Finite ι]
  (hf : Ideal.span (Set.range f) = ⊤) (p : ℕ) :
  Function.Exact ⇑(TauCeti.cechLocalizationDifferential M f p)
    ⇑(TauCeti.cechLocalizationDifferential M f (p + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cechComplexLocalization_exact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/LocalizedModule/Cech.html#TauCeti.cechComplexLocalization_exact).

## Sources

- [Tau Ceti documentation: `TauCeti.cechComplexLocalization_exact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/LocalizedModule/Cech.html#TauCeti.cechComplexLocalization_exact)
- [Source of `TauCeti.cechComplexLocalization_exact` in TauCeti/Algebra/Module/LocalizedModule/Cech.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/LocalizedModule/Cech.lean#L643)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
