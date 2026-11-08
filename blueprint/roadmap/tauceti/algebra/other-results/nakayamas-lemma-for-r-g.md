---
declaration: theorem
origin: cited
lean: TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq, TauCeti.isSuperfluous_smul_top_of_isNilpotent
statement: formalized
proof: formalized
---

# Nakayama's lemma for `R[G]^ι`

An `R[G]`-linear endomorphism of `R[G]^ι` that is onto
modulo the maximal ideal is bijective.

```lean
TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq.{u_1, u_2, u_3}
  {R : Type u_1} [CommRing R] [IsLocalRing R] {G : Type u_2} [Monoid G] [Finite G] {ι : Type u_3}
  [Finite ι] (θ : (ι → MonoidAlgebra R G) →ₗ[MonoidAlgebra R G] ι → MonoidAlgebra R G)
  (h :
    ∀ (y : ι → MonoidAlgebra R G),
      ∃ x,
        ∀ (i : ι),
          (MonoidAlgebra.mapRingHom G (IsLocalRing.residue R)) (θ x i) =
            (MonoidAlgebra.mapRingHom G (IsLocalRing.residue R)) (y i)) :
  Function.Bijective ⇑θ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/LocalRing.html#TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq).

## Other forms

**Nakayama's lemma for a nilpotent ideal.** Formalized in Tau Ceti as [`TauCeti.isSuperfluous_smul_top_of_isNilpotent`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Submodule/Superfluous.html#TauCeti.isSuperfluous_smul_top_of_isNilpotent).

```lean
TauCeti.isSuperfluous_smul_top_of_isNilpotent.{u, v} {R : Type u} {M : Type v} [Semiring R]
  [AddCommMonoid M] [_root_.Module R M] {I : Ideal R} (hI : IsNilpotent I) :
  TauCeti.IsSuperfluous (I • ⊤)
```

## Sources

- [Tau Ceti documentation: `TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/LocalRing.html#TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq)
- [Source of `TauCeti.MonoidAlgebra.bijective_of_forall_exists_mapRingHom_residue_eq` in TauCeti/Algebra/MonoidAlgebra/LocalRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/MonoidAlgebra/LocalRing.lean#L50)
