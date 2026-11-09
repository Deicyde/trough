---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep
statement: formalized
proof: formalized
---

# Modular-Artin reduction of the local Euler characteristic formula

If `χ_F = φ_F` holds
for the inflation to `G_F` of every representation of a finite Galois quotient `G_F ⧸ V` induced
from a cyclic subgroup of order prime to `ℓ`, then it holds for every finite smooth discrete
`ZMod ℓ`-representation of `G_F`.

```lean
TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep (p : ℕ)
  [Fact (Nat.Prime p)] (F : Type) [Field F] [CharZero F] [ValuativeRel F] [TopologicalSpace F]
  [IsNonarchimedeanLocalField F] [TauCeti.FinitePadicExtension F p] (ℓ : ℕ) [Fact (Nat.Prime ℓ)]
  (h :
    ∀ (V : OpenNormalSubgroup (Field.absoluteGaloisGroup F))
      (C : Subgroup (Field.absoluteGaloisGroup F ⧸ ↑V.toOpenSubgroup)),
      IsCyclic ↥C ∧ ¬ℓ ∣ Nat.card ↥C →
        ∀ (B : FDRep (ZMod ℓ) ↥C),
          TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯
              ((TauCeti.ClassFieldTheory.fdGalRepOfQuotient ℓ F V).obj (TauCeti.indFDRep B)) =
            TauCeti.ClassFieldTheory.localCardNorm p
              ((TauCeti.ClassFieldTheory.fdGalRepOfQuotient ℓ F V).obj (TauCeti.indFDRep B)))
  (A : TauCeti.ClassFieldTheory.GalRep ℓ F) [Finite ↑A] [DiscreteTopology ↑A]
  [Fact (TauCeti.IsSmoothDiscrete (ZMod ℓ) A)] :
  TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯ A = TauCeti.ClassFieldTheory.localCardNorm p A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's induction identity for every virtual class over every field](../../../representation-theory/grothendieck-group/artins-induction-identity-for-every-virtual-clas.md)
- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Euler characteristic formula and `G₀`](the-euler-characteristic-formula-and-g0.md)
- [Kolchin's common fixed vector theorem](../../../linear-algebra/other-results/kolchins-common-fixed-vector-theorem.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Local Tate duality in degree one](local-tate-duality-in-degree-one.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/ModularInduction.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/ModularInduction.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep)
- [Source of `TauCeti.ClassFieldTheory.localEulerCharacteristic_eq_localCardNorm_of_indFDRep` in TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/ModularInduction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/ModularInduction.lean#L51)
