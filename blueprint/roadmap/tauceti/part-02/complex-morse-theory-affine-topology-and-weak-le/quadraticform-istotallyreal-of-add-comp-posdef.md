---
declaration: theorem
origin: cited
lean: QuadraticForm.isTotallyReal_of_add_comp_posDef
statement: formalized
proof: formalized
---

# QuadraticForm.isTotallyReal\_of\_add\_comp\_posDef

A submodule on which `Q` is nonpositive is totally real for a linear endomorphism `J` if
`Q(v) + Q(Jv)` is positive for every nonzero `v`.

```lean
QuadraticForm.isTotallyReal_of_add_comp_posDef.{u_1, u_2} {R : Type u_1} {E : Type u_2}
  [CommSemiring R] [PartialOrder R] [IsOrderedAddMonoid R] [AddCommMonoid E] [_root_.Module R E]
  (Q : QuadraticForm R E) {W : Submodule R E} (J : E →ₗ[R] E)
  (hQJ : QuadraticMap.PosDef (Q + QuadraticMap.comp Q J)) (hW : ∀ v ∈ W, Q v ≤ 0) :
  TauCeti.IsTotallyReal J W
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticForm.isTotallyReal_of_add_comp_posDef`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TotallyReal/QuadraticForm.html#QuadraticForm.isTotallyReal_of_add_comp_posDef).

## Sources

- [Tau Ceti documentation: `QuadraticForm.isTotallyReal_of_add_comp_posDef`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TotallyReal/QuadraticForm.html#QuadraticForm.isTotallyReal_of_add_comp_posDef)
- [Source of `QuadraticForm.isTotallyReal_of_add_comp_posDef` in TauCeti/LinearAlgebra/TotallyReal/QuadraticForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/TotallyReal/QuadraticForm.lean#L56)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
