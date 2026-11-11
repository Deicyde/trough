---
declaration: theorem
origin: cited
lean: TauCeti.skolemNoether
statement: formalized
proof: formalized
---

# The Skolem-Noether theorem

Two `K`-algebra homomorphisms `f g : B →ₐ[K] A` from a
finite-dimensional **central simple** `K`-algebra `B` to a finite-dimensional **simple** `K`-algebra
`A` are conjugate: there is a unit `u` of `A` with `g x = u * f x * u⁻¹` for all `x : B`.

Finite-dimensionality of `B` is not among the hypotheses: it follows from them, because `f` is
injective, `B` being simple and `A` nontrivial. The proof does use it, to make `B ⊗[K] Aᵐᵒᵖ`
Artinian, and with it the classification of modules that produces the conjugating isomorphism.

```lean
TauCeti.skolemNoether.{u_1, u_2, u_3} (K : Type u_1) {A : Type u_2} {B : Type u_3} [Field K]
  [Ring A] [Algebra K A] [Ring B] [Algebra K B] [IsSimpleRing A] [FiniteDimensional K A]
  [Algebra.IsCentral K B] [IsSimpleRing B] (f g : B →ₐ[K] A) : ∃ u, ∀ (x : B), g x = ↑u * f x * ↑u⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.skolemNoether`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/SkolemNoether.html#TauCeti.skolemNoether).

## Sources

- [Tau Ceti documentation: `TauCeti.skolemNoether`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/SkolemNoether.html#TauCeti.skolemNoether)
- [Source of `TauCeti.skolemNoether` in TauCeti/Algebra/CentralSimple/SkolemNoether.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/CentralSimple/SkolemNoether.lean#L100)
