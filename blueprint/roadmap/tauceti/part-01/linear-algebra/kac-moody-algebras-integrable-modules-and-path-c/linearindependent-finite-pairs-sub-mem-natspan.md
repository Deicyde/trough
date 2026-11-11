---
declaration: theorem
origin: cited
lean: LinearIndependent.finite_pairs_sub_mem_natSpan
statement: formalized
proof: formalized
---

# LinearIndependent.finite_pairs_sub_mem_natSpan

Only finitely many pairs in two translated negative cones have a prescribed sum.
This gives finite convolution coefficients for functions supported in such cones.

```lean
LinearIndependent.finite_pairs_sub_mem_natSpan.{u_1, u_2} {ι : Type u_1} {M : Type u_2}
  [AddCommGroup M] {v : ι → M} (hv : LinearIndependent ℕ v) (lam μ ξ : M) :
  {p |
      lam - p.1 ∈ Submodule.span ℕ (Set.range v) ∧
        μ - p.2 ∈ Submodule.span ℕ (Set.range v) ∧ p.1 + p.2 = ξ}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearIndependent.finite_pairs_sub_mem_natSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.html#LinearIndependent.finite_pairs_sub_mem_natSpan).

## Sources

- [Tau Ceti documentation: `LinearIndependent.finite_pairs_sub_mem_natSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.html#LinearIndependent.finite_pairs_sub_mem_natSpan)
- [Source of `LinearIndependent.finite_pairs_sub_mem_natSpan` in TauCeti/LinearAlgebra/LinearIndependent/NatSpan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/LinearIndependent/NatSpan.lean#L143)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
