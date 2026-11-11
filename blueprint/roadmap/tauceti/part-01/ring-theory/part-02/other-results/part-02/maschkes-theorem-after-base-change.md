---
declaration: theorem
origin: cited
lean: MonoidAlgebra.isSemisimpleRing_tensor
statement: formalized
proof: formalized
---

# Maschke's theorem after base change

If `k` is a field in which the order of the finite
group `G` is nonzero, then the base change `R[G] ⊗[R] k` of the group algebra over any commutative
ring `R` mapping to `k` is a semisimple ring, being isomorphic to `k[G]`.

```lean
MonoidAlgebra.isSemisimpleRing_tensor.{u_1, u_2, u_3} (R : Type u_1) [CommRing R] (k : Type u_2)
  [Field k] [Algebra R k] (G : Type u_3) [Group G] [Finite G] [NeZero ↑(Nat.card G)] :
  IsSemisimpleRing (TensorProduct R (MonoidAlgebra R G) k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonoidAlgebra.isSemisimpleRing_tensor`](https://taucetiproject.org/docs/TauCeti/RingTheory/TensorProduct/MonoidAlgebra.html#MonoidAlgebra.isSemisimpleRing_tensor).

## Sources

- [Tau Ceti documentation: `MonoidAlgebra.isSemisimpleRing_tensor`](https://taucetiproject.org/docs/TauCeti/RingTheory/TensorProduct/MonoidAlgebra.html#MonoidAlgebra.isSemisimpleRing_tensor)
- [Source of `MonoidAlgebra.isSemisimpleRing_tensor` in TauCeti/RingTheory/TensorProduct/MonoidAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/TensorProduct/MonoidAlgebra.lean#L98)
