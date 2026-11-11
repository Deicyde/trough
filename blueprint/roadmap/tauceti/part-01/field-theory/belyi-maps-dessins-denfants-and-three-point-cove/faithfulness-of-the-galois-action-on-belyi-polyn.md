---
declaration: theorem
origin: cited
lean: TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map
statement: formalized
proof: formalized
---

# Faithfulness of the Galois action on Belyi polynomials

Let `K` be a field algebraic over
`ℚ`, such as `AlgebraicClosure ℚ`. For every field endomorphism `σ ≠ id` of `K` there is a
nonconstant polynomial `P` over `K` with all its critical values in `{0, 1}`, in every field
extension of `K`, such that no affine change of variable carries `P` to its conjugate `P^σ`.

```lean
TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map.{v, u_1} {K : Type u_1} [Field K]
  [CharZero K] [Algebra.IsAlgebraic ℚ K] {σ : K →+* K} (hσ : σ ≠ RingHom.id K) :
  ∃ P,
    0 < P.natDegree ∧
      (∀ (L : Type v) [inst : Field L] [inst_1 : Algebra K L],
          Polynomial.criticalValues L P ⊆ {0, 1}) ∧
        ∀ (a b : K),
          a ≠ 0 → P.comp (Polynomial.C a * Polynomial.X + Polynomial.C b) ≠ Polynomial.map σ P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Lenstra/Belyi.html#TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Lenstra/Belyi.html#TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map)
- [Source of `TauCeti.exists_polynomial_criticalValues_subset_comp_ne_map` in TauCeti/Algebra/Polynomial/Lenstra/Belyi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Polynomial/Lenstra/Belyi.lean#L156)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
