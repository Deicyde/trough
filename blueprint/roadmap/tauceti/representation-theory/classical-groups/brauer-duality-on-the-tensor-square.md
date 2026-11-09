---
declaration: theorem
origin: cited
lean: TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one, TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors, TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer, TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero, TauCeti.range_brauerActionOrth_two_eq_centralizer
statement: formalized
proof: formalized
---

# Brauer duality on the tensor square

Over a field `K` with `2 ≠ 0` that has a point
`(c, s)` of the unit circle with `c ≠ 0` and `s ≠ 0`, the image of the Brauer algebra `B₂(n)` in
the endomorphisms of `(Kⁿ)^{⊗2}` is the commutant of the diagonal action of the orthogonal group:
an operator commuting with every `g ⊗ g` is a combination of the identity, the flip of the two
tensor factors and the cup-cap generator.

```lean
TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one.{u_1} (K : Type u_1) [Field K]
  (n : ℕ) (h2 : 2 ≠ 0) {c s : K} (hcs : c ^ 2 + s ^ 2 = 1) (hc : c ≠ 0) (hs : s ≠ 0) :
  (TauCeti.brauerActionOrth K n 2).range =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdOrthogonalRep K n).tensorPower 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.html#TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one).

## Other forms

**Brauer duality for the orthogonal group on two strands.** Formalized in Tau Ceti as [`TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/TwoStrands.html#TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors).

```lean
TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors.{u} (R : Type u) [CommRing R]
  (n : ℕ) [NoZeroDivisors R] (h2 : 2 ≠ 0) (hrot : ∃ c s, c ^ 2 + s ^ 2 = 1 ∧ c * s ≠ 0) :
  (TauCeti.brauerActionOrth R n 2).range =
    Subalgebra.centralizer R (Set.range ⇑((TauCeti.stdOrthogonalRep R n).tensorPower 2))
```

**Brauer duality for the symplectic group on two strands.** Formalized in Tau Ceti as [`TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.html#TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer).

```lean
TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer.{u_1} {K : Type u_1} [CommRing K]
  {n : ℕ} [IsDomain K] (ht : ∃ t, ∀ (m : ℕ), 0 < m → m ≤ 4 → t ^ m ≠ 1) :
  K[TauCeti.symplecticCrossing K n, TauCeti.symplecticCupCap K n] =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdSymplecticRep K n).tensorPower 2))
```

**Brauer duality for the symplectic group on two strands in characteristic zero, for instance over `ℂ`.** Formalized in Tau Ceti as [`TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.html#TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero).

```lean
TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero.{u_1} {K : Type u_1}
  [Field K] [CharZero K] {n : ℕ} :
  K[TauCeti.symplecticCrossing K n, TauCeti.symplecticCupCap K n] =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdSymplecticRep K n).tensorPower 2))
```

**Brauer duality on the tensor square in characteristic zero.** Formalized in Tau Ceti as [`TauCeti.range_brauerActionOrth_two_eq_centralizer`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.html#TauCeti.range_brauerActionOrth_two_eq_centralizer).

```lean
TauCeti.range_brauerActionOrth_two_eq_centralizer.{u_1} (K : Type u_1) [Field K] [CharZero K]
  (n : ℕ) :
  (TauCeti.brauerActionOrth K n 2).range =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdOrthogonalRep K n).tensorPower 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.html#TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one)
- [Source of `TauCeti.range_brauerActionOrth_two_eq_centralizer_of_sq_add_sq_eq_one` in TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.lean#L291)
