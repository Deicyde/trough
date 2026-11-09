---
declaration: theorem
origin: cited
lean: Koethe.KotheConjecture, Koethe.KotherConjecture.variants.le_KotherRadical, Koethe.KotherConjecture.variants.general_matrix, Koethe.KotherConjecture.variants.two_by_two_matrix, Koethe.KotherConjecture.variants.matrixOver_KotherRadical, Koethe.KotherConjecture.variants.general_matrix_of_KotheConjecture, Koethe.KotherConjecture.variants.KotheConjecture_of_le_KotherRadical, Koethe.KotherConjecture.variants.le_KotherRadical_of_KotheConjecture, Koethe.KotherConjecture.variants.general_matrix_of_le_KotherRadical, Koethe.KotherConjecture.variants.general_matrix_of_two_by_two_matrix, Koethe.KotherConjecture.variants.general_matrix_of_matrixOver_KotherRadical, Koethe.KotherConjecture.variants.matrixOver_KotherRadical_of_general_matrix, Koethe.amitsur_conjecture
statement: formalized
---

# Köthe conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/K%C3%B6the_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Koethe.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 13 research or textbook statements: 5 open and 8 solved. It also has 1 test statement and 12 API statements, counted here but not shown.

## `Koethe.KotheConjecture`

Open: stated without proof.

> The **Köthe conjecture**: In any ring, the sum of two nil left ideals is nil.

```lean
theorem KotheConjecture (I J : Ideal R) (hI : IsNil I) (hJ : IsNil J) : IsNil (I + J)
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L115).

## `Koethe.KotherConjecture.variants.le_KotherRadical`

Open: stated without proof.

> The **Köthe conjecture**: every left nil radical is contained in the Köthe radical.

```lean
theorem KotherConjecture.variants.le_KotherRadical {I : Ideal R} (hI : IsNil I) :
    (I : Set R) ⊆ KotheRadical R
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L120).

## `Koethe.KotherConjecture.variants.general_matrix`

Open: stated without proof.

> The **Köthe conjecture**: for any nil ideal `I` of `R`, the matrix ideal `M_n(I)` is a nil ideal
> of the matrix ring `M_n(R)`.

```lean
theorem KotherConjecture.variants.general_matrix {I : TwoSidedIdeal R} (hI : IsNil I)
    (n : Type*) [Fintype n] : IsNil (matrix n I)
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L128).

## `Koethe.KotherConjecture.variants.two_by_two_matrix`

Open: stated without proof.

> The **Köthe conjecture**: for any nil ideal `I` of `R`, the matrix ideal `M_2(I)` is a nil ideal
> of the matrix ring `M_2(R)`.

```lean
theorem KotherConjecture.variants.two_by_two_matrix {I : TwoSidedIdeal R} (hI : IsNil I) :
    IsNil (matrix (Fin 2) I)
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L135).

## `Koethe.KotherConjecture.variants.matrixOver_KotherRadical`

Open: stated without proof.

> The **Köthe conjecture**: for any finite index type `n`, the Köthe radical of the matrix
> ring `M_n(R)` is the ideal `M_n(Nil*(R))` of matrices with entries in the Köthe radical of `R`.

```lean
theorem KotherConjecture.variants.matrixOver_KotherRadical (n : Type*) [Fintype n] :
    matrix n (Nil* R) = Nil* (Matrix n n R)
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L143).

## `Koethe.KotherConjecture.variants.general_matrix_of_KotheConjecture`

Proved here.

> The Köthe conjecture (for rings in universe `max u v`) implies the general matrix
> formulation for rings in universe `u` and index types in universe `v`.

```lean
theorem KotherConjecture.variants.general_matrix_of_KotheConjecture
    (h : type_of% @KotheConjecture.{max u v}) :
    type_of% @KotherConjecture.variants.general_matrix.{u, v}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 236](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L236).

## `Koethe.KotherConjecture.variants.KotheConjecture_of_le_KotherRadical`

Proved here.

> If every nil left ideal is contained in the Köthe radical, then the Köthe conjecture holds.

```lean
theorem KotherConjecture.variants.KotheConjecture_of_le_KotherRadical
    (h : type_of% @KotherConjecture.variants.le_KotherRadical.{u}) :
    type_of% @KotheConjecture.{u}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 246](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L246).

## `Koethe.KotherConjecture.variants.le_KotherRadical_of_KotheConjecture`

Proved here.

> The Köthe conjecture implies that every nil left ideal is contained in the Köthe radical.

```lean
theorem KotherConjecture.variants.le_KotherRadical_of_KotheConjecture
    (h : type_of% @KotheConjecture.{u}) :
    type_of% @KotherConjecture.variants.le_KotherRadical.{u}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 256](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L256).

## `Koethe.KotherConjecture.variants.general_matrix_of_le_KotherRadical`

Proved here.

> If every nil left ideal is contained in the Köthe radical (for rings in universe `max u v`),
> then the general matrix formulation holds.

```lean
theorem KotherConjecture.variants.general_matrix_of_le_KotherRadical
    (h : type_of% @KotherConjecture.variants.le_KotherRadical.{max u v}) :
    type_of% @KotherConjecture.variants.general_matrix.{u, v}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 283](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L283).

## `Koethe.KotherConjecture.variants.general_matrix_of_two_by_two_matrix`

Proved here.

> The `2 × 2` matrix formulation of the Köthe conjecture (for rings in universe `u`) implies
> the general matrix formulation (Krempa): one first deduces the case of `2 ^ k × 2 ^ k` matrices
> by induction and then embeds `M_n(R)` in a corner of `M_{2 ^ k}(R)`.

```lean
theorem KotherConjecture.variants.general_matrix_of_two_by_two_matrix
    (h : type_of% @KotherConjecture.variants.two_by_two_matrix.{u}) :
    type_of% @KotherConjecture.variants.general_matrix.{u, v}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 346](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L346).

## `Koethe.KotherConjecture.variants.general_matrix_of_matrixOver_KotherRadical`

Proved here.

> The formulation of the Köthe conjecture in terms of the Köthe radical of matrix rings implies
> the general matrix formulation.

```lean
theorem KotherConjecture.variants.general_matrix_of_matrixOver_KotherRadical
    (h : type_of% @KotherConjecture.variants.matrixOver_KotherRadical.{u, v}) :
    type_of% @KotherConjecture.variants.general_matrix.{u, v}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 368](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L368).

## `Koethe.KotherConjecture.variants.matrixOver_KotherRadical_of_general_matrix`

Proved here.

> The general matrix formulation of the Köthe conjecture implies the formulation in terms of
> the Köthe radical of matrix rings.

```lean
theorem KotherConjecture.variants.matrixOver_KotherRadical_of_general_matrix
    (h : type_of% @KotherConjecture.variants.general_matrix.{u, v}) :
    type_of% @KotherConjecture.variants.matrixOver_KotherRadical.{u, v}
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 380](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L380).

## `Koethe.amitsur_conjecture`

Solved: stated here without proof.

> The **Amitsur Conjecture**: If `J` is a nil ideal in `R`, then `J[x]` is a nil ideal of the polynomial ring `R[x]`.
> This is known to be false, see Agata Smoktunowicz, _Polynomial rings over nil rings need not be nil_.

```lean
theorem amitsur_conjecture : ¬ ∀ (R : Type) [Ring R] (J : TwoSidedIdeal R), IsNil J →
    IsNil (TwoSidedIdeal.map (Polynomial.C) J)
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Wikipedia/Koethe.lean, line 426](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean#L426).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Koethe.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Koethe.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/K%C3%B6the_conjecture)
