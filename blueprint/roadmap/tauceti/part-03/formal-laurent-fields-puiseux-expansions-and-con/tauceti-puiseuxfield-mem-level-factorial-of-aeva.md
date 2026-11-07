---
declaration: theorem
origin: cited
lean: TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.puiseuxField.mem\_level\_factorial\_of\_aeval\_eq\_zero

If `K` contains all roots of unity, then a Puiseux series that is a root of a nonzero
polynomial of degree `d` over `K⸨X⸩` lies in level `d!`. Thus all roots of such a polynomial lie in
a common level.

```lean
TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero.{u_1} {K : Type u_1} [Field K]
  [∀ (n : ℕ+), HasEnoughRootsOfUnity K ↑n] {p : Polynomial (LaurentSeries K)} (hp : p ≠ 0)
  {x : ↥(TauCeti.puiseuxField K)} (hx : (Polynomial.aeval x) p = 0) :
  x ∈ TauCeti.puiseuxField.level K p.natDegree.factorial.toPNat'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.puiseuxField.levelGalEquivRootsOfUnity](tauceti-puiseuxfield-levelgalequivrootsofunity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero)
- [Source of `TauCeti.puiseuxField.mem_level_factorial_of_aeval_eq_zero` in TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean#L107)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
