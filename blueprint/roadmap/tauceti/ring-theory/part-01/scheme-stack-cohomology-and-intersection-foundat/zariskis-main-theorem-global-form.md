---
declaration: theorem
origin: cited
lean: Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top
statement: formalized
proof: formalized
---

# Zariski's main theorem, global form

A quasi-finite algebra `A` of finite type over `R`
has a module-finite subalgebra `A'` and finitely many elements `r ∈ A'` generating the unit ideal
of `A`, such that for every `x ∈ A` and every such `r`, all large enough powers of `r` move `x`
into `A'`. Geometrically, `Spec A` is covered by finitely many basic opens `D(r)` on which it
agrees with the finite `R`-scheme `Spec A'`.

```lean
Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top.{u_1, u_2} {R : Type u_1} {A : Type u_2}
  [CommRing R] [CommRing A] [Algebra R A] [Algebra.FiniteType R A] [Algebra.QuasiFinite R A] :
  ∃ A' s,
    (Subalgebra.toSubmodule A').FG ∧
      ↑s ⊆ ↑A' ∧ Ideal.span ↑s = ⊤ ∧ ∀ r ∈ s, ∀ (x : A), ∀ᶠ (m : ℕ) in Filter.atTop, r ^ m * x ∈ A'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/QuasiFinite/ZariskisMainTheorem.html#Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top).

## Sources

- [Tau Ceti documentation: `Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/QuasiFinite/ZariskisMainTheorem.html#Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top)
- [Source of `Algebra.QuasiFinite.exists_fg_subalgebra_and_span_eq_top` in TauCeti/RingTheory/QuasiFinite/ZariskisMainTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/QuasiFinite/ZariskisMainTheorem.lean#L41)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
