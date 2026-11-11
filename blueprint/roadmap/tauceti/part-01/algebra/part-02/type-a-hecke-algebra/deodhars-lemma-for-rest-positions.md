---
declaration: theorem
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem, TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_mem_of_mem
statement: formalized
proof: formalized
---

# Deodhar's lemma for rest positions

If neither position crossed by `T i` is selected in
`S`, then `T i` passes through the inverse shuffle word of `S` and becomes the generator crossing
the corresponding two of the last `l` positions: the first position `strand i` is the
`S.restIndex (strand i)`-th rest position.

```lean
TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem.{u_1} {k l : ℕ} {R : Type u_1}
  [CommRing R] {q : Rˣ} {i : Fin (k + l - 1)} {S : TauCeti.TypeAHeckeAlgebra.ShuffleMask k l}
  (ha : TauCeti.BraidGroup.strand i ∉ ↑S) (hb : TauCeti.BraidGroup.strandSucc i ∉ ↑S) :
  TauCeti.TypeAHeckeAlgebra.T q i * TauCeti.TypeAHeckeAlgebra.shuffleInvWord q S =
    TauCeti.TypeAHeckeAlgebra.shuffleInvWord q S *
      TauCeti.TypeAHeckeAlgebra.T q ⟨k + S.restIndex (TauCeti.BraidGroup.strand i), ⋯⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Shuffle/Induced.html#TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem).

## Other forms

**Deodhar's lemma for selected positions.** Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_mem_of_mem`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Shuffle/Induced.html#TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_mem_of_mem).

```lean
TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_mem_of_mem.{u_1} {k l : ℕ} {R : Type u_1}
  [CommRing R] {q : Rˣ} {i : Fin (k + l - 1)} {S : TauCeti.TypeAHeckeAlgebra.ShuffleMask k l}
  (ha : TauCeti.BraidGroup.strand i ∈ ↑S) (hb : TauCeti.BraidGroup.strandSucc i ∈ ↑S) :
  TauCeti.TypeAHeckeAlgebra.T q i * TauCeti.TypeAHeckeAlgebra.shuffleInvWord q S =
    TauCeti.TypeAHeckeAlgebra.shuffleInvWord q S *
      TauCeti.TypeAHeckeAlgebra.T q ⟨↑i - S.restIndex (TauCeti.BraidGroup.strand i), ⋯⟩
```

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Shuffle/Induced.html#TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem)
- [Source of `TauCeti.TypeAHeckeAlgebra.T_mul_shuffleInvWord_of_notMem_of_notMem` in TauCeti/Algebra/TypeAHeckeAlgebra/Shuffle/Induced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TypeAHeckeAlgebra/Shuffle/Induced.lean#L321)
