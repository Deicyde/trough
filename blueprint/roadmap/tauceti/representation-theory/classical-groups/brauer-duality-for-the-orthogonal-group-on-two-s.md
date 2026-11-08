---
declaration: theorem
origin: cited
lean: TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors
statement: formalized
proof: formalized
---

# Brauer duality for the orthogonal group on two strands

Over a commutative ring without
zero divisors in which `2 ≠ 0` and which contains a point `(c, s)` of the unit circle with
`c * s ≠ 0`, the operators on `Rⁿ ⊗ Rⁿ` commuting with the diagonal action of the orthogonal
group are exactly the image of the Brauer algebra `B₂(n)`: the combinations of the identity, the
flip of the two factors, and the contraction-expansion `x ⊗ y ↦ (x ⬝ᵥ y) • ∑ᵢ eᵢ ⊗ eᵢ`.

Some point of the circle with `c * s ≠ 0` is needed when `n = 2`: over `ZMod 3` the orthogonal
group of the plane consists of the signed permutation matrices, which commute with the projection
onto the span of `e₀ ⊗ e₀` and `e₁ ⊗ e₁`, and that projection is not in the image.

```lean
TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors.{u} (R : Type u) [CommRing R]
  (n : ℕ) [NoZeroDivisors R] (h2 : 2 ≠ 0) (hrot : ∃ c s, c ^ 2 + s ^ 2 = 1 ∧ c * s ≠ 0) :
  (TauCeti.brauerActionOrth R n 2).range =
    Subalgebra.centralizer R (Set.range ⇑((TauCeti.stdOrthogonalRep R n).tensorPower 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/TwoStrands.html#TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors).

## Sources

- [Tau Ceti documentation: `TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/TwoStrands.html#TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors)
- [Source of `TauCeti.range_brauerActionOrth_two_eq_centralizer_of_noZeroDivisors` in TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/TwoStrands.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/TwoStrands.lean#L221)
