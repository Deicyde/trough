---
declaration: theorem
origin: cited
lean: TauCeti.brauer2EquivH2_baseChange
statement: formalized
proof: formalized
---

# TauCeti.brauer2EquivH2_baseChange

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

## Proof depends on

- [Artin--Wedderburn over a separably closed field](../../../algebra/part-02/central-simple/artin-wedderburn-over-a-separably-closed-field.md)
- [The dimension count behind the centralizer theorem, asking only for what it uses](../../../algebra/part-02/central-simple/the-dimension-count-behind-the-centralizer-theor.md)
- [The Skolem-Noether theorem](../../../algebra/part-02/central-simple/the-skolem-noether-theorem.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/part-02/central-simple/wedderburn-artin-for-central-simple-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange)
- [Source of `TauCeti.brauer2EquivH2_baseChange` in TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean#L69)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
