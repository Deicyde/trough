---
declaration: theorem
origin: cited
lean: TopPair.isIso_cubicalHomologyKunneth, TopCat.isIso_singularHomologyKunnethRel, TauCeti.isIso_cubicalHomologyKunnethRel_of_projective, TauCeti.isIso_cubicalHomologyKunnethRel, TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing
statement: formalized
proof: formalized
---

# The relative Künneth theorem

if the relative cubical homology modules of a pair
`P = (X, A)` are projective, for instance free, then for every space `Y` the relative Künneth map
`⨁_{p + q = n} Hₚ(X, A; k) ⊗ H_q(Y; k) ⟶ Hₙ(X × Y, A × Y; k)` is an isomorphism, over every
commutative ring `k`.

```lean
TopPair.isIso_cubicalHomologyKunneth.{u} (k : Type u) [CommRing k] (P : TopPair) (Y : TopCat)
  [∀ (p : ℕ),
      Module.Projective k ↑(HomologicalComplex.homology (TopPair.cubicalChainComplex k P) p)]
  (n : ℕ) : CategoryTheory.IsIso (TopPair.cubicalHomologyKunneth k P Y n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Künneth theorem for split complexes](../../algebra/part-02/homology/the-kunneth-theorem-for-split-complexes.md)
- [The relative cubical Eilenberg–Zilber theorem](../singular/the-relative-cubical-eilenberg-zilber-theorem.md)
- [The relative Eilenberg–Zilber theorem](../singular/the-relative-eilenberg-zilber-theorem.md)

## Lean

Formalized in Tau Ceti as [`TopPair.isIso_cubicalHomologyKunneth`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Relative/Kunneth.html#TopPair.isIso_cubicalHomologyKunneth).

## Other forms

**The relative Künneth theorem.** Formalized in Tau Ceti as [`TopCat.isIso_singularHomologyKunnethRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Relative.html#TopCat.isIso_singularHomologyKunnethRel).

```lean
TopCat.isIso_singularHomologyKunnethRel.{w} {k : Type w} [CommRing k] (X Y : TopCat) (B : Set ↑X)
  (R S : ModuleCat k)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopPair.ofSubset B).singularChainComplex R) p)]
  [∀ (p : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TopPair.ofSubset B).singularChainComplex R) p)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TopCat.toSSet.obj Y).chainComplex S) q)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TopCat.toSSet.obj Y).chainComplex S) q)]
  (n : ℕ) : CategoryTheory.IsIso (X.singularHomologyKunnethRel Y B R S n)
```

**The relative Künneth theorem for a pair with projective relative homology.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethRel_of_projective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel_of_projective).

```lean
TauCeti.isIso_cubicalHomologyKunnethRel_of_projective.{u} (k : Type u) [CommRing k] (X : TopCat)
  (P : TopPair)
  [∀ (q : ℕ),
      Module.Projective k ↑(HomologicalComplex.homology (TopPair.cubicalChainComplex k P) q)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethRel k X P n)
```

**The relative Künneth theorem for cubical homology.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel).

```lean
TauCeti.isIso_cubicalHomologyKunnethRel.{u} (k : Type u) [CommRing k] (X : TopCat) (P : TopPair)
  [∀ (p : ℕ),
      CategoryTheory.IsSplitMono
        (HomologicalComplex.iCycles ((TauCeti.normalizedCubicalChainComplex k).obj X) p)]
  [∀ (p : ℕ),
      CategoryTheory.IsSplitEpi
        (HomologicalComplex.homologyπ ((TauCeti.normalizedCubicalChainComplex k).obj X) p)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitMono (HomologicalComplex.iCycles (TopPair.cubicalChainComplex k P) q)]
  [∀ (q : ℕ),
      CategoryTheory.IsSplitEpi (HomologicalComplex.homologyπ (TopPair.cubicalChainComplex k P) q)]
  (n : ℕ) : CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethRel k X P n)
```

**The relative Künneth theorem over a semisimple ring, for instance a field.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing).

```lean
TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing.{u} (k : Type u) [CommRing k]
  (X : TopCat) (P : TopPair) [IsSemisimpleRing k] (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethRel k X P n)
```

## Sources

- [Tau Ceti documentation: `TopPair.isIso_cubicalHomologyKunneth`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Relative/Kunneth.html#TopPair.isIso_cubicalHomologyKunneth)
- [Source of `TopPair.isIso_cubicalHomologyKunneth` in TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Relative/Kunneth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Relative/Kunneth.lean#L190)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
