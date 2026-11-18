---
catalog: module
lean: Language.Hom, Language.Hom.ext_iff', Language.Hom.map_nil, Language.Hom.map_append, Language.Hom.map_cons, Language.Hom.liftAux, Language.Hom.liftAux_eq_flatMap, Language.Hom.listAux_left_inv, Language.Hom.listAux_right_inv, Language.Hom.lift, Language.Hom.lift_eq_flatMap, Language.Hom.reduceOption, Language.Hom.reduceOption_apply, Language.image, Language.preimage, Language.mem_image, Language.mem_preimage, Language.image_singleton, Language.image_zero, Language.image_add, Language.image_iSup, Language.image_one, Language.image_mul, Language.image_pow, Language.image_kstar
statement: formalized
proof: formalized
---

# Language homomorphism

`Cslib.Computability.Languages.LanguageHom`, in [Cslib/Computability/Languages/LanguageHom.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean), by Ching-Tsun Chou.

`Language.Hom` (structure, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L28))

> A language homomorphism from `α` to `β` is a map from `List α` to `List β` which
> preserves the empty word `[]` and concatenation `(· ++ ·)`.

```lean
structure Hom (α β : Type*) where
  /-- The map of a language homomorphism. -/
  toFun : List α → List β
  map_nil' : toFun [] = []
  map_append' (as as' : List α) : toFun (as ++ as') = toFun as ++ toFun as'
```

`Language.Hom.ext_iff'` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L44))

```lean
theorem ext_iff' (f f' : Hom α β) :
    f = f' ↔ ∀ as, f as = f' as
```

`Language.Hom.map_nil` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L54))

```lean
theorem map_nil (f : Hom α β) : f [] = []
```

`Language.Hom.map_append` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L57))

```lean
theorem map_append (f : Hom α β) (as as' : List α) : f (as ++ as') = (f as) ++ (f as')
```

`Language.Hom.map_cons` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L61))

```lean
theorem map_cons (f : Hom α β) (a : α) (as : List α) :
    f (a :: as) = f [a] ++ f as
```

`Language.Hom.liftAux` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L67))

> This auxiliary function should not be used outside this file.
> Instead, use the equivalence `lift` below.

```lean
def liftAux (f : α → List β) : Hom α β
```

`Language.Hom.liftAux_eq_flatMap` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L72))

```lean
theorem liftAux_eq_flatMap (f : α → List β) : liftAux f = List.flatMap f
```

`Language.Hom.listAux_left_inv` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L75))

```lean
theorem listAux_left_inv (f : α → List β) :
    (fun f a ↦ f [a]) (liftAux f) = f
```

`Language.Hom.listAux_right_inv` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L79))

```lean
theorem listAux_right_inv (f : Hom α β) :
    liftAux (fun a ↦ f [a]) = f
```

`Language.Hom.lift` (definition, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L91))

> An equivalence from `f : α → List β` to `Hom α β`, whose forward direction can be
> used to define language homomorphisms conveniently.

```lean
def lift : (α → List β) ≃ (Hom α β)
```

`Language.Hom.lift_eq_flatMap` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L98))

> `lift.toFun` is in fact `List.flatMap`.

```lean
theorem lift_eq_flatMap (f : α → List β) : lift f = List.flatMap f
```

`Language.Hom.reduceOption` (definition, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L102))

> Dropping the `none`s from a list of options is a language homomorphism.

```lean
def reduceOption : Hom (Option α) α
```

`Language.Hom.reduceOption_apply` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L108))

```lean
theorem reduceOption_apply (as : List (Option α)) : reduceOption as = as.reduceOption
```

`Language.image` (definition, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L116))

> The image of a language under a function `f`, which need not be a language homomorphism.

```lean
def image (f : List α → List β) (l : Language α) : Language β
```

`Language.preimage` (definition, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L120))

> The preimage of a language under a function `f`, which need not be a language homomorphism.

```lean
def preimage (f : List α → List β) (l : Language β) : Language α
```

`Language.mem_image` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L124))

```lean
theorem mem_image (f : List α → List β) (l : Language α) (bs : List β) :
    bs ∈ l.image f ↔ ∃ as, as ∈ l ∧ f as = bs
```

`Language.mem_preimage` (theorem, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L129))

```lean
theorem mem_preimage (f : List α → List β) (l : Language β) (as : List α) :
    as ∈ l.preimage f ↔ f as ∈ l
```

`Language.image_singleton` (theorem, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L133))

```lean
theorem image_singleton (f : List α → List β) (as : List α) :
    ({as} : Language α).image f = {f as}
```

`Language.image_zero` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L138))

```lean
theorem image_zero (f : List α → List β) : (0 : Language α).image f = 0
```

`Language.image_add` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L141))

```lean
theorem image_add (f : List α → List β) (l1 l2 : Language α) :
    (l1 + l2).image f = l1.image f + l2.image f
```

`Language.image_iSup` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L145))

```lean
theorem image_iSup (f : List α → List β) {I : Type*} (l : I → Language α) :
    (⨆ i : I, l i).image f = ⨆ i : I, (l i).image f
```

> The following distributive laws for the `image` operation requires the function `f`
> to be a language homomorphism.

`Language.image_one` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L152))

```lean
theorem image_one (f : Hom α β) : (1 : Language α).image f = 1
```

`Language.image_mul` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L156))

```lean
theorem image_mul (f : Hom α β) (l1 l2 : Language α) :
    (l1 * l2).image f = l1.image f * l2.image f
```

`Language.image_pow` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L161))

```lean
theorem image_pow (f : Hom α β) (l : Language α) (n : ℕ) :
    (l^n).image f = (l.image f)^n
```

`Language.image_kstar` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean#L167))

```lean
theorem image_kstar (f : Hom α β) (l : Language α) :
    (l∗).image f = (l.image f)∗
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/LanguageHom.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/LanguageHom.lean)
