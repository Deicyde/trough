---
declaration: theorem
origin: cited
lean: NumberField.fg_units_integralClosure, NumberField.unitsMulEquivTorsionProdMultiplicative
statement: formalized
proof: formalized
---

# Dirichlet's unit theorem (`NumberField.fg_units_integralClosure`)

**Dirichlet's unit theorem** (finite generation) for the integral closure of `𝓞 K` in a
finite extension `L` of the number field `K`: its unit group is finitely generated.

```lean
NumberField.fg_units_integralClosure.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K] [Field L]
  [Algebra K L] [NumberField K] [FiniteDimensional K L] :
  Group.FG (↥(integralClosure (NumberField.RingOfIntegers K) L))ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.fg_units_integralClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/IntegralClosure.html#NumberField.fg_units_integralClosure).

## Other forms

**Dirichlet's unit theorem, structural form.** Formalized in Tau Ceti as [`NumberField.unitsMulEquivTorsionProdMultiplicative`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Dirichlet.html#NumberField.unitsMulEquivTorsionProdMultiplicative).

```lean
NumberField.unitsMulEquivTorsionProdMultiplicative.{u_1} (F : Type u_1) [Field F] [NumberField F] :
  (NumberField.RingOfIntegers F)ˣ ≃*
    ↥(NumberField.Units.torsion F) × Multiplicative (Fin (NumberField.Units.rank F) → ℤ)
```

## Sources

- [Tau Ceti documentation: `NumberField.fg_units_integralClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/IntegralClosure.html#NumberField.fg_units_integralClosure)
- [Source of `NumberField.fg_units_integralClosure` in TauCeti/NumberTheory/NumberField/IntegralClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/IntegralClosure.lean#L69)
