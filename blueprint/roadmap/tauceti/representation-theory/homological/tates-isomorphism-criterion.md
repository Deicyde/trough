---
declaration: theorem
origin: cited
lean: TauCeti.TateCohomology.map_bijective_of_forall_isPGroup, TauCeti.TateCohomology.map_res_bijective_of_forall_isPGroup
statement: formalized
proof: formalized
---

# Tate's isomorphism criterion

Let `G` be a finite group and `f : A ⟶ B` a morphism of
representations of `G`. If, for every subgroup `S` of `G` of prime-power order, the map induced by
`f` on the Tate cohomology of `S` is surjective in degree `q - 1`, bijective in degree `q` and
injective in degree `q + 1`, then `f` induces a bijection `Ĥⁿ(G, A) → Ĥⁿ(G, B)` in every
degree `n`.

```lean
TauCeti.TateCohomology.map_bijective_of_forall_isPGroup.{u} {k G : Type u} [CommRing k] [Group G]
  {A B : Rep.{u, u, u} k G} (f : A ⟶ B) [Fintype G] {q : ℤ}
  (hsurj :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Surjective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor (q - 1)).map ((Rep.resFunctor S.subtype).map f))))
  (hbij :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Bijective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor q).map ((Rep.resFunctor S.subtype).map f))))
  (hinj :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Injective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor (q + 1)).map ((Rep.resFunctor S.subtype).map f))))
  (n : ℤ) :
  Function.Bijective ⇑(CategoryTheory.ConcreteCategory.hom ((tateCohomologyFunctor n).map f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tate's cohomological triviality criterion (Milne II 3.10)](tates-cohomological-triviality-criterion-milne-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TateCohomology.map_bijective_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/IsoCriterion.html#TauCeti.TateCohomology.map_bijective_of_forall_isPGroup).

## Other forms

**Tate's isomorphism criterion, on every subgroup.** Formalized in Tau Ceti as [`TauCeti.TateCohomology.map_res_bijective_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/IsoCriterion.html#TauCeti.TateCohomology.map_res_bijective_of_forall_isPGroup).

```lean
TauCeti.TateCohomology.map_res_bijective_of_forall_isPGroup.{u} {k G : Type u} [CommRing k]
  [Group G] {A B : Rep.{u, u, u} k G} (f : A ⟶ B) [Finite G] {q : ℤ}
  (hsurj :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Surjective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor (q - 1)).map ((Rep.resFunctor S.subtype).map f))))
  (hbij :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Bijective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor q).map ((Rep.resFunctor S.subtype).map f))))
  (hinj :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S →
        Function.Injective
          ⇑(CategoryTheory.ConcreteCategory.hom
              ((tateCohomologyFunctor (q + 1)).map ((Rep.resFunctor S.subtype).map f))))
  (S : Subgroup G) [Fintype ↥S] (n : ℤ) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom
        ((tateCohomologyFunctor n).map ((Rep.resFunctor S.subtype).map f)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.TateCohomology.map_bijective_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/IsoCriterion.html#TauCeti.TateCohomology.map_bijective_of_forall_isPGroup)
- [Source of `TauCeti.TateCohomology.map_bijective_of_forall_isPGroup` in TauCeti/RepresentationTheory/Homological/TateCohomology/IsoCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/TateCohomology/IsoCriterion.lean#L149)
