---
declaration: theorem
origin: cited
lean: TauCeti.etale_aeval_of_basis
statement: formalized
proof: formalized
---

# The Jacobian criterion for étaleness

If `T` is smooth over `R` and the differentials
`d aᵢ` of elements `aᵢ` of `T` form a basis of `Ω[T⁄R]`, then `T` is étale over the
polynomial ring `R[Xᵢ]` via `Xᵢ ↦ aᵢ`. The index type is then automatically finite unless `T` is
trivial.

```lean
TauCeti.etale_aeval_of_basis.{u_1, u_3, u_4} {R : Type u_1} {T : Type u_3} [CommRing R] [CommRing T]
  [Algebra R T] [Algebra.Smooth R T] {ι : Type u_4} (a : ι → T) (b : Module.Basis ι T Ω[T⁄R])
  (hb : ∀ (i : ι), b i = (KaehlerDifferential.D R T) (a i)) : (MvPolynomial.aeval a).Etale
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.etale_aeval_of_basis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Kaehler/FormallyEtale.html#TauCeti.etale_aeval_of_basis).

## Sources

- [Tau Ceti documentation: `TauCeti.etale_aeval_of_basis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Kaehler/FormallyEtale.html#TauCeti.etale_aeval_of_basis)
- [Source of `TauCeti.etale_aeval_of_basis` in TauCeti/RingTheory/Kaehler/FormallyEtale.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Kaehler/FormallyEtale.lean#L150)
