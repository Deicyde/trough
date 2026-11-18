---
catalog: module
lean: Cslib.Logic.Modal.Unimodal.K, Cslib.Logic.Modal.Unimodal.T, Cslib.Logic.Modal.Unimodal.B, Cslib.Logic.Modal.Unimodal.Four, Cslib.Logic.Modal.Unimodal.Five, Cslib.Logic.Modal.Unimodal.K45, Cslib.Logic.Modal.Unimodal.D, Cslib.Logic.Modal.Unimodal.D4, Cslib.Logic.Modal.Unimodal.D5, Cslib.Logic.Modal.Unimodal.D45, Cslib.Logic.Modal.Unimodal.DB, Cslib.Logic.Modal.Unimodal.TB, Cslib.Logic.Modal.Unimodal.KB5, Cslib.Logic.Modal.Unimodal.S4, Cslib.Logic.Modal.Unimodal.S5, Cslib.Logic.Modal.Unimodal.k_subset_d, Cslib.Logic.Modal.Unimodal.k_subset_b, Cslib.Logic.Modal.Unimodal.k_subset_four, Cslib.Logic.Modal.Unimodal.k_subset_five, Cslib.Logic.Modal.Unimodal.d_subset_t, Cslib.Logic.Modal.Unimodal.k_subset_t, Cslib.Logic.Modal.Unimodal.K.k_valid, Cslib.Logic.Modal.Unimodal.T.t_valid
statement: formalized
proof: formalized
---

# Modal Logic Cube

`Cslib.Logics.Modal.Unimodal.Cube`, in [Cslib/Logics/Modal/Unimodal/Cube.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean), by Fabrizio Montesi, Marianna Girlando.

> This module formalises the Modal Cube for basic modal logic, including all the 15 foundational modal
> logics and their relationships.
>
> ## References
>
> * [P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*][Blackburn2001]

`Cslib.Logic.Modal.Unimodal.K` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L29))

> The modal logic K.

```lean
def K World Atom
```

`Cslib.Logic.Modal.Unimodal.T` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L33))

> The modal logic T.

```lean
def T World Atom
```

`Cslib.Logic.Modal.Unimodal.B` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L37))

> The modal logic B.

```lean
def B World Atom
```

`Cslib.Logic.Modal.Unimodal.Four` (definition, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L41))

> The modal logic 4.

```lean
def Four World Atom
```

`Cslib.Logic.Modal.Unimodal.Five` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L45))

> The modal logic 5.

```lean
def Five World Atom
```

`Cslib.Logic.Modal.Unimodal.K45` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L49))

> The modal logic K45.

```lean
def K45 World Atom
```

`Cslib.Logic.Modal.Unimodal.D` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L54))

> The modal logic D.

```lean
def D World Atom
```

`Cslib.Logic.Modal.Unimodal.D4` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L58))

> The modal logic D4.

```lean
def D4 World Atom
```

`Cslib.Logic.Modal.Unimodal.D5` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L63))

> The modal logic D5.

```lean
def D5 World Atom
```

`Cslib.Logic.Modal.Unimodal.D45` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L68))

> The modal logic D45.

```lean
def D45 World Atom
```

`Cslib.Logic.Modal.Unimodal.DB` (definition, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L74))

> The modal logic DB.

```lean
def DB World Atom
```

`Cslib.Logic.Modal.Unimodal.TB` (definition, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L79))

> The modal logic TB.

```lean
def TB World Atom
```

`Cslib.Logic.Modal.Unimodal.KB5` (definition, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L84))

> The modal logic KB5.

```lean
def KB5 World Atom
```

`Cslib.Logic.Modal.Unimodal.S4` (definition, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L89))

> The modal logic S4.

```lean
def S4 World Atom
```

`Cslib.Logic.Modal.Unimodal.S5` (definition, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L94))

> The modal logic S5.

```lean
def S5 World Atom
```

> ## Ordering of Modal Logics
>
> This section proves the essential inclusions of modal logics. Inclusions among compound logics
> follow by forgetting frame conditions in their defining model classes.

`Cslib.Logic.Modal.Unimodal.k_subset_d` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L109))

```lean
theorem k_subset_d : K World Atom ⊆ D World Atom
```

`Cslib.Logic.Modal.Unimodal.k_subset_b` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L112))

```lean
theorem k_subset_b : K World Atom ⊆ B World Atom
```

`Cslib.Logic.Modal.Unimodal.k_subset_four` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L115))

```lean
theorem k_subset_four : K World Atom ⊆ Four World Atom
```

`Cslib.Logic.Modal.Unimodal.k_subset_five` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L118))

```lean
theorem k_subset_five : K World Atom ⊆ Five World Atom
```

`Cslib.Logic.Modal.Unimodal.d_subset_t` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L122))

```lean
theorem d_subset_t : D World Atom ⊆ T World Atom
```

`Cslib.Logic.Modal.Unimodal.k_subset_t` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L125))

```lean
theorem k_subset_t : (K World Atom ⊆ T World Atom)
```

> ## Validity
>
> This section showcases how to prove the expected validities in the different modal logics.

`Cslib.Logic.Modal.Unimodal.K.k_valid` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L144))

> The axiom K is valid in the logic K.

```lean
theorem K.k_valid : (□(φ₁ → φ₂) → (□φ₁ → □φ₂) : Proposition Atom) ∈ K World Atom
```

`Cslib.Logic.Modal.Unimodal.T.t_valid` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean#L148))

> The axiom T is valid in the logic T.

```lean
theorem T.t_valid : (φ → ◇φ : Proposition Atom) ∈ T World Atom
```

## Depends on

- [Basic Modal Logic](basic.md)

## Proof depends on

- [Relations: Euclidean Relations](../../../foundations/relation/euclidean.md)

## Sources

- [Cslib/Logics/Modal/Unimodal/Cube.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Unimodal/Cube.lean)
