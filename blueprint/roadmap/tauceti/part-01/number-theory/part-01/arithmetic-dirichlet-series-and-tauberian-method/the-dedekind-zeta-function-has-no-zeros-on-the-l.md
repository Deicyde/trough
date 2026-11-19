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
- [Source of `TauCeti.ne_zero_of_eqOn_dedekindZeta` in TauCeti/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/DedekindZeta.lean#L190)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ArithmeticDirichletSeries/STATUS.md)
