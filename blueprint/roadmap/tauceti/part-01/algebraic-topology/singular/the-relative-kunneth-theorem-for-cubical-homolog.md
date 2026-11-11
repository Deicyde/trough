---
declaration: theorem
origin: cited
lean: TauCeti.isIso_cubicalHomologyKunnethRel, TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing
statement: formalized
proof: formalized
---

# The relative Künneth theorem for cubical homology

if the cycles of `N(X)` and `N(Y, B)`
split off their terms and their homology splits off the cycles, the relative Künneth map
`⨁_{p + q = n} Hₚ(X; k) ⊗ H_q(Y, B; k) ⟶ Hₙ(X × Y, X × B; k)` is an isomorphism.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Künneth theorem for split complexes](../../algebra/part-02/homology/the-kunneth-theorem-for-split-complexes.md)
- [The relative cubical Eilenberg–Zilber theorem](the-relative-cubical-eilenberg-zilber-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel).

## Other forms

**The relative Künneth theorem over a semisimple ring, for instance a field.** Formalized in Tau Ceti as [`TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing).

```lean
TauCeti.isIso_cubicalHomologyKunnethRel_of_isSemisimpleRing.{u} (k : Type u) [CommRing k]
  (X : TopCat) (P : TopPair) [IsSemisimpleRing k] (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.cubicalHomologyKunnethRel k X P n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_cubicalHomologyKunnethRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.isIso_cubicalHomologyKunnethRel)
- [Source of `TauCeti.isIso_cubicalHomologyKunnethRel` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.lean#L275)
