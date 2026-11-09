---
declaration: theorem
origin: cited
lean: TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv
statement: formalized
proof: formalized
---

# The equivariant Kummer isomorphism on Kummer classes (`TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv`)

Under
`kummerH1FiniteRepresentationEquiv`, the Kummer class of a power class `x` corresponds to the
homomorphism `μₙ → Lˣ ⧸ (Lˣ)ⁿ` sending `ξ` to `log ξ • x`, with `log : μₙ ≃ ℤ/n` the
identification `kummerCoeffAddEquivZMod`.

```lean
TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv.{u, v} {K : Type u} [Field K] {L : Type v}
  [Field L] [Algebra K L] [Normal K L] (sigma : L →ₐ[K] SeparableClosure K) (n : ℕ) (hn : IsUnit ↑n)
  (hN : ∀ g ∈ sigma.fieldRange.fixingSubgroup, ∀ (xi : TauCeti.KummerCoeff K n), g • xi = xi)
  (x : Additive (TauCeti.powerClassQuotient Lˣ n)) (xi : TauCeti.KummerCoeff K n) :
  ((dualTensorHom (ZMod n) (TauCeti.KummerCoeff K n) (Additive (TauCeti.powerClassQuotient Lˣ n)))
        ((TauCeti.kummerH1FiniteRepresentationEquiv sigma n hn hN)
          ((TauCeti.fixingSubgroupKummerEquivOfTrivial sigma hn (TauCeti.kummerCoeffAddEquivZMod hn)
              ⋯ hN)
            x)))
      xi =
    (TauCeti.kummerCoeffAddEquivZMod hn) xi • x
```

## Depends on

- [The Kummer isomorphism](../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.html#TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.html#TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv)
- [Source of `TauCeti.dualTensorHom_kummerH1FiniteRepresentationEquiv` in TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.lean#L681)
