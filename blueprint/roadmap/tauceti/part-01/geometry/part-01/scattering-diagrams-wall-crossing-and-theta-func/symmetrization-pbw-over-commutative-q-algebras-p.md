---
declaration: theorem
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv
statement: formalized
proof: formalized
---

# Symmetrization PBW over commutative `ℚ`-algebras (Petracci)

for an arbitrary Lie algebra
`L` over a commutative `ℚ`-algebra `R`, there is a linear equivalence `Sym_R(L) ≃ U_R(L)` sending a
product of `d` elements to `1/d!` times the sum of their products in all orders.

```lean
TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv.{v} (R : Type) (L : Type v)
  [CommRing R] [Algebra ℚ R] [LieRing L] [LieAlgebra R L] :
  ∃ β,
    ∀ (d : ℕ) (x : Fin d → L),
      β (∏ j, (SymmetricAlgebra.ι R L) (x j)) =
        (algebraMap ℚ R) (↑d.factorial)⁻¹ •
          ∑ σ, (List.ofFn fun j => (UniversalEnvelopingAlgebra.ι R) (x (σ j))).prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Symmetrization/Equiv.html#TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Symmetrization/Equiv.html#TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.exists_pbwSymmetrizationEquiv` in TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Symmetrization/Equiv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/UniversalEnveloping/PBW/Symmetrization/Equiv.lean#L103)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
