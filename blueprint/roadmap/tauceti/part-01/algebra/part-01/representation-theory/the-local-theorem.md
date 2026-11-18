---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.tfae_exists_isAlmostSplit
statement: formalized
proof: formalized
---

# The local theorem

Let `A` and `T` be objects with local endomorphism rings, `A` not
projective and `T` not injective, such that `Ext¹_E(B, T)` and `Ext¹_E(A, X)` have finite length
for all `B` and `X`. The following are equivalent:

1. there is an almost-split conflation `T ⟶ Y ⟶ A`;
2. `(E/𝒫)(A, -) ≅ D Ext¹_E(-, T)`: for some `φ`, every `stablePairing φ B` is bijective;
3. `(E/ℐ)(-, T) ≅ D Ext¹_E(A, -)`, that is, `T` represents `D Ext¹_E(A, -)` on `E/ℐ`: for some
   `φ`, every `costablePairing φ X` is bijective.

In 1 ⇒ 2 and 1 ⇒ 3, any `φ` not vanishing on the almost-split class works.

```lean
TauCeti.ExactStructure.tfae_exists_isAlmostSplit.{w, v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} {A T : C} (R : Type u_1) [CommRing R] [CategoryTheory.Linear R C]
  (Q : Type w) [AddCommGroup Q] [_root_.Module R Q] [Module.Injective R Q] [Small.{w, u_1} R]
  (hQ : ∀ (𝔪 : Ideal R), 𝔪.IsMaximal → Module.length R (R ⧸ 𝔪 →ₗ[R] Q) = 1)
  [IsLocalRing (CategoryTheory.End A)] [IsLocalRing (CategoryTheory.End T)] (hA : ¬E.isProjective A)
  (hT : ¬E.isInjective T) (hB : ∀ (B : C), IsFiniteLength R (E.Ext1 B T))
  (hX : ∀ (X : C), IsFiniteLength R (E.Ext1 A X)) :
  [∃ e, e.shortComplex.IsAlmostSplit,
      ∃ φ, ∀ (B : C), Function.Bijective ⇑(TauCeti.ExactStructure.stablePairing φ B),
      ∃ φ, ∀ (X : C), Function.Bijective ⇑(TauCeti.ExactStructure.costablePairing φ X)].TFAE
```

## Depends on

- [TauCeti.ExactStructure.Ext1](tauceti-exactstructure-ext1.md)

## Proof depends on

- [Jacobson's lemma](../../../category-theory/preadditive/jacobsons-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.tfae_exists_isAlmostSplit`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/LocalDuality.html#TauCeti.ExactStructure.tfae_exists_isAlmostSplit).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.tfae_exists_isAlmostSplit`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/YonedaExt/LocalDuality.html#TauCeti.ExactStructure.tfae_exists_isAlmostSplit)
- [Source of `TauCeti.ExactStructure.tfae_exists_isAlmostSplit` in TauCeti/CategoryTheory/Exact/YonedaExt/LocalDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/YonedaExt/LocalDuality.lean#L323)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
