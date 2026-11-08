---
declaration: theorem
origin: cited
lean: ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite, TauCeti.IsGoodDixonPrime.isSemisimpleRing, Representation.IntertwiningMap.exists_leftInverse_of_injective
statement: formalized
proof: formalized
---

# Maschke's theorem in orthogonal form

A finite-dimensional representation `π` of a finite
group on an inner product space is an internal direct sum of finitely many irreducible
subrepresentations, of dimensions adding up to `dim V`, which are moreover pairwise *orthogonal*
for an invariant inner product `⟪e ·, e ·⟫` obtained from the given one by a continuous linear
automorphism `e` of the carrier.

This is the finite shadow of complete reducibility, and all that is finite about it is the
production of `e`: unitarity is not assumed but produced, by the finite unitarian trick
`ContRepresentation.exists_isUnitary_congr_of_finite`, and the decomposition of `π` itself is then
`ContRepresentation.IsUnitary.exists_orthogonal_irreducible_decomposition_of_congr`, which
decomposes the unitary model and carries every block back along the equivalence of representations
`ContRepresentation.congrEquiv : π.Equiv (congr e π)` for an arbitrary group. The blocks are
therefore subrepresentations of `π` itself.

Distorting the inner product by `e` is unavoidable and is what "Maschke" costs here: Lean fixes one
inner product on `V`, and a representation of a finite group need not preserve it, only the average
`|G|⁻¹ ∑ g, ⟪π g ·, π g ·⟫` of its translates. So the blocks need not be orthogonal for `⟪·, ·⟫`,
and orthogonality is stated for the invariant form `⟪e ·, e ·⟫` that the unitarian trick produces —
equivalently, their images under `e` are the orthogonal family decomposing the unitary model
`congr e π`. It is that orthogonality which the compact theory contributes over Mathlib's Maschke,
which produces complements but no inner product; the plain semisimplicity is not restated here,
being already a Mathlib instance for every field in which `|G|` is invertible.

```lean
ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {G : Type u_2} {V : Type u_3} [RCLike 𝕜] [Group G] [Finite G]
  [NormedAddCommGroup V] [InnerProductSpace 𝕜 V] [FiniteDimensional 𝕜 V]
  (π : ContRepresentation 𝕜 G V) :
  ∃ e n U,
    (e.congr π).IsUnitary ∧
      (∀ (i : Fin n), (U i).toRepresentation.IsIrreducible) ∧
        (Pairwise fun i j =>
            ∀ v ∈ (U i).toSubmodule, ∀ w ∈ (U j).toSubmodule, inner 𝕜 (e v) (e w) = 0) ∧
          (DirectSum.IsInternal fun i => (U i).toSubmodule) ∧
            Module.finrank 𝕜 V = ∑ i, Module.finrank 𝕜 ↥(U i).toSubmodule
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/Finite.html#ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite).

## Other forms

**Maschke's theorem at a good Dixon prime.** Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.isSemisimpleRing).

```lean
TauCeti.IsGoodDixonPrime.isSemisimpleRing.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) : IsSemisimpleRing (MonoidAlgebra (ZMod p) G)
```

**Maschke's theorem for intertwining maps.** Formalized in Tau Ceti as [`Representation.IntertwiningMap.exists_leftInverse_of_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Maschke.html#Representation.IntertwiningMap.exists_leftInverse_of_injective).

```lean
Representation.IntertwiningMap.exists_leftInverse_of_injective.{u_1, u_2, u_3, u_4} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} {W : Type u_4} [Field k] [Group G] [Finite G] [NeZero ↑(Nat.card G)]
  [AddCommGroup V] [_root_.Module k V] [AddCommGroup W] [_root_.Module k W]
  {ρ : Representation k G V} {σ : Representation k G W} (f : ρ.IntertwiningMap σ)
  (hf : Function.Injective ⇑f) : ∃ p, p.comp f = Representation.IntertwiningMap.id ρ
```

## Sources

- [Tau Ceti documentation: `ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/Finite.html#ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite)
- [Source of `ContRepresentation.exists_orthogonal_irreducible_decomposition_of_finite` in TauCeti/RepresentationTheory/Compact/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Compact/Finite.lean#L790)
