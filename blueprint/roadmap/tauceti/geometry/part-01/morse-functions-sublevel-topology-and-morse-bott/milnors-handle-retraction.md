---
declaration: theorem
origin: cited
lean: TauCeti.exists_inter_quadraticSublevelUnionCell_deformation
statement: formalized
proof: formalized
---

# Milnor's handle retraction

If every fibre `{v | (u, v) ∈ X}` of `X` is star-shaped about
the origin, then `X ∩ quadraticSublevelUnionCell ε` is a strong deformation retract of `X`: there
is a retraction of `X` onto it, and a homotopy in `X` from this retraction to the identity which
fixes `X ∩ quadraticSublevelUnionCell ε`. Both are restrictions of
`TauCeti.quadraticHandleRetraction ε` and `TauCeti.quadraticHandleDeformation ε`.

```lean
TauCeti.exists_inter_quadraticSublevelUnionCell_deformation.{u_1, u_2} {Eᵤ : Type u_1}
  {Eₛ : Type u_2} [NormedAddCommGroup Eᵤ] [NormedAddCommGroup Eₛ] [NormedSpace ℝ Eₛ]
  {X : Set (Eᵤ × Eₛ)} (hX : ∀ (u : Eᵤ), StarConvex ℝ 0 {v | (u, v) ∈ X}) (ε : ℝ) :
  ∃ r,
    (∀ (x : ↑(X ∩ TauCeti.quadraticSublevelUnionCell ε)), r ((ContinuousMap.inclusion ⋯) x) = x) ∧
      Nonempty
        (((ContinuousMap.inclusion ⋯).comp r).HomotopyRel (ContinuousMap.id ↑X)
          {x | ↑x ∈ TauCeti.quadraticSublevelUnionCell ε})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_inter_quadraticSublevelUnionCell_deformation`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/HandleRetraction.html#TauCeti.exists_inter_quadraticSublevelUnionCell_deformation).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_inter_quadraticSublevelUnionCell_deformation`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/HandleRetraction.html#TauCeti.exists_inter_quadraticSublevelUnionCell_deformation)
- [Source of `TauCeti.exists_inter_quadraticSublevelUnionCell_deformation` in TauCeti/Analysis/Calculus/Morse/HandleRetraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/HandleRetraction.lean#L198)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
