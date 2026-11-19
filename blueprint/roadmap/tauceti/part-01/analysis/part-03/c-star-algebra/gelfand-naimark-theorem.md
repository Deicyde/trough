---
declaration: theorem
origin: cited
lean: TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation, TauCeti.CStarAlgebra.exists_faithful_representation
statement: formalized
proof: formalized
---

# Gelfand–Naimark theorem

Every C⋆-algebra `A`, possibly nonunital and nonseparable, has a
faithful nondegenerate representation on a Hilbert space in the universe of `A`: the Hilbert
direct sum of the GNS representations of all positive functionals on `A`. For the zero algebra the
Hilbert space is zero.

```lean
TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation.{w} (A : Type w)
  [NonUnitalCStarAlgebra A] :
  ∃ H x x_1, ∃ (x_2 : CompleteSpace H), ∃ π, Function.Injective ⇑π ∧ π.IsNondegenerate
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Representation/GNS.html#TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation).

## Other forms

**Gelfand–Naimark theorem, unital form.** Formalized in Tau Ceti as [`TauCeti.CStarAlgebra.exists_faithful_representation`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Representation/GNS.html#TauCeti.CStarAlgebra.exists_faithful_representation).

```lean
TauCeti.CStarAlgebra.exists_faithful_representation.{w} (B : Type w) [CStarAlgebra B] :
  ∃ H x x_1, ∃ (x_2 : CompleteSpace H), ∃ π, Function.Injective ⇑π
```

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Representation/GNS.html#TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation)
- [Source of `TauCeti.CStarAlgebra.exists_faithful_nondegenerate_representation` in TauCeti/Analysis/CStarAlgebra/Representation/GNS.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Representation/GNS.lean#L93)
