---
declaration: theorem
origin: cited
lean: TauCeti.isFiniteEtaleSplit_iff_exists_section
statement: formalized
proof: formalized
---

# TauCeti.isFiniteEtaleSplit\_iff\_exists\_section

A ring has no nonsplit finite étale covers if and only if every faithfully flat finite étale
algebra over it admits a section. Faithful flatness is needed: over a nonzero ring the zero
algebra is finite étale and totally split, but has no section.

```lean
TauCeti.isFiniteEtaleSplit_iff_exists_section.{u} {R : Type u} [CommRing R] :
  TauCeti.IsFiniteEtaleSplit R ↔
    ∀ (T : Type u) [inst : CommRing T] [inst_1 : Algebra R T] [Algebra.Etale R T]
      [Module.Finite R T] [Module.FaithfullyFlat R T], Nonempty (T →ₐ[R] R)
```

## Depends on

- [TauCeti.IsFiniteEtaleSplit](tauceti-isfiniteetalesplit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isFiniteEtaleSplit_iff_exists_section`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/FiniteEtaleSplit/Basic.html#TauCeti.isFiniteEtaleSplit_iff_exists_section).

## Sources

- [Tau Ceti documentation: `TauCeti.isFiniteEtaleSplit_iff_exists_section`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/FiniteEtaleSplit/Basic.html#TauCeti.isFiniteEtaleSplit_iff_exists_section)
- [Source of `TauCeti.isFiniteEtaleSplit_iff_exists_section` in TauCeti/RingTheory/Etale/FiniteEtaleSplit/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Etale/FiniteEtaleSplit/Basic.lean#L342)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
