---
declaration: def
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.basisTw
statement: formalized
---

# The basis theorem

the elements `T_w`, `w : W`, form a basis of the type-A Hecke algebra
over every commutative ring and for every unit parameter.

```lean
TauCeti.TypeAHeckeAlgebra.basisTw.{u_1, u_2} {R : Type u_1} [CommRing R] (q : Rˣ) {n : ℕ}
  {W : Type u_2} [Group W] (cs : CoxeterSystem (CoxeterMatrix.A (n - 1)) W) :
  Module.Basis W R (TauCeti.TypeAHeckeAlgebra R q n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Matsumoto's theorem, relational form](../../group-theory/coxeter/matsumotos-theorem-relational-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.basisTw`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Basis.html#TauCeti.TypeAHeckeAlgebra.basisTw).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.basisTw`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Basis.html#TauCeti.TypeAHeckeAlgebra.basisTw)
- [Source of `TauCeti.TypeAHeckeAlgebra.basisTw` in TauCeti/Algebra/TypeAHeckeAlgebra/Basis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/Basis.lean#L140)
