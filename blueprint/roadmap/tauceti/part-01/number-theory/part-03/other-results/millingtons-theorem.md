---
declaration: theorem
origin: cited
lean: TauCeti.ModularGroup.millington, TauCeti.ModularGroup.modularIsoClassEquiv
statement: formalized
proof: formalized
---

# Millington's theorem

Two modular coset triples of degree `n` are isomorphic if and only
if the subgroups are conjugate in `PSL(2, ℤ)`.

```lean
TauCeti.ModularGroup.millington {n : ℕ}
  {Γ₁ Γ₂ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ)}
  (e₁ : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ ⧸ Γ₁ ≃ Fin n)
  (e₂ : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ ⧸ Γ₂ ≃ Fin n) :
  (TauCeti.ModularGroup.modularTriple Γ₁ e₁).Equivalent (TauCeti.ModularGroup.modularTriple Γ₂ e₂) ↔
    ∃ g, g • Γ₁ = Γ₂
```

## Depends on

- [Millington's theorem for `Δ(a, b, c)` (relational form)](../../../group-theory/other-results/part-01/millingtons-theorem-for-a-b-c-relational-form.md)
- [The presentation of the modular group by its cusp generator](../../part-02/noncongruence-subgroups-of-the-modular-group-and/the-presentation-of-the-modular-group-by-its-cus.md)
- [TauCeti.ModularGroup.U](../../part-02/noncongruence-subgroups-of-the-modular-group-and/tauceti-modulargroup-u.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.millington`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Modular/CosetTriple.html#TauCeti.ModularGroup.millington).

## Other forms

**Millington's theorem (bundled bijection).** Formalized in Tau Ceti as [`TauCeti.ModularGroup.modularIsoClassEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Modular/CosetTriple.html#TauCeti.ModularGroup.modularIsoClassEquiv).

```lean
TauCeti.ModularGroup.modularIsoClassEquiv {n : ℕ} [NeZero n] :
  MulAction.orbitRel.Quotient (ConjAct (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ))
      ↥(Subgroup.ofIndex (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ) n) ≃
    ↑(TauCeti.ModularGroup.modularIsoClasses n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.millington`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Modular/CosetTriple.html#TauCeti.ModularGroup.millington)
- [Source of `TauCeti.ModularGroup.millington` in TauCeti/NumberTheory/Modular/CosetTriple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Modular/CosetTriple.lean#L353)
