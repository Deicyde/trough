---
catalog: module
lean: Cslib.Frame, Cslib.Frame.project, Cslib.Frame.diagonal, Cslib.Frame.r_const_of_diagonal, Cslib.Frame.diagonal_of_r, Cslib.Frame.DiagonalInverse, Cslib.Frame.DiagonalSymm, Cslib.Frame.Trans, Cslib.Frame.RightEuclidean, Cslib.Frame.PreservesMap, Cslib.Frame.ofRelations, Cslib.Frame.ofRelations_iff, Cslib.Frame.ofRelations_diagonal_iff
statement: formalized
proof: formalized
---

# Modal Frames

`Cslib.Foundations.Semantics.Frame.Basic`, in [Cslib/Foundations/Semantics/Frame/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean), by Fabrizio Montesi.

> A frame is a structure of relations, each with its own arity.
>
> ## Implementation notes
>
> Frames for general modal logic were formulated with modal similarity types [Blackburn2001], which
> we generalise here to arbitrary polynomial functors.
>
> ## References
>
> * [P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*][Blackburn2001]

`Cslib.Frame` (structure, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L38))

> A frame is an indexed structure of general relations that can differ in argument positions.
>
> Frames are typically used in combination with modal logics or akin concepts. This is why we use
> `op` (for operator) to range over relation indexes.
>
> The definition generalises Definition 1.23 in [Blackburn2001] to general operator signatures given
> as `PFunctor`s and possibly-empty world types.

```lean
structure Frame (World : Type u) (τ : PFunctor) where
  /-- Accessibility relations. -/
  r : (op : τ.A) → World → (τ.B op → World) → Prop
```

`Cslib.Frame.project` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L45))

> The binary relation obtained by observing position `i` of the worlds accessible via `op`.

```lean
def project (f : Frame World τ) (op : τ.A) (i : τ.B op) : World → World → Prop
```

`Cslib.Frame.diagonal` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L51))

> The binary relation induced by restricting the accessibility relation of `op`
> to constant tuples of worlds.

```lean
def diagonal (f : Frame World τ) (op : τ.A) : World → World → Prop
```

`Cslib.Frame.r_const_of_diagonal` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L55))

```lean
theorem r_const_of_diagonal {f : Frame World τ} (h : f.diagonal op w w') :
    f.r op w (fun _ => w')
```

`Cslib.Frame.diagonal_of_r` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L59))

```lean
theorem diagonal_of_r [PFunctor.Unary τ] {f : Frame World τ} (h : f.r op w ws) :
    f.diagonal op w (ws default)
```

`Cslib.Frame.DiagonalInverse` (class, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L63))

> Two operators in a frame have inverse diagonal relations.

```lean
class DiagonalInverse (f : Frame World τ) (op₁ op₂ : τ.A) where
  diagonalInverse : ∀ w w', f.diagonal op₁ w w' ↔ f.diagonal op₂ w' w
```

`Cslib.Frame.DiagonalSymm` (class, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L71))

> A frame is diagonally symmetric at `op` if, whenever `w` accesses `ws`, some component of `ws`
> accesses the constant sequence at `w`.

```lean
class DiagonalSymm (f : Frame World τ) (op : τ.A) where
  symm w ws : f.r op w ws → ∃ i, f.r op (ws i) (fun _ => w)
```

`Cslib.Frame.Trans` (class, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L77))

> A frame is transitive at `op` if accessibility can be composed through any accessible component:
> whenever `w` accesses `ws₁` and `ws₁ i` accesses `ws₂`, then `w` accesses `ws₂`.

```lean
class Trans (f : Frame World τ) (op : τ.A) where
  trans w ws₁ i ws₂ : f.r op w ws₁ → f.r op (ws₁ i) ws₂ → f.r op w ws₂
```

`Cslib.Frame.RightEuclidean` (class, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L90))

> A frame is right Euclidean at `op` if, whenever a world `w` accesses two tuples `ws₁` and
> `ws₂`, some component of `ws₂` accesses `ws₁`.

```lean
class RightEuclidean (f : Frame World τ) (op : τ.A) where
  rightEuclidean w ws₁ ws₂ : f.r op w ws₁ → f.r op w ws₂ → ∃ i, f.r op (ws₂ i) ws₁
```

`Cslib.Frame.PreservesMap` (definition, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L96))

> A predicate map `Ps` is preserved from `P` by `op` if, whenever `P` holds at a world `w`,
> then for every tuple `ws` accessible from `w` via `op`, each component `ws i` satisfies the
> corresponding predicate `Ps i`.

```lean
def PreservesMap (f : Frame α τ) (op : τ.A) (P : α → Prop) (Ps : τ.B op → α → Prop) : Prop
```

`Cslib.Frame.ofRelations` (definition, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L100))

> Builds a unary frame from an indexed family of binary relations.

```lean
def ofRelations {τ : PFunctor} [τ.Unary] (r : τ.A → World → World → Prop) :
    Frame World τ
```

`Cslib.Frame.ofRelations_iff` (lemma, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L105))

```lean
lemma ofRelations_iff {τ : PFunctor} [τ.Unary] (r : τ.A → World → World → Prop) (i : τ.A)
    (w : World) (ws : τ.B i → World) : (ofRelations r).r i w ws ↔ r i w (ws default)
```

`Cslib.Frame.ofRelations_diagonal_iff` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean#L109))

```lean
lemma ofRelations_diagonal_iff {τ : PFunctor} [τ.Unary]
    (r : τ.A → World → World → Prop) (i : τ.A) (w w' : World) :
    (ofRelations r).diagonal i w w' ↔ r i w w'
```

## Depends on

- [Polynomial Functors](../../data/pfunctor/basic.md)

## Sources

- [Cslib/Foundations/Semantics/Frame/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/Frame/Basic.lean)
