---
declaration: def
origin: cited
lean: TauCeti.AInfinityRightModule.yonedaHomotopyEquiv
statement: formalized
---

# The Yoneda lemma for right `A∞` modules

Over an `A∞` algebra with a strict unit `e`,
for a module on which `e` is a right unit for the binary operation, evaluation at `e` is a
homotopy equivalence from the morphism complex out of the free module of rank one to the
underlying complex of the module, with homotopy inverse the Yoneda cochains.

```lean
TauCeti.AInfinityRightModule.yonedaHomotopyEquiv.{u} {R A M : Type u} [CommRing R] [AddCommGroup A]
  [_root_.Module R A] [AddCommGroup M] [_root_.Module R M] {AA : TauCeti.AInfinityAlgebra R A}
  (MM : TauCeti.AInfinityRightModule AA M) {e : A} (he : AA.StrictUnit e)
  (hM : ∀ (x : M), ((MM.m 2) x) ![e] = x) :
  HomotopyEquiv (AA.toRightModule.homComplex MM) MM.cochainComplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityRightModule.yonedaHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Yoneda.html#TauCeti.AInfinityRightModule.yonedaHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityRightModule.yonedaHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Yoneda.html#TauCeti.AInfinityRightModule.yonedaHomotopyEquiv)
- [Source of `TauCeti.AInfinityRightModule.yonedaHomotopyEquiv` in TauCeti/Algebra/Homology/AInfinity/Module/Right/Yoneda.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Module/Right/Yoneda.lean#L584)
