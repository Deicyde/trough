---
declaration: section
origin: cited
lean: HomologicalComplex₂.DoubleComplex, HomologicalComplex₂.DoubleComplex.equivHomologicalComplex₂, HomologicalComplex₂, HomologicalComplex₂.d_f_comp_d_f, HomologicalComplex₂.d_comm, CategoryTheory.Functor.mapBifunctorHomologicalComplex, CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_X_X, CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_d_f
statement: formalized
proof: formalized
---

# 12.18 Double complexes and associated total complexes

Section 12.18 of the Stacks Project, [Tag 0FNB](https://stacks.math.columbia.edu/tag/0FNB). 7 tags here are carried by 19 declarations of the repository (all in StacksCore) and 33 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 012Y, a definition

[Tag 012Y](https://stacks.math.columbia.edu/tag/012Y) in the Stacks Project.

**`HomologicalComplex₂.DoubleComplex`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L57). The attribute's comment: “the tag's definition, as a structure shaped like `HomologicalComplex`”. References: EGA 0 (11.2.1), “partial”; EGA 0 (11.3.1); SGA 4 XVII (0.4), “case |I| = 2”; SGA 4 XVII (0.4), “case |I| = 2”.

> **Stacks 012Y.** A double complex: a `ℤ × ℤ`-indexed family of objects with a horizontal and
> a vertical differential, such that `d₁ ∘ d₁ = 0`, `d₂ ∘ d₂ = 0` and the squares commute.

```lean
structure DoubleComplex (C : Type*) [Category* C] [HasZeroMorphisms C]
```

**`HomologicalComplex₂.DoubleComplex.equivHomologicalComplex₂`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L120). The attribute's comment: “identified with `HomologicalComplex₂ C (up ℤ) (up ℤ)` by a bijection”.

> **Stacks 012Y**, identified with Mathlib: double complexes are exactly the bicomplexes
> `HomologicalComplex₂ C (up ℤ) (up ℤ)`, over any category with zero morphisms.

```lean
def DoubleComplex.equivHomologicalComplex₂ (C : Type*) [Category* C] [HasZeroMorphisms C] :
    DoubleComplex C ≃ HomologicalComplex₂ C (up ℤ) (up ℤ)
```

Declarations registered for the tag:

- [`HomologicalComplex₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L37) (StacksCore): “any complex shapes, any category with zero morphisms; the first index is outer”. References: EGA 0 (11.2.1), “more general”; EGA 0 (11.3.1); EGA 0 (11.6.1), “more general”; EGA 0 (11.7.1).
- [`HomologicalComplex₂.d_f_comp_d_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.d_f_comp_d_f#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L39) (StacksCore): “rule (1), `d₁ ∘ d₁ = 0`; rule (2) is `d_comp_d` on each column”.
- [`HomologicalComplex₂.d_comm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.d_comm#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L41) (StacksCore): “rule (3), the squares commute; stated with its two sides swapped”. References: EGA 0 (11.3.1), “more general”.

## Tag 0A5J, an example

[Tag 0A5J](https://stacks.math.columbia.edu/tag/0A5J) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.mapBifunctorHomologicalComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapBifunctorHomologicalComplex#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Bifunctor.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/Bifunctor.lean#L28) (StacksCore): “curried `F`, zero morphisms only, any shapes, functorial in both complexes”.
- [`CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_X_X`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_X_X#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Bifunctor.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/Bifunctor.lean#L30) (StacksCore): “the term `K^{p, q} = X^p ⊗ Y^q`”.
- [`CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_d_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_d_f#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Bifunctor.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/Bifunctor.lean#L32) (StacksCore): “the first differential, induced by `d_X` and the identity of `Y^q`”.
- [`CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_X_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapBifunctorHomologicalComplex_obj_obj_X_d#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Bifunctor.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/Bifunctor.lean#L34) (StacksCore): “the second differential, induced by the identity of `X^p` and `d_Y`”.

## Tag 012Z, a definition

[Tag 012Z](https://stacks.math.columbia.edu/tag/012Z) in the Stacks Project.

**`HomologicalComplex₂.hasTotal_of_finite`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplex.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L62). The attribute's comment: “existence: finite coproducts, finitely many nonzero `A^{p, n - p}` for each `n`”.

> **Stacks 012Z**, the existence remark: `Tot(A)` exists when finite coproducts do and each
> antidiagonal `{(p, q) | π (p, q) = n}` carries only finitely many nonzero terms.

```lean
theorem hasTotal_of_finite (K : HomologicalComplex₂ C c₁ c₂) (c₁₂ : ComplexShape I₁₂)
    [TotalComplexShape c₁ c₂ c₁₂] [HasFiniteCoproducts C]
    (h : ∀ n, {pq : I₁ × I₂ | π c₁ c₂ c₁₂ pq = n ∧ ¬ IsZero ((K.X pq.1).X pq.2)}.Finite) :
    K.HasTotal c₁₂
```

**`HomologicalComplex₂.ιTotal_d_up_ℤ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplex.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L115). The attribute's comment: “the tag's formula `d₁ + (-1)^p d₂` on each summand, for `ℤ`-cochain complexes”. References: SGA 4 Vbis (2.3.2), “differential formula”; SGA 4 XVII (1.1.4), “double complex, ⊕ case”.

> **Stacks 012Z**, the differential summand-wise for a `ℤ`-cochain double complex: on the
> summand `A^{p, q}` of `Tot(A)^n` it is `d₁^{p, q} + (-1)^p d₂^{p, q}`.

```lean
theorem ιTotal_d_up_ℤ (p q n : ℤ) (h : p + q = n) :
    K.ιTotal (up ℤ) p q n h ≫ (K.total (up ℤ)).d n (n + 1) =
      (K.d p (p + 1)).f q ≫ K.ιTotal (up ℤ) (p + 1) q (n + 1) (by dsimp; lia) +
        p.negOnePow •
          ((K.X p).d q (q + 1) ≫ K.ιTotal (up ℤ) p (q + 1) (n + 1) (by dsimp; lia))
```

Declarations registered for the tag:

- [`ComplexShape.instTotalComplexShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ComplexShape.instTotalComplexShape#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ComplexShapeSigns.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ComplexShapeSigns.lean#L19) (StacksCore): “the sign convention: `π (p, q) = p + q`, `ε₁ = 1`, `ε₂ (p, q) = c.ε p`”.
- [`ComplexShape.ε_up_ℤ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ComplexShape.ε_up_ℤ#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ComplexShapeSigns.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ComplexShapeSigns.lean#L21) (StacksCore): “the tag's sign `(-1)^p`, as `(up ℤ).ε p`”.
- [`HomologicalComplex₂.total`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.total#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L40) (StacksCore): “for any shapes with a `TotalComplexShape`, over any preadditive category”. References: EGA 0 (11.3.1); EGA 0 (11.3.5).
- [`HomologicalComplex₂.HasTotal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.HasTotal#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L42) (StacksCore): “the tag's "if it exists": each `⨁_{π (p, q) = n} A^{p, q}` exists”. References: EGA 0 (11.3.1), “more general”.
- [`HomologicalComplex₂.total_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.total_d#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L44) (StacksCore): “the differential is `D₁ + D₂`”. References: EGA 0 (11.3.1), “partial”.
- [`HomologicalComplex₂.d₁_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.d₁_eq#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L45) (StacksCore): “`D₁` acts on the summand `A^{p, q}` by `ε₁ • d₁^{p, q}`”.
- [`HomologicalComplex₂.d₂_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.d₂_eq#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L47) (StacksCore): “`D₂` acts on the summand `A^{p, q}` by `ε₂ • d₂^{p, q}`”.
- [`HomologicalComplex₂.totalFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalFunctor#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplex.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplex.lean#L49) (StacksCore): “`Tot` as a functor”. References: EGA 0 (11.3.1), “partial”; EGA 0 (11.3.5).
- [`CategoryTheory.Limits.instHasCoproductsOfShapeOfHasCountableCoproductsOfCountable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.instHasCoproductsOfShapeOfHasCountableCoproductsOfCountable#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Countable.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Countable.lean#L16) (StacksCore): “Tot exists when countable coproducts do: each antidiagonal is countable”.

## Tag 08BI, a remark

[Tag 08BI](https://stacks.math.columbia.edu/tag/08BI) in the Stacks Project.

**`HomologicalComplex₃`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex.lean#L54). The attribute's comment: “the triple complex, as a complex of bicomplexes, for any three complex shapes”.

> **Stacks 08BI**, the triple complex. Given a category `C` and three complex shapes `c₁`, `c₂`
> and `c₃` on types `I₁`, `I₂` and `I₃`, a tricomplex `K : HomologicalComplex₃ C c₁ c₂ c₃` is a
> complex `K : HomologicalComplex (HomologicalComplex₂ C c₂ c₃) c₁` of bicomplexes.

```lean
abbrev HomologicalComplex₃ [HasZeroMorphisms C]
```

**`HomologicalComplex₃.int₂₃`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex.lean#L81). The attribute's comment: “`Tot₂₃`, integrating the last two indices; termwise, for any shapes”.

> Given a tricomplex `K : HomologicalComplex₃ C c₁ c₂ c₃` and a complex shape `c₂₃` with
> `TotalComplexShape c₂ c₃ c₂₃`, this is the bicomplex in `HomologicalComplex₂ C c₁ c₂₃` whose
> column indexed by `i₁` is `(K.X i₁).total c₂₃`: Stacks' `Tot₂₃(A^{•, •, •})`.

```lean
noncomputable abbrev int₂₃ [K.HasInt₂₃ c₂₃] : HomologicalComplex₂ C c₁ c₂₃
```

**`HomologicalComplex₃.int₁₂`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex.lean#L137). The attribute's comment: “`Tot₁₂`, integrating the first two indices; termwise, for any shapes”.

> Given a tricomplex `K : HomologicalComplex₃ C c₁ c₂ c₃` and a complex shape `c₁₂` with
> `TotalComplexShape c₁ c₂ c₁₂`, this is the bicomplex in `HomologicalComplex₂ C c₁₂ c₃` whose row
> indexed by `i₃` is `(K.X' i₃).total c₁₂`, the total complex of the slice at `i₃`, and whose second
> differential is induced by the third differential of `K`: Stacks' `Tot₁₂(A^{•, •, •})`.

```lean
noncomputable abbrev int₁₂ [K.HasInt₁₂ c₁₂] : HomologicalComplex₂ C c₁₂ c₃
```

**`HomologicalComplex₃.totalAssociator`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex/Associator.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex/Associator.lean#L133). The attribute's comment: “`Tot(Tot₁₂) ≅ Tot(Tot₂₃)`, the identity on every summand, under `Associative`”.

> **Stacks 08BI**: the two ways of forming the total complex of a tricomplex agree,
> `Tot(Tot₁₂(A)) ≅ Tot(Tot₂₃(A))`, by the isomorphism which is the identity on every summand.

```lean
noncomputable def totalAssociator : K.total₁₂ c₁₂ c ≅ K.total₂₃ c₂₃ c
```

**`HomologicalComplex₃.ιTotal₁₂_d_up_ℤ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex/Associator.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex/Associator.lean#L147). The attribute's comment: “the tag's `d₁ + (-1)^p d₂ + (-1)^{p + q} d₃` on `A^{p, q, r}`, over `ℤ`”.

> **Stacks 08BI**, the tag's formula for the differential of the total complex of a `ℤ`-cochain
> triple complex: on the summand `A^{p, q, r}` it is `d₁ + (-1)^p d₂ + (-1)^{p + q} d₃`.

```lean
theorem ιTotal₁₂_d_up_ℤ (p q r n : ℤ) (h : p + q + r = n) :
    A.ιTotal₁₂ (up ℤ) (up ℤ) p q r n h ≫ (A.total₁₂ (up ℤ) (up ℤ)).d n (n + 1) =
      ((A.d p (p + 1)).f q).f r ≫ A.ιTotal₁₂ (up ℤ) (up ℤ) (p + 1) q r (n + 1)
        (by
          change p + 1 + q + r = n + 1
          rw [← h, Int.add_right_comm p 1 q, Int.add_right_comm (p + q) 1 r]) +
        p.negOnePow •
          (((A.X p).d q (q + 1)).f r ≫ A.ιTotal₁₂ (up ℤ) (up ℤ) p (q + 1) r (n + 1)
            (by
              change p + (q + 1) + r = n + 1
              rw [← h, ← Int.add_assoc p q 1, Int.add_right_comm (p + q) 1 r])) +
        (p + q).negOnePow •
          (((A.X p).X q).d r (r + 1) ≫ A.ιTotal₁₂ (up ℤ) (up ℤ) p q (r + 1) (n + 1)
            (by
              change p + q + (r + 1) = n + 1
              rw [← h]; exact (Int.add_assoc (p + q) r 1).symm))
```

**`HomologicalComplex₃.total₁₂`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex/Total12.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex/Total12.lean#L51). The attribute's comment: “the tag's `Tot`, as `Tot(Tot₁₂)`; any shapes, signs from the `TotalComplexShape`s”.

> **Stacks 08BI**, the total complex of a tricomplex `K : HomologicalComplex₃ C c₁ c₂ c₃`, formed
> as the total complex of the bicomplex `K.int₁₂ c₁₂ : HomologicalComplex₂ C c₁₂ c₃`. For
> `ℤ`-cochain shapes its differential carries the tag's signs `d₁ + (-1)^p d₂ + (-1)^{p + q} d₃`,
> see `ιTotal₁₂_d_up_ℤ`, so this is the tag's `Tot(A^{•, •, •})` itself, and also its
> `Tot(Tot₁₂(A^{•, •, •}))`.

```lean
noncomputable abbrev total₁₂ : HomologicalComplex C c
```

**`HomologicalComplex₃.total₁₂_d`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex/Total12.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex/Total12.lean#L371). The attribute's comment: “the differential of `Tot` is the sum of the three signed pieces”.

> The differential of `Tot(Tot₁₂)` is `D₁ + D₂ + D₃`.

```lean
lemma total₁₂_d (j j' : J) :
    (K.total₁₂ c₁₂ c).d j j' = K.D₁ c₁₂ c j j' + K.D₂ c₁₂ c j j' + K.D₃ c₁₂ c j j'
```

**`HomologicalComplex₃.total₂₃`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalTricomplex/Total23.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalTricomplex/Total23.lean#L48). The attribute's comment: “`Tot(Tot₂₃)`; any shapes”.

> **Stacks 08BI**, `Tot(Tot₂₃(A^{•, •, •}))`: the total complex of a tricomplex
> `K : HomologicalComplex₃ C c₁ c₂ c₃` as the total complex of the bicomplex
> `K.int₂₃ c₂₃ : HomologicalComplex₂ C c₁ c₂₃`.

```lean
noncomputable abbrev total₂₃ : HomologicalComplex C c
```

Declarations registered for the tag:

- [`HomologicalComplex.mapBifunctorAssociator`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.mapBifunctorAssociator#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/BifunctorAssociator.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/BifunctorAssociator.lean#L16) (StacksCore): “the bifunctor case: `Tot(Tot(F₁₂(K₁, K₂)) ⊗ K₃) ≅ Tot(K₁ ⊗ Tot(G₂₃(K₂, K₃)))`”.
- [`ComplexShape.Associative`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ComplexShape.Associative#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ComplexShapeSigns.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ComplexShapeSigns.lean#L23) (StacksCore): “the sign compatibility under which `Tot(Tot₁₂)` and `Tot(Tot₂₃)` agree”.

## Tag 0FLG, a remark

[Tag 0FLG](https://stacks.math.columbia.edu/tag/0FLG) in the Stacks Project.

**`HomologicalComplex₂.totalShift₁₂Iso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L68). The attribute's comment: “the tag's `γ` for a general `[a, b]`, inverted to run in Mathlib's direction”.

> **Stacks 0FLG**, the inverse of the tag's `γ : Tot(A)[a + b] → Tot(A[a, b])`: the composite
> of Mathlib's `totalShift₁Iso a` on `A[0, b]` and `totalShift₂Iso b` on `A`. On the summand
> `A^{p, q}` it is `(-1)^{pb}`, the tag's sign; see `ι_totalShift₁₂Iso_hom_f`.

```lean
noncomputable def totalShift₁₂Iso :
    ((shiftFunctor₂ C y ⋙ shiftFunctor₁ C x).obj K).total (up ℤ) ≅ (K.total (up ℤ))⟦x + y⟧
```

**`HomologicalComplex₂.ι_totalShift₁₂Iso_hom_f`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L78). The attribute's comment: “the sign of `γ⁻¹`: `(-1)^{pb}` on the summand `A^{p, q}` of `Tot(A)`”.

> **Stacks 0FLG**, the sign of `γ⁻¹`: on the summand `A^{p, q}` of `Tot(A[a, b])`, which is
> the summand `A^{p + a, q + b}` of `A`, it is `(-1)^{(p + a) b}`.

```lean
lemma ι_totalShift₁₂Iso_hom_f (p q n : ℤ) (h : p + q = n) (p' : ℤ) (hp' : p' = p + x)
    (q' : ℤ) (hq' : q' = q + y) (n' : ℤ) (hn' : n' = n + (x + y)) :
    ((shiftFunctor₂ C y ⋙ shiftFunctor₁ C x).obj K).ιTotal (up ℤ) p q n h ≫
        (K.totalShift₁₂Iso x y).hom.f n =
      (p' * y).negOnePow • (((shiftFunctor₂ C y).obj K).shiftFunctor₁XXIso p x p' hp' q).hom ≫
        (K.shiftFunctor₂XXIso p' q y q' hq').hom ≫ K.ιTotal (up ℤ) p' q' n' (by dsimp; lia) ≫
          (CochainComplex.shiftFunctorObjXIso (K.total (up ℤ)) (x + y) n n' hn').inv
```

**`HomologicalComplex₂.ι_totalShift₁₂Iso_inv_f`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L99). The attribute's comment: “the tag's `γ`: `ε(p, q, a, b) = (-1)^{pb}` on the summand `A^{p, q}`”.

> **Stacks 0FLG**, the tag's `γ : Tot(A)[a + b] → Tot(A[a, b])` itself: on the summand
> `A^{p', q'}` of `Tot(A)[a + b]` it is `(-1)^{p' b}` times the identification of `A^{p', q'}` with
> the summand `(A[a, b])^{p, q}`, where `p' = p + a` and `q' = q + b`.

```lean
lemma ι_totalShift₁₂Iso_inv_f (p q n : ℤ) (h : p + q = n) (p' : ℤ) (hp' : p' = p + x)
    (q' : ℤ) (hq' : q' = q + y) (n' : ℤ) (hn' : n' = n + (x + y)) :
    K.ιTotal (up ℤ) p' q' n' (by dsimp; lia) ≫
        (CochainComplex.shiftFunctorObjXIso (K.total (up ℤ)) (x + y) n n' hn').inv ≫
          (K.totalShift₁₂Iso x y).inv.f n =
      (p' * y).negOnePow • (K.shiftFunctor₂XXIso p' q y q' hq').inv ≫
        (((shiftFunctor₂ C y).obj K).shiftFunctor₁XXIso p x p' hp' q).inv ≫
          ((shiftFunctor₂ C y ⋙ shiftFunctor₁ C x).obj K).ιTotal (up ℤ) p q n h
```

Declarations registered for the tag:

- [`HomologicalComplex₂.shiftFunctor₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.shiftFunctor₁#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L36) (StacksCore): “the shift `[a, 0]`: `A^{p + a, q}` with the sign `(-1)^a` on `d₁`”. References: SGA 4 XVII (1.1.4.2.1), “I = {1”.
- [`HomologicalComplex₂.shiftFunctor₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.shiftFunctor₂#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L38) (StacksCore): “the shift `[0, b]`: `A^{p, q + b}` with the sign `(-1)^b` on `d₂`”.
- [`HomologicalComplex₂.totalShift₁Iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₁Iso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L40) (StacksCore): “`γ⁻¹` for `[a, 0]`, without signs”.
- [`HomologicalComplex₂.totalShift₂Iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₂Iso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L41) (StacksCore): “`γ⁻¹` for `[0, b]`, the sign `(-1)^{pb}` on the summand `A^{p, q}`”.
- [`HomologicalComplex₂.totalShift₁Iso_trans_totalShift₂Iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₁Iso_trans_totalShift₂Iso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L43) (StacksCore): “combining `[a, 0]` and `[0, b]` in the other order costs the sign `(-1)^{ab}`”. References: SGA 4 XVII (1.1.4.7), “special case”.

## Tag 0G6A, a remark

[Tag 0G6A](https://stacks.math.columbia.edu/tag/0G6A) in the Stacks Project.

**`HomologicalComplex₂.totalMapHomotopy₂`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexHomotopy.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexHomotopy.lean#L283). The attribute's comment: “point 2: `Tot` of maps homotopic as complexes of rows are homotopic; any shapes”.

> **Stacks 0G6A**, second point: a homotopy between maps `f, g` of bicomplexes regarded as
> complexes of rows, i.e. between the flipped maps, induces a homotopy between `Tot(f)` and `Tot(g)`;
> on the summand `(i₁, i₂)` it is `ε₂ (i₁, c₂.prev i₂) • h.hom i₂ (c₂.prev i₂)`, which for
> `ℤ`-cochain shapes is the tag's `(-1)^p h^{p, q}` on `A^{p, q}`.

```lean
noncomputable def totalMapHomotopy₂ : Homotopy (total.map f c₁₂) (total.map g c₁₂)
```

**`HomologicalComplex₂.ιTotal_totalMapHomotopy₂_hom`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexHomotopy.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexHomotopy.lean#L292). The attribute's comment: “the tag's `h'`: `(-1)^p h^{p, q}` on the summand `A^{p, q}`, as `ε₂`”.

> The homotopy `totalMapHomotopy₂ h₂` on the summand `(i₁, i₂')`: it is the component at `i₁`
> of `h₂.hom i₂' i₂` into the summand `(i₁, i₂)`, `i₂ = c₂.prev i₂'`, up to the sign `ε₂ (i₁, i₂)`;
> for `ℤ`-cochain shapes this is Stacks 0G6A's `h'`, given by `(-1)^p h^{p, q}` on `A^{p, q}`.

```lean
lemma ιTotal_totalMapHomotopy₂_hom (i₁ : I₁) (i₂ i₂' : I₂) (j j' : I₁₂)
    (hj : ComplexShape.π c₁ c₂ c₁₂ (i₁, i₂') = j) (h' : c₂.prev i₂' = i₂) :
    K.ιTotal c₁₂ i₁ i₂' j hj ≫ (totalMapHomotopy₂ h₂ c₁₂).hom j j' =
      ComplexShape.ε₂ c₁ c₂ c₁₂ (i₁, i₂) • (h₂.hom i₂' i₂).f i₁ ≫ L.ιTotalOrZero c₁₂ i₁ i₂ j'
```

Declarations registered for the tag:

- [`HomologicalComplex.mapBifunctorMapHomotopy₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.mapBifunctorMapHomotopy₂#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/BifunctorHomotopy.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/BifunctorHomotopy.lean#L17) (StacksCore): “point 2 for the bicomplexes `F(K₁, K₂)`: a homotopy in the second variable”.
- [`HomologicalComplex₂.flip`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.flip#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L46) (StacksCore): “`DoubleComp(𝒜)` as complexes of complexes with outer index `q`: the flip”. References: EGA 0 (11.3.5).
- [`HomologicalComplex₂.shiftFunctor₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.shiftFunctor₂#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L52) (StacksCore): “point 1: the shift of `A` as a complex of rows is `[0, 1]`”.
- [`HomologicalComplex₂.totalShift₂Iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₂Iso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L54) (StacksCore): “point 1: `Tot` is compatible with the shift `[0, 1]`; the tag's `γ`, inverted”.
- [`HomologicalComplex₂.totalShift₂Iso_hom_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₂Iso_hom_naturality#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L56) (StacksCore): “point 1: the compatibility isomorphism is functorial”.

## Tag 0G6B, a remark

[Tag 0G6B](https://stacks.math.columbia.edu/tag/0G6B) in the Stacks Project.

**`HomologicalComplex₂.totalMapHomotopy₁`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexHomotopy.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexHomotopy.lean#L149). The attribute's comment: “point 2: `Tot` of homotopic maps of double complexes are homotopic; any shapes”.

> **Stacks 0G6B**, second point: a homotopy `h` between maps `f, g` of bicomplexes, regarded as
> complexes of columns, induces a homotopy between `Tot(f)` and `Tot(g)`; on the summand
> `(i₁, i₂)` it is `ε₁ (c₁.prev i₁, i₂) • h.hom i₁ (c₁.prev i₁)`, which for `ℤ`-cochain shapes is
> the tag's `h^{p, q}` on `A^{p, q}`.

```lean
noncomputable def totalMapHomotopy₁ : Homotopy (total.map f c₁₂) (total.map g c₁₂)
```

**`HomologicalComplex₂.ιTotal_totalMapHomotopy₁_hom`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/TotalComplexHomotopy.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexHomotopy.lean#L158). The attribute's comment: “the tag's `h'`: `h^{p, q}` on the summand `A^{p, q}`, times `ε₁`”.

> The homotopy `totalMapHomotopy₁ h` on the summand `(i₁', i₂)`: it is `h.hom i₁' i₁` into the
> summand `(i₁, i₂)`, `i₁ = c₁.prev i₁'`, up to the sign `ε₁ (i₁, i₂)`; for `ℤ`-cochain shapes this
> is Stacks 0G6B's `h'`, given by `h^{p, q}` on `A^{p, q}`.

```lean
lemma ιTotal_totalMapHomotopy₁_hom (i₁ i₁' : I₁) (i₂ : I₂) (j j' : I₁₂)
    (hj : ComplexShape.π c₁ c₂ c₁₂ (i₁', i₂) = j) (h' : c₁.prev i₁' = i₁) :
    K.ιTotal c₁₂ i₁' i₂ j hj ≫ (totalMapHomotopy₁ h c₁₂).hom j j' =
      ComplexShape.ε₁ c₁ c₂ c₁₂ (i₁, i₂) • (h.hom i₁' i₁).f i₂ ≫ L.ιTotalOrZero c₁₂ i₁ i₂ j'
```

Declarations registered for the tag:

- [`HomologicalComplex.mapBifunctorMapHomotopy₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.mapBifunctorMapHomotopy₁#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/BifunctorHomotopy.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/BifunctorHomotopy.lean#L15) (StacksCore): “point 2 for the bicomplexes `F(K₁, K₂)`: a homotopy in the first variable”.
- [`HomologicalComplex₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalBicomplex.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomologicalBicomplex.lean#L44) (StacksCore): “`DoubleComp(𝒜)` as complexes of complexes with outer index `p`, Mathlib's view”. References: EGA 0 (11.2.1), “more general”; EGA 0 (11.3.1); EGA 0 (11.6.1), “more general”; EGA 0 (11.7.1).
- [`HomologicalComplex₂.shiftFunctor₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.shiftFunctor₁#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L46) (StacksCore): “point 1: the shift of `A` as a complex of columns is `[1, 0]`”. References: SGA 4 XVII (1.1.4.2.1), “I = {1”.
- [`HomologicalComplex₂.totalShift₁Iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₁Iso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L48) (StacksCore): “point 1: `Tot` is compatible with the shift `[1, 0]`; the tag's `γ`, inverted”.
- [`HomologicalComplex₂.totalShift₁Iso_hom_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex₂.totalShift₁Iso_hom_naturality#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/TotalComplexShift.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/TotalComplexShift.lean#L50) (StacksCore): “point 1: the compatibility isomorphism is functorial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.18, Tag 0FNB](https://stacks.math.columbia.edu/tag/0FNB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
