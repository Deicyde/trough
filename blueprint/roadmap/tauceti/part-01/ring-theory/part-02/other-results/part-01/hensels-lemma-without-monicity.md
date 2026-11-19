---
declaration: theorem
origin: cited
lean: Polynomial.exists_isRoot_sub_mem
statement: formalized
proof: formalized
---

# Hensel's lemma without monicity

Over a Henselian pair `(R, J)`, a simple root of a
polynomial modulo `J` lifts to a root with the same image in `R ⧸ J`, whether or not the polynomial
is monic.

```lean
Polynomial.exists_isRoot_sub_mem.{u_1} {R : Type u_1} [CommRing R] {J : Ideal R} [HenselianRing R J]
  (f : Polynomial R) {a₀ : R} (h₁ : Polynomial.eval a₀ f ∈ J)
  (h₂ : IsUnit ((Ideal.Quotient.mk J) (Polynomial.eval a₀ (Polynomial.derivative f)))) :
  ∃ a, f.IsRoot a ∧ a - a₀ ∈ J
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.exists_isRoot_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Basic.html#Polynomial.exists_isRoot_sub_mem).

## Sources

- [Tau Ceti documentation: `Polynomial.exists_isRoot_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Basic.html#Polynomial.exists_isRoot_sub_mem)
- [Source of `Polynomial.exists_isRoot_sub_mem` in TauCeti/RingTheory/Henselian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Henselian/Basic.lean#L202)
