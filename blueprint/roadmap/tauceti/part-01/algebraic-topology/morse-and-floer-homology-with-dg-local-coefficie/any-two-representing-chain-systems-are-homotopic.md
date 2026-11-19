---
declaration: theorem
origin: cited
lean: TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy
statement: formalized
proof: formalized
---

# Any two representing chain systems are homotopic

Let `S` and `S'` be twisting chain
systems representing the same classes `μ x y` of `H_{ind x - ind y - 1}(M x y, A x y)`, for
associative composition maps `ι` with values in the subspaces `A x y`. If the maps
`H_{ind x - ind y - 1}(M x y) → H_{ind x - ind y - 1}(M x y, A x y)` are injective whenever
`ind y < ind x`, then there is a homotopy from `S` to `S'`.

For the compactified trajectory spaces of a Morse function, `M x y` is a compact manifold with
corners of dimension `ind x - ind y - 1` and boundary `A x y`, which has no homology in that
degree, so the injectivity holds. The push-forwards of the homotopy then relate the
Barraud–Cornea cocycles of `S` and `S'` by a continuation cocycle
(`TauCeti.TwistingChainSystem.Homotopy.continuationCocycle`).

```lean
TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy.{u, u_1} {P : Type u_1} [Fintype P]
  {ind : P → ℤ} {M : P → P → TopCat} {ι : (x y z : P) → C(↑(M x y) × ↑(M y z), ↑(M x z))}
  {k : Type u} [CommRing k] {A : (x y : P) → Set ↑(M x y)}
  {μ :
    (x y : P) →
      ↑(HomologicalComplex.homology (TopPair.cubicalChainComplex k (TopPair.ofSubset (A x y)))
          (ind x - ind y - 1).toNat)}
  {S S' : TauCeti.TwistingChainSystem ind ι k}
  (hS : TauCeti.TwistingChainSystem.IsRepresenting A S μ)
  (hS' : TauCeti.TwistingChainSystem.IsRepresenting A S' μ)
  (hι :
    ∀ (x w z y : P) (a : ↑(M x w)) (b : ↑(M w z)) (c : ↑(M z y)),
      (ι x z y) ((ι x w z) (a, b), c) = (ι x w y) (a, (ι w z y) (b, c)))
  (hA : ∀ (x z y : P) (p : ↑(M x z) × ↑(M z y)), (ι x z y) p ∈ A x y)
  (hinj :
    ∀ (x y : P),
      ind y < ind x →
        Function.Injective
          ⇑(ModuleCat.Hom.hom
              (HomologicalComplex.homologyMap
                (CategoryTheory.Limits.cokernel.π
                  ((TauCeti.normalizedCubicalChainComplex k).map TopPair.map))
                (ind x - ind y - 1).toNat))) :
  Nonempty (S.Homotopy S')
```

## Depends on

- [TauCeti.TwistingChainSystem](tauceti-twistingchainsystem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/ChainSystemHomotopy.html#TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/ChainSystemHomotopy.html#TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy)
- [Source of `TauCeti.TwistingChainSystem.IsRepresenting.nonempty_homotopy` in TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/ChainSystemHomotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/MonoidAlgebra/ChainSystemHomotopy.lean#L304)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
