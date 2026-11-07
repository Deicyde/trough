---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq
statement: formalized
proof: formalized
---

# `GL₂(ℤ/Nℤ)` acts freely on `𝕄(𝒫, [Γ(N)])`

for every rigid `𝒫`. Let `V` represent the
simultaneous problem `(𝒫, [Γ(N)])` with the naive full level-`N` problem, on which `GL₂(ℤ/Nℤ)` acts
by change of basis. If a point of `V.base` with values in a nonempty scheme is fixed by a matrix
`g`, then `g = 1`. For `N = 3` this is the freeness of the action of `GL₂(𝔽₃)` on the moduli scheme
of `𝒫` rigidified by naive level-three structures.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq.{u}
  {B : AlgebraicGeometry.Scheme} {P : TauCeti.AlgebraicGeometry.ModuliProblem B}
  {V : TauCeti.AlgebraicGeometry.EllObj B} {N : ℕ} (hP : P.IsRigid)
  (R :
    CategoryTheory.Functor.RepresentableBy
      (CategoryTheory.MonoidalCategoryStruct.tensorObj P
        (TauCeti.AlgebraicGeometry.ModuliProblem.gammaNaive B N))
      V)
  {T : AlgebraicGeometry.Scheme} [Nonempty ↥T] {x : T ⟶ V.base} {g : (GL (Fin 2) (ZMod N))ᵐᵒᵖ}
  (hx :
    CategoryTheory.CategoryStruct.comp x
        ((TauCeti.AlgebraicGeometry.ModuliProblem.simultaneousAction R
                  (TauCeti.AlgebraicGeometry.ModuliProblem.gammaNaiveAction B N))
                g).asIso.hom.base =
      x) :
  g = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/FreeAction.html#TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/FreeAction.html#TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.IsRigid.eq_one_of_comp_simultaneousAction_gammaNaiveAction_base_eq` in TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/FreeAction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/FreeAction.lean#L175)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
