---
catalog: module
lean: Cslib.Logic.Modal.Proposition.denotation, Cslib.Logic.Modal.satisfies_mem_denotation, Cslib.Logic.Modal.not_denotation, Cslib.Logic.Modal.theoryEq_denotation_eq, Cslib.Logic.Modal.Proposition.equiv_iff_denotation_eq, Cslib.Logic.Modal.Proposition.denotation_eq_of_equiv
statement: formalized
proof: formalized
---

# Denotational semantics for Modal Logic

`Cslib.Logics.Modal.Denotation`, in [Cslib/Logics/Modal/Denotation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean), by Fabrizio Montesi.

> A denotational semantics for modal logic, inspired by the one for Hennessy-Milner Logic
> (`Cslib.Logic.HML`).

`Cslib.Logic.Modal.Proposition.denotation` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L25))

> Denotation of a proposition.

```lean
def Proposition.denotation (m : Model World τ Atom) :
    Proposition τ Atom → Set World
```

`Cslib.Logic.Modal.satisfies_mem_denotation` (theorem, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L35))

> Characterisation theorem for the denotational semantics.

```lean
theorem satisfies_mem_denotation {m : Model World τ Atom} {φ : Proposition τ Atom} :
    w ∈ φ.denotation m ↔ ⇓Modal[m,w ⊨ φ]
```

`Cslib.Logic.Modal.not_denotation` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L42))

> A world is in the denotation of a proposition iff it is not in the denotation of the negation
> of the proposition.

```lean
theorem not_denotation {m : Model World τ Atom} (φ : Proposition τ Atom) :
    w ∉ (¬φ).denotation m ↔ w ∈ φ.denotation m
```

`Cslib.Logic.Modal.theoryEq_denotation_eq` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L47))

> Two worlds are theory-equivalent iff they are denotationally equivalent.

```lean
theorem theoryEq_denotation_eq {m : Model World τ Atom} {w₁ w₂ : World} :
    (TheoryEq m w₁ w₂) ↔
    (∀ (φ : Proposition τ Atom), w₁ ∈ (φ.denotation m) ↔ w₂ ∈ (φ.denotation m))
```

`Cslib.Logic.Modal.Proposition.equiv_iff_denotation_eq` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L54))

> Logically equivalent propositions under a model have the same denotation.

```lean
theorem Proposition.equiv_iff_denotation_eq :
    (φ₁ ≡[Equiv m] φ₂) ↔ φ₁.denotation m = φ₂.denotation m
```

`Cslib.Logic.Modal.Proposition.denotation_eq_of_equiv` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean#L66))

> `grind`-friendly first part of `Proposition.equiv_iff_denotation_eq`.

```lean
theorem Proposition.denotation_eq_of_equiv (h : φ₁ ≡[Equiv m] φ₂) :
    φ₁.denotation m = φ₂.denotation m
```

## Depends on

- [Logical Equivalence in Modal Logic](logicalequivalence.md)

## Sources

- [Cslib/Logics/Modal/Denotation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Denotation.lean)
