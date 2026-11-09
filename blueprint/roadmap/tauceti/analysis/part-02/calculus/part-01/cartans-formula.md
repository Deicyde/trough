---
declaration: theorem
origin: cited
lean: TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add, TauCeti.lieDerivForm_eq_curryLeft_extDeriv_add
statement: formalized
proof: formalized
---

# Cartan's formula

**Cartan's formula** within a set, `L_V ω = ι_V dω + d (ι_V ω)`, where the interior product
`ι_V` inserts `V` into the first slot.

```lean
TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {k : ℕ} {V : E → E} {s : Set E} {x : E}
  {ω : E → E [⋀^Fin (k + 1)]→L[𝕜] F} (hω : DifferentiableWithinAt 𝕜 ω s x)
  (hV : DifferentiableWithinAt 𝕜 V s x) (hs : UniqueDiffWithinAt 𝕜 s x) :
  TauCeti.lieDerivFormWithin V ω s x =
    (extDerivWithin ω s x).curryLeft (V x) + extDerivWithin (fun y => (ω y).curryLeft (V y)) s x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/LieDeriv.html#TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add).

## Other forms

**Cartan's formula.** Formalized in Tau Ceti as [`TauCeti.lieDerivForm_eq_curryLeft_extDeriv_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/LieDeriv.html#TauCeti.lieDerivForm_eq_curryLeft_extDeriv_add).

```lean
TauCeti.lieDerivForm_eq_curryLeft_extDeriv_add.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {k : ℕ} {V : E → E} {x : E}
  {ω : E → E [⋀^Fin (k + 1)]→L[𝕜] F} (hω : DifferentiableAt 𝕜 ω x) (hV : DifferentiableAt 𝕜 V x) :
  TauCeti.lieDerivForm V ω x =
    (extDeriv ω x).curryLeft (V x) + extDeriv (fun y => (ω y).curryLeft (V y)) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/LieDeriv.html#TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add)
- [Source of `TauCeti.lieDerivFormWithin_eq_curryLeft_extDerivWithin_add` in TauCeti/Analysis/Calculus/DifferentialForm/LieDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/DifferentialForm/LieDeriv.lean#L182)
