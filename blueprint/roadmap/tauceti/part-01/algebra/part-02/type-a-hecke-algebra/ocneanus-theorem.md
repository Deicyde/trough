---
declaration: theorem
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace, TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace
statement: formalized
proof: formalized
---

# Ocneanu's theorem

Every Markov trace with parameter `z` is the Ocneanu trace.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace.{u_1} {R : Type u_1} [CommRing R]
  {q : Rˣ} {z : R} {τ : TauCeti.InfiniteTypeAHeckeAlgebra R q →ₗ[R] R}
  (hτ : TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ) :
  τ = TauCeti.InfiniteTypeAHeckeAlgebra.ocneanuTrace R q z
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](../../part-01/type-a-hecke-algebras-braid-traces-and-positive/tauceti-infinitetypeaheckealgebra.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra.stage](../../part-01/type-a-hecke-algebras-braid-traces-and-positive/tauceti-infinitetypeaheckealgebra-stage.md)

## Proof depends on

- [The basis theorem](the-basis-theorem.md)
- [Matsumoto's theorem, relational form](../../../group-theory/coxeter/matsumotos-theorem-relational-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace).

## Other forms

**Ocneanu's theorem.** Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace).

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace.{u_1} {R : Type u_1} [CommRing R]
  {q : Rˣ} (z : R) : ∃! τ, TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ
```

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace` in TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.lean#L488)
