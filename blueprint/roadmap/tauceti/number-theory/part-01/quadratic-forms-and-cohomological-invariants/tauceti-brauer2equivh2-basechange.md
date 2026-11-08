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

- [The comparison isomorphism `Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous cohomology, for `K` in any universe](the-comparison-isomorphism-br-k-h2-cont-g-k-ks-x.md)

## Proof depends on

- [The dimension count behind the centralizer theorem, asking only for what it uses](../../../algebra/central-simple/the-dimension-count-behind-the-centralizer-theor.md)
- [The Skolem-Noether theorem](../../../algebra/central-simple/the-skolem-noether-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.brauer2EquivH2_baseChange`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.html#TauCeti.brauer2EquivH2_baseChange)
- [Source of `TauCeti.brauer2EquivH2_baseChange` in TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CrossedProduct/BaseChange/Naturality.lean#L69)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
