---
declaration: theorem
origin: cited
lean: TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq, TauCeti.FormalVertexAxioms.eq_field_of_ncoeff_apply_vacuum_eq
statement: formalized
proof: formalized
---

# Goddard's uniqueness theorem

Two fields that are local to every field `Y(a,z)` of a
formal vertex algebra and agree on the vacuum are equal.

```lean
TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq.{u_1, u_2} {R : Type u_1} {V : Type u_2}
  [CommRing R] [AddCommGroup V] [_root_.Module R V] (A : TauCeti.FormalVertexAxioms R V)
  {B C : VertexOperator R V} (hB : ∀ (a : V), ∃ N, B.IsLocalOfOrder (A.field a) N)
  (hC : ∀ (a : V), ∃ N, C.IsLocalOfOrder (A.field a) N)
  (h : ∀ (n : ℤ), (VertexOperator.ncoeff B n) A.vacuum = (VertexOperator.ncoeff C n) A.vacuum) :
  B = C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Vertex/Axioms.html#TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq).

## Other forms

**Goddard's uniqueness theorem, field form.** Formalized in Tau Ceti as [`TauCeti.FormalVertexAxioms.eq_field_of_ncoeff_apply_vacuum_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Vertex/Axioms.html#TauCeti.FormalVertexAxioms.eq_field_of_ncoeff_apply_vacuum_eq).

```lean
TauCeti.FormalVertexAxioms.eq_field_of_ncoeff_apply_vacuum_eq.{u_1, u_2} {R : Type u_1}
  {V : Type u_2} [CommRing R] [AddCommGroup V] [_root_.Module R V]
  (A : TauCeti.FormalVertexAxioms R V) {B : VertexOperator R V} {b : V}
  (hB : ∀ (a : V), ∃ N, B.IsLocalOfOrder (A.field a) N)
  (h :
    ∀ (n : ℤ),
      (VertexOperator.ncoeff B n) A.vacuum = (VertexOperator.ncoeff (A.field b) n) A.vacuum) :
  B = A.field b
```

## Sources

- [Tau Ceti documentation: `TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Vertex/Axioms.html#TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq)
- [Source of `TauCeti.FormalVertexAxioms.eq_of_ncoeff_apply_vacuum_eq` in TauCeti/Algebra/Vertex/Axioms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Vertex/Axioms.lean#L202)
