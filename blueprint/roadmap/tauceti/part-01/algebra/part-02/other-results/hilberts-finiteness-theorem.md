---
declaration: theorem
origin: cited
lean: TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra
statement: formalized
proof: formalized
---

# Hilbert's finiteness theorem

For a finite-dimensional comodule `V` over a linearly
reductive commutative bialgebra, the invariants of the symmetric algebra `Sym V` form a finitely
generated algebra.

```lean
TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra.{u, v, u_1} {k : Type u} [Field k]
  {H : Type v} [CommSemiring H] [Bialgebra k H] (hH : TauCeti.Coalgebra.IsLinearlyReductive k H)
  (V : Type u_1) [AddCommMonoid V] [_root_.Module k V] [TauCeti.Comodule k H V]
  [Module.Finite k V] : (TauCeti.ComoduleAlgebra.coinvariants k H (SymmetricAlgebra k V)).FG
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/LinearlyReductive.html#TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/LinearlyReductive.html#TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra)
- [Source of `TauCeti.ComoduleAlgebra.fg_coinvariants_symmetricAlgebra` in TauCeti/Algebra/Bialgebra/ComoduleAlgebra/LinearlyReductive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Bialgebra/ComoduleAlgebra/LinearlyReductive.lean#L120)
