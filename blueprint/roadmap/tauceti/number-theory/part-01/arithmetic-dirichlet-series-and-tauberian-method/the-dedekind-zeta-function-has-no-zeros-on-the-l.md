---
declaration: theorem
origin: cited
lean: TauCeti.ne_zero_of_eqOn_dedekindZeta
statement: formalized
proof: formalized
---

# The Dedekind zeta function has no zeros on the line `Re s = 1` away from its pole

If `f`
agrees with `ζ_K` on `Re s > 1` and is complex differentiable at a point `s ≠ 1` with `Re s = 1`,
then `f s ≠ 0`. By `exists_differentiableOn_eq_dedekindZeta_sub`, such an `f` exists: the
meromorphic continuation of `ζ_K`.

```lean
TauCeti.ne_zero_of_eqOn_dedekindZeta.{u_1} {K : Type u_1} [Field K] [NumberField K] {f : ℂ → ℂ}
  {s : ℂ} (hs : s.re = 1) (hs1 : s ≠ 1) (hf : DifferentiableAt ℂ f s)
  (hfζ : Set.EqOn f (NumberField.dedekindZeta K) {z | 1 < z.re}) : f s ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ne_zero_of_eqOn_dedekindZeta`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/DedekindZeta.html#TauCeti.ne_zero_of_eqOn_dedekindZeta).

## Sources

- [Tau Ceti documentation: `TauCeti.ne_zero_of_eqOn_dedekindZeta`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/DedekindZeta.html#TauCeti.ne_zero_of_eqOn_dedekindZeta)
- [Source of `TauCeti.ne_zero_of_eqOn_dedekindZeta` in TauCeti/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/DedekindZeta.lean#L192)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
