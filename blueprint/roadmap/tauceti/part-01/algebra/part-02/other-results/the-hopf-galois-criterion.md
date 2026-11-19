---
declaration: theorem
origin: cited
lean: TauCeti.ComoduleAlgebra.surjective_galoisMap_iff
statement: formalized
proof: formalized
---

# The Hopf–Galois criterion

Let `H` be a commutative Hopf algebra which is a finite
projective `R`-module, so that `G = Spec H` is a finite locally free group scheme over `Spec R`,
and let `A` be a commutative `H`-comodule algebra. The action of `G` on `Spec A` is free, in the
sense that the Galois map `A ⊗[R] A → A ⊗[R] H` is surjective, if and only if `A` is faithfully
flat over its coinvariants `A^{co H}` and the Galois map `A ⊗[A^{co H}] A → A ⊗[R] H` is
bijective, that is, `Spec A ⟶ Spec A^{co H}` is a `G`-torsor.

```lean
TauCeti.ComoduleAlgebra.surjective_galoisMap_iff.{u, u_1} {R : Type u_1} {H A : Type u} [CommRing R]
  [CommRing H] [HopfAlgebra R H] [CommRing A] [Algebra R A] [TauCeti.ComoduleAlgebra R H A]
  [Module.Finite R H] [Module.Projective R H] :
  Function.Surjective ⇑(TauCeti.ComoduleAlgebra.galoisMap R ⋯) ↔
    Module.FaithfullyFlat (↥(TauCeti.ComoduleAlgebra.coinvariants R H A)) A ∧
      Function.Bijective
        ⇑(TauCeti.ComoduleAlgebra.galoisMap ↥(TauCeti.ComoduleAlgebra.coinvariants R H A) ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton on a finite projective module](../../../linear-algebra/part-02/other-results/cayley-hamilton-on-a-finite-projective-module.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ComoduleAlgebra.surjective_galoisMap_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/Free.html#TauCeti.ComoduleAlgebra.surjective_galoisMap_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ComoduleAlgebra.surjective_galoisMap_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/Free.html#TauCeti.ComoduleAlgebra.surjective_galoisMap_iff)
- [Source of `TauCeti.ComoduleAlgebra.surjective_galoisMap_iff` in TauCeti/Algebra/Bialgebra/ComoduleAlgebra/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/Free.lean#L285)
