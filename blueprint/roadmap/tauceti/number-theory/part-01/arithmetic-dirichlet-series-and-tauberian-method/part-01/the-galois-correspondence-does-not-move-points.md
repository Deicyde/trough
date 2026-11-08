---
declaration: theorem
origin: cited
lean: Subgroup.coe_subgroupEquivAlgEquiv, Subgroup.subgroupEquivAlgEquiv_smul_ideal
statement: formalized
proof: formalized
---

# The Galois correspondence does not move points

For a subgroup `H` of `Gal(L/K)`, the
automorphism of `L` over `L ^ H` attached to `τ ∈ H` is `τ` itself on elements.

```lean
Subgroup.coe_subgroupEquivAlgEquiv.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K] [Field L]
  [Algebra K L] [FiniteDimensional K L] (H : Subgroup Gal(L/K)) (τ : ↥H) (x : L) :
  ((IntermediateField.subgroupEquivAlgEquiv H) τ) x = ↑τ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.coe_subgroupEquivAlgEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/FixedField.html#Subgroup.coe_subgroupEquivAlgEquiv).

## Other forms

**The Galois correspondence does not move ideals.** Formalized in Tau Ceti as [`Subgroup.subgroupEquivAlgEquiv_smul_ideal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/FixedField.html#Subgroup.subgroupEquivAlgEquiv_smul_ideal).

```lean
Subgroup.subgroupEquivAlgEquiv_smul_ideal.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [Field L] [Algebra K L] [FiniteDimensional K L] (H : Subgroup Gal(L/K)) (τ : ↥H)
  (Q : Ideal (NumberField.RingOfIntegers L)) :
  (IntermediateField.subgroupEquivAlgEquiv H) τ • Q = ↑τ • Q
```

## Sources

- [Tau Ceti documentation: `Subgroup.coe_subgroupEquivAlgEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/FixedField.html#Subgroup.coe_subgroupEquivAlgEquiv)
- [Source of `Subgroup.coe_subgroupEquivAlgEquiv` in TauCeti/NumberTheory/NumberField/FixedField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/FixedField.lean#L92)
