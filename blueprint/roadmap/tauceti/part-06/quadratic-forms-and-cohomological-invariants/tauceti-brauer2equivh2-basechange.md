---
declaration: theorem
origin: cited
lean: TauCeti.brauer2EquivH2_baseChange
statement: formalized
proof: formalized
---

# TauCeti.brauer2EquivH2\_baseChange

Scalar extension of any two-torsion Brauer class corresponds under `ι` to
restriction of its mod-two Galois cohomology class.

```lean
TauCeti.brauer2EquivH2_baseChange.{u} {K L : Type u} [Field K] [Field L] [Algebra K L]
  [FiniteDimensional K L] (σ : L →ₐ[K] SeparableClosure K) [Invertible 2] [Invertible 2]
  (x : ↥(TauCeti.BrauerGroup.twoTorsion K)) :
  (TauCeti.brauer2EquivH2 L) (Additive.ofMul ((TauCeti.BrauerGroup.twoTorsionBaseChange K L) x)) =
    (CategoryTheory.ConcreteCategory.hom (TauCeti.galoisRes K L σ 2))
      ((TauCeti.brauer2EquivH2 K) (Additive.ofMul x))
```

## Depends on

- [The comparison isomorphism](the-comparison-isomorphism.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange)
- [Source of `TauCeti.brauer2EquivH2_baseChange` in TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean#L69)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
