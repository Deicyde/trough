---
declaration: def
origin: cited
lean: LinearIndependent.natSpanHeight
statement: formalized
---

# LinearIndependent.natSpanHeight

The height of an element of the nonnegative span of an independent family is the sum of
its coordinates. For simple roots, this is the usual root height on the positive root cone.

```lean
LinearIndependent.natSpanHeight.{u_1, u_2} {ι : Type u_1} {M : Type u_2} [AddCommMonoid M]
  {v : ι → M} (hv : LinearIndependent ℕ v) : ↥(Submodule.span ℕ (Set.range v)) →+ ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearIndependent.natSpanHeight`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.html#LinearIndependent.natSpanHeight).

## Sources

- [Tau Ceti documentation: `LinearIndependent.natSpanHeight`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.html#LinearIndependent.natSpanHeight)
- [Source of `LinearIndependent.natSpanHeight` in TauCeti/LinearAlgebra/LinearIndependent/NatSpan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.lean#L45)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
