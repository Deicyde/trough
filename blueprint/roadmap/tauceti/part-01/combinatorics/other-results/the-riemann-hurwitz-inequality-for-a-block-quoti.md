---
declaration: theorem
origin: cited
lean: TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient
statement: formalized
proof: formalized
---

# The Riemann–Hurwitz inequality for a block quotient

The Euler characteristic of a triple
with transitive monodromy is at most `|B|` times that of its quotient by a nonempty block `B`.

```lean
TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient {n m : ℕ}
  {t : TauCeti.PermutationTriple n} {B : Set (Fin n)}
  (e : ↑(MulAction.orbit (↥t.monodromyGroup) B) ≃ Fin m)
  (ht : MulAction.IsPretransitive (↥t.monodromyGroup) (Fin n))
  (hB : MulAction.IsBlock (↥t.monodromyGroup) B) (hBne : B.Nonempty) :
  t.eulerChar ≤ ↑B.ncard * (t.blockQuotient B e).eulerChar
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/BlockQuotient.html#TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/BlockQuotient.html#TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient)
- [Source of `TauCeti.PermutationTriple.eulerChar_le_ncard_mul_eulerChar_blockQuotient` in TauCeti/Combinatorics/PermutationTriple/BlockQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/PermutationTriple/BlockQuotient.lean#L584)
