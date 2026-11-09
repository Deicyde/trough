---
declaration: def
origin: cited
lean: TauCeti.leviForm
statement: formalized
---

# TauCeti.leviForm

The **Levi form** of a real function `f` at `x`: the sesquilinear form
`(D²f(x)(v, w) + D²f(x)(I • v, I • w) + I * (D²f(x)(I • v, w) - D²f(x)(v, I • w))) / 4`,
conjugate-linear in `v` and complex-linear in `w`. Its matrix entries in holomorphic coordinates
are the Wirtinger derivatives, with the arguments reversed: for `C²` `f` and coordinate vectors
`e_j`, `leviForm f x (e_k) (e_j) = ∂²f / ∂z_j ∂(conj z_k)`.

```lean
TauCeti.leviForm.{u_1} {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℂ V] (f : V → ℝ) (x : V) :
  V →ₗ⋆[ℂ] V →ₗ[ℂ] ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.leviForm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LeviForm.html#TauCeti.leviForm).

## Sources

- [Tau Ceti documentation: `TauCeti.leviForm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LeviForm.html#TauCeti.leviForm)
- [Source of `TauCeti.leviForm` in TauCeti/Analysis/Complex/LeviForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/LeviForm.lean#L114)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
