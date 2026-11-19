---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_eq_quadRepBilin_apply, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.quadRepPolar_eq_two_smul_jordanTriple, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_outer_comm, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_diag, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_add_left, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_smul_left, PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_add_right
statement: formalized
proof: formalized
---

# The Jordan triple product

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Quadratic.Triple`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean): 11 declarations, 11 with a docstring.

> The Jordan triple product `{a, b, c}`: symmetry, linearity and the diagonal `{a, b, a} = U_a b`.

## i. Overview

> The Jordan triple product `{a, b, c} = a ∘ (b ∘ c) + c ∘ (b ∘ a) - (a ∘ c) ∘ b` is the polarization
> of the quadratic representation: `{a, b, a} = U_a b`.

## ii. Key results

> - `JordanAlgebra.jordanTriple` : the triple product.
> - `JordanAlgebra.jordanTriple_diag` : `{a, b, a} = U_a b`.

## iv. References

> * None.

## A. The triple product

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L50).

> The Jordan triple product, written directly to retain a computable algebraic definition.

```lean
def jordanTriple (a b c : E) : E
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_eq_quadRepBilin_apply`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L55).

> The triple product is precisely the action of the canonical bilinear quadratic operator on
> its middle variable.  Thus no second bundled triple-operator API is needed: `quadRepBilin a c`
> is already the operator `b ↦ {a,b,c}`.

```lean
lemma jordanTriple_eq_quadRepBilin_apply (a b c : E) :
    jordanTriple a b c = quadRepBilin a c b
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.quadRepPolar_eq_two_smul_jordanTriple`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L61).

> The existing quadratic polarization is exactly twice the Jordan triple product.

```lean
lemma quadRepPolar_eq_two_smul_jordanTriple (a b c : E) :
    quadRepPolar a c b = (2 : ℝ) • jordanTriple a b c
```

## B. Symmetry, diagonal and linearity

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_outer_comm`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L69).

> The Jordan triple product is symmetric in its outer variables.

```lean
lemma jordanTriple_outer_comm (a b c : E) : jordanTriple a b c = jordanTriple c b a
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_diag`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L74).

> The diagonal of the triple product is the quadratic representation.

```lean
lemma jordanTriple_diag (a b : E) : jordanTriple a b a = U a b
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_add_left`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L81).

> Additivity in the first outer variable.

```lean
lemma jordanTriple_add_left (a b c d : E) :
    jordanTriple (a + b) c d = jordanTriple a c d + jordanTriple b c d
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_smul_left`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L88).

> Real linearity in the first outer variable.

```lean
lemma jordanTriple_smul_left (r : ℝ) (a b c : E) :
    jordanTriple (r • a) b c = r • jordanTriple a b c
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_add_right`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L102).

> Additivity in the third outer variable.

```lean
lemma jordanTriple_add_right (a b c d : E) :
    jordanTriple a b (c + d) = jordanTriple a b c + jordanTriple a b d
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_smul_right`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L108).

> Real linearity in the third outer variable.

```lean
lemma jordanTriple_smul_right (r : ℝ) (a b c : E) :
    jordanTriple a b (r • c) = r • jordanTriple a b c
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_add_middle`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L117).

> Additivity in the middle variable.

```lean
lemma jordanTriple_add_middle (a b c d : E) :
    jordanTriple a (b + c) d = jordanTriple a b d + jordanTriple a c d
```

**`PhyslibAlpha.ProbabilisticTheory.JordanAlgebra.jordanTriple_smul_middle`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean#L124).

> Real linearity in the middle variable.

```lean
lemma jordanTriple_smul_middle (r : ℝ) (a b c : E) :
    jordanTriple a (r • b) c = r • jordanTriple a b c
```

## Depends on

- [Powers, multiplication operators and the quadratic representation](../part-01/operator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Triple.lean)
