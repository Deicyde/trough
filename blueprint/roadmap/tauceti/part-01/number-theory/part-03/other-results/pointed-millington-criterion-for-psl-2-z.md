---
declaration: theorem
origin: cited
lean: TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff
statement: formalized
proof: formalized
---

# Pointed Millington criterion for `PSL(2, ℤ)`

Two modular triples marked at their base
cosets `e₁ 1` and `e₂ 1` define the same marked isomorphism class if and only if `Γ₁ = Γ₂`.

```lean
TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff {n : ℕ}
  {Γ₁ Γ₂ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ)}
  (e₁ : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ ⧸ Γ₁ ≃ Fin n)
  (e₂ : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ ⧸ Γ₂ ≃ Fin n) :
  TauCeti.MarkedIsoClass.mk ⟨TauCeti.ModularGroup.modularTriple Γ₁ e₁, ⋯⟩ (e₁ ↑1) =
      TauCeti.MarkedIsoClass.mk ⟨TauCeti.ModularGroup.modularTriple Γ₂ e₂, ⋯⟩ (e₂ ↑1) ↔
    Γ₁ = Γ₂
```

## Depends on

- [TauCeti.ModularGroup.U](../../part-02/noncongruence-subgroups-of-the-modular-group-and/tauceti-modulargroup-u.md)

## Proof depends on

- [Pointed Millington criterion for `Δ(a, b, c)`](../../../group-theory/other-results/part-01/pointed-millington-criterion-for-a-b-c.md)
- [The presentation of the modular group by its cusp generator](../../part-02/noncongruence-subgroups-of-the-modular-group-and/the-presentation-of-the-modular-group-by-its-cus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Modular/CosetTriple.html#TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Modular/CosetTriple.html#TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff)
- [Source of `TauCeti.ModularGroup.markedIsoClass_modularTriple_eq_iff` in TauCeti/NumberTheory/Modular/CosetTriple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Modular/CosetTriple.lean#L364)
