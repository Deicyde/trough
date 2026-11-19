---
declaration: theorem
origin: cited
lean: TauCeti.isIso_cubicalHomologyKunneth, TauCeti.isIso_singularHomologyKunnethPair, TauCeti.isIso_singularHomologyKunnethPair_of_isSemisimpleRing, TauCeti.isIso_singularHomologyKunnethPair_of_projective, TauCeti.isIso_cubicalHomologyKunnethPair, TauCeti.isIso_cubicalHomologyKunnethPair_of_isSemisimpleRing, TauCeti.isIso_cubicalHomologyKunnethPair_of_projective, TauCeti.isIso_cubicalHomologyKunneth_of_isSemisimpleRing, TauCeti.isIso_cubicalHomologyKunneth_of_projective, TopCat.isIso_singularHomologyKunneth, TopCat.isIso_singularHomologyKunneth_of_projective, TopCat.isIso_singularHomologyKunneth_of_projective_homology
statement: formalized
proof: formalized
---

# The Künneth theorem for cubical homology

if the cycles of the normalized cubical chain
complexes split off their terms and their homology splits off the cycles, the Künneth map
`⨁_{p + q = n} Hₚ(X; k) ⊗ H_q(Y; k) ⟶ Hₙ(X × Y; k)` is an isomorphism.  This is the Künneth
theorem for the chain complexes `N(X; k)` and `N(Y; k)`, transported along the cubical
Eilenberg–Zilber quasi-isomorphism.

```lean
TauCeti.isIso_cubicalHomologyKunneth.{u} (k : Type u) [CommRing k] (X Y : TopCat)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TauCeti.normalizedCubicalChainComplex k).obj X) p)]
  [∀ (p : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TauCeti.normalizedCubicalChainComplex k).obj X) p)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TauCeti.normalizedCubicalChainComplex k).obj Y) q)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TauCeti.normalizedCubicalChainComplex k).obj Y) q)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunneth k X Y n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cubical Eilenberg–Zilber theorem](the-cubical-eilenberg-zilber-theorem.md)
- [The Eilenberg–Zilber theorem for singular chains](the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Künneth theorem for split complexes](../../algebra/part-02/homology/the-kunneth-theorem-for-split-complexes.md)
- [The small-chain theorem for a product of open pairs](the-small-chain-theorem-for-a-product-of-open-pa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunneth`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.isIso_cubicalHomologyKunneth).

## Other forms

**The Künneth theorem for a product of open pairs in singular homology.** Formalized in Tau Ceti as [`TauCeti.isIso_singularHomologyKunnethPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.html#TauCeti.isIso_singularHomologyKunnethPair).

```lean
TauCeti.isIso_singularHomologyKunnethPair.{u} (k : Type u) [CommRing k] {X Y : TopCat} {A : Set ↑X}
  {B : Set ↑Y} (hA : IsOpen A) (hB : IsOpen B) (n : ℕ)
  [CategoryTheory.IsIso
      (TauCeti.cubicalHomologyKunnethPair k (TopPair.ofSubset A) (TopPair.ofSubset B) n)] :
  CategoryTheory.IsIso (TauCeti.singularHomologyKunnethPair k A B n)
```

**The Künneth theorem for a product of open pairs over a field.** Formalized in Tau Ceti as [`TauCeti.isIso_singularHomologyKunnethPair_of_isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.html#TauCeti.isIso_singularHomologyKunnethPair_of_isSemisimpleRing).

```lean
TauCeti.isIso_singularHomologyKunnethPair_of_isSemisimpleRing.{u} (k : Type u) [CommRing k]
  {X Y : TopCat} {A : Set ↑X} {B : Set ↑Y} [IsSemisimpleRing k] (hA : IsOpen A) (hB : IsOpen B)
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.singularHomologyKunnethPair k A B n)
```

**The Künneth theorem for a product of open pairs with projective homology.** Formalized in Tau Ceti as [`TauCeti.isIso_singularHomologyKunnethPair_of_projective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Excisive.html#TauCeti.isIso_singularHomologyKunnethPair_of_projective).

```lean
TauCeti.isIso_singularHomologyKunnethPair_of_projective.{u} (k : Type u) [CommRing k] {X Y : TopCat}
  {A : Set ↑X} {B : Set ↑Y} (hA : IsOpen A) (hB : IsOpen B)
  [hA' : ∀ (p : ℕ), CategoryTheory.Projective ((TopPair.ofSubset A).singularHomology (↧k) p)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.singularHomologyKunnethPair k A B n)
```

**The Künneth theorem for a product of pairs.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Pair.html#TauCeti.isIso_cubicalHomologyKunnethPair).

```lean
TauCeti.isIso_cubicalHomologyKunnethPair.{u} (k : Type u) [CommRing k] (P Q : TopPair)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono (HomologicalComplex.iCycles (TopPair.cubicalChainComplex k P) p)]
  [∀ (p : ℕ),
      CategoryTheory.IsSplitEpi (HomologicalComplex.homologyπ (TopPair.cubicalChainComplex k P) p)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono (HomologicalComplex.iCycles (TopPair.cubicalChainComplex k Q) q)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitEpi (HomologicalComplex.homologyπ (TopPair.cubicalChainComplex k Q) q)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethPair k P Q n)
```

**The Künneth theorem for a product of pairs over a semisimple ring, for instance a field.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethPair_of_isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Pair.html#TauCeti.isIso_cubicalHomologyKunnethPair_of_isSemisimpleRing).

```lean
TauCeti.isIso_cubicalHomologyKunnethPair_of_isSemisimpleRing.{u} (k : Type u) [CommRing k]
  (P Q : TopPair) [IsSemisimpleRing k] (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethPair k P Q n)
```

**The Künneth theorem for a product of pairs with projective homology.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethPair_of_projective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Pair.html#TauCeti.isIso_cubicalHomologyKunnethPair_of_projective).

```lean
TauCeti.isIso_cubicalHomologyKunnethPair_of_projective.{u} (k : Type u) [CommRing k] (P Q : TopPair)
  [∀ (p : ℕ),
      CategoryTheory.Projective (HomologicalComplex.homology (TopPair.cubicalChainComplex k P) p)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethPair k P Q n)
```

**The Künneth theorem for cubical homology over a semisimple ring, for instance a field.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunneth_of_isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.isIso_cubicalHomologyKunneth_of_isSemisimpleRing).

```lean
TauCeti.isIso_cubicalHomologyKunneth_of_isSemisimpleRing.{u} (k : Type u) [CommRing k]
  (X Y : TopCat) [IsSemisimpleRing k] (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.cubicalHomologyKunneth k X Y n)
```

**The Künneth theorem for cubical homology with projective homology.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunneth_of_projective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.isIso_cubicalHomologyKunneth_of_projective).

```lean
TauCeti.isIso_cubicalHomologyKunneth_of_projective.{u} (k : Type u) [CommRing k] (X Y : TopCat)
  [NoZeroDivisors k] [IsPrincipalIdealRing k]
  [∀ (p : ℕ),
      CategoryTheory.Projective
        (HomologicalComplex.homology ((TauCeti.normalizedCubicalChainComplex k).obj X) p)]
  [∀ (q : ℕ),
      CategoryTheory.Projective
        (HomologicalComplex.homology ((TauCeti.normalizedCubicalChainComplex k).obj Y) q)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunneth k X Y n)
```

**The Künneth theorem for split singular chains.** Formalized in Tau Ceti as [`TopCat.isIso_singularHomologyKunneth`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Basic.html#TopCat.isIso_singularHomologyKunneth).

```lean
TopCat.isIso_singularHomologyKunneth.{w} {k : Type w} [CommRing k] (X Y : TopCat)
  (M N : ModuleCat k)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopCat.toSSet.obj X).chainComplex M) p)]
  [∀ (p : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TopCat.toSSet.obj X).chainComplex M) p)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopCat.toSSet.obj Y).chainComplex N) q)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TopCat.toSSet.obj Y).chainComplex N) q)]
  (n : ℕ) : CategoryTheory.IsIso (X.singularHomologyKunneth Y M N n)
```

**The Künneth theorem with projective homology.** Formalized in Tau Ceti as [`TopCat.isIso_singularHomologyKunneth_of_projective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Basic.html#TopCat.isIso_singularHomologyKunneth_of_projective).

```lean
TopCat.isIso_singularHomologyKunneth_of_projective.{w} {k : Type w} [CommRing k] (X Y : TopCat)
  (M N : ModuleCat k)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopCat.toSSet.obj X).chainComplex M) p)]
  [hX :
    ∀ (p : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj M).obj X)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopCat.toSSet.obj Y).chainComplex N) q)]
  [hY :
    ∀ (q : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) q).obj N).obj Y)]
  (n : ℕ) : CategoryTheory.IsIso (X.singularHomologyKunneth Y M N n)
```

**The Künneth theorem with projective homology over any commutative ring.** Formalized in Tau Ceti as [`TopCat.isIso_singularHomologyKunneth_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Basic.html#TopCat.isIso_singularHomologyKunneth_of_projective_homology).

```lean
TopCat.isIso_singularHomologyKunneth_of_projective_homology.{w} {k : Type w} [CommRing k]
  (X Y : TopCat) (M N : ModuleCat k) [Module.Projective k ↑M] [Module.Projective k ↑N]
  [hX :
    ∀ (p : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) p).obj M).obj X)]
  [hY :
    ∀ (q : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) q).obj N).obj Y)]
  (n : ℕ) : CategoryTheory.IsIso (X.singularHomologyKunneth Y M N n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_cubicalHomologyKunneth`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.isIso_cubicalHomologyKunneth)
- [Source of `TauCeti.isIso_cubicalHomologyKunneth` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean#L154)
