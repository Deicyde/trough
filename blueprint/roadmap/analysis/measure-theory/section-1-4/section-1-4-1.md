---
declaration: class
origin: cited
lean: ConcreteBooleanAlgebra, ConcreteBooleanAlgebra.instOrderTop, ConcreteBooleanAlgebra.instOrderBot, EuclideanSpace'.elementary_boolean_algebra, JordanMeasurable.boolean_algebra, LebesgueMeasurable.boolean_algebra, IsNull.boolean_algebra, ConcreteBooleanAlgebra.restrict, ConcreteBooleanAlgebra.toBooleanAlgebra, IsPartition.to_ConcreteBooleanAlgebra, DyadicCube'.partition, IsPartition.boolean_algebra_eq_iff, ConcreteBooleanAlgebra.atomic_of_finite, EuclideanSpace'.elementary_boolean_algebra_not_atomic, JordanMeasurable.boolean_algebra_not_atomic, LebesgueMeasurable.boolean_algebra_not_atomic, IsNull.boolean_algebra_not_atomic, ConcreteBooleanAlgebra.instInfSet, ConcreteBooleanAlgebra.instSupSet, ConcreteBooleanAlgebra.eq_generated_by_iff, EuclideanSpace'.elementary_boolean_algebra_generated_by_boxes, ConcreteBooleanAlgebra.generated_by_eq
statement: formalized
---

# Section 1.4.1: Boolean algebras

> A companion to (the introduction to) Section 1.4.1 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_4_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 18 labelled items, carried by 22 declarations: 22 definitions (14 with a value left as `sorry`). It also has 26 declarations with no label, counted here but not shown.

## Definition 1.4.1

`ConcreteBooleanAlgebra` (class, [line 13](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L13)). A definition.

> Definition 1.4.1

```lean
class ConcreteBooleanAlgebra (X:Type*)
```

## Example 1.4.3

`ConcreteBooleanAlgebra.instOrderTop` (instance, [line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L40)). A definition.

> Example 1.4.3 (the largest algebra)

```lean
instance ConcreteBooleanAlgebra.instOrderTop {X:Type*} : OrderTop (ConcreteBooleanAlgebra X)
```

`ConcreteBooleanAlgebra.instOrderBot` (instance, [line 52](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L52)). A definition.

> Example 1.4.3 (the smallest algebra)

```lean
instance ConcreteBooleanAlgebra.instOrderBot {X:Type*} : OrderBot (ConcreteBooleanAlgebra X)
```

## Exercise 1.4.1

`EuclideanSpace'.elementary_boolean_algebra` (def, [line 67](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L67)). A definition whose value is left as `sorry`.

> Exercise 1.4.1 (Elementary algebra)

```lean
def EuclideanSpace'.elementary_boolean_algebra (d:ℕ) : ConcreteBooleanAlgebra (EuclideanSpace' d)
```

## Example 1.4.4

`JordanMeasurable.boolean_algebra` (def, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L76)). A definition whose value is left as `sorry`.

> Example 1.4.4 (Jordan algebra)

```lean
def JordanMeasurable.boolean_algebra (d:ℕ) : ConcreteBooleanAlgebra (EuclideanSpace' d)
```

## Example 1.4.5

`LebesgueMeasurable.boolean_algebra` (def, [line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L92)). A definition.

> Example 1.4.5 (Lebesgue algebra)

```lean
def LebesgueMeasurable.boolean_algebra (d:ℕ) : ConcreteBooleanAlgebra (EuclideanSpace' d)
```

## Example 1.4.6

`IsNull.boolean_algebra` (def, [line 108](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L108)). A definition.

> Example 1.4.6 (Null algebra)

```lean
def IsNull.boolean_algebra (d:ℕ) : ConcreteBooleanAlgebra (EuclideanSpace' d)
```

## Exercise 1.4.2

`ConcreteBooleanAlgebra.restrict` (def, [line 144](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L144)). A definition.

> Exercise 1.4.2 (Restriction)

```lean
def ConcreteBooleanAlgebra.restrict {X:Type*} (B: ConcreteBooleanAlgebra X) (A:Set X) : ConcreteBooleanAlgebra A
```

## Remark 1.4.2

`ConcreteBooleanAlgebra.toBooleanAlgebra` (def, [line 159](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L159)). A definition whose value is left as `sorry`.

> Remark 1.4.2: `ConcreteBooleanAlgebra`s are `BooleanAlgebra`s

```lean
def ConcreteBooleanAlgebra.toBooleanAlgebra {X:Type*} (B: ConcreteBooleanAlgebra X) : BooleanAlgebra (B.measurableSets)
```

## Example 1.4.7

`IsPartition.to_ConcreteBooleanAlgebra` (def, [line 182](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L182)). A definition whose value is left as `sorry`.

> Example 1.4.7 (Atomic algebra)

```lean
def IsPartition.to_ConcreteBooleanAlgebra {I X: Type*} {atoms: I → Set X} (h_part: IsPartition atoms) : ConcreteBooleanAlgebra X
```

## Example 1.4.8

`DyadicCube'.partition` (def, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L234)). A definition whose value is left as `sorry`.

> Example 1.4.8

```lean
def DyadicCube'.partition (d n:ℕ) : IsPartition (fun (a: Fin d → ℤ) ↦ (DyadicCube' n a).toSet)
```

## Exercise 1.4.3

`IsPartition.boolean_algebra_eq_iff` (def, [line 246](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L246)). A definition whose value is left as `sorry`.

> Exercise 1.4.3 (Non-empty atoms of an atomic algebra determined up to relabeling)

```lean
def IsPartition.boolean_algebra_eq_iff {I J X:Type*} {parts_I: I → Set X} {parts_J: J → Set X}
  (hI: IsPartition parts_I) (hJ: IsPartition parts_J) : hI.to_ConcreteBooleanAlgebra = hJ.to_ConcreteBooleanAlgebra ↔ hI.remove_empty.relabels hJ.remove_empty
```

## Exercise 1.4.4

`ConcreteBooleanAlgebra.atomic_of_finite` (def, [line 258](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L258)). A definition whose value is left as `sorry`.

> Exercise 1.4.4 (Finite boolean algebras are atomic)

```lean
def ConcreteBooleanAlgebra.atomic_of_finite {X:Type*} (B: ConcreteBooleanAlgebra X) (h_fin: (B.measurableSets).Finite) : B.isAtomic
```

## Exercise 1.4.5

`EuclideanSpace'.elementary_boolean_algebra_not_atomic` (def, [line 264](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L264)). A definition whose value is left as `sorry`.

> Exercise 1.4.5 (elementary algebra not atomic)

```lean
def EuclideanSpace'.elementary_boolean_algebra_not_atomic (d:ℕ) (hd: d ≥ 1) : ¬ (EuclideanSpace'.elementary_boolean_algebra d).isAtomic
```

`JordanMeasurable.boolean_algebra_not_atomic` (def, [line 268](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L268)). A definition whose value is left as `sorry`.

> Exercise 1.4.5 (Jordan algebra not atomic)

```lean
def JordanMeasurable.boolean_algebra_not_atomic (d:ℕ) (hd: d ≥ 1) : ¬ (JordanMeasurable.boolean_algebra d).isAtomic
```

`LebesgueMeasurable.boolean_algebra_not_atomic` (def, [line 272](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L272)). A definition whose value is left as `sorry`.

> Exercise 1.4.5 (Lebesgue algebra not atomic)

```lean
def LebesgueMeasurable.boolean_algebra_not_atomic (d:ℕ) (hd: d ≥ 1) : ¬ (LebesgueMeasurable.boolean_algebra d).isAtomic
```

`IsNull.boolean_algebra_not_atomic` (def, [line 276](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L276)). A definition whose value is left as `sorry`.

> Exercise 1.4.5 (Null algebra not atomic)

```lean
def IsNull.boolean_algebra_not_atomic (d:ℕ) (hd: d ≥ 1) : ¬ (IsNull.boolean_algebra d).isAtomic
```

## Exercise 1.4.6

`ConcreteBooleanAlgebra.instInfSet` (instance, [line 280](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L280)). A definition.

> Exercise 1.4.6 (Intersection of algebras)

```lean
instance ConcreteBooleanAlgebra.instInfSet {X:Type*} : InfSet (ConcreteBooleanAlgebra X)
```

## Definition 1.4.10

`ConcreteBooleanAlgebra.instSupSet` (instance, [line 295](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L295)). A definition.

> Definition 1.4.10 (Generation of algebras)

```lean
instance ConcreteBooleanAlgebra.instSupSet {X:Type*} : SupSet (ConcreteBooleanAlgebra X)
```

## Example 1.4.11

`ConcreteBooleanAlgebra.eq_generated_by_iff` (instance, [line 317](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L317)). A definition whose value is left as `sorry`.

> Example 1.4.11

```lean
instance ConcreteBooleanAlgebra.eq_generated_by_iff {X:Type*} (F: Set (Set X)) : (∃ (B : ConcreteBooleanAlgebra X), B.measurableSets = F) ↔ (ConcreteBooleanAlgebra.generated_by F).measurableSets = F
```

## Exercise 1.4.7

`EuclideanSpace'.elementary_boolean_algebra_generated_by_boxes` (instance, [line 320](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L320)). A definition whose value is left as `sorry`.

> Exercise 1.4.7 (Generation by boxes)

```lean
instance EuclideanSpace'.elementary_boolean_algebra_generated_by_boxes (d:ℕ) : EuclideanSpace'.elementary_boolean_algebra d =
  ConcreteBooleanAlgebra.generated_by (Box.toSet '' Set.univ)
```

## Exercise 1.4.9

`ConcreteBooleanAlgebra.generated_by_eq` (def, [line 324](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean#L324)). A definition whose value is left as `sorry`.

> Exercise 1.4.9 (Recursive definition of generated Boolean algebra).

```lean
def ConcreteBooleanAlgebra.generated_by_eq {X:Type*} (F: Set (Set X)) :
  (ConcreteBooleanAlgebra.generated_by F).measurableSets =
  ⋃ n, Nat.rec (motive := fun _ ↦ Set (Set X)) F (fun n G ↦ { E: Set X | (∃ S: Finset G, E = ⋃ (H:S), H) ∨ (∃ S: Finset G, E = (⋃ (H:S), H)ᶜ) }) n
```

## Depends on

- [Section 1.3.5: Littlewood's three principles](../section-1-3/section-1-3-5.md)

## Sources

- [Analysis/MeasureTheory/Section_1_4_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_1.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_4_1.html)
