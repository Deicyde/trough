---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.toEnd_ambient_eq, PhyslibAlpha.Sl2.toEnd_ambient_pow, PhyslibAlpha.Sl2.commute_of_lie_eq_zero, PhyslibAlpha.Sl2.apply_pow_comm, PhyslibAlpha.Sl2.pow_apply_eq_zero, PhyslibAlpha.Sl2.map_mem_span_of_range, PhyslibAlpha.Sl2.prim_h, PhyslibAlpha.Sl2.prim_e
statement: formalized
proof: formalized
---

# A basis for two commuting sl₂ actions

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.BivariateBasis`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean): 60 declarations, 60 with a docstring.

> Builds a joint primitive vector and bivariate ladder basis for commuting triples.

## i. Overview

> Two commuting `sl₂` triples have a joint primitive vector: a primitive-weight space for
> the first triple is invariant under the second. Iterating the two lowering operators from
> that vector produces a grid of weight vectors. For a jointly irreducible action, these form
> a basis with explicit raising, lowering, and weight formulas.

## ii. Key results

> - `exists_joint_primitive` finds a common highest-weight vector.
> - `IsBivariateGrid` records the standard `V(n1) ⊗ V(n2)` action formulas on a grid family.
> - `exists_bivariate_basis` constructs a grid basis satisfying `IsBivariateGrid`.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Joint primitive vectors and strings

**`PhyslibAlpha.Sl2.toEnd_ambient_eq`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L52).

> Under the tautological action, `LieModule.toEnd` is the original endomorphism.

```lean
lemma toEnd_ambient_eq (x : Module.End K V) :
    LieModule.toEnd K (Module.End K V) V x = x
```

**`PhyslibAlpha.Sl2.toEnd_ambient_pow`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L58).

> Powers of the tautological action are powers of the endomorphism.

```lean
lemma toEnd_ambient_pow (x : Module.End K V) (k : ℕ) :
    LieModule.toEnd K (Module.End K V) V x ^ k = x ^ k
```

**`PhyslibAlpha.Sl2.commute_of_lie_eq_zero`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L63).

> Commuting endomorphisms have vanishing associative-ring bracket, and conversely.

```lean
lemma commute_of_lie_eq_zero {a b : Module.End K V} (h : ⁅a, b⁆ = 0) : Commute a b
```

**`PhyslibAlpha.Sl2.apply_pow_comm`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L68).

> A power of `f` commutes past an endomorphism commuting with `f`.

```lean
lemma apply_pow_comm {f y : Module.End K V} (hy : Commute f y) (a : ℕ) (v : V) :
    y ((f ^ a) v) = (f ^ a) (y v)
```

**`PhyslibAlpha.Sl2.pow_apply_eq_zero`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L73).

> Powers of an endomorphism vanish beyond the first vanishing power.

```lean
lemma pow_apply_eq_zero {f : Module.End K V} {v : V} {k : ℕ} (h : (f ^ k) v = 0) {a : ℕ}
    (ha : k ≤ a) : (f ^ a) v = 0
```

**`PhyslibAlpha.Sl2.map_mem_span_of_range`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L79).

> A linear map sending a spanning family into its span preserves the span.

```lean
lemma map_mem_span_of_range {ι : Type*} (g : ι → V) (y : Module.End K V)
    (hy : ∀ i, y (g i) ∈ Submodule.span K (Set.range g)) :
    ∀ v ∈ Submodule.span K (Set.range g), y v ∈ Submodule.span K (Set.range g)
```

**`PhyslibAlpha.Sl2.prim_h`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L90).

> A primitive vector is a `h`-eigenvector, in plain-operator form.

```lean
lemma prim_h (P : t.HasPrimitiveVectorWith m (n : K)) : h m = (n : K) • m
```

**`PhyslibAlpha.Sl2.prim_e`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L94).

> A primitive vector is killed by `e`, in plain-operator form.

```lean
lemma prim_e (P : t.HasPrimitiveVectorWith m (n : K)) : e m = 0
```

**`PhyslibAlpha.Sl2.prim_h_pow`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L98).

> The `h`-weights along a lowering string, in plain-operator form.

```lean
lemma prim_h_pow (P : t.HasPrimitiveVectorWith m (n : K)) (k : ℕ) :
    h ((f ^ k) m) = ((n : K) - 2 * k) • (f ^ k) m
```

**`PhyslibAlpha.Sl2.prim_e_pow_succ`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L103).

> The raising operator along a lowering string, in plain-operator form.

```lean
lemma prim_e_pow_succ (P : t.HasPrimitiveVectorWith m (n : K)) (k : ℕ) :
    e ((f ^ (k + 1)) m) = (((k : K) + 1) * ((n : K) - k)) • (f ^ k) m
```

**`PhyslibAlpha.Sl2.prim_f_pow_zero`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L108).

> A lowering string closes after `n + 1` steps, in plain-operator form.

```lean
lemma prim_f_pow_zero [CharZero K] [FiniteDimensional K V]
    (P : t.HasPrimitiveVectorWith m (n : K)) : (f ^ (n + 1)) m = 0
```

**`PhyslibAlpha.Sl2.prim_f_pow_ne_zero`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L113).

> The first `n + 1` lowering steps of a primitive vector are nonzero.

```lean
lemma prim_f_pow_ne_zero [CharZero K] (P : t.HasPrimitiveVectorWith m (n : K)) {k : ℕ}
    (hk : k ≤ n) : (f ^ k) m ≠ 0
```

**`PhyslibAlpha.Sl2.eq_zero_of_sub_eq_mul`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L120).

> A difference of two numbers in `[0, n]` that is a multiple of `n + 1` vanishes.

```lean
lemma eq_zero_of_sub_eq_mul {n a a' d : ℤ} (ha : 0 ≤ a ∧ a ≤ n) (ha' : 0 ≤ a' ∧ a' ≤ n)
    (h : a' - a = (n + 1) * d) : d = 0
```

**`PhyslibAlpha.Sl2.int_weight_inj`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L130).

> The integer weights `(n1 - 2a) + (n1 + 1)(n2 - 2b)` separate grid points.

```lean
lemma int_weight_inj {n1 n2 a a' b b' : ℕ} (ha : a ≤ n1) (ha' : a' ≤ n1)
    (h : (n1 : ℤ) - 2 * a + ((n1 : ℤ) + 1) * ((n2 : ℤ) - 2 * b) =
      (n1 : ℤ) - 2 * a' + ((n1 : ℤ) + 1) * ((n2 : ℤ) - 2 * b')) : a = a' ∧ b = b'
```

**`PhyslibAlpha.Sl2.weight_pair_injective`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L139).

> The combined weights `h1 + (n1 + 1) h2` separate the points of the grid.

```lean
lemma weight_pair_injective [CharZero K] {n1 n2 : ℕ} :
    Function.Injective (fun p : Fin (n1 + 1) × Fin (n2 + 1) =>
      ((n1 : K) - 2 * (p.1 : ℕ)) + ((n1 : K) + 1) * ((n2 : K) - 2 * (p.2 : ℕ)))
```

**`PhyslibAlpha.Sl2.IsBivariateGrid`**, a structure, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L153).

> A family `g` indexed by the grid `Fin (n1 + 1) × Fin (n2 + 1)` realises the standard
> `V(n1) ⊗ V(n2)` action of two commuting `sl₂`-triples: `g (a, b)` has weights
> `(n1 - 2a, n2 - 2b)`, the lowering operators shift one index, and the raising operators
> shift it back with the standard coefficients.

```lean
structure IsBivariateGrid (h1 e1 f1 h2 e2 f2 : Module.End K V) (n1 n2 : ℕ)
    (g : Fin (n1 + 1) × Fin (n2 + 1) → V) : Prop where
  /-- The first Cartan operator acts diagonally. -/
  h1_apply (a : Fin (n1 + 1)) (b : Fin (n2 + 1)) :
    h1 (g (a, b)) = ((n1 : K) - 2 * (a : ℕ)) • g (a, b)
  /-- The second Cartan operator acts diagonally. -/
  h2_apply (a : Fin (n1 + 1)) (b : Fin (n2 + 1)) :
    h2 (g (a, b)) = ((n2 : K) - 2 * (b : ℕ)) • g (a, b)
  /-- The first raising operator kills the first row. -/
  e1_zero (b : Fin (n2 + 1)) : e1 (g (0, b)) = 0
  /-- The first raising operator lowers the first index. -/
  e1_pos (a : Fin (n1 + 1)) (_ : 0 < (a : ℕ)) (b : Fin (n2 + 1)) : e1 (g (a, b)) =
    (((a : ℕ) : K) * ((n1 : K) - ((a : ℕ) : K) + 1)) • g (⟨(a : ℕ) - 1, by omega⟩, b)
  /-- The first lowering operator raises the first index. -/
  f1_lt (a : Fin (n1 + 1)) (_ : (a : ℕ) < n1) (b : Fin (n2 + 1)) :
    f1 (g (a, b)) = g (⟨(a : ℕ) + 1, by omega⟩, b)
  /-- The first lowering operator kills the last row. -/
  f1_last (b : Fin (n2 + 1)) : f1 (g (Fin.last n1, b)) = 0
  /-- The second raising operator kills the first column. -/
  e2_zero (a : Fin (n1 + 1)) : e2 (g (a, 0)) = 0
  /-- The second raising operator lowers the second index. -/
  e2_pos (a : Fin (n1 + 1)) (b : Fin (n2 + 1)) (_ : 0 < (b : ℕ)) : e2 (g (a, b)) =
    (((b : ℕ) : K) * ((n2 : K) - ((b : ℕ) : K) + 1)) • g (a, ⟨(b : ℕ) - 1, by omega⟩)
  /-- The second lowering operator raises the second index. -/
  f2_lt (a : Fin (n1 + 1)) (b : Fin (n2 + 1)) (_ : (b : ℕ) < n2) :
    f2 (g (a, b)) = g (a, ⟨(b : ℕ) + 1, by omega⟩)
  /-- The second lowering operator kills the last column. -/
  f2_last (a : Fin (n1 + 1)) : f2 (g (a, Fin.last n2)) = 0
```

**`PhyslibAlpha.Sl2.JointlyIrreducible`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L183).

> No proper nonzero subspace is invariant under all six operators of two `sl₂`-triples.

```lean
def JointlyIrreducible (h1 e1 f1 h2 e2 f2 : Module.End K V) : Prop
```

**`PhyslibAlpha.Sl2.gridVec`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L189).

> The vector `f1 ^ a (f2 ^ b m)` of the bivariate lowering grid.

```lean
def gridVec (f1 f2 : Module.End K V) (m : V) (a b : ℕ) : V
```

**`PhyslibAlpha.Sl2.gridFun`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L192).

> The bivariate lowering grid, indexed by `Fin (n1 + 1) × Fin (n2 + 1)`.

```lean
def gridFun (f1 f2 : Module.End K V) (m : V) (n1 n2 : ℕ) :
    Fin (n1 + 1) × Fin (n2 + 1) → V
```

**`PhyslibAlpha.Sl2.gridSpan`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L196).

> The span of the bivariate lowering grid.

```lean
def gridSpan (f1 f2 : Module.End K V) (m : V) (n1 n2 : ℕ) : Submodule K V
```

**`PhyslibAlpha.Sl2.grid_primitive1`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L210).

> Each lowering of the second triple is still primitive for the first triple.

```lean
lemma grid_primitive1 {b : ℕ} (hb : b ≤ n2) :
    t1.HasPrimitiveVectorWith ((f2 ^ b) m0) (n1 : K)
```

**`PhyslibAlpha.Sl2.grid_ne`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L219).

> The grid vectors inside the rectangle are nonzero.

```lean
lemma grid_ne {a b : ℕ} (ha : a ≤ n1) (hb : b ≤ n2) : gridVec f1 f2 m0 a b ≠ 0
```

**`PhyslibAlpha.Sl2.grid_h1`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L223).

> The first Cartan weight of a grid vector.

```lean
lemma grid_h1 {b : ℕ} (a : ℕ) (hb : b ≤ n2) :
    h1 (gridVec f1 f2 m0 a b) = ((n1 : K) - 2 * a) • gridVec f1 f2 m0 a b
```

**`PhyslibAlpha.Sl2.grid_h2`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L229).

> The second Cartan weight of a grid vector.

```lean
lemma grid_h2 (a b : ℕ) :
    h2 (gridVec f1 f2 m0 a b) = ((n2 : K) - 2 * b) • gridVec f1 f2 m0 a b
```

**`PhyslibAlpha.Sl2.grid_e1_zero`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L234).

> The first raising operator kills the top of each column.

```lean
lemma grid_e1_zero {b : ℕ} (hb : b ≤ n2) : e1 (gridVec f1 f2 m0 0 b) = 0
```

**`PhyslibAlpha.Sl2.grid_e1_succ`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L238).

> The first raising operator on a grid vector.

```lean
lemma grid_e1_succ {b : ℕ} (a : ℕ) (hb : b ≤ n2) :
    e1 (gridVec f1 f2 m0 (a + 1) b) =
      (((a : K) + 1) * ((n1 : K) - a)) • gridVec f1 f2 m0 a b
```

**`PhyslibAlpha.Sl2.grid_f1`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L245).

> The first lowering operator shifts the first index.

```lean
lemma grid_f1 (a b : ℕ) : f1 (gridVec f1 f2 m0 a b) = gridVec f1 f2 m0 (a + 1) b
```

**`PhyslibAlpha.Sl2.grid_f1_last`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L249).

> The first lowering operator kills the end of each column.

```lean
lemma grid_f1_last [FiniteDimensional K V] {b : ℕ} (hb : b ≤ n2) :
    f1 (gridVec f1 f2 m0 n1 b) = 0
```

**`PhyslibAlpha.Sl2.grid_e2_zero`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L256).

> The second raising operator kills the top of each row.

```lean
lemma grid_e2_zero (a : ℕ) : e2 (gridVec f1 f2 m0 a 0) = 0
```

**`PhyslibAlpha.Sl2.grid_e2_succ`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L262).

> The second raising operator on a grid vector.

```lean
lemma grid_e2_succ (a b : ℕ) :
    e2 (gridVec f1 f2 m0 a (b + 1)) =
      (((b : K) + 1) * ((n2 : K) - b)) • gridVec f1 f2 m0 a b
```

**`PhyslibAlpha.Sl2.grid_f2`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L270).

> The second lowering operator shifts the second index.

```lean
lemma grid_f2 (a b : ℕ) : f2 (gridVec f1 f2 m0 a b) = gridVec f1 f2 m0 a (b + 1)
```

**`PhyslibAlpha.Sl2.grid_f2_last`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L276).

> The second lowering operator kills the end of each row.

```lean
lemma grid_f2_last [FiniteDimensional K V] (a : ℕ) : f2 (gridVec f1 f2 m0 a n2) = 0
```

**`PhyslibAlpha.Sl2.grid_eq_zero`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L280).

> Grid vectors outside the rectangle vanish.

```lean
lemma grid_eq_zero [FiniteDimensional K V] {a b : ℕ} (h : n1 < a ∨ n2 < b) :
    gridVec f1 f2 m0 a b = 0
```

**`PhyslibAlpha.Sl2.grid_mem_gridSpan`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L289).

> Every grid vector lies in the span of the finite grid.

```lean
lemma grid_mem_gridSpan [FiniteDimensional K V] (a b : ℕ) :
    gridVec f1 f2 m0 a b ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_h1`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L300).

> The span of the grid is stable under `h1`.

```lean
lemma gridSpan_stable_h1 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, h1 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_h2`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L307).

> The span of the grid is stable under `h2`.

```lean
lemma gridSpan_stable_h2 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, h2 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_f1`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L314).

> The span of the grid is stable under `f1`.

```lean
lemma gridSpan_stable_f1 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, f1 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_f2`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L321).

> The span of the grid is stable under `f2`.

```lean
lemma gridSpan_stable_f2 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, f2 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_e1`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L328).

> The span of the grid is stable under `e1`.

```lean
lemma gridSpan_stable_e1 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, e1 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable_e2`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L340).

> The span of the grid is stable under `e2`.

```lean
lemma gridSpan_stable_e2 : ∀ v ∈ gridSpan f1 f2 m0 n1 n2, e2 v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_stable`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L351).

> The span of the grid is stable under all six generators.

```lean
lemma gridSpan_stable {x : Module.End K V} (hx : x ∈ ({h1, e1, f1, h2, e2, f2} : Set _)) :
    ∀ v ∈ gridSpan f1 f2 m0 n1 n2, x v ∈ gridSpan f1 f2 m0 n1 n2
```

**`PhyslibAlpha.Sl2.gridSpan_eq_top`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L359).

> Joint irreducibility forces the grid to span.

```lean
lemma gridSpan_eq_top (hirr : JointlyIrreducible h1 e1 f1 h2 e2 f2) :
    gridSpan f1 f2 m0 n1 n2 = ⊤
```

**`PhyslibAlpha.Sl2.top_le_span_gridFun`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L368).

> The grid spans, in the form needed to build a basis.

```lean
lemma top_le_span_gridFun (hirr : JointlyIrreducible h1 e1 f1 h2 e2 f2) :
    ⊤ ≤ Submodule.span K (Set.range (gridFun f1 f2 m0 n1 n2))
```

**`PhyslibAlpha.Sl2.grid_hasEigenvector`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L375).

> The combined Cartan operator has the grid vectors as eigenvectors.

```lean
lemma grid_hasEigenvector (p : Fin (n1 + 1) × Fin (n2 + 1)) :
    (h1 + ((n1 : K) + 1) • h2).HasEigenvector
      (((n1 : K) - 2 * (p.1 : ℕ)) + ((n1 : K) + 1) * ((n2 : K) - 2 * (p.2 : ℕ)))
      (gridFun f1 f2 m0 n1 n2 p)
```

**`PhyslibAlpha.Sl2.grid_linearIndependent`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L388).

> The bivariate grid is linearly independent.

```lean
lemma grid_linearIndependent : LinearIndependent K (gridFun f1 f2 m0 n1 n2)
```

**`PhyslibAlpha.Sl2.grid_e1_pos`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L394).

> The first raising operator on a grid vector, for a positive index.

```lean
lemma grid_e1_pos (a : Fin (n1 + 1)) (ha : 0 < (a : ℕ)) {b : ℕ} (hb : b ≤ n2) :
    e1 (gridVec f1 f2 m0 a b) = (((a : ℕ) : K) * ((n1 : K) - ((a : ℕ) : K) + 1)) •
      gridVec f1 f2 m0 ((a : ℕ) - 1) b
```

**`PhyslibAlpha.Sl2.grid_e2_pos`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L405).

> The second raising operator on a grid vector, for a positive index.

```lean
lemma grid_e2_pos (a : ℕ) (b : Fin (n2 + 1)) (hb : 0 < (b : ℕ)) :
    e2 (gridVec f1 f2 m0 a b) = (((b : ℕ) : K) * ((n2 : K) - ((b : ℕ) : K) + 1)) •
      gridVec f1 f2 m0 a ((b : ℕ) - 1)
```

**`PhyslibAlpha.Sl2.gridFun_isBivariateGrid`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L415).

> The grid realises the standard bivariate action.

```lean
lemma gridFun_isBivariateGrid :
    IsBivariateGrid h1 e1 f1 h2 e2 f2 n1 n2 (gridFun f1 f2 m0 n1 n2)
```

**`PhyslibAlpha.Sl2.primSpace`**, a def, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L432).

> The first-triple primitive vectors of weight `n`: vectors killed by `e` with `h`-weight `n`.

```lean
def primSpace (h e : Module.End K V) (n : K) : Submodule K V
```

**`PhyslibAlpha.Sl2.mem_primSpace`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L436).

> Membership in `primSpace`, in plain-operator form.

```lean
lemma mem_primSpace {h e : Module.End K V} {n : K} {v : V} :
    v ∈ primSpace h e n ↔ e v = 0 ∧ h v = n • v
```

**`PhyslibAlpha.Sl2.primSpace_map_mem`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L441).

> An endomorphism commuting with `e` and `h` preserves `primSpace`.

```lean
lemma primSpace_map_mem {h e y : Module.End K V} {n : K} {v : V} (hey : Commute e y)
    (hhy : Commute h y) (hv : v ∈ primSpace h e n) : y v ∈ primSpace h e n
```

**`PhyslibAlpha.Sl2.hasPrimitiveVectorWith_of_mem_primSpace`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L450).

> A vector of `primSpace` that is nonzero is primitive.

```lean
lemma hasPrimitiveVectorWith_of_mem_primSpace {h e f : Module.End K V} {t : IsSl2Triple h e f}
    {n : K} {w : V} (hw : w ∈ primSpace h e n) (hne : w ≠ 0) : t.HasPrimitiveVectorWith w n
```

**`PhyslibAlpha.Sl2.commute_of_hcomm`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L455).

> Commuting triples give commuting operators.

```lean
lemma commute_of_hcomm {h1 e1 f1 h2 e2 f2 : Module.End K V}
    (hcomm : ∀ x ∈ ({h1, e1, f1} : Set (Module.End K V)),
      ∀ y ∈ ({h2, e2, f2} : Set (Module.End K V)), ⁅x, y⁆ = 0) :
    ∀ x ∈ ({h1, e1, f1} : Set (Module.End K V)),
      ∀ y ∈ ({h2, e2, f2} : Set (Module.End K V)), Commute x y
```

**`PhyslibAlpha.Sl2.nontrivial_of_isSl2Triple`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L463).

> The representation space of a nonzero `sl₂`-triple is nontrivial.

```lean
lemma nontrivial_of_isSl2Triple {h e f : Module.End K V} (t : IsSl2Triple h e f) :
    Nontrivial V
```

**`PhyslibAlpha.Sl2.lie_mem_of_generators`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L470).

> A subspace stable under the generators is stable under the generated subalgebra.

```lean
lemma lie_mem_of_generators {h e f : Module.End K V} (t : IsSl2Triple h e f) (W : Submodule K V)
    (hh : ∀ v ∈ W, h v ∈ W) (he : ∀ v ∈ W, e v ∈ W) (hf : ∀ v ∈ W, f v ∈ W)
    (x : ↥(t.toLieSubalgebra (R := K))) {v : V} (hv : v ∈ W) : ⁅(x : Module.End K V), v⁆ ∈ W
```

**`PhyslibAlpha.Sl2.hasPrimitiveVectorWith_of_sub`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L480).

> A primitive vector of the induced triple on a Lie submodule is primitive in `V`.

```lean
lemma hasPrimitiveVectorWith_of_sub {h e f : Module.End K V} {t : IsSl2Triple h e f}
    {N : LieSubmodule K ↥(t.toLieSubalgebra (R := K)) V} {w : N} {n : K}
    (P : (isSl2Triple_sub (K := K) t).HasPrimitiveVectorWith w n) :
    t.HasPrimitiveVectorWith (w : V) n
```

**`PhyslibAlpha.Sl2.exists_primitive_in_invariant`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L497).

> A nonzero subspace stable under the generators contains a primitive vector.

```lean
lemma exists_primitive_in_invariant {h e f : Module.End K V} (t : IsSl2Triple h e f)
    (W : Submodule K V) (hW : W ≠ ⊥) (hh : ∀ v ∈ W, h v ∈ W) (he : ∀ v ∈ W, e v ∈ W)
    (hf : ∀ v ∈ W, f v ∈ W) : ∃ (n : ℕ) (w : V), w ∈ W ∧ t.HasPrimitiveVectorWith w (n : K)
```

**`PhyslibAlpha.Sl2.primSpace_stable`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L521).

> The primitive space of the first triple is stable under every operator of the second.

```lean
lemma primSpace_stable {n : K} {y : Module.End K V} {v : V}
    (hc : ∀ x ∈ ({h1, e1, f1} : Set (Module.End K V)),
      ∀ y ∈ ({h2, e2, f2} : Set (Module.End K V)), Commute x y)
    (hy : y ∈ ({h2, e2, f2} : Set (Module.End K V))) (hv : v ∈ primSpace h1 e1 n) :
    y v ∈ primSpace h1 e1 n
```

**`PhyslibAlpha.Sl2.exists_joint_primitive`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L532).

> Two commuting triples have a common primitive vector. The primitive-weight space for
> the first triple is invariant under the second, so a primitive vector for the second can be
> chosen inside it.

```lean
lemma exists_joint_primitive : ∃ (n1 n2 : ℕ) (m0 : V), m0 ≠ 0 ∧
    t1.HasPrimitiveVectorWith m0 (n1 : K) ∧ t2.HasPrimitiveVectorWith m0 (n2 : K)
```

**`PhyslibAlpha.Sl2.exists_bivariate_basis`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean#L548).

> For a jointly irreducible pair of commuting triples, the vectors `f1 ^ a (f2 ^ b m0)`
> form a basis. The basis realises the standard bivariate action, including the endpoints of
> each string.

```lean
lemma exists_bivariate_basis :
    ∃ (n1 n2 : ℕ) (B : Module.Basis (Fin (n1 + 1) × Fin (n2 + 1)) K V),
      IsBivariateGrid h1 e1 f1 h2 e2 f2 n1 n2 B
```

## Depends on

- [The standard sl₂ Lie module](sl2-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/BivariateBasis.lean)
