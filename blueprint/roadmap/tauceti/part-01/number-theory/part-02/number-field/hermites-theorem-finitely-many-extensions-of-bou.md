---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset
statement: formalized
proof: formalized
---

# Hermite's theorem: finitely many extensions of bounded degree are unramified outside a finite set

Inside a field `A` containing the number field `K`, only finitely many finite extensions
`L / K` have degree at most `d` and are ramified only at places in the finite set `S`.

```lean
TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset.{u_1, u_3} {K : Type u_1}
  [Field K] [NumberField K] (A : Type u_3) [Field A] [Algebra K A] (d : ℕ)
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))) :
  {L | Module.finrank K ↥↑L ≤ d ∧ TauCeti.NumberField.ramifiedSupport K ↥↑L ⊆ S}.Finite
```

## Depends on

- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [The upper bound of Dedekind's different theorem](../local-field/the-upper-bound-of-dedekinds-different-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Hermite.html#TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Hermite.html#TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset)
- [Source of `TauCeti.NumberField.finite_of_finrank_le_of_ramifiedSupport_subset` in TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Hermite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Hermite.lean#L127)
