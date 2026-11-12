---
catalog: module
lean: Cslib.Logic.Modal.Proposition.Context.dynDiamond, Cslib.Logic.Modal.Proposition.unary_triangle_eq_dynDiamond, Cslib.Logic.Modal.Satisfies.dynDiamond_iff_exists, Cslib.Logic.Modal.Satisfies.dynBox_iff_forall, Cslib.Logic.Modal.Satisfies.dynBox_dynDiamond_diagonalInverse₁, Cslib.Logic.Modal.Satisfies.dynBox_dynDiamond_diagonalInverse₂, Cslib.Logic.Modal.Satisfies.unary_dual
statement: formalized
proof: formalized
---

# Unary Modal Logic

`Cslib.Logics.Modal.Unary.Basic`, in [Cslib/Logics/Modal/Unary/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean), by Fabrizio Montesi.

`Cslib.Logic.Modal.Proposition.Context.dynDiamond` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L27))

> Context constructor for the dynamic diamond modality.

```lean
def Proposition.Context.dynDiamond (c : Context τ Atom) (a : τ.A) : Context τ Atom
```

`Cslib.Logic.Modal.Proposition.unary_triangle_eq_dynDiamond` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L31))

```lean
theorem Proposition.unary_triangle_eq_dynDiamond {a : τ.A}
    (φs : PropositionMap τ a Atom) : (Δ[a]φs) = d⟨a⟩(φs default)
```

`Cslib.Logic.Modal.Satisfies.dynDiamond_iff_exists` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L37))

```lean
theorem Satisfies.dynDiamond_iff_exists {m : Model World τ Atom}
    {φ : Proposition τ Atom} : ⇓Modal[m,w ⊨ d⟨a⟩φ] ↔
      ∃ w', m.toFrame.diagonal a w w' ∧ ⇓Modal[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.dynBox_iff_forall` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L42))

```lean
theorem Satisfies.dynBox_iff_forall {m : Model World τ Atom} {φ : Proposition τ Atom} :
    ⇓Modal[m,w ⊨ d[a]φ] ↔ ∀ w', m.toFrame.diagonal a w w' → ⇓Modal[m,w' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.dynBox_dynDiamond_diagonalInverse₁` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L46))

> If two operators `op₁` and `op₂` have inverse diagonal relations, then `φ → d[op₁](d⟨op₂⟩φ)`.

```lean
theorem Satisfies.dynBox_dynDiamond_diagonalInverse₁ {m : Model World τ Atom}
    {op₁ op₂ : τ.A} [m.toFrame.DiagonalInverse op₁ op₂] {φ : Proposition τ Atom} :
    ⇓Modal[m,w ⊨ φ → d[op₁](d⟨op₂⟩φ)]
```

`Cslib.Logic.Modal.Satisfies.dynBox_dynDiamond_diagonalInverse₂` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L52))

> If two operators `op₁` and `op₂` have inverse diagonal relations, then `φ → d[op₂](d⟨op₁⟩φ)`.

```lean
theorem Satisfies.dynBox_dynDiamond_diagonalInverse₂ {m : Model World τ Atom}
    {op₁ op₂ : τ.A} [m.toFrame.DiagonalInverse op₁ op₂] {φ : Proposition τ Atom} :
    ⇓Modal[m,w ⊨ φ → d[op₂](d⟨op₁⟩φ)]
```

`Cslib.Logic.Modal.Satisfies.unary_dual` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean#L59))

> The dual axiom (reformulated for unary modal logic).

```lean
theorem Satisfies.unary_dual (f : Frame World τ) {a : τ.A} {φ : Proposition τ Atom} :
    Axiom f⇓(d⟨a⟩φ ↔ ¬d[a]¬φ)
```

## Depends on

- [Logical Equivalence in Modal Logic](../logicalequivalence.md)

## Sources

- [Cslib/Logics/Modal/Unary/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unary/Basic.lean)
