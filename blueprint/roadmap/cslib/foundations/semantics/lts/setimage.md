---
catalog: module
lean: Cslib.LTS.setImage, Cslib.LTS.setImageMultistep, Cslib.LTS.mem_setImage, Cslib.LTS.tr_setImage, Cslib.LTS.mem_setImageMultistep, Cslib.LTS.mTr_setImage, Cslib.LTS.setImage_empty, Cslib.LTS.setImageMultistep_setImage_head, Cslib.LTS.setImageMultistep_foldl_setImage, Cslib.LTS.mem_foldl_setImage, Cslib.LTS.setImage_singleton, Cslib.LTS.setImage_union, Cslib.LTS.setImage_iUnion, Cslib.LTS.setImage_mono, Cslib.LTS.setImageMultistep_nil, Cslib.LTS.setImageMultistep_empty, Cslib.LTS.setImageMultistep_singleton, Cslib.LTS.setImageMultistep_union, Cslib.LTS.setImageMultistep_iUnion, Cslib.LTS.setImageMultistep_mono, Cslib.LTS.setImageMultistep_append
statement: formalized
proof: formalized
---

# Images of sets of states

`Cslib.Foundations.Semantics.LTS.SetImage`, in [Cslib/Foundations/Semantics/LTS/SetImage.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean), by Fabrizio Montesi, Yusuf Demir.

> The image of a set of states of an `LTS` along a label and along a list of labels, with lemmas on
> membership, singletons, the empty set and the empty list, unions, monotonicity and concatenation.
>
> ## Main definitions
>
> - `LTS.setImage`: the `μ`-image of a set of states.
> - `LTS.setImageMultistep`: the `μs`-image of a set of states, for a list of labels `μs`.
>
> ## Main statements
>
> - `LTS.mem_setImage`, `LTS.mem_setImageMultistep`: membership through `Tr` and `MTr`.
> - `LTS.setImageMultistep_foldl_setImage`: the multistep image is a left fold of `setImage`.
> - `LTS.setImage_union`, `LTS.setImageMultistep_union`: images distribute over unions.
> - `LTS.setImageMultistep_append`: the image along `μs₁ ++ μs₂` is the image along `μs₂` of the
>   image along `μs₁`.

`Cslib.LTS.setImage` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L43))

> The `μ`-image of a set of states `S` is the union of all `μ`-images of the states in `S`.

```lean
def setImage (S : Set State) (μ : Label) : Set State
```

`Cslib.LTS.setImageMultistep` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L49))

> The `μs`-image of a set of states `S`, where `μs` is a list of labels, is the union of all
> `μs`-images of the states in `S`.

```lean
def setImageMultistep (S : Set State) (μs : List Label) : Set State
```

`Cslib.LTS.mem_setImage` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L54))

> Characterisation of `setImage` wrt `Tr`.

```lean
theorem mem_setImage {lts : LTS State Label} :
  s' ∈ lts.setImage S μ ↔ ∃ s ∈ S, lts.Tr s μ s'
```

`Cslib.LTS.tr_setImage` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L59))

```lean
theorem tr_setImage {lts : LTS State Label} (hs : s ∈ S) (htr : lts.Tr s μ s') :
  s' ∈ lts.setImage S μ
```

`Cslib.LTS.mem_setImageMultistep` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L64))

> Characterisation of `setImageMultistep` with `MTr`.

```lean
theorem mem_setImageMultistep {lts : LTS State Label} :
  s' ∈ lts.setImageMultistep S μs ↔ ∃ s ∈ S, lts.MTr s μs s'
```

`Cslib.LTS.mTr_setImage` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L70))

```lean
theorem mTr_setImage {lts : LTS State Label} (hs : s ∈ S) (htr : lts.MTr s μs s') :
  s' ∈ lts.setImageMultistep S μs
```

`Cslib.LTS.setImage_empty` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L75))

> The image of the empty set is always the empty set.

```lean
theorem setImage_empty (lts : LTS State Label) : lts.setImage ∅ μ = ∅
```

`Cslib.LTS.setImageMultistep_setImage_head` (lemma, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L78))

```lean
lemma setImageMultistep_setImage_head (lts : LTS State Label) :
  lts.setImageMultistep S (μ :: μs) = lts.setImageMultistep (lts.setImage S μ ) μs
```

`Cslib.LTS.setImageMultistep_foldl_setImage` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L83))

> Characterisation of `setImageMultistep` as `List.foldl` on `setImage`.

```lean
theorem setImageMultistep_foldl_setImage (lts : LTS State Label) :
  lts.setImageMultistep = List.foldl lts.setImage
```

`Cslib.LTS.mem_foldl_setImage` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L90))

> Characterisation of membership in `List.foldl lts.setImage` with `MTr`.

```lean
theorem mem_foldl_setImage (lts : LTS State Label) :
  s' ∈ List.foldl lts.setImage S μs ↔ ∃ s ∈ S, lts.MTr s μs s'
```

`Cslib.LTS.setImage_singleton` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L97))

> The image of a singleton is the image of its element.

```lean
theorem setImage_singleton (s : State) (μ : Label) : lts.setImage {s} μ = lts.image s μ
```

`Cslib.LTS.setImage_union` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L103))

> Images of sets distribute over binary unions.

```lean
theorem setImage_union (S T : Set State) (μ : Label) :
    lts.setImage (S ∪ T) μ = lts.setImage S μ ∪ lts.setImage T μ
```

`Cslib.LTS.setImage_iUnion` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L110))

> Images of sets distribute over indexed unions.

```lean
theorem setImage_iUnion {ι : Sort*} (S : ι → Set State) (μ : Label) :
    lts.setImage (⋃ i, S i) μ = ⋃ i, lts.setImage (S i) μ
```

`Cslib.LTS.setImage_mono` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L118))

> Taking the image of a set is monotone.

```lean
theorem setImage_mono {S T : Set State} (h : S ⊆ T) (μ : Label) :
    lts.setImage S μ ⊆ lts.setImage T μ
```

`Cslib.LTS.setImageMultistep_nil` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L126))

> The multistep image of a set along the empty list is the set itself.

```lean
theorem setImageMultistep_nil (S : Set State) : lts.setImageMultistep S [] = S
```

`Cslib.LTS.setImageMultistep_empty` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L132))

> The multistep image of the empty set is empty.

```lean
theorem setImageMultistep_empty (μs : List Label) : lts.setImageMultistep ∅ μs = ∅
```

`Cslib.LTS.setImageMultistep_singleton` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L138))

> The multistep image of a singleton is the multistep image of its element.

```lean
theorem setImageMultistep_singleton (s : State) (μs : List Label) :
    lts.setImageMultistep {s} μs = lts.imageMultistep s μs
```

`Cslib.LTS.setImageMultistep_union` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L145))

> Multistep images of sets distribute over binary unions.

```lean
theorem setImageMultistep_union (S T : Set State) (μs : List Label) :
    lts.setImageMultistep (S ∪ T) μs =
      lts.setImageMultistep S μs ∪ lts.setImageMultistep T μs
```

`Cslib.LTS.setImageMultistep_iUnion` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L153))

> Multistep images of sets distribute over indexed unions.

```lean
theorem setImageMultistep_iUnion {ι : Sort*} (S : ι → Set State) (μs : List Label) :
    lts.setImageMultistep (⋃ i, S i) μs = ⋃ i, lts.setImageMultistep (S i) μs
```

`Cslib.LTS.setImageMultistep_mono` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L161))

> Taking the multistep image of a set is monotone.

```lean
theorem setImageMultistep_mono {S T : Set State} (h : S ⊆ T) (μs : List Label) :
    lts.setImageMultistep S μs ⊆ lts.setImageMultistep T μs
```

`Cslib.LTS.setImageMultistep_append` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean#L170))

> The multistep image along `μs₁ ++ μs₂` is the multistep image along `μs₂` of the multistep
> image along `μs₁`.

```lean
theorem setImageMultistep_append (S : Set State) (μs₁ μs₂ : List Label) :
    lts.setImageMultistep S (μs₁ ++ μs₂) =
      lts.setImageMultistep (lts.setImageMultistep S μs₁) μs₂
```

## Depends on

- [Labelled Transition System (LTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/SetImage.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/SetImage.lean)
