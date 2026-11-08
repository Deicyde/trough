---
declaration: theorem
origin: cited
lean: NumberField.artinSymbol_eq_map_autCongr
statement: formalized
proof: formalized
---

# The Artin symbol is equivariant under an isomorphism of extensions

For `e : L ≃ₐ[K] L'`,
the symbol computed in `L'` is the image of the one computed in `L` under the induced isomorphism
`AlgEquiv.autCongr e` of Galois groups.

```lean
NumberField.artinSymbol_eq_map_autCongr.{u_1, u_2, u_3} {K : Type u_1} [Field K] [NumberField K]
  {L : Type u_2} {L' : Type u_3} [Field L] [Algebra K L] [Field L'] [Algebra K L'] [NumberField L]
  [IsGalois K L] [NumberField L'] [IsGalois K L'] (𝔭 : Ideal (NumberField.RingOfIntegers K))
  [𝔭.IsMaximal] (e : L ≃ₐ[K] L')
  (hur :
    ∀ (Q : Ideal (NumberField.RingOfIntegers L)) [inst : Q.IsPrime] [Q.LiesOver 𝔭],
      Algebra.IsUnramifiedAt (NumberField.RingOfIntegers K) Q)
  (hur' :
    ∀ (Q : Ideal (NumberField.RingOfIntegers L')) [inst : Q.IsPrime] [Q.LiesOver 𝔭],
      Algebra.IsUnramifiedAt (NumberField.RingOfIntegers K) Q) :
  NumberField.artinSymbol 𝔭 hur' =
    ConjClasses.map e.autCongr.toMonoidHom (NumberField.artinSymbol 𝔭 hur)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.artinSymbol_eq_map_autCongr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ArtinSymbol.html#NumberField.artinSymbol_eq_map_autCongr).

## Sources

- [Tau Ceti documentation: `NumberField.artinSymbol_eq_map_autCongr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ArtinSymbol.html#NumberField.artinSymbol_eq_map_autCongr)
- [Source of `NumberField.artinSymbol_eq_map_autCongr` in TauCeti/NumberTheory/NumberField/ArtinSymbol.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/ArtinSymbol.lean#L173)
