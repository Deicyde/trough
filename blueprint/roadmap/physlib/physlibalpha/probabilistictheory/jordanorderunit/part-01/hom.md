---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.JordanHom, ProbabilisticTheory.JordanAlgebra.JordanHom.ext, ProbabilisticTheory.JordanAlgebra.JordanHom.map_zero, ProbabilisticTheory.JordanAlgebra.JordanHom.map_add, ProbabilisticTheory.JordanAlgebra.JordanHom.map_smul, ProbabilisticTheory.JordanAlgebra.JordanHom.map_one, ProbabilisticTheory.JordanAlgebra.JordanHom.map_mul, ProbabilisticTheory.JordanAlgebra.JordanHom.id
statement: formalized
proof: formalized
---

# Jordan homomorphisms

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Hom`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean): 15 declarations (1 instance with no name), 3 with a docstring.

> Jordan homomorphisms: unital real-linear maps between Jordan algebras preserving the product.

## i. Overview

> A Jordan homomorphism between unital real Jordan algebras is a real-linear unital map preserving the
> Jordan product.

## ii. Key results

> - `JordanAlgebra.JordanHom` : Jordan homomorphisms.
> - `JordanAlgebra.JordanHom.comp` : composition.
> - `JordanAlgebra.JordanHom.id` : the identity Jordan homomorphism.
> - `JordanAlgebra.JordanHom.comp_assoc` : composition is associative.

## iv. References

> * None.

## A. Jordan homomorphisms

**`ProbabilisticTheory.JordanAlgebra.JordanHom`**, a structure, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L56).

> A unital real-linear map preserving the Jordan product.

```lean
structure JordanHom (E F : Type*) [NonAssocCommRing E] [Module ℝ E]
    [NonAssocCommRing F] [Module ℝ F] extends E →ₗ[ℝ] F where
  map_one' : toLinearMap 1 = 1
  map_mul' : ∀ x y, toLinearMap (x * y) = toLinearMap x * toLinearMap y
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L63).

```lean
instance : CoeFun (JordanHom E F) fun _ => E → F
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.ext`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L66).

```lean
lemma ext {f g : JordanHom E F} (h : ∀ x, f x = g x) : f = g
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.map_zero`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L75).

```lean
lemma map_zero (f : JordanHom E F) : f 0 = 0
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.map_add`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L78).

```lean
lemma map_add (f : JordanHom E F) (x y : E) : f (x + y) = f x + f y
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.map_smul`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L81).

```lean
lemma map_smul (f : JordanHom E F) (r : ℝ) (x : E) : f (r • x) = r • f x
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.map_one`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L85).

```lean
lemma map_one (f : JordanHom E F) : f 1 = 1
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.map_mul`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L88).

```lean
lemma map_mul (f : JordanHom E F) (x y : E) : f (x * y) = f x * f y
```

## B. Identity and composition

**`ProbabilisticTheory.JordanAlgebra.JordanHom.id`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L98).

> The identity Jordan homomorphism.

```lean
def id : JordanHom E E
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.comp`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L104).

> Composition of unital real Jordan homomorphisms.

```lean
def comp (g : JordanHom F G) (f : JordanHom E F) : JordanHom E G
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.id_apply`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L110).

```lean
lemma id_apply (x : E) : id x = x
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.comp_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L113).

```lean
lemma comp_apply (g : JordanHom F G) (f : JordanHom E F) (x : E) :
    g.comp f x = g (f x)
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.id_comp`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L117).

```lean
lemma id_comp (f : JordanHom E F) : (id : JordanHom F F).comp f = f
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.comp_id`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L122).

```lean
lemma comp_id (f : JordanHom E F) : f.comp (id : JordanHom E E) = f
```

**`ProbabilisticTheory.JordanAlgebra.JordanHom.comp_assoc`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean#L126).

```lean
lemma comp_assoc (h : JordanHom G E) (g : JordanHom F G) (f : JordanHom E F) :
    (h.comp g).comp f = h.comp (g.comp f)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Hom.lean)
