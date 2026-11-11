---
declaration: theorem
origin: cited
lean: SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι
statement: formalized
proof: formalized
---

# SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι

Over a commutative rational algebra, an element of a symmetric algebra is
primitive exactly when it is a generator.

```lean
SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommRing R] [Algebra ℚ R] [AddCommMonoid M] [_root_.Module R M] (p : SymmetricAlgebra R M) :
  Bialgebra.IsPrimitiveElem R p ↔ p ∈ Set.range ⇑(SymmetricAlgebra.ι R M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Primitive.html#SymmetricAlgebra.isPrimitiveElem_iff_mem_range_%CE%B9).

## Sources

- [Tau Ceti documentation: `SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Primitive.html#SymmetricAlgebra.isPrimitiveElem_iff_mem_range_%CE%B9)
- [Source of `SymmetricAlgebra.isPrimitiveElem_iff_mem_range_ι` in TauCeti/LinearAlgebra/SymmetricAlgebra/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SymmetricAlgebra/Primitive.lean#L43)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
