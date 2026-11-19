---
catalog: module
lean: Polynomial.Bivariate.coeff, Polynomial.Bivariate.leadingCoeffY, Polynomial.Bivariate.natDegreeY, Polynomial.Bivariate.degreeX, Polynomial.Bivariate.totalDegree, Polynomial.Bivariate.weightedDegree, Polynomial.Bivariate.natWeightedDegree, Polynomial.Bivariate.weightedDegree_ne_none, Polynomial.Bivariate.natWeightedDegree_mem_weight_list, Polynomial.Bivariate.weight_le_natWeightedDegree_of_lt_natDegree_succ, Polynomial.Bivariate.weightedDegree_eq_natWeightedDegree, Polynomial.Bivariate.total_deg_as_weighted_deg, Polynomial.Bivariate.degreeX_as_weighted_deg, Polynomial.Bivariate.degreeY_as_weighted_deg, Polynomial.Bivariate.coeff_natDegree_le_degreeX, Polynomial.Bivariate.degreeX_mul_le, Polynomial.Bivariate.exists_max_index_degreeX, Polynomial.Bivariate.natDegree_sum_eq_of_unique, Polynomial.Bivariate.degreeX_mul_ge, Polynomial.Bivariate.degreeX_mul, Polynomial.Bivariate.evalX, Polynomial.Bivariate.evalY, Polynomial.Bivariate.evalX_eq_map, Polynomial.Bivariate.degreeX_swap, Polynomial.Bivariate.evalY_eq_evalX_swap, Polynomial.Bivariate.natDegreeY_swap, Polynomial.Bivariate.card_evalX_eq_zero_le_degreeX, Polynomial.Bivariate.descend_evalX, Polynomial.Bivariate.exists_x_preserve_natDegreeY, CompPoly.CBivariate.degreeX_toPoly, CompPoly.CBivariate.totalDegree_toPoly_spec, CompPoly.CBivariate.natWeightedDegree_toPoly
statement: formalized
proof: formalized
---

# Mathlib-Facing Bivariate Degree Helpers

`CompPoly.ToMathlib.Polynomial.BivariateDegree`, in [CompPoly/ToMathlib/Polynomial/BivariateDegree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean), by Quang Dao.

> This file collects degree- and evaluation-oriented helpers for Mathlib's bivariate
> polynomial surface `R[X][Y]` that are useful as a bridge layer between CompPoly and
> downstream developments such as ArkLib.
>
> The intended split is:
>
> - `CompPoly/Bivariate/*` for the native computable `CBivariate` representation;
> - `CompPoly/ToMathlib/*` for Mathlib-facing transport and helper lemmas.

`Polynomial.Bivariate.coeff` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L43))

> `(i, j)`-coefficient of a polynomial, i.e. the coefficient of `X^i Y^j`.

```lean
def coeff (f : F[X][Y]) (i j : ℕ) : F
```

`Polynomial.Bivariate.leadingCoeffY` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L49))

> The polynomial coefficient of the highest power of `Y`. This is the leading coefficient in the
> classical sense if the bivariate polynomial is interpreted as a univariate polynomial over `F[X]`.

```lean
def leadingCoeffY (f : F[X][Y]) : F[X]
```

`Polynomial.Bivariate.natDegreeY` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L53))

> The `Y`-degree of a bivariate polynomial, as a natural number.

```lean
def natDegreeY (f : F[X][Y]) : ℕ
```

`Polynomial.Bivariate.degreeX` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L57))

> The `X`-degree of a bivariate polynomial.

```lean
def degreeX (f : F[X][Y]) : ℕ
```

`Polynomial.Bivariate.totalDegree` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L61))

> The total degree of a bivariate polynomial.

```lean
def totalDegree (f : F[X][Y]) : ℕ
```

`Polynomial.Bivariate.weightedDegree` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L67))

> `(u, v)`-weighted degree of a polynomial.
> The maximal `u * i + v * j` such that the polynomial `p`
> contains a monomial `x^i * y^j`.

```lean
def weightedDegree (p : F[X][Y]) (u v : ℕ) : Option ℕ
```

`Polynomial.Bivariate.natWeightedDegree` (definition, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L72))

> The natural-number-valued `(u, v)`-weighted degree.

```lean
def natWeightedDegree (f : F[X][Y]) (u v : ℕ) : ℕ
```

`Polynomial.Bivariate.weightedDegree_ne_none` (lemma, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L78))

> The weighted degree is always defined (never `none`).

```lean
lemma weightedDegree_ne_none (f : F[X][Y]) (u v : ℕ) :
    weightedDegree f u v ≠ none
```

`Polynomial.Bivariate.natWeightedDegree_mem_weight_list` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L83))

```lean
theorem natWeightedDegree_mem_weight_list {u v : ℕ} :
    natWeightedDegree f u v ∈
      List.map (fun n => u * (f.coeff n).natDegree + v * n)
        (List.range f.natDegree.succ)
```

`Polynomial.Bivariate.weight_le_natWeightedDegree_of_lt_natDegree_succ` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L107))

```lean
theorem weight_le_natWeightedDegree_of_lt_natDegree_succ {u v n : ℕ}
    (hn : n < f.natDegree.succ) :
    u * (f.coeff n).natDegree + v * n ≤ natWeightedDegree f u v
```

`Polynomial.Bivariate.weightedDegree_eq_natWeightedDegree` (lemma, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L135))

```lean
lemma weightedDegree_eq_natWeightedDegree {u v : ℕ} :
    weightedDegree f u v = natWeightedDegree f u v
```

`Polynomial.Bivariate.total_deg_as_weighted_deg` (lemma, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L159))

> The total degree of a bivariate polynomial is equal to the `(1, 1)`-weighted degree.

```lean
lemma total_deg_as_weighted_deg :
    totalDegree f = natWeightedDegree f 1 1
```

`Polynomial.Bivariate.degreeX_as_weighted_deg` (lemma, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L165))

> The `X`-degree of a bivariate polynomial is equal to the `(1, 0)`-weighted degree.

```lean
lemma degreeX_as_weighted_deg :
    degreeX f = natWeightedDegree f 1 0
```

`Polynomial.Bivariate.degreeY_as_weighted_deg` (lemma, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L171))

> The `Y`-degree of a bivariate polynomial is equal to the `(0, 1)`-weighted degree.

```lean
lemma degreeY_as_weighted_deg :
    natDegreeY f = natWeightedDegree f 0 1
```

`Polynomial.Bivariate.coeff_natDegree_le_degreeX` (theorem, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L181))

```lean
theorem coeff_natDegree_le_degreeX (f : F[X][Y]) (n : ℕ) : (f.coeff n).natDegree ≤ degreeX f
```

`Polynomial.Bivariate.degreeX_mul_le` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L190))

```lean
theorem degreeX_mul_le (f g : F[X][Y]) : degreeX (f * g) ≤ degreeX f + degreeX g
```

`Polynomial.Bivariate.exists_max_index_degreeX` (theorem, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L206))

```lean
theorem exists_max_index_degreeX (f : F[X][Y]) (hf : f ≠ 0) :
    ∃ mm ∈ f.support,
      (f.coeff mm).natDegree = degreeX f ∧
      ∀ n, mm < n → (f.coeff n).natDegree < degreeX f ∨ f.coeff n = 0
```

`Polynomial.Bivariate.natDegree_sum_eq_of_unique` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L256))

```lean
theorem natDegree_sum_eq_of_unique {α : Type*} {s : Finset α} {f : α → F[X]} {deg : ℕ}
    (mx : α) (hmx : mx ∈ s) :
    (f mx).natDegree = deg →
    (∀ y ∈ s, y ≠ mx → (f y).natDegree < deg ∨ f y = 0) →
    (∑ x ∈ s, f x).natDegree = deg
```

`Polynomial.Bivariate.degreeX_mul_ge` (theorem, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L309))

```lean
theorem degreeX_mul_ge [IsDomain F] (f g : F[X][Y]) (hf : f ≠ 0) (hg : g ≠ 0) :
    degreeX f + degreeX g ≤ degreeX (f * g)
```

`Polynomial.Bivariate.degreeX_mul` (theorem, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L412))

```lean
theorem degreeX_mul [IsDomain F] (f g : F[X][Y]) (hf : f ≠ 0) (hg : g ≠ 0) :
    degreeX (f * g) = degreeX f + degreeX g
```

`Polynomial.Bivariate.evalX` (definition, [line 417](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L417))

> The evaluation at a point of a bivariate polynomial in the first variable `X`.

```lean
def evalX (a : F) (f : F[X][Y]) : Polynomial F
```

`Polynomial.Bivariate.evalY` (definition, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L421))

> The evaluation at a point of a bivariate polynomial in the second variable `Y`.

```lean
def evalY (a : F) (f : F[X][Y]) : Polynomial F
```

`Polynomial.Bivariate.evalX_eq_map` (lemma, [line 430](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L430))

```lean
lemma evalX_eq_map (x : F) (f : F[X][Y]) :
    Polynomial.Bivariate.evalX x f = f.map (Polynomial.evalRingHom x)
```

`Polynomial.Bivariate.degreeX_swap` (lemma, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L442))

```lean
lemma degreeX_swap (f : F[X][Y]) :
    Polynomial.Bivariate.degreeX (Polynomial.Bivariate.swap f) =
      Polynomial.Bivariate.natDegreeY f
```

`Polynomial.Bivariate.evalY_eq_evalX_swap` (lemma, [line 525](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L525))

```lean
lemma evalY_eq_evalX_swap (y : F) (f : F[X][Y]) :
    Polynomial.Bivariate.evalY y f =
      Polynomial.Bivariate.evalX y (Polynomial.Bivariate.swap f)
```

`Polynomial.Bivariate.natDegreeY_swap` (lemma, [line 549](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L549))

```lean
lemma natDegreeY_swap (f : F[X][Y]) :
    Polynomial.Bivariate.natDegreeY (Polynomial.Bivariate.swap f) =
      Polynomial.Bivariate.degreeX f
```

`Polynomial.Bivariate.card_evalX_eq_zero_le_degreeX` (lemma, [line 572](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L572))

```lean
lemma card_evalX_eq_zero_le_degreeX (A : F[X][Y]) (hA : A ≠ 0) (P : Finset F) :
    (P.filter (fun x => evalX x A = 0)).card ≤ degreeX A
```

`Polynomial.Bivariate.descend_evalX` (lemma, [line 594](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L594))

```lean
lemma descend_evalX {A B G A1 B1 : F[X][Y]} (hA : A = G * A1) (hB : B = G * B1)
    (x : F) (hx : evalX x G ≠ 0) (q : F[X]) (h : evalX x B = q * evalX x A) :
    evalX x B1 = q * evalX x A1
```

`Polynomial.Bivariate.exists_x_preserve_natDegreeY` (lemma, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L613))

```lean
lemma exists_x_preserve_natDegreeY (B : F[X][Y]) (hB : B ≠ 0) (P : Finset F)
    (hcard : degreeX B < P.card) :
    ∃ x ∈ P, (evalX x B).natDegree = natDegreeY B
```

`CompPoly.CBivariate.degreeX_toPoly` (theorem, [line 655](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L655))

> The computable X-degree agrees with the Mathlib-facing `degreeX` after `toPoly`.

```lean
theorem degreeX_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Ring R]
    (f : CBivariate R) :
    Polynomial.Bivariate.degreeX (toPoly f) =
      CBivariate.natDegreeX (R := R) f
```

`CompPoly.CBivariate.totalDegree_toPoly_spec` (theorem, [line 663](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L663))

> The computable total degree agrees with the Mathlib-facing total degree after `toPoly`.

```lean
theorem totalDegree_toPoly_spec {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Ring R]
    (f : CBivariate R) :
    Polynomial.Bivariate.totalDegree (toPoly f) =
      CBivariate.totalDegree (R := R) f
```

`CompPoly.CBivariate.natWeightedDegree_toPoly` (theorem, [line 670](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean#L670))

```lean
theorem natWeightedDegree_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Ring R]
    (f : CBivariate R) (u v : ℕ) :
    Polynomial.Bivariate.natWeightedDegree (toPoly f) u v =
      CBivariate.natWeightedDegree (R := R) f u v
```

## Depends on

- [Equivalence with Mathlib Bivariate Polynomials](../../bivariate/topoly.md)

## Sources

- [CompPoly/ToMathlib/Polynomial/BivariateDegree.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Polynomial/BivariateDegree.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.BivariateDegree.json)
