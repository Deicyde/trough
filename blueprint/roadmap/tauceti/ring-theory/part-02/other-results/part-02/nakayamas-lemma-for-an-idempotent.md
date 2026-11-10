---
declaration: theorem
origin: cited
lean: IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem
statement: formalized
proof: formalized
---

# Nakayama's lemma for an idempotent

Let `T` be a module-finite `S`-algebra and `J` an
ideal of `S` in the Jacobson radical. If an idempotent `e` of `T` satisfies `e T ⊆ S e + JT`, then
`e T = S e`.

```lean
IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem.{u_2, u_3} {S : Type u_2} {T : Type u_3}
  [CommRing S] [CommRing T] [Algebra S T] [Module.Finite S T] {J : Ideal S} (hJ : J ≤ ⊥.jacobson)
  {e : T} (he : IsIdempotentElem e)
  (h : ∀ (x : T), ∃ s, e * x - s • e ∈ Ideal.map (algebraMap S T) J) (x : T) : ∃ s, s • e = e * x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Idempotents/Jacobson.html#IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem).

## Sources

- [Tau Ceti documentation: `IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Idempotents/Jacobson.html#IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem)
- [Source of `IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem` in TauCeti/RingTheory/Idempotents/Jacobson.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Idempotents/Jacobson.lean#L94)
