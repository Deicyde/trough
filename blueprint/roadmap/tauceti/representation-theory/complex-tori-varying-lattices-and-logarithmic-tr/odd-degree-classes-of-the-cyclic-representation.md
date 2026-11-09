---
declaration: theorem
origin: cited
lean: AddEquiv.groupCohomologyπOdd_cyclicRep_eq_iff
statement: formalized
proof: formalized
---

# Odd-degree classes of the cyclic representation

Two norm-zero elements `x` and `y`
have the same class in odd degree exactly when `y = x + (b - A b)` for some `b : T`.

```lean
AddEquiv.groupCohomologyπOdd_cyclicRep_eq_iff {T : Type} [AddCommGroup T] {m : ℕ} [NeZero m]
  (A : T ≃+ T) (hA : (⇑A)^[m] = id) (i : ℕ) (hi : Odd i)
  (x y : ↥(Rep.Hom.hom (A.cyclicRep hA).norm.asHom).ker) :
  (CategoryTheory.ConcreteCategory.hom
          (Rep.FiniteCyclicGroup.groupCohomologyπOdd (A.cyclicRep hA) (Multiplicative.ofAdd 1) ⋯ i
            hi))
        x =
      (CategoryTheory.ConcreteCategory.hom
          (Rep.FiniteCyclicGroup.groupCohomologyπOdd (A.cyclicRep hA) (Multiplicative.ofAdd 1) ⋯ i
            hi))
        y ↔
    ∃ b, ↑y = ↑x + (b - A b)
```

## Depends on

- [AddEquiv.cyclicRep](addequiv-cyclicrep.md)

## Lean

Formalized in Tau Ceti as [`AddEquiv.groupCohomologyπOdd_cyclicRep_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#AddEquiv.groupCohomology%CF%80Odd_cyclicRep_eq_iff).

## Sources

- [Tau Ceti documentation: `AddEquiv.groupCohomologyπOdd_cyclicRep_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#AddEquiv.groupCohomology%CF%80Odd_cyclicRep_eq_iff)
- [Source of `AddEquiv.groupCohomologyπOdd_cyclicRep_eq_iff` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L178)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
