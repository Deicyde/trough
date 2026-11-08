---
declaration: theorem
origin: cited
lean: HeckeCoset.heckeSum_eq_sum_of_rightCosets
statement: formalized
proof: formalized
---

# The Hecke sum of a `Γ₁`-invariant map is the sum over any decomposition of the double coset into right cosets

If the right cosets `Γ₁ aᵢ` are pairwise distinct and cover `Γ₁ D.out Γ₂`,
then `heckeSum D ρ q = ∑ᵢ q ∘ ρ(aᵢ)`.

So the map is attached to the double coset itself: the representatives `D.out` and `v.out` that
`heckeSum` happens to pick are one such family, and every other family gives the same map. The
hypothesis `ha` records that the family lies in the monoid `ρ` acts through; it is automatic
when the family lies in the double coset and `Γ₁ ≤ Δ'`.

```lean
HeckeCoset.heckeSum_eq_sum_of_rightCosets.{u_1, u_2, u_3, u_4, u_5, u_6} {G : Type u_1} [Group G]
  {Δ Δ' : Submonoid G} {Γ₁ Γ₂ : Subgroup G} (D : HeckeCoset Δ Γ₁ Γ₂) {R : Type u_2} {S : Type u_3}
  {V : Type u_4} {W : Type u_5} [Semiring R] [Semiring S] [AddCommMonoid V] [_root_.Module R V]
  [AddCommMonoid W] [_root_.Module S W] {σ : R →+* S} (ρ : Representation R (↥Δ') V)
  (hD : ↑(Quotient.out D) ∈ Δ') (hΓ₂ : Γ₂.toSubmonoid ≤ Δ') {q : V →ₛₗ[σ] W}
  [Finite (DoubleCoset.DecompQuotient Γ₂ Γ₁ (↑(Quotient.out D))⁻¹)] (hΓ₁ : Γ₁.toSubmonoid ≤ Δ')
  (hq : ∀ (γ : G) (hγ : γ ∈ Γ₁), q ∘ₛₗ ρ ⟨γ, ⋯⟩ = q) {ι : Type u_6} [Fintype ι] (a : ι → G)
  (ha : ∀ (i : ι), a i ∈ Δ')
  (hcover : DoubleCoset.doubleCoset ↑(Quotient.out D) ↑Γ₁ ↑Γ₂ = ⋃ i, MulOpposite.op (a i) • ↑Γ₁)
  (hinj : Function.Injective fun i => MulOpposite.op (a i) • ↑Γ₁) :
  D.heckeSum ρ hD hΓ₂ q = ∑ i, q ∘ₛₗ ρ ⟨a i, ⋯⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's decomposition of a double coset into right cosets](shimuras-decomposition-of-a-double-coset-into-ri.md)

## Lean

Formalized in Tau Ceti as [`HeckeCoset.heckeSum_eq_sum_of_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Representation.html#HeckeCoset.heckeSum_eq_sum_of_rightCosets).

## Sources

- [Tau Ceti documentation: `HeckeCoset.heckeSum_eq_sum_of_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Representation.html#HeckeCoset.heckeSum_eq_sum_of_rightCosets)
- [Source of `HeckeCoset.heckeSum_eq_sum_of_rightCosets` in TauCeti/NumberTheory/HeckeRing/Representation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/HeckeRing/Representation.lean#L128)
