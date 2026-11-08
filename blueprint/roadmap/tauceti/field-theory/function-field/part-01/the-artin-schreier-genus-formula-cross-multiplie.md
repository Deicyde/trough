---
declaration: theorem
origin: cited
lean: TauCeti.artinSchreier_genus_formula
statement: formalized
proof: formalized
---

# The Artin--Schreier genus formula, cross-multiplied for a possible constant-field extension

The representatives may vary with the place. Pole orders are weighted by residue
field degrees, not by the number of poles.

```lean
TauCeti.artinSchreier_genus_formula.{u, u', v, v'} {k : Type u} {k' : Type u'} {F : Type v}
  {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  (hF : TauCeti.IsFunctionField k F) (hF' : TauCeti.IsFunctionField k' F') (p : ℕ)
  [Fact (Nat.Prime p)] [CharP F p] {y : F'} {u : F} (hgen : F⟮y⟯ = ⊤)
  (hy : y ^ p - y = (algebraMap F F') u) (S : Finset (TauCeti.Place k F))
  (m : TauCeti.Place k F → ℕ)
  (hpole : ∀ P ∈ S, ∃ w, P.ord (u - (w ^ p - w)) = -↑(m P) ∧ ¬↑p ∣ P.ord (u - (w ^ p - w)))
  (hreg : ∀ P ∉ S, ∃ w, u - (w ^ p - w) ∈ P.integers) [Algebra.IsSeparable k k']
  (hex : IsIntegrallyClosedIn k F) (hex' : IsIntegrallyClosedIn k' F')
  (hu : ∀ (w : F), w ^ p - w ≠ u) :
  ↑(Module.finrank k k') * (2 * ↑(TauCeti.genus k' F') - 2) =
    ↑p * (2 * ↑(TauCeti.genus k F) - 2) + (↑p - 1) * ∑ P ∈ S, (↑(m P) + 1) * ↑P.degree
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental identity](the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.artinSchreier_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Genus.html#TauCeti.artinSchreier_genus_formula).

## Sources

- [Tau Ceti documentation: `TauCeti.artinSchreier_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Genus.html#TauCeti.artinSchreier_genus_formula)
- [Source of `TauCeti.artinSchreier_genus_formula` in TauCeti/FieldTheory/FunctionField/ArtinSchreier/Genus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Genus.lean#L187)
